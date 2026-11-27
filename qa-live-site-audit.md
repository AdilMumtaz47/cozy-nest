# Cozy Nest — Live-Site Audit (read-only)

**Site:** https://www.cozynesthomeideas.com/ — audited with `curl` (and `python3` for JSON) only. No files edited, no build run, no push, no form submitted, nothing clicked that changes state.

**Audit date:** Friday 2026-11-27. Times below are UTC; PKT = UTC+5, so 09:29 UTC = 14:29 PKT.
**Caveat:** another coordinator was editing/pushing this repo during the audit, so the live site may have changed between checks. Each section notes when it was checked.

## Verdict up front

- **Sitemap: 79/79 resolve to 200** (after following redirects) — **zero non-200**. BUT every sitemap URL is non-www and every one 308-redirects to the www canonical. The sitemap does not match the canonical host.
- **Search index: valid JSON, 62 entries**, all 62 article slugs present exactly once, identical set to the sitemap's 62 post slugs. Keys are abbreviated (`t`/`u`/`c`/`i`), not the full words `title`/`url`/`category`/`ideas`.
- **Homepage: 200, 9 sections, 62 cards** — exactly as expected; hero links to `2027-christmas-decor-ideas`; header and footer elements all present; `pinned` appears **0 times**.
- **Category pages: 9/9 return 200**, card counts match the homepage sections exactly.
- **Trust pages: 7/7 return 200, zero placeholder hits**; contact form posts to Formspree; footer on trust pages links to all 7 trust pages.
- **Dead internal links: none** — all 82 distinct internal hrefs from homepage + 9 category + 7 trust pages return 200.
- **Robots: 200, mentions the sitemap. Favicon: 200.**
- **Two real findings:** (1) sitemap lists the non-www host while the live canonical is www (all 79 URLs 308-redirect); (2) the footer's Facebook / X / Instagram icons all link to the same Pinterest profile URL — the Facebook and X icons are mislabelled/mislinked.

## 1. Sitemap

- **Checked:** 2026-11-27 09:29:00 UTC (fetch, 200, 8,647 bytes) and 09:29:13–09:30:47 UTC (status curl of every URL, following redirects); raw no-follow re-check 09:32:03 UTC; `/terms-and-conditions/` individually re-verified 09:30:51 UTC (see note below).
- **URL fetched:** https://www.cozynesthomeideas.com/sitemap.xml → 200.
- **`<loc>` count: 79** (expected 79 — matches). Breakdown: 1 homepage + 9 category pages + 62 posts + 7 trust pages.
- **www vs non-www: all 79 `<loc>` URLs use the NON-www form** (`https://cozynesthomeideas.com/...`); **zero** use `https://www.`.
- **Statuses (following redirects, `curl -L`): 79 × 200, zero non-200.**
- **Raw statuses (no redirect following): 79 × 308**, each redirecting to the identical path on `https://www.cozynesthomeideas.com/`. Spot-check: non-www homepage `308 → https://www.cozynesthomeideas.com/`; www homepage returns 200 directly. So the sitemap's host does not match the live canonical host — every sitemap URL resolves only via a redirect.
- **Method note:** the first sequential loop wrote 78 status lines because the URL list's last line (`/terms-and-conditions/`) had no trailing newline and the `while read` loop skipped it. That URL was curled separately at 09:30:51 UTC: `200 https://www.cozynesthomeideas.com/terms-and-conditions/` (and it is included in the 79 × 308 raw re-check). No URL was left unchecked.

### Sitemap status table (final status after following redirects; rows in alphabetical order)

