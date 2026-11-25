#!/usr/bin/env python3
"""Static-site builder for the Pinterest home-decor blog (Cozy Nest)."""
import html
import json
import os
import re
import sys
import urllib.parse
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


def pin_create_url(page_url, media_url, description):
    """Pinterest pin-creator link for one photo — same construction as the
    article 'Save this list on Pinterest' button (url + media + description,
    URL-encoded). Opens Pinterest's pin creator for that photo in a new tab."""
    return (
        "https://pinterest.com/pin/create/button/?"
        + urllib.parse.urlencode({
            "url": page_url,
            "media": media_url,
            "description": description,
        })
    )


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


def render_tip(line):
    """One tip box after an idea. Marker lines in article markdown:
      > TIP:QUICK: <short advice, 1-2 sentences>
      > TIP:CHECK: item one; item two; item three
      > TIP:GUIDE: Label: value | Label: value | Label: value
    Rendered as a pale warm-cream callout box (Nesting Oak-style),
    emoji-led. Rotation across a 30-idea article: idea n%3==1 QUICK,
    n%3==2 CHECK, n%3==0 GUIDE, so each article carries 10 of each."""
    rest = line[len("> TIP:"):].strip()
    kind, _, content = rest.partition(":")
    kind = kind.strip().upper()
    content = content.strip()
    if kind == "CHECK":
        items = [x.strip() for x in content.split(";") if x.strip()]
        lis = "".join(f"<li>{md_inline(x)}</li>" for x in items)
        return ('<aside class="tip-box tip-check">'
                '<p class="tip-label">✅ Before you buy</p>'
                f"<ul>{lis}</ul></aside>")
    if kind == "GUIDE":
        cols = []
        for part in content.split("|"):
            part = part.strip()
            if not part:
                continue
            label, _, value = part.partition(":")
            cols.append(
                f'<div><span class="col-label">{esc(label.strip())}</span>'
                f'<span class="col-value">{md_inline(value.strip())}</span></div>'
            )
        return ('<aside class="tip-box tip-guide">'
                '<p class="tip-label">Quick guide</p>'
                f'<div class="tip-guide-cols">{"".join(cols)}</div></aside>')
    # QUICK (default)
    return ('<aside class="tip-box tip-quick">'
            f"<p><strong>💡 Quick Tip:</strong> {md_inline(content)}</p></aside>")


