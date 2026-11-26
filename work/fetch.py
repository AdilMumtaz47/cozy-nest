#!/usr/bin/env python3
"""Parse image-search JSONs into per-article candidate lists, download them."""
import json, os, sys, subprocess, hashlib
from PIL import Image

WORK = os.path.expanduser("~/workspace/pinterest-blog/work")

def parse(slug):
    cands = []
    seen = set()
    d = os.path.join(WORK, slug)
    for fn in sorted(os.listdir(d)):
        if not (fn.endswith(".json") and fn.startswith("s")):
            continue
        try:
            data = json.load(open(os.path.join(d, fn)))
        except Exception as e:
            print(f"{slug}/{fn}: parse error {e}")
            continue
        for r in data.get("results", []):
            mu = r.get("media_url")
            if not mu or mu in seen:
                continue
            seen.add(mu)
            cands.append({
                "media_url": mu,
                "page_url": r.get("page_url", ""),
                "desc": (r.get("description") or "").replace("\n", " "),
                "title": r.get("title", ""),
            })
    return cands

def download(slug, cands):
    canddir = os.path.join(WORK, slug, "cand")
    os.makedirs(canddir, exist_ok=True)
    meta = []
    for i, c in enumerate(cands, 1):
        fn = f"{i:02d}.bin"
        path = os.path.join(canddir, fn)
        if not os.path.exists(path) or os.path.getsize(path) == 0:
            r = subprocess.run([
                "curl", "-fsSL", "--connect-timeout", "10", "--max-time", "60",
                "-A", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
                "-H", "Accept: image/png,image/jpeg,image/gif,image/webp,image/*;q=0.5",
                "-H", "Referer: https://www.google.com/",
                "-o", path, c["media_url"]], capture_output=True)
            if r.returncode != 0:
                print(f"{slug} {fn}: download failed")
                continue
        try:
            im = Image.open(path)
            im.verify()
            im2 = Image.open(path)
            w, h = im2.size
            fmt = im2.format
        except Exception as e:
            print(f"{slug} {fn}: not an image ({e})")
            continue
        meta.append({"idx": i, "file": fn, "w": w, "h": h, "fmt": fmt,
                     "bytes": os.path.getsize(path),
                     "media_url": c["media_url"], "page_url": c["page_url"],
                     "desc": c["desc"], "title": c["title"]})
        print(f"{slug} {fn}: {w}x{h} {fmt} {os.path.getsize(path)//1024}KB")
    json.dump(meta, open(os.path.join(WORK, slug, "cand_meta.json"), "w"), indent=1)
    return meta

if __name__ == "__main__":
    for slug in sys.argv[1:]:
        cands = parse(slug)
        print(f"== {slug}: {len(cands)} unique candidates")
        download(slug, cands)