| # | URL | Final status |
|---|------------------------------|--------------|
| 1 | https://cozynesthomeideas.com/ | 200 |
| 2 | https://cozynesthomeideas.com/about/ | 200 |
| 3 | https://cozynesthomeideas.com/categories/bathroom-decor/ | 200 |
| 4 | https://cozynesthomeideas.com/categories/bedroom-decor/ | 200 |
| 5 | https://cozynesthomeideas.com/categories/christmas-decor/ | 200 |
| 6 | https://cozynesthomeideas.com/categories/dining-room-decor/ | 200 |
| 7 | https://cozynesthomeideas.com/categories/hallway-decor/ | 200 |
| 8 | https://cozynesthomeideas.com/categories/home-decor/ | 200 |
| 9 | https://cozynesthomeideas.com/categories/kitchen-decor/ | 200 |
| 10 | https://cozynesthomeideas.com/categories/living-room-decor/ | 200 |
| 11 | https://cozynesthomeideas.com/categories/outdoor-decor/ | 200 |
| 12 | https://cozynesthomeideas.com/contact/ | 200 |
| 13 | https://cozynesthomeideas.com/cookie-policy/ | 200 |
| 14 | https://cozynesthomeideas.com/disclaimer/ | 200 |
| 15 | https://cozynesthomeideas.com/editorial-policy/ | 200 |
| 16 | https://cozynesthomeideas.com/posts/2027-christmas-decor-ideas/ | 200 |
| 17 | https://cozynesthomeideas.com/posts/2027-home-decor-ideas/ | 200 |
| 18 | https://cozynesthomeideas.com/posts/2027-interior-design-trends/ | 200 |
| 19 | https://cozynesthomeideas.com/posts/afrohemian-decor-living-room/ | 200 |
| 20 | https://cozynesthomeideas.com/posts/afrohemian-decor/ | 200 |
| 21 | https://cozynesthomeideas.com/posts/bathroom-decor-ideas-2027/ | 200 |
| 22 | https://cozynesthomeideas.com/posts/bathroom-decor-ideas-apartment/ | 200 |
| 23 | https://cozynesthomeideas.com/posts/bathroom-decor-ideas-small-spaces/ | 200 |
| 24 | https://cozynesthomeideas.com/posts/bathroom-decor-ideas/ | 200 |
| 25 | https://cozynesthomeideas.com/posts/bedroom-decor-ideas-2027/ | 200 |
| 26 | https://cozynesthomeideas.com/posts/boho-bedroom/ | 200 |
| 27 | https://cozynesthomeideas.com/posts/boho-living-room/ | 200 |
| 28 | https://cozynesthomeideas.com/posts/bookshelf-decor-ideas-for-bedrooms/ | 200 |
| 29 | https://cozynesthomeideas.com/posts/bookshelf-decor-ideas/ | 200 |
| 30 | https://cozynesthomeideas.com/posts/cabbage-crush-decor/ | 200 |
| 31 | https://cozynesthomeideas.com/posts/cabbage-crush/ | 200 |
| 32 | https://cozynesthomeideas.com/posts/christmas-bedroom/ | 200 |
| 33 | https://cozynesthomeideas.com/posts/christmas-dining-room-decor-ideas/ | 200 |
| 34 | https://cozynesthomeideas.com/posts/christmas-front-porch-decor-ideas/ | 200 |
| 35 | https://cozynesthomeideas.com/posts/christmas-island-centerpiece-ideas/ | 200 |
| 36 | https://cozynesthomeideas.com/posts/christmas-kitchen/ | 200 |
| 37 | https://cozynesthomeideas.com/posts/christmas-laundry-room-decor-ideas/ | 200 |
| 38 | https://cozynesthomeideas.com/posts/christmas-living-room/ | 200 |
| 39 | https://cozynesthomeideas.com/posts/christmas-nursery-decor-ideas/ | 200 |
| 40 | https://cozynesthomeideas.com/posts/christmas-sunroom-decor-ideas/ | 200 |
| 41 | https://cozynesthomeideas.com/posts/christmas-table-decor-ideas/ | 200 |
| 42 | https://cozynesthomeideas.com/posts/christmas-table/ | 200 |
| 43 | https://cozynesthomeideas.com/posts/christmas-tree/ | 200 |
| 44 | https://cozynesthomeideas.com/posts/cozy-christmas/ | 200 |
| 45 | https://cozynesthomeideas.com/posts/diy-tree-collar-wood/ | 200 |
| 46 | https://cozynesthomeideas.com/posts/diy-tree-collar/ | 200 |
| 47 | https://cozynesthomeideas.com/posts/doorway-garland/ | 200 |
| 48 | https://cozynesthomeideas.com/posts/fall-home-decor-ideas-living-rooms/ | 200 |
| 49 | https://cozynesthomeideas.com/posts/farmhouse-kitchen/ | 200 |
| 50 | https://cozynesthomeideas.com/posts/farmhouse-living-room/ | 200 |
| 51 | https://cozynesthomeideas.com/posts/funhaus-interior/ | 200 |
| 52 | https://cozynesthomeideas.com/posts/funhaus/ | 200 |
| 53 | https://cozynesthomeideas.com/posts/gallery-wall-ideas-living-room/ | 200 |
| 54 | https://cozynesthomeideas.com/posts/garland-on-mantle/ | 200 |
| 55 | https://cozynesthomeideas.com/posts/gingerbread-house-door-decorations-diy/ | 200 |
| 56 | https://cozynesthomeideas.com/posts/gingerbread-house-door-decorations/ | 200 |
| 57 | https://cozynesthomeideas.com/posts/hallway-decor-ideas/ | 200 |
| 58 | https://cozynesthomeideas.com/posts/home-decor-trends-2027/ | 200 |
| 59 | https://cozynesthomeideas.com/posts/home-library-lighting-ideas/ | 200 |
| 60 | https://cozynesthomeideas.com/posts/kitchen-decor-ideas-2027/ | 200 |
| 61 | https://cozynesthomeideas.com/posts/modern-farmhouse-bedroom/ | 200 |
| 62 | https://cozynesthomeideas.com/posts/modern-farmhouse/ | 200 |
| 63 | https://cozynesthomeideas.com/posts/neo-deco-living-room/ | 200 |
| 64 | https://cozynesthomeideas.com/posts/neo-deco/ | 200 |
| 65 | https://cozynesthomeideas.com/posts/neutral-bedroom/ | 200 |
| 66 | https://cozynesthomeideas.com/posts/neutral-kitchen-decor-ideas/ | 200 |
| 67 | https://cozynesthomeideas.com/posts/new-year-bedroom-decor-ideas/ | 200 |
| 68 | https://cozynesthomeideas.com/posts/new-year-living-room-decor-ideas/ | 200 |
| 69 | https://cozynesthomeideas.com/posts/patio-decor-ideas/ | 200 |
| 70 | https://cozynesthomeideas.com/posts/rustic-home-decor-ideas/ | 200 |
| 71 | https://cozynesthomeideas.com/posts/rustic-home-kitchen/ | 200 |
| 72 | https://cozynesthomeideas.com/posts/small-kitchen-decor-ideas/ | 200 |
| 73 | https://cozynesthomeideas.com/posts/stocking-hanging-ideas/ | 200 |
| 74 | https://cozynesthomeideas.com/posts/table-decor-ideas/ | 200 |
| 75 | https://cozynesthomeideas.com/posts/valentine-mantel-decor/ | 200 |
| 76 | https://cozynesthomeideas.com/posts/winter-home/ | 200 |
| 77 | https://cozynesthomeideas.com/posts/winter-window-art/ | 200 |
| 78 | https://cozynesthomeideas.com/privacy-policy/ | 200 |
| 79 | https://cozynesthomeideas.com/terms-and-conditions/ | 200 |

