# Contributing — authoring skills for vibe-glaze

This repo is a collection of **Claude Code Skills**. Each skill is a directory under
`.claude/skills/` that a Claude Code session auto-discovers and loads on demand. These
conventions keep the skills consistent, reliable, and well-cited.

## Skill anatomy

```
.claude/skills/<skill-name>/
├── SKILL.md          # required: YAML frontmatter + concise instructions
├── <topic>.md        # optional: reference docs loaded on demand
├── scripts/          # optional: executable helpers (python3, no deps)
└── data/             # optional: curated data (JSON)
```

### SKILL.md frontmatter

```yaml
---
name: glaze-chemistry
description: >-
  Glaze oxide chemistry and colorant behavior. Use for questions about fluxes,
  stabilizers, glass-formers, colorants in oxidation vs reduction, TiO2 vs rutile,
  crazing/shivering, or thermal expansion at cone 6.
---
```

- **`description` is the only thing loaded at session start** — it's what makes the skill
  auto-trigger. Lead with concrete use cases and pack in the words a user would actually
  type: *glaze, cone 6, reduction, oxidation, crazing, shivering, UMF, flux, rutile,
  saggar, digitalfire*. Keep `description` (+ optional `when_to_use`) under ~1,536 chars.
- `name` defaults to the directory name; the directory name also defines the `/slash`
  command. Use `lowercase-with-hyphens`.

### Keep SKILL.md short (progressive disclosure)

SKILL.md stays in context for the rest of the session once loaded, so keep it terse
(target well under ~500 lines). Put bulk reference material in sibling `.md` files and
link to them, e.g. `See colorants-atmosphere.md for the full ranking.` Reference bundled
files with `${CLAUDE_SKILL_DIR}/...` so paths resolve regardless of working directory.

### Scripts & data

- Scripts must run on stock **`python3` (3.11+) with no third-party dependencies**.
- Document exact invocation and input format in SKILL.md, e.g.
  `python3 ${CLAUDE_SKILL_DIR}/scripts/umf.py <recipe.json>`.
- Keep curated data in `data/*.json` with a `source` / citation field on every entry.

## Citation discipline (important)

This repo's value is being *more rigorous than chat*. Therefore:

1. **Cite the specific Digital Fire page** for a chemistry claim — link the
   `/oxide/<symbol>`, `/glossary/<term+with+plus>`, `/material/<name>`, or
   `/recipe/<code>` page, not just "digitalfire.com". The `digitalfire-search` skill
   documents the URL patterns.
2. **Distinguish sourced facts from reasoned inference.** When a claim is physics/chemistry
   reasoning rather than a direct citation (e.g. saggar gas behavior), say so explicitly
   and mark it. Never present an inference as if it were sourced.
3. **Numbers are estimates.** Thermal-expansion values are relative and factor-set
   dependent; body expansion cannot be calculated. Flag guidance-level numbers.

## Data sourcing & licensing

- **Do not copy Glazy's open dataset** into this repo — it is CC BY-NC-SA 4.0
  (NonCommercial). Use it for reference only.
- Build bundled material analyses from primary/public sources (Digital Fire material
  pages, manufacturer data sheets) and record the source in the data file.

## Testing a skill locally

- Run any scripts directly and confirm sane output (see each skill's SKILL.md for a smoke
  test / worked example).
- Open a fresh Claude Code session in this repo, ask a question that *should* trigger the
  skill, and confirm it loads and answers with citations. If it doesn't trigger, tighten
  the `description` with better trigger words.
