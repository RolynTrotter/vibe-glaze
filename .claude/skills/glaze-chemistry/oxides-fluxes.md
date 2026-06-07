# Oxide roles: fluxes, stabilizers, glass-formers

A glaze is a glass. Its oxides sort into three structural roles — the basis of the Seger /
Unity Molecular Formula (UMF). See [glossary/formula+unity](https://digitalfire.com/glossary/unity+formula)
and use `glaze-calc`'s `umf.py` to compute the ratios for any recipe.

## The three columns

- **RO / R2O — fluxes (the "bases").** Lower the melting point and form the glass network's
  modifiers.
  - **R2O (alkalis):** Li2O, Na2O, K2O — strong, low-temperature fluxes; high thermal
    expansion (Na2O, K2O are the biggest expansion contributors; **Li2O is the exception —
    a strong flux with LOW expansion**).
  - **RO (alkaline earths / others):** CaO (the workhorse high-temp flux), MgO (refractory at
    low %, matting/satin at cone 6, low expansion), BaO/SrO (matte fluxes), ZnO (flux +
    crystallization), PbO (toxic — not used in studio cone-6 work).
- **R2O3 — stabilizers / intermediates.** Chiefly **Al2O3 (alumina)** — stiffens the melt,
  prevents running and devitrification, raises durability, and controls glossy-vs-matte.
  **B2O3 (boron)** sits here by formula but *acts as a flux* — it is the key **low-expansion
  melter** that makes most cone-6 glazes possible.
- **RO2 — glass-formers.** **SiO2 (silica)** is the glass. **TiO2** and **ZrO2** are also
  RO2; both also act as opacifiers/crystallizers (and TiO2 as a colorant/variegator).

The **SiO2:Al2O3 ratio** is the main lever for surface: low ratio (~5–6:1) → matte/stiff;
high ratio (~8–12:1) → glossy/fluid. Glossy cone-6 transparents typically land ~7–10:1.

## What melts a glaze at cone 6 (≈1222 °C)

Cone 6 is too cool for feldspar alone to melt well, so cone-6 glazes lean on **boron**:
- **Boron frits** (Ferro **3134** = high-boron, no alumina; **3124** = boron + some alumina)
  are the usual primary melters. Gerstley borate / its substitutes are the raw-material route.
- **Feldspars / nepheline syenite** supply KNaO + Al2O3 + SiO2 (the glass backbone).
- **Whiting / wollastonite / dolomite** supply CaO (and MgO from dolomite/talc) — the
  high-temperature fluxes that mature the melt and add durability.
- **Silica** and **kaolin (EPK)** supply SiO2 and Al2O3 to balance the UMF (kaolin also
  supplies plasticity/suspension to the raw slurry).

A balanced cone-6 glossy roughly targets: fluxes summing to 1.0 with a healthy CaO share,
some boron, Al2O3 ~0.3–0.4, SiO2 ~3–4 (ratio ~8–10:1). Mattes drop the SiO2:Al2O3 ratio
and/or raise MgO/BaO. Verify any recipe with `umf.py`.

## Opacifiers and colorant oxides (quick reference)

- **Opacifiers:** **SnO2 (tin)** ~5–8% for a soft white; **zircon (ZrO2 as zirconium
  silicate)** ~8–12% for a brighter, cheaper white; **TiO2** for crystalline opacity +
  variegation.
- **Colorant oxides** and their atmosphere behavior are covered in `colorants-atmosphere.md`:
  Fe2O3, CuO, CoO, Cr2O3, MnO, NiO, TiO2. Their melt effects vary — iron and copper flux in
  reduction; chrome and tin together can give pinks; chrome + zinc goes brown; cobalt is a
  strong, stable blue at <1%.

For melting points, expansion factors, and hazards of an individual oxide, go to its Digital
Fire page (`/oxide/<symbol>`) via the `digitalfire-search` skill.
