"""Validation checks for the handbook. Writes reports to validation-reports/.

    python -I _build/validate.py [--no-links]
"""
import csv, re, sqlite3, sys, json, urllib.request, urllib.error, ssl, concurrent.futures as cf
from pathlib import Path
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "html" / "Interactive-PM-Handbook"
REP = ROOT / "validation-reports"
REP.mkdir(exist_ok=True)


# ------------------------------------------------------------------ SQL examples
def check_sql():
    con = sqlite3.connect(":memory:")
    for t in ("users", "events", "orders"):
        rows = list(csv.reader(open(ROOT / "datasets" / f"{t}.csv", encoding="utf-8")))
        con.execute(f"create table {t} ({','.join(rows[0])})")
        con.executemany(f"insert into {t} values ({','.join('?' * len(rows[0]))})", rows[1:])
    out = ["# SQL example check", "", "Every ```sql block in content/ executed against the synthetic datasets with SQLite.", ""]
    ok = bad = 0
    for f in sorted((ROOT / "content").rglob("*.md")):
        for i, m in enumerate(re.finditer(r"```sql\n(.*?)```", f.read_text(encoding="utf-8"), re.S)):
            q = m.group(1).strip()
            try:
                res = con.execute(q).fetchall()
                ok += 1
                out.append(f"- PASS `{f.relative_to(ROOT)}` #{i + 1}: {len(res)} row(s); first: `{res[0] if res else '—'}`")
            except Exception as e:
                bad += 1
                out.append(f"- FAIL `{f.relative_to(ROOT)}` #{i + 1}: {e}")
    out.insert(3, f"**Result: {ok} passed, {bad} failed.**\n")
    (REP / "sql-check.md").write_text("\n".join(out), encoding="utf-8")
    return ok, bad


# ------------------------------------------------------------------ internal links / anchors in the site
class Collector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.hrefs = set(), []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "a" and "href" in a:
            self.hrefs.append(a["href"])


def check_site():
    pages = {}
    for p in SITE.glob("*.html"):
        c = Collector()
        c.feed(p.read_text(encoding="utf-8"))
        pages[p.name] = c
    problems, n_links, ext = [], 0, set()
    for name, c in pages.items():
        for h in c.hrefs:
            if h.startswith(("http://", "https://")):
                ext.add(h)
                continue
            if h.startswith(("mailto:", "javascript:")):
                continue
            n_links += 1
            target, _, frag = h.partition("#")
            if target == "":
                target = name
            path = (SITE / target)
            if not path.exists():
                problems.append(f"{name}: missing file → {h}")
                continue
            if frag and target in pages and frag not in pages[target].ids:
                problems.append(f"{name}: missing anchor → {h}")
    # figure counts per module
    figs = []
    for p in sorted(SITE.glob("m*.html")):
        t = p.read_text(encoding="utf-8")
        figs.append((p.name, t.count('class="viz'), t.count("<h2"), t.count('class="quiz"'), t.count("todo-banner")))
    out = ["# Site checks", "", f"Pages: {len(pages)} · internal links checked: {n_links} · problems: {len(problems)}", ""]
    out += [f"- {x}" for x in problems] or ["- No broken internal links or anchors."]
    out += ["", "## Visuals per module", "", "| Page | Figures | Sections (h2) | Quizzes | Placeholder banners |", "|---|---:|---:|---:|---:|"]
    out += [f"| {a} | {b} | {c} | {d} | {e} |" for a, b, c, d, e in figs]
    (REP / "site-checks.md").write_text("\n".join(out), encoding="utf-8")
    return problems, ext


# ------------------------------------------------------------------ external links
def check_links(urls):
    ctx = ssl.create_default_context()
    hdr = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"}

    def one(u):
        for method in ("HEAD", "GET"):
            try:
                req = urllib.request.Request(u, headers=hdr, method=method)
                with urllib.request.urlopen(req, timeout=20, context=ctx) as r:
                    return u, r.status, r.geturl()
            except urllib.error.HTTPError as e:
                if method == "GET" or e.code not in (403, 405, 400, 404, 429):
                    return u, e.code, ""
            except Exception as e:
                if method == "GET":
                    return u, f"error: {type(e).__name__}", ""
        return u, "unknown", ""

    with cf.ThreadPoolExecutor(12) as ex:
        res = sorted(ex.map(one, sorted(urls)), key=lambda x: str(x[1]))
    ok = [r for r in res if isinstance(r[1], int) and r[1] < 400]
    blocked = [r for r in res if r[1] in (401, 403, 429)]
    broken = [r for r in res if r not in ok and r not in blocked]
    out = ["# External link check", "", f"Checked {len(res)} unique URLs: **{len(ok)} OK**, **{len(blocked)} blocked automated access (manual check needed)**, **{len(broken)} failed**.", "",
           "| Status | URL | Final URL (if redirected) |", "|---|---|---|"]
    out += [f"| {s} | {u} | {f if f and f != u else ''} |" for u, s, f in res]
    (REP / "link-check.md").write_text("\n".join(out), encoding="utf-8")
    return ok, blocked, broken


if __name__ == "__main__":
    ok, bad = check_sql()
    print(f"SQL: {ok} passed, {bad} failed")
    problems, ext = check_site()
    print(f"Site: {len(problems)} internal link problems; {len(ext)} external URLs")
    for p in problems[:20]:
        print("  ", p)
    if "--no-links" not in sys.argv:
        ok_, blocked, broken = check_links(ext)
        print(f"Links: {len(ok_)} ok, {len(blocked)} blocked, {len(broken)} failed")
        for u, s, _ in broken:
            print("  BROKEN", s, u)
        for u, s, _ in blocked:
            print("  BLOCKED", s, u)
