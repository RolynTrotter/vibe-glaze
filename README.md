# vibe-glaze

A repository of **Claude Code Skills** for ceramics — specifically glaze chemistry,
kiln-atmosphere science, and recipe formulation for a studio potter who throws
**porcelain** and fires a **home electric kiln at cone 6**, with **saggars** for
localized reduction.

The goal: open a Claude Code session *in this repo* and have it outperform plain chat
on real ceramics questions — grounded chemistry, disciplined citations to
[Tony Hansen's Digital Fire](https://digitalfire.com), and actual calculation
(UMF, thermal-expansion fit, batch math) instead of hand-waving.

## How to use it

1. Open a Claude Code session with this repository as the working directory.
2. The skills under [`.claude/skills/`](.claude/skills/) are auto-discovered. Ask a
   normal question ("which colorants shift most in reduction?", "design a cone-6 rutile
   blue from G2926B", "how does Insight compute thermal expansion?") and the relevant
   skill loads automatically. You can also invoke one explicitly, e.g. `/glaze-calc`.
3. Calculation scripts live inside the `glaze-calc` skill and are run by the session on
   your behalf (`python3` — no third-party dependencies).

## Planned skills (v1.0)

| Skill | What it does |
|-------|--------------|
| `glaze-chemistry` | Oxide roles (flux / stabilizer / glass-former), colorant behavior in oxidation vs reduction, TiO₂ vs rutile, and the thermal-expansion math — every claim cited to Digital Fire. |
| `firing-and-atmosphere` | The physical chemistry of *firing*: how reduction is created (CO / combustion), and saggar dynamics — trapped gases and water vapor at cone 6. |
| `digitalfire-search` | How to search and **cite** digitalfire.com reliably (stable URL patterns, sitemap) plus secondary sources. |
| `glaze-calc` | Scripts + curated data: recipe→UMF, glaze CTE estimate with body-fit check, and unit/batch conversions. |
| `glaze-recipe-formulation` | The end-to-end workflow: start from a base recipe (e.g. G2926B), apply additions, sanity-check with the calc scripts, and output a grams batch with mixing + application instructions. |

See the repo's GitHub issues for the v1.0 backlog and status.

## Repository layout

```
.claude/skills/<name>/SKILL.md   # one skill per directory (auto-discovered)
.claude/skills/<name>/*.md        # reference docs (progressive disclosure)
.claude/skills/glaze-calc/scripts # python calculators
.claude/skills/glaze-calc/data    # curated material analyses, oxide data, base recipes
```

## Sources & attribution

- **Digital Fire** (digitalfire.com, Tony Hansen) is the primary reference. Skills cite
  specific oxide / glossary / material / recipe pages rather than asserting from memory.
- **Glazy** (glazy.org) and its [open data](https://github.com/derekphilipau/glazy-data)
  are used for reference only; that data is **CC BY-NC-SA 4.0 (NonCommercial)**, so this
  repo does **not** copy it. Bundled material analyses are built from primary/public
  sources and cited in-place.

## Disclaimer

This repo helps you reason about and design glazes; it does not replace testing. Always
fire test tiles, verify glaze fit empirically, and confirm **food-safety / leaching**
for functional ware. Thermal-expansion numbers are *relative* estimates (body expansion
cannot be reliably calculated). Treat all outputs as a starting point, not gospel.
