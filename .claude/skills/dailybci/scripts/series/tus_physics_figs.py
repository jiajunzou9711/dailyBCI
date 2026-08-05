"""TUS 物理原理 first-principles schematics (2026-08-05 方法论期).
自制 SVG 示意图，经 playwright chromium 渲染成 PNG。
"""
import os, math, subprocess, tempfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-08-05-tus-lgn", "figs")
os.makedirs(OUT, exist_ok=True)

ACC = "#2F6DB5"; ACCD = "#1E4E86"; TINT = "#E9F0F8"
INK = "#1A1A1A"; BODY = "#4A4A4A"; GRAY = "#8A8A8A"; LINE = "#D6DBE2"
RED = "#C0392B"; REDT = "#F7E9E7"; GRN = "#2E7D57"; GRNT = "#E7F2EC"
CARD_L = "#DCE5F0"

DEFS = (
    '<defs>'
    '<marker id="ah" markerWidth="10" markerHeight="10" refX="8" refY="3" '
    'orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="%s"/></marker>'
    '<marker id="ahr" markerWidth="10" markerHeight="10" refX="8" refY="3" '
    'orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="%s"/></marker>'
    '<marker id="ahk" markerWidth="10" markerHeight="10" refX="8" refY="3" '
    'orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="%s"/></marker>'
    '</defs>' % (ACC, RED, INK)
)


def T(x, y, s, size=25, fill=INK, anchor="middle", weight="400"):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" font-weight="{weight}">{s}</text>')


def box(x, y, w, h, fill, stroke, rx=12, sw=1.5):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')


def line(x1, y1, x2, y2, stroke=INK, sw=2, dash=None, marker=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    m = f' marker-end="url(#{marker})"' if marker else ""
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" '
            f'stroke-width="{sw}"{d}{m}/>')


def circ(cx, cy, r, fill, stroke, sw=1.5):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw}"/>')


def dot_field(x0, x1, rows, lam, amp, phase=0.0, r=3.4, colour=INK):
    """分子点阵：静止位置按 sin 被推挤，形成疏密带。"""
    s = []
    n = int((x1 - x0) / 9)
    for i in range(n + 1):
        xr = x0 + i * (x1 - x0) / n
        dx = amp * math.sin(2 * math.pi * (xr - x0) / lam + phase)
        x = xr + dx
        if x < x0 - 2 or x > x1 + 2:
            continue
        for y in rows:
            s.append(f'<circle cx="{x:.1f}" cy="{y}" r="{r}" fill="{colour}" opacity="0.78"/>')
    return "".join(s)


