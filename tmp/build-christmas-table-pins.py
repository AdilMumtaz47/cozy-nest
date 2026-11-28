#!/usr/bin/env python3
"""Build the 3 Christmas Table pins in the Collage Grid style.

Layout (1024x1536, replicating the approved sample pin-style-test/collage-grid.jpg):
- 2x2 grid of real article photos, 512px wide each, thin white centre gutter
- Top row y 0-640, cream title band y 640-896 (dark-green rules top/bottom),
  bottom row y 896-1536.
- Title in dark-green DejaVu Serif Bold, centred in the band, auto-fit to width.
Photos are centre-cropped to the 512x640 cell (0.8 aspect); all sources are
>=768px wide, so cells are downscaled, never upscaled.
"""
import os
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.expanduser("~/workspace/pinterest-blog")
IMG_DIR = os.path.join(BASE, "images/christmas-table")
PIN_DIR = os.path.join(BASE, "images/pins")
PREVIEW_DIR = os.path.expanduser("~/workspace/your_files/christmas-table-pins")

W, H = 1024, 1536
BAND_TOP, BAND_BOTTOM = 640, 896
CELL_W, CELL_H = 512, 640
CREAM = (246, 241, 229)
GREEN = (51, 81, 29)
WHITE = (255, 255, 255)
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"

PINS = [
    {
        "n": 1,
        "photos": [
            "christmas-table-red-green-gold-centerpiece.jpg",      # idea 1 (hero)
            "christmas-table-red-plaid-runner-floral-plates.jpg",   # idea 3
            "christmas-table-family-dinner-tree-fireplace.jpg",     # idea 26
            "christmas-table-gold-vase-rose-centerpiece.jpg",       # idea 30
        ],
        "lines": ["30 Christmas Table Ideas", "for a Festive Dinner"],
    },
    {
        "n": 2,
        "photos": [
            "christmas-table-red-velvet-napkin-gold-charger.jpg",   # idea 6
            "christmas-table-red-roses-gold-runner.jpg",            # idea 7
            "christmas-table-gold-charger-hurricane-candle.jpg",    # idea 8
            "christmas-table-formal-tall-taper-candles.jpg",        # idea 10
        ],
        "lines": ["30+ Christmas Table Ideas", "For Velvet Napkins,",
                  "Gold Chargers and Candlelight"],
    },
    {
        "n": 3,
        "photos": [
            "christmas-table-dinner-served-candlelight.jpg",        # idea 25
            "christmas-table-candlelit-wood-gold-candlesticks.jpg", # idea 24
            "christmas-table-wooden-bowl-pinecone-centerpiece.jpg", # idea 20
            "christmas-table-dried-oranges-amber-glasses.jpg",      # idea 22
        ],
        "lines": ["30+ Christmas Table Ideas", "For Candlelit Christmas Dinners"],
    },
]


def centre_crop(im, tw, th):
    """Crop image to target aspect (centred), then resize to target size."""
    w, h = im.size
    target = tw / th
    if w / h > target:  # too wide: crop width
        nw = int(h * target)
        x0 = (w - nw) // 2
        im = im.crop((x0, 0, x0 + nw, h))
    else:  # too tall: crop height
        nh = int(w / target)
        y0 = (h - nh) // 2
        im = im.crop((0, y0, w, y0 + nh))
    return im.resize((tw, th), Image.LANCZOS)


def fit_font(lines, max_w, start_size):
    size = start_size
    while size > 24:
        font = ImageFont.truetype(FONT_PATH, size)
        widths = [font.getbbox(l)[2] for l in lines]
        if max(widths) <= max_w:
            return font, size
        size -= 2
    return ImageFont.truetype(FONT_PATH, size), size


def build(pin):
    canvas = Image.new("RGB", (W, H), WHITE)
    cells = []
    for i, f in enumerate(pin["photos"]):
        im = Image.open(os.path.join(IMG_DIR, f)).convert("RGB")
        w = CELL_W if i % 2 == 0 else CELL_W - 4  # right column leaves a 4px white gutter
        cells.append(centre_crop(im, w, CELL_H))
    # top row, bottom row (4px white gutter down the middle)
    canvas.paste(cells[0], (0, 0))
    canvas.paste(cells[1], (W // 2 + 4, 0))
    canvas.paste(cells[2], (0, BAND_BOTTOM))
    canvas.paste(cells[3], (W // 2 + 4, BAND_BOTTOM))
    draw = ImageDraw.Draw(canvas)
    # cream band
    draw.rectangle([0, BAND_TOP, W, BAND_BOTTOM], fill=CREAM)
    draw.line([0, BAND_TOP, W, BAND_TOP], fill=GREEN, width=3)
    draw.line([0, BAND_BOTTOM, W, BAND_BOTTOM], fill=GREEN, width=3)
    # title text, centred in the band
    lines = pin["lines"]
    start = 76 if len(lines) == 2 else 60
    font, size = fit_font(lines, W - 84, start)
    line_h = int(size * 1.18)
    total_h = line_h * len(lines)
    y = BAND_TOP + (BAND_BOTTOM - BAND_TOP - total_h) // 2
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        tw = bbox[2] - bbox[0]
        draw.text(((W - tw) / 2, y), line, font=font, fill=GREEN)
        y += line_h
    return canvas


os.makedirs(PIN_DIR, exist_ok=True)
os.makedirs(PREVIEW_DIR, exist_ok=True)
for pin in PINS:
    img = build(pin)
    png = os.path.join(PIN_DIR, f"christmas-table-pin{pin['n']}.png")
    jpg = os.path.join(PREVIEW_DIR, f"pin{pin['n']}.jpg")
    img.save(png)
    img.save(jpg, quality=92)
    print(f"pin{pin['n']}: {img.size} -> {png} + {jpg}")
    print("   photos:", ", ".join(pin["photos"]))
