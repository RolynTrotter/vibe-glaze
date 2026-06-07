# Mixing & application (cone-6 porcelain studio)

Numbers below are **guidance-level starting points** — dial in by testing. Concept pages:
[glossary/specific+gravity](https://digitalfire.com/glossary/specific+gravity),
[glossary/thixotropy](https://digitalfire.com/glossary/thixotropy),
[glossary/brushing+glaze](https://digitalfire.com/glossary/brushing+glaze),
[glossary/dipping+glaze](https://digitalfire.com/glossary/dipping+glaze).

## Batching

- Recipe = materials as **weight %** summing to ~100; colorants/opacifiers/additives are
  **additions on top** ("+2% iron"). Scale to grams with `glaze-calc`:
  `python3 convert.py batch <recipe> <dry_grams>`, and additions with `convert.py add`.
- For a few test tiles, 100–300 g dry is plenty; for dipping a load, 2–5 kg.

## Water & specific gravity (the key control)

**Specific gravity (SG)** of the slurry controls applied thickness more than anything else.
Measure it: weigh a known volume (e.g. 100 mL) of well-stirred glaze; grams ÷ mL = SG. Convert
to % solids with `python3 convert.py sg <value>`.

| Application | Target SG | Notes |
|-------------|-----------|-------|
| **Dipping** | ~1.40–1.50 | One smooth coat; tune dwell time. Most studio glazes. |
| **Brushing**| ~1.25–1.35 | Thinner + a gum medium; needs 2–3 coats, cross-hatched. |
| Pouring/spraying | ~1.35–1.45 | Between the two; spraying builds in light passes. |

Adjust SG by adding water (lower) or letting it settle and decanting water (raise). Always
**sieve** a new batch through 80–100 mesh (twice) to disperse colorants and remove lumps.

## Suspension & application additives

- **Bentonite** (~2% of the dry batch, *added with the dry materials before water*) keeps the
  glaze in suspension and hardens the dry coat. Already a small amount in many recipes.
- **CMC gum** (carboxymethyl cellulose) = the **brushing medium**: it suspends, slows drying,
  and gives brushability. Make a gel (~1–4% CMC powder in hot water, let it hydrate) and mix it
  into a brushing batch. **Not used in dipping glazes** (it slows drying too much).
- **Epsom salts** (a pinch dissolved in water) = **flocculant**: thickens/gels a watery,
  settling glaze (raises thixotropy) without adding solids — useful when SG is right but the
  glaze settles hard or applies thin.
- **Thixotropy:** a good dipping glaze gels slightly at rest and flows when moving (even, drip-
  free coats). Flocculate (epsom) to increase it; deflocculate (a drop of Darvan) to decrease.

## Applying to porcelain (thrown, bisque-fired)

- Glaze goes on **bisque** (porous, ~cone 06–04). Make sure bisque is **clean and dust-free**
  (wipe/damp-sponge); oils from handling cause crawling.
- Porcelain bisque is dense/less absorbent than earthenware — it drinks glaze **slower**, so
  dip a touch longer or run a slightly higher SG than you would on a thirsty body.
- **Even thickness** matters: too thick → crawling, running, pinholes; too thin → dry/underfired
  surface and washed-out color. Aim for roughly a credit-card thickness (~1 mm) unless the
  glaze wants more.
- **Wax-resist** feet/bottoms; clean any glaze off the foot before firing.
- For **saggar pieces**, application interacts with the flashing — often slips/bare-burnished
  porcelain or thin glaze is used so the reduction/metal vapor reads. Test a sample saggar.

## Always

- **Test tiles first** (and ideally a line blend when dialing colorant %). Fire on your real
  schedule and body.
- **Food safety:** any functional ware must be checked for durability/leaching — crazed glazes
  and high copper/manganese/barium are red flags. Decorative-only otherwise.