# ---------- Fig 1: 压缩与稀疏的来源、传播、以及某一点的来回 ----------
def fig_wave():
    s = []
    s.append(box(30, 24, 900, 56, TINT, ACC, 12, 1.5))
    s.append(T(480, 60, "压缩区与稀疏区从哪来,怎么走,某一点经历什么", 26, ACCD, weight="700"))

    # ---- ① 换能器的两个半周期 ----
    s.append(T(48, 122, "① 换能器每秒伸缩 50 万次,两个半周期各造出一种区域", 24, INK,
               anchor="start", weight="700"))
    for k, (bx, tit, sub, col, colt, step) in enumerate([
            (48, "表面前伸", "挤压紧邻组织 → 压缩区", RED, REDT, 7),
            (496, "表面后缩", "紧邻组织后退让位 → 稀疏区", ACC, TINT, 17)]):
        s.append(box(bx, 140, 416, 200, "#FCFDFE", CARD_L, 12, 1.5))
        s.append(box(bx + 18, 176, 26, 92, colt, col, 5, 1.6))
        s.append(T(bx + 31, 300, "换能器", 17, GRAY))
        # 伸/缩方向箭头
        ax = bx + 52
        if k == 0:
            s.append(line(ax, 222, ax + 30, 222, col, 3, None, "ahr"))
        else:
            s.append(line(ax + 30, 222, ax, 222, col, 3, None, "ahr"))
        rows = [196, 222, 248]
        # 紧邻层：密(step 小) 或 疏(step 大)
        near0, near1 = bx + 100, bx + 244
        x = near0
        while x <= near1:
            for y in rows:
                s.append(f'<circle cx="{x}" cy="{y}" r="3.4" fill="{INK}" opacity="0.8"/>')
            x += step
        # 远处：常态间距
        x = bx + 258
        while x <= bx + 400:
            for y in rows:
                s.append(f'<circle cx="{x}" cy="{y}" r="3.4" fill="{GRAY}" opacity="0.55"/>')
            x += 12
        s.append(line(near0, 268, near1, 268, col, 1.6))
        s.append(line(near0, 262, near0, 274, col, 1.6))
        s.append(line(near1, 262, near1, 274, col, 1.6))
        s.append(T((near0 + near1) / 2, 290, "紧邻层", 18, col))
        s.append(T(bx + 329, 290, "常态间距", 18, GRAY))
        s.append(T(bx + 250, 166, tit, 23, col, weight="700"))
        s.append(T(bx + 208, 326, sub, 21, BODY))

    # ---- ② 一串压缩/稀疏向前传播 ----
    s.append(T(48, 362, "② 它们一个接一个向前传播,速度 1540 m/s(声速)", 24, INK,
               anchor="start", weight="700"))
    sx, ex = 48, 852
    x0, lam = sx + 16, 190
    s.append(box(sx, 380, ex - sx + 60, 152, "#FCFDFE", CARD_L, 12, 1.5))
    rows = [418, 446, 474]
    s.append(dot_field(x0, ex, rows, lam, 17, 0.0))
    # 疏密标注：压缩中心在 x0+lam*(0.5+n)，稀疏中心在 x0+lam*n
    for n in range(5):
        cx = x0 + lam * n
        if sx + 20 < cx < ex:
            s.append(T(cx, 408, "稀疏", 17, ACC, weight="700"))
        cc = x0 + lam * (n + 0.5)
        if cc < ex:
            s.append(T(cc, 408, "压缩", 17, RED, weight="700"))
    # 波长（相邻两个压缩中心之间）
    b0, b1 = x0 + lam * 0.5, x0 + lam * 1.5
    s.append(line(b0, 496, b1, 496, GRAY, 1.6))
    s.append(line(b0, 490, b0, 502, GRAY, 1.6))
    s.append(line(b1, 490, b1, 502, GRAY, 1.6))
    s.append(T((b0 + b1) / 2, 518, "一个波长 ≈ 3.1 mm", 19, GRAY))
    s.append(line(ex - 150, 518, ex + 40, 518, INK, 2.4, None, "ahk"))
    s.append(T(ex - 40, 506, "传播方向", 19, INK))

    # ---- ③ 固定一点随时间的来回 ----
    s.append(T(48, 578, "③ 盯住组织深处某一个固定点,它经历的是:", 24, INK,
               anchor="start", weight="700"))
    s.append(box(48, 596, 864, 140, "#FCFDFE", CARD_L, 12, 1.5))
    steps = [("压缩区到达", "分子向前", RED, 1), ("稀疏区到达", "分子向后", ACC, -1),
             ("压缩区到达", "分子向前", RED, 1), ("稀疏区到达", "分子向后", ACC, -1)]
    for i, (top, bot, col, d) in enumerate(steps):
        cx = 155 + i * 202
        s.append(T(cx, 630, top, 21, col, weight="700"))
        s.append(circ(cx, 664, 9, col, col, 1))
        if d > 0:
            s.append(line(cx + 16, 664, cx + 58, 664, col, 3, None, "ahr" if col == RED else "ah"))
        else:
            s.append(line(cx - 16, 664, cx - 58, 664, col, 3, None, "ahr" if col == RED else "ah"))
        s.append(T(cx, 708, bot, 21, BODY))
        if i < 3:
            s.append(T(cx + 101, 668, "→", 24, GRAY))
    s.append(T(480, 768, "每秒 50 万轮。分子来回一次移动约 0.15 µm,峰值速度约 0.46 m/s,", 21, BODY))
    s.append(T(480, 796, "始终停在原位附近——向前传播的是状态,不是物质。", 21, BODY))
    return 960, 820, "".join(s)


