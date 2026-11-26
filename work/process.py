#!/usr/bin/env python3
"""Process selected candidates into final article images (portrait 3:4, JPEG q~82, <400KB)."""
import json, os, sys
from PIL import Image

WORK = os.path.expanduser("~/workspace/pinterest-blog/work")
BLOG = os.path.expanduser("~/workspace/pinterest-blog")

def crop34(im):
    w, h = im.size
    tw = int(h * 0.75)
    if tw <= w:
        x0 = (w - tw) // 2
        return im.crop((x0, 0, x0 + tw, h))
    th = int(w / 0.75)
    y0 = (h - th) // 2
    return im.crop((0, y0, w, y0 + th))

def process(slug, sel):
    meta = {m["idx"]: m for m in json.load(open(os.path.join(WORK, slug, "cand_meta.json")))}
    canddir = os.path.join(WORK, slug, "cand")
    outdir = os.path.join(BLOG, "images", slug)
    os.makedirs(outdir, exist_ok=True)
    report = []
    for item in sel:
        idx = item["idx"]
        m = meta[idx]
        im = Image.open(os.path.join(canddir, m["file"])).convert("RGB")
        im = crop34(im)
        w, h = im.size
        if w >= 1024:
            tw = 1024
        elif w >= 768:
            tw = 768
        else:
            tw = w  # sub-768 exception: never upscale
        im = im.resize((tw, int(tw * 4 / 3)), Image.LANCZOS)
        out = os.path.join(outdir, item["file"])
        q = 82
        im.save(out, "JPEG", quality=q, optimize=True)
        while os.path.getsize(out) > 400000 and q > 55:
            q -= 7
            im.save(out, "JPEG", quality=q, optimize=True)
        sz = os.path.getsize(out)
        report.append({"idx": idx, "file": item["file"], "w": tw, "h": int(tw * 4 / 3),
                       "bytes": sz, "q": q, "src_w": m["w"], "src_h": m["h"],
                       "page_url": m["page_url"], "media_url": m["media_url"],
                       "name": item["name"], "alt": item["alt"]})
        print(f"{slug} #{idx} -> {item['file']} {tw}x{int(tw*4/3)} q{q} {sz//1024}KB")
    json.dump(report, open(os.path.join(WORK, slug, "final_report.json"), "w"), indent=1)
    return report

if __name__ == "__main__":
    sel = json.load(open(sys.argv[1]))
    slug = sys.argv[2]
    process(slug, sel)
