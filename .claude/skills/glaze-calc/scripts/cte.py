#!/usr/bin/env python3
"""Estimate a glaze's coefficient of thermal expansion (CTE) and check fit.

Method (the same idea Insight / Glazy use): convert the recipe to oxide moles,
take each oxide's MOLE FRACTION of the whole, multiply by that oxide's published
linear-expansion factor, and sum. The per-oxide breakdown is printed so the math
is legible.

CTE_glaze = sum( mole_fraction_i * factor_i )   [factors are x10^-7/degC]

Usage:
  python3 cte.py G2926B
  python3 cte.py recipe.json --body 6.8
  python3 cte.py G2926B --add "Lithium Carbonate=3"

--body is your CLAY BODY'S measured CTE in x10^-6/degC (default 6.8, a typical
cone-6 porcelain placeholder - measure or get your real value; body expansion
CANNOT be reliably calculated).

IMPORTANT: absolute CTE values are factor-set dependent. Use this to compare
recipes and to see the DIRECTION an addition pushes expansion, not as an
absolute truth. Always confirm fit empirically (test tiles, the ice-water /
boiling test for crazing).
"""
import argparse
import sys

import glazelib as g

DEFAULT_BODY = 6.8  # x10^-6/degC, typical cone-6 porcelain placeholder


def parse_add(spec):
    out = {}
    for part in (spec or "").split(","):
        if "=" in part:
            k, v = part.split("=", 1)
            out[k.strip()] = float(v)
    return out


def main():
    ap = argparse.ArgumentParser(description="Glaze CTE estimate + body-fit check")
    ap.add_argument("recipe", help="base-recipe code, JSON file path, or - for stdin")
    ap.add_argument("--add", help='additions, e.g. "Lithium Carbonate=3"')
    ap.add_argument("--body", type=float, default=DEFAULT_BODY,
                    help="clay body CTE in x10^-6/degC (default %(default)s)")
    args = ap.parse_args()

    oxides = g.load_oxides()
    materials = g.load_materials()
    recipe = g.load_recipe(args.recipe)
    if args.add:
        adds = recipe.setdefault("additions", {})
        for k, v in parse_add(args.add).items():
            adds[k] = adds.get(k, 0.0) + v

    _, oxide_mol, unknown = g.recipe_to_oxides(recipe, materials, oxides)
    if unknown:
        sys.exit("ERROR: unknown material/oxide(s): " + ", ".join(unknown))
    total_mol = sum(oxide_mol.values())
    if total_mol <= 0:
        sys.exit("ERROR: no oxides produced from this recipe.")

    rows = []
    cte_e7 = 0.0
    for ox, mol in oxide_mol.items():
        frac = mol / total_mol
        factor = oxides[ox]["cte_factor"]
        contrib = frac * factor
        cte_e7 += contrib
        rows.append((ox, frac, factor, contrib))
    rows.sort(key=lambda r: -r[3])

    glaze_cte = cte_e7 / 10.0  # x10^-7 -> x10^-6

    name = recipe.get("name", args.recipe)
    print("=" * 64)
    print("Thermal expansion (CTE)  -  " + str(name))
    if recipe.get("additions"):
        print("additions: " + ", ".join(f"+{v}% {k}" for k, v in recipe["additions"].items()))
    print("=" * 64)
    print(f"{'oxide':<6}{'mole%':>9}{'factor':>9}{'contrib(e-7)':>14}{'% of CTE':>10}")
    for ox, frac, factor, contrib in rows:
        print(f"{ox:<6}{frac * 100:>8.2f}%{factor:>9.0f}{contrib:>14.2f}"
              f"{contrib / cte_e7 * 100:>9.1f}%")
    print("-" * 64)
    print(f"Glaze CTE  = {glaze_cte:.2f} x10^-6 /degC   "
          f"({cte_e7:.1f} x10^-7)")
    print(f"Body CTE   = {args.body:.2f} x10^-6 /degC   (your input)")

    diff = glaze_cte - args.body
    print(f"Difference = {diff:+.2f} x10^-6  (glaze - body)")
    print("-" * 64)
    if diff > 0.3:
        print("FIT: CRAZING risk. Glaze expansion is higher than the body, so the")
        print("     glaze cools into TENSION and may craze. Lower it: more SiO2/Al2O3,")
        print("     add Li2O/MgO/B2O3, or trade K2O/Na2O for those.")
    elif diff < -1.5:
        print("FIT: SHIVERING risk. Glaze expansion is far below the body, so the")
        print("     glaze is under heavy COMPRESSION and may shiver off edges. Raise")
        print("     it: more KNaO (feldspar), less Li2O/MgO/boron.")
    else:
        print("FIT: Likely OK. Glaze sits at/just below the body -> mild, beneficial")
        print("     compression (Hansen's rule of thumb). Still confirm with tests.")
    print("=" * 64)
    print("Reminder: relative estimate only (factor set in oxides.json). Body CTE")
    print("cannot be calculated - use a measured value. See thermal-expansion.md.")


if __name__ == "__main__":
    main()
