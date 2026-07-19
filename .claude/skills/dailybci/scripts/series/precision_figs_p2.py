"""Series ⑥「侵入式 BCI 要不要放得准」下篇 — self-made SVG schematics.
Rendered to PNG via playwright chromium (series track convention).
"""
import os, math, subprocess, tempfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "series-invasive-bci-precision", "figs-p2")
os.makedirs(OUT, exist_ok=True)

ACC = "#2F6DB5"; ACCD = "#1E4E86"; TINT = "#E9F0F8"
INK = "#1A1A1A"; BODY = "#4A4A4A"; GRAY = "#8A8A8A"; LINE = "#D6DBE2"
WARN = "#C2544D"; WARNT = "#F7ECEB"
CHIPF = "#F2F3F1"; CHIPL = "#DBDCD8"
MID = "#7FA6D0"

DEFS = ('<defs>'
        '<marker id="ah" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" '
        'markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="%s"/></marker>'
        '<marker id="ahw" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" '
        'markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="%s"/></marker>'
        '<marker id="ahg" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" '
        'markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="%s"/></marker>'
        '</defs>' % (ACC, WARN, GRAY))


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


# ---------- Fig 1 (卡3): 微动幅度 vs 单单元区 + 力学失配 ----------
def fig_micromotion():
    s = []
    s.append(T(480, 42, "人脑每个心动周期的位移，数倍于单单元区", 30, INK, weight="700"))

    # scale comparison bars
    X0 = 300
    s.append(T(X0 - 16, 120, "单单元区（上篇）", 22, BODY, anchor="end"))
    s.append(f'<rect x="{X0}" y="102" width="42" height="24" rx="5" fill="{ACC}" opacity="0.75"/>')
    s.append(T(X0 + 56, 121, "约 50 µm", 21, ACCD, anchor="start", weight="700"))

    s.append(T(X0 - 16, 186, "人脑心动周期位移", 22, BODY, anchor="end"))
    s.append(f'<rect x="{X0}" y="168" width="84" height="24" rx="5" fill="{WARN}" opacity="0.30"/>')
    s.append(f'<rect x="{X0}" y="168" width="420" height="24" rx="5" fill="none" '
             f'stroke="{WARN}" stroke-width="2" stroke-dasharray="6 5"/>')
    s.append(T(X0 + 436, 187, "100 – 500 µm", 21, WARN, anchor="start", weight="700"))
    s.append(T(480, 226, "同一把尺子上，位移是单单元区的 2–10 倍", 22, BODY))

    # mismatch
    s.append(line(120, 262, 840, 262, LINE, 1.5))
    s.append(T(480, 302, "为什么这点位移要紧：力学失配", 26, ACCD, weight="700"))
    for cx, nm, val, col in [(268, "硅电极", "约 165 GPa", GRAY),
                             (692, "脑组织", "约 1–10 kPa", ACC)]:
        s.append(box(cx - 118, 344, 236, 104, CHIPF if col == GRAY else TINT,
                     col, 12, 2))
        s.append(T(cx, 384, nm, 26, INK, weight="700"))
        s.append(T(cx, 420, val, 24, BODY if col == GRAY else ACCD, weight="700"))
    s.append(line(392, 396, 566, 396, GRAY, 2, "6 5"))
    s.append(T(480, 382, "相差约 10⁷–10⁸ 倍", 23, WARN, weight="700"))
    s.append(T(480, 470, "（量级差太大，无法按比例作图）", 19, GRAY))

    s.append(box(150, 500, 660, 58, TINT, ACC, 14, 1.5))
    s.append(T(480, 536, "刚性电极几乎不形变，应变集中到界面那一薄层", 25, ACCD, weight="700"))
    return 960, 582, "".join(s)


