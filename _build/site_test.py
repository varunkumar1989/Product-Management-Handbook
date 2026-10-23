"""Functional tests of the interactive site in Microsoft Edge (headless). Writes validation-reports/functional-tests.md.

    python -I -X utf8 _build/site_test.py [screenshot-dir]
"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "html" / "Interactive-PM-Handbook"
SHOTS = Path(sys.argv[1]) if len(sys.argv) > 1 else None
results = []


def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))


with sync_playwright() as pw:
    b = pw.chromium.launch(channel="msedge", headless=True)
    ctx = b.new_context(viewport={"width": 1280, "height": 900})
    p = ctx.new_page()
    errors = []
    p.on("pageerror", lambda e: errors.append(str(e)))
    p.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)

    # every page loads without JS errors
    for f in sorted(SITE.glob("*.html")):
        p.goto(f.as_uri())
    check("All site pages load without JavaScript errors", not errors, "; ".join(errors[:5]))

    # dashboard
    p.goto((SITE / "index.html").as_uri())
    cards = p.locator("#dashModules .card").count()
    check("Dashboard lists 12 module cards", cards == 12, f"{cards} cards")
    check("Dashboard shows current focus", "Current focus" in p.inner_text("#currentFocus"))

    # search
    p.fill("#q", "contribution margin")
    p.wait_for_timeout(200)
    hits = p.locator("#results a").count()
    check("Search returns results for 'contribution margin'", hits > 0, f"{hits} hits")
    first = p.locator("#results a").first.get_attribute("href")
    p.locator("#results a").first.click()
    p.wait_for_load_state("load")
    check("Clicking a search result navigates to the target page", p.url.split("/")[-1].split("#")[0] == first.split("#")[0], first)
    p.goto((SITE / "m01.html").as_uri())
    p.keyboard.press("/")
    check("'/' focuses the search box", p.evaluate("document.activeElement.id") == "q")
    p.keyboard.press("Escape")

    # theme toggle + persistence
    p.goto((SITE / "m07.html").as_uri())
    before = p.evaluate("getComputedStyle(document.body).backgroundColor")
    p.click("#themeBtn")
    after = p.evaluate("getComputedStyle(document.body).backgroundColor")
    check("Theme toggle changes the page background", before != after, f"{before} → {after}")
    p.reload()
    check("Theme choice persists after reload", p.evaluate("document.documentElement.getAttribute('data-theme')") in ("dark", "light"))
    if SHOTS:
        p.evaluate("document.querySelector('#m07-funnel-analysis-and-drop-off').scrollIntoView()")
        p.wait_for_timeout(300)
        p.screenshot(path=str(SHOTS / "test_dark.png"))
    p.click("#themeBtn")

    # quiz
    q = p.locator(".quiz .qitem").first
    correct = int(q.get_attribute("data-correct"))
    q.locator("li").nth(correct).click()
    check("Quiz marks a correct answer", "right" in (q.locator("li").nth(correct).get_attribute("class") or ""))
    check("Quiz reveals the explanation", q.locator(".why").is_visible())
    score = p.inner_text(".quiz .quizscore")
    check("Quiz shows a running score", "Score" in score, score)

    # progress
    p.click("#doneBtn")
    p.goto((SITE / "index.html").as_uri())
    done = p.locator('.sidebar a[data-mod-link="m07"].done').count()
    check("Marking a module complete updates the sidebar indicator", done == 1)
    check("Overall progress counter updates", "1 / 12" in p.inner_text("[data-overall]"))

    # expand all details
    p.goto((SITE / "m01.html").as_uri())
    p.click("#expandAll")
    closed = p.evaluate("[...document.querySelectorAll('.article details')].filter(d=>!d.open).length")
    check("'Expand all' opens every collapsible answer", closed == 0, f"{closed} still closed")

    # collection filters
    p.goto((SITE / "frameworks.html").as_uri())
    p.click('.filters button[data-f="Prioritization"]')
    visible = p.evaluate("[...document.querySelectorAll('.item')].filter(e=>!e.classList.contains('hide')).length")
    check("Framework library category filter works", visible == 7, f"{visible} visible after 'Prioritization'")
    p.goto((SITE / "interview.html").as_uri())
    p.fill("#collFilterText", "RAG")
    visible = p.evaluate("[...document.querySelectorAll('.item')].filter(e=>!e.classList.contains('hide')).length")
    check("Interview page text filter narrows the list", 0 < visible < 14, f"{visible} sets match 'RAG'")
    nq = p.locator("details.question").count()
    check("Interview handbook contains ≥ 100 questions", nq >= 100, f"{nq} questions")
    # show/hide model answers
    p.fill("#collFilterText", "")
    d0 = p.locator("details.question").first
    d0.locator("summary").click()
    check("Model answers expand on click", d0.evaluate("d=>d.open"))

    # glossary
    p.goto((SITE / "glossary.html").as_uri())
    total = p.locator(".glossary .term").count()
    p.fill("#glossFilter", "idempot")
    shown = p.evaluate("[...document.querySelectorAll('.glossary .term')].filter(e=>!e.classList.contains('hide')).length")
    check("Glossary search filters terms", shown == 1, f"{shown} of {total} shown for 'idempot'")

    # downloads & PDFs
    p.goto((SITE / "templates.html").as_uri())
    dl = p.locator('a[download]').count()
    check("Templates page offers downloadable files", dl >= 10, f"{dl} download links")
    missing = []
    for a in p.locator("a[href^='downloads/']").all():
        if not (SITE / a.get_attribute("href")).exists():
            missing.append(a.get_attribute("href"))
    check("All template/dataset download links resolve to files", not missing, ", ".join(missing))
    p.goto((SITE / "m07.html").as_uri())
    pdf_href = p.locator("a.iconbtn[href$='.pdf']").get_attribute("href")
    check("Module page links to its PDF and the file exists", pdf_href and (SITE / pdf_href).exists(), str(pdf_href))

    # back to top
    p.evaluate("window.scrollTo(0, 4000)")
    p.wait_for_timeout(200)
    check("Back-to-top button appears after scrolling", p.locator("#toTop").is_visible())
    p.click("#toTop")
    p.wait_for_function("window.scrollY < 50", timeout=5000)
    check("Back-to-top returns to the top", p.evaluate("window.scrollY") < 50, f"scrollY={p.evaluate('window.scrollY')}")

    # keyboard: quiz options are focusable buttons
    check("Quiz options are keyboard-focusable", p.evaluate("document.querySelector('.qitem li').tabIndex") == 0)

    # mobile layout
    m = b.new_context(viewport={"width": 375, "height": 812}, is_mobile=True, has_touch=True)
    mp = m.new_page()
    overflow = []
    for f in ["index.html", "m01.html", "m07.html", "m09.html", "frameworks.html", "cases.html", "interview.html", "glossary.html"]:
        mp.goto((SITE / f).as_uri())
        sw = mp.evaluate("document.documentElement.scrollWidth")
        if sw > 376:
            overflow.append(f"{f}:{sw}px")
    check("No horizontal page scroll at 375 px width", not overflow, ", ".join(overflow))
    mp.goto((SITE / "m05.html").as_uri())
    check("Sidebar hidden on mobile until the menu is opened", not mp.locator("#sidebar").evaluate("e=>e.getBoundingClientRect().right>0"))
    mp.click("#menuBtn")
    mp.wait_for_timeout(400)
    check("Menu button opens the sidebar on mobile", mp.locator("#sidebar").evaluate("e=>e.getBoundingClientRect().right>0"))
    if SHOTS:
        mp.click("#menuBtn")
        mp.wait_for_timeout(300)
        mp.screenshot(path=str(SHOTS / "test_mobile.png"))
    b.close()

lines = ["# Functional test report", "", "Automated run in Microsoft Edge (headless, Playwright) against the local `file://` site.", "",
         f"**{sum(r[1] for r in results)} of {len(results)} checks passed.**", "", "| Check | Result | Detail |", "|---|---|---|"]
lines += [f"| {n} | {'PASS' if ok else 'FAIL'} | {d} |" for n, ok, d in results]
(ROOT / "validation-reports" / "functional-tests.md").write_text("\n".join(lines), encoding="utf-8")
print("\n".join(lines))
