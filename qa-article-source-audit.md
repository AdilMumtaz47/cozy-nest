# Cozy Nest — Article SOURCE Audit (read-only)

- **Audited:** 2026-11-27 (PKT) — all 62 article markdown files in `content/posts/` (`_template.md` excluded)
- **Method:** scripted checks of frontmatter + body text, plus file-existence checks under `images/<slug>/`. No file was edited, `build.py` was not run (only read, to confirm how images/takeaways render). `build.py` skips inline `![...]` lines and inserts one figure per idea section from the frontmatter `images` list, in order; a paragraph-form Takeaway still renders, just not as the "Key Takeaways" bullet box.
- **Headline:** **47 of 62 articles clean, 15 with at least one anomaly.** No missing images anywhere. No placeholder/junk text anywhere. No article is missing ideas, FAQs, takeaways, title, category, or date.

## Totals

| Check | Result |
|---|---|
| Articles audited | 62 |
| Clean (no anomaly under checks 1–8) | 47 |
| With ≥1 anomaly | 15 |
| Idea sections | 62/62 have exactly 30, numbered 1–30 sequentially, no gaps/dupes |
| Frontmatter images | 62/62 list exactly 30 files; all 1,860 referenced files exist on disk; no duplicates |
| Inline body image lines | 30 in 38 articles; 0 in 24 articles (see Format note — not counted as a defect) |
| FAQs | 62/62 have exactly 8 Q&A pairs (496 answers total, 39–60 words) |
| Tip boxes | 20 originals have 0 (by design, not flagged); 42 newer have exactly 30, all 10 QUICK / 10 CHECK / 10 GUIDE by count |
| Takeaway section | present in 62/62; bullets in 61/62 |
| Frontmatter title / category / date | present and valid (YYYY-MM-DD) in 62/62; `slug` field matches filename in 62/62; all categories are among the 9 valid ones; no duplicate titles |
| Internal links | 151 total; 2 dead (same slug, one article) |
| Placeholder/junk hits | 0 (searched: lorem, TODO, XXX, [TODO], placeholder, pinned, TBD, FIXME, "coming soon"; plus a scan for prose lines ending in `,` `:` `;` or a dash — nothing) |

## Per-article anomaly list (15 articles)

### Tip-box rotation swaps — 8 articles
Rotation rule (from `_template.md`): idea n%3==1 → QUICK, n%3==2 → CHECK, n%3==0 → GUIDE. All 8 still total exactly 30 tips at 10/10/10 — only the order is swapped at two ideas each. In every case idea 1 is wrong (should be QUICK).

| Slug | Idea 1 (actual → expected) | Second swap (idea, actual → expected) |
|---|---|---|
| 2027-home-decor-ideas | 1: CHECK → QUICK | 26: QUICK → CHECK |
| 2027-interior-design-trends | 1: GUIDE → QUICK | 21: QUICK → GUIDE |
| bedroom-decor-ideas-2027 | 1: CHECK → QUICK | 5: QUICK → CHECK |
| cabbage-crush-decor | 1: CHECK → QUICK | 2: QUICK → CHECK |
| gallery-wall-ideas-living-room | 1: GUIDE → QUICK | 3: QUICK → GUIDE |
| home-library-lighting-ideas | 1: CHECK → QUICK | 2: QUICK → CHECK |
| neo-deco-living-room | 1: GUIDE → QUICK | 6: QUICK → GUIDE |
| new-year-bedroom-decor-ideas | 1: CHECK → QUICK | 8: QUICK → CHECK |

The other 34 tipped articles follow the QUICK/CHECK/GUIDE rotation exactly at every idea.

### Dead internal link — 1 article
- **neutral-bedroom** — links to `/posts/cozy-winter-bedroom-ideas/` **twice**, and that slug does not exist among the 62 articles:
  - L75 (intro paragraph): "…and [30 Cozy Winter Bedroom Ideas for a Warm Retreat](/posts/cozy-winter-bedroom-ideas/) shows the seasonal version."
  - L261 (Takeaway bullet): "…and [30 Cozy Winter Bedroom Ideas for a Warm Retreat](/posts/cozy-winter-bedroom-ideas/) shows the seasonal version."
  - Note: `_template.md` is itself a draft for the `cozy-winter-bedroom-ideas` slug — the target article exists only as the template, not as a published article. All other 149 internal links resolve to an existing slug (45 distinct targets checked, relative and absolute `cozynesthomeideas.com` forms).