## 2. Search index

- **Checked:** 2026-11-27 09:29:00 UTC (fetch, 200, 81,885 bytes).
- **URL:** https://www.cozynesthomeideas.com/search-index.json → 200.
- **Valid JSON: yes** — a JSON array.
- **Entries: 62.**
- **Fields:** every entry has all four fields, but under **abbreviated keys, not the full names**: `t` (title), `u` (url), `c` (category), `i` (ideas, a list). All 62 entries have non-empty `t`, `u`, `c` and a non-empty `i` list. No entry is missing any of the four.
- **Ideas per entry:** every entry's `i` list has exactly 31 items (30 numbered ideas + "Key Takeaways").
- **Slugs:** all 62 article slugs appear **exactly once** (62 unique slugs, zero duplicates).
- **Sitemap cross-check:** the set of 62 slugs in the search index is **identical** to the set of 62 post slugs in the sitemap — nothing in one is missing from the other.
- **Entries per category (search index `c` values):** Home Decor 16, Christmas Decor 15, Bedroom Decor 7, Kitchen Decor 7, Living Room Decor 7, Bathroom Decor 4, Outdoor Decor 4, Dining Room Decor 1, Hallway Decor 1 — total 62, matching the homepage section counts.

## 3. Homepage

- **Checked:** 2026-11-27 09:29:00 UTC (fetch, 200, 54,237 bytes); structure analysed 09:30:58 UTC.
- **URL:** https://www.cozynesthomeideas.com/ → **200**.
- **Category sections: 9** (expected 9). **Article cards: 62 total** (expected 62). One `<section class='grid'>` per section; each section's "See all N … ideas" sub-line matches its card count.

