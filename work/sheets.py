#!/usr/bin/env python3
"""Build labeled contact sheets (12 per sheet) from candidate images for visual verification."""
import json, os, sys
from PIL import Image, ImageDraw

WORK = os.path.expanduser("~/workspace/pinterest-blog/work")

def crop34(im):
    w, h = im.size
    tw = int(h * 0.75)
    if tw <= w:
        x0 = (w - tw) // 2
        return im.crop((x0, 0, x0 + tw, h))
    th = int(w / 0.75)
    y0 = (h - th) // 2
    return im.crop((0, y0, w, y0 + th))

def sheets(slug, indices=None):
    meta = json.load(open(os.path.join(WORK, slug, "cand_meta.json")))
    canddir = os.path.join(WORK, slug, "cand")
    outdir = os.path.join(WORK, slug, "sheets")
    os.makedirs(outdir, exist_ok=True)
    if indices is not None:
        meta = [m for m in meta if m["idx"] in indices]
    per = 12
    for si in range(0, len(meta), per):
        chunk = meta[si:si + per]
        cols, rows = 4, 3
        tw, th = 400, 533
        sheet = Image.new("RGB", (cols * tw, rows * (th + 28)), "white")
        d = ImageDraw.Draw(sheet)
        for j, m in enumerate(chunk):
            try:
                im = Image.open(os.path.join(canddir, m["file"])).convert("RGB")
            except Exception:
                continue
            im = crop34(im).resize((tw, th), Image.LANCZOS)
            x, y = (j % cols) * tw, (j // cols) * (th + 28)
            sheet.paste(im, (x, y + 28))
            d.text((x + 6, y + 6), f"#{m['idx']} {m['w']}x{m['h']}", fill="black")
        fn = os.path.join(outdir, f"sheet-{si//per + 1:02d}.jpg")
        sheet.save(fn, "JPEG", quality=80)
        print(fn, len(chunk), "items")

if __name__ == "__main__":
    sheets(sys.argv[1])