# ---------- Fig 2 (卡5): 听力半径随时间缩小 ----------
def fig_radius_shrink():
    s = []
    s.append(T(480, 42, "异物反应从两头挤压听力半径", 30, INK, weight="700"))

    for i, (cx, ttl, sub) in enumerate([(260, "植入当时", "神经元紧贴电极"),
                                        (700, "数周之后", "被推到数百微米外")]):
        s.append(T(cx, 92, ttl, 26, ACCD if i == 0 else WARN, weight="700"))
        s.append(T(cx, 120, sub, 21, BODY))
        cy = 250
        # listening radius disc
        r = 108 if i == 0 else 56
        s.append(circ(cx, cy, r, TINT if i == 0 else WARNT, ACC if i == 0 else WARN, 2, "7 6"))
        s.append(T(cx, cy + r + 28, "听力半径", 21, ACC if i == 0 else WARN, weight="700"))
        # electrode
        s.append(f'<rect x="{cx - 9}" y="{cy - 130}" width="18" height="130" rx="4" '
                 f'fill="#FFFFFF" stroke={chr(34)}{GRAY}{chr(34)} stroke-width="2"/>')
        # encapsulation sheath on right panel
        if i == 1:
            s.append(circ(cx, cy, 30, "#E4E4E2", "#B9B9B4", 2))
            s.append(T(cx + 42, cy - 40, "胶质包裹", 20, BODY, anchor="start"))
        # neurons
        import random
        random.seed(7 + i)
        pts = [(18, -40), (26, 24), (-24, 34), (-30, -26), (40, -8), (-44, 12)] if i == 0 else \
              [(96, -54), (112, 40), (-104, 52), (-118, -40), (132, -6), (-90, -70)]
        for dx, dy in pts:
            s.append(circ(cx + dx, cy + dy, 8, ACC if i == 0 else GRAY,
                          ACCD if i == 0 else GRAY, 1.5))
        s.append(T(cx, cy + r + 54, "神经元" + ("在半径内" if i == 0 else "被推到半径外"),
                   20, BODY))

    s.append(line(480, 140, 480, 400, LINE, 2, "5 6"))

    rows = [("空间：kill zone 把源推远",
             "100 µm 内神经元密度降约 40%，4–8 周退到数百微米"),
            ("噪声：阻抗上升把地板抬高",
             "胶质包裹增大界面阻抗，检测外界进一步内缩")]
    for i, (h, d) in enumerate(rows):
        y = 424 + i * 62
        s.append(box(90, y, 780, 52, CHIPF, CHIPL, 10, 1.3))
        s.append(T(112, y + 32, h, 23, WARN, anchor="start", weight="700"))
        s.append(T(430, y + 32, d, 21, BODY, anchor="start"))
    s.append(T(480, 588, "一个把源推远，一个把地板抬高", 25, ACCD, weight="700"))
    return 960, 616, "".join(s)


# ---------- Fig 3 (卡7): 海马 vs 运动皮层 ----------
def fig_drift():
    s = []
    s.append(T(480, 42, "单神经元在漂，群体的低维结构却稳", 30, INK, weight="700"))
    s.append(line(480, 76, 480, 470, LINE, 2))

    # --- left: hippocampus overlap ---
    s.append(T(240, 108, "海马（小鼠）", 26, WARN, weight="700"))
    s.append(T(240, 138, "每天换一批位置细胞", 21, BODY))
    c1, c2, cy, r = 192, 304, 258, 76
    s.append(circ(c1, cy, r, WARNT, WARN, 2))
    s.append(circ(c2, cy, r, WARNT, WARN, 2))
    s.append(T(126, cy - 92, "第 1 天", 21, BODY))
    s.append(T(372, cy - 92, "第 2 天", 21, BODY))
    s.append(f'<path d="M248,{cy - 51} A76,76 0 0 1 248,{cy + 51} A76,76 0 0 1 248,{cy - 51} Z" '
             f'fill="{WARN}" opacity="0.45"/>')
    s.append(T(248, cy - 74, "15–25%", 22, WARN, weight="700"))
    s.append(T(240, cy + 128, "仅这一小撮重叠且保持原位置野", 21, BODY))
    s.append(T(240, cy + 158, "却已足够维持数周的空间表征", 21, BODY))

    # --- right: motor cortex manifold ---
    s.append(T(720, 108, "运动皮层（猕猴，2 年）", 26, ACCD, weight="700"))
    s.append(T(720, 138, "单元换人，流形不变", 21, BODY))
    mx, my = 720, 250
    import random
    random.seed(3)
    for dx, col, seed in ((-104, ACCD, 3), (104, "#9AA0A6", 9)):
        cx0 = mx + dx
        s.append(f'<ellipse cx="{cx0}" cy="{my}" rx="76" ry="46" fill="{ACC}" '
                 f'opacity="0.16" transform="rotate(-18 {cx0} {my})"/>')
        s.append(f'<ellipse cx="{cx0}" cy="{my}" rx="76" ry="46" fill="none" stroke="{ACC}" '
                 f'stroke-width="2.2" transform="rotate(-18 {cx0} {my})"/>')
        random.seed(seed)
        for _ in range(10):
            a = random.uniform(0, 6.28); rr = random.uniform(0, 0.78)
            px = cx0 + 66 * rr * math.cos(a); py = my + 40 * rr * math.sin(a)
            s.append(circ(px, py, 5, col, col, 1))
    s.append(line(mx - 20, my, mx + 20, my, GRAY, 2, "5 5", marker="ahg"))
    s.append(T(mx, my - 74, "形状全等", 21, ACCD, weight="700"))
    s.append(T(mx - 104, my + 80, "第 1 天", 21, BODY))
    s.append(T(mx + 104, my + 80, "两年后", 21, BODY))
    s.append(T(720, my + 116, "点 = 记录到的神经元，换了一批", 21, BODY))
    s.append(T(720, my + 146, "但低维流形的形状保持稳定", 21, ACCD, weight="700"))

    s.append(box(110, 490, 740, 92, TINT, ACC, 14, 1.5))
    s.append(T(480, 524, "固定解码器（建在原始神经活动上）明显退化", 24, BODY))
    s.append(T(480, 558, "建在稳定流形上的解码器，两年都可靠", 25, ACCD, weight="700"))
    return 960, 606, "".join(s)


