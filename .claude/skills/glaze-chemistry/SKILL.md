---
name: glaze-chemistry
description: >-
  Ceramic glaze oxide chemistry and colorant behavior, with Digital Fire citations.
  Use for: how colorants behave in oxidation vs reduction (copper, iron, titanium,
  manganese, cobalt, chrome, nickel, rutile); the difference between titanium dioxide
  and rutile; oxide roles as fluxes / stabilizers / glass-formers (RO, R2O3, RO2) at
  cone 6; what causes crazing vs shivering; and how thermal expansion (COE/CTE) is
  calculated. Trigger on glaze chemistry, oxide, flux, colorant, oxidation, reduction,
  copper red, celadon, tenmoku, rutile, titania, crazing, shivering, thermal expansion,
  Seger, UMF, cone 6.
---

# glaze-chemistry

Grounded reference knowledge for glaze chemistry, focused on **cone 6 porcelain** in a
home **electric kiln** (oxidation), with **saggar** local reduction as a deliberate option.
The companion `glaze-calc` skill does the arithmetic; this skill explains the chemistry.

## Citation discipline

Cite the **specific Digital Fire page** for a claim — `/oxide/<symbol>`,
`/glossary/<term+with+plus>`, `/material/<name>` (see the `digitalfire-search` skill for URL
patterns). Prefer oxide/glossary pages. When a statement is reasoning rather than a direct
citation, say so. Treat numeric values (expansion, %) as guidance and recommend testing.

## Reference docs (load as needed)

- **`colorants-atmosphere.md`** — every colorant ranked by how much it shifts between
  oxidation and reduction (copper and iron biggest; titanium does react; cobalt/chrome/nickel
  basically stable), plus **TiO2 vs rutile**, and a saggar note.
- **`oxides-fluxes.md`** — the RO / R2O3 / RO2 roles, which fluxes matter at cone 6
  (boron + frits, alkalis, alkaline earths), and the common opacifiers/colorant oxides.
- **`thermal-expansion.md`** — **how COE/CTE is calculated** (answers "how does Insight do
  it?"), why crazing/shivering happen, and how to adjust fit.
- **`cones.md`** — cones as heatwork, cone 6 vs cone 10, porcelain firing.

## Quick answers

- **Biggest atmosphere shifts:** Copper (green ⇄ blood-red) and iron (amber antiflux ⇄ FeO
  powerful flux, celadon/tenmoku). Titanium *does* react in reduction. Cobalt, chrome, and
  nickel are essentially atmosphere-stable — their variation comes from the host glaze, not
  the atmosphere. Full ranking + citations in `colorants-atmosphere.md`.
- **Crazing** = glaze expansion too **high** vs the body (glaze in tension, cracks). **Shivering**
  = expansion too **low** (glaze in compression, flakes off). Fix by moving expansion;
  see `thermal-expansion.md`. Compute it with `glaze-calc`'s `cte.py`.
- **Want a number?** Use `glaze-calc` (`umf.py`, `cte.py`) rather than estimating by hand.
