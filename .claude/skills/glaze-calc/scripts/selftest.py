#!/usr/bin/env python3
"""Tiny smoke test for the glaze-calc tools. Run: python3 selftest.py
Exits non-zero on failure. No third-party deps."""
import glazelib as g

FLUX = {"flux_r2o", "flux_ro"}


def approx(a, b, tol):
    return abs(a - b) <= tol


def main():
    oxides = g.load_oxides()
    materials = g.load_materials()
    recipe = g.load_recipe("G2926B")

    _, mol, unknown = g.recipe_to_oxides(recipe, materials, oxides)
    assert not unknown, f"unknown materials/oxides: {unknown}"

    # UMF: fluxes unify to 1.0
    flux_total = sum(m for ox, m in mol.items() if oxides[ox]["role"] in FLUX)
    umf = {ox: m / flux_total for ox, m in mol.items()}
    flux_sum = sum(umf[ox] for ox in umf if oxides[ox]["role"] in FLUX)
    assert approx(flux_sum, 1.0, 1e-9), f"flux unity != 1.0: {flux_sum}"

    ratio = umf["SiO2"] / umf["Al2O3"]
    assert 5.0 <= ratio <= 12.0, f"SiO2:Al2O3 out of range: {ratio:.2f}"

    # CTE: G2926B should land in a believable glaze range
    total = sum(mol.values())
    cte_e7 = sum((m / total) * oxides[ox]["cte_factor"] for ox, m in mol.items())
    glaze_cte = cte_e7 / 10.0
    assert 5.0 <= glaze_cte <= 9.0, f"CTE out of range: {glaze_cte:.2f}"

    # every material analysis references known oxides and is plausibly ~100 with LOI
    for name, m in materials.items():
        for ox in m["analysis"]:
            assert ox in oxides, f"{name}: unknown oxide {ox}"
        total_pct = sum(m["analysis"].values()) + m.get("LOI", 0)
        assert 95 <= total_pct <= 102, f"{name}: oxides+LOI = {total_pct:.1f} (expected ~100)"

    print(f"OK  G2926B: SiO2:Al2O3={ratio:.2f}:1, flux unity={flux_sum:.3f}, "
          f"CTE={glaze_cte:.2f}e-6  |  {len(materials)} materials, "
          f"{len(oxides)} oxides validated")


if __name__ == "__main__":
    main()
