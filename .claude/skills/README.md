# Skills index

Each subdirectory here is a Claude Code Skill, auto-discovered when a session runs in this
repo. See [`../../CONTRIBUTING.md`](../../CONTRIBUTING.md) for authoring conventions.

## v1.0 skills

- **`glaze-chemistry/`** — oxide roles, colorant behavior in oxidation vs reduction,
  TiO₂ vs rutile, and thermal-expansion math. Cited to Digital Fire.
- **`firing-and-atmosphere/`** — how reduction is created (CO / combustion) and saggar
  atmosphere dynamics (trapped gases / water vapor at cone 6).
- **`digitalfire-search/`** — stable URL patterns + citation discipline for digitalfire.com
  and secondary sources.
- **`glaze-calc/`** — `scripts/` (recipe→UMF, CTE + body fit, unit/batch conversions) and
  `data/` (material analyses, oxide constants, base recipes).
- **`glaze-recipe-formulation/`** — end-to-end workflow: base recipe → additions → calc
  sanity check → grams batch + mixing & application instructions.

All five v1.0 skills are implemented. Calculation tools live in `glaze-calc/scripts/`
(run `python3 selftest.py` there for a smoke test).
