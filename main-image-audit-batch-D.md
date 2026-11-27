# Main Image Audit — Batch D

Audit-only review of the first (main) image of each article: width measured with PIL, visual inspection for sharpness, eye-catchiness, and the 16:9 middle-band hero crop. REPLACE if width < 768px, blurry/soft, dull/dark/empty, or weak in the 16:9 crop. Replacements are picked from within the same article only. No files were edited.

| slug | first image file | first image width | verdict | reason | replacement file + idea number + width |
|---|---|---|---|---|---|
| farmhouse-kitchen | farmhouse-kitchen-white-cabinets-butcher-block.jpg | 768 | KEEP | Sharp, bright, inviting; white cabinets + butcher block fill the middle band well | — |
| farmhouse-living-room | farmhouse-living-room-slipcovered-sofa-pair-wood-table.jpg | 900 | KEEP | Sharp, warm, inviting; sofas, wood table and hydrangeas sit in the middle band | — |
| funhaus | funhaus-rainbow-kitchen-cabinets.jpg | 768 | KEEP | Sharp, very bright and bold; rainbow cabinets fill the frame and the middle band | — |
| funhaus-interior | funhaus-interior-living-room-color-drenched-sofa-wall.jpg | 768 | KEEP | Sharp, bright pink sofa + color-blocked wall; strong middle band | — |
| gallery-wall-ideas-living-room | gallery-wall-ideas-living-room-symmetrical-grid-sofa.jpg | 683 | REPLACE | Width 683px is under the 768px minimum (image itself is sharp and pleasant) | gallery-wall-ideas-living-room-black-white-photo-gallery.jpg — idea 3 — 1024px wide |
| garland-on-mantle | garland-on-mantle-classic-stockings-wreath.jpg | 1024 | KEEP | Sharp, warm and festive; lit garland, wreath and stockings fill the middle band | — |
| gingerbread-house-door-decorations | gingerbread-house-door-decorations-full-facade.jpg | 1024 | KEEP | Sharp, colorful and eye-catching; door + peppermint wreath sit in the middle band | — |
| gingerbread-house-door-decorations-diy | gingerbread-house-door-decorations-diy-peppermint-wreath.jpg | 1024 | KEEP | Sharp, bright peppermint wreath fills the frame and the middle band | — |
| hallway-decor-ideas | hallway-decor-ideas-console-table-mirror-wood.jpg | 1024 | KEEP | Sharp, bright and inviting; mirror, console and vase sit in the middle band | — |
| home-decor-trends-2027 | home-decor-trends-2027-warm-earthy-terracotta-living-room.jpg | 768 | KEEP | Sharp, warm and inviting; terracotta sofa + live-edge table fill the middle band | — |
| home-library-lighting-ideas | home-library-lighting-ideas-brass-desk-lamp-open-book.jpg | 1000 | REPLACE | Sharp lamp but the frame is dark/moody overall; the 16:9 middle band is mostly dark bookshelves and reads dull as a hero/card | home-library-lighting-ideas-floor-lamp-reading-chair.jpg — idea 2 — 1024px wide |

## Summary

- **KEEP: 9** — farmhouse-kitchen, farmhouse-living-room, funhaus, funhaus-interior, garland-on-mantle, gingerbread-house-door-decorations, gingerbread-house-door-decorations-diy, hallway-decor-ideas, home-decor-trends-2027
- **REPLACE: 2** — gallery-wall-ideas-living-room (683px, under minimum), home-library-lighting-ideas (too dark for hero/card)

## Replacement notes

- **gallery-wall-ideas-living-room → idea 3** (`gallery-wall-ideas-living-room-black-white-photo-gallery.jpg`, 1024px): bright, sharp, clean symmetrical black-and-white photo grid above a white sectional sofa — same lead idea as the original, works well in the 16:9 middle band (frames + sofa). Also considered: idea 2 salon-style eclectic mix (800px, colorful, orange sofa) and idea 5 gallery above fireplace (896px).
- **home-library-lighting-ideas → idea 2** (`home-library-lighting-ideas-floor-lamp-reading-chair.jpg`, 1024px): warm glowing floor lamp beside a tufted reading chair with full bookshelves behind — bright, inviting, directly shows a library lighting idea, strong middle band. Also considered: idea 25 sunlight library window (1024px, golden sunbeams) and idea 7 crystal chandelier paneled library (1024px).