# ---------- Fig 4 (卡9): 一条性质救三个问题 ----------
def fig_one_property():
    s = []
    s.append(T(480, 44, "三个不相干的问题，救法出自同一条性质", 30, INK, weight="700"))

    rows = [("放不准", "空间问题", "撒一批电极，总有一些落在能记到信号的地方"),
            ("通道坏掉", "生物问题", "好通道还够多，解码器丢掉坏的接着用"),
            ("编码漂移", "编码问题", "单元在漂，群体的低维结构稳，对齐回去就行")]
    for i, (nm, kind, fix) in enumerate(rows):
        y = 96 + i * 108
        s.append(box(60, y, 250, 88, CHIPF, CHIPL, 12, 1.4))
        s.append(T(90, y + 38, nm, 26, INK, anchor="start", weight="700"))
        s.append(T(90, y + 70, kind, 21, GRAY, anchor="start"))
        s.append(line(322, y + 44, 372, y + 44, GRAY, 2, marker="ahg"))
        s.append(box(386, y, 514, 88, TINT, ACC, 12, 1.4))
        s.append(T(410, y + 52, fix, 22, ACCD, anchor="start"))

    s.append(box(60, 434, 840, 74, "#FFFFFF", ACC, 14, 2))
    s.append(T(480, 468, "共用的前提只有一条", 22, GRAY))
    s.append(T(480, 500, "信息铺在一大群神经元里，不锁在任何一个身上", 27, ACCD, weight="700"))
    return 960, 542, "".join(s)


# ---------- Fig 5 (卡10): 坐标系转了，形状没变 ----------
def fig_alignment():
    s = []
    s.append(T(480, 42, "变的是坐标系，不是形状", 30, INK, weight="700"))

    def ring(cx, cy, rot, col, label_top):
        out = []
        out.append(circ(cx, cy, 74, "none", col, 1.6, "5 6"))
        for k in range(8):
            a = math.radians(-90 + k * 45 + rot)
            px = cx + 74 * math.cos(a); py = cy + 74 * math.sin(a)
            hot = (k == 0)
            out.append(circ(px, py, 9 if hot else 6,
                            col if hot else "#FFFFFF", col, 2))
            if hot:
                out.append(T(px, py - 20, label_top, 20, col, weight="700"))
        return "".join(out)

    panels = [(180, 0, ACC, "第 1 天", "「上」在环顶"),
              (480, 115, WARN, "第 30 天", "环整体转了"),
              (790, 0, ACC, "对齐后", "「上」回到环顶")]
    for cx, rot, col, ttl, sub in panels:
        s.append(T(cx, 100, ttl, 25, col, weight="700"))
        s.append(ring(cx, 250, rot, col, "上"))
        s.append(T(cx, 366, sub, 21, BODY))

    s.append(line(268, 250, 336, 250, GRAY, 2, "5 5", marker="ahg"))
    s.append(T(302, 236, "神经元换了一批", 19, GRAY))
    s.append(f'<path d="M604,250 A56,56 0 0 1 700,232" fill="none" stroke="{ACCD}" '
             f'stroke-width="2.5" marker-end="url(#ah)"/>')
    s.append(T(652, 300, "转回去", 21, ACCD, weight="700"))

    s.append(T(480, 412, "解码器死认位置，于是把转过来的点按旧含义解读", 23, WARN))
    s.append(box(120, 434, 720, 84, TINT, ACC, 14, 1.5))
    s.append(T(480, 468, "转多少度，靠环上流动的时间模式对齐即可确定", 25, ACCD, weight="700"))
    s.append(T(480, 500, "不需要知道用户当时在想什么", 23, ACC))
    return 960, 552, "".join(s)


