"""Screenshot helper: python -I _build/shot.py <file-or-url> <out.png> [width] [height] [full] [dark] [clipY clipH]"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

src, out = sys.argv[1], sys.argv[2]
w = int(sys.argv[3]) if len(sys.argv) > 3 else 1280
h = int(sys.argv[4]) if len(sys.argv) > 4 else 900
full = "full" in sys.argv[5:]
dark = "dark" in sys.argv[5:]
url = src if "://" in src else Path(src).resolve().as_uri()
with sync_playwright() as pw:
    b = pw.chromium.launch(channel="msedge", headless=True)
    ctx = b.new_context(viewport={"width": w, "height": h}, color_scheme="dark" if dark else "light")
    p = ctx.new_page()
    msgs = []
    p.on("console", lambda m: msgs.append(f"{m.type}: {m.text}") if m.type in ("error", "warning") else None)
    p.on("pageerror", lambda e: msgs.append(f"pageerror: {e}"))
    p.goto(url, wait_until="load")
    anchor = next((a for a in sys.argv[5:] if a.startswith("#")), None)
    if anchor:
        p.add_style_tag(content="html{scroll-behavior:auto !important}")
        p.evaluate(f"document.querySelector('{anchor}').scrollIntoView({{behavior:'instant',block:'start'}})")
        p.wait_for_timeout(700)
    if "figs" in sys.argv[5:]:
        figs = p.query_selector_all("figure.viz")
        for i, f in enumerate(figs):
            f.scroll_into_view_if_needed()
            f.screenshot(path=out.replace(".png", f"_{i:02d}.png"))
        print(len(figs), "figures")
    else:
        p.screenshot(path=out, full_page=full)
    for m in msgs:
        print(m)
    b.close()
print("saved", out)
