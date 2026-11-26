#!/usr/bin/env python3
"""Render the four articles + image provenance lists from data modules."""
import json, os, sys, importlib

WORK = os.path.expanduser("~/workspace/pinterest-blog/work")
BLOG = os.path.expanduser("~/workspace/pinterest-blog")

SCREEN = {
    "diy-tree-collar-wood": ("diy tree collar wood", "STRONG (screen #5, Nov 25, 2026)"),
    "diy-tree-collar": ("diy tree collar", "WINNABLE (screen #4, Nov 25, 2026)"),
    "garland-on-mantle": ("garland on mantle", "WINNABLE (screen #5, Nov 25, 2026)"),
    "doorway-garland": ("doorway garland", "WINNABLE (screen #5, Nov 25, 2026)"),
}

def tip(n):
    if n % 3 == 1:
        return None  # filled from per-idea data below
    return None

# Per-idea tips, keyed by (slug, idea number). Written to match each idea.
TIPS = {}

def render(slug, data_mod, screen_label):
    sel = json.load(open(os.path.join(WORK, slug, "sel.json")))
    rep = json.load(open(os.path.join(WORK, slug, "final_report.json")))
    assert len(sel) == 30 and len(rep) == 30, (slug, len(sel), len(rep))
    assert len(data_mod.IDEAS) == 30, (slug, len(data_mod.IDEAS))
    assert len(data_mod.FAQS) == 8, (slug, len(data_mod.FAQS))
    for r in rep:
        assert r["bytes"] < 400000, r
        assert r["w"] >= 300

    # --- article markdown ---
    lines = []
    lines.append("---")
    lines.append(f'title: "{data_mod.TITLE}"')
    lines.append(f'slug: "{data_mod.SLUG}"')
    lines.append(f'description: "{data_mod.DESCRIPTION}"')
    lines.append(f'keyword: "{data_mod.KEYWORD}"')
    lines.append(f'category: "{data_mod.CATEGORY}"')
    lines.append(f'date: "{data_mod.DATE}"')
    lines.append("images:")
    for s in sel:
        lines.append(f'  - file: "{s["file"]}"')
        lines.append(f'    alt: "{s["alt"]}"')
    lines.append("---")
    lines.append("")
    lines.append(f"# {data_mod.TITLE}")
    lines.append("")
    for p in data_mod.INTRO:
        lines.append(p)
        lines.append("")
    for i, (name, paras) in enumerate(data_mod.IDEAS, 1):
        s = sel[i - 1]
        assert s["name"] == name, (slug, i, s["name"], name)
        lines.append(f"## {i}. {name}")
        lines.append("")
        for p in paras:
            lines.append(p)
            lines.append("")
        lines.append(f"![{s['alt']}](/images/{slug}/{s['file']})")
        lines.append("")
        lines.append(TIPS[(slug, i)])
        lines.append("")
    lines.append("## Takeaway")
    lines.append("")
    lines.append(data_mod.TAKEAWAY)
    lines.append("")
    lines.append("## Frequently Asked Questions")
    lines.append("")
    for q, a in data_mod.FAQS:
        wc = len(a.split())
        assert 40 <= wc <= 60, (slug, q, wc)
        lines.append(f"### {q}")
        lines.append("")
        lines.append(a)
        lines.append("")
    md = "\n".join(lines)
    with open(os.path.join(BLOG, "content", "posts", f"{slug}.md"), "w") as f:
        f.write(md)
    print(f"{slug}: article written, {len(md.splitlines())} lines")

    # --- image provenance list ---
    kw, screen = SCREEN[slug]
    sub = [r for r in rep if r["w"] < 768]
    widths = f"{30 - len(sub)} photos >=768px. " + (
        f"{len(sub)} photos below 768px at source (noted below) — sources topped out below 768px, not upscaled: " +
        ", ".join(f"#{i+1} {r['w']}px" for i, r in enumerate(rep) if r["w"] < 768) + "." if sub else "No sub-768px exceptions.")
    hdr = [
        f"# {data_mod.TITLE} — image provenance list",
        "",
        f'Keyword: "{kw}" ({screen}).',
        f"All 30 images: real photos, portrait, JPEG q~82, <400KB, sharpness verified visually (full frame + bottom 35% strip), Nov 26 2026.",
        "IG/web split: 0 Instagram / 30 web (the image-search CLI returned no instagram.com source pages across the searches for this article).",
        "",
        f"Widths: {widths}" + (" Several sources were 1000px square product shots, so the 3:4 portrait crop yields 750px." if slug == "diy-tree-collar" else ""),
        "",
        "| Design | Original file | New file | Alt text | Source URL |",
        "|---|---|---|---|---|",
    ]
    for i, (r, s) in enumerate(zip(rep, sel), 1):
        hdr.append(f"| {i} {s['name']} | cand/{r['idx']:02d}.bin | {s['file']} | {s['alt']} | {r['page_url']} |")
    with open(os.path.join(BLOG, f"{slug}-image-list.md"), "w") as f:
        f.write("\n".join(hdr) + "\n")
    print(f"{slug}: image list written; exceptions: {len(sub)}")

if __name__ == "__main__":
    import data_tips
    TIPS.update(data_tips.TIPS)
    for slug, modname, screen in [
        ("diy-tree-collar-wood", "data_wood", "STRONG"),
        ("diy-tree-collar", "data_general", "WINNABLE"),
        ("garland-on-mantle", "data_mantel", "WINNABLE"),
        ("doorway-garland", "data_doorway", "WINNABLE"),
    ]:
        mod = importlib.import_module(modname)
        render(slug, mod, screen)