# ---------- Fig 6 (卡12): 密集低维 vs 稀疏 ----------
def fig_dense_sparse():
    s = []
    s.append(T(480, 42, "信号一旦稀疏，随机撒网就碰不到", 30, INK, weight="700"))
    import random

    for i, (cx, ttl, sub, nlit, col) in enumerate([
            (250, "密集、低维", "很多神经元各带一部分信息", 34, ACC),
            (710, "稀疏", "只有极少数神经元携带该变量", 4, WARN)]):
        s.append(T(cx, 96, ttl, 27, col, weight="700"))
        s.append(T(cx, 126, sub, 21, BODY))
        random.seed(11 + i)
        cells = []
        for r in range(7):
            for c in range(7):
                px = cx - 138 + c * 46 + random.uniform(-6, 6)
                py = 176 + r * 40 + random.uniform(-5, 5)
                cells.append((px, py))
        lit = set(random.sample(range(len(cells)), nlit))
        for k, (px, py) in enumerate(cells):
            if k in lit:
                s.append(circ(px, py, 9, col, col, 1.5))
            else:
                s.append(circ(px, py, 7, "#FFFFFF", "#D8DBE0", 1.5))
        # random electrode sites
        random.seed(41 + i)
        for _ in range(4):
            k = random.randrange(len(cells))
            px, py = cells[k]
            s.append(circ(px, py, 20, "none", INK, 2, "4 4"))
        s.append(T(cx, 476, "圈 = 随机落点的电极", 20, GRAY))
        s.append(T(cx, 508, "随机采样也够" if i == 0 else "大概率全部落空",
                   23, col, weight="700"))

    s.append(line(480, 150, 480, 460, LINE, 2, "5 6"))
    s.append(box(120, 532, 720, 56, TINT, ACC, 14, 1.5))
    s.append(T(480, 567, "密集低维 → 冗余成立　　稀疏 → 冗余失效", 26, ACCD, weight="700"))
    return 960, 612, "".join(s)


# ---------- Fig 7 (卡15): 维度谱 ----------
def fig_dimension_spectrum():
    s = []
    s.append(T(480, 42, "维度是任务的函数，不是脑区的标签", 30, INK, weight="700"))

    X0, X1, Y = 120, 860, 250
    s.append(line(X0, Y, X1, Y, GRAY, 2.5, marker="ahg"))
    s.append(T(X0, Y + 42, "低维", 22, BODY))
    s.append(T(X1 - 20, Y + 42, "高维", 22, BODY))

    items = [(212, "运动皮层", "定型动作", "约 10 维", ACC),
             (452, "前额叶", "复杂认知", "高维·混合选择性", MID),
             (668, "视觉皮层", "自然刺激", "高维·幂律 1/n", MID),
             (846, "全脑", "大尺度记录", "未见饱和", GRAY)]
    for x, nm, task, val, col in items:
        s.append(circ(x, Y, 9, col, col, 1.5))
        s.append(T(x, Y - 96, nm, 24, INK, weight="700"))
        s.append(T(x, Y - 68, task, 20, GRAY))
        s.append(line(x, Y - 56, x, Y - 16, col, 1.6))
        s.append(T(x, Y + 82, val, 21, col if col != GRAY else BODY))

    # task-dependence arrow on motor cortex
    s.append(f'<path d="M212,{Y + 116} C300,{Y + 152} 380,{Y + 152} 452,{Y + 118}" '
             f'fill="none" stroke="{WARN}" stroke-width="2.2" stroke-dasharray="6 5" '
             f'marker-end="url(#ahw)"/>')
    s.append(T(332, Y + 186, "同一个运动皮层，换成更丰富的自然行为", 22, WARN))
    s.append(T(332, Y + 214, "维度就会往右移", 22, WARN, weight="700"))

    s.append(box(120, 512, 720, 82, TINT, ACC, 14, 1.5))
    s.append(T(480, 546, "维度 =（脑区 × 任务 × 记录尺度）的函数", 26, ACCD, weight="700"))
    s.append(T(480, 578, "测到的低维，一部分是简单实验任务造成的", 22, ACC))
    return 960, 626, "".join(s)


FIGS = {
    "p2fig1-micromotion": fig_micromotion,
    "p2fig2-radius-shrink": fig_radius_shrink,
    "p2fig3-drift": fig_drift,
    "p2fig4-one-property": fig_one_property,
    "p2fig5-alignment": fig_alignment,
    "p2fig6-dense-sparse": fig_dense_sparse,
    "p2fig7-dimension": fig_dimension_spectrum,
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
