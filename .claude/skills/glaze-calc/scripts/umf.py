#!/usr/bin/env python3
"""Convert a glaze recipe (materials by weight) into a Unity Molecular Formula.

Usage:
  python3 umf.py G2926B                  # a built-in base recipe code
  python3 umf.py recipe.json             # a recipe JSON file
  python3 umf.py -                       # recipe JSON on stdin
  python3 umf.py G2926B --add "Titanium Dioxide=4,Black Iron Oxide=2"

Recipe JSON shape:
  {"name": "...",
   "materials": {"Nepheline Syenite": 18.3, "Ferro Frit 3134": 25.4, ...},
   "additions": {"Titanium Dioxide": 4}}     # optional, added on top

Output: UMF grouped as fluxes (unity = 1.0) / stabilizers (R2O3) /
glass-formers (RO2) / colorants, plus SiO2:Al2O3 and R2O:RO ratios.
"""
import argparse
import sys

import glazelib as g

FLUX = {"flux_r2o", "flux_ro"}
GROUP_ORDER = [
    ("Fluxes (RO/R2O, unity = 1.0)", ("flux_r2o", "flux_ro")),
    ("Stabilizers (R2O3)", ("stabilizer",)),
    ("Glass-formers (RO2)", ("glass_former",)),
    ("Colorants / opacifiers / other", ("colorant", "opacifier", "other")),
]


def parse_add(spec):
    out = {}
    if not spec:
        return out
    for part in spec.split(","):
        if "=" in part:
            k, v = part.split("=", 1)
            out[k.strip()] = float(v)
    return out


def main():
    ap = argparse.ArgumentParser(description="Recipe -> Unity Molecular Formula")
    ap.add_argument("recipe", help="base-recipe code, JSON file path, or - for stdin")
    ap.add_argument("--add", help='additions, e.g. "Titanium Dioxide=4,Rutile=2"')
    args = ap.parse_args()

    oxides = g.load_oxides()
    materials = g.load_materials()
    recipe = g.load_recipe(args.recipe)
    if args.add:
        adds = recipe.setdefault("additions", {})
        for k, v in parse_add(args.add).items():
            adds[k] = adds.get(k, 0.0) + v

    oxide_g, oxide_mol, unknown = g.recipe_to_oxides(recipe, materials, oxides)
    if unknown:
        sys.exit("ERROR: unknown material/oxide(s): " + ", ".join(unknown) +
                 "\nCheck spelling or add them to data/materials.json.")
    if not oxide_mol:
        sys.exit("ERROR: no oxides produced from this recipe.")

    flux_total = sum(m for ox, m in oxide_mol.items() if oxides[ox]["role"] in FLUX)
    if flux_total <= 0:
        sys.exit("ERROR: no flux oxides; cannot compute unity formula.")
    umf = {ox: m / flux_total for ox, m in oxide_mol.items()}

    name = recipe.get("name", args.recipe)
    print("=" * 60)
    print("UMF  -  " + str(name))
    if recipe.get("additions"):
        print("additions: " + ", ".join(f"+{v}% {k}" for k, v in recipe["additions"].items()))
    print("=" * 60)

    for title, roles in GROUP_ORDER:
        rows = sorted((ox for ox in umf if oxides[ox]["role"] in roles),
                      key=lambda o: -umf[o])
        if not rows:
            continue
        print("\n" + title)
        for ox in rows:
            print(f"  {ox:<6} {umf[ox]:7.3f}")

    sio2 = umf.get("SiO2", 0.0)
    al2o3 = umf.get("Al2O3", 0.0)
    r2o = sum(m for ox, m in umf.items() if oxides[ox]["role"] == "flux_r2o")
    ro = sum(m for ox, m in umf.items() if oxides[ox]["role"] == "flux_ro")
    print("\n" + "-" * 60)
    if al2o3 > 0:
        print(f"  SiO2 : Al2O3   = {sio2 / al2o3:5.2f} : 1   "
              "(cone-6 glossy typically ~7-10:1)")
    print(f"  R2O : RO flux  = {r2o:4.2f} : {ro:4.2f}")
    b2o3 = umf.get("B2O3", 0.0)
    if b2o3:
        print(f"  B2O3 (flux-acting stabilizer) = {b2o3:.3f}")
    print(f"  Total batch weight charged = "
          f"{sum(g.combined_batch(recipe).values()):.1f}")
    print("-" * 60)
    print("Note: UMF describes the FIRED glass (mole ratios), not the batch.")


if __name__ == "__main__":
    main()