# ---------- 封面概念图：三道关卡逐层拦掉干扰，只有一条通过 ----------
def cover_concept():
    """概念图：多条来源进入,三道对照各拦下一部分,只有真效应那条通到底。零文字。"""
    W_, H_ = 900, 380
    s = []
    gates = [286, 470, 654]
    x_in, x_out = 34, 872
    # 三道关卡
    for gx in gates:
        s.append(f'<rect x="{gx-7}" y="34" width="14" height="{H_-68}" rx="7" '
                 f'fill="#D9DEE5"/>')

    def wave(x0, x1, y, amp, col, sw, phase=0.0, dot_end=False, fade=False):
        pts = []
        n = int(x1 - x0)
        for i in range(n + 1):
            xx = x0 + i
            yy = y + amp * math.sin(2 * math.pi * i / 62.0 + phase)
            pts.append(f"{xx},{yy:.1f}")
        op = "0.45" if fade else "0.95"
        out = [f'<polyline points="{" ".join(pts)}" fill="none" stroke="{col}" '
               f'stroke-width="{sw}" stroke-linecap="round" opacity="{op}"/>']
        if dot_end:
            out.append(f'<circle cx="{x1}" cy="{y:.1f}" r="{sw*1.5:.1f}" fill="{col}" opacity="{op}"/>')
        return "".join(out)

    G = "#9AA3AD"
    # 四条干扰:两条止于第一道,一条止于第二道,一条止于第三道
    s.append(wave(x_in, gates[0] - 10, 74, 13, G, 5, 0.0, True, True))
    s.append(wave(x_in, gates[0] - 10, 136, 11, G, 5, 1.6, True, True))
    s.append(wave(x_in, gates[1] - 10, 300, 12, G, 5, 0.8, True, True))
    s.append(wave(x_in, gates[2] - 10, 348, 10, G, 5, 2.4, True, True))
    # 真效应:穿过三道,出口更粗更干净
    s.append(wave(x_in, gates[2] + 10, 208, 14, ACC, 6, 0.4))
    s.append(wave(gates[2] + 10, x_out, 208, 14, ACC, 8, 0.4, True))
    return W_, H_, "".join(s)


# ---------- 目录卡 ----------
def toc():
    s = []
    items = [
        ("1", "读数分不清来源", "频率标记只解决其中一半"),
        ("2", "警觉度会同时抬高两侧", "用解剖侧化做同一试次内对照"),
        ("3", "装置只贴在头的一侧", "改焦点深度,而非关掉超声"),
        ("4", "三层合成一个判据", "真实效应只应落在一格里"),
        ("5", "超声脉冲里装着什么", "从载波到一个恒定的单向推力"),
        ("6", "参数为何可能决定方向", "以及证据目前走到哪一步"),
    ]
    y = 26
    for n, title, sub in items:
        s.append(box(30, y, 900, 76, "#F7F9FC", CARD_L, 14, 1.5))
        s.append(circ(76, y + 38, 25, TINT, ACC, 1.5))
        s.append(T(76, y + 48, n, 29, ACCD, weight="700"))
        s.append(T(122, y + 33, title, 29, INK, anchor="start", weight="700"))
        s.append(T(122, y + 62, sub, 21, GRAY, anchor="start"))
        y += 89
    return 960, y + 10, "".join(s)


