"""Series ⑥「侵入式 BCI 要不要放得准」上篇 — self-made SVG schematics.
Rendered to PNG via playwright chromium (series track convention).
"""
import os, math, subprocess, tempfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))      # .claude/skills/dailybci
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "series-invasive-bci-precision", "figs")
os.makedirs(OUT, exist_ok=True)

ACC = "#2F6DB5"; ACCD = "#1E4E86"; TINT = "#E9F0F8"
INK = "#1A1A1A"; BODY = "#4A4A4A"; GRAY = "#8A8A8A"; LINE = "#D6DBE2"
WARN = "#C2544D"; WARNT = "#F7ECEB"
CHIPF = "#F2F3F1"; CHIPL = "#DBDCD8"

DEFS = (
    '<defs>'
    '<marker id="ah" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" '
    'markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="%s"/></marker>'
    '<marker id="ahw" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" '
    'markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="%s"/></marker>'
    '<marker id="ahg" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" '
    'markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="%s"/></marker>'
    '</defs>' % (ACC, WARN, GRAY)
)


def T(x, y, s, size=25, fill=INK, anchor="middle", weight="400"):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" font-weight="{weight}">{s}</text>')


def box(x, y, w, h, fill, stroke, rx=12, sw=1.5):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')


def line(x1, y1, x2, y2, stroke=LINE, sw=1.5, dash=None, marker=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    m = f' marker-end="url(#{marker})"' if marker else ""
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" '
            f'stroke-width="{sw}"{d}{m}/>')


def circ(cx, cy, r, fill="none", stroke=ACC, sw=2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" '
            f'stroke-width="{sw}"{d}/>')


# ---------- Fig 1 (卡6): 够准 = 实际偏了多少 < 最多能偏多少 ----------
def fig_inequality():
    s = []
    s.append(T(480, 44, "够准，就是这两段在比大小", 30, INK, weight="700"))

    CY = 244
    ROW_TOL, ROW_VERDICT = 402, 434
    panels = [
        dict(cx=250, title="浅、大、旁边安全", tol=112, miss=58, ang=-40,
             ok=True, note="落点在圈内 → 够准", mark="✓"),
        dict(cx=700, title="深、小、紧挨要害", tol=54, miss=104, ang=-32,
             ok=False, note="落点在圈外 → 不够准", mark="✗"),
    ]
    for p_ in panels:
        cx = p_["cx"]; col = ACC if p_["ok"] else WARN
        s.append(T(cx, 96, p_["title"], 26, ACCD if p_["ok"] else WARN, weight="700"))
        s.append(circ(cx, CY, p_["tol"], TINT if p_["ok"] else WARNT, col, 2, "7 6"))
        s.append(circ(cx, CY, 5, col, col, 1))
        s.append(T(cx - 12, CY + 26, "靶点", 21, BODY, anchor="end"))
        a = math.radians(p_["ang"])
        ex = cx + p_["miss"] * math.cos(a); ey = CY + p_["miss"] * math.sin(a)
        s.append(line(cx, CY, ex, ey, col, 3, marker="ah" if p_["ok"] else "ahw"))
        s.append(circ(ex, ey, 8, "#FFFFFF", col, 2.5))
        s.append(T(ex + 16, ey - 16, "实际偏了多少", 21, INK, anchor="start"))
        s.append(T(ex + 16, ey + 8, p_["mark"], 26, col, anchor="start", weight="700"))
        s.append(T(cx, ROW_TOL, "最多能偏多少", 22, col, weight="700"))
        s.append(T(cx, ROW_VERDICT, p_["note"], 22, BODY))

    s.append(f'<path d="M918,132 C890,196 904,268 884,336" stroke="{WARN}" '
             f'stroke-width="9" fill="none" opacity="0.5" stroke-linecap="round"/>')
    s.append(T(884, 108, "旁边是血管 /", 20, WARN))
    s.append(T(884, 132, "别的功能核团", 20, WARN))

    s.append(box(150, 470, 660, 62, TINT, ACC, 14, 1.5))
    s.append(T(480, 509, "实际偏了多少  <  最多能偏多少   →   够准", 27, ACCD, weight="700"))
    return 960, 556, "".join(s)