| Section | Cards | Sub-line count |
|---------|------:|----------------|
| Christmas Decor | 15 | 15 |
| Home Decor | 16 | 16 |
| Bedroom Decor | 7 | 7 |
| Kitchen Decor | 7 | 7 |
| Living Room Decor | 7 | 7 |
| Bathroom Decor | 4 | 4 |
| Outdoor Decor | 4 | 4 |
| Dining Room Decor | 1 | 1 |
| Hallway Decor | 1 | 1 |

- **Featured hero: present** — one `<section class='feature'>`, labelled "Christmas Decor · Featured", linking to **`/posts/2027-christmas-decor-ideas/`** ("30 2027 Christmas Decor Ideas for a Festive Home"). The same article also appears as the first card in the Christmas Decor section.
- **Header: present and complete** — logo image (`/images/logo.jpg`, alt "Cozy Nest logo", linked to `/`), brand text "Cozy Nest", red Follow button (class `nav-follow header-follow`, CSS `background: #e60023`, text "Follow on Pinterest" / short form "Follow", linking to https://www.pinterest.com/cozynestbysayed/), nav links (Home + all 9 category pages), and a search button (`id="search-open"`, aria-label "Search").
- **Footer: present and complete** — newsletter band (heading "Never miss a new list", email input, "Join" submit button; form posts to `https://formspree.io/f/mljbvkdz`), wordmark "Cozy Nest", social links, and the 3 columns with headings **"Quick Links"**, **"Categories"**, **"Legal"** (title case in the HTML, not all-caps — the all-caps form is presumably a CSS uppercase style). Quick Links: Home, About, Contact, Editorial Policy. Categories: all 9. Legal: Privacy Policy, Terms & Conditions, Disclaimer, Cookie Policy.
- **Social links in footer — FINDING:** there are 4 footer social anchors, all pointing to the **same** URL, https://www.pinterest.com/cozynestbysayed/ — but three of them carry the titles **"Facebook"**, **"X"** and **"Instagram"** (with the Facebook/X/Instagram SVG icons). Only the fourth ("Follow on Pinterest") is labelled correctly. So the Facebook and X icons are mislabelled/mislinked: clicking the Facebook icon takes the visitor to Pinterest, not Facebook. The same Pinterest URL is also the header Follow button's target (correctly labelled there).
- **Grep for "pinned": 0 occurrences** (case-insensitive) in the homepage HTML — as expected. Note: the hero does contain a Pinterest share link (`class='pin-badge'`, `pinterest.com/pin/create/button/`), which is a share button, not the word "pinned".

## 4. Category pages

- **Checked:** 2026-11-27 09:31:14–09:31:17 UTC (parallel fetch).
- **All 9 return 200**, and every page's card count matches its homepage section exactly.

| Category page | Status | Cards | Homepage section count | Match |
|---------------|--------|------:|-----------------------:|-------|
| /categories/bathroom-decor/ | 200 | 4 | 4 | Yes |
| /categories/bedroom-decor/ | 200 | 7 | 7 | Yes |
| /categories/christmas-decor/ | 200 | 15 | 15 | Yes |
| /categories/dining-room-decor/ | 200 | 1 | 1 | Yes |
| /categories/hallway-decor/ | 200 | 1 | 1 | Yes |
| /categories/home-decor/ | 200 | 16 | 16 | Yes |
| /categories/kitchen-decor/ | 200 | 7 | 7 | Yes |
| /categories/living-room-decor/ | 200 | 7 | 7 | Yes |
| /categories/outdoor-decor/ | 200 | 4 | 4 | Yes |

## 5. Trust pages

- **Checked:** 2026-11-27 09:31:14–09:31:17 UTC (parallel fetch); placeholder greps and footer checks run on those same fetches.

| Page | Status | Placeholder hits (lorem / TODO / XXX / "coming soon" / "[insert" / "pinned", case-insensitive) |
|------|--------|------------------------------------------------------------------------------------------------|
| /about/ | 200 | None |
| /contact/ | 200 | None |
| /editorial-policy/ | 200 | None |
| /privacy-policy/ | 200 | None |
| /terms-and-conditions/ | 200 | None |
| /disclaimer/ | 200 | None |
| /cookie-policy/ | 200 | None |

- **Placeholder hits: none on any of the 7 pages.**
- **Contact form: present and posting to Formspree.** `/contact/` contains two forms: the contact form `<form class="contact-form" action="https://formspree.io/f/mljbvvvk" method="POST">` and the footer newsletter form (`https://formspree.io/f/mljbvkdz`). The contact endpoint (`mljbvvvk`) is distinct from the newsletter endpoint (`mljbvkdz`). (No form was submitted — read-only audit.)
- **Footer trust links:** checked on `/about/`, `/contact/` and `/privacy-policy/` — the footer on each links to **all 7 trust pages** (`/about/`, `/contact/`, `/editorial-policy/`, `/privacy-policy/`, `/terms-and-conditions/`, `/disclaimer/`, `/cookie-policy/`). No trust link missing on any of the three pages checked.

## 6. Dead internal links

- **Checked:** link extraction from the 09:29:00 UTC homepage fetch and the 09:31:14–09:31:17 UTC category/trust fetches; status curl 2026-11-27 09:31:30–09:31:36 UTC (parallel, following redirects).
- **Scope:** every `href` starting with `/` in the homepage + all 9 category pages + all 7 trust pages, deduplicated. Article (`/posts/…`) links are included in this count because they appear as hrefs on those pages; no article page content was audited (another auditor covers article pages).
- **Distinct internal hrefs: 82** — 62 posts + 9 categories + 9 pages/other (`/`, `/about/`, `/contact/`, `/cookie-policy`, `/cookie-policy/`, `/disclaimer/`, `/editorial-policy/`, `/privacy-policy/`, `/terms-and-conditions/`) + `/styles.css` + `/favicon.ico`.
- **Result: all 82 return 200. Zero dead internal links.**
- **Note:** `/cookie-policy` (no trailing slash) appears as a distinct href on the `/privacy-policy/` page, alongside the slashed `/cookie-policy/` used in the footer. Both return 200 (the no-slash www URL returns 200 directly; the non-www no-slash URL 308-redirects to the www no-slash URL). Not a failure, just an inconsistency in link form.

## 7. Robots + favicon

- **Checked:** 2026-11-27 09:31:14–09:31:17 UTC.
- **`/robots.txt`: 200** (74 bytes). Contents:
```
User-agent: *
Allow: /
Sitemap: https://cozynesthomeideas.com/sitemap.xml
```
  It mentions the sitemap — but note the sitemap URL given is the **non-www** form, matching the sitemap's own `<loc>` host, not the www canonical.
- **`/favicon.ico`: 200** (6,982 bytes, `image/vnd.microsoft.icon`; a valid multi-size Windows icon resource: 16×16 and 32×32).

## Findings summary (failures / issues only)

1. **Sitemap host ≠ canonical host (all 79 URLs).** Every `<loc>` uses `https://cozynesthomeideas.com/…` (non-www) while the live site's canonical host is `https://www.cozynesthomeideas.com/` — every sitemap URL returns 308 to the www form before returning 200. `robots.txt` also points at the non-www sitemap URL. Fix would be to regenerate the sitemap (and the robots.txt sitemap line) with the www host. Final statuses are all 200, so nothing is broken for visitors; this is a crawl/canonical-consistency issue.
2. **Footer social icons mislabelled/mislinked.** The Facebook, X and Instagram icons in the footer all link to https://www.pinterest.com/cozynestbysayed/ (the Pinterest profile). Only the "Follow on Pinterest" link is labelled correctly. If there are no Facebook/X/Instagram profiles, those icons should be removed or replaced with the Pinterest link labelled as Pinterest; if the profiles exist, the hrefs should point at them.
3. **Minor, not a failure:** the search index uses abbreviated keys (`t`/`u`/`c`/`i`) rather than `title`/`url`/`category`/`ideas` — fine as long as the site's search JS reads the abbreviated form (it evidently does, since the fields are consistently present); flagging only so nobody "fixes" it by renaming keys without updating the JS. Also, `/privacy-policy/` links to `/cookie-policy` without a trailing slash while the footer uses `/cookie-policy/` — both work, just inconsistent.

Everything else checked passed: sitemap 79/79 final-200, search index 62/62 slugs exactly once and identical to the sitemap set, homepage 9 sections / 62 cards, hero present, header/footer complete, `pinned` 0×, category counts match, trust pages 200 with no placeholders, contact form posts to Formspree (`formspree.io/f/mljbvvvk`), footer links all 7 trust pages, 82/82 internal hrefs 200, robots 200 with sitemap line, favicon 200.

