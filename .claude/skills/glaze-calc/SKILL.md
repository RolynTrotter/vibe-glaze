---
name: glaze-calc
description: >-
  Glaze calculation tools (Python, no dependencies). Use to compute a recipe's
  UMF / Seger unity molecular formula, estimate thermal expansion (CTE/COE) and
  check glaze-body fit (crazing/shivering), scale a recipe to a batch weight, and
  convert units (grams/ounces, Celsius/Fahrenheit, cone-to-temperature, specific
  gravity to % solids, "+X% addition" math). Trigger on UMF, Seger formula, unity,
  flux ratio, SiO2:Al2O3, thermal expansion, COE, CTE, crazing fit, batch scaling,
  specific gravity, cone temperature.
---

# glaze-calc

Calculators for glaze chemistry and batching. Stock `python3` (3.8+), no third-party
packages. Run them with the working directory at this skill's `scripts/` folder, or use
absolute paths. Reference data lives in `data/` (oxide constants, material analyses,
base recipes) — see `${CLAUDE_SKILL_DIR}/data/`.

> Always state which numbers are estimates. CTE is **relative** (factor-set dependent) and
> body expansion cannot be calculated. Confirm fit and food-safety empirically.

## Recipe input format

A recipe is JSON. `materials` are the base (batch percentages or any weights);
`additions` are colorants/opacifiers/fluxes added **on top** (the studio "+X%" convention):

```json
{"name": "My glaze",
 "materials": {"Nepheline Syenite": 18.3, "Ferro Frit 3134": 25.4, "EPK": 19.6,
               "Wollastonite": 6.9, "Silica": 37.6, "Talc": 2.3},
 "additions": {"Titanium Dioxide": 4, "Black Iron Oxide": 2}}
```

You can also pass a built-in base-recipe **code** (e.g. `G2926B`) instead of a file, and
add materials inline with `--add`. Material names are matched case-insensitively with
aliases (see `data/materials.json`). Unknown materials error out clearly — add them to
`materials.json` rather than guessing.

## Commands

```bash
cd ${CLAUDE_SKILL_DIR}/scripts

# UMF (unity molecular formula)
python3 umf.py G2926B
python3 umf.py recipe.json
python3 umf.py G2926B --add "Black Iron Oxide=2,Titanium Dioxide=4"

# Thermal expansion + fit (pass your body's measured CTE in x10^-6 with --body)
python3 cte.py G2926B --body 6.8
python3 cte.py G2926B --add "Lithium Carbonate=3"

# Conversions / batching
python3 convert.py cone 6                # cone -> approx temperature
python3 convert.py batch G2926B 5000     # scale recipe to 5000 g dry
python3 convert.py add 5000 3            # grams for a +3% addition on 5000 g
python3 convert.py sg 1.45               # slurry SG -> % solids by weight
python3 convert.py g-oz 28.35            # and oz-g, c-f, f-c
```

## How the math works (so you can explain it)

- **UMF** (`umf.py`): normalize the batch → multiply each material by its oxide analysis to
  get oxide grams (LOI burns off) → divide by molar mass to get **moles** → divide every
  oxide by the **sum of the flux moles (RO + R2O)** so fluxes total **1.0**. Report grouped
  by role plus the **SiO2:Al2O3** and **R2O:RO** ratios. Boron (B2O3) is grouped with the
  stabilizers but acts as a flux.
- **CTE** (`cte.py`): `CTE = Σ (oxide mole fraction × that oxide's expansion factor)`. The
  per-oxide breakdown is printed so you can see, e.g., that Na2O/K2O dominate expansion. This
  is the same additivity idea Insight/Glazy use — see the `glaze-chemistry`
  skill's `thermal-expansion.md` for the full explanation and the factor-set caveats.

## Smoke test / expected output

`python3 umf.py G2926B` → fluxes sum to 1.0 (CaO ~0.60 dominant), **SiO2:Al2O3 ≈ 10–11:1**
(high silica — G2926B is a deliberately low-mobility ultra-clear). `python3 cte.py G2926B`
→ glaze CTE ≈ **7.0 ×10⁻⁶/°C**, "Likely OK" vs a 6.8 body. `python3 convert.py cone 6`
→ **~1222 °C**. If these are wildly off, the data files were edited — check `data/`.

> Precision note: absolute UMF/CTE depend on the **typical** analyses in `data/materials.json`.
> For a published recipe, cross-check against Insight/Glazy and your supplier's data sheets.
