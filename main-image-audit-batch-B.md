# Main Image Audit — Batch B

Audited 2026-11-27 (read-only). Each article's first `images:` entry in `content/posts/<slug>.md` was measured and visually inspected for sharpness, eye-catchiness, and the 16:9 hero middle-band crop. Width under 768px fails on its own.

| slug | first image file | first image width | verdict | reason | replacement file + idea number + width |
|---|---|---|---|---|---|
| boho-living-room | boho-living-room-macrame-kilim-pillows.jpg | 1024 | KEEP | Sharp, bright, colourful; sofa + macrame + kilim pillows fill the hero band well. | — |
| bookshelf-decor-ideas | bookshelf-decor-ideas-books-by-color-rainbow.jpg | 1024 | KEEP | Sharp, very colourful rainbow shelves; striking as hero and card, works in any crop. | — |
| bookshelf-decor-ideas-for-bedrooms | bookshelf-decor-ideas-for-bedrooms-floating-shelves-above-bed.jpg | 1024 | KEEP | Sharp, warm and inviting; bed + floating shelves fill the middle band. | — |
| cabbage-crush | cabbage-crush-sage-green-kitchen-open-shelves.jpg | 750 | REPLACE | Width 750px < 768px (fails on size; visually fine, sharp and bright). | cabbage-crush-dining-room-green-panelled-walls.jpg, idea 13, 1024px |
| cabbage-crush-decor | cabbage-crush-decor-sage-green-accent-wall-living-room.jpg | 750 | REPLACE | Width 750px < 768px; also pale/muted with a large empty wall in the hero band. | cabbage-crush-decor-botanical-print-gallery-wall.jpg, idea 2, 896px |
| christmas-bedroom | christmas-bedroom-plaid-bedding-wreath-garland.jpg | 768 | KEEP | Sharp, warm and festive; plaid bed, wreath and tree fill the hero band. | — |
| christmas-dining-room-decor-ideas | christmas-dining-room-decor-ideas-long-wooden-table-greenery-runner.jpg | 1024 | KEEP | Sharp, warm, festive long table with red/green runner and candles; strong middle band. | — |
| christmas-front-porch-decor-ideas | christmas-front-porch-decor-ideas-snowy-porch-dusk-garland.jpg | 1024 | KEEP | Sharp, glowing dusk porch; red door, wreath, garland and snow fill the hero band. | — |
| christmas-island-centerpiece-ideas | christmas-island-centerpiece-ideas-garland-runner-cookies-candles.jpg | 768 | KEEP | Sharp and bright; cookie stand, ornament bowl and garland fill the middle band. | — |
| christmas-kitchen | christmas-kitchen-red-green-garland-cabinets.jpg | 864 | KEEP | Sharp, bright and festive; garland, red ornaments and cabinets fill the hero band. | — |
| christmas-laundry-room-decor-ideas | christmas-laundry-room-decor-ideas-wreath-on-the-door.jpg | 896 | KEEP | Sharp and bright; wreath on the door is centred in the hero band, with garland and red rug. | — |

## Summary

- **KEEP: 9** — boho-living-room, bookshelf-decor-ideas, bookshelf-decor-ideas-for-bedrooms, christmas-bedroom, christmas-dining-room-decor-ideas, christmas-front-porch-decor-ideas, christmas-island-centerpiece-ideas, christmas-kitchen, christmas-laundry-room-decor-ideas.
- **REPLACE: 2** — cabbage-crush, cabbage-crush-decor (both first images 750px wide, under the 768px bar).

## Replacement notes

- **cabbage-crush → idea 13, `cabbage-crush-dining-room-green-panelled-walls.jpg` (1024px):** bright, sharp, vivid green panelled dining room with crystal chandelier, set round table and green velvet chairs; the 16:9 middle band holds the chandelier, greenery centrepiece and set table. Runner-up: idea 3, `cabbage-crush-dining-room-dark-botanical-wallpaper.jpg` (1024px) — more dramatic/darker; idea 6, `cabbage-crush-kitchen-botanical-print-gallery.jpg` (1024px) — sunny alternative.
- **cabbage-crush-decor → idea 2, `cabbage-crush-decor-botanical-print-gallery-wall.jpg` (896px):** bright, sharp and fresh — botanical print gallery wall above a sage green sofa with a fiddle-leaf plant; the 16:9 middle band is full of prints and sofa, and it represents the article's core ideas (botanical prints + green textiles) in one shot. Runner-up: idea 3, `cabbage-crush-decor-green-velvet-armchair.jpg` (1024px) — bolder emerald armchair, darker/moodier; idea 12, `cabbage-crush-decor-green-built-in-bookshelves.jpg` (1024px).

## Method

- First-image widths measured with PIL from the files in `images/<slug>/`.
- All 11 first images visually inspected. For the 2 REPLACE articles, 7 other photos each were visually inspected (all ≥768px candidates shortlisted by width and subject) before picking the replacement; replacements come from within the same article, no web fetches.
- No files were edited.
