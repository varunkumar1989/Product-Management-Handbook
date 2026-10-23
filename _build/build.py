#!/usr/bin/env python
"""Static-site + print-HTML builder for the PM Master Handbook.

    python -I _build/build.py

Reads content/**/*.md (+ glossary.yaml), renders charts/diagrams/quizzes from
fenced blocks, and writes:
  html/Interactive-PM-Handbook/*.html   (interactive site, works from file://)
  _build/print/*.html                    (inputs for pdf.py)
  index.html                              (project entry point)
"""
import json, re, shutil, sys, datetime
from html import escape
from pathlib import Path

import markdown, yaml

sys.path.insert(0, str(Path(__file__).parent))
import charts

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
SITE = ROOT / "html" / "Interactive-PM-Handbook"
PRINT = ROOT / "_build" / "print"
ASSETS = ROOT / "_build" / "assets"
VERSION = "v0.1 · " + datetime.date.today().strftime("%d %B %Y")
TITLE = "Product Management Master Handbook"

MODULE_FILES = {  # slug used for module PDFs
    1: "Module-01-Fundamentals", 2: "Module-02-Strategy", 3: "Module-03-Discovery", 4: "Module-04-Prioritization",
    5: "Module-05-UX-Design", 6: "Module-06-Communication", 7: "Module-07-Analytics", 8: "Module-08-Growth",
    9: "Module-09-Tech-System-Design", 10: "Module-10-LLM-RAG", 11: "Module-11-Vibe-Coding", 12: "Module-12-Agentic-AI",
}
COLLECTIONS = [
    # key, title, dir, blurb
    ("frameworks", "Framework Library", "frameworks", "29 frameworks, each with a visual model, worked example, usage criteria, limitations and a reusable template."),
    ("cases", "Case Study Library", "cases", "Twelve product case studies. Company cases use only public, well-known facts; all numbers are labelled hypothetical unless sourced."),
    ("projects", "Practical Projects & Portfolio", "projects", "Five end-to-end projects with briefs, datasets, templates, model solutions and portfolio guidance."),
    ("interview", "Interview Handbook", "interview", "100+ questions by category and difficulty, each with what the interviewer tests, a structure, a model answer and common mistakes."),
]
SIMPLE_PAGES = [  # key, title, file
    ("start", "Start Here", "pages/start.md"),
    ("resources", "References & Resources", "pages/resources.md"),
    ("appendix", "Appendix: Source Coverage & Gap Analysis", None),
]


# ------------------------------------------------------------------ helpers
def read_md(path):
    return parse_md(Path(path).read_text(encoding="utf-8"))


def read_items(path):
    """A collection file may hold several entries separated by a line '<!-- item -->'."""
    txt = Path(path).read_text(encoding="utf-8")
    parts = [p.strip("\n") for p in re.split(r"^<!-- item -->[ \t]*$", txt, flags=re.M)]
    return [parse_md(p) for p in parts if p.strip()]


def parse_md(txt):
    meta = {}
    if txt.startswith("---"):
        _, fm, body = txt.split("---", 2)
        fm = "\n".join(
            re.sub(r"^(title|subtitle|summary|sources|category):[ \t]+(?![\"'\[{|>])(.+?)[ \t]*$",
                   lambda m: f'{m.group(1)}: "' + m.group(2).replace("\\", "\\\\").replace('"', '\\"') + '"', ln)
            for ln in fm.split("\n"))
        meta = yaml.safe_load(fm) or {}
        txt = body.lstrip("\n")
    return meta, txt


def demote(md_text, by=2):
    """Lower Markdown heading levels (e.g. '# ' -> '### ') for embedding standalone docs."""
    return re.sub(r"^(#{1,4}) ", lambda m: "#" * min(6, len(m.group(1)) + by) + " ", md_text, flags=re.M)


def strip_tags(h):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h)).strip()


def slugify_with(prefix):
    def _s(value, sep):
        v = re.sub(r"[^\w\s-]", "", value.lower()).strip()
        v = re.sub(r"[-\s]+", sep, v)
        return f"{prefix}-{v}"[:90]
    return _s


_PLAIN_KEYS = re.compile(r"^(\s*)(title|caption|alt|xlabel|ylabel|rowhead|unit|center|label|fmt):[ \t]+(?![\[{|>&*!%@`])(.+?)[ \t]*$")
_QUOTED = re.compile(r'^("([^"\\]|\\.)*"|\'([^\']|\'\')*\')$')


def fix_yaml(body):
    """Auto-quote plain-scalar values for known text keys so ': ' or ' #' inside captions can't break YAML."""
    out = []
    for ln in body.split("\n"):
        m = _PLAIN_KEYS.match(ln)
        if m and not _QUOTED.match(m.group(3)):
            v = m.group(3).replace("\\", "\\\\").replace('"', '\\"')
            ln = f'{m.group(1)}{m.group(2)}: "{v}"'
        out.append(ln)
    return "\n".join(out)


