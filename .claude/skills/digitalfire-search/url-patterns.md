# Digital Fire URL patterns (reference)

The Digital Fire Reference Library exposes its database through clean, permanent URLs of the
form `digitalfire.com/<section>/<identifier>`. Build the URL and `WebFetch` it.

## Sections and patterns

| Section | List page | Item pattern | Examples |
|---------|-----------|--------------|----------|
| Oxides | `/oxides` or `/oxide/list` | `/oxide/<symbol>` (numeric id also works) | `/oxide/cuo`, `/oxide/fe2o3`, `/oxide/tio2`, `/oxide/coo`, `/oxide/cr2o3`, `/oxide/mno`, `/oxide/nio`, `/oxide/k2o` |
| Materials | `/material/list` | `/material/<name>` or `/material/<id>` | `/material/rutile`, `/material/nepheline+syenite`, `/material/ferro+frit+3134`, `/material/epk` |
| Recipes | `/recipe/list` | `/recipe/<code>` | `/recipe/g2926b`, `/recipe/g2934` |
| Glossary | (search box) | `/glossary/<term+with+plus>` | `/glossary/reduction+firing`, `/glossary/oxidation+firing`, `/glossary/co-efficient+of+thermal+expansion`, `/glossary/calculated+thermal+expansion`, `/glossary/crazing`, `/glossary/specific+gravity`, `/glossary/thixotropy`, `/glossary/brushing+glaze`, `/glossary/dipping+glaze` |
| Articles | `/article/list`? | `/article/<title+with+plus>` | `/article/understanding+thermal+expansion+in+ceramic+glazes` |
| Tests | `/test/list` | `/test/<id>` | |
| Troubles | `/trouble/list` | `/trouble/<name>` | glaze-defect troubleshooting |
| Minerals | `/mineral/list` | | |
| Hazards | `/hazard/list` | | material safety |
| Properties | `/property/list` | | |
| Firing schedules | `/schedule/list` | | |
| Temperatures | `/temperature/list` | | cone/temperature |
| Typecodes | `/typecode/list` | | glaze type classification |
| Pictures/Media | `/picture/list` | | |
| Projects | `/project/list` | | |
| Videos | `/video/list` | | |

## Conventions

- **Spaces → `+`** (occasionally `%20`). Names are case-insensitive; lowercase is safe.
- **Oxide symbols** use the chemical formula lowercased: `cuo`, `fe2o3`, `tio2`, `al2o3`,
  `sio2`, `na2o`, `k2o`, `cao`, `mgo`, `zno`, `b2o3`, `zro2`, `sno2`.
- An **oxide page** contains a data block (physical constants, expansion), Notes, "Mechanisms"
  subsections (e.g. Glaze Color), images with captions, and cross-links to related materials
  and tests — quote the Notes/Mechanisms for chemistry claims.

## Enumerating / discovery

- **Sitemap index:** `https://digitalfire.com/sitemapindex.xml` lists the canonical URLs.
  `robots.txt` sets a **20-second crawl-delay** and disallows `/cgi-bin/`, `/videos/`,
  `/uploads/` — fetch one page at a time, politely.
- **No documented public API / JSON export.** The predictable URLs + sitemap are the reliable
  mechanical access path.
- **Search-query URL: UNVERIFIED.** A `?q=`-style endpoint returned 404 in testing. Use the
  on-site search box if needed, but don't hard-code a query URL without confirming the live
  request format first.

## Quick citation recipe

1. Identify the entity (oxide / material / recipe / concept).
2. Build the URL from the table above.
3. `WebFetch` it; quote the relevant line.
4. Cite the full path, e.g. `digitalfire.com/oxide/cuo`.