# ---------- 2×2 判据 ----------
def fig_2x2():
    s = []
    s.append(box(30, 22, 900, 54, TINT, ACC, 12, 1.5))
    s.append(T(480, 57, "三层合起来的判据:真实效应只应落在一格", 26, ACCD, weight="700"))
    cx0, cy0, cw, ch = 300, 150, 300, 132
    s.append(T(cx0 + cw / 2, 132, "被声束覆盖的半视野", 22, INK, weight="700"))
    s.append(T(cx0 + cw + cw / 2, 132, "未被覆盖的半视野", 22, GRAY, weight="700"))
    rows = [("打深部 (70 mm)", True), ("打浅层 (30 mm)", False)]
    for r, (lab, deep) in enumerate(rows):
        yy = cy0 + r * ch
        s.append(T(288, yy + ch / 2 + 8, lab, 22, INK if deep else GRAY,
                   anchor="end", weight="700"))
        for c in range(2):
            xx = cx0 + c * cw
            hit = deep and c == 0
            s.append(box(xx, yy, cw, ch, "#EAF3EC" if hit else "#FBFCFD",
                         GRN if hit else CARD_L, 10, 3 if hit else 1.5))
            if hit:
                s.append(T(xx + cw / 2, yy + ch / 2 - 4, "效应应出现在这里", 23, GRN, weight="700"))
                s.append(T(xx + cw / 2, yy + ch / 2 + 30, "其余三格不应变", 20, GRAY))
    # 其它落点的含义
    y = 440
    s.append(T(48, y, "落点落在别处,各自指向一种解释:", 24, INK, anchor="start", weight="700"))
    alts = [("四格一起变", "全局效应:警觉度、整体皮层兴奋性"),
            ("按半视野分开变,与深度无关", "装置偏侧带来的空间注意效应"),
            ("只有深部一行变,但两半视野一起变", "深部声能有作用,未经由该视觉通路")]
    y += 22
    for a, b in alts:
        s.append(box(48, y, 864, 62, "#FCFDFE", CARD_L, 10, 1.5))
        s.append(T(72, y + 38, a, 22, RED, anchor="start", weight="700"))
        s.append(T(500, y + 38, b, 21, BODY, anchor="start"))
        y += 72
    s.append(T(480, y + 34, "判据在实验开始前定死,看到什么都按它判。", 22, ACCD, weight="700"))
    return 960, y + 60, "".join(s)


# ---------- 脉冲的两层结构 ----------
def fig_pulse():
    s = []
    s.append(box(30, 22, 900, 54, TINT, ACC, 12, 1.5))
    s.append(T(480, 57, "里层是 500 kHz 载波,外层是毫秒级开关包络", 26, ACCD, weight="700"))

    # A 载波
    s.append(T(48, 118, "① 里层:载波(全程不变)", 24, INK, anchor="start", weight="700"))
    s.append(box(48, 134, 864, 150, "#FCFDFE", CARD_L, 12, 1.5))
    mid = 209
    pts = []
    for i in range(0, 761):
        xx = 90 + i
        yy = mid - 46 * math.sin(2 * math.pi * i / 76)
        pts.append(f"{xx},{yy:.1f}")
    s.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{ACC}" stroke-width="2.6"/>')
    s.append(line(90, 262, 166, 262, GRAY, 1.6))
    s.append(line(90, 256, 90, 268, GRAY, 1.6))
    s.append(line(166, 256, 166, 268, GRAY, 1.6))
    s.append(T(128, 282, "2 微秒", 19, GRAY))
    s.append(T(700, 282, "脉冲开着期间一直这样振荡", 20, BODY))

    # B 包络
    s.append(T(48, 330, "② 外层:包络。占空比锁定 10%,脉冲重复频率决定脉冲长度", 24, INK,
               anchor="start", weight="700"))
    s.append(box(48, 348, 864, 300, "#FCFDFE", CARD_L, 12, 1.5))
    x0, wpx = 112, 690          # 视窗 = 20.5 毫秒
    rows = [("4.875 Hz", "脉冲 20.5 ms", [(0.0, 1.0)], "此窗口内一直开着"),
            ("48.75 Hz", "脉冲 2.05 ms", [(i / 10, i / 10 + 0.1) for i in range(1)] +
             [(0.0, 0.1)], ""),
            ("487.5 Hz", "脉冲 0.205 ms", [(i / 10, i / 10 + 0.01) for i in range(10)], "")]
    yb = 392
    for lab, dur, blocks, note in rows:
        s.append(T(104, yb + 40, lab, 22, INK, anchor="end", weight="700"))
        s.append(line(x0, yb + 62, x0 + wpx, yb + 62, LINE, 1.6))
        seen = set()
        for a, b in blocks:
            if (a, b) in seen:
                continue
            seen.add((a, b))
            bx = x0 + a * wpx
            bw = max((b - a) * wpx, 1.6)
            s.append(f'<rect x="{bx:.1f}" y="{yb}" width="{bw:.1f}" height="62" '
                     f'fill="{ACC}" opacity="0.85"/>')
        s.append(T(x0 + wpx + 12, yb + 40, dur, 20, ACCD, anchor="start"))
        if note:
            s.append(T(x0 + wpx / 2, yb + 40, note, 19, "#FFFFFF", weight="700"))
        yb += 84
    s.append(T(480, 686, "视窗 = 20.5 毫秒。三档的总能量相同,变的只有能量被切成什么形状。",
               21, BODY))
    return 960, 712, "".join(s)