FENCE = re.compile(r"^```(chart|quiz|formula)[ \t]*\n(.*?)^```[ \t]*$", re.S | re.M)


def render_quiz(spec, qid):
    items = spec if isinstance(spec, list) else spec["questions"]
    out = [f'<div class="quiz" data-quiz="{qid}"><h4>Check your understanding</h4>']
    for q in items:
        a = int(q["answer"])
        lis = "".join(f'<li class="{"is-correct" if i == a else ""}">{escape(str(o))}</li>' for i, o in enumerate(q["options"]))
        out.append(f'<div class="qitem" data-correct="{a}"><p class="q">{escape(q["q"])}</p><ol>{lis}</ol>'
                   f'<div class="why"><strong>Why:</strong> {escape(q["why"])}</div></div>')
    out.append('<div class="quizscore" aria-live="polite"></div><button class="iconbtn quizreset noprint" type="button">Reset quiz</button></div>')
    return "".join(out)


SVG_STYLE = """<style>
svg{--ink:#101828;--muted:#475467;--line:#D0D5DD;--grid:#E4E7EC;--bg2:#F8FAFC;--surface:#fff;--ink2:#344054;--warn:#B54708;--warn-bg:#FFFAEB;
--c1:#2563EB;--c2:#7C3AED;--c3:#D97706;--c4:#059669;--c5:#DB2777;--c6:#64748B;font-family:'Segoe UI',Arial,sans-serif;background:#fff}
text{fill:var(--ink);font-size:12.5px}text.small{font-size:11.5px}text.tiny{font-size:10.5px}text.b{font-weight:700}text.mut{fill:var(--muted)}
text.warn{fill:var(--warn)}text.on-fill{fill:#fff}text.quad{fill:var(--muted);font-size:11px;font-style:italic}
.grid{stroke:var(--grid)}.grid.dash{stroke-dasharray:4 4}.axis{stroke:var(--muted);stroke-width:1.2}.plot{fill:var(--bg2);stroke:var(--line)}
.node{fill:var(--bg2);stroke:var(--line);stroke-width:1.5}.node.hl{fill:#E8EFFE;stroke:var(--c1)}.edge{stroke:var(--muted);stroke-width:1.6;fill:none}
.arrowhead{fill:var(--muted)}.reject{fill:var(--c3);fill-opacity:.4}.empty{fill:var(--bg2);stroke:var(--line);stroke-dasharray:3 3}
.phone{fill:#fff;stroke:var(--ink2);stroke-width:2.2}.wf-bar{fill:var(--bg2);stroke:var(--line)}.wf-img{fill:var(--bg2);stroke:var(--line);stroke-dasharray:4 3}
.wf-input{fill:#fff;stroke:var(--muted)}.wf-warn{fill:var(--warn-bg);stroke:var(--c3)}
</style>"""
_svg_counts = {}


def export_svg(fig_html, prefix, title):
    """Save each generated SVG as a standalone, light-theme file in diagrams/ for reuse in slides or docs."""
    m = re.search(r"(<svg[^>]*>)(.*)</svg>", fig_html, re.S)
    if not m:
        return
    _svg_counts[prefix] = _svg_counts.get(prefix, 0) + 1
    slug = re.sub(r"[^a-z0-9]+", "-", str(title).lower()).strip("-")[:60]
    (ROOT / "diagrams").mkdir(exist_ok=True)
    (ROOT / "diagrams" / f"{prefix}-{_svg_counts[prefix]:02d}-{slug}.svg").write_text(
        m.group(1) + SVG_STYLE + f"<title>{escape(str(title))}</title>" + m.group(2) + "</svg>", encoding="utf-8")


def render_md(text, prefix, quiz_id=None):
    stash = {}

    def sub(m):
        kind, body = m.group(1), m.group(2)
        key = f"@@STASH{len(stash)}@@"
        if kind == "chart":
            try:
                spec = yaml.safe_load(fix_yaml(body))
                ttl = spec.get("title", "chart")
                stash[key] = charts.render(spec)
                export_svg(stash[key], prefix, ttl)
            except Exception as e:
                raise RuntimeError(f"chart error in {prefix}: {e}\n{body[:400]}") from e
        elif kind == "quiz":
            try:
                stash[key] = render_quiz(yaml.safe_load(body), quiz_id or prefix)
            except Exception as e:
                raise RuntimeError(f"quiz error in {prefix}: {e}\n{body[:400]}") from e
        else:
            stash[key] = f'<div class="formula">{escape(body.rstrip())}</div>'
        return f"\n\n{key}\n\n"

    text = FENCE.sub(sub, text)
    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "toc", "attr_list", "admonition", "md_in_html", "sane_lists", "pymdownx.details"],
        extension_configs={"toc": {"slugify": slugify_with(prefix), "permalink": False}},
    )
    html = md.convert(text)
    for k, v in stash.items():
        html = html.replace(f"<p>{k}</p>", v)
    html = re.sub(r"<table>", '<div class="tablewrap"><table>', html)
    html = html.replace("</table>", "</table></div>")
    return html


