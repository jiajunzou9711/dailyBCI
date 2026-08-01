"""DLAG / mDLAG 方法论期 — 自制 SVG 示意图（2026-08-01）.

主线: 问题变了 -> 老工具的位置 -> 六步结构 -> 三处关键原理 -> 结果怎么读.
渲染: playwright chromium screenshot.
"""
import math
import os
import subprocess
import tempfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-08-01-dlag", "figs")
os.makedirs(OUT, exist_ok=True)

ACC = "#2F6DB5"; ACCD = "#1E4E86"; TINT = "#E9F0F8"
INK = "#1A1A1A"; BODY = "#4A4A4A"; GRAY = "#8A8A8A"; LINE = "#D6DBE2"
RED = "#C0392B"; REDT = "#F7E9E7"; GRN = "#2E7D57"; GRNT = "#E7F2EC"
AMB = "#8A6D1A"; AMBT = "#FBF7E9"; AMBL = "#D9C98A"
CARD_L = "#DCE5F0"

DEFS = (
    '<defs>'
    '<marker id="ah" markerWidth="10" markerHeight="10" refX="8" refY="3" '
    'orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="%s"/></marker>'
    '<marker id="ahr" markerWidth="10" markerHeight="10" refX="8" refY="3" '
    'orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="%s"/></marker>'
    '<marker id="ahg" markerWidth="10" markerHeight="10" refX="8" refY="3" '
    'orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="%s"/></marker>'
    '</defs>' % (ACC, RED, GRAY)
)


def T(x, y, s, size=25, fill=INK, anchor="middle", weight="400"):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" font-weight="{weight}">{s}</text>')


def box(x, y, w, h, fill, stroke, rx=12, sw=1.5, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')


def line(x1, y1, x2, y2, stroke=INK, sw=2, dash=None, marker=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    m = f' marker-end="url(#{marker})"' if marker else ""
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" '
            f'stroke-width="{sw}"{d}{m}/>')


def circ(cx, cy, r, fill, stroke, sw=1.5):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw}"/>')


