"""SVG chart and diagram generators for the PM handbook.

Every function returns an HTML <figure> containing an inline SVG that uses CSS
variables (see style.css), so one source renders correctly in light mode, dark
mode and the printed PDF.  All data shown is passed in by the caller; nothing is
fabricated here.
"""
from html import escape
import math

PALETTE = ["var(--c1)", "var(--c2)", "var(--c3)", "var(--c4)", "var(--c5)", "var(--c6)"]


def _e(s):
    return escape(str(s), quote=True)


def wrap(text, width):
    words, lines, cur = str(text).split(), [], ""
    for w in words:
        if len(cur) + len(w) + (1 if cur else 0) <= width:
            cur = (cur + " " + w).strip()
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines or [""]


def _text(x, y, s, cls="", anchor="middle", width=None, lh=14):
    lines = wrap(s, width) if width else [str(s)]
    out = [f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">']
    for i, ln in enumerate(lines):
        out.append(f'<tspan x="{x}" dy="{0 if i == 0 else lh}">{_e(ln)}</tspan>')
    out.append("</text>")
    return "".join(out)


def _fig(svg, title, caption, alt):
    cap = f"<figcaption><strong>{_e(title)}.</strong> {_e(caption)}</figcaption>" if caption else f"<figcaption><strong>{_e(title)}</strong></figcaption>"
    return f'<figure class="viz" role="img" aria-label="{_e(alt or title)}">{svg}{cap}</figure>'


def _fmt(v, fmt):
    if fmt == "pct":
        return f"{v:g}%"
    if fmt == "inr":
        return f"₹{v:,.0f}"
    if fmt == "usd":
        return f"${v:,.0f}"
    if isinstance(v, float) and v != int(v):
        return f"{v:,.2f}".rstrip("0").rstrip(".")
    return f"{v:,.0f}" if isinstance(v, (int, float)) else str(v)


def _nice_max(v):
    if v <= 0:
        return 1
    p = 10 ** math.floor(math.log10(v))
    for m in (1, 2, 2.5, 5, 10):
        if v <= m * p:
            return m * p
    return 10 * p


# ---------------------------------------------------------------- funnel
def funnel(title, stages, caption="", unit="", alt=""):
    W, rowh, gap = 720, 46, 8
    H = len(stages) * (rowh + gap) + 20
    top = stages[0][1]
    parts = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">']
    cx, LABW = 400, 150
    for i, (lab, v) in enumerate(stages):
        w = max(8, 380 * v / top)
        y = 10 + i * (rowh + gap)
        parts.append(_text(LABW + 8, y + rowh / 2 + 5, lab, "b small", "end", width=22, lh=12))
        parts.append(f'<rect x="{cx - w / 2}" y="{y}" width="{w}" height="{rowh}" rx="6" fill="{PALETTE[i % 3]}" opacity="{1 - i * 0.06:.2f}"/>')
        vt = f"{_fmt(v, '')}{unit}"
        if w >= 70:
            parts.append(_text(cx, y + rowh / 2 + 5, vt, "on-fill b"))
        else:
            parts.append(_text(cx + w / 2 + 8, y + rowh / 2 + 5, vt, "b small", "start"))
        if i > 0:
            prev = stages[i - 1][1]
            parts.append(_text(W - 150, y + rowh / 2 - 2, f"{v / prev * 100:.1f}".rstrip("0").rstrip(".") + "% of previous", "mut small", "start"))
            parts.append(_text(W - 150, y + rowh / 2 + 13, f"{100 - v / prev * 100:.1f}".rstrip("0").rstrip(".") + "% drop-off", "warn small", "start"))
    parts.append("</svg>")
    return _fig("".join(parts), title, caption, alt or f"Funnel: " + "; ".join(f"{l} {v}" for l, v in stages))


# ---------------------------------------------------------------- bars
def bar(title, cats, series, caption="", ylabel="", fmt="", alt="", horizontal=False):
    if horizontal:
        return hbar(title, list(zip(cats, series[next(iter(series))])), caption, fmt, alt)
    names = list(series)
    W, H = 720, 330
    L, R, T, B = 64, 20, 20, 60
    mx = _nice_max(max(max(v) for v in series.values()))
    pw, ph = W - L - R, H - T - B
    p = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">']
    for k in range(5):
        v = mx * k / 4
        y = T + ph - ph * k / 4
        p.append(f'<line x1="{L}" y1="{y}" x2="{W - R}" y2="{y}" class="grid"/>')
        p.append(_text(L - 8, y + 4, _fmt(v, fmt), "mut small", "end"))
    gw = pw / len(cats)
    bw = min(46, gw * 0.7 / len(names))
    for i, c in enumerate(cats):
        gx = L + gw * i + gw / 2 - bw * len(names) / 2
        for j, n in enumerate(names):
            v = series[n][i]
            h = ph * v / mx
            x = gx + j * bw
            p.append(f'<rect x="{x:.1f}" y="{T + ph - h:.1f}" width="{bw - 3:.1f}" height="{h:.1f}" rx="3" fill="{PALETTE[j % 6]}"/>')
            p.append(_text(x + (bw - 3) / 2, T + ph - h - 5, _fmt(v, fmt), "small b"))
        p.append(_text(L + gw * i + gw / 2, H - B + 18, c, "small", width=max(8, int(gw / 6.5))))
    p.append(f'<line x1="{L}" y1="{T + ph}" x2="{W - R}" y2="{T + ph}" class="axis"/>')
    if ylabel:
        p.append(f'<text x="14" y="{T + ph / 2}" class="mut small" text-anchor="middle" transform="rotate(-90 14 {T + ph / 2})">{_e(ylabel)}</text>')
    if len(names) > 1:
        lx = L
        for j, n in enumerate(names):
            p.append(f'<rect x="{lx}" y="{H - 14}" width="10" height="10" rx="2" fill="{PALETTE[j % 6]}"/>')
            p.append(_text(lx + 14, H - 5, n, "small", "start"))
            lx += 30 + len(n) * 6.5
    p.append("</svg>")
    return _fig("".join(p), title, caption, alt or f"Bar chart: {title}")


def hbar(title, items, caption="", fmt="", alt="", highlight=None):
    rowh = 34
    W, L, R = 720, 190, 70
    H = rowh * len(items) + 24
    mx = _nice_max(max(v for _, v in items))
    p = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">']
    for i, (lab, v) in enumerate(items):
        y = 10 + i * rowh
        w = (W - L - R) * v / mx
        col = "var(--c3)" if (highlight is not None and i == highlight) else "var(--c1)"
        p.append(_text(L - 10, y + 18, lab, "small", "end", width=30, lh=11))
        p.append(f'<rect x="{L}" y="{y + 4}" width="{w:.1f}" height="{rowh - 12}" rx="4" fill="{col}"/>')
        p.append(_text(L + w + 8, y + 19, _fmt(v, fmt), "small b", "start"))
    p.append("</svg>")
    return _fig("".join(p), title, caption, alt or f"Horizontal bars: {title}")


# ---------------------------------------------------------------- line
def line(title, xs, series, caption="", ylabel="", fmt="", alt="", ymax=None, ymin=0):
    W, H = 720, 330
    L, R, T, B = 64, 24, 20, 62
    names = list(series)
    mx = ymax or _nice_max(max(max(v) for v in series.values()))
    rng = mx - ymin
    pw, ph = W - L - R, H - T - B
    p = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">']
    for k in range(5):
        v = ymin + rng * k / 4
        y = T + ph - ph * k / 4
        p.append(f'<line x1="{L}" y1="{y}" x2="{W - R}" y2="{y}" class="grid"/>')
        p.append(_text(L - 8, y + 4, _fmt(v, fmt), "mut small", "end"))
    n = len(xs)
    step = max(1, math.ceil(n / 12))
    for i, x in enumerate(xs):
        px = L + pw * (i / (n - 1) if n > 1 else 0.5)
        if i % step == 0:
            p.append(_text(px, H - B + 18, x, "small"))
    for j, nm in enumerate(names):
        pts = []
        for i, v in enumerate(series[nm]):
            px = L + pw * (i / (n - 1) if n > 1 else 0.5)
            py = T + ph - ph * (v - ymin) / rng
            pts.append((px, py))
        p.append(f'<polyline points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in pts)}" fill="none" stroke="{PALETTE[j % 6]}" stroke-width="2.5" stroke-linejoin="round"/>')
        for a, b in pts:
            p.append(f'<circle cx="{a:.1f}" cy="{b:.1f}" r="3.5" fill="{PALETTE[j % 6]}"/>')
        if n <= 12:
            off = -9 if j % 2 == 0 else 17
            for (a, b), v in zip(pts, series[nm]):
                p.append(_text(a, b + off, _fmt(v, fmt), "small b"))
    p.append(f'<line x1="{L}" y1="{T + ph}" x2="{W - R}" y2="{T + ph}" class="axis"/>')
    if ylabel:
        p.append(f'<text x="14" y="{T + ph / 2}" class="mut small" text-anchor="middle" transform="rotate(-90 14 {T + ph / 2})">{_e(ylabel)}</text>')
    if len(names) > 1:
        lx = L
        for j, nm in enumerate(names):
            p.append(f'<rect x="{lx}" y="{H - 14}" width="10" height="10" rx="2" fill="{PALETTE[j % 6]}"/>')
            p.append(_text(lx + 14, H - 5, nm, "small", "start"))
            lx += 30 + len(nm) * 6.5
    p.append("</svg>")
    return _fig("".join(p), title, caption, alt or f"Line chart: {title}")


# ---------------------------------------------------------------- heatmap
def heatmap(title, rows, cols, matrix, caption="", fmt="pct", alt="", rowhead="Cohort", vmax=100):
    cw, rh, LW, T = 70, 34, 110, 34
    W = LW + cw * len(cols) + 20
    H = T + rh * len(rows) + 16
    p = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">']
    p.append(_text(LW - 10, T - 12, rowhead, "small b mut", "end"))
    for j, c in enumerate(cols):
        p.append(_text(LW + cw * j + cw / 2, T - 12, c, "small b"))
    for i, r in enumerate(rows):
        p.append(_text(LW - 10, T + rh * i + rh / 2 + 4, r, "small", "end"))
        for j, v in enumerate(matrix[i]):
            x, y = LW + cw * j, T + rh * i
            if v is None:
                p.append(f'<rect x="{x + 2}" y="{y + 2}" width="{cw - 4}" height="{rh - 4}" rx="4" class="empty"/>')
                continue
            a = max(0.08, min(1, v / vmax))
            p.append(f'<rect x="{x + 2}" y="{y + 2}" width="{cw - 4}" height="{rh - 4}" rx="4" fill="var(--c1)" fill-opacity="{a:.2f}"/>')
            label = f"{v:.1f}%" if fmt == "pct" else _fmt(v, fmt)
            p.append(_text(x + cw / 2, y + rh / 2 + 4, label, "small b " + ("on-fill" if a > 0.55 else "")))
    p.append("</svg>")
    return _fig("".join(p), title, caption, alt or f"Heatmap: {title}")


# ---------------------------------------------------------------- bubble / scatter / 2x2
def scatter(title, points, xlabel, ylabel, caption="", alt="", xmax=None, ymax=None, quad=None, xmin=0, ymin=0):
    """points: list of dict(label, x, y, size optional, group optional). quad: 4 corner labels [TL,TR,BL,BR]."""
    W, H = 720, 400
    L, R, T, B = 70, 20, 20, 56
    xm = xmax or _nice_max(max(p["x"] for p in points))
    ym = ymax or _nice_max(max(p["y"] for p in points))
    pw, ph = W - L - R, H - T - B
    s = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">']
    s.append(f'<rect x="{L}" y="{T}" width="{pw}" height="{ph}" class="plot"/>')
    s.append(f'<line x1="{L + pw / 2}" y1="{T}" x2="{L + pw / 2}" y2="{T + ph}" class="grid dash"/>')
    s.append(f'<line x1="{L}" y1="{T + ph / 2}" x2="{L + pw}" y2="{T + ph / 2}" class="grid dash"/>')
    if quad:
        s.append(_text(L + 8, T + 16, quad[0], "quad", "start"))
        s.append(_text(L + pw - 8, T + 16, quad[1], "quad", "end"))
        s.append(_text(L + 8, T + ph - 8, quad[2], "quad", "start"))
        s.append(_text(L + pw - 8, T + ph - 8, quad[3], "quad", "end"))
    groups = {}
    for pt in points:
        g = pt.get("group", "")
        groups.setdefault(g, len(groups))
    for pt in points:
        x = L + pw * (pt["x"] - xmin) / (xm - xmin)
        y = T + ph - ph * (pt["y"] - ymin) / (ym - ymin)
        r = pt.get("size", 9)
        col = PALETTE[groups[pt.get("group", "")] % 6]
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{col}" fill-opacity="0.82" stroke="var(--surface)" stroke-width="1.5"/>')
        if x > L + pw * 0.72:  # keep labels inside the plot near the right edge
            s.append(_text(x - r - 4, y + 4, pt["label"], "small", "end"))
        else:
            s.append(_text(x + r + 4, y + 4, pt["label"], "small", "start"))
    s.append(f'<line x1="{L}" y1="{T + ph}" x2="{L + pw}" y2="{T + ph}" class="axis"/><line x1="{L}" y1="{T}" x2="{L}" y2="{T + ph}" class="axis"/>')
    s.append(_text(L + pw / 2, H - 12, xlabel, "small b mut"))
    s.append(f'<text x="16" y="{T + ph / 2}" class="small b mut" text-anchor="middle" transform="rotate(-90 16 {T + ph / 2})">{_e(ylabel)}</text>')
    if len(groups) > 1 and "" not in groups:
        lx = L
        for g, i in groups.items():
            s.append(f'<circle cx="{lx + 5}" cy="{H - 30}" r="5" fill="{PALETTE[i % 6]}"/>')
            s.append(_text(lx + 14, H - 26, g, "small", "start"))
            lx += 30 + len(g) * 6.5
    s.append("</svg>")
    return _fig("".join(s), title, caption, alt or f"Scatter: {title}")


# ---------------------------------------------------------------- normal curve (hypothesis tests)
def normal_curve(title, caption="", alt="", z_crit=1.96, observed=None, two_sided=True):
    W, H = 720, 300
    L, R, T, B = 40, 30, 30, 52
    pw, ph = W - L - R, H - T - B
    def pdf(z):
        return math.exp(-z * z / 2) / math.sqrt(2 * math.pi)
    def X(z):
        return L + pw * (z + 4.5) / 9
    def Y(d):
        return T + ph - ph * d / 0.42
    s = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">']
    zs = [i / 20 - 4.5 for i in range(181)]
    def area(z0, z1):
        pts = [(X(z), Y(pdf(z))) for z in zs if z0 <= z <= z1]
        if not pts:
            return ""
        d = f"M{pts[0][0]:.1f},{Y(0):.1f} " + " ".join(f"L{a:.1f},{b:.1f}" for a, b in pts) + f" L{pts[-1][0]:.1f},{Y(0):.1f} Z"
        return f'<path d="{d}" class="reject"/>'
    s.append(area(z_crit, 4.5))
    if two_sided:
        s.append(area(-4.5, -z_crit))
    pts = " ".join(f"{X(z):.1f},{Y(pdf(z)):.1f}" for z in zs)
    s.append(f'<polyline points="{pts}" fill="none" stroke="var(--c1)" stroke-width="2.5"/>')
    s.append(f'<line x1="{L}" y1="{Y(0)}" x2="{W - R}" y2="{Y(0)}" class="axis"/>')
    for z in range(-4, 5):
        s.append(_text(X(z), Y(0) + 16, str(z), "small mut"))
    for zc in ([-z_crit, z_crit] if two_sided else [z_crit]):
        s.append(f'<line x1="{X(zc)}" y1="{T}" x2="{X(zc)}" y2="{Y(0)}" class="grid dash"/>')
        s.append(_text(X(zc), T - 6, f"z = {zc:+.2f}", "small b"))
    if observed is not None:
        s.append(f'<line x1="{X(observed)}" y1="{T + 10}" x2="{X(observed)}" y2="{Y(0)}" stroke="var(--c3)" stroke-width="3"/>')
        s.append(_text(X(observed) - 8, T + 24, f"observed z = {observed:.2f}", "small b", "end"))
    s.append(_text(W / 2, H - 8, "Test statistic z when H0 (no real difference) is true. Shaded = rejection region (α).", "small mut"))
    s.append("</svg>")
    return _fig("".join(s), title, caption, alt or f"Normal curve for {title}")


# ---------------------------------------------------------------- flows and layered diagrams
def stepflow(title, steps, caption="", alt="", per_row=None):
    """Horizontal chain of numbered steps. steps: list of str or (head, detail)."""
    n = len(steps)
    per_row = per_row or (n if n <= 5 else math.ceil(n / math.ceil(n / 5)))
    rows = math.ceil(n / per_row)
    W = 720
    bw = (W - 20 - (per_row - 1) * 30) / per_row
    max_detail = max((len(wrap(st[1], max(12, int(bw / 5.6)))) for st in steps if isinstance(st, (list, tuple)) and st[1]), default=0)
    bh = max(92, 56 + 11 * max_detail)
    H = rows * (bh + 34) + 6
    s = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg"><defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" class="arrowhead"/></marker></defs>']
    for i, st in enumerate(steps):
        r, c = divmod(i, per_row)
        x = 10 + c * (bw + 30)
        y = 6 + r * (bh + 34)
        head, detail = (st if isinstance(st, (list, tuple)) else (st, ""))
        s.append(f'<rect x="{x:.1f}" y="{y}" width="{bw:.1f}" height="{bh}" rx="10" class="node"/>')
        s.append(f'<circle cx="{x + 16:.1f}" cy="{y + 16}" r="11" fill="var(--c1)"/>')
        s.append(_text(x + 16, y + 20, i + 1, "on-fill b small"))
        s.append(_text(x + bw / 2 + 8, y + 22, head, "b small", width=max(10, int(bw / 7.2)), lh=13))
        if detail:
            s.append(_text(x + bw / 2, y + 52, detail, "mut tiny", width=max(12, int(bw / 5.6)), lh=11))
        if c < per_row - 1 and i < n - 1:
            s.append(f'<line x1="{x + bw + 3:.1f}" y1="{y + bh / 2}" x2="{x + bw + 27:.1f}" y2="{y + bh / 2}" class="edge" marker-end="url(#ah)"/>')
        if c == per_row - 1 and i < n - 1:
            nx = 10 + bw / 2
            s.append(f'<path d="M{x + bw / 2:.1f},{y + bh + 2} L{x + bw / 2:.1f},{y + bh + 14} L{nx:.1f},{y + bh + 14} L{nx:.1f},{y + bh + 32}" class="edge" fill="none" marker-end="url(#ah)"/>')
    s.append("</svg>")
    return _fig("".join(s), title, caption, alt or f"Process: " + " → ".join(x if isinstance(x, str) else x[0] for x in steps))


def layers(title, rows, edges=None, caption="", alt="", width=720, labels=None):
    """Layered diagram. rows: list of lists of node labels (top→bottom, or a dict {'id':'Label'}).
    edges: list of [from_label, to_label, optional edge label]. labels: optional row captions."""
    nrows = len(rows)
    nodeh = 58
    vgap = 52
    TOP = 20
    H = nrows * nodeh + (nrows - 1) * vgap + 24 + TOP
    pos = {}
    s = [f'<svg viewBox="0 0 {width} {H}" xmlns="http://www.w3.org/2000/svg"><defs><marker id="ah2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" class="arrowhead"/></marker></defs>']
    LABW = 0
    if labels:
        LABW = 92
    for r, row in enumerate(rows):
        n = len(row)
        usable = width - LABW - 76  # 30px gutters each side leave room for routed back-edges
        bw = min(170 if n > 1 else 420, (usable - (n - 1) * 20) / n)
        total = n * bw + (n - 1) * 20
        x0 = LABW + 38 + (usable - total) / 2
        y = 10 + TOP + r * (nodeh + vgap)
        if labels and r < len(labels) and labels[r]:
            s.append(_text(4, y + nodeh / 2 + 4, labels[r], "small b mut", "start", width=12, lh=12))
        for i, lab in enumerate(row):
            x = x0 + i * (bw + 20)
            pos[lab] = (x + bw / 2, y, y + nodeh, bw / 2)
            s.append(f'<rect x="{x:.1f}" y="{y}" width="{bw:.1f}" height="{nodeh}" rx="8" class="node"/>')
            s.append(_text(x + bw / 2, y + nodeh / 2 - (3 if len(wrap(lab, int(bw / 6.6))) > 1 else -4), lab, "small b", width=int(bw / 6.6), lh=12))
    for e in edges or []:
        a, b = e[0], e[1]
        if a not in pos or b not in pos:
            raise KeyError(f"edge refers to unknown node: {a} -> {b}")
        ax, ay0, ay1, ahw = pos[a]
        bx, by0, by1, bhw = pos[b]
        if by0 < ay0:
            # back-edge: route around the outside so it never crosses nodes
            right = ax >= width / 2
            sgn = 1 if right else -1
            sx, sy = ax + sgn * ahw, (ay0 + ay1) / 2
            tx, ty = bx + sgn * bhw, (by0 + by1) / 2
            same_row = [v for v in pos.values() if v[1] == by0]
            outer = max(v[0] + v[3] for v in same_row) if right else min(v[0] - v[3] for v in same_row)
            xo = (max(sx, outer) + 22) if right else (min(sx, outer) - 22)
            if abs(tx - outer) < 1:
                s.append(f'<path d="M{sx:.1f},{sy:.1f} L{xo:.1f},{sy:.1f} L{xo:.1f},{ty:.1f} L{tx + sgn * 3:.1f},{ty:.1f}" class="edge" fill="none" marker-end="url(#ah2)"/>')
            else:  # target is not on the outer edge of its row: go over the top and drop in
                top_y = by0 - 14
                s.append(f'<path d="M{sx:.1f},{sy:.1f} L{xo:.1f},{sy:.1f} L{xo:.1f},{top_y:.1f} L{bx:.1f},{top_y:.1f} L{bx:.1f},{by0 - 3:.1f}" class="edge" fill="none" marker-end="url(#ah2)"/>')
            if len(e) > 2 and e[2]:
                s.append(_text(xo + sgn * 4, (sy + ty) / 2, e[2], "tiny mut edge-label", "start" if right else "end"))
            continue
        if by0 > ay0:
            x1, y1, x2, y2 = ax, ay1, bx, by0 - 3
        else:
            x1, y1, x2, y2 = (ax + (ahw if bx > ax else -ahw)), ay0 + nodeh / 2, (bx + (-bhw - 3 if bx > ax else bhw + 3)), by0 + nodeh / 2
        my = (y1 + y2) / 2
        if by0 == ay0:
            s.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" class="edge" marker-end="url(#ah2)"/>')
        else:
            s.append(f'<path d="M{x1:.1f},{y1:.1f} C{x1:.1f},{my:.1f} {x2:.1f},{my:.1f} {x2:.1f},{y2:.1f}" class="edge" fill="none" marker-end="url(#ah2)"/>')
        if len(e) > 2 and e[2]:
            s.append(_text((x1 + x2) / 2 + 4, my + 3, e[2], "tiny mut edge-label", "start"))
    s.append("</svg>")
    return _fig("".join(s), title, caption, alt or f"Diagram: {title}")


def tree(title, root, caption="", alt=""):
    """Metric/issue tree. root = {'label':..., 'children':[...]} nested up to 3 levels."""
    cols = []
    def collect(n, d):
        while len(cols) <= d:
            cols.append([])
        cols[d].append(n)
        for c in n.get("children", []):
            collect(c, d + 1)
    collect(root, 0)
    W = 720
    colw = W / len(cols)
    bw = colw - 30
    leaves = [n for n in cols[-1]]
    rowh = 64
    # assign y by leaf order recursively
    ys = {}
    counter = [0]
    def place(n):
        ch = n.get("children", [])
        if not ch:
            ys[id(n)] = 10 + counter[0] * rowh + 28
            counter[0] += 1
        else:
            for c in ch:
                place(c)
            ys[id(n)] = (ys[id(ch[0])] + ys[id(ch[-1])]) / 2
    place(root)
    H = counter[0] * rowh + 20
    s = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">']
    def draw(n, d):
        x = d * colw + 8
        y = ys[id(n)]
        for c in n.get("children", []):
            cx = (d + 1) * colw + 8
            cy = ys[id(c)]
            s.append(f'<path d="M{x + bw:.1f},{y:.1f} C{x + bw + 14:.1f},{y:.1f} {cx - 14:.1f},{cy:.1f} {cx:.1f},{cy:.1f}" class="edge" fill="none"/>')
            draw(c, d + 1)
        cls = "node hl" if d == 0 else "node"
        s.append(f'<rect x="{x:.1f}" y="{y - 26:.1f}" width="{bw:.1f}" height="52" rx="8" class="{cls}"/>')
        nl = len(wrap(n["label"], int(bw / 6.2)))
        s.append(_text(x + bw / 2, y + 4 - (nl - 1) * 6, n["label"], "small b" if d == 0 else "small", width=int(bw / 6.2), lh=12))
    draw(root, 0)
    s.append("</svg>")
    return _fig("".join(s), title, caption, alt or f"Tree: {title}")


def compare(title, headers, rows, caption="", alt=""):
    """Compact comparison table rendered as HTML (kept in a figure so it prints as a unit)."""
    th = "".join(f"<th>{_e(h)}</th>" for h in headers)
    body = "".join("<tr>" + "".join(f"<td>{_e(c)}</td>" for c in r) + "</tr>" for r in rows)
    cap = f"<figcaption><strong>{_e(title)}.</strong> {_e(caption)}</figcaption>" if caption else ""
    return f'<figure class="viz table-fig"><div class="tablewrap"><table><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>{cap}</figure>'


def phone(title, screens, caption="", alt=""):
    """Annotated mobile wireframes. screens: list of dict(name, items=[('btn'|'text'|'img'|'input'|'bar'|'row', label)], notes=[...]).
    These are ILLUSTRATIVE wireframes, never real product screenshots."""
    n = len(screens)
    pw, ph = 190, 360
    W = n * (pw + 150) + 10
    W = min(W, 760)
    sc = W / (n * (pw + 150) + 10) if n * (pw + 150) + 10 > 760 else 1
    Wt = n * (pw + 150) + 10
    s = [f'<svg viewBox="0 0 {Wt} {ph + 56}" xmlns="http://www.w3.org/2000/svg">']
    for i, sc_ in enumerate(screens):
        x0 = 10 + i * (pw + 150)
        s.append(f'<rect x="{x0}" y="26" width="{pw}" height="{ph}" rx="22" class="phone"/>')
        s.append(_text(x0 + pw / 2, 16, sc_["name"], "small b"))
        y = 52
        for kind, lab in sc_["items"]:
            if kind == "bar":
                s.append(f'<rect x="{x0 + 12}" y="{y}" width="{pw - 24}" height="26" rx="5" class="wf-bar"/>')
                s.append(_text(x0 + pw / 2, y + 17, lab, "tiny b"))
                y += 34
            elif kind == "text":
                s.append(_text(x0 + 16, y + 12, lab, "tiny", "start", width=32, lh=11))
                y += 14 + 11 * (len(wrap(lab, 32)) - 1) + 8
            elif kind == "img":
                s.append(f'<rect x="{x0 + 12}" y="{y}" width="{pw - 24}" height="64" rx="6" class="wf-img"/>')
                s.append(_text(x0 + pw / 2, y + 36, lab, "tiny mut"))
                y += 72
            elif kind == "input":
                s.append(f'<rect x="{x0 + 12}" y="{y}" width="{pw - 24}" height="28" rx="5" class="wf-input"/>')
                s.append(_text(x0 + 20, y + 18, lab, "tiny mut", "start"))
                y += 36
            elif kind == "row":
                s.append(f'<line x1="{x0 + 12}" y1="{y + 26}" x2="{x0 + pw - 12}" y2="{y + 26}" class="grid"/>')
                a, _, b = lab.partition("|")
                s.append(_text(x0 + 16, y + 17, a, "tiny", "start"))
                s.append(_text(x0 + pw - 16, y + 17, b, "tiny b", "end"))
                y += 30
            elif kind == "btn":
                s.append(f'<rect x="{x0 + 12}" y="{y}" width="{pw - 24}" height="32" rx="8" fill="var(--c1)"/>')
                s.append(_text(x0 + pw / 2, y + 21, lab, "tiny b on-fill"))
                y += 42
            elif kind == "warn":
                s.append(f'<rect x="{x0 + 12}" y="{y}" width="{pw - 24}" height="32" rx="6" class="wf-warn"/>')
                s.append(_text(x0 + pw / 2, y + 20, lab, "tiny b"))
                y += 40
        for k, note in enumerate(sc_.get("notes", [])):
            ny = 60 + k * 62
            s.append(f'<circle cx="{x0 + pw + 14}" cy="{ny}" r="10" fill="var(--c3)"/>')
            s.append(_text(x0 + pw + 14, ny + 4, k + 1, "tiny b on-fill"))
            s.append(_text(x0 + pw + 30, ny + 4, note, "tiny", "start", width=19, lh=11))
    s.append("</svg>")
    return _fig("".join(s), title + " (illustrative wireframe, not a real product screenshot)", caption, alt or title)


# ---------------------------------------------------------------- pareto
def pareto(title, items, caption="", alt="", ylabel="count"):
    """items: [(label, count)] — sorted descending automatically; cumulative % line on right axis."""
    items = sorted(items, key=lambda x: -x[1])
    total = sum(v for _, v in items)
    W, H = 720, 340
    L, R, T, B = 60, 56, 20, 74
    pw, ph = W - L - R, H - T - B
    mx = _nice_max(items[0][1])
    s = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">']
    for k in range(5):
        y = T + ph - ph * k / 4
        s.append(f'<line x1="{L}" y1="{y}" x2="{W - R}" y2="{y}" class="grid"/>')
        s.append(_text(L - 8, y + 4, f"{mx * k / 4:g}", "mut small", "end"))
        s.append(_text(W - R + 8, y + 4, f"{25 * k}%", "mut small", "start"))
    gw = pw / len(items)
    cum, pts = 0, []
    for i, (lab, v) in enumerate(items):
        h = ph * v / mx
        x = L + gw * i + gw * 0.15
        s.append(f'<rect x="{x:.1f}" y="{T + ph - h:.1f}" width="{gw * 0.7:.1f}" height="{h:.1f}" rx="3" fill="var(--c1)"/>')
        s.append(_text(x + gw * 0.35, T + ph - h - 5, v, "small b"))
        s.append(_text(L + gw * i + gw / 2, H - B + 16, lab, "small", width=max(8, int(gw / 6.2))))
        cum += v
        pts.append((L + gw * i + gw / 2, T + ph - ph * cum / total, cum / total))
    s.append(f'<polyline points="{" ".join(f"{a:.1f},{b:.1f}" for a, b, _ in pts)}" fill="none" stroke="var(--c3)" stroke-width="2.5"/>')
    for a, b, c in pts:
        s.append(f'<circle cx="{a:.1f}" cy="{b:.1f}" r="3.5" fill="var(--c3)"/>')
        s.append(_text(a, b - 8, f"{c * 100:.0f}%", "tiny b warn"))
    y80 = T + ph - ph * 0.8
    s.append(f'<line x1="{L}" y1="{y80:.1f}" x2="{W - R}" y2="{y80:.1f}" class="grid dash"/>')
    s.append(f'<line x1="{L}" y1="{T + ph}" x2="{W - R}" y2="{T + ph}" class="axis"/>')
    s.append("</svg>")
    return _fig("".join(s), title, caption, alt or f"Pareto chart: {title}")


# ---------------------------------------------------------------- loop (cycle / feedback loop)
def loop(title, nodes, caption="", alt="", kind="R", center=None):
    """nodes: list of labels around a circle (clockwise from top). kind: 'R' reinforcing, 'B' balancing (centre badge)."""
    n = len(nodes)
    W, H = 720, 380
    cx, cy, rx, ry = W / 2, H / 2, 230, 130
    s = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg"><defs><marker id="ah3" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" class="arrowhead"/></marker></defs>']
    pos = []
    for i, lab in enumerate(nodes):
        ang = -math.pi / 2 + 2 * math.pi * i / n
        pos.append((cx + rx * math.cos(ang), cy + ry * math.sin(ang), ang))
    bw, bh = 150, 46
    for i in range(n):
        x1, y1, a1 = pos[i]
        x2, y2, a2 = pos[(i + 1) % n]
        mx_, my_ = (x1 + x2) / 2, (y1 + y2) / 2
        # pull the control point outward from the centre to curve the arrow
        dx, dy = mx_ - cx, my_ - cy
        d = math.hypot(dx, dy) or 1
        qx, qy = mx_ + dx / d * 28, my_ + dy / d * 28
        # shorten ends so arrows stop at box edges
        def trim(px, py, tx, ty, k):
            vx, vy = tx - px, ty - py
            L_ = math.hypot(vx, vy) or 1
            return px + vx / L_ * k, py + vy / L_ * k
        span = math.hypot(x2 - x1, y2 - y1)
        sx, sy = trim(x1, y1, qx, qy, min(62, span * 0.3))
        ex, ey = trim(x2, y2, qx, qy, min(66, span * 0.32))
        s.append(f'<path d="M{sx:.1f},{sy:.1f} Q{qx:.1f},{qy:.1f} {ex:.1f},{ey:.1f}" class="edge" fill="none" marker-end="url(#ah3)"/>')
    for (x, y, _), lab in zip(pos, nodes):
        s.append(f'<rect x="{x - bw / 2:.1f}" y="{y - bh / 2:.1f}" width="{bw}" height="{bh}" rx="10" class="node"/>')
        nl = len(wrap(lab, 22))
        s.append(_text(x, y + 4 - (nl - 1) * 6, lab, "small b", width=22, lh=12))
    badge = center or ("Reinforcing loop" if kind == "R" else "Balancing loop")
    s.append(f'<circle cx="{cx}" cy="{cy}" r="46" fill="var(--c2)" fill-opacity=".15" stroke="var(--c2)" stroke-width="2"/>')
    nb = len(wrap(badge, 11))
    s.append(_text(cx, cy + 4 - (nb - 1) * 6, badge, "small b", width=11, lh=12))
    s.append("</svg>")
    return _fig("".join(s), title, caption, alt or f"Loop diagram: {title}")


# ---------------------------------------------------------------- canvas grid (BMC, SWOT, PESTLE...)
def canvas(title, cols, cells, caption="", alt=""):
    """HTML grid. cols = number of columns. cells = list of dict(title, text (str or list), span=1, rows=1, tone=optional)."""
    out = []
    for c in cells:
        txt = c.get("text", "")
        body = "<ul>" + "".join(f"<li>{_e(t)}</li>" for t in txt) + "</ul>" if isinstance(txt, list) else f"<p>{_e(txt)}</p>"
        style = f'grid-column:span {c.get("span", 1)};grid-row:span {c.get("rows", 1)}'
        out.append(f'<div class="cv tone-{c.get("tone", "n")}" style="{style}"><h5>{_e(c["title"])}</h5>{body}</div>')
    cap = f"<figcaption><strong>{_e(title)}.</strong> {_e(caption)}</figcaption>" if caption else f"<figcaption><strong>{_e(title)}</strong></figcaption>"
    return f'<figure class="viz canvas-fig" role="group" aria-label="{_e(alt or title)}"><div class="canvas" style="grid-template-columns:repeat({int(cols)},minmax(0,1fr))">{"".join(out)}</div>{cap}</figure>'


def concentric(title, rings, caption="", alt=""):
    """Nested circles for TAM/SAM/SOM. rings: outer->inner list of (label, value_text, detail)."""
    n = len(rings)
    W, H = 720, 360
    cx, base_r = 190, 165
    cy = H - 15
    s = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">']
    radii = [base_r * (1 - 0.3 * i) if i else base_r for i in range(n)]
    radii = [base_r * (0.62 ** i) for i in range(n)]
    for i, (lab, val, det) in enumerate(rings):
        r = radii[i]
        s.append(f'<circle cx="{cx}" cy="{cy - r}" r="{r:.1f}" fill="{PALETTE[i % 3]}" fill-opacity="{0.16 + 0.14 * i:.2f}" stroke="{PALETTE[i % 3]}" stroke-width="2"/>')
        s.append(_text(cx, cy - 2 * r + 24 + 0, lab, "b small"))
        ly = 60 + i * 96
        s.append(f'<line x1="{cx + r * 0.7:.1f}" y1="{cy - 2 * r + 24:.1f}" x2="400" y2="{ly - 4}" class="grid dash"/>')
        s.append(f'<text x="410" y="{ly}" class="b" text-anchor="start" style="font-size:17px">{_e(val)}</text>')
        s.append(_text(410, ly + 18, det, "small mut", "start", width=54, lh=13))
    s.append("</svg>")
    return _fig("".join(s), title, caption, alt or f"Concentric market circles: {title}")



# ---------------------------------------------------------------- desktop app wireframe (illustrative)
def _wf_items(s, items, x0, y, w, notes_pos):
    """Draw stacked wireframe items inside a column; returns the new y. A label starting with
    '[n] ' gets a numbered marker that links to note n under the figure."""
    for kind, lab in items:
        lab = str(lab)
        mark = None
        if lab.startswith("[") and "]" in lab[:4]:
            mark, lab = lab[1:lab.index("]")], lab[lab.index("]") + 1:].strip()
        y0 = y
        if kind == "bar":
            s.append(f'<rect x="{x0}" y="{y}" width="{w}" height="26" rx="5" class="wf-bar"/>')
            s.append(_text(x0 + 10, y + 17, lab, "tiny b", "start"))
            y += 34
        elif kind == "tabs":
            parts = lab.split("|")
            tw = w / max(1, len(parts))
            for i, t in enumerate(parts):
                on = t.startswith("*")
                t = t.lstrip("*")
                s.append(f'<rect x="{x0 + i * tw:.1f}" y="{y}" width="{tw - 4:.1f}" height="22" rx="5" ' + ('fill="var(--c1)"' if on else 'class="wf-bar"') + '/>')
                s.append(_text(x0 + i * tw + tw / 2 - 2, y + 15, t, "tiny b on-fill" if on else "tiny"))
            y += 30
        elif kind == "text":
            n = len(wrap(lab, int(w / 5.4)))
            s.append(_text(x0 + 4, y + 11, lab, "tiny", "start", width=int(w / 5.4), lh=11))
            y += 8 + 11 * n + 4
        elif kind == "img":
            s.append(f'<rect x="{x0}" y="{y}" width="{w}" height="56" rx="6" class="wf-img"/>')
            s.append(_text(x0 + w / 2, y + 32, lab, "tiny mut"))
            y += 64
        elif kind == "input":
            s.append(f'<rect x="{x0}" y="{y}" width="{w}" height="28" rx="6" class="wf-input"/>')
            s.append(_text(x0 + 10, y + 18, lab, "tiny mut", "start"))
            y += 36
        elif kind == "btn":
            bw = min(w, max(90, 7 * len(lab) + 24))
            s.append(f'<rect x="{x0}" y="{y}" width="{bw}" height="28" rx="7" fill="var(--c1)"/>')
            s.append(_text(x0 + bw / 2, y + 18, lab, "tiny b on-fill"))
            y += 36
        elif kind == "row":
            a, _, b = lab.partition("|")
            s.append(f'<line x1="{x0}" y1="{y + 24}" x2="{x0 + w}" y2="{y + 24}" class="grid"/>')
            s.append(_text(x0 + 4, y + 16, a, "tiny", "start"))
            s.append(_text(x0 + w - 4, y + 16, b, "tiny b", "end"))
            y += 28
        elif kind in ("user", "ai"):
            n = len(wrap(lab, int(w * 0.78 / 5.4)))
            bh = 12 + 11 * n
            bw = w * 0.82
            bx = x0 + w - bw if kind == "user" else x0
            fill = 'fill="var(--c1)" fill-opacity=".14" stroke="var(--c1)"' if kind == "user" else 'class="wf-bar"'
            s.append(f'<rect x="{bx:.1f}" y="{y}" width="{bw:.1f}" height="{bh}" rx="9" {fill}/>')
            s.append(_text(bx + 8, y + 15, lab, "tiny", "start", width=int(w * 0.78 / 5.4), lh=11))
            y += bh + 8
        elif kind == "code":
            lines = lab.split("\\n") if "\\n" in lab else lab.split(" ;; ")
            bh = 12 + 12 * len(lines)
            s.append(f'<rect x="{x0}" y="{y}" width="{w}" height="{bh}" rx="6" fill="var(--ink)" fill-opacity=".9"/>')
            for i, ln in enumerate(lines):
                s.append(f'<text x="{x0 + 8}" y="{y + 16 + 12 * i}" class="tiny on-fill" text-anchor="start" style="font-family:ui-monospace,Consolas,monospace">{_e(ln)}</text>')
            y += bh + 8
        elif kind == "warn":
            s.append(f'<rect x="{x0}" y="{y}" width="{w}" height="28" rx="6" class="wf-warn"/>')
            s.append(_text(x0 + 10, y + 18, lab, "tiny b", "start"))
            y += 36
        elif kind == "ok":
            s.append(f'<rect x="{x0}" y="{y}" width="{w}" height="28" rx="6" fill="var(--c4)" fill-opacity=".14" stroke="var(--c4)"/>')
            s.append(_text(x0 + 10, y + 18, lab, "tiny b", "start"))
            y += 36
        elif kind == "toggle":
            a, _, b = lab.partition("|")
            on = b.strip().lower() in ("on", "yes", "true")
            s.append(_text(x0 + 4, y + 16, a, "tiny", "start"))
            s.append(f'<rect x="{x0 + w - 34}" y="{y + 5}" width="30" height="16" rx="8" ' + ('fill="var(--c4)"' if on else 'class="wf-bar"') + '/>')
            s.append(f'<circle cx="{x0 + w - (12 if on else 26)}" cy="{y + 13}" r="6" fill="#fff" stroke="var(--line)"/>')
            y += 28
        if mark:
            s.append(f'<circle cx="{x0 + w + 2}" cy="{y0 + 10}" r="9" fill="var(--c3)"/>')
            s.append(_text(x0 + w + 2, y0 + 14, mark, "tiny b on-fill"))
    return y


def window(title, app, main, sidebar=None, panel=None, notes=None, url="", caption="", alt=""):
    """Annotated desktop-app wireframe. Always labelled illustrative: it shows the layout and the
    clicks in order, not a real screenshot of the product."""
    W = 720
    s = []
    side_w = 150 if sidebar else 0
    pan_w = 190 if panel else 0
    top = 34
    mx = 12 + side_w + 14
    mw = W - mx - 14 - pan_w - (12 if panel else 0) - 14
    body = []
    yb = top + 14
    if sidebar:
        y = yb
        for it in sidebar:
            on = str(it).startswith("*")
            t = str(it).lstrip("*")
            mark = None
            if t.startswith("[") and "]" in t[:4]:
                mark, t = t[1:t.index("]")], t[t.index("]") + 1:].strip()
            if on:
                body.append(f'<rect x="20" y="{y - 13}" width="{side_w - 12}" height="20" rx="5" fill="var(--c1)" fill-opacity=".16"/>')
            body.append(_text(28, y + 1, t, "tiny b" if on else "tiny", "start"))
            if mark:
                body.append(f'<circle cx="{side_w - 4}" cy="{y - 3}" r="9" fill="var(--c3)"/>')
                body.append(_text(side_w - 4, y + 1, mark, "tiny b on-fill"))
            y += 24
        side_end = y
    else:
        side_end = yb
    main_end = _wf_items(body, main, mx, yb, mw, None)
    pan_end = yb
    if panel:
        px = W - 14 - pan_w
        pan_end = _wf_items(body, panel, px + 8, yb, pan_w - 16, None)
    H_frame = max(side_end, main_end, pan_end) + 10
    notes = notes or []
    note_h = 0
    note_svg = []
    if notes:
        y = H_frame + 22
        for k, nt in enumerate(notes):
            lines = wrap(nt, 104)
            note_svg.append(f'<circle cx="24" cy="{y - 4}" r="9" fill="var(--c3)"/>')
            note_svg.append(_text(24, y, k + 1, "tiny b on-fill"))
            note_svg.append(_text(40, y, nt, "small", "start", width=104, lh=14))
            y += 14 * len(lines) + 8
        note_h = y - H_frame
    H = H_frame + note_h + 6
    s.append(f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">')
    s.append(f'<rect x="6" y="6" width="{W - 12}" height="{H_frame - 6}" rx="12" class="phone"/>')
    s.append(f'<line x1="6" y1="{top}" x2="{W - 6}" y2="{top}" class="grid"/>')
    for i, c in enumerate(("var(--c5)", "var(--c3)", "var(--c4)")):
        s.append(f'<circle cx="{22 + i * 14}" cy="20" r="4.5" fill="{c}"/>')
    s.append(_text(76, 24, app, "small b", "start"))
    if url:
        s.append(f'<rect x="{W / 2 - 150}" y="11" width="300" height="17" rx="8" class="wf-bar"/>')
        s.append(_text(W / 2, 23, url, "tiny mut"))
    if sidebar:
        s.append(f'<rect x="12" y="{top + 4}" width="{side_w}" height="{H_frame - top - 10}" rx="8" class="wf-bar" fill-opacity=".6"/>')
    if panel:
        px = W - 14 - pan_w
        s.append(f'<rect x="{px}" y="{top + 4}" width="{pan_w}" height="{H_frame - top - 10}" rx="8" class="wf-bar" fill-opacity=".45"/>')
    s += body + note_svg
    s.append("</svg>")
    return _fig("".join(s), title + " (illustrative wireframe, not a real product screenshot)", caption, alt or title)


# ---------------------------------------------------------------- automation workflow canvas
_KIND = {"trigger": ("var(--c4)", "TRIGGER"), "action": ("var(--c1)", "ACTION"), "ai": ("var(--c2)", "AI STEP"),
         "logic": ("var(--c3)", "LOGIC"), "output": ("var(--c5)", "OUTPUT"), "human": ("var(--c6)", "HUMAN"),
         "data": ("var(--c6)", "DATA")}


def workflow(title, nodes, branch=None, caption="", alt="", per_row=4):
    """Automation canvas in the style of n8n / Make / Zapier. nodes: list of [kind, label, detail].
    branch: optional {"paths": [[edge_label, [[kind,label,detail], ...]], [edge_label, [...]]]} drawn after the last node."""
    W = 720
    n = len(nodes)
    per_row = min(per_row, max(1, n))
    gap = 34
    bw = (W - 20 - (per_row - 1) * gap) / per_row
    allnodes = list(nodes) + [nd for _, ch in (branch or {}).get("paths", []) for nd in ch]
    def need(nd, w):
        ll = len(wrap(nd[1], max(10, int((w - 22) / 6.6))))
        dl = len(wrap(nd[2], max(12, int((w - 22) / 5.3)))) if len(nd) > 2 and nd[2] else 0
        return 33 + 13 * ll + (4 + 11 * dl if dl else 0) + 8
    bh = max(84, max(need(nd, bw) for nd in allnodes))
    rows = math.ceil(n / per_row)
    pos = []
    for i in range(n):
        r, c = divmod(i, per_row)
        if r % 2 == 1:
            c = per_row - 1 - c  # snake so arrows stay short
        pos.append((10 + c * (bw + gap), 8 + r * (bh + 40)))
    H = 8 + rows * (bh + 40)
    bpaths = (branch or {}).get("paths", [])
    if bpaths:
        H += len(bpaths) * (bh + 26) + 10
    s = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg"><defs><marker id="ahw" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" class="arrowhead"/></marker></defs>']

    def node(x, y, w, k, label, detail):
        col, tag = _KIND.get(k, _KIND["action"])
        s.append(f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="{bh}" rx="10" class="node"/>')
        s.append(f'<rect x="{x:.1f}" y="{y}" width="7" height="{bh}" rx="3" fill="{col}"/>')
        s.append(f'<text x="{x + 16:.1f}" y="{y + 16}" class="tiny b" text-anchor="start" fill="{col}" style="fill:{col}">{tag}</text>')
        s.append(_text(x + 16, y + 33, label, "small b", "start", width=max(10, int((w - 22) / 6.6)), lh=13))
        if detail:
            nl = len(wrap(label, max(10, int((w - 22) / 6.6))))
            s.append(_text(x + 16, y + 33 + 13 * nl + 4, detail, "tiny mut", "start", width=max(12, int((w - 22) / 5.3)), lh=11))

    for i, (nd, (x, y)) in enumerate(zip(nodes, pos)):
        k, label = nd[0], nd[1]
        node(x, y, bw, k, label, nd[2] if len(nd) > 2 else "")
        if i < n - 1:
            x2, y2 = pos[i + 1]
            if y2 == y:
                if x2 > x:
                    s.append(f'<line x1="{x + bw + 2:.1f}" y1="{y + bh / 2}" x2="{x2 - 3:.1f}" y2="{y + bh / 2}" class="edge" marker-end="url(#ahw)"/>')
                else:
                    s.append(f'<line x1="{x - 2:.1f}" y1="{y + bh / 2}" x2="{x2 + bw + 3:.1f}" y2="{y + bh / 2}" class="edge" marker-end="url(#ahw)"/>')
            else:
                s.append(f'<line x1="{x + bw / 2:.1f}" y1="{y + bh + 2}" x2="{x2 + bw / 2:.1f}" y2="{y2 - 3}" class="edge" marker-end="url(#ahw)"/>')
    if bpaths:
        lx, ly = pos[-1]
        sx, sy = lx + bw / 2, ly + bh
        y = 8 + rows * (bh + 40)
        for label, chain in bpaths:
            m = len(chain)
            cw = (W - 20 - 110 - (m - 1) * gap) / max(1, m)
            cw = min(cw, bw)
            x = 120
            s.append(f'<path d="M{sx:.1f},{sy + 2} L{sx:.1f},{y - 12} L60,{y - 12} L60,{y + bh / 2} L{x - 3},{y + bh / 2}" class="edge" fill="none" marker-end="url(#ahw)"/>')
            s.append(f'<rect x="14" y="{y + bh / 2 - 22}" width="92" height="18" rx="9" fill="var(--c3)" fill-opacity=".18" stroke="var(--c3)"/>')
            s.append(_text(60, y + bh / 2 - 9, label, "tiny b"))
            for j, nd in enumerate(chain):
                node(x, y, cw, nd[0], nd[1], nd[2] if len(nd) > 2 else "")
                if j < m - 1:
                    s.append(f'<line x1="{x + cw + 2:.1f}" y1="{y + bh / 2}" x2="{x + cw + gap - 3:.1f}" y2="{y + bh / 2}" class="edge" marker-end="url(#ahw)"/>')
                x += cw + gap
            y += bh + 26
    s.append("</svg>")
    names = {"trigger": "Trigger (starts the flow)", "action": "Action", "ai": "AI step", "logic": "Logic (filter, IF, router)",
             "output": "Output", "human": "Human step", "data": "Data"}
    legend = " · ".join(names[k] for k in sorted({nd[0] for nd in nodes} | {nd[0] for _, ch in bpaths for nd in ch}) if k in names)
    cap = (caption + " " if caption else "") + f"Node types shown: {legend}."
    return _fig("".join(s), title, cap, alt or "Workflow: " + " → ".join(nd[1] for nd in nodes))


# ---------------------------------------------------------------- dispatcher
def render(spec):
    t = spec.pop("type")
    fn = {
        "funnel": lambda d: funnel(d["title"], d["stages"], d.get("caption", ""), d.get("unit", ""), d.get("alt", "")),
        "bar": lambda d: bar(d["title"], d["cats"], d["series"], d.get("caption", ""), d.get("ylabel", ""), d.get("fmt", ""), d.get("alt", "")),
        "hbar": lambda d: hbar(d["title"], d["items"], d.get("caption", ""), d.get("fmt", ""), d.get("alt", ""), d.get("highlight")),
        "line": lambda d: line(d["title"], d["xs"], d["series"], d.get("caption", ""), d.get("ylabel", ""), d.get("fmt", ""), d.get("alt", ""), d.get("ymax"), d.get("ymin", 0)),
        "heatmap": lambda d: heatmap(d["title"], d["rows"], d["cols"], d["matrix"], d.get("caption", ""), d.get("fmt", "pct"), d.get("alt", ""), d.get("rowhead", "Cohort"), d.get("vmax", 100)),
        "scatter": lambda d: scatter(d["title"], d["points"], d["xlabel"], d["ylabel"], d.get("caption", ""), d.get("alt", ""), d.get("xmax"), d.get("ymax"), d.get("quad"), d.get("xmin", 0), d.get("ymin", 0)),
        "normal": lambda d: normal_curve(d["title"], d.get("caption", ""), d.get("alt", ""), d.get("z_crit", 1.96), d.get("observed"), d.get("two_sided", True)),
        "steps": lambda d: stepflow(d["title"], d["steps"], d.get("caption", ""), d.get("alt", ""), d.get("per_row")),
        "layers": lambda d: layers(d["title"], d["rows"], d.get("edges"), d.get("caption", ""), d.get("alt", ""), d.get("width", 720), d.get("labels")),
        "tree": lambda d: tree(d["title"], d["root"], d.get("caption", ""), d.get("alt", "")),
        "compare": lambda d: compare(d["title"], d["headers"], d["rows"], d.get("caption", ""), d.get("alt", "")),
        "phone": lambda d: phone(d["title"], d["screens"], d.get("caption", ""), d.get("alt", "")),
        "pareto": lambda d: pareto(d["title"], d["items"], d.get("caption", ""), d.get("alt", ""), d.get("ylabel", "count")),
        "loop": lambda d: loop(d["title"], d["nodes"], d.get("caption", ""), d.get("alt", ""), d.get("kind", "R"), d.get("center")),
        "canvas": lambda d: canvas(d["title"], d.get("cols", 3), d["cells"], d.get("caption", ""), d.get("alt", "")),
        "concentric": lambda d: concentric(d["title"], d["rings"], d.get("caption", ""), d.get("alt", "")),
        "window": lambda d: window(d["title"], d.get("app", ""), d.get("main", []), d.get("sidebar"), d.get("panel"), d.get("notes"), d.get("url", ""), d.get("caption", ""), d.get("alt", "")),
        "workflow": lambda d: workflow(d["title"], d["nodes"], d.get("branch"), d.get("caption", ""), d.get("alt", ""), d.get("per_row", 4)),
    }[t]
    return fn(spec)