def number_headings(html, n):
    c2 = c3 = 0
    toc = []

    def rep(m):
        nonlocal c2, c3
        lvl, attrs, inner = m.group(1), m.group(2), m.group(3)
        idm = re.search(r'id="([^"]+)"', attrs)
        hid = idm.group(1) if idm else ""
        if lvl == "2":
            c2 += 1; c3 = 0
            label = f"{n}.{c2}"
            toc.append((hid, label, strip_tags(inner)))
        else:
            c3 += 1
            label = f"{n}.{c2}.{c3}"
        return f'<h{lvl}{attrs}><span class="hnum">{label}</span> {inner}</h{lvl}>'

    return re.sub(r"<h([23])([^>]*)>(.*?)</h\1>", rep, html, flags=re.S), toc


def section_chunks(html, page_title, page_url):
    """Split rendered HTML into h2/h3 sections for the search index."""
    out = []
    parts = re.split(r'(<h[23][^>]*>.*?</h[23]>)', html, flags=re.S)
    cur_h, cur_id, buf = page_title, "", []

    def flush():
        txt = strip_tags(" ".join(buf))
        if txt or cur_h:
            out.append({"p": page_title, "h": cur_h, "u": page_url + (f"#{cur_id}" if cur_id else ""), "x": txt[:1400]})

    for part in parts:
        m = re.match(r'<h[23][^>]*id="([^"]+)"[^>]*>(.*?)</h[23]>', part, flags=re.S)
        if m:
            flush()
            cur_id, cur_h, buf = m.group(1), strip_tags(m.group(2)), []
        else:
            buf.append(part)
    flush()
    return out


# ------------------------------------------------------------------ page shell
def nav_html(modules, current):
    def a(href, label, key, num=None, mod=None):
        cur = ' aria-current="page"' if key == current else ""
        dm = f' data-mod-link="{mod}"' if mod else ""
        n = f'<span class="num">{num}</span>' if num is not None else ""
        return f'<a href="{href}"{cur}{dm}>{n}<span>{escape(label)}</span></a>'

    h = [a("index.html", "Learning dashboard", "home"), a("start.html", "Start here", "start"), "<h5>Product Core modules</h5>"]
    for m in modules:
        h.append(a(m["url"], m["title"], m["id"], m["n"], m["id"]))
    h.append("<h5>Libraries</h5>")
    for key, title, _, _ in COLLECTIONS:
        h.append(a(f"{key}.html", title, key))
    h.append(a("templates.html", "Templates & datasets", "templates"))
    h.append(a("glossary.html", "Glossary", "glossary"))
    h.append(a("resources.html", "References & resources", "resources"))
    h.append(a("appendix.html", "Source coverage", "appendix"))
    return "\n".join(h)


def site_page(key, title, body, modules, head="", extra_js="", pdf_link=None):
    pdf = f'<a class="iconbtn" href="{pdf_link}">⬇ PDF</a>' if pdf_link else ""
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(title)} · {TITLE}</title>
<script>try{{var t=localStorage.getItem('pmh.theme');if(t)document.documentElement.setAttribute('data-theme',t)}}catch(e){{}}</script>
<link rel="stylesheet" href="assets/style.css">{head}</head>
<body>
<a href="#content" class="noprint" style="position:absolute;left:-999px" onfocus="this.style.left='8px'">Skip to content</a>
<header class="topbar">
  <button class="iconbtn menu-toggle" id="menuBtn" aria-label="Toggle navigation" aria-expanded="false" aria-controls="sidebar">☰</button>
  <a class="brand" href="index.html"><span class="logo" aria-hidden="true"></span><span class="t">PM Master Handbook</span></a>
  <div class="searchbox"><input id="q" type="search" placeholder="Search topics, frameworks, terms…  ( / )" aria-label="Search the handbook" autocomplete="off"><div class="results" id="results" role="listbox"></div></div>
  {pdf}
  <button class="iconbtn" id="themeBtn" type="button" aria-pressed="false">☾ Dark</button>