# ---------- Fig 2 (卡8): 三区标尺 + 衰减撞噪声地板 ----------
def fig_three_zones():
    s = []
    s.append(T(480, 42, "听力半径 = 衰减曲线撞上噪声地板", 30, INK, weight="700"))

    X0, X1 = 120, 872
    Y0, Y1 = 306, 92
    UM = lambda u: X0 + (X1 - X0) * u / 200.0
    UV = lambda v: Y0 - (Y0 - Y1) * v / 120.0

    s.append(line(X0, Y0, X1, Y0, GRAY, 2))
    s.append(line(X0, Y0, X0, Y1 - 6, GRAY, 2))
    s.append(T(X0 - 16, Y1 - 12, "动作电位幅度 (µV)", 21, BODY, anchor="start"))
    for v in (0, 60, 120):
        s.append(T(X0 - 12, UV(v) + 7, str(v), 19, GRAY, anchor="end"))
        if v:
            s.append(line(X0 - 6, UV(v), X0, UV(v), GRAY, 1.5))

    pts = [f"{UM(i):.1f},{UV(113.2 * math.exp(-i / 69.3)):.1f}" for i in range(0, 201, 2)]
    s.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{ACC}" stroke-width="3.5"/>')

    s.append(line(X0, UV(15), X1, UV(15), WARN, 2.5, "8 6"))
    s.append(T(X1 - 6, UV(15) - 14, "噪声地板", 22, WARN, anchor="end", weight="700"))
    s.append(line(UM(140), UV(15), UM(140), Y0, GRAY, 1.6, "4 5"))
    s.append(circ(UM(140), UV(15), 7, "#FFFFFF", WARN, 2.5))

    BY, BH = 332, 40
    zones = [(0, 50, "单单元区", "分得清是哪个神经元", ACC, TINT),
             (50, 140, "多单元区", "听得到，分不清是谁", "#7FA6D0", "#F1F5FA"),
             (140, 200, "噪声区", "只剩背景噪声", GRAY, CHIPF)]
    for a, b, nm, sub, col, fill in zones:
        s.append(f'<rect x="{UM(a):.1f}" y="{BY}" width="{UM(b) - UM(a):.1f}" height="{BH}" '
                 f'fill="{fill}" stroke="{col}" stroke-width="1.5"/>')
        s.append(T((UM(a) + UM(b)) / 2, BY + 27, nm, 23, col, weight="700"))
        s.append(T((UM(a) + UM(b)) / 2, BY + BH + 26, sub, 20, BODY))
    for u in (0, 50, 140, 200):
        s.append(T(UM(u), Y0 + 21, "200+" if u == 200 else str(u), 19, GRAY))
    s.append(T(480, BY + BH + 90, "距电极的距离 (µm)", 21, BODY))

    CY = 526
    s.append(T(480, CY, "换个频段听，尺度整个变一档", 25, ACCD, weight="700"))
    rows = [("动作电位", "几十 – 140 µm", 100, ACC),
            ("LFP · 神经元各干各的", "250 – 500 µm", 260, "#7FA6D0"),
            ("LFP · 神经元同步活动", "可达毫米级", 520, GRAY)]
    for i, (nm, val, w, col) in enumerate(rows):
        y = CY + 30 + i * 46
        s.append(T(300, y + 22, nm, 21, BODY, anchor="end"))
        s.append(f'<rect x="316" y="{y + 6}" width="{w}" height="22" rx="6" '
                 f'fill="{col}" opacity="0.65"/>')
        s.append(T(316 + w + 14, y + 24, val, 20, ACCD if col != GRAY else BODY, anchor="start"))
    return 960, 720, "".join(s)


