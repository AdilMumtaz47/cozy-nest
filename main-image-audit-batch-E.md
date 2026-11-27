# Main Image Audit — Batch E

Audit of the first (main) image of each assigned article. Read-only audit; no files were edited.
Site: `~/workspace/pinterest-blog/`. Main image = first entry of the frontmatter `images:` list in `content/posts/<slug>.md`.
Rule: REPLACE if width < 768px, or blurry/soft, or dull/dark/empty, or weak in the 16:9 hero middle-band crop.

| slug | first image file | first image width | verdict | reason | replacement file + idea number + width |
|---|---|---|---|---|---|
| kitchen-decor-ideas-2027 | kitchen-decor-ideas-2027-white-shaker-cabinets.jpg | 1024 | KEEP | Bright, sharp white shaker kitchen; cabinets, backsplash and fruit bowl fill the 16:9 middle band well. | — |
| modern-farmhouse | modern-farmhouse-shiplap-fireplace-armchairs.jpg | 896 | KEEP | Bright, sharp shiplap fireplace with lit fire and armchairs; inviting, subject centred in the middle band. | — |
| modern-farmhouse-bedroom | modern-farmhouse-bedroom-shiplap-dark-beams.jpg | 768 | KEEP | Sharp, bright bedroom; bed, reclaimed-wood headboard and beams sit in the middle band. | — |
| neo-deco | neo-deco-emerald-velvet-sofa.jpg | 896 | KEEP | Sharp, striking emerald velvet sofa against black-and-gold deco panelling; sofa fills the middle band. | — |
| neo-deco-living-room | neo-deco-living-room-black-and-gold.jpg | 896 | KEEP | Sharp, bold black curved sofa with gold fan wallpaper; dark by design but high-contrast and eye-catching, sofa in the middle band. | — |
| neutral-bedroom | neutral-bedroom-cream-bedding-drum-pendant.jpg | 768 | KEEP | Bright, sharp cream bedroom; bed and pendant centred, inviting, works in the middle band. | — |
| neutral-kitchen-decor-ideas | neutral-kitchen-decor-ideas-white-shaker-wood-island.jpg | 768 | KEEP | Bright, sharp white kitchen; wood island with flowers centred in the middle band. | — |
| new-year-bedroom-decor-ideas | new-year-bedroom-decor-ideas-white-bedding-reset.jpg | 459 | REPLACE | Only 459px wide (fails the 768px minimum) and visually plain: white pillows against a white wall, empty and washed-out, no decor interest. | new-year-bedroom-decor-ideas-champagne-metallic-throw.jpg — idea 8 — 1024px |
| new-year-living-room-decor-ideas | new-year-living-room-decor-ideas-gold-balloon-cluster-sofa.jpg | 683 | REPLACE | Only 683px wide (fails the 768px minimum); the balloon shot itself is festive, but width alone fails it. | new-year-living-room-decor-ideas-gold-silver-bauble-mantel-garland.jpg — idea 4 — 848px |
| patio-decor-ideas | patio-decor-ideas-string-lights-evening.jpg | 1024 | KEEP | Sharp, gorgeous dusk patio with glowing string lights across the middle band; inviting and eye-catching. | — |
| rustic-home-decor-ideas | rustic-home-decor-ideas-open-wood-shelves-kitchen.jpg | 896 | KEEP | Bright, sharp rustic kitchen; open wood shelves, copper pots and window light fill the middle band. | — |

## Replacement notes

- **new-year-bedroom-decor-ideas → idea 8, `new-year-bedroom-decor-ideas-champagne-metallic-throw.jpg` (1024px):** sharp, bright, full frontal bed in champagne-gold metallic bedding with matching pillows, mirrored nightstands, lamps and framed art — bold, unmistakably New Year, symmetrical composition survives the 16:9 middle-band crop. Runner-up: idea 6 warm fairy lights (819px), warm and glowing but darker overall.
- **new-year-living-room-decor-ideas → idea 4, `new-year-living-room-decor-ideas-gold-silver-bauble-mantel-garland.jpg` (848px):** sharp, bright frontal fireplace with a lit fire, gold-and-silver bauble garland, round mirror and gifts — festive, clear subject, garland and fire sit in the 16:9 middle band. Runner-up: idea 3 gold-white countdown mantel (896px), also glowing and festive but a tighter side-angle mantel close-up.

## Summary

- KEEP: 9 of 11
- REPLACE: 2 of 11 — new-year-bedroom-decor-ideas, new-year-living-room-decor-ideas (both failed on width < 768px; the bedroom one was also plain/empty)
- No files were edited; replacements are picks only, to be applied in the separate swap step.