</header>
<div class="shell">
<nav class="sidebar" id="sidebar" aria-label="Handbook navigation">{nav_html(modules, key)}
<h5>Progress</h5><div style="padding:0 9px"><div class="progressbar"><i data-overall-bar></i></div><small class="mut" style="color:var(--muted)">Modules completed: <b data-overall>0 / 12</b></small><br><button class="iconbtn" style="margin-top:8px" data-reset-progress type="button">Reset progress</button></div>
</nav>
<main class="main" id="content"><div class="article">
{body}
</div></main>
</div>
<button class="iconbtn totop" id="toTop" type="button" aria-label="Back to top">↑ Top</button>
<script src="assets/search-index.js"></script>
<script src="assets/app.js"></script>{extra_js}
</body></html>"""


def page_head(kicker, title, sub, chips=()):
    ch = "".join(f'<span class="chip">{escape(c)}</span>' for c in chips)
    return f'<header class="page-head"><div class="kicker">{escape(kicker)}</div><h1>{escape(title)}</h1><p>{escape(sub)}</p><div class="chips">{ch}</div></header>'


# ------------------------------------------------------------------ main build
def build():
    for d in (SITE, PRINT, SITE / "assets", SITE / "downloads", ROOT / "_build" / "print", ROOT / "diagrams"):
        d.mkdir(parents=True, exist_ok=True)
    for old in (ROOT / "diagrams").glob("*.svg"):
        old.unlink()
    for f in ASSETS.iterdir():
        shutil.copy(f, SITE / "assets" / f.name)

    # ---- modules
    modules = []
    for f in sorted((CONTENT / "modules").glob("m*.md")):
        meta, txt = read_md(f)
        n = int(meta["n"])
        mid = meta["id"]
        html = render_md(txt, mid, quiz_id=mid)
        html, toc = number_headings(html, n)
        modules.append({
            "id": mid, "n": n, "title": meta["title"], "subtitle": meta.get("subtitle", ""), "summary": meta.get("summary", ""),
            "hours": meta.get("hours", 6), "status": meta.get("status", "draft"), "sources": meta.get("sources", ""),
            "url": f"{mid}.html", "html": html, "toc": toc, "pdf": MODULE_FILES.get(n, f"Module-{n:02d}"),
        })
    # placeholders for modules not yet written, so navigation always shows all 12
    have = {m["n"] for m in modules}
    titles = {
        1: "Fundamentals of Product Management", 2: "Product Strategy and Strategic Thinking", 3: "Problem Discovery and Market Research",
        4: "Problem Framing and Prioritization", 5: "UX and Design Collaboration", 6: "Effective Communication and Stakeholder Management",
        7: "Product Analytics and Metrics", 8: "Product Launch, Growth, and Monetization", 9: "Tech 101 and System Design for PMs",
        10: "LLMs, RAGs, and AI Foundations", 11: "Vibe Coding for Product Managers", 12: "Agentic AI and AI Systems",
    }
    for n in range(1, 13):
        if n not in have:
            modules.append({"id": f"m{n:02d}", "n": n, "title": titles[n], "subtitle": "", "summary": "Not yet written — see PROGRESS.md.", "hours": 6,
                            "status": "not written", "sources": "", "url": f"m{n:02d}.html", "pdf": MODULE_FILES[n],
                            "html": '<div class="todo-banner"><b>Not yet written.</b> This module is planned and tracked in <code>PROGRESS.md</code>. No placeholder content is presented as finished material.</div>', "toc": [], "stub": True})
    modules.sort(key=lambda m: m["n"])

    index = []
    pdf_exists = lambda name: (ROOT / "pdf" / f"{name}.pdf").exists()

    for i, m in enumerate(modules):
        pdf_link = f"pdf/{m['pdf']}.pdf" if pdf_exists(m["pdf"]) else None
        ptoc = ""
        if m["toc"]:
            ptoc = '<details class="pagetoc" open><summary>On this page</summary><ol>' + "".join(
                f'<li><a href="#{h}">{escape(t)}</a></li>' for h, _, t in m["toc"]) + "</ol></details>"
        prev = modules[i - 1] if i else None
        nxt = modules[i + 1] if i < len(modules) - 1 else None
        nav = '<div class="modnav">' + (f'<a href="{prev["url"]}"><small>← Previous</small>Module {prev["n"]}: {escape(prev["title"])}</a>' if prev else "<span></span>") + \
              (f'<a href="{nxt["url"]}"><small>Next →</small>Module {nxt["n"]}: {escape(nxt["title"])}</a>' if nxt else "<span></span>") + "</div>"
        chips = [f"≈ {m['hours']} h study", m["status"].capitalize()]
        if m.get("sources"):
            chips.append("Sources: " + m["sources"])
        done = f'<p class="noprint"><button class="iconbtn donebtn" id="doneBtn" data-mod="{m["id"]}" aria-pressed="false" type="button">Mark module complete</button> <button class="iconbtn" id="expandAll" type="button">Expand all</button></p>'
        body = page_head(f"Module {m['n']}", m["title"], m["subtitle"] or m["summary"], chips) + done + ptoc + m["html"] + nav
        (SITE / m["url"]).write_text(site_page(m["id"], f"Module {m['n']}: {m['title']}", body, modules, pdf_link=pdf_link), encoding="utf-8")
        if not m.get("stub"):
            index += section_chunks(m["html"], f"Module {m['n']}: {m['title']}", m["url"])

    # ---- collections
    coll_data = {}
    for key, title, dirn, blurb in COLLECTIONS:
        d = CONTENT / dirn
        items = []
        for f in sorted(d.glob("*.md")) if d.exists() else []:
            for meta, txt in read_items(f):
                iid = meta.get("id", f.stem)
                html = render_md(txt, f"{key}-{iid}", quiz_id=f"{key}-{iid}")
                items.append({"id": iid, "title": meta["title"], "cat": meta.get("category", "General"), "summary": meta.get("summary", ""),
                              "order": meta.get("order", 999), "html": html, "meta": meta})
        ids = [it["id"] for it in items]
        dup = {i for i in ids if ids.count(i) > 1}
        if dup:
            raise RuntimeError(f"duplicate ids in {key}: {dup}")
        items.sort(key=lambda x: (x["order"], x["title"]))
        coll_data[key] = items
        cats = sorted({c for it in items for c in str(it["cat"]).split("|")})
        flt = '<div class="filters" data-for="' + key + '" role="group" aria-label="Filter"><button type="button" data-f="all" aria-pressed="true">All</button>' + \
              "".join(f'<button type="button" data-f="{escape(c)}" aria-pressed="false">{escape(c)}</button>' for c in cats) + "</div>" \
              '<p class="noprint"><input id="collFilterText" type="search" placeholder="Filter this page…" aria-label="Filter this page" class="iconbtn" style="min-width:260px"> <button class="iconbtn" id="expandAll" type="button">Expand all</button></p>'
        if items:
            idx = '<div class="cards noprint">' + "".join(
                f'<a class="card" href="#{key}-{it["id"]}"><span class="tag">{escape(str(it["cat"]).split("|")[0])}</span><h3>{escape(it["title"])}</h3><p>{escape(it["summary"])}</p></a>' for it in items) + "</div>"
            sections = "".join(
                f'<section class="item coll-item" id="{key}-{it["id"]}" data-cat="{escape(str(it["cat"]))}"><h2>{escape(it["title"])}</h2>{it["html"]}</section>' for it in items)
            index_html = idx + flt + sections
            for it in items:
                index += section_chunks(f'<h2 id="{key}-{it["id"]}">{escape(it["title"])}</h2>' + it["html"], title, f"{key}.html")
        else:
            index_html = '<div class="todo-banner"><b>Not yet written.</b> See <code>PROGRESS.md</code>.</div>'
        pdf_link = f"pdf/{ {'frameworks':'Framework-Library','cases':'Case-Study-Library','projects':'Practical-Projects','interview':'Interview-Handbook'}[key] }.pdf"
        pdf_link = pdf_link if (SITE / pdf_link).exists() or (ROOT / pdf_link).exists() else None
        body = page_head("Library", title, blurb, [f"{len(items)} entries"]) + index_html
        (SITE / f"{key}.html").write_text(site_page(key, title, body, modules, pdf_link=pdf_link), encoding="utf-8")

    # ---- simple pages
    simple_html = {}
    for key, title, rel in SIMPLE_PAGES:
        if key == "appendix":
            parts = []
            for fn in ("source-coverage-matrix.md", "curriculum-gap-analysis.md"):
                _, t = read_md(ROOT / fn)
                parts.append(render_md(re.sub(r"^# ", "## ", t, count=1, flags=re.M), f"app-{fn[:6]}"))
            html = "".join(parts)
        else:
            p = CONTENT / rel
            if not p.exists():
                html = '<div class="todo-banner"><b>Not yet written.</b></div>'
            else:
                meta, t = read_md(p)
                html = render_md(t, key)
        simple_html[key] = html
        body = page_head("Handbook", title, "", []) + html
        (SITE / f"{key}.html").write_text(site_page(key, title, body, modules), encoding="utf-8")
        index += section_chunks(html, title, f"{key}.html")

    # ---- templates & datasets
    tdir, ddir = ROOT / "templates", ROOT / "datasets"
    t_html = ['<p>Reusable artefacts. Open them here or download the Markdown file and paste it into Docs, Notion, Confluence or Jira.</p>']
    tfiles = sorted(tdir.glob("*.md")) if tdir.exists() else []
    starter = tdir / "vibe-coding-starter"
    if starter.exists():
        dst = SITE / "downloads" / "vibe-coding-starter"
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(starter, dst)
        shutil.make_archive(str(SITE / "downloads" / "vibe-coding-starter"), "zip", starter)
        t_html.append('<div class="admonition tip"><p class="admonition-title">Hands-on starter (Module 11)</p><p>'
                      '<a href="downloads/vibe-coding-starter/index.html">Open the Fee-Clear Cart prototype</a> · '
                      '<a href="downloads/vibe-coding-starter.zip" download>Download the starter (.zip)</a> — plain HTML/CSS/JS, fictional data, no real payments.</p></div>')
    for f in tfiles:
        shutil.copy(f, SITE / "downloads" / f.name)
        meta, t = read_md(f)
        ttl = meta.get("title", f.stem.replace("-", " ").title())
        body_html = render_md(demote(t), f"tpl-{f.stem}")
        t_html.append(f'<details><summary>{escape(ttl)}</summary><p class="noprint"><a href="downloads/{f.name}" download>⬇ Download {f.name}</a></p>{body_html}</details>')
        index += section_chunks(f'<h2 id="tpl-{f.stem}">{escape(ttl)}</h2>' + body_html, "Templates", "templates.html")
    dfiles = sorted(ddir.glob("*.csv")) if ddir.exists() else []
    t_html.append("<h2>Sample datasets</h2><p>All datasets are <b>synthetic, hypothetical</b> and generated for teaching. They are not real company data.</p><ul>")
    for f in dfiles:
        shutil.copy(f, SITE / "downloads" / f.name)
        t_html.append(f'<li><a href="downloads/{f.name}" download>{f.name}</a> — {sum(1 for _ in f.open(encoding="utf-8")) - 1} rows</li>')
    t_html.append("</ul>")
    tbody = page_head("Library", "Templates & Datasets", "Reusable PM templates and synthetic practice data.", [f"{len(tfiles)} templates", f"{len(dfiles)} datasets"]) + "".join(t_html)
    (SITE / "templates.html").write_text(site_page("templates", "Templates & datasets", tbody, modules), encoding="utf-8")

    # ---- glossary
    g = yaml.safe_load((CONTENT / "glossary.yaml").read_text(encoding="utf-8")) if (CONTENT / "glossary.yaml").exists() else []
    g.sort(key=lambda x: x["term"].lower())
    gl = '<p class="noprint"><input id="glossFilter" type="search" class="iconbtn" style="min-width:280px" placeholder="Search terms…" aria-label="Search glossary"></p><dl class="glossary">' + "".join(
        f'<div class="term"><dt id="g-{re.sub(r"[^a-z0-9]+", "-", x["term"].lower()).strip("-")}">{escape(x["term"])}</dt><dd>{escape(x["def"])}' +
        (f' <small>(Module {x["module"]})</small>' if x.get("module") else "") + "</dd></div>" for x in g) + "</dl>"
    for x in g:
        index.append({"p": "Glossary", "h": x["term"], "u": "glossary.html#g-" + re.sub(r"[^a-z0-9]+", "-", x["term"].lower()).strip("-"), "x": x["def"][:600]})
    gbody = page_head("Reference", "Glossary", "Searchable definitions of PM, analytics, technical and AI terms.", [f"{len(g)} terms"]) + gl
    (SITE / "glossary.html").write_text(site_page("glossary", "Glossary", gbody, modules), encoding="utf-8")

    # ---- dashboard
    js_modules = [{"id": m["id"], "n": m["n"], "title": m["title"], "summary": m["summary"], "hours": m["hours"], "status": m["status"], "url": m["url"]} for m in modules]
    written = sum(1 for m in modules if not m.get("stub"))
    lib = "".join(f'<a class="card" href="{k}.html"><span class="tag">Library</span><h3>{escape(t)}</h3><p>{escape(b)}</p><div class="meta">{len(coll_data[k])} entries</div></a>' for k, t, _, b in COLLECTIONS)
    lib += '<a class="card" href="templates.html"><span class="tag">Library</span><h3>Templates &amp; datasets</h3><p>Reusable PM artefacts and synthetic practice data.</p></a>'
    lib += '<a class="card" href="glossary.html"><span class="tag">Reference</span><h3>Glossary</h3><p>Searchable definitions.</p></a>'
    dash = f"""<section class="hero"><div class="kicker">{VERSION}</div><h1>{TITLE}</h1>