### FAQ answer 1 word under the floor — 1 article
- **neutral-kitchen-decor-ideas** — Q6 "How do I add contrast to a neutral kitchen without colour?" is **39 words** (floor is 40). Answer: "Use black or brass in small doses: a black tap, brass handles, a dark pendant or a charcoal oven. Three dark pieces at most is the rule — enough to anchor the room, not enough to break the calm palette." (Em dash counted as punctuation, not a word.) All other 495 FAQ answers are 40–60 words; nothing exceeds 60.

### Takeaway in paragraph form — 1 article (known, confirmed)
- **2027-interior-design-trends** — `## Takeaway` is a single 105-word paragraph, 0 bullets (all other 61 articles have 3–4 bullets). Already known; confirmed present, so this is a format note, not a missing section. (This article is already in the anomaly list for its tip-rotation swap.)

### Category-rule flags — 5 articles
Judged from title + first 3 idea headings, and the full 30 headings where the call needed it. Only clear misfits listed; borderline cases (e.g. `christmas-table` pair vs Dining Room, `bookshelf-decor-ideas`, `valentine-mantel-decor`) were deliberately NOT flagged — see "Not flagged" below.

| Slug | Current | Should be | Reason |
|---|---|---|---|
| christmas-living-room | Christmas Decor | **Living Room Decor** | All 30 ideas are living-room scenes (sectional, sofa, fireplace, string-light canopy). Site convention is room-beats-Christmas: christmas-bedroom → Bedroom Decor, christmas-kitchen → Kitchen Decor, christmas-dining-room-decor-ideas → Dining Room Decor. |
| new-year-living-room-decor-ideas | Home Decor | **Living Room Decor** | Title says "Living Room" and all 30 ideas are living-room items (sofa, mantel, coffee table, bar cart, reading nook). Filed under the general category although a specific one fits. |
| christmas-table-decor-ideas | Christmas Decor | **Dining Room Decor** | All 30 ideas are dining-table settings (chargers, runners, centerpieces, place settings). Same room-beats-Christmas convention as above; no "Table" category exists, Dining Room is the closest room. |
| christmas-table | Christmas Decor | **Dining Room Decor** | Same as above — all 30 ideas are a set dining table (chargers, runners, formal/family table settings). |
| doorway-garland | Christmas Decor | **Outdoor Decor** | 24 of 30 ideas are exterior front doors (navy/teal/black/wood front door, double doors, dusk lantern); only ~6 are interior hall/living-room doorways. Title has no "Christmas" in it. Precedent: the Christmas-themed front-door articles (gingerbread-house-door-decorations, -diy) are filed under Outdoor Decor, as is christmas-front-porch-decor-ideas. |

## Format notes (not defects)

- **Inline body images: 24 articles carry images frontmatter-only.** `build.py` ignores inline `![...]` lines and renders one figure per idea from the frontmatter list, so nothing is missing on the live page. Frontmatter-only (0 inline lines): the 20 originals (boho-bedroom, boho-living-room, christmas-bedroom, christmas-dining-room-decor-ideas, christmas-front-porch-decor-ideas, christmas-kitchen, christmas-living-room, christmas-table, christmas-table-decor-ideas, christmas-tree, cozy-christmas, farmhouse-kitchen, farmhouse-living-room, modern-farmhouse, modern-farmhouse-bedroom, neutral-bedroom, rustic-home-decor-ideas, rustic-home-kitchen, small-kitchen-decor-ideas, winter-home) plus 4 transitional Nov-24 articles that DO have 30 tip boxes but no inline images (bathroom-decor-ideas, bookshelf-decor-ideas, hallway-decor-ideas, patio-decor-ideas). The other 38 articles (all dated Nov 25–27) have 30 inline image lines each, matching their frontmatter lists exactly.
- **Tip boxes by generation:** 20 originals (Nov 23–24) have 0 tips by design; the other 42 (4 × Nov 24, 5 × Nov 25, 19 × Nov 26, 14 × Nov 27) have exactly 30. No newer article is missing tips; no original was flagged for having none.
- **Thumbnail files:** every `images/<slug>/` directory holds its 30 article images. 50 directories also contain `thumb.jpg` + `thumb-720.jpg`; 12 do not (2027-home-decor-ideas, 2027-interior-design-trends, bedroom-decor-ideas-2027, cabbage-crush, cabbage-crush-decor, christmas-sunroom-decor-ideas, diy-tree-collar, diy-tree-collar-wood, gallery-wall-ideas-living-room, home-library-lighting-ideas, new-year-bedroom-decor-ideas, new-year-living-room-decor-ideas). These look like build-generated thumbnails, so this is an observation for the build owner, not an article-source defect — no article image is missing.

