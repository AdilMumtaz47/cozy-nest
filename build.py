#!/usr/bin/env python3
"""Static-site builder for the Pinterest home-decor blog (Cozy Nest)."""
import html
import os
import re
import sys
from datetime import date

ROOT = os.path.dirname(os.path.abspath(__file__))
POSTS_DIR = os.path.join(ROOT, "content", "posts")
SITE_NAME = "Cozy Nest"
SITE_URL = "https://cozynesthomeideas.com"
SITE_DESC = "Home decor inspiration — room ideas, seasonal looks and cozy corners, one list at a time."
LOGO_URL = "/images/logo.jpg"


def cat_slug(category):
    return re.sub(r"[^a-z0-9]+", "-", (category or "General").lower()).strip("-")


def categories_of(articles):
    cats = {}
    for a in articles:
        c = a["meta"].get("category", "General")
        cats.setdefault(c, []).append(a)
    return dict(sorted(cats.items()))


def esc(s):
    return html.escape(s or "", quote=True)


def parse_frontmatter(text):
    """Minimal frontmatter parser for our known fields. Returns (meta, body)."""
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        return {}, text
    raw, body = m.group(1), m.group(2)
    meta = {}
    images = []
    current = None
    for line in raw.splitlines():
        if re.match(r"^images:\s*$", line):
            current = "images"
            continue
        if current == "images":
            mm = re.match(r'^\s*-\s*file:\s*"?(.*?)"?\s*$', line)
            if mm:
                images.append({"file": mm.group(1).strip(), "alt": ""})
                continue
            mm = re.match(r'^\s*alt:\s*"?(.*?)"?\s*$', line)
            if mm and images:
                images[-1]["alt"] = mm.group(1).strip()
                continue
        mm = re.match(r'^([A-Za-z_]+):\s*"?(.*?)"?\s*$', line)
        if mm:
            meta[mm.group(1)] = mm.group(2).strip()
    meta["images"] = images
    return meta, body


