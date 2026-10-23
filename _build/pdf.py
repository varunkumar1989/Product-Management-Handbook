#!/usr/bin/env python
"""Render _build/print/*.html to A4 PDFs with bookmarks, page numbers and a filled-in TOC.

    python -I _build/pdf.py [Name ...]      # names without .html; default = all
Uses the installed Microsoft Edge via Playwright (no browser download).
"""
import sys, json, re
from pathlib import Path
import pymupdf
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
PRINT = ROOT / "_build" / "print"
OUT = ROOT / "pdf"
OUT.mkdir(exist_ok=True)

FOOTER = ('<div style="font-size:8px;width:100%;text-align:center;color:#667085;font-family:Segoe UI,Arial">'
          'Product Management Master Handbook &nbsp;·&nbsp; page <span class="pageNumber"></span> of <span class="totalPages"></span></div>')


def render(page, html_path, pdf_path):
    page.goto(html_path.as_uri(), wait_until="load")
    page.emulate_media(media="print")
    page.evaluate("document.querySelectorAll('details').forEach(d=>d.open=true)")
    page.wait_for_timeout(300)
    page.pdf(path=str(pdf_path), format="A4", print_background=True, display_header_footer=True,
             footer_template=FOOTER, header_template="<span></span>", outline=True, tagged=True,
             margin={"top": "16mm", "bottom": "18mm", "left": "15mm", "right": "15mm"})


def fill_toc(page, pdf_path):
    """Find page numbers for each TOC entry in the first-pass PDF and write them into the DOM."""
    entries = page.evaluate("[...document.querySelectorAll('.toc-list li')].map(li=>({find:li.dataset.find,lvl:li.className}))")
    if not entries:
        return False
    doc = pymupdf.open(str(pdf_path))
    # last TOC page = last page containing the end marker
    end = 0
    for i, p in enumerate(doc):
        if p.search_for("§§END-OF-TOC§§"):
            end = i
    ptr = end + 1
    nums = []
    for e in entries:
        text = e["find"]
        key = text.split(": ", 1)[-1] if text.startswith("Module ") else text
        found = None
        for i in range(ptr, len(doc)):
            if doc[i].search_for(key[:70]) or doc[i].search_for(text[:70]):
                found = i
                break
        if found is None:
            nums.append("–")
        else:
            ptr = found
            nums.append(str(found + 1))
    page.evaluate("(nums)=>{document.querySelectorAll('.toc-list li .pg').forEach((el,i)=>el.textContent=nums[i])}", nums)
    return True


PDF_OPTS = dict(format="A4", print_background=True, display_header_footer=True, footer_template=FOOTER,
                header_template="<span></span>", outline=True, tagged=True,
                margin={"top": "16mm", "bottom": "18mm", "left": "15mm", "right": "15mm"})


def clean_outline(page, pdf_path):
    """Chromium's tagged outline can duplicate or glue heading text; rebuild titles from the DOM."""
    dom = page.evaluate("""[...document.querySelectorAll('h1,h2,h3')]
        .filter(h=>!h.closest('figure') && !h.closest('.toc-page') && !h.closest('.cover'))
        .map(h=>({lvl:+h.tagName[1], text:h.innerText.replace(/\\s+/g,' ').trim(), id:h.id||''}))""")
    doc = pymupdf.open(str(pdf_path))
    toc_end = -1
    for i, p in enumerate(doc):
        if p.search_for("§§END-OF-TOC§§"):
            toc_end = i
    # locate each heading's page by searching forward through the document text (after the contents pages)
    toc, ptr = [], toc_end + 1
    if toc_end >= 0:
        toc.append([1, "Contents", 2 if toc_end >= 1 else 1])
    for h in dom:
        txt = h["text"]
        key = txt.split(" ", 1)[1] if re.match(r"^\d+(\.\d+)+ ", txt) else txt
        key = key[:60]
        found = None
        for i in range(ptr, len(doc)):
            if doc[i].search_for(key):
                found = i
                break
        if found is None:
            continue
        ptr = found
        toc.append([h["lvl"], txt, found + 1])
    # levels must start at 1 and not jump by more than one
    fixed, prev = [], 0
    for lvl, t, p in toc:
        lvl = max(1, min(lvl, prev + 1))
        fixed.append([lvl, t, p])
        prev = lvl
    doc.set_toc(fixed)
    tmp = pdf_path.with_suffix(".tmp.pdf")
    doc.save(str(tmp), garbage=3, deflate=True)
    doc.close()
    tmp.replace(pdf_path)
    return len(fixed)


def main(names):
    files = [PRINT / f"{n}.html" for n in names] if names else sorted(PRINT.glob("*.html"))
    with sync_playwright() as pw:
        browser = pw.chromium.launch(channel="msedge", headless=True)
        ctx = browser.new_context()
        page = ctx.new_page()
        for f in files:
            out = OUT / (f.stem + ".pdf")
            page.goto(f.as_uri(), wait_until="load")
            page.evaluate("""()=>{const t=document.querySelector('.toc-page');if(t){const s=document.createElement('div');
              s.textContent='§§END-OF-TOC§§';s.style.cssText='font-size:1px;color:#fff;height:1px;overflow:hidden';t.appendChild(s)}}""")
            page.emulate_media(media="print")
            page.evaluate("document.querySelectorAll('details').forEach(d=>d.open=true)")
            page.wait_for_timeout(300)
            page.pdf(path=str(out), **PDF_OPTS)
            if fill_toc(page, out):
                page.pdf(path=str(out), **PDF_OPTS)
            n = clean_outline(page, out)
            d = pymupdf.open(str(out))
            print(f"{out.name}: {len(d)} pages, {n} bookmarks, {out.stat().st_size // 1024} KB")
            d.close()
        browser.close()


if __name__ == "__main__":
    main(sys.argv[1:])