# ---------- 两个成分的分化 ----------
def fig_two_comp():
    s = []
    s.append(box(30, 22, 900, 54, TINT, ACC, 12, 1.5))
    s.append(T(480, 57, "振动成分不随脉冲长短变,辐射力位移随之改变", 26, ACCD, weight="700"))

    # 左：位移爬升需要时间
    s.append(box(48, 100, 420, 380, "#FCFDFE", CARD_L, 12, 1.5))
    s.append(T(258, 136, "力一开,位移逐渐爬升", 23, INK, weight="700"))
    bx, by, bw2, bh2 = 92, 158, 330, 50
    s.append(f'<rect x="{bx}" y="{by}" width="{bw2*0.55:.0f}" height="{bh2}" fill="{ACC}" opacity="0.28"/>')
    s.append(T(bx + bw2 * 0.28, by + 33, "力 = F0", 21, ACCD, weight="700"))
    s.append(T(bx + bw2 * 0.78, by + 33, "力 = 0", 21, GRAY))
    ax_y, ax_x0 = 430, 92
    s.append(line(ax_x0, ax_y, ax_x0 + 330, ax_y, INK, 2))
    s.append(line(ax_x0, ax_y, ax_x0, 250, INK, 2))
    pts = []
    for i in range(0, 182):
        t = i / 100.0
        pts.append(f"{ax_x0 + i:.0f},{ax_y - 140 * (1 - math.exp(-t)):.1f}")
    for i in range(182, 331):
        t = (i - 182) / 100.0
        pts.append(f"{ax_x0 + i:.0f},{ax_y - 140 * (1 - math.exp(-1.82)) * math.exp(-t):.1f}")
    s.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{RED}" stroke-width="3"/>')
    s.append(line(ax_x0, ax_y - 140, ax_x0 + 330, ax_y - 140, GRAY, 1.4, "5,4"))
    s.append(T(ax_x0 + 252, ax_y - 148, "平衡位移", 18, GRAY))
    s.append(T(258, 466, "爬升的特征时间:软组织在亚毫秒-毫秒量级", 19, BODY))

    # 右：三档达到的峰值
    s.append(box(492, 100, 420, 380, "#FCFDFE", CARD_L, 12, 1.5))
    s.append(T(702, 136, "三档脉冲各能推到多远", 23, INK, weight="700"))
    base = 406
    s.append(line(540, base - 200, 878, base - 200, GRAY, 1.4, "5,4"))
    s.append(T(566, base - 208, "满位移", 18, GRAY, anchor="start"))
    for i, (lab, frac, col) in enumerate([("20.5 ms", 1.00, RED),
                                          ("2.05 ms", 0.87, "#D98A00"),
                                          ("0.205 ms", 0.21, ACC)]):
        cx = 588 + i * 114
        h = 200 * frac
        s.append(f'<rect x="{cx-38}" y="{base-h:.0f}" width="76" height="{h:.0f}" '
                 f'fill="{col}" opacity="0.75" rx="5"/>')
        s.append(T(cx, base + 30, lab, 20, INK, weight="700"))
    s.append(T(702, 468, "峰值位移差约 5 倍;振动成分三档完全相同", 19, BODY))

    s.append(T(480, 522, "分母(振动)不变、分子(辐射力位移)随脉冲变长而增大,", 22, ACCD, weight="700"))
    s.append(T(480, 552, "两者的比重因此改变。", 22, ACCD, weight="700"))
    return 960, 580, "".join(s)


FIGS = {"cover-concept": cover_concept, "toc": toc, "fig-2x2": fig_2x2,
        "fig-pulse": fig_pulse, "fig-wave-origin": fig_wave,
        "fig-two-comp": fig_two_comp}


def render(name, w, h, inner, bg="#FFFFFF"):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
           f'viewBox="0 0 {w} {h}" font-family="HeitiSC,Helvetica,Arial,sans-serif">'
           f'{DEFS}<rect width="{w}" height="{h}" fill="{bg}"/>{inner}</svg>')
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
        p = render(name, w, h, inner, "#FAFAFA" if name == "cover-concept" else "#FFFFFF")
        print("rendered", p, f"({w}x{h})")