def md_inline(text):
    """Tiny inline markdown: **bold**, *italic*, [text](url)."""
    text = esc(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    text = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', text)
    return text


def md_to_html(body, meta):
    """Convert an article body to HTML. Design sections are ## headings with one
    image each (in order, from meta['images']); FAQs are ### under the FAQ H2.
    Each design section gets an "N of 30" counter (the big decor sites all
    number their list items); a <!--MORELIKE--> marker goes after the 3rd
    design section for build_article to fill with a related card."""
    total_items = sum(
        1 for ln in body.splitlines()
        if ln.startswith("## ")
        and not ln[3:].strip().lower().startswith(("frequently asked", "takeaway"))
    )
    out = []
    faqs = []
    in_faq = False
    img_idx = 0
    item_idx = 0
    lines = body.splitlines()
    i = 0
    buf = []
    def flush():
        nonlocal buf
        if buf:
            out.append("<p>" + " ".join(md_inline(x.strip()) for x in buf if x.strip()) + "</p>")
            buf = []
    while i < len(lines):
        line = lines[i]
        # Skip the H1 line and image-markdown lines: the builder adds its own
        # H1 from frontmatter and inserts one figure per design section from
        # the frontmatter images list, in order. Keeping them would print a
        # stray "# ..." paragraph and a mangled image link.
        if line.startswith("# ") or line.startswith("!["):
            i += 1
            continue
        if line.startswith("## "):
            flush()
            title = line[3:].strip()
            if title.lower().startswith("frequently asked"):
                # FAQs are collected and rendered by build_article as a visible
                # accordion; nothing is printed here.
                in_faq = True
            elif title.lower().startswith("takeaway"):
                in_faq = False
                out.append("<h2>Takeaway</h2>")
            else:
                in_faq = False
                item_idx += 1
                out.append(
                    f'<p class="item-num">{item_idx:02d} of {total_items}</p>'
                    f"<h2>{esc(title)}</h2>"
                )
                if img_idx < len(meta.get("images", [])):
                    im = meta["images"][img_idx]
                    img_idx += 1
                    out.append(
                        f'<figure><img src="/images/{esc(meta["slug"])}/{esc(im["file"])}" '
                        f'alt="{esc(im["alt"])}" loading="lazy">'
                        f"<figcaption>{esc(im['alt'])}</figcaption></figure>"
                    )
                    if item_idx == 3:
                        out.append("<!--MORELIKE-->")
        elif line.startswith("### ") and in_faq:
            flush()
            q = line[4:].strip()
            ans_lines = []
            j = i + 1
            while j < len(lines) and not lines[j].startswith("#"):
                if lines[j].strip():
                    ans_lines.append(lines[j].strip())
                j += 1
            ans = " ".join(ans_lines)
            faqs.append((q, ans))
            i = j - 1
        elif line.strip() == "":
            flush()
        else:
            buf.append(line)
        i += 1
    flush()
    return "".join(out), faqs


def page_shell(title, meta_desc, body_html, extra_head="", nav_cats=None, og_image=None):
    nav_links = '<a href="/">Home</a>'
    for name, slug in (nav_cats or []):
        nav_links += f'<a href="/categories/{slug}/">{esc(name)}</a>'
    og_img = ""
    if og_image:
        og_img = (f'<meta property="og:image" content="{esc(og_image)}">\n'
                  f'<meta name="twitter:image" content="{esc(og_image)}">\n')
    foot_links = "".join(
        f'<a href="/categories/{slug}/">{esc(name)}</a>' for name, slug in (nav_cats or [])
    )
    year = date.today().year
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(meta_desc)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(meta_desc)}">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
{og_img}<link rel="stylesheet" href="/styles.css">
<link rel="icon" href="/favicon.ico">
{extra_head}</head>
<body>
<header class="site-header"><div class="header-inner">
<a class="brand" href="/"><img src="{LOGO_URL}" alt="Cozy Nest logo" width="46" height="46">
<span><span class="brand-name">{esc(SITE_NAME)}</span>
<span class="brand-tag">HOME DECOR IDEAS</span></span></a>
<nav>{nav_links}</nav></div></header>
<main>
{body_html}
</main>
<footer class="site-footer"><div class="footer-inner">
<div class="footer-brand"><img src="{LOGO_URL}" alt="Cozy Nest logo" width="52" height="52">
<p><span class="brand-name">{esc(SITE_NAME)}</span></p>
<p>{esc(SITE_DESC)} Every list is made to be saved and actually used at home.</p></div>
<div class="footer-links"><h3>Browse by room</h3>{foot_links}<a href="/">All ideas</a></div>
<div class="footer-links"><h3>Cozy Nest</h3><a href="/">Home</a><a href="https://www.pinterest.com/cozynestbysayed/" target="_blank" rel="noopener">Follow on Pinterest</a></div>
</div><div class="footer-bottom">&copy; {year} {esc(SITE_NAME)} — home decor inspiration, one list at a time.</div></footer>
</body>
</html>
"""


def load_articles():
    articles = []
    if not os.path.isdir(POSTS_DIR):
        return articles
    for fn in sorted(os.listdir(POSTS_DIR)):
        if not fn.endswith(".md") or fn.startswith("_"):
            continue
        path = os.path.join(POSTS_DIR, fn)
        with open(path, encoding="utf-8") as f:
            meta, body = parse_frontmatter(f.read())
        if not meta.get("slug"):
            print(f"SKIP {fn}: no slug in frontmatter")
            continue
        body_html, faqs = md_to_html(body, meta)
        articles.append({"meta": meta, "body_html": body_html, "faqs": faqs, "file": fn})
    articles.sort(key=lambda a: a["meta"].get("date", ""), reverse=True)
    return articles


def build_article(a, all_articles):
    m = a["meta"]
    slug = m["slug"]
    n = len(m.get("images", []))
    # FAQ JSON-LD, 1:1 with the visible answers
    faq_json = ""
    if a["faqs"]:
        items = ",\n".join(
            '{"@type": "Question", "name": %s, "acceptedAnswer": {"@type": "Answer", "text": %s}}'
            % (json_str(q), json_str(ans)) for q, ans in a["faqs"]
        )
        faq_json = (
            '<script type="application/ld+json">{"@context": "https://schema.org", '
            f'"@type": "FAQPage", "mainEntity": [{items}]}}</script>'
        )
    article_json = (
        '<script type="application/ld+json">{"@context": "https://schema.org", '
        f'"@type": "Article", "headline": {json_str(m["title"])}, '
        f'"datePublished": {json_str(m.get("date", ""))}, '
        f'"author": {{"@type": "Organization", "name": {json_str(SITE_NAME)}}}}}</script>'
    )
    related = [x for x in all_articles if x["meta"]["slug"] != slug][:3]
    rel_html = ""
    if related:
        cards = "".join(card_html(r) for r in related)
        rel_html = (
            f"<section class='related'><h2>You may also like</h2>"
            f"<div class='grid'>{cards}</div></section>"
        )
    faq_html = ""
    if a["faqs"]:
        items = "".join(
            f"<details><summary>{esc(q)}</summary><p>{md_inline(ans)}</p></details>"
            for q, ans in a["faqs"]
        )
        faq_html = (
            f"<section class='faq'><h2>Frequently Asked Questions</h2>{items}</section>"
        )
    og_image = None
    if m.get("images"):
        og_image = f"{SITE_URL}/images/{slug}/{m['images'][0]['file']}"
    nav_cats = [(c, cat_slug(c)) for c in categories_of(all_articles)]
    # Pin-it button (Pinterest-native share) + author box
    import urllib.parse
    pin_url = (
        "https://pinterest.com/pin/create/button/?"
        + urllib.parse.urlencode({
            "url": f"{SITE_URL}/posts/{slug}/",
            "media": og_image or "",
            "description": m["title"],
        })
    )
    pin_html = (
        f'<p><a class="pin-btn" href="{pin_url}" target="_blank" rel="noopener">'
        f"Save this list on Pinterest</a></p>"
    )
    author_html = (
        f"<section class='author-box'><img src='{LOGO_URL}' alt='Cozy Nest logo' width='64' height='64'>"
        f"<div><h3>About Cozy Nest</h3><p>Cozy Nest shares warm, practical home decor "
        f"ideas — room by room, season by season — so your home feels like home. "
        f"Every list is made to be saved and actually used.</p></div></section>"
    )
    body_html = a["body_html"]
    if "<!--MORELIKE-->" in body_html and related:
        r = related[0]
        rm = r["meta"]
        rthumb = thumb_for(rm["slug"], rm["images"][0]["file"]) if rm.get("images") else ""
        more_html = (
            f"<aside class='more-like'><p>More like this</p>"
            f"<a href='/posts/{esc(rm['slug'])}/'>"
            f"<img src='/images/{esc(rm['slug'])}/{esc(rthumb)}' alt='{esc(rm['title'])}' loading='lazy'>"
            f"<span>{esc(rm['title'])}</span></a></aside>"
        )
        body_html = body_html.replace("<!--MORELIKE-->", more_html, 1)
    else:
        body_html = body_html.replace("<!--MORELIKE-->", "", 1)
    body = (
        f'<article><p class="crumb"><a href="/">Home</a> / '
        f'<a href="/categories/{cat_slug(m.get("category", ""))}/">{esc(m.get("category", ""))}</a></p>'
        f"<h1>{esc(m['title'])}</h1>"
        f'<p class="meta-line">{esc(m.get("date", ""))} &middot; {n} ideas</p>'
        f"{pin_html}{body_html}{faq_html}{author_html}{rel_html}"
        f'<p><a class="back-link" href="/">&larr; Back to all ideas</a></p></article>'
    )
    out_dir = os.path.join(ROOT, "posts", slug)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(page_shell(m["title"], m.get("description", ""), body,
                           faq_json + article_json, nav_cats=nav_cats, og_image=og_image))
    return slug


def thumb_for(slug, first_file):
    """Card thumbnails for the homepage/category cards. Two sizes are
    generated from the article's first image on first build and reused
    afterwards: thumb.jpg (360px wide, q70) for slow connections and
    thumb-720.jpg (720px wide, q80) for retina screens, served via srcset
    in card_html(). Regenerate by deleting the thumb files before a build."""
    thumb_dir = os.path.join(ROOT, "images", slug)
    if not first_file:
        return ""
    try:
        from PIL import Image
        src = os.path.join(thumb_dir, first_file)
        im = Image.open(src).convert("RGB")
        w, h = im.size
        for name, nw, q in (("thumb.jpg", 360, 70), ("thumb-720.jpg", 720, 80)):
            path = os.path.join(thumb_dir, name)
            if not os.path.exists(path):
                nh = round(h * nw / w)
                im.resize((nw, nh), Image.LANCZOS).save(path, "JPEG", quality=q)
                print(f"thumb {slug}/{name} ({nw}x{nh})")
    except Exception as e:
        print(f"thumb SKIP {slug}: {e}")
        return first_file
    return "thumb.jpg" if os.path.exists(os.path.join(thumb_dir, "thumb.jpg")) else first_file


def thumb_srcset(slug):
    """srcset + sizes attributes for a card thumbnail, or '' if no 720
    version exists yet. Cards are 1 column <640px, 2 columns <960px,
    3 columns above (max ~360px wide), so retina phones pick the 720w file."""
    small = os.path.join(ROOT, "images", slug, "thumb.jpg")
    large = os.path.join(ROOT, "images", slug, "thumb-720.jpg")
    if os.path.exists(small) and os.path.exists(large):
        return (f'srcset="/images/{esc(slug)}/thumb.jpg 360w, '
                f'/images/{esc(slug)}/thumb-720.jpg 720w" '
                f'sizes="(max-width: 639px) 100vw, (max-width: 959px) 50vw, 360px"')
    return ""


def card_html(a):
    m = a["meta"]
    img = ""
    if m.get("images"):
        im = m["images"][0]
        thumb = thumb_for(m["slug"], im["file"])
        srcset = thumb_srcset(m["slug"])
        srcset_attr = f" {srcset}" if srcset else ""
        img = (f'<img src="/images/{esc(m["slug"])}/{esc(thumb)}"'
               f'{srcset_attr} '
               f'alt="{esc(im["alt"])}" loading="lazy">')
    return (
        f'<article class="card"><a href="/posts/{esc(m["slug"])}/">{img}'
        f"<h2>{esc(m['title'])}</h2><p>{esc(m.get('description', ''))}</p>"
        f'<p class="meta-line">{esc(m.get("date", ""))} &middot; {esc(m.get("category", ""))}</p>'
        f"</a></article>"
    )


def json_str(s):
    import json
    return json.dumps(s or "", ensure_ascii=False)


def build_home(articles):
    nav_cats = [(c, cat_slug(c)) for c in categories_of(articles)]
    chips = "".join(
        f'<a class="chip" href="/categories/{cat_slug(c)}/">{esc(c)} <span>({len(v)})</span></a>'
        for c, v in categories_of(articles).items()
    )
    if articles:
        featured = articles[0]
        fm = featured["meta"]
        fimg = ""
        if fm.get("images"):
            fim = fm["images"][0]
            fimg = (f'<img src="/images/{esc(fm["slug"])}/{esc(fim["file"])}" '
                    f'alt="{esc(fim["alt"])}" loading="lazy">')
        hero = (
            f"<section class='feature'><a href='/posts/{esc(fm['slug'])}/'>{fimg}"
            f"<div class='feature-text'><p class='feature-cat'>{esc(fm.get('category', ''))} &middot; Featured</p>"
            f"<h2>{esc(fm['title'])}</h2><p>{esc(fm.get('description', ''))}</p>"
            f"<span class='feature-link'>See the 30 ideas &rarr;</span></div></a></section>"
        )
        rest = articles[1:]
        cards = "".join(card_html(a) for a in rest)
        grid = (
            f"<h2 class='section-title'>Latest ideas</h2>"
            f"<p class='section-sub'>Fresh lists for every room and every season.</p>"
            f"<section class='grid'>{cards}</section>"
        )
    else:
        hero = ""
        grid = "<section class='grid'><p>First articles coming soon — the first list is being written now.</p></section>"
    body = (
        f"<section class='hero'><img class='hero-logo' src='{LOGO_URL}' alt='Cozy Nest logo' width='96' height='96'>"
        f"<h1>{esc(SITE_NAME)}</h1><p>{esc(SITE_DESC)}</p>"
        f"<div class='chips'>{chips}</div></section>{hero}{grid}"
    )
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(page_shell(SITE_NAME + " — Home Decor Ideas", SITE_DESC, body,
                           nav_cats=nav_cats, og_image=SITE_URL + LOGO_URL))


def build_categories(articles):
    nav_cats = [(c, cat_slug(c)) for c in categories_of(articles)]
    for cat, items in categories_of(articles).items():
        slug = cat_slug(cat)
        cards = "".join(card_html(a) for a in items)
        body = (
            f"<section class='category-hero'><h1>{esc(cat)}</h1>"
            f"<p>{len(items)} idea list{'s' if len(items) != 1 else ''} to make your home feel like home.</p></section>"
            f"<section class='grid'>{cards}</section>"
        )
        out_dir = os.path.join(ROOT, "categories", slug)
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(page_shell(f"{cat} — {SITE_NAME}",
                               f"{cat} ideas from {SITE_NAME} — room ideas, seasonal looks and cozy corners.",
                               body, nav_cats=nav_cats))
    return [cat_slug(c) for c in categories_of(articles)]


def build_sitemap(articles, cat_slugs=None):
    urls = [SITE_URL + "/"]
    for s in (cat_slugs or []):
        urls.append(f"{SITE_URL}/categories/{s}/")
    for a in articles:
        urls.append(f"{SITE_URL}/posts/{a['meta']['slug']}/")
    today = date.today().isoformat()
    items = "".join(f"<url><loc>{esc(u)}</loc><lastmod>{today}</lastmod></url>" for u in urls)
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{items}</urlset>')
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")


def main():
    articles = load_articles()
    for a in articles:
        slug = build_article(a, articles)
        n = len(a["meta"].get("images", []))
        print(f"built /posts/{slug}/ ({n} images, {len(a['faqs'])} FAQs)")
    build_home(articles)
    cat_slugs = build_categories(articles)
    build_sitemap(articles, cat_slugs)
    print(f"done: {len(articles)} article(s), {len(cat_slugs)} categor(ies), homepage + sitemap written.")


if __name__ == "__main__":
    main()
