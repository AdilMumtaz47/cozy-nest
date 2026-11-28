# Pin Style Test Plan — Cozy Nest

Prepared Nov 27, 2026. Adil's ask: "see the way people are making thumbnails for their pins and bring some good ideas so I can choose easily — every group of pins in a different style of thumbnail so we can test which kind of thumbnail attracts more."

## The 6 styles

**Control — Friend's Style (already in use, Cozy Christmas, Nov 28).**
Big number on top flanked by leaf sprigs, script + bold condensed text over a warm room photo, year badge where sensible. The @IndoorDecorHub / Decor Canvas style Adil chose Nov 27. This is the benchmark the new styles must beat.

**1. Photo-Only Editorial** — no text on the image at all; one beautiful sharp photo fills the frame. Different because the photo is the entire pitch. Should work best when the photo itself is the scroll-stopper (a stunning table/room). Sample: `photo-only-editorial` (base: dinner-served-candlelight).

**2. Solid Top Text Band** — a solid deep-green band across the top ~30% carries the headline in bold white serif; the photo fills the bottom ~70% clean. Different because readability is decoupled from the photo — text never fights the image. Should work best for busy photos and small screens. Sample: `top-text-band` (base: red-green-gold centerpiece, idea #1).

**3. Collage Grid** — four different photos in a 2×2 grid with a slim cream title band across the centre. Different because it previews the *variety* inside the listicle instead of one hero shot. Should work best for listicles where several ideas are equally strong. Sample: `collage-grid` (bases: dinner-served-candlelight, red-plaid-runner-floral-plates, poinsettia-lantern-white-table, white-cloth-red-goblets).

**4. Text-Over-Photo** — one single photo filling the whole pin as the background, title laid directly over it, big and filling the image — like the friend's pin (big number on top, script + bold text over the photo, soft cream glow behind the text for readability). Title font is **RED** (deep crimson, Adil's call Nov 27: "make the font in red color rest is absouluty stunning ok"). No bands, no panels, no sprigs, no year badge. Renamed from Centre Panel on Adil's feedback (Nov 27: "not ok i want single image in the background and filled the image with the titile like the image i gave you the refrance of my friends pin") — the solid cream band was the problem. Same photo, same words as the Centre Panel sample. Sample: `text-over-photo` (base: bright-white-woven-placemats).

**5. List Preview** — plain warm-cream background, one small framed photo on top, headline + a numbered list of 4 real idea names from the article. Different because it delivers usable value *inside* the pin — a mini-preview, not just a cover. Should work best for planners/savers. Sample: `list-preview` (photo: red-velvet-napkin-gold-charger, idea #6; ideas #6, #1, #8, #10, verbatim headings).

All 5 samples use the SAME pin text (the exact article title, "30 Christmas Table Ideas for a Festive Dinner") and NO year on the image, so only the design varies. All are 1024×1536, real photos from the christmas-table article, verified (spelling, cut-off, watermark, people, sharpness). PNG masters: `images/pins/style-test/`; JPG q92 previews: `~/workspace/your_files/pin-style-test/`.

## Rotation — which group gets which style

One style per pin group (all 3 pins of a group share the style; the 3 angles/texts from each group's brief stay, only the design changes). Everything else stays constant: same 3 daily slots (5 AM / 11 AM / 5 PM PKT), same board practice, same description style.

| Date | Group (article) | Style |
|---|---|---|
| Nov 28 | Cozy Christmas | Control (friend's style) — done |
| Nov 29 | Christmas Table | **Collage Grid** — Adil's pick (Nov 27, "both are nice") — 3 pins built, Collage Grid style, verified |
| Nov 30 | christmas-table-decor-ideas | **Text-Over-Photo** — Adil's other pick (Nov 27, "both are nice"); remade Nov 27 on his feedback (band rejected — title overlaid directly on the single photo, like the friend's pin) |
| Nov 30 | christmas-living-room | **Top Text Band** |
| Dec 1 | boho-living-room | **Photo-Only Editorial** |
| Dec 1 | christmas-dining-room-decor-ideas | **List Preview** |

Final assignments set Nov 27 by Adil's picks (Collage Grid + Bottom Panel, now Text-Over-Photo) and the parent agent's expert call: the two table articles are near-identical topics on consecutive days, so the Collage Grid vs Text-Over-Photo pair is the cleanest style comparison in the whole test. The remaining three styles fill the Nov 30 / Dec 1 groups in the default order.

## How to measure (and how honest the read is)

Per pin, record from Pinterest Analytics: impressions, outbound clicks, saves, plus CTR (clicks ÷ impressions) and save rate (saves ÷ impressions). Record in a tracking table: style, article, pin #, post date/time, impressions, clicks, saves.

- **First read: 2 weeks after posting** — early and directional only.
- **Verdict: 6–8 weeks** — Pinterest distribution typically builds over the first 90 days; viral pins peak 6–12 months after posting. Do not crown a winner at week 2.
- **Winner =** the best outbound-click rate + save rate across its 3 pins (not raw totals — later groups post into different seasonal demand).
- **Honest limits (tell Adil plainly):** this is directional, NOT a clean A/B test. Topics differ between groups (a Christmas table and a boho living room attract different audiences); the control carries a year badge while the 5 samples do not; the 3 pins in a group share a style but have different angles/photos. A style that wins here is "worth making the default", not proven better in isolation. If the winner and runner-up are close, re-test them head-to-head on two similar topics.

## What happens after

- Winner becomes the default style for later groups; the runner-up stays as the alternate.
- If a style clearly flops (bottom of the table on both clicks and saves), drop it.
- Keep 3 fresh designs per article (different images/angles) — fresh pins drive 90%+ of site traffic; never re-pin the same image.

## Styles considered and NOT tested (and why)

- **Before/After split** — needs a genuine makeover; faking one from listicle stock photos would break the site's real-photos rule. Only if a real before/after article exists.
- **Video pins** — a format change, not a thumbnail style; test separately if video capacity exists (vendor claims ~2× engagement, no published methodology — treat as directional).
- **"X Ways to Y" headlines / Single-Promise Hero** — copy formulas, not layouts; they look identical to the control once placed. Test as headline variants inside a style, not as styles.

## Research behind this (2026, sources)

- GenSumo 148k-pin dataset (2025–early 2026): text overlay (5–8 words) vs image-only = **2.1× outbound clicks overall, 1.6× in home decor**; 2:3 vertical = +45% impressions vs square; light/warm backgrounds = +38% saves vs dark; infographic/text-heavy pins = +22% saves, +28% clicks. https://gensumo.com/research/pinterest-pin-design-report/
- Fresh pins (new image + layout + overlay) drive 90%+ of creator-site traffic (Tailwind 1.2M-pin benchmark). 3–5 visually distinct designs per article.
- Text: 5–8 words, bold/semi-bold, headline 60–72pt equivalent; 15+ words = 29% lower close-up rate; script only for accent words. Contrast ≥ 4.5:1. Keep overlay out of the bottom edge (Direct Links CTA). No thick black/white borders (−9% impressions).
- Judge slowly: distribution builds over 90 days; ~20% of pins show no distribution in week 1; test needs 6–8 weeks minimum (84Pins CTR benchmarks, July 2026).
- Research method note: no live Pinterest browser was available for this pass — findings come from text web search and fetched pages (PinsRank, PinAutopilot, PostEverywhere, GenSumo, 84Pins). The friend's exact pin layout could not be independently verified from text (Pinterest profile returned 403); it rests on the Nov 27 brief + Adil's screenshot. A live-browser look at @IndoorDecorHub pins is still worth doing once to lock the control spec.