## Not flagged (borderline, per the brief)

- `christmas-table` / `christmas-table-decor-ideas` vs Dining Room was flagged above on the site-convention argument; the reverse view (Christmas theme is the unifier, as with christmas-tree / stocking-hanging-ideas) is legitimate — the flag is a recommendation, not a proven error.
- `bookshelf-decor-ideas` (Living Room Decor): ideas span office, kitchen, nursery and entryway shelves as well as living-room ones, but bookshelves are most associated with living rooms and no better single category exists — left as-is.
- `valentine-mantel-decor` and `garland-on-mantle` (Home Decor / Christmas Decor): mantels are usually living-room fireplaces, but also occur in bedrooms, and there is no Mantel category — left as-is.
- `winter-window-art` (Christmas Decor): snowflake window art is Christmas-seasonal; no Window category exists — left as-is.
- `christmas-nursery-decor-ideas`, `christmas-sunroom-decor-ideas`, `christmas-laundry-room-decor-ideas` (Christmas Decor): no Nursery / Sunroom / Laundry category exists, so Christmas Decor is the only fit — correct as-is.
- `home-library-lighting-ideas`, `table-decor-ideas`, `afrohemian-decor`, `cabbage-crush`, `cabbage-crush-decor`, `funhaus`, `funhaus-interior`, `neo-deco`, `modern-farmhouse`, `rustic-home-decor-ideas`, `winter-home`, `2027-home-decor-ideas`, `2027-interior-design-trends`, `home-decor-trends-2027` (Home Decor): all genuinely multi-room / whole-home topics — Home Decor is correct.

## Recount (to avoid any double-counting)

- Articles with ≥1 anomaly (15): 2027-home-decor-ideas, 2027-interior-design-trends, bedroom-decor-ideas-2027, cabbage-crush-decor, gallery-wall-ideas-living-room, home-library-lighting-ideas, neo-deco-living-room, new-year-bedroom-decor-ideas (tip rotation); neutral-bedroom (dead link); neutral-kitchen-decor-ideas (FAQ 39 words); christmas-living-room, new-year-living-room-decor-ideas, christmas-table-decor-ideas, christmas-table, doorway-garland (category).
- Articles fully clean (47): all remaining slugs — 2027-christmas-decor-ideas, afrohemian-decor, afrohemian-decor-living-room, bathroom-decor-ideas, bathroom-decor-ideas-2027, bathroom-decor-ideas-apartment, bathroom-decor-ideas-small-spaces, boho-bedroom, boho-living-room, bookshelf-decor-ideas, bookshelf-decor-ideas-for-bedrooms, cabbage-crush, christmas-bedroom, christmas-dining-room-decor-ideas, christmas-front-porch-decor-ideas, christmas-island-centerpiece-ideas, christmas-kitchen, christmas-laundry-room-decor-ideas, christmas-nursery-decor-ideas, christmas-sunroom-decor-ideas, christmas-tree, cozy-christmas, diy-tree-collar, diy-tree-collar-wood, fall-home-decor-ideas-living-rooms, farmhouse-kitchen, farmhouse-living-room, funhaus, funhaus-interior, garland-on-mantle, gingerbread-house-door-decorations, gingerbread-house-door-decorations-diy, hallway-decor-ideas, home-decor-trends-2027, kitchen-decor-ideas-2027, modern-farmhouse, modern-farmhouse-bedroom, neo-deco, patio-decor-ideas, rustic-home-decor-ideas, rustic-home-kitchen, small-kitchen-decor-ideas, stocking-hanging-ideas, table-decor-ideas, valentine-mantel-decor, winter-home, winter-window-art.
- 15 + 47 = 62. ✓