def md_to_html(body, meta):
    """Convert an article body to HTML. Design sections are ## headings with one
    image each (in order, from meta['images']); FAQs are ### under the FAQ H2.
    Each design section gets an "N of 30" counter (the big decor sites all
    number their list items) and an id anchor; a <!--TOC--> marker goes after
    the intro, before idea #1, for build_article to fill with the table of
    contents. Returns (html, faqs, toc) where toc is [(anchor, label)].
    Each figure carries a small red Pinterest "P" badge on its top-left
    corner, and the "Takeaway" H2 gets an id anchor too."""
    total_items = sum(
        1 for ln in body.splitlines()
        if ln.startswith("## ")
        and not ln[3:].strip().lower().startswith(("frequently asked", "takeaway"))
    )
    out = []
    faqs = []
    toc = []
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
                out.append('<h2 id="takeaway">Takeaway</h2>')
            else:
                in_faq = False
                item_idx += 1
                anchor = f"idea-{item_idx}"
                toc.append((anchor, title))
                if item_idx == 1:
                    out.append("<!--TOC-->")
                out.append(
                    f'<p class="item-num">{item_idx:02d} of {total_items}</p>'
                    f'<h2 id="{anchor}">{esc(title)}</h2>'
                )
                if img_idx < len(meta.get("images", [])):
                    im = meta["images"][img_idx]
                    img_idx += 1
                    fig_pin = pin_create_url(
                        f"{SITE_URL}/posts/{meta['slug']}/",
                        f"{SITE_URL}/images/{meta['slug']}/{im['file']}",
                        title,
                    )
                    out.append(
                        f'<figure><a class="pin-badge" href="{fig_pin}" target="_blank" rel="noopener">P</a>'
                        f'<img src="/images/{esc(meta["slug"])}/{esc(im["file"])}" '
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
        elif line.startswith("> TIP:"):
            # Tip box after an idea (see render_tip): flush the idea's
            # paragraphs first, then emit the callout box.
            flush()
            out.append(render_tip(line))
        elif line.strip() == "":
            flush()
        else:
            buf.append(line)
        i += 1
    flush()
    return "".join(out), faqs, toc


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
<header class="site-header"><div class="header-top">
<a class="brand" href="/"><img src="{LOGO_URL}" alt="Cozy Nest logo" width="64" height="64">
<span><span class="brand-name">{esc(SITE_NAME)}</span>
<span class="brand-tag">HOME DECOR IDEAS</span></span></a>
</div><nav class="main-nav"><div class="nav-inner"><div class="nav-links">{nav_links}</div>
<button class="nav-search" type="button" id="search-open" aria-label="Search" aria-haspopup="dialog" title="Search"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><line x1="16.5" y1="16.5" x2="21" y2="21"/></svg></button>
</div></nav></header>
<main>
{body_html}
</main>
<footer class="site-footer"><div class="footer-inner">
<div class="footer-logo"><img src="{LOGO_URL}" alt="Cozy Nest logo" width="52" height="52"></div>
<nav class="footer-nav"><a href="/">Home</a>{foot_links}</nav>
<div class="footer-social">
<a href="https://www.pinterest.com/cozynestbysayed/" target="_blank" rel="noopener" title="Facebook"><svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" aria-hidden="true"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg></a>
<a href="https://www.pinterest.com/cozynestbysayed/" target="_blank" rel="noopener" title="X"><svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" aria-hidden="true"><path d="M18.901 1.153h3.68l-8.04 9.19L24 22.846h-7.406l-5.8-7.584-6.638 7.584H.474l8.6-9.83L0 1.154h7.594l5.243 6.932ZM17.61 20.644h2.039L6.486 3.24H4.298Z"/></svg></a>
<a href="https://www.pinterest.com/cozynestbysayed/" target="_blank" rel="noopener" title="Instagram"><svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" aria-hidden="true"><path d="M12 0C8.74 0 8.333.015 7.053.072 5.775.132 4.905.333 4.14.63c-.789.306-1.459.717-2.126 1.384S.935 3.35.63 4.14C.333 4.905.131 5.775.072 7.053.012 8.333 0 8.74 0 12s.015 3.667.072 4.947c.06 1.277.261 2.148.558 2.913.306.788.717 1.459 1.384 2.126.667.666 1.336 1.079 2.126 1.384.766.296 1.636.499 2.913.558C8.333 23.988 8.74 24 12 24s3.667-.015 4.947-.072c1.277-.06 2.148-.262 2.913-.558.788-.306 1.459-.718 2.126-1.384.666-.667 1.079-1.335 1.384-2.126.296-.765.499-1.636.558-2.913.06-1.28.072-1.687.072-4.947s-.015-3.667-.072-4.947c-.06-1.277-.262-2.149-.558-2.913-.306-.789-.718-1.459-1.384-2.126C21.319 1.347 20.651.935 19.86.63c-.765-.297-1.636-.499-2.913-.558C15.667.012 15.26 0 12 0zm0 2.16c3.203 0 3.585.016 4.85.071 1.17.055 1.805.249 2.227.415.562.217.96.477 1.382.896.419.42.679.819.896 1.381.164.422.36 1.057.413 2.227.057 1.266.07 1.646.07 4.85s-.015 3.585-.074 4.85c-.061 1.17-.256 1.805-.421 2.227-.224.562-.479.96-.899 1.382-.419.419-.824.679-1.38.896-.42.164-1.065.36-2.235.413-1.274.057-1.649.07-4.859.07-3.211 0-3.586-.015-4.859-.074-1.171-.061-1.816-.256-2.236-.421-.569-.224-.96-.479-1.379-.899-.421-.419-.69-.824-.9-1.38-.165-.42-.359-1.065-.42-2.235-.045-1.26-.061-1.649-.061-4.844 0-3.196.016-3.586.061-4.861.061-1.17.255-1.814.42-2.234.21-.57.479-.96.9-1.381.419-.419.81-.689 1.379-.898.42-.166 1.051-.361 2.221-.421 1.275-.045 1.65-.06 4.859-.06l.045.03zm0 3.678c-3.405 0-6.162 2.76-6.162 6.162 0 3.405 2.76 6.162 6.162 6.162 3.405 0 6.162-2.76 6.162-6.162 0-3.405-2.76-6.162-6.162-6.162zM12 16c-2.21 0-4-1.79-4-4s1.79-4 4-4 4 1.79 4 4-1.79 4-4 4zm7.846-10.405c0 .795-.646 1.44-1.44 1.44-.795 0-1.44-.646-1.44-1.44 0-.794.646-1.439 1.44-1.439.793-.001 1.44.645 1.44 1.439z"/></svg></a>
<a href="https://www.pinterest.com/cozynestbysayed/" target="_blank" rel="noopener">Follow on Pinterest</a></div>
</div>
<div class="footer-note">{esc(SITE_DESC)} Every list is made to be saved and actually used at home.</div>
<div class="footer-bottom">&copy; {year} {esc(SITE_NAME)} — home decor inspiration, one list at a time.</div></footer>
<div class="search-overlay" id="search-overlay" hidden>
<div class="search-panel" role="dialog" aria-modal="true" aria-label="Search Cozy Nest">
<div class="search-bar">
<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><line x1="16.5" y1="16.5" x2="21" y2="21"/></svg>
<input id="search-input" type="search" placeholder="Search ideas, rooms, styles…" aria-label="Search ideas" autocomplete="off">
<button type="button" class="search-close" id="search-close" aria-label="Close search">&times;</button>
</div>
<p class="search-hint" id="search-hint">Search every list — try “bathroom”, “bookshelf” or “fall”.</p>
<div class="search-results" id="search-results"></div>
</div>
</div>
<script src="/search.js" defer></script>
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
        body_html, faqs, toc = md_to_html(body, meta)
        articles.append({"meta": meta, "body_html": body_html, "faqs": faqs, "toc": toc, "file": fn})
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
            f"<section class='related'><h2>Similar Posts</h2>"
            f"<div class='grid'>{cards}</div></section>"
        )
    faq_html = ""
    if a["faqs"]:
        items = "".join(
            f"<details><summary>{esc(q)}</summary><p>{md_inline(ans)}</p></details>"
            for q, ans in a["faqs"]
        )
        faq_html = (
            f"<section class='faq' id='faq'><h2>Frequently Asked Questions</h2>{items}</section>"
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
    # Table of contents: all 30 ideas + FAQ, linked to the H2 anchors.
    toc_entries = list(a.get("toc", []))
    if a["faqs"]:
        toc_entries.append(("faq", "Frequently Asked Questions"))
    toc_html = ""
    if toc_entries:
        toc_items = "".join(
            f'<li><a href="#{esc(anchor)}">{esc(label)}</a></li>'
            for anchor, label in toc_entries
        )
        toc_html = (
            f'<details class="toc" open><summary>Table of Contents</summary>'
            f"<ul>{toc_items}</ul></details>"
        )
    body_html = a["body_html"].replace("<!--TOC-->", toc_html, 1)
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
    # Hero first, then the white article card overlapping its bottom edge.
    hero_html = ""
    if m.get("images"):
        fim = m["images"][0]
        hero_html = (
            f'<div class="article-hero"><a class="pin-badge" href="{pin_url}" target="_blank" rel="noopener">P</a>'
            f'<img src="/images/{esc(slug)}/{esc(fim["file"])}" alt="{esc(fim["alt"])}"></div>'
        )
    # Sidebar: latest posts (3 stacked items, thumb above title).
    latest = [x for x in all_articles if x["meta"]["slug"] != slug][:3]
    side_items = ""
    for r in latest:
        rm = r["meta"]
        sthumb = thumb_for(rm["slug"], rm["images"][0]["file"]) if rm.get("images") else ""
        simg = (f"<img src='/images/{esc(rm['slug'])}/{esc(sthumb)}' "
                f"alt='{esc(rm['title'])}' loading='lazy'>") if sthumb else ""
        side_items += (
            f"<a class='side-item' href='/posts/{esc(rm['slug'])}/'>{simg}"
            f"<span class='side-title'>{esc(rm['title'])}</span></a>"
        )
    sidebar_html = f"<aside class='sidebar'><h2>Latest Post</h2>{side_items}</aside>"
    body = (
        f'<div class="article-layout"><div class="article-col">'
        f'<p class="crumb"><a href="/">Home</a> / '
        f'<a href="/categories/{cat_slug(m.get("category", ""))}/">{esc(m.get("category", ""))}</a></p>'
        f"{hero_html}"
        f'<article class="article-card">'
        f'<p class="cat-label">{esc(m.get("category", ""))}</p>'
        f"<h1>{esc(m['title'])}</h1>"
        f'<p class="meta-line">{esc(m.get("date", ""))}</p>'
        f"{pin_html}{body_html}{faq_html}{author_html}"
        f"</article></div>{sidebar_html}</div>"
        f"{rel_html}"
        f'<p><a class="back-link" href="/">&larr; Back to all ideas</a></p>'
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
    # No big hero block: the header already carries the logo + "Cozy Nest"
    # + "HOME DECOR IDEAS" and the nav already lists all categories, so the
    # homepage opens straight onto the featured article (header, nav, then
    # content — like an article page).
    if articles:
        featured = articles[0]
        fm = featured["meta"]
        fimg = ""
        feat_pin = ""
        if fm.get("images"):
            fim = fm["images"][0]
            # Eager load: this is the first thing on the page, so it must
            # appear immediately instead of leaving empty space while loading.
            fimg = (f'<img src="/images/{esc(fm["slug"])}/{esc(fim["file"])}" '
                    f'alt="{esc(fim["alt"])}" fetchpriority="high">')
            feat_pin = pin_create_url(
                f"{SITE_URL}/posts/{fm['slug']}/",
                f"{SITE_URL}/images/{fm['slug']}/{fim['file']}",
                fm["title"],
            )
        # The badge is a SIBLING of the article link (never nested inside
        # it — nested links are invalid HTML and the click would follow the
        # article). .feature is position:relative, so the badge still sits
        # over the top-left of the feature image, exactly as before.
        badge = (f"<a class='pin-badge' href='{feat_pin}' target='_blank' rel='noopener'>P</a>"
                 if feat_pin else "")
        hero = (
            f"<section class='feature'>{badge}<a href='/posts/{esc(fm['slug'])}/'>"
            f"<div class='feature-img'>{fimg}</div>"
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
    body = f"{hero}{grid}"
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


def build_search_index(articles):
    """Lean client-side search index, rebuilt on every build so new
    articles become searchable automatically. One entry per article:
    title, url, category, and the 30 idea headings (from the TOC the
    builder already collects). No body text, no image URLs — keeps the
    file small for slow mobile connections."""
    entries = []
    for a in articles:
        m = a["meta"]
        ideas = [label for _, label in a.get("toc", [])]
        entries.append({
            "t": m["title"],
            "u": f"/posts/{m['slug']}/",
            "c": m.get("category", ""),
            "i": ideas,
        })
    with open(os.path.join(ROOT, "search-index.json"), "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, separators=(",", ":"))
    print(f"search index: {len(entries)} article(s)")
    return entries


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
    build_search_index(articles)
    print(f"done: {len(articles)} article(s), {len(cat_slugs)} categor(ies), homepage + sitemap written.")


if __name__ == "__main__":
    main()