def poly(pts, stroke, sw=2.5, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return (f'<polyline points="{p}" fill="none" stroke="{stroke}" '
            f'stroke-width="{sw}" stroke-linejoin="round"{d}/>')


# ---------------------------------------------------------------- 目录卡
def toc():
    s = []
    items = [
        ("1", "问题变了", "一次记录同时覆盖十几个脑区"),
        ("2", "老工具的位置", "方向与维度只能占一边"),
        ("3", "六步结构", "每一步解决上一步暴露的问题"),
        ("4", "三处关键原理", "判断结果可信度的依据"),
        ("5", "结果怎么读", "可读与不可读的清单"),
        ("6", "局限与地位", "结论该打多少折"),
    ]
    y = 30
    for n, title, sub in items:
        s.append(box(30, y, 900, 78, "#F7F9FC", CARD_L, 14, 1.5))
        s.append(circ(78, y + 39, 26, TINT, ACC, 1.5))
        s.append(T(78, y + 49, n, 30, ACCD, weight="700"))
        s.append(T(126, y + 34, title, 30, INK, anchor="start", weight="700"))
        s.append(T(126, y + 64, sub, 22, GRAY, anchor="start"))
        y += 92
    return 960, y + 20, "".join(s)


# ---------------------------------------------------------------- 卡3 场景
def fig_scene():
    s = []
    s.append(T(480, 46, "记录规模变了，能问的问题也变了", 28, INK, weight="700"))

    # 左：单区
    s.append(box(40, 76, 420, 330, "#FAFBFD", CARD_L, 16, 1.5))
    s.append(T(250, 116, "过去：一次记录一个区", 25, GRAY, weight="700"))
    s.append(circ(250, 210, 58, TINT, ACC, 2))
    s.append(T(250, 220, "A 区", 26, ACCD, weight="700"))
    s.append(box(90, 300, 320, 76, TINT, ACC, 12, 1.5))
    s.append(T(250, 330, "问题：这个区编码什么", 24, ACCD, weight="700"))
    s.append(T(250, 360, "对象是单个群体内部", 21, BODY))

    # 右：多区
    s.append(box(500, 76, 420, 330, "#FAFBFD", CARD_L, 16, 1.5))
    s.append(T(710, 116, "现在：同时记录十几个区", 25, ACCD, weight="700"))
    cx, cy, R = 710, 208, 74
    nodes = []
    for i in range(6):
        a = math.radians(-90 + i * 60)
        nodes.append((cx + R * math.cos(a), cy + R * math.sin(a)))
    for i in range(6):
        for j in range(i + 1, 6):
            s.append(line(nodes[i][0], nodes[i][1], nodes[j][0], nodes[j][1],
                          "#B9CCE4", 1.6))
    for i, (nx, ny) in enumerate(nodes):
        s.append(circ(nx, ny, 22, TINT, ACC, 1.8))
    s.append(box(540, 300, 340, 76, TINT, ACC, 12, 1.5))
    s.append(T(710, 330, "问题：这些区之间共享什么", 24, ACCD, weight="700"))
    s.append(T(710, 360, "谁的活动领先", 21, BODY))

    # 底部条
    s.append(box(40, 428, 880, 74, AMBT, AMBL, 14, 1.5))
    s.append(T(480, 464, "后一类问题只在同时记录下才存在", 26, AMB, weight="700"))
    s.append(T(480, 492, "两个神经元没有在同一时刻被记录，它们之间的协同波动就没有数据可算",
                22, BODY))
    return 960, 526, "".join(s)


# ---------------------------------------------------------------- 卡5 判据
def fig_decide():
    s = []
    s.append(T(480, 44, "三个条件同时满足，才值得用这类模型", 28, INK, weight="700"))
    conds = [("① 多个群体之间", "而非单个群体内部"),
             ("② 关心方向", "哪个区的活动领先"),
             ("③ 需要逐试次", "试次平均不够用")]
    x = 40
    for t, sub in conds:
        s.append(box(x, 68, 280, 86, TINT, ACC, 12, 1.5))
        s.append(T(x + 140, 102, t, 25, ACCD, weight="700"))
        s.append(T(x + 140, 133, sub, 21, BODY))
        x += 300

    s.append(T(480, 196, "只满足一两条时，更简单的工具足够", 25, GRAY, weight="700"))
    rows = [("这个区能否编码变量 X", "解码器（回归 / 分类）"),
            ("两个神经元之间有无有向关系", "Granger 因果"),
            ("这个群体主要沿哪些方向变异", "PCA"),
            ("两个区的活动有多少重合", "CCA / communication subspace"),
            ("单个群体的逐试次动力学", "GPFA")]
    y = 218
    s.append(box(40, y, 880, 44, TINT, ACC, 10, 1.5))
    s.append(T(70, y + 30, "你的问题", 23, ACCD, anchor="start", weight="700"))
    s.append(T(530, y + 30, "用什么", 23, ACCD, anchor="start", weight="700"))
    y += 48
    for q, tool in rows:
        s.append(box(40, y, 880, 48, "#FAFBFD", CARD_L, 10, 1.2))
        s.append(T(70, y + 32, q, 23, BODY, anchor="start"))
        s.append(T(530, y + 32, tool, 23, INK, anchor="start", weight="700"))
        y += 52
    return 960, y + 16, "".join(s)


# ---------------------------------------------------------------- 卡6 定位
def fig_position():
    s = []
    s.append(T(480, 42, "维度与方向，老工具只能占一边", 28, INK, weight="700"))
    X0, X1, Y0, Y1 = 130, 900, 100, 470
    s.append(box(X0, Y0, X1 - X0, Y1 - Y0, "#FCFDFE", LINE, 10, 1.5))
    s.append(line((X0 + X1) / 2, Y0, (X0 + X1) / 2, Y1, LINE, 1.5, "6 6"))
    s.append(line(X0, (Y0 + Y1) / 2, X1, (Y0 + Y1) / 2, LINE, 1.5, "6 6"))
    # axes labels
    s.append(T((X0 + X1) / 2, Y1 + 40, "能否给出方向（谁领先）", 24, INK, weight="700"))
    s.append(T(X0 + 150, Y1 + 40, "无", 22, GRAY))
    s.append(T(X1 - 150, Y1 + 40, "有", 22, GRAY))
    s.append(f'<text x="60" y="{(Y0+Y1)/2}" font-size="24" fill="{INK}" '
             f'text-anchor="middle" font-weight="700" '
             f'transform="rotate(-90 60 {(Y0+Y1)/2})">能否给出维度（有几路）</text>')

    def tool(cx, cy, name, note, fill, stroke, tc):
        s.append(box(cx - 145, cy - 44, 290, 88, fill, stroke, 12, 1.6))
        s.append(T(cx, cy - 8, name, 25, tc, weight="700"))
        s.append(T(cx, cy + 24, note, 20, BODY))

    tool(300, 152, "PCA", "不区分共享与私有", "#FAFBFD", CARD_L, INK)
    tool(300, 244, "CCA / 通信子空间", "时间关系被预先设定", "#FAFBFD", CARD_L, INK)
    tool(300, 400, "成对相关", "只有强弱", "#FAFBFD", CARD_L, INK)
    tool(700, 400, "Granger 因果", "配对数量随神经元数平方增长", "#FAFBFD", CARD_L, INK)
    s.append(box(555, 130, 290, 118, TINT, ACC, 14, 2.2, "8 6"))
    s.append(T(700, 172, "DLAG / mDLAG", 27, ACCD, weight="700"))
    s.append(T(700, 206, "维度与方向同时给出", 22, ACCD))
    s.append(T(700, 234, "并支持逐试次", 22, BODY))
    return 960, Y1 + 66, "".join(s)


# ---------------------------------------------------------------- 卡7 六步
def fig_sixsteps():
    s = []
    s.append(T(480, 40, "六步结构：每一步解决上一步暴露的问题", 28, INK, weight="700"))
    s.append(T(300, 76, "遇到的问题", 22, RED, weight="700"))
    s.append(T(750, 76, "对应的处理", 22, ACCD, weight="700"))
    steps = [
        ("两两相关表有 N²/2 个数，难解读也不可靠", "假设相关来自少数共同成分"),
        ("真共享与各自的独立波动混在一起", "划出私有成分"),
        ("动作电位太稀疏，单个时间窗估不出东西", "加时间平滑先验"),
        ("区内局部结构远强于跨区结构", "给潜在成分预先分类"),
        ("只知道有关系，不知道谁领先", "每条跨区成分配一个延迟"),
        ("组数多了，归属子集组合数爆炸", "归属改由估计得出"),
    ]
    y = 96
    for i, (p, f) in enumerate(steps, 1):
        s.append(box(30, y, 480, 62, REDT, "#E3B7B1", 12, 1.3))
        s.append(T(52, y + 39, p, 22, BODY, anchor="start"))
        s.append(line(516, y + 31, 552, y + 31, ACC, 2.4, None, "ah"))
        s.append(box(560, y, 370, 62, TINT, ACC, 12, 1.3))
        s.append(circ(592, y + 31, 17, "#FFFFFF", ACC, 1.5))
        s.append(T(592, y + 39, str(i), 22, ACCD, weight="700"))
        s.append(T(618, y + 39, f, 22, ACCD, anchor="start", weight="700"))
        y += 72
    return 960, y + 12, "".join(s)


# ---------------------------------------------------------------- 卡8 协方差表
def fig_cov():
    s = []
    s.append(T(480, 42, "私有成分只能影响对角线", 28, INK, weight="700"))
    names = ["神经元 1", "神经元 2", "神经元 3"]
    x0, y0, cw, ch = 250, 110, 210, 92
    for j, n in enumerate(names):
        s.append(T(x0 + cw * j + cw / 2, y0 - 16, n, 22, GRAY))
    for i, n in enumerate(names):
        s.append(T(x0 - 20, y0 + ch * i + ch / 2 + 8, n, 22, GRAY, anchor="end"))
    for i in range(3):
        for j in range(3):
            cx, cy = x0 + cw * j, y0 + ch * i
            if i == j:
                s.append(box(cx + 4, cy + 4, cw - 8, ch - 8, AMBT, AMBL, 10, 1.6))
                s.append(T(cx + cw / 2, cy + ch / 2 - 2, "共享 + 私有", 22, AMB, weight="700"))
                s.append(T(cx + cw / 2, cy + ch / 2 + 26, "两者都有份", 19, BODY))
            else:
                s.append(box(cx + 4, cy + 4, cw - 8, ch - 8, TINT, ACC, 10, 1.6))
                s.append(T(cx + cw / 2, cy + ch / 2 - 2, "只能由载荷产生", 21, ACCD, weight="700"))
                s.append(T(cx + cw / 2, cy + ch / 2 + 26, "私有贡献恒为 0", 19, BODY))
    yb = y0 + ch * 3 + 26
    s.append(box(40, yb, 880, 116, "#FAFBFD", CARD_L, 14, 1.5))
    s.append(T(480, yb + 40, "不同神经元之间的协方差，全部由载荷承担", 25, INK, weight="700"))
    s.append(T(480, yb + 74, "这是共享与私有能被分开的依据", 22, BODY))
    s.append(T(480, yb + 102, "也说明每组神经元太少时这个划分解不开：两个神经元时无解", 21, GRAY))
    return 960, yb + 142, "".join(s)


# ---------------------------------------------------------------- 卡9 稀疏
def fig_sparse_a():
    s = []
    s.append(T(480, 40, "逐窗估计不可用，所以要让相邻时刻互相提供信息", 27, INK, weight="700"))

    # panel A
    s.append(box(30, 60, 900, 216, "#FCFDFE", LINE, 12, 1.4))
    s.append(T(52, 90, "5 ms 分箱的动作电位（20 个箱，共 3 个事件）", 22, GRAY, anchor="start"))
    bx0, bw = 80, 40
    for i in range(20):
        s.append(line(bx0 + i * bw, 104, bx0 + i * bw, 128, "#E8EDF3", 1))
    s.append(line(bx0, 128, bx0 + 20 * bw, 128, LINE, 1.5))
    for b in (3, 10, 17):
        cxp = bx0 + (b - 0.5) * bw
        s.append(line(cxp, 100, cxp, 128, ACCD, 4))
    # step estimate
    base, top = 246, 160
    s.append(line(bx0, base, bx0 + 20 * bw, base, LINE, 1.5))
    s.append(T(66, base + 6, "0", 20, GRAY, anchor="end"))
    s.append(T(66, top + 6, "200", 20, GRAY, anchor="end"))
    pts = []
    for i in range(20):
        yv = top if (i + 1) in (3, 10, 17) else base
        pts.append((bx0 + i * bw, yv)); pts.append((bx0 + (i + 1) * bw, yv))
    s.append(poly(pts, RED, 2.4))
    s.append(T(905, top - 22, "Hz", 20, GRAY, anchor="end"))
    s.append(line(bx0, base - 8, bx0 + 20 * bw, base - 8, GRN, 2.6, "7 5"))
    s.append(T(905, 90, "红：逐窗估计　绿：真实发放率", 21, BODY, anchor="end"))
    s.append(box(30, 296, 900, 62, AMBT, AMBL, 12, 1.5))
    s.append(T(480, 334, "单个时间窗里的证据不足以支撑任何估计，只能借用邻近时刻",
                24, AMB, weight="700"))
    return 960, 380, "".join(s)


# ---------------------------------------------------------------- 卡10 旋转
def fig_sparse_b():
    s = []
    yb = 20
    s.append(T(480, yb + 14, "时间尺度不同的两条成分，混合后不再合法", 27, INK, weight="700"))
    z1 = [0.2, 0.5, 0.8, 1.0, 1.0, 0.8, 0.5, 0.2, -0.1, -0.4]
    z2 = [1.0, -0.9, 0.8, -1.0, 0.9, -0.8, 1.0, -0.9, 0.8, -1.0]
    zm = [0.85, -0.28, 1.13, 0.00, 1.34, 0.00, 1.06, -0.50, 0.50, -0.99]
    panels = [(40, "慢成分", z1, ACC), (350, "快成分", z2, GRAY), (660, "两者混合", zm, RED)]
    for px, label, zz, col in panels:
        s.append(box(px, yb + 16, 260, 168, "#FCFDFE", LINE, 12, 1.4))
        mid = yb + 100
        s.append(line(px + 16, mid, px + 244, mid, LINE, 1.2, "4 4"))
        pts = [(px + 22 + i * 24, mid - v * 46) for i, v in enumerate(zz)]
        s.append(poly(pts, col, 2.6))
        s.append(T(px + 130, yb + 210, label, 24, col, weight="700"))
    s.append(T(170, yb + 244, "相邻落差小 · 长程有漂移", 21, BODY))
    s.append(T(480, yb + 244, "相邻落差大 · 长程无结构", 21, BODY))
    s.append(T(790, yb + 244, "相邻落差大 · 长程有漂移", 21, RED, weight="700"))
    s.append(box(40, yb + 264, 880, 62, AMBT, AMBL, 12, 1.5))
    s.append(T(480, yb + 302, "单一时间尺度给不出「近处骤变、远处仍有关联」，混合后的曲线被模型排除",
                23, AMB, weight="700"))
    return 960, yb + 348, "".join(s)


# ---------------------------------------------------------------- 图注册


# ---------------------------------------------------------------- 卡11 延迟
def fig_delay():
    s = []
    s.append(T(480, 40, "方向来自时间差", 28, INK, weight="700"))
    X0, X1 = 90, 900
    base = 300
    s.append(line(X0, base, X1, base, LINE, 1.5))

    def bump(shift, col, dash=None):
        pts = []
        for k in range(0, 81):
            t = 20 + k * 0.75
            v = math.exp(-((t - 50 - shift) ** 2) / 450.0)
            x = X0 + (t - 20) / 60.0 * (X1 - X0)
            pts.append((x, base - v * 170))
        return poly(pts, col, 3.0, dash)

    s.append(bump(0, ACC))
    s.append(bump(12, RED))
    xa = X0 + (50 - 20) / 60.0 * (X1 - X0)
    xb = X0 + (62 - 20) / 60.0 * (X1 - X0)
    s.append(line(xa, base - 170, xa, base + 22, ACC, 1.6, "5 5"))
    s.append(line(xb, base - 170, xb, base + 22, RED, 1.6, "5 5"))
    s.append(line(xa, base + 40, xb, base + 40, INK, 2, None, "ah"))
    s.append(T((xa + xb) / 2, base + 32, "延迟", 22, INK, weight="700"))
    s.append(T(xa - 14, base - 186, "A 区", 24, ACC, anchor="end", weight="700"))
    s.append(T(xb + 14, base - 186, "B 区", 24, RED, anchor="start", weight="700"))
    s.append(T(480, base + 78, "同一条时间过程，在两个区出现的时刻不同；延迟的符号给出方向",
                23, BODY))

    y = base + 106
    s.append(box(40, y, 430, 118, GRNT, GRN, 12, 1.5))
    s.append(T(255, y + 40, "变化快的成分", 25, GRN, weight="700"))
    s.append(T(255, y + 76, "平移一点就明显对不上", 22, BODY))
    s.append(T(255, y + 104, "延迟被约束得紧，方向可信", 21, BODY))
    s.append(box(490, y, 430, 118, REDT, RED, 12, 1.5))
    s.append(T(705, y + 40, "变化慢的成分", 25, RED, weight="700"))
    s.append(T(705, y + 76, "平移一点看不出差别", 22, BODY))
    s.append(T(705, y + 104, "延迟约束松，方向可能定不下来", 21, BODY))
    return 960, y + 148, "".join(s)


# ---------------------------------------------------------------- 卡13 结果怎么读
def fig_read():
    s = []
    s.append(T(480, 42, "输出并非每一项都可以直接解读", 28, INK, weight="700"))
    rows = [
        ("解释方差百分比", "可以", "依赖成分条数与纳入的脑区集合", GRN),
        ("归属子集（涉及哪些区）", "可以", "依赖阈值，需看一段阈值范围", GRN),
        ("载荷的相对符号（谁与谁同相）", "可以", "无附加条件", GRN),
        ("成分曲线的形状", "有条件", "时间尺度须与其他成分明显不同", AMB),
        ("延迟与方向", "有条件", "仅在成分变化足够快时可信", AMB),
        ("成员极少的成分", "需警惕", "可能来自分选污染或成对耦合", AMB),
        ("成分的绝对数值", "不能", "尺度由约定固定，纵轴为任意单位", RED),
        ("成分与载荷的整体符号", "不能", "同时取负后数据不变", RED),
    ]
    y = 74
    s.append(box(30, y, 900, 44, TINT, ACC, 10, 1.5))
    s.append(T(56, y + 30, "输出", 22, ACCD, anchor="start", weight="700"))
    s.append(T(430, y + 30, "能否解读", 22, ACCD, anchor="start", weight="700"))
    s.append(T(560, y + 30, "条件", 22, ACCD, anchor="start", weight="700"))
    y += 48
    for name, verdict, cond, col in rows:
        s.append(box(30, y, 900, 50, "#FAFBFD", CARD_L, 10, 1.2))
        s.append(T(56, y + 33, name, 22, INK, anchor="start"))
        s.append(T(430, y + 33, verdict, 22, col, anchor="start", weight="700"))
        s.append(T(560, y + 33, cond, 21, BODY, anchor="start"))
        y += 54
    return 960, y + 14, "".join(s)


FIGS = {
    "toc": toc,
    "fig-scene": fig_scene,
    "fig-decide": fig_decide,
    "fig-position": fig_position,
    "fig-sixsteps": fig_sixsteps,
    "fig-cov": fig_cov,
    "fig-sparse-a": fig_sparse_a,
    "fig-sparse-b": fig_sparse_b,
    "fig-delay": fig_delay,
    "fig-read": fig_read,
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
        p = render(name, w, h, inner)
        print("rendered", p, f"({w}x{h})")