# ---------- Fig 3 (卡11): 涂层解耦 ----------
def fig_decoupling():
    s = []
    s.append(T(480, 40, "两个『面积』，管两件不同的事", 30, INK, weight="700"))

    FOOT = 250                       # identical geometric footprint
    for k, (cx, titl, sub, col, coated) in enumerate([
            (250, "裸金属", "表面平滑", GRAY, False),
            (700, "镀涂层", "分形粗糙", ACC, True)]):
        x0 = cx - FOOT / 2
        s.append(T(cx, 96, titl, 27, col if coated else BODY, weight="700"))
        s.append(T(cx, 124, sub, 21, BODY))
        # contact body
        s.append(f'<rect x="{x0}" y="176" width="{FOOT}" height="72" rx="4" '
                 f'fill="{TINT if coated else CHIPF}" stroke="{col}" stroke-width="2.5"/>')
        # surface texture
        if coated:
            d = [f"M{x0},176"]
            step = FOOT / 25.0
            for i in range(25):
                xa = x0 + i * step
                d.append(f"L{xa + step * 0.25:.1f},158 L{xa + step * 0.5:.1f},176 "
                         f"L{xa + step * 0.75:.1f},162 L{xa + step:.1f},176")
            s.append(f'<path d="{" ".join(d)}" fill="none" stroke="{ACC}" stroke-width="2.2"/>')
        else:
            s.append(line(x0, 176, x0 + FOOT, 176, BODY, 3))
        # effective-area readout
        s.append(T(cx, 292, "有效表面积" + ("  大几十–上百倍" if coated else "  小"), 22,
                   ACCD if coated else BODY, weight="700"))
        s.append(T(cx, 322, ("阻抗低 → 噪声地板低" if coated else "阻抗高 → 噪声地板高"),
                   22, ACCD if coated else WARN))
        # footprint bracket
        s.append(line(x0, 356, x0 + FOOT, 356, INK, 2))
        s.append(line(x0, 348, x0, 364, INK, 2))
        s.append(line(x0 + FOOT, 348, x0 + FOOT, 364, INK, 2))
        s.append(T(cx, 388, "几何足印", 22, INK, weight="700"))

    s.append(line(376, 212, 572, 212, GRAY, 2, "6 6", marker="ahg"))
    s.append(T(474, 200, "足印不变", 21, GRAY))

    s.append(box(120, 414, 720, 62, TINT, ACC, 14, 1.5))
    s.append(T(480, 442, "足印决定『范围与分辨』 · 有效表面积决定『阻抗与噪声』", 25, ACCD, weight="700"))
    s.append(T(480, 468, "涂层只涨后者、不涨前者 → 低噪声与高分辨兼得", 23, ACC))
    return 960, 500, "".join(s)


