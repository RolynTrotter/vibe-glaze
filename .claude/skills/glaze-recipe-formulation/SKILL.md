---
name: glaze-recipe-formulation
description: >-
  End-to-end workflow for designing/altering a cone-6 porcelain glaze and turning it into
  something to actually mix and apply. Use when asked to construct, formulate, modify, or
  "build a recipe for" a glaze (e.g. a rutile blue, a celadon, a satin white), to add
  colorants/opacifiers to a base, to start from a named base like G2926B and apply
  additions, or to produce a weigh-out batch with mixing and application instructions.
  Trigger on construct/build/design a glaze, glaze recipe, base glaze, add colorant,
  rutile blue, celadon, satin matte, batch out, mix a glaze, application, brushing,
  dipping.
---

# glaze-recipe-formulation

Turns a glaze idea into a tested-on-paper recipe and concrete mixing/application
instructions, pulling in the other skills:
`glaze-chemistry` (what oxides/colorants do) · `firing-and-atmosphere` (oxidation/saggar) ·
`digitalfire-search` (find/cite bases & data) · `glaze-calc` (UMF, CTE, batching).

Default context: **cone 6, porcelain, electric (oxidation)**, with **saggar** as the
reduction option. Always end with a test-tile suggestion and a food-safety caveat.

## Workflow

1. **Clarify intent.** Color, surface (glossy/satin/matte), transparent vs opaque,
   functional vs decorative, atmosphere (oxidation vs saggar reduction), and the body's CTE
   if known. Ask only what you can't reasonably assume.
2. **Pick a base.**
   - A named Digital Fire base by code — e.g. **G2926B** (cone-6 glossy transparent) — from
     `glaze-calc/data/base-recipes.json`, or fetch it live via `digitalfire-search`.
   - Or draft one: balance fluxes (boron/frit + CaO + KNaO), Al2O3 ~0.3–0.4, SiO2 ~3–4, using
     `glaze-chemistry/oxides-fluxes.md`. Verify with `umf.py`.
3. **Apply additions (the "+X%" convention).** Colorants/opacifiers/fluxes on top of the
   base 100. Use `glaze-chemistry/colorants-atmosphere.md` to choose and predict color
   (account for atmosphere — copper/iron/titania shift in saggar reduction).
4. **Sanity-check with `glaze-calc`.**
   ```bash
   cd ../glaze-calc/scripts
   python3 umf.py G2926B --add "Rutile=4,Cobalt Carbonate=0.5"   # fluxes, SiO2:Al2O3
   python3 cte.py G2926B --add "Rutile=4" --body <your_body_CTE> # crazing/shivering fit
   ```
   Check: fluxes reasonable, SiO2:Al2O3 in range for the surface you want, CTE vs body OK.
   Note that a flux *addition* barely moves CTE — to change fit, substitute, don't sprinkle
   (see `glaze-chemistry/thermal-expansion.md`).
5. **Batch it out.** `python3 convert.py batch <recipe> <grams>` for a weigh-out in grams.
6. **Output** (always include all of these):
   - Final recipe: base materials (%) + additions (+%), and the **grams** for the requested
     batch size.
   - **Mixing instructions**: water, sieve, target specific gravity, suspension additives —
     see `mixing.md`.
   - **Application**: brushing vs dipping, thickness, on porcelain (bisque) — see `mixing.md`.
   - **Test plan**: test tiles before a full load; for saggar pieces, a test saggar.
   - **Caveats**: results need firing to confirm; **food-safety/leaching** must be verified
     for functional ware (especially colorants like copper/manganese/barium and any crazing).

## Worked example: rutile blue on G2926B (from the user's questions)

> "Construct a rutile blue glaze using G2926B as the base with additions of black iron oxide
> and titanium dioxide" — then "consider it with a 3% lithium carbonate addition."

- **Chemistry:** rutile/titania blues come from titania-driven micro-crystallization
  scattering light to read blue, warmed/broken by iron; a touch of cobalt deepens the blue.
  Black iron oxide adds iron color + speckle; TiO2 adds the crystallization/opacity. In a
  **saggar** these warm/variegate further (see `colorants-atmosphere.md`).
- **Draft:** G2926B base + (e.g.) Titanium Dioxide 4%, Black Iron Oxide 2% (optionally
  Cobalt Carbonate 0.5–1% if a stronger, more reliable blue is wanted). Confirm with
  `umf.py G2926B --add "Titanium Dioxide=4,Black Iron Oxide=2"`.
- **The lithium concern:** if crazing is the worry, run
  `cte.py G2926B --add "Lithium Carbonate=3"` — you'll see a **+3% addition barely changes
  CTE**. The honest move is to *substitute* Li2O for some KNaO (or add SiO2) to actually lower
  expansion; lithium *added* mainly increases melt fluidity (which can also intensify a rutile
  break). Explain this trade-off rather than implying +3% "fixes" fit.
- Then batch and give mixing/application per `mixing.md`, and recommend a line-blend of
  test tiles (vary TiO2 and iron) before committing.