<p>A visual, interactive study system built from your 55-lecture course notes and extended to the 12 Product Core modules. Progress is saved in this browser only.</p>
<div class="stat"><div><b data-overall>0 / 12</b>modules completed</div><div><b>{written} / 12</b>modules written</div><div><b id="totalHours">—</b>planned study time</div></div>
<div class="progressbar" style="margin-top:14px"><i data-overall-bar></i></div><p id="currentFocus" style="margin-top:10px"></p></section>
<h2>Learning dashboard</h2><div class="cards" id="dashModules"></div>
<h2>Libraries</h2><div class="cards">{lib}</div>
<p class="noprint"><small>Hypothetical examples are labelled. Company facts are limited to widely known public information; verify before quoting.</small></p>"""
    (SITE / "index.html").write_text(site_page("home", "Learning dashboard", dash, modules), encoding="utf-8")

    # ---- search index + data
    (SITE / "assets" / "search-index.js").write_text("window.PMH=" + json.dumps({"modules": js_modules, "index": index}, ensure_ascii=False) + ";", encoding="utf-8")

    # ---- copy pdfs into site if present
    (SITE / "pdf").mkdir(exist_ok=True)
    for f in (ROOT / "pdf").glob("*.pdf"):
        shutil.copy(f, SITE / "pdf" / f.name)

    # ---- print documents (inputs for pdf.py)
    write_print(modules, coll_data, simple_html, g, tfiles)

    # ---- project entry point
    write_root_index(modules, coll_data)
    print(f"built: {written}/12 modules written; " + ", ".join(f"{k}:{len(v)}" for k, v in coll_data.items()) + f"; templates:{len(tfiles)}; datasets:{len(dfiles)}; glossary:{len(g)}; search sections:{len(index)}")


# ------------------------------------------------------------------ print documents
def print_doc(title, body, css="../assets/style.css"):
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{escape(title)}</title>
<link rel="stylesheet" href="{css}"></head><body class="print" data-theme="light"><div class="article">{body}</div></body></html>"""


