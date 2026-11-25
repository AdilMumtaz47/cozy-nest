# Pinterest Master Record — Cozy Nest (Home Decor)

Check this file BEFORE proposing or screening any new keyword. Never start work
on a keyword/topic already covered here.

## Setup (Section 0)

- **Niche:** Home decor
- **Site name:** Cozy Nest
- **Pinterest account name:** NEW account — Adil creates it himself (old account CLOSED, forget it)
- **Pinterest account URL:** TBD (after creation + warm-up)
- **Pinterest email:** sayedb253@gmail.com (Adil's second email, different from the workflow email)
- **Website URL:** https://cozynesthomeideas.com (Adil's pick, Nov 23, 2026 — to buy: $12.08/yr, or $6.48 first year with NEWCOM648)
- **GitHub org/repo:** TBD (Adil creates the GitHub account himself)
- **Article folder:** `content/posts/`
- **Images folder:** `images/` (article images per slug; pins in `images/pins/`)
- **Claimed website:** no (claim it once the site is live and the new Pinterest account is warmed up)
- **Business account:** yes (new Pinterest account = business account)
- **Gmail (new, for this workflow):** jacksparrowccv7891@gmail.com — GitHub, Vercel, domain, Google Search Console
- **Language:** English

## Status

- **2026-11-23:** Niche decided (home decor). Site name confirmed: **Cozy Nest**. Workflow email: jacksparrowccv7891@gmail.com. Old Pinterest account CLOSED — forget it; Adil creates a NEW Pinterest account himself on a different email. **Adil's schedule (Nov 23, 17:20 PKT): Days 1–5 warm-up (clicks, likes, comments); Days 6–7: 1 article/day → 3 pins; Days 8–20: 2 articles/day → 6 pins; Day 21+: 3 articles/day → 9 pins.** **20-article buffer (Adil, Nov 23, 17:22 PKT): 20 articles must be READY on Muse's side by Day 6 (written, images verified, in the repo) — publishing follows the ramp from the buffer; Muse keeps writing the next ones as it publishes.** Muse's work starts Day 6. Go slowly.
- **Batch 2 keyword screening started Nov 23, 17:22 PKT** (subagent) — 15 more home decor keywords, to reach 20 article topics for the buffer.
- **Batch 2 DONE Nov 23, 17:24 PKT:** 8 STRONG, 5 WINNABLE, 2 REJECTED (winter living room, scandinavian living room). **20-article buffer LOCKED** (keyword-screen-2.md): 17 STRONG + 3 WINNABLE, 9 Christmas / 3 winter / 8 evergreen. Article 1 writing started (subagent): christmas living room decor ideas, images-first per Section 5.3.
- **BLOCKER (changed Nov 23):** old Pinterest account is closed, not coming back. No Pinterest steps until Adil creates the new account AND finishes the warm-up week. Do NOT create a Pinterest account for him — he creates all accounts himself.

- **RESET Nov 23, 18:55 PKT (Adil):** the Google-screened keyword batches and all 10 articles are VOID — from scratch. Pinterest keyword research (autocomplete source, Section 3.1) re-running now; no articles until it is done and Adil says go.
- **PINTEREST RESEARCH DONE Nov 23, 19:19 PKT** (browser, signed in as Cozy Nest, search-only): 40 phrases screened on Pinterest, **27 winnable** (5 STRONG, 22 WINNABLE), 13 fail. Full tables: `keyword-screen-pinterest.md`. Strongest: cozy christmas (1 listicle). Old Google top picks that FAILED on Pinterest: christmas living room decor ideas (saturated), christmas tree decor ideas (saturated), christmas kitchen decor ideas (saturated + 8), christmas bedroom decor ideas (8), cozy winter bedroom ideas (7), farmhouse living room ideas (8), small bedroom decor ideas (8). Winter mantel = men's coats, wrong intent. Distinct topics among the 27: 17 (near-duplicate forms are reserves, not second articles). 3 more topics needed from autocomplete candidates (to be screened first) for a 20-article buffer. **No articles written — awaiting Adil's go.**

- **IMAGE QUALITY RULE CHANGE (Adil, Nov 24, 2026 — overrides the friend's workflow rule):** the workflow's <100,000-byte image cap is LIFTED — it forced heavy compression / small dimensions and made images look blurry on phones. New bar from now on: **no image on the website or Pinterest may look low quality or blurry.** Article photos: portrait, width ≥768px (prefer 1024px when the source offers it), JPEG quality ~80–85, file size as needed for sharpness but kept sensible (target ~120–300KB each, never >400KB, never megabytes). Sharpness judged by LOOKING at the image, not just by numbers. Card thumbnails: 720px wide (q80) served with srcset (360w + 720w) so retina phones get the sharp version and slow connections still get the small one. All 600 article photos are being re-fetched from their original sources at higher resolution (never upscaled) to this bar. Article images are lazy-loaded, so the bigger files do not slow the first paint.

- **IMAGE REWORK COMPLETE + LIVE (Nov 24, 2026, evening — commit e44ac872, 726 files):** all 600 photos re-fetched from their original sources at higher resolution (never upscaled), each visually verified (sharpness, watermark incl. bottom 35% strip, on-topic, no person-as-subject / AI-looking). **139 upgraded, 461 kept** (already sharp at 768px). Per-article: batch-1 Christmas 76 upgraded (biggest), boho group 43, winter group 8, christmas-kitchen group 7, rustic group 5. Final stats: 75.5 MB total (was 52.4), median 96 KB, max 393,733 bytes, 77 images ≥1024px wide. **Could not be fully improved (2):** christmas-dining-room-decor-ideas #17 (720px — source tops out there) and rustic-home-decor-ideas #3 (736px — best clean source) — both noted in their provenance files. Card thumbs now 720px (q80) + srcset (360w/720w). Push took 6 attempts: GitHub's object reads are eventually consistent (same blob sha returned 404, 200, 404 within 30s) — push-site.py now uses nested trees, keep-alive through the sandbox proxy, blob/tree reuse, read-consistency retries, and verify-after-create. **Live verified:** homepage feature + 19 srcset cards, boho-living-room article 30/30 ideas + 8 FAQs + author box, sitemap 28 URLs; byte checks live (boho hero 326,294; christmas-living-room hero 170,264; thumb-720 118,439). Originals backup (pre-rework) kept at ~/workspace/pinterest-blog.rework-backup-20261124/ (outside the site). Follow-up (not blocking): 4 pre-existing cross-article duplicate photo pairs left as-is.

## Covered keywords

**VOID — Google-screened, superseded Nov 23, 18:55 PKT. Do not use. Awaiting Pinterest re-research.**

| Keyword | Listicles / 12 | Verdict | Article slug | Date |
|---|---|---|---|---|
| christmas living room decor ideas | 1/4 | STRONG | christmas-living-room-decor-ideas | 2026-11-23 |
| christmas dining room decor ideas | 1/5 | STRONG | christmas-dining-room-decor-ideas | 2026-11-23 |
| rustic home decor ideas | 1/4 | STRONG | rustic-home-decor-ideas | 2026-11-23 |

## Articles

**RESET Nov 23, 18:55 PKT (Adil: "forget the articles you wrote before — it should be from scratch"):** all 10 Google-keyword articles DELETED (files, images, provenance lists, built pages). Site rebuilt at 0 articles. Keyword research is being redone from scratch on Pinterest (autocomplete source, per workflow Section 3.1). No new articles until that research is done and Adil says go.

**Article 1 WRITTEN from scratch (Nov 23, ~19:30 PKT, after Adil's go-ahead):** keyword "cozy christmas" — Pinterest-verified STRONG (1 listicle, not in autocomplete). 30 real photos, 0 IG / 30 web, all verified full-frame + bottom-35% strip. NOT published (no GitHub/Vercel yet), no pins made.

**Articles 2–5 WRITTEN from scratch (Nov 23, ~19:32–19:42 PKT, after Adil said "yes all 5"):** all Pinterest-verified STRONG keywords, 30 real photos + 8 FAQs each, verified, NOT published, no pins made. Full list in the table below. Site now holds 5 articles / 150 photos, ready for the domain + GitHub/Vercel steps. Next batch (articles 6–10) NOT started — needs Adil's pick from the next-5 shortlist in `next-batch-5.md`; do not write until he says go.

| Slug | Title | Designs | Date published | Live URL |
|---|---|---|---|---|
| cozy-christmas | 30 Cozy Christmas Ideas for a Warm, Glowing Home | 30 | not published yet | — |
| christmas-table | 30 Christmas Table Ideas for a Festive Dinner | 30 | not published yet | — |
| christmas-table-decor-ideas | 30 Christmas Table Decor Ideas for a Warm, Festive Feast | 30 | not published yet | — |
| christmas-living-room | 30 Christmas Living Room Ideas for a Warm, Festive Home | 30 | not published yet | — |
| boho-living-room | 30 Boho Living Room Ideas for a Relaxed, Layered Home | 30 | not published yet | — |

**Articles 6–20 WRITTEN (Nov 24, 2026, evening — 20-article buffer COMPLETE):** all Pinterest-verified keywords (13 from the Nov 23 Pinterest screen + 2 screened Nov 24: modern farmhouse bedroom, rustic home kitchen — both WINNABLE, 6 listicles). Each: 30 real photos (0 IG / 30 web — image-search CLI returned no instagram.com sources), 8 FAQs (40–60 words), verified individually by the coordinator (PIL: JPEG/portrait/<100KB, frontmatter 1:1 with disk, 30 design sections, FAQ heading "Frequently Asked Questions" per the redesigned build.py). `python3 build.py` exit 0: 20 articles, all 30 images / 8 FAQs, built HTML checked (30 figures + 8 FAQ accordions each), sitemap complete. NOT pushed to GitHub yet — parent pushes after this report. Rejected and NOT built: rustic home exterior (7 listicles), modern farmhouse bathroom (8 listicles). Note: `thumb.jpg` in each image folder is a build.py-generated card thumbnail, not a 31st article image. One near-limit image: christmas-tree #8 at 99,987 bytes (still under 100,000).

| Slug | Title | Designs | Date published | Live URL |
|---|---|---|---|---|
| christmas-dining-room-decor-ideas | 30 Christmas Dining Room Decor Ideas for a Warm, Festive Gathering | 30 | not published yet | — |
| boho-bedroom | 30 Boho Bedroom Ideas for a Calm, Layered Retreat | 30 | not published yet | — |
| neutral-bedroom | 30 Neutral Bedroom Ideas for a Calm, Timeless Retreat | 30 | not published yet | — |
| farmhouse-kitchen | 30 Farmhouse Kitchen Ideas for a Warm, Gathered Home | 30 | not published yet | — |
| rustic-home-decor-ideas | 30 Rustic Home Decor Ideas for a Warm, Natural Home | 30 | not published yet | — |
| christmas-bedroom | 30 Christmas Bedroom Ideas for a Cozy, Festive Retreat | 30 | not published yet | — |
| christmas-tree | 30 Christmas Tree Ideas for a Warm, Glowing Holiday | 30 | not published yet | — |
| small-kitchen-decor-ideas | 30 Small Kitchen Decor Ideas for a Charming, Clever Space | 30 | not published yet | — |
| christmas-front-porch-decor-ideas | 30 Christmas Front Porch Decor Ideas for a Warm Welcome | 30 | not published yet | — |
| winter-home | 30 Winter Home Ideas for a Cozy, Snowy Season | 30 | not published yet | — |
| modern-farmhouse | 30 Modern Farmhouse Ideas for a Fresh, Warm Home | 30 | not published yet | — |
| farmhouse-living-room | 30 Farmhouse Living Room Ideas for a Warm, Collected Home | 30 | not published yet | — |
| christmas-kitchen | 30 Christmas Kitchen Ideas for a Warm, Festive Heart of the Home | 30 | not published yet | — |
| modern-farmhouse-bedroom | 30 Modern Farmhouse Bedroom Ideas for a Fresh, Calm Retreat | 30 | not published yet | — |
| rustic-home-kitchen | 30 Rustic Home Kitchen Ideas for a Warm, Natural Heart of the Home | 30 | not published yet | — |

Site now holds 20 articles / 600 photos.

## Boards

| Board name (exact) | Description written | Date created |
|---|---|---|
| Christmas Living Room Decor Ideas | yes (352 chars) | 2026-11-23 |
| Rustic Home Decor Ideas | yes (382 chars) | 2026-11-23 |
| Cozy Winter Bedroom Ideas | yes (389 chars) | 2026-11-23 |

## Pins (published + scheduled)

| Article slug | Pin | Title | Board | Scheduled / published | URL |
|---|---|---|---|---|---|
| (none yet) | | | | | |

## Performance (weekly notes)

| Week | Impressions (30d) | Outbound clicks | Saves | Top clickers / notes |
|---|---|---|---|---|
| (none yet) | | | | |

## Day 1 setup — DONE (Nov 23, 2026, 17:47 PKT)
- **Pinterest profile:** https://www.pinterest.com/cozynestbysayed/ — username **cozynestbysayed**, display name **Cozy Nest**, business account (already was).
- **Bio set:** "Cozy home decor ideas for every room and every season — warm living rooms, calm bedrooms, rustic kitchens and festive touches to make home feel like home."
- **3 boards created** (names + descriptions exact, 0 pins each):
  1. Christmas Living Room Decor Ideas — https://www.pinterest.com/cozynestbysayed/christmas-living-room-decor-ideas/
  2. Rustic Home Decor Ideas — https://www.pinterest.com/cozynestbysayed/rustic-home-decor-ideas/
  3. Cozy Winter Bedroom Ideas — https://www.pinterest.com/cozynestbysayed/cozy-winter-bedroom-ideas/
- No website link added yet (site not live), no profile photo, no pins posted, nobody followed.
- 11 "cozy nest" usernames were taken before cozynestbysayed (cozynest, cozynestdecor, cozynesthome, thecozynest, cozynestliving, cozynesthomedecor, cozynesthaven, cozynestcorner, cozynestdiaries, mycozynestdecor, cozynesthomeliving).
- Note: profile already had 1 pre-existing pin ("Must Know Home Decor Trends for 2027" in Unorganised ideas, saved ~1h before the setup session) — Adil's own save, not added by Muse.
- Warm-up Days 2–5 now: save 5–10 pins/day from other accounts into matching boards, follow a few accounts, no own pins/links yet.

## Redesign — Nesting Oak style, Cozy Nest identity (Nov 24, 2026, evening PKT)
- **Adil:** "make my website like this website, slightly different" — reference https://nestingoak.com/neutral-living-room-ideas/ (visual audit on file in parent chat). Adapted the design language only; no brand, logo, name, text or content copied.
- **Palette:** page warm off-white #f5efe6; content white; header pale cream #f6f3e7; footer pale lemon-cream #f4eeda; primary accent dark olive #425d0b / #485129 (nav bar, all headings, category labels); sage #8d9773 secondary; body text #333333; no blue links. Terracotta #b4552d kept only as a small secondary accent (feature link, chip hover).
- **Header:** pale cream band, centered nest logo + "Cozy Nest" wordmark; below it a full-width solid dark-olive nav bar, white sans-serif links centered (Home + categories), decorative search icon at right (no search backend yet).
- **Article hero:** first photo first, wide 16:9 crop, square corners; white article card overlaps the hero's bottom edge; inside the card: small bold caps olive category label, large bold dark-olive serif H1, small grey date line, Pin-it button, intro, TOC, 30 ideas, FAQ, author box.
- **Article body:** two-column desktop — white article card + right sidebar "Latest Post" (3 stacked items, thumb above olive-serif title); stacks on mobile.
- **Table of Contents:** light-grey box (thin grey border, slightly rounded, 20px padding) after the intro, before idea #1, titled "Table of Contents" with a collapse toggle (details/summary); lists all 30 ideas + FAQ, links black, no doubled numbers.
- **Pinterest:** small solid-red rectangle with white "P" overlapping the top-left corner of the hero, the homepage feature image, and each article photo. "Save this list on Pinterest" button kept. **PIN-IT BUTTON RULE (Adil, Nov 24):** the button currently opens Pinterest's pin creator pre-filled with the article (works with no pins yet), but once pins are published (first pins Nov 28, Day 6), each article's button must link to that article's OWN pin on Pinterest — record each pin URL in the article frontmatter and wire the button to it. The red P badges on photos keep opening the pin creator so visitors can save any photo.
- **Kept:** FAQ accordion (8 FAQs), author box ("About Cozy Nest"), "More like this" box, related as "Similar Posts" image cards, "NN of 30" counters above each H2, thumbs + srcset (360w + 720w), nest logo + wordmark, category pages, sitemap. Footer/author-box wording "made to be saved" (Adil's rule: website says "saved", Pinterest says "pinned" — no "pinned" anywhere in site copy, verified by grep on every build).
- **Footer:** pale lemon-cream band; left nest logo icon only; center nav links in dark-olive sans-serif; right social icons (Facebook, X, Instagram — all link to the Pinterest profile for now, no accounts exist yet) + "Follow on Pinterest" link. Tagline + copyright centered below.
- **Not adapted:** no search backend (icon decorative); no post prev/next navigation; no carousel for Similar Posts (plain 3-card grid). **TIP BOXES DECISION (Adil, Nov 24, "ok as you said"):** per-idea tip/checklist boxes (Nesting Oak-style cream boxes) go on NEW articles only, starting with Neutral Living Room — one box per idea, written as part of the article. The 20 existing articles stay as they are; revisit the back catalog later if the new ones perform well. One box per article was the cheaper alternative, not chosen.
- **LIVE Nov 24, ~19:35 PKT — commit b0348dd5 (727 files).** Verified live: homepage 200 (featured hero + 19 srcset refs + 19 cards + olive nav + footer social + "made to be saved", zero "pinned"); article 200 (hero + TOC 31 entries + 30 item-nums + 9 details + 30 figures + 31 pin badges + 3 sidebar items + Similar Posts + author box, zero "pinned"); sitemap 28 URLs. Push took ~21 min (per-changed-file GET retries against GitHub read-consistency flakes — known cost, script is idempotent).
- **Cleanup:** the internal working note `nesting-oak-comparison-20261124.md` (written 18:47 PKT) was swept into the push because it sat in the site root; it is NOT rendered on the site. Removed from the repo (delete commit 2fe40b05) and preserved at `~/workspace/research_notes/nesting-oak-comparison-20261124.md`. It flags two gaps NOT in this redesign: per-idea "Visual element" tip/checklist boxes (600 blocks for all 20 articles — cost decision for Adil: all-20 vs new-articles-only vs skip) and longer problem-framing intros (cheap on new articles only), plus a catalogue gap: no "Neutral Living Room" article yet (needs a Pinterest screen first per the workflow rule).

## Pin-badge fix + homepage opening — LIVE (Nov 24, 2026, ~19:57 PKT)
- **Bug (Adil clicked it):** every red "P" pin badge was a decorative `<span>`, doing nothing; worse, the homepage feature badge sat INSIDE the article `<a>`, so clicking the P opened the article. Only the "Save this list on Pinterest" button worked.
- **Fix (commit 35e862a9, 726 files):** all badges are now real links to Pinterest's pin creator (`pinterest.com/pin/create/button/?url=…&media=…&description=…`, URL-encoded, `target="_blank" rel="noopener"`). Article pages: 31 badge links each (1 hero + 30 figures; hero pins the first image with the article title, each figure pins its own photo with that idea's title). Homepage feature badge is a SIBLING of the article link (never nested — `.feature` is now `position:relative` so the badge still sits over the image's top-left); `a.pin-badge` CSS keeps the exact look (red rectangle, white P, no underline). "Save this list" button unchanged.
- **Homepage opening (Adil: "i like the second image interface"):** the big hero block (96px logo + "Cozy Nest" H1 + tagline + category chips) is REMOVED from `build_home` — the header already carries logo + name + tag and the nav already lists all 7 categories. Homepage now opens as header band → olive nav bar → featured article immediately. Feature image loads eagerly (`fetchpriority="high"`, no `loading="lazy"`) so no empty cream space while it loads.
- **Verified live:** homepage 200 (no hero-logo/chips/H1, header+nav intact, feature badge is a pin link not nested in the article link, feature img `fetchpriority="high"`); article 200 (31 badge links, 0 spans, pin-btn intact, all URLs valid); sitemap 200 (28 URLs); 0× "pinned". Clicking any red P now opens Pinterest's pin creator for that photo in a new tab.

## Header alignment + nav weight — LIVE (Nov 24, 2026, ~20:20 PKT)
- **Header (Adil: "the logo and name seems not inline centered"):** cause was the brand link holding a two-line text block (name + tag), so the logo centered on the block, not the name line. Fix (commit 0596f71d): brand link now holds ONLY the logo img + "Cozy Nest" name (one inline-flex line, vertically centered); "HOME DECOR IDEAS" moved out into its own block directly below, centered across the full header width (`.brand-tag` display:block, text-align:center; 12px, same color/spacing). Header stays in the pale cream band; nav bar unchanged.
- **Nav weight (Adil sees no bold fonts):** headings were already bold Georgia serif — unchanged. The thin-looking part was the nav links (regular 400). Fix: `.nav-links a` now `font-weight: 600` (semibold). No Google Font or new font family added — Georgia + system sans stay, so no extra download on slow mobile connections.
- **Verified live:** homepage 200 (header: logo + name one line, tag centered below; nav semibold in live CSS; hero still gone, feature img eager, badge link present); article 200 (31 badge links, 0 spans, pin-btn intact, all URLs valid); sitemap 200 (28 URLs); 0× "pinned".

## Header tag refined — LIVE (Nov 24, 2026, ~20:35 PKT)
- **Refinement (Adil, after seeing the header):** first asked to remove "HOME DECOR IDEAS" from under the logo (it repeats what the nav bar says), then refined: KEEP it, but tight under the "Cozy Nest" name. A removal push was started and killed mid-flight (SIGTERM, ~76s in) BEFORE it landed — branch never moved from 0596f71d, so the removal never went live.
- **Final layout (commit 10b5a932, 726 files):** brand link holds logo img + text span, one inline-flex line, vertically centered. Inside the text span: brand-name on top, brand-tag ("HOME DECOR IDEAS") directly beneath it, tight against the name (`.brand-tag` display:block, text-align:left, margin-top:2px; 12px size, color, 1.5px letter-spacing unchanged). NOT centered across the header, NOT in its own block below the unit.
- **Verified live:** homepage 200 (header: logo + name with tag tight underneath, tag appears exactly once; nav, feature, "made to be saved" intact, 0× "pinned"); article 200 (tag once, TOC, 30 counters, 32 pin-create links, pin-btn intact); sitemap 200 (28 URLs); live CSS confirms the `.brand-tag` rule. Tag occurs once per page across the whole built site (28 pages = 20 articles + homepage + 7 category pages).
- **Centering fix (Adil, Nov 24, 20:32 PKT — "HOME DECOR IDEAS is not exactly centered under the Cozy Nest"):** tag was left-aligned under the name, so its centre sat left of the name's centre. Fix (commit bd5a30cd, 726 files): `.brand-tag` text-align:left → center, so the tag centres exactly under "Cozy Nest" within the name-width span. Verified live: homepage 200, tag once, live CSS shows text-align:center; article 200; sitemap 200 (28 URLs); 0× "pinned".

## 4 new articles with per-idea tip boxes — LIVE (Nov 24, 2026, ~21:30 PKT)

- **Topics (Adil: "Write all four"):** fresh Pinterest screen #2, Nov 24 evening — all four WINNABLE, no STRONG: hallway decor ideas (4 listicles), bathroom decor ideas (5), patio decor ideas (6), bookshelf decor ideas (6). Neutral Living Room was REJECTED the same evening (12/10/7 listicles), so the tip boxes debut on these four instead.
- **New articles:** hallway-decor-ideas ("30 Hallway Decor Ideas for a Warm First Impression", Home Decor), bathroom-decor-ideas ("30 Bathroom Decor Ideas for a Calm, Spa-Like Retreat", Home Decor), patio-decor-ideas ("30 Patio Decor Ideas for Relaxed Outdoor Living", Outdoor Decor), bookshelf-decor-ideas ("30 Bookshelf Decor Ideas for a Collected, Lived-In Look", Living Room Decor). Each: 30 ideas, 30 real photos (0 IG / 30 web), 8 FAQs (40–60 words), 30 tip boxes. Cross-links: hallway → farmhouse living room + christmas front porch; bathroom → neutral bedroom + modern farmhouse bedroom; patio → christmas front porch + winter home; bookshelf → boho living room + farmhouse living room. Existing articles' cross-links untouched. No new categories — still 7, so sitemap is now 32 URLs (24 articles + homepage + 7 categories).
- **TIP-BOX FORMAT (implemented in build.py + styles.css, unit-tested before the builders started):** markdown markers in article bodies, rendered as pale warm-cream callout boxes (`.tip-box`, #fbf7ec bg, olive left border, emoji-led) after each idea's paragraphs. Rotation by idea number: n%3==1 `> TIP:QUICK: <1-2 sentences>` ("💡 Quick Tip:"), n%3==2 `> TIP:CHECK: item; item; item` ("✅ Before you buy" + bullets), n%3==0 `> TIP:GUIDE: Label: value | Label: value | Label: value` ("Quick guide", exactly 3 columns, stacks on mobile). 10 of each per article. Format documented in content/posts/_template.md. The 20 existing articles have NO tip boxes (Adil's decision: new articles only).
- **Photos (Nov 24 quality bar — the <100,000-byte cap stays LIFTED):** all 120 JPEG portrait, quality ~82, <400,000 bytes, width ≥768px except 8 noted exceptions, never upscaled: hallway 6 (575–736px), bathroom 1 (562px, towel warmer), patio 1 (765px, side table — widest portrait crop possible from its source). Bookshelf: none. All visually verified full-frame + bottom 35% strip; defects caught and replaced (bookshelf: Pinterest lens button baked into a corner; patio: a "© www.plusmood.com" watermark + a 404 source; bathroom: 9 first picks rejected incl. one ChatGPT_Image and one Gemini_Generated_Image candidate). Provenance lists: hallway/bathroom/patio/bookshelf-decor-ideas-image-list.md.
- **PUSH SAGA:** first push attempt killed by SIGTERM after ~94 min with nothing landed (branch stayed at bd5a30cd, live site unchanged — the script prints progress only at the end when piped through tail). Re-run with full output logged to /tmp/push4.log landed in ~15 min (blob reuse from the killed run): **commit c70095f7e4a716abfbf07a5160906a8005627ea1, 866 files on main**.
- **Verified live:** all 4 article pages 200 (30 figures, 30 tip boxes, 8 FAQ accordions, 30 item-nums, TOC, pin button + 32 pin-create links, 0× "pinned"); homepage 200 (23 cards + feature, all 4 new slugs present, 0× "pinned"); sitemap 200 (32 URLs, all 4 new slugs). Site now 24 articles total.

## 4 new articles (screen #3) — LIVE (Nov 25, 2026, ~13:45 PKT)

- **Topics (Adil: "Write all five"):** fresh Pinterest screen #3, Nov 25 midday — 1 STRONG + 4 WINNABLE: bookshelf decor ideas for bedrooms (3 listicles, STRONG), bathroom decor ideas apartment (5), bathroom decor ideas small spaces (6), gallery wall ideas living room (6), fall home decor ideas living rooms (6). **Only 4 of the 5 were built:** the bookshelf-bedrooms re-check could NOT be performed — it needs the signed-in Pinterest session in the main browser, which the build coordinator (subagent) cannot reach. Its "exact phrase absent" call stays unconfirmed (autocomplete dropdown came up blank twice in screen #3; the 3-listicle count is solid). Do the browser re-check before building it: if the exact phrase IS in autocomplete, the article is REJECTED; if the dropdown is blank again, proceed on the 3-listicle count.
- **New articles:** bathroom-decor-ideas-apartment ("30 Bathroom Decor Ideas for Apartments", Home Decor), bathroom-decor-ideas-small-spaces ("30 Bathroom Decor Ideas for Small Spaces", Home Decor), gallery-wall-ideas-living-room ("30 Gallery Wall Ideas for Living Rooms", Living Room Decor), fall-home-decor-ideas-living-rooms ("30 Fall Home Decor Ideas for Living Rooms", Living Room Decor). Each: 30 ideas, 30 real photos (0 IG / 30 web), 8 FAQs (40–60 words), 30 tip boxes (10 QUICK / 10 CHECK / 10 GUIDE, existing format unchanged). Cross-links: both bathroom articles link to each other AND to bathroom-decor-ideas (the apartment article's small-spaces link was added by the coordinator after the sibling landed — the builder had skipped it as a dead link); gallery wall → boho living room + farmhouse living room; fall living rooms → winter home + christmas living room. Existing articles' cross-links untouched. No new categories — still 7, so sitemap is now 36 URLs (28 articles + homepage + 7 categories).

- **CATEGORY RULE (Adil, Nov 25):** every article goes in its most specific relevant category (room/topic, e.g. Bathroom Decor, Hallway Decor) — never file a room-specific article under generic "Home Decor"; "Home Decor" is only for genuinely general topics (modern farmhouse, rustic home, winter home). The nav bar is built from frontmatter by build.py, so it lists every category that has articles. Applied Nov 25: bathroom articles → "Bathroom Decor", hallway → "Hallway Decor" (9 categories after the change).
- **Photos (Nov 24 quality bar — the <100,000-byte cap stays LIFTED):** all 120 JPEG portrait, quality ~80–85, <400,000 bytes, visually verified full-frame + bottom 35% strip. Sub-768px exceptions, never upscaled, all noted in provenance lists: gallery wall 7 (576–750px), fall living rooms 2 (both 736px), bathroom small spaces 1 (736px), bathroom apartment 0. Defects caught and replaced: gallery wall 7 sources (404s, refused connections, landscape crops too narrow); fall living rooms 2 (a site watermark, AI-looking book-spine text); bathroom small spaces 2 (a "WCFW" brand badge on a mirror; Semrush AI-image URLs + a render rejected outright); bathroom apartment 3 sub-768px candidates rejected and replaced. Provenance lists: bathroom-decor-ideas-apartment / bathroom-decor-ideas-small-spaces / gallery-wall-ideas-living-room / fall-home-decor-ideas-living-rooms-image-list.md.
- **Push:** push-site.py as-is, landed first try in ~108 min: **commit 16587a3945059c86ad9fcb0bfca26c243d3e733d, 1006 files on main**.
- **Verified live:** all 4 article pages 200 (30 figures, 30 tip boxes, 9 details = 8 FAQ accordions + TOC, 30 item-nums, TOC, 0× "pinned"); homepage 200 (all 4 new slugs present, 0× "pinned"); sitemap 200 (36 URLs, all 4 new slugs). Site now 28 articles total.
