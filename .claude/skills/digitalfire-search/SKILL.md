---
name: digitalfire-search
description: >-
  How to find and CITE pages on Digital Fire (digitalfire.com, Tony Hansen's ceramic
  reference library) reliably, plus other ceramics data sources. Use when you need to
  look up an oxide, material, glaze recipe, or glossary term on digitalfire, construct
  the right URL, or cite a source for a glaze-chemistry claim. Trigger on digitalfire,
  Digital Fire, Tony Hansen, Insight, look up oxide/material/recipe, cite a source,
  glaze recipe database, ceramic reference.
---

# digitalfire-search

Digital Fire is the highest-quality free ceramics reference. Its URLs are **stable and
predictable**, so you can usually go straight to the right page (and fetch it to quote
accurately) instead of guessing. This skill documents the patterns and citation rules; see
`url-patterns.md` for the full table.

## Go-to URL patterns

| You want | URL | Example |
|----------|-----|---------|
| An **oxide** | `digitalfire.com/oxide/<symbol>` | `/oxide/cuo`, `/oxide/fe2o3`, `/oxide/tio2` |
| A **material** | `digitalfire.com/material/<name>` | `/material/rutile`, `/material/nepheline+syenite` |
| A **recipe** | `digitalfire.com/recipe/<code>` | `/recipe/g2926b` |
| A **glossary** term | `digitalfire.com/glossary/<term+with+plus>` | `/glossary/reduction+firing` |
| An **article** | `digitalfire.com/article/<title+with+plus>` | |
| A **section list** | `digitalfire.com/<section>/list` | `/recipe/list`, `/test/list` |

Spaces in names become **`+`** (sometimes `%20`). Lowercase works. To enumerate everything,
use the **sitemap index**: `https://digitalfire.com/sitemapindex.xml` (robots.txt sets a 20s
crawl-delay — fetch politely).

## How to use it

1. **Construct the URL** from the pattern and `WebFetch` it to read/quote the actual page,
   rather than relying on memory. Oxide and glossary pages are the most authoritative for
   chemistry claims.
2. **Cite the specific page** you used (full path), not just "digitalfire.com".
3. If a name doesn't resolve, try the index/list page or the sitemap, or search the site's
   own search box. **Caveat:** a constructable `?q=` search-query URL was **not verified**
   (a probe returned 404) — don't hard-code a search endpoint; prefer the predictable URLs +
   sitemap, or inspect the live search request first.

## Other sources (secondary)

- **Glazy** (glazy.org) — large community recipe library + UMF/Stull analysis. Filter URLs
  like `glazy.org/search?base_type=110`. Its open dataset
  ([github.com/derekphilipau/glazy-data](https://github.com/derekphilipau/glazy-data)) is
  **CC BY-NC-SA 4.0 (NonCommercial)** — reference only; **do not copy it into this repo** (see
  `CONTRIBUTING.md`).
- **Insight-live** (insight-live.com) — Hansen's glaze-calc app (UMF, COE, etc.); good for
  cross-checking `glaze-calc` numbers.
- **openglaze** (github.com/KyaniteLabs/openglaze) — open-source glaze calculator.

See `url-patterns.md` for the complete section list and more examples.