# ---------- Fig 4 (卡13): 电流-距离 r² ----------
def fig_current_distance():
    s = []
    s.append(T(480, 42, "刺激的范围：阈值随距离平方增长", 30, INK, weight="700"))

    X0, X1 = 120, 600
    Y0, Y1 = 386, 118
    RMAX, IMAX = 150.0, 25.0
    UM = lambda r: X0 + (X1 - X0) * r / RMAX
    UA = lambda i: Y0 - (Y0 - Y1) * i / IMAX
    K = 10.0 / (85.0 ** 2)

    s.append(line(X0, Y0, X1 + 18, Y0, GRAY, 2, marker="ahg"))
    s.append(line(X0, Y0, X0, Y1 - 12, GRAY, 2, marker="ahg"))
    s.append(T(X0 - 12, Y1 - 24, "阈值电流 (µA)", 21, BODY, anchor="start"))
    s.append(T((X0 + X1) / 2, Y0 + 48, "神经元距电极的距离 (µm)", 21, BODY))
    for r in (0, 50, 85, 150):
        s.append(T(UM(r), Y0 + 22, str(r), 19, GRAY))
    for i in (10, 20):
        s.append(T(X0 - 12, UA(i) + 7, str(i), 19, GRAY, anchor="end"))

    pts = [f"{UM(r):.1f},{UA(K * r * r):.1f}" for r in range(0, 135, 2)]
    s.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{ACC}" stroke-width="3.5"/>')
    s.append(T(X0 + 18, Y1 + 6, "I = I₀ + k·r²", 23, ACCD, anchor="start", weight="700"))

    s.append(line(X0, UA(10), UM(85), UA(10), WARN, 2, "7 6"))
    s.append(line(UM(85), UA(10), UM(85), Y0, WARN, 2, "7 6"))
    s.append(circ(UM(85), UA(10), 7, "#FFFFFF", WARN, 2.5))
    s.append(T(UM(85) - 14, UA(10) - 16, "10 µA → 约 85 µm", 22, WARN,
               anchor="end", weight="700"))

    SX, SY = 776, 250
    s.append(T(776, 128, "电流越大，激活范围越大", 24, ACCD, weight="700"))
    s.append(f'<circle cx="{SX}" cy="{SY}" r="88" fill="{ACC}" opacity="0.14"/>')
    s.append(circ(SX, SY, 88, "none", ACC, 2, "6 5"))
    s.append(f'<circle cx="{SX}" cy="{SY}" r="52" fill="{ACC}" opacity="0.34"/>')
    s.append(circ(SX, SY, 52, "none", ACCD, 2))
    s.append(circ(SX, SY, 5, INK, INK, 1))
    s.append(line(SX, SY - 52, SX + 96, SY - 52, ACCD, 1.4))
    s.append(T(SX + 100, SY - 46, "10 µA", 20, ACCD, anchor="start", weight="700"))
    s.append(line(SX, SY - 88, SX + 60, SY - 88, ACC, 1.4))
    s.append(T(SX + 64, SY - 82, "25 µA", 20, ACC, anchor="start"))

    s.append(box(636, 396, 292, 88, CHIPF, CHIPL, 12, 1.4))
    s.append(T(782, 428, "记录：被动衰减，半径不可调", 20, BODY))
    s.append(T(782, 460, "刺激：注入电流，半径可调", 20, ACCD, weight="700"))
    return 960, 508, "".join(s)


