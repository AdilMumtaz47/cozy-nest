# Nesting Oak vs Cozy Nest — what "like this" means (prepared 2026-11-24, ~18:47 PKT)

Adil sent this link at 2026-11-24 13:45 UTC (18:45 PKT) with "i want website like this":
https://nestingoak.com/neutral-living-room-ideas/?utm_source=Pinterest&utm_medium=organic

## Status update — read the MEMORY.md change that landed during this run

- **IMAGE REWORK COMPLETE + LIVE (Nov 24, 18:48 PKT):** all 600 photos re-fetched at
  higher resolution, live commit e44ac87. The "upload still pending" status from the
  13:37 UTC chat update is now superseded — the sharp photos ARE live.
- **REDESIGN IN PROGRESS (Adil, Nov 24):** rebuild Cozy Nest in the Nesting Oak style
  — warm cream bg (#f5efe6), white article card, dark-olive nav bar (#425d0b) + olive
  serif headings, hero photo above a title card, TOC box, red Pinterest pin button on
  photos, sidebar "Latest Post", Similar Posts cards — SLIGHTLY DIFFERENT, keeping
  Cozy Nest's nest logo + own identity (no copying their brand/content). Next: first
  publish day Nov 28 (Day 6).
- So this note is NOT a proposal to start a redesign — it is the checked comparison
  behind the redesign already underway, plus the two Nesting Oak elements the current
  redesign spec does not cover, and one catalogue gap.

## What Nesting Oak's article actually is (read live 2026-11-24 13:45 UTC)

- WordPress listicle: "20 Neutral Living Room Ideas That Feel Warm, Calm and Inviting"
- 20 ideas (not 30). Portrait photos, 683x1024 WebP, one per idea.
- Intro: 3 short paragraphs framing the problem (neutral rooms can feel flat).
- **Table of Contents** listing all 20 ideas, right after the intro.
- Each idea: numbered H2 + photo + 2 paragraphs, PLUS a **"Visual element" box** that
  changes per idea — a quick-guide card with emoji icons, a "Quick Tip" callout, a
  comparison table, a checklist, a before/after, or numbered steps.
- Ends with a Conclusion + "Save these neutral living room ideas to your Pinterest
  boards" line. Shows Published 2025-09-06 and Updated 2026-11-10.
- No FAQ section and no author box visible in the extracted page text.

## What Cozy Nest already has (read live 2026-11-24 13:47 UTC)

Checked against the closest match, "30 Neutral Bedroom Ideas for a Calm, Timeless Retreat"
(https://www.cozynesthomeideas.com/posts/neutral-bedroom/):

- 30 ideas per article (more than Nesting Oak's 20) — keep this, do not shrink to 20.
- "01 of 30" counters, 2 paragraphs per idea, Pin-it button at the top, "More like
  this" after idea 3, "You may also like" 3-card grid at the end, About Cozy Nest
  author box, Takeaway closer.
- **8 FAQs per article** (visible accordion + FAQPage JSON-LD) — Nesting Oak has none.
  This is already a Cozy Nest advantage; do not drop it to copy Nesting Oak.
- Photos now rebuilt to the Nov 24 quality bar (portrait, width >=768px, JPEG q80-85)
  — wider/sharper than Nesting Oak's 683px images. Do not copy their smaller size.

## What Cozy Nest does NOT have — the real gaps

1. **No Table of Contents.** `build.py` `build_article()` (~/workspace/pinterest-blog/build.py,
   lines 218-308) generates no TOC. This is the cheapest win: a TOC can be
   auto-generated from the existing H2 titles in the template — no new content to
   write, one rebuild of all 20 articles.
2. **No per-idea tip/checklist box.** Nesting Oak has one "Visual element" box per
   idea. Cozy Nest has none. Copying this for all 20 articles = 600 new content
   blocks (20 x 30) — the expensive part. Realistic options: (a) skip it, (b) add it
   only to NEW articles going forward, (c) add one short tip box per article instead
   of per idea.
3. **Shorter intro.** Cozy intros are 2 paragraphs; Nesting Oak's is 3 with a clearer
   problem frame. Cheap to lengthen on new articles; rewriting 20 live intros is
   medium work.
4. **No "Neutral Living Room" article at all.** Cozy Nest's 20 live articles include
   farmhouse / boho / Christmas living rooms, but no neutral living room. The exact
   topic Adil linked is a gap in the catalogue.

## What "like this" should NOT mean

- Do NOT migrate to WordPress — Cozy Nest is a static site (build.py + Vercel);
  rebuilding on WordPress would be a full rebuild for no reader benefit.
- Do NOT cut articles from 30 ideas to 20, drop the FAQ, or shrink photos to 683px.
- Do NOT write the Neutral Living Room article yet: "neutral living room" /
  "neutral living room ideas" was never screened in
  ~/workspace/pinterest-blog/keyword-screen-pinterest.md (only "neutral bedroom"
  was screened: WINNABLE, 4-6 listicles). The workflow rule is Pinterest
  search/autocomplete only, never Google — screen it on Pinterest first, then build.

## Suggested decision for Adil (3 questions, in order)

1. TOC on all 20 articles? — small template change, ships with the next rebuild.
   (Can ride along with the sharp-photo rework push that is still pending.)
2. Per-idea tip boxes: all 20 articles, new articles only, or skip? — this is the
   cost decision; all-20 is the big one (600 blocks).
3. Next article = "Neutral Living Room Ideas" after a Pinterest screen? — fills the
   exact topic he linked; needs the Pinterest check first per the workflow rule.

## Timing / dependencies

- Photo rework is LIVE (commit e44ac87, 18:48 PKT) — no longer pending.
- First publish day is Nov 28 (Day 6). A TOC change before then is clean; per-idea
  boxes across 20 articles would not be ready by then.
- The two Nesting Oak elements NOT in the current redesign spec: per-idea visual
  boxes (600 blocks — the expensive one; suggest new-articles-only or skip) and a
  longer problem-framing intro (cheap on new articles only).
