"""PDF quality checks: blank pages, text past the right margin, links, bookmarks. Writes validation-reports/pdf-qa.md.

    python -I _build/pdf_qa.py [render-sample]
"""
import sys
from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parent.parent
PDF = ROOT / "pdf"
REP = ROOT / "validation-reports"
RIGHT_LIMIT = 595.3 - 15 * 72 / 25.4 + 4   # A4 width minus right margin, plus 4pt tolerance

lines = ["# PDF QA report", "", "| File | Pages | Bookmarks | Link annotations | Near-blank pages | Pages with text past right margin |", "|---|---:|---:|---:|---|---|"]
issues_total = 0
for f in sorted(PDF.glob("*.pdf")):
    d = pymupdf.open(str(f))
    blank, overflow, links = [], [], 0
    for i, p in enumerate(d):
        txt = p.get_text().strip()
        body = txt.replace("Product Management Master Handbook", "").strip()
        if len(body) < 40 and not p.get_images() and len(p.get_drawings()) < 3:
            blank.append(i + 1)
        for b in p.get_text("dict")["blocks"]:
            for l in b.get("lines", []):
                for s in l["spans"]:
                    if s["text"].strip() and s["bbox"][2] > RIGHT_LIMIT:
                        overflow.append(i + 1)
                        break
        links += len(p.get_links())
    overflow = sorted(set(overflow))
    issues_total += len(blank) + len(overflow)
    lines.append(f"| {f.name} | {len(d)} | {len(d.get_toc())} | {links} | {', '.join(map(str, blank)) or '—'} | {', '.join(map(str, overflow[:15])) or '—'}{' …' if len(overflow) > 15 else ''} |")
    if "render-sample" in sys.argv and f.stem.startswith("Complete"):
        out = Path(sys.argv[-1]) if len(sys.argv) > 2 else REP
        for i in list(range(0, 6)) + [len(d) // 4, len(d) // 2, 3 * len(d) // 4, len(d) - 3, len(d) - 1]:
            d[i].get_pixmap(dpi=55).save(str(out / f"complete_p{i + 1:03d}.png"))
lines += ["", f"Total flagged pages: {issues_total}. Near-blank = fewer than 40 characters of body text and no images/drawings."]
(REP / "pdf-qa.md").write_text("\n".join(lines), encoding="utf-8")
print("\n".join(lines))