def cover(title, subtitle, extra=""):
    return f"""<section class="cover"><div><div class="stripe"></div><h1>{escape(title)}</h1><div class="sub">{escape(subtitle)}</div></div>
<div class="meta">{extra}<br>{VERSION}<br>Built from the 55-lecture course study guide and extended to the 12-module Product Core curriculum.<br>
Hypothetical examples are labelled; no real company results are invented.</div></section>"""


def write_print(modules, coll_data, simple_html, glossary, tfiles):
    PRINT.mkdir(parents=True, exist_ok=True)

    def mod_block(m, first=False):
        if m.get("stub"):
            return ""
        h = page_head_print(f"Module {m['n']}", m["title"], m["subtitle"] or m["summary"], [f"≈ {m['hours']} h study"])
        return f'<section class="module-start" id="{m["id"]}">{h}{m["html"]}</section>'

    def coll_block(key, title, intro, num):
        items = coll_data.get(key, [])
        if not items:
            return "", []
        inner = "".join(f'<section class="coll-item" id="{key}-{it["id"]}"><h2>{escape(it["title"])}</h2>{it["html"]}</section>' for it in items)
        h = page_head_print("Part", title, intro, [f"{len(items)} entries"])
        return f'<section class="module-start" id="{key}-part">{h}{inner}</section>', [(f"{key}-{it['id']}", it["title"]) for it in items]

    # per-module PDFs
    for m in modules:
        if m.get("stub"):
            continue
        body = cover(f"Module {m['n']}: {m['title']}", m["subtitle"] or m["summary"], "Product Management Master Handbook") + \
            '<section class="toc-page"><h1>Contents</h1><ul class="toc-list">' + \
            "".join(f'<li class="l2" data-find="{escape(t)}"><span>{lab} {escape(t)}</span><span class="dots"></span><span class="pg">·</span></li>' for _, lab, t in m["toc"]) + "</ul></section>" + \
            mod_block(m)
        (PRINT / f"{m['pdf']}.html").write_text(print_doc(f"Module {m['n']}", body), encoding="utf-8")

    # complete handbook
    toc = []
    blocks = []
    start_html = simple_html.get("start", "")
    if start_html:
        blocks.append(f'<section class="module-start" id="start">{page_head_print("Handbook", "Start Here", "", [])}{start_html}</section>')
        toc.append((1, "Start Here", "start"))
    for m in modules:
        if m.get("stub"):
            continue
        blocks.append(mod_block(m))
        toc.append((1, f"Module {m['n']}: {m['title']}", m["id"]))
        for h, lab, t in m["toc"]:
            toc.append((2, f"{lab} {t}", h))
    for key, title, _, blurb in COLLECTIONS:
        b, ents = coll_block(key, title, blurb, 0)
        if b:
            blocks.append(b)
            toc.append((1, title, f"{key}-part"))
            for iid, t in ents:
                toc.append((2, t, iid))
    # templates, glossary, resources, appendix
    if tfiles:
        tb = "".join(f'<section class="coll-item"><h2>{escape(read_md(f)[0].get("title", f.stem))}</h2>{render_md(demote(read_md(f)[1]), "ptpl-" + f.stem)}</section>' for f in tfiles)
        blocks.append(f'<section class="module-start" id="templates-part">{page_head_print("Part", "Templates", "Reusable PM artefacts.", [])}{tb}</section>')
        toc.append((1, "Templates", "templates-part"))
    gl = '<dl class="glossary">' + "".join(f'<div class="term"><dt>{escape(x["term"])}</dt><dd>{escape(x["def"])}</dd></div>' for x in glossary) + "</dl>"
    blocks.append(f'<section class="module-start" id="glossary-part">{page_head_print("Reference", "Glossary", "", [])}{gl}</section>')
    toc.append((1, "Glossary", "glossary-part"))
    for key, t in (("resources", "References & Resources"), ("appendix", "Appendix: Source Coverage & Gap Analysis")):
        if simple_html.get(key):
            blocks.append(f'<section class="module-start" id="{key}-part">{page_head_print("Part", t, "", [])}{simple_html[key]}</section>')
            toc.append((1, t, f"{key}-part"))
    toc_html = '<section class="toc-page"><h1>Table of contents</h1><ul class="toc-list">' + "".join(
        f'<li class="l{lv}" data-find="{escape(t)}"><a href="#{a}"><span>{escape(t)}</span></a><span class="dots"></span><span class="pg" data-pg="{a}">·</span></li>' for lv, t, a in toc) + "</ul></section>"
    body = cover(TITLE, "From fundamentals to agentic AI: a visual study system for aspiring and working Product Managers") + toc_html + "".join(blocks)
    (PRINT / "Complete-PM-Master-Handbook.html").write_text(print_doc(TITLE, body), encoding="utf-8")
    json.dump({"toc": toc}, open(PRINT / "complete-toc.json", "w", encoding="utf-8"))

    for key, fn in (("frameworks", "Framework-Library"), ("cases", "Case-Study-Library"), ("projects", "Practical-Projects"), ("interview", "Interview-Handbook")):
        t = next(c[1] for c in COLLECTIONS if c[0] == key)
        b, ents = coll_block(key, t, next(c[3] for c in COLLECTIONS if c[0] == key), 0)
        if b:
            body = cover(t, next(c[3] for c in COLLECTIONS if c[0] == key), "Product Management Master Handbook") + b.replace("module-start", "", 1)
            (PRINT / f"{fn}.html").write_text(print_doc(t, body), encoding="utf-8")


