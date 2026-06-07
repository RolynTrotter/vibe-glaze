# Thermal expansion (COE/CTE): the math, and glaze fit

This answers "**how does Insight Live compute thermal expansion, and what's the math behind
it?**" and explains crazing/shivering. To get a number for a real recipe, run
`glaze-calc`'s `cte.py` — it prints the exact per-oxide breakdown described here.

## The calculation (additivity of oxide factors)

The coefficient of thermal expansion of a glass is estimated as a **weighted sum of its
oxides' individual expansion factors**. Each oxide has an empirically-derived factor; the
glaze's expansion is the sum of (how much of that oxide is present) × (its factor):

```
CTE_glaze  =  Σ ( fraction_of_oxide_i  ×  expansion_factor_i )
```

That's the whole idea — it's a **weighted average**, not a per-mole or per-bond calculation.
Insight, Glazy, and `cte.py` all do this; they differ mainly in (a) whether the "fraction"
is by **mole** or by **weight**, and (b) **which published factor set** they use. `cte.py`
uses **mole fractions** of all the oxides and an English & Turner / Appen-style factor set
(listed in `glaze-calc/data/oxides.json`), reporting the result in ×10⁻⁶/°C. Source concept:
[glossary/calculated+thermal+expansion](https://digitalfire.com/glossary/calculated+thermal+expansion).

### Worked example (G2926B, from `cte.py`)

| oxide | mole% | factor (×10⁻⁷) | contribution | share |
|-------|------:|------:|------:|------:|
| SiO2  | 73.2% | 38  | 27.8 | 40% |
| Na2O  |  4.3% | 395 | 16.8 | 24% |
| CaO   |  9.0% | 163 | 14.6 | 21% |
| Al2O3 |  6.8% | 63  |  4.3 |  6% |
| B2O3  |  5.0% | 66  |  3.3 |  5% |
| K2O   |  0.6% | 465 |  2.6 |  4% |
| …     |       |     |      |     |
| **Sum** | | | **70.1 ×10⁻⁷** = **7.0 ×10⁻⁶/°C** | |

Notice **Na2O and K2O dominate** despite small mole% — their factors are ~10× silica's. That
is *the* practical insight: **the alkalis (KNaO) drive expansion**, so they are what you trade
to fix fit.

## Two big caveats (state these every time)

1. **It's relative, not absolute.** Appen, English & Turner, and Winkelmann-Schott factor
   sets disagree, especially for Al2O3, B2O3, and Li2O (which behave non-linearly). Use the
   number to **compare recipes** and judge **direction**, and cross-check against Insight/Glazy
   for an authoritative figure. Hansen stresses expansion can be predicted only *relatively*.
2. **Body expansion CANNOT be calculated.** Clay bodies are mineralogically complex
   (quartz inversion, cristobalite, mullite). You must use a **measured** body value or a
   manufacturer figure. `cte.py`'s `--body` defaults to a placeholder ~6.8 ×10⁻⁶ — replace it
   with your porcelain's real number. See
   [glossary/co-efficient+of+thermal+expansion](https://digitalfire.com/glossary/co-efficient+of+thermal+expansion).

## Crazing vs shivering (fit)

Glaze and body shrink as they cool. The mismatch sets up stress:
- **Glaze expansion HIGHER than body** → glaze ends in **tension** → it cracks: **crazing**
  (a fine crack network). A food-safety/strength problem on functional ware.
- **Glaze expansion LOWER than body** → glaze ends in **compression** → if excessive it
  **shivers** (flakes off edges/rims). More dangerous than crazing.
- **Hansen's rule of thumb:** aim for the body to have **slightly higher** expansion than the
  glaze, so the glaze sits under **mild compression** — strongest and craze-resistant.

### Adjusting fit (which direction to move)

To **lower** glaze expansion (cure crazing): reduce KNaO (less feldspar/neph sy); add or
substitute in **Li2O, MgO, B2O3** (low-expansion melters); add SiO2/Al2O3 if the melt allows.
To **raise** expansion (cure shivering): more KNaO, less lithia/magnesia/boron.

> Note from the calculator: a small flux **addition on top** (e.g. +3% lithium carbonate)
> barely moves calculated CTE, because it only slightly shifts every mole fraction. Lithium
> lowers expansion most effectively when it **substitutes for** K2O/Na2O, not when it's just
> sprinkled on top. `cte.py --add "Lithium Carbonate=3"` shows this directly.

Always confirm fit empirically: a 300 °F→ice-water (or boiling-water→ice) thermal-shock
test will reveal crazing that calculation misses.