# ---------- Fig 5 (卡15): 电流聚焦 ----------
def fig_current_steering():
    s = []
    s.append(T(480, 42, "电流聚焦：不动电极，只改电流分配", 30, INK, weight="700"))

    s.append(T(250, 92, "沿电极上下滑动", 25, ACCD, weight="700"))
    TOP, GAP = 136, 96
    scen = [(96, "A 100%", 1.0, 0.0), (250, "A 50% / B 50%", 0.5, 0.5),
            (404, "A 70% / B 30%", 0.7, 0.3)]
    for cx, lab, fa, fb in scen:
        s.append(f'<rect x="{cx - 17}" y="{TOP}" width="34" height="212" rx="9" '
                 f'fill="#FFFFFF" stroke="{GRAY}" stroke-width="2"/>')
        ya, yb = TOP + 54, TOP + 54 + GAP
        for yy, nm, fr in ((ya, "A", fa), (yb, "B", fb)):
            s.append(f'<rect x="{cx - 17}" y="{yy - 15}" width="34" height="30" '
                     f'fill="{ACC}" opacity="{max(fr, 0.0):.2f}"/>')
            s.append(f'<rect x="{cx - 17}" y="{yy - 15}" width="34" height="30" '
                     f'fill="none" stroke="{ACC}" stroke-width="2"/>')
            s.append(T(cx - 26, yy + 7, nm, 19, BODY, anchor="end"))
            s.append(T(cx + 26, yy + 7, f"{int(fr * 100)}%", 18, ACCD if fr else GRAY,
                       anchor="start"))
        cy = ya + (yb - ya) * fb
        s.append(f'<ellipse cx="{cx}" cy="{cy:.0f}" rx="44" ry="38" fill="{ACC}" opacity="0.20"/>')
        s.append(f'<ellipse cx="{cx}" cy="{cy:.0f}" rx="44" ry="38" fill="none" '
                 f'stroke="{ACC}" stroke-width="2" stroke-dasharray="6 5"/>')
        s.append(T(cx, TOP + 244, lab, 20, INK, weight="700"))
        if abs(fb - 0.5) < 0.01:
            s.append(T(cx, TOP + 270, "虚拟触点", 20, ACCD, weight="700"))
    s.append(line(150, TOP + 100, 198, TOP + 100, GRAY, 2, "5 5", marker="ahg"))
    s.append(line(304, TOP + 100, 352, TOP + 100, GRAY, 2, "5 5", marker="ahg"))
    s.append(T(250, TOP + 310, "激活中心连续滑动，电极一动不动", 22, BODY))

    s.append(line(520, 100, 520, 448, LINE, 2))

    s.append(T(730, 92, "沿圆周偏向一侧", 25, ACCD, weight="700"))
    CX, CY, R = 706, 252, 82
    a0, a1 = 135, 225
    r0, r1 = math.radians(a0), math.radians(a1)
    AR = R + 62
    s.append(f'<path d="M{CX},{CY} L{CX + AR * math.cos(r0):.1f},{CY + AR * math.sin(r0):.1f} '
             f'A{AR},{AR} 0 0 1 {CX + AR * math.cos(r1):.1f},{CY + AR * math.sin(r1):.1f} Z" '
             f'fill="{ACC}" opacity="0.20"/>')
    s.append(circ(CX, CY, R, "#FFFFFF", GRAY, 2.5))
    for b0, b1, on in ((135, 225, True), (232, 315, False), (322, 408, False)):
        c0, c1 = math.radians(b0), math.radians(b1)
        s.append(f'<path d="M{CX + R * math.cos(c0):.1f},{CY + R * math.sin(c0):.1f} '
                 f'A{R},{R} 0 0 1 {CX + R * math.cos(c1):.1f},{CY + R * math.sin(c1):.1f}" '
                 f'fill="none" stroke="{ACC if on else CHIPL}" stroke-width="13" '
                 f'stroke-linecap="round"/>')
    s.append(circ(CX, CY, 4, GRAY, GRAY, 1))
    s.append(T(CX - 152, CY + 7, "通电", 20, ACCD, weight="700"))
    s.append(f'<path d="M926,150 C898,208 910,286 890,344" stroke="{WARN}" stroke-width="9" '
             f'fill="none" opacity="0.5" stroke-linecap="round"/>')
    s.append(T(880, 382, "邻近通路", 21, WARN, anchor="middle"))
    s.append(T(880, 406, "→ 避开", 21, WARN, anchor="middle"))
    s.append(T(672, 382, "激活偏向通电那一侧", 22, BODY, anchor="middle"))

    s.append(box(150, 464, 660, 56, TINT, ACC, 14, 1.5))
    s.append(T(480, 499, "可移动、可塑形；不可无限缩小", 26, ACCD, weight="700"))
    return 960, 544, "".join(s)


FIGS = {
    "fig1-inequality": fig_inequality,
    "fig2-three-zones": fig_three_zones,
    "fig3-decoupling": fig_decoupling,
    "fig4-current-distance": fig_current_distance,
    "fig5-current-steering": fig_current_steering,
}


def render(name, w, h, inner):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
           f'viewBox="0 0 {w} {h}" font-family="HeitiSC,Helvetica,Arial,sans-serif">'
           f'{DEFS}<rect width="{w}" height="{h}" fill="#FFFFFF"/>{inner}</svg>')
    html = (f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>'
            f'@font-face{{font-family:"HeitiSC";src:url("file://{FONT}");}}'
            f'*{{margin:0;padding:0}}body{{width:{w}px;height:{h}px}}</style></head>'
            f'<body>{svg}</body></html>')
    tmp = tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8")
    tmp.write(html); tmp.close()
    out = os.path.join(OUT, name + ".png")
    subprocess.run(["npx", "playwright", "screenshot", f"file://{tmp.name}", out,
                    f"--viewport-size={w},{h}", "--wait-for-timeout=600"],
                   check=True, capture_output=True, text=True)
    os.unlink(tmp.name)
    return out


if __name__ == "__main__":
    for name, fn in FIGS.items():
        w, h, inner = fn()
        print("rendered", render(name, w, h, inner), f"({w}x{h})")