def page_head_print(kicker, title, sub, chips):
    return page_head(kicker, title, sub, chips)


def write_root_index(modules, coll_data):
    rows = []
    for m in modules:
        pdf = f'<a href="pdf/{m["pdf"]}.pdf">PDF</a>' if (ROOT / "pdf" / f'{m["pdf"]}.pdf').exists() else '<span style="color:#98A2B3">PDF pending</span>'
        st = "written" if not m.get("stub") else "not yet written"
        rows.append(f'<tr><td>{m["n"]}</td><td><a href="html/Interactive-PM-Handbook/{m["url"]}">{escape(m["title"])}</a></td><td>{st}</td><td>{pdf}</td></tr>')
    comp = '<a href="pdf/Complete-PM-Master-Handbook.pdf">Complete handbook (PDF)</a>' if (ROOT / "pdf" / "Complete-PM-Master-Handbook.pdf").exists() else "Complete handbook PDF — pending"
    html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{TITLE}</title>
<style>body{{font:16px/1.6 "Segoe UI",system-ui,sans-serif;margin:0;color:#101828;background:#fff}}main{{max-width:900px;margin:0 auto;padding:32px 20px}}h1{{margin:.2em 0}}
.hero{{background:linear-gradient(135deg,#101828,#1d3a8a 60%,#7C3AED 140%);color:#fff;border-radius:16px;padding:28px}}.hero a{{color:#fff;font-weight:700}}
table{{border-collapse:collapse;width:100%}}td,th{{border-bottom:1px solid #E4E7EC;padding:8px;text-align:left}}a{{color:#2563EB}}ul{{padding-left:1.2em}}</style></head><body><main>
<div class="hero"><h1>{TITLE}</h1><p>{VERSION}</p><p><a href="html/Interactive-PM-Handbook/index.html">Open the interactive handbook →</a></p></div>
<h2>Modules</h2><table><thead><tr><th>#</th><th>Module (HTML)</th><th>Status</th><th>PDF</th></tr></thead><tbody>{"".join(rows)}</tbody></table>
<h2>Libraries</h2><ul>
<li><a href="html/Interactive-PM-Handbook/frameworks.html">Framework library</a> ({len(coll_data.get("frameworks", []))})</li>
<li><a href="html/Interactive-PM-Handbook/cases.html">Case studies</a> ({len(coll_data.get("cases", []))})</li>
<li><a href="html/Interactive-PM-Handbook/projects.html">Practical projects</a> ({len(coll_data.get("projects", []))})</li>
<li><a href="html/Interactive-PM-Handbook/interview.html">Interview handbook</a> ({len(coll_data.get("interview", []))} sets)</li>
<li><a href="html/Interactive-PM-Handbook/templates.html">Templates &amp; datasets</a></li>
<li><a href="html/Interactive-PM-Handbook/glossary.html">Glossary</a></li></ul>
<h2>Project files</h2><ul><li>{comp}</li><li><a href="README.md">README</a> · <a href="PROGRESS.md">PROGRESS</a> · <a href="source-coverage-matrix.md">Source coverage matrix</a> · <a href="curriculum-gap-analysis.md">Curriculum gap analysis</a></li>
<li><a href="validation-reports/">Validation reports</a></li></ul></main></body></html>"""
    (ROOT / "index.html").write_text(html, encoding="utf-8")


if __name__ == "__main__":
    build()
