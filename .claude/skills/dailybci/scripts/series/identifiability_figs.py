"""跨 session 可辨识性 原理期 — 自制 SVG 示意图（2026-07-31）.

主线: 边缘 vs 联合 -> 边缘不决定联合 -> 可辨识性而非估计 -> 判据 -> stitching 的位置.
渲染: playwright chromium screenshot.
"""
import os, subprocess, tempfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-07-31-identifiability", "figs")
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


# ---------------------------------------------------------------- 目录卡
def toc():
    s = []
    items = [
        ("1", "困境在哪", "单神经元分辨率、多脑区、同时,三者难兼得"),
        ("2", "拆词", "「把多次记录拼起来」混着两个意思"),
        ("3", "一次记录给什么", "同时给整张表,分次只给两条边"),
        ("4", "核心", "同样的两条边,可以对应截然不同的真相"),
        ("5", "性质", "多攒试次消不掉这个不确定"),
        ("6", "出路", "一条判据,以及跨 session 模型的位置"),
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


# ---------------------------------------------------------------- 卡3 困境
def fig_dilemma():
    s = []
    s.append(box(30, 24, 900, 56, TINT, ACC, 12, 1.5))
    s.append(T(480, 60, "覆盖范围与信号分辨率,现有手段各占一端", 26, ACCD, weight="700"))

    # left: 大范围低分辨率
    s.append(box(60, 110, 380, 300, GRNT, GRN, 14, 1.5))
    s.append(T(250, 152, "覆盖多个脑区 · 容易", 26, GRN, weight="700"))
    for i, t in enumerate(["EEG  头皮脑电", "MEG  脑磁图", "fMRI 功能磁共振",
                           "功能超声", "ECoG 皮层表面电极"]):
        s.append(T(100, 196 + i * 38, t, 23, BODY, anchor="start"))
    s.append(line(90, 378, 410, 378, GRN, 1.5, "5,4"))
    s.append(T(250, 400, "记录的是场电位或血流信号", 21, GRN))

    # right: 单神经元
    s.append(box(520, 110, 380, 300, REDT, RED, 14, 1.5))
    s.append(T(710, 152, "拿到单个动作电位 · 需侵入", 26, RED, weight="700"))
    for i, t in enumerate(["穿刺式硅探针", "犹他阵列等皮层内电极"]):
        s.append(T(560, 200 + i * 38, t, 23, BODY, anchor="start"))
    s.append(box(556, 258, 308, 92, "#FFFFFF", RED, 10, 1.2))
    s.append(T(710, 292, "一次能同时读多少个位置", 22, INK))
    s.append(T(710, 324, "被记录通道数卡死", 24, RED, weight="700"))
    s.append(line(550, 378, 870, 378, RED, 1.5, "5,4"))
    s.append(T(710, 400, "覆盖范围受通道数限制", 21, RED))

    # bottom conclusion
    s.append(box(60, 440, 840, 76, AMBT, AMBL, 14, 1.5))
    s.append(T(480, 476, "稀缺的是三者的组合", 25, AMB, weight="700"))
    s.append(T(480, 506, "单神经元分辨率   ×   多个脑区   ×   同时", 25, AMB, weight="700"))
    return 960, 540, "".join(s)


# ---------------------------------------------------------------- 卡5 两种拼
def fig_two_joins():
    s = []
    s.append(box(30, 24, 900, 56, TINT, ACC, 12, 1.5))
    s.append(T(480, 60, "「把多次记录加起来」指的是两件事", 26, ACCD, weight="700"))

    # A 拼神经元
    s.append(box(50, 106, 400, 330, "#F7F9FC", CARD_L, 14, 1.5))
    s.append(T(250, 146, "一 · 拼神经元", 28, ACCD, weight="700"))
    s.append(T(250, 178, "伪群体 pseudo-population", 21, GRAY))
    for i, (lbl, col) in enumerate([("session 1  神经元 A B", ACC), ("session 2  神经元 C D", GRN)]):
        s.append(box(80, 206 + i * 56, 340, 44, "#FFFFFF", col, 8, 1.2))
        s.append(T(250, 234 + i * 56, lbl, 22, BODY))
    s.append(line(250, 322, 250, 348, GRAY, 2, None, "ahg"))
    s.append(box(80, 356, 340, 52, TINT, ACC, 8, 1.2))
    s.append(T(250, 388, "并成一个群体  A B C D  再分析", 22, ACCD, weight="700"))

    # B 拼结果
    s.append(box(510, 106, 400, 330, "#F7F9FC", CARD_L, 14, 1.5))
    s.append(T(710, 146, "二 · 拼结果", 28, ACCD, weight="700"))
    s.append(T(710, 178, "各自算完,把数字加总", 21, GRAY))
    for i, (lbl, col) in enumerate([("session 1  算出结果 →  12", ACC), ("session 2  算出结果 →  9", GRN)]):
        s.append(box(540, 206 + i * 56, 340, 44, "#FFFFFF", col, 8, 1.2))
        s.append(T(710, 234 + i * 56, lbl, 22, BODY))
    s.append(line(710, 322, 710, 348, GRAY, 2, None, "ahg"))
    s.append(box(540, 356, 340, 52, TINT, ACC, 8, 1.2))
    s.append(T(710, 388, "两组结果互不重叠,直接相加 = 21", 22, ACCD, weight="700"))

    s.append(box(50, 456, 860, 62, AMBT, AMBL, 14, 1.5))
    s.append(T(480, 494, "共同点:两者都无法恢复跨次的配对信息", 26, AMB, weight="700"))
    return 960, 540, "".join(s)


# ---------------------------------------------------------------- 表格绘制工具
def _table(x, y, cells, cw=150, ch=88, hi=None, fill="#FFFFFF"):
    """cells = [[a,b],[c,d]]; hi = set of (r,c) to tint."""
    s = []
    hi = hi or set()
    s.append(T(x + cw, y - 22, "v = 0", 24, BODY))
    s.append(T(x + cw * 2, y - 22, "v = 1", 24, BODY))
    for r in range(2):
        s.append(T(x + cw * 0.22, y + ch * r + ch * 0.62, f"u = {r}", 24, BODY))
        for c in range(2):
            f = TINT if (r, c) in hi else fill
            s.append(box(x + cw * (c + 1) - cw * 0.5, y + ch * r, cw, ch, f, "#B9C4D2", 6, 1.4))
            s.append(T(x + cw * (c + 1), y + ch * r + ch * 0.63, str(cells[r][c]), 34, INK, weight="700"))
    return "".join(s)


# ---------------------------------------------------------------- 卡7 联合表
def fig_joint():
    s = []
    s.append(box(30, 24, 900, 56, TINT, ACC, 12, 1.5))
    s.append(T(480, 60, "同时记录两个神经元,拿到的是配对记录", 26, ACCD, weight="700"))
    s.append(T(480, 116, "同一条件 1000 试次,每次记下 (u, v) 这一对取值", 24, BODY))
    s.append(T(480, 150, "0 = 该窗口内没发放     1 = 发放了", 21, GRAY))

    s.append(T(480, 208, "联合分布", 26, ACCD, weight="700"))
    s.append(_table(255, 278, [[400, 100], [100, 400]], hi={(0, 0), (1, 1)}))

    s.append(box(120, 476, 720, 74, GRNT, GRN, 14, 1.5))
    s.append(T(480, 510, "对角线 400 / 400 远大于非对角 100 / 100", 24, GRN, weight="700"))
    s.append(T(480, 538, "这两个神经元倾向于一起发放、也一起沉默", 23, BODY))
    s.append(T(480, 580, "本图数字为便于说明而构造的算例", 19, GRAY))
    return 960, 604, "".join(s)


# ---------------------------------------------------------------- 卡8 边缘
def fig_marginal():
    s = []
    s.append(box(30, 24, 900, 56, TINT, ACC, 12, 1.5))
    s.append(T(480, 60, "分次记录只给出表格边上的两条和", 26, ACCD, weight="700"))

    x, y, cw, ch = 225, 190, 150, 88
    # inner cells greyed to show "unknown"
    for r in range(2):
        for c in range(2):
            s.append(box(x + cw * (c + 1) - cw * 0.5, y + ch * r, cw, ch, "#F3F4F6", "#C8CDD4", 6, 1.4))
            s.append(T(x + cw * (c + 1), y + ch * r + ch * 0.63, "?", 34, GRAY, weight="700"))
    s.append(T(x + cw, y - 26, "v = 0", 23, BODY))
    s.append(T(x + cw * 2, y - 26, "v = 1", 23, BODY))
    s.append(T(x + cw * 0.5, y + ch * 0.62, "u = 0", 23, BODY))
    s.append(T(x + cw * 0.5, y + ch * 1.62, "u = 1", 23, BODY))

    # row sums
    s.append(T(x + cw * 3.0, y - 26, "行和", 23, ACCD, weight="700"))
    for r in range(2):
        s.append(box(x + cw * 2.5, y + ch * r, cw, ch, TINT, ACC, 6, 1.6))
        s.append(T(x + cw * 3.0, y + ch * r + ch * 0.63, "500", 32, ACCD, weight="700"))
    # col sums
    s.append(T(x + cw * 0.22, y + ch * 2 + 54, "列和", 23, ACCD, weight="700"))
    for c in range(2):
        s.append(box(x + cw * (c + 1) - cw * 0.5, y + ch * 2 + 12, cw, ch, TINT, ACC, 6, 1.6))
        s.append(T(x + cw * (c + 1), y + ch * 2 + 12 + ch * 0.63, "500", 32, ACCD, weight="700"))

    s.append(box(120, 470, 720, 100, AMBT, AMBL, 14, 1.5))
    s.append(T(480, 504, "你知道 u 有一半试次发放、v 有一半试次发放", 24, AMB))
    s.append(T(480, 538, "不知道它们是不是同一半试次", 26, AMB, weight="700"))
    s.append(T(480, 596, "边缘化 = 把另一个变量的所有取值加总掉,不再区分", 21, GRAY))
    return 960, 630, "".join(s)


# ---------------------------------------------------------------- 卡9 三张表
def fig_three():
    s = []
    s.append(box(30, 24, 900, 56, TINT, ACC, 12, 1.5))
    s.append(T(480, 60, "三张表的边缘完全相同,内部截然不同", 26, ACCD, weight="700"))

    data = [
        ([[400, 100], [100, 400]], "一起发放、一起沉默", "共同驱动", "+0.6", GRN, GRNT),
        ([[100, 400], [400, 100]], "一个发放另一个沉默", "相互抑制", "−0.6", RED, REDT),
        ([[250, 250], [250, 250]], "彼此毫无关系", "相互独立", "0", GRAY, "#F3F4F6"),
    ]
    cw, ch = 108, 66
    for i, (cells, desc, mech, rho, col, tint) in enumerate(data):
        bx = 40 + i * 300
        s.append(box(bx, 106, 280, 380, "#FFFFFF", col, 14, 1.6))
        for r in range(2):
            for c in range(2):
                s.append(box(bx + 30 + c * cw, 150 + r * ch, cw - 8, ch - 8, tint, col, 6, 1.2))
                s.append(T(bx + 30 + c * cw + (cw - 8) / 2, 150 + r * ch + 40,
                           str(cells[r][c]), 26, INK, weight="700"))
        s.append(line(bx + 26, 292, bx + 254, 292, col, 1.2, "5,4"))
        s.append(T(bx + 140, 326, desc, 21, BODY))
        s.append(T(bx + 140, 360, mech, 26, col, weight="700"))
        s.append(box(bx + 70, 384, 140, 54, tint, col, 8, 1.2))
        s.append(T(bx + 140, 420, "ρ = " + rho, 26, col, weight="700"))
        s.append(T(bx + 140, 466, "行和列和均为 500", 20, GRAY))

    s.append(box(60, 508, 840, 62, AMBT, AMBL, 14, 1.5))
    s.append(T(480, 546, "分次记录得到的观测,在这三种情况下完全一样", 26, AMB, weight="700"))
    return 960, 592, "".join(s)


# ---------------------------------------------------------------- 卡10 a 扫 rho
def fig_sweep():
    s = []
    s.append(box(30, 24, 900, 56, TINT, ACC, 12, 1.5))
    s.append(T(480, 60, "边缘固定后只剩一个自由参数 a", 26, ACCD, weight="700"))

    # parameterised table
    cw, ch = 150, 74
    x, y = 150, 130
    cells = [["a", "500 − a"], ["500 − a", "a"]]
    for r in range(2):
        for c in range(2):
            f = TINT if r == c else "#FFFFFF"
            s.append(box(x + c * cw, y + r * ch, cw - 6, ch - 6, f, "#B9C4D2", 6, 1.4))
            s.append(T(x + c * cw + (cw - 6) / 2, y + r * ch + 46, cells[r][c], 26, INK, weight="700"))
    s.append(T(x + cw, y - 16, "行和、列和均固定为 500", 21, GRAY))

    s.append(box(500, 132, 400, 116, "#F7F9FC", CARD_L, 12, 1.5))
    s.append(T(700, 176, "ρ  =  a / 250  −  1", 34, ACCD, weight="700"))
    s.append(T(700, 218, "u、v 的均值与标准差都是 0.5", 21, GRAY))

    # axis
    ax_y = 340
    s.append(line(120, ax_y, 840, ax_y, INK, 2))
    for i, (a, rho) in enumerate([(0, "−1"), (125, "−0.5"), (250, "0"), (375, "+0.5"), (500, "+1")]):
        px = 120 + i * 180
        s.append(line(px, ax_y - 9, px, ax_y + 9, INK, 2))
        s.append(T(px, ax_y - 24, f"a = {a}", 22, BODY))
        s.append(T(px, ax_y + 46, "ρ = " + rho, 25, ACCD, weight="700"))
    s.append(T(480, ax_y + 92, "a 扫过 0 到 500,ρ 扫满 −1 到 +1", 26, INK, weight="700"))

    s.append(box(90, 470, 780, 68, AMBT, AMBL, 14, 1.5))
    s.append(T(480, 502, "在这个算例里,边缘分布对 ρ 的约束等于零", 25, AMB, weight="700"))
    s.append(T(480, 528, "一般情形下边缘给出的是一个可行区间,不会收缩成一个点", 21, AMB))
    return 960, 562, "".join(s)


# ---------------------------------------------------------------- 卡11 两类问题
def fig_identify():
    s = []
    s.append(box(30, 24, 900, 56, TINT, ACC, 12, 1.5))
    s.append(T(480, 60, "判据:有无限多试次,这个不确定会消失吗", 26, ACCD, weight="700"))

    s.append(line(480, 90, 480, 128, GRAY, 2))
    s.append(line(230, 128, 730, 128, GRAY, 2))
    s.append(line(230, 128, 230, 160, GRAY, 2, None, "ahg"))
    s.append(line(730, 128, 730, 160, GRAY, 2, None, "ahg"))

    # left: estimation
    s.append(box(60, 166, 340, 268, GRNT, GRN, 14, 1.6))
    s.append(T(230, 206, "会消失", 30, GRN, weight="700"))
    s.append(T(230, 244, "估计问题", 27, INK, weight="700"))
    s.append(line(90, 268, 370, 268, GRN, 1.2, "5,4"))
    for i, t in enumerate(["真相唯一", "只是被有限样本与噪声掩盖",
                           "更多数据有用", "更好的模型有用"]):
        s.append(T(230, 300 + i * 34, t, 22, BODY))

    # right: identifiability
    s.append(box(560, 166, 340, 268, REDT, RED, 14, 1.6))
    s.append(T(730, 206, "不会消失", 30, RED, weight="700"))
    s.append(T(730, 244, "可辨识性问题", 27, INK, weight="700"))
    s.append(line(590, 268, 870, 268, RED, 1.2, "5,4"))
    for i, t in enumerate(["两个不同的真相", "产生完全相同的观测",
                           "再多数据也分不出", "换任何模型都一样"]):
        s.append(T(730, 300 + i * 34, t, 22, BODY))

    s.append(box(60, 456, 840, 74, AMBT, AMBL, 14, 1.5))
    s.append(T(480, 490, "三张表落在右边:一亿个试次与一千个试次", 24, AMB))
    s.append(T(480, 520, "在区分它们这件事上能力相同,都是零", 26, AMB, weight="700"))
    return 960, 554, "".join(s)


# ---------------------------------------------------------------- 卡12 后验=先验
def fig_bayes():
    s = []
    s.append(box(30, 24, 900, 56, TINT, ACC, 12, 1.5))
    s.append(T(480, 60, "在不可辨识的方向上,数据没有更新任何东西", 26, ACCD, weight="700"))

    s.append(box(150, 106, 660, 76, "#F7F9FC", CARD_L, 12, 1.5))
    s.append(T(480, 156, "后验    正比于    先验  ×  似然", 32, ACCD, weight="700"))

    # likelihood flat plot
    s.append(box(80, 206, 380, 250, "#FFFFFF", "#B9C4D2", 12, 1.4))
    s.append(T(270, 240, "似然沿 a 是常数", 24, INK, weight="700"))
    s.append(line(120, 400, 420, 400, INK, 2))
    s.append(line(120, 400, 120, 268, INK, 2))
    s.append(line(130, 320, 410, 320, RED, 3))
    s.append(T(270, 300, "a 取任何值,数据同样可能", 20, RED))
    s.append(T(270, 428, "a  从 0 到 500", 21, BODY))

    # posterior = prior
    s.append(box(500, 206, 380, 250, "#FFFFFF", "#B9C4D2", 12, 1.4))
    s.append(T(690, 240, "于是", 22, GRAY))
    s.append(T(690, 296, "后验  =  先验", 36, ACCD, weight="700"))
    s.append(line(540, 330, 840, 330, LINE, 1.5, "5,4"))
    s.append(T(690, 368, "模型输出的那个数", 22, BODY))
    s.append(T(690, 402, "完全来自它的先验", 24, RED, weight="700"))
    s.append(T(690, 436, "这叫插补,属于推断", 22, BODY))

    s.append(box(80, 480, 800, 62, AMBT, AMBL, 14, 1.5))
    s.append(T(480, 518, "模型不创造信息,模型引入假设", 28, AMB, weight="700"))
    return 960, 566, "".join(s)


# ---------------------------------------------------------------- 卡14 清单
def fig_checklist():
    s = []
    s.append(box(30, 24, 900, 56, TINT, ACC, 12, 1.5))
    s.append(T(480, 60, "按判据,常见分析分成两类", 26, ACCD, weight="700"))

    s.append(box(50, 106, 410, 356, GRNT, GRN, 14, 1.6))
    s.append(T(255, 148, "可以跨 session 拼", 28, GRN, weight="700"))
    s.append(T(255, 180, "在等价类上恒定 · 都是边缘的函数", 20, BODY))
    s.append(line(80, 200, 430, 200, GRN, 1.2, "5,4"))
    for i, t in enumerate(["单神经元调谐曲线", "条件平均发放",
                           "试次平均的群体几何", "试次平均的解码"]):
        s.append(circ(100, 236 + i * 46, 7, GRN, GRN, 1))
        s.append(T(122, 244 + i * 46, t, 24, INK, anchor="start"))

    s.append(box(500, 106, 410, 356, REDT, RED, 14, 1.6))
    s.append(T(705, 148, "不能跨 session 拼", 28, RED, weight="700"))
    s.append(T(705, 180, "随自由度变化 · 依赖联合表内部", 20, BODY))
    s.append(line(530, 200, 880, 200, RED, 1.2, "5,4"))
    for i, t in enumerate(["噪声相关", "Granger 因果",
                           "跨区共享的潜在变异", "communication subspace"]):
        s.append(circ(550, 236 + i * 46, 7, RED, RED, 1))
        s.append(T(572, 244 + i * 46, t, 24, INK, anchor="start"))

    s.append(box(50, 482, 860, 66, AMBT, AMBL, 14, 1.5))
    s.append(T(480, 522, "动手前问一句:我要的这个量,会不会随那个未知的自由度变化", 25, AMB, weight="700"))
    return 960, 572, "".join(s)


# ---------------------------------------------------------------- 卡15 stitching
def fig_stitch():
    s = []
    s.append(box(30, 24, 900, 56, TINT, ACC, 12, 1.5))
    s.append(T(480, 60, "假设不改变观测,它缩小的是候选集合", 26, ACCD, weight="700"))

    # before
    s.append(box(70, 110, 340, 230, "#FFFFFF", "#B9C4D2", 14, 1.4))
    s.append(T(240, 148, "只有观测", 25, INK, weight="700"))
    s.append(line(110, 258, 370, 258, INK, 2))
    s.append(line(110, 258, 110, 186, INK, 2))
    s.append(line(118, 210, 362, 210, RED, 14))
    s.append(T(240, 292, "整条线都与数据相容", 22, RED))
    s.append(T(240, 320, "a  从 0 到 500", 20, BODY))

    s.append(line(430, 224, 500, 224, GRAY, 2.5, None, "ahg"))
    s.append(T(465, 206, "加假设", 20, GRAY))
    s.append(T(465, 254, "加锚点", 20, GRAY))

    # after
    s.append(box(530, 110, 340, 230, "#FFFFFF", "#B9C4D2", 14, 1.4))
    s.append(T(700, 148, "观测 + 结构假设", 25, INK, weight="700"))
    s.append(line(570, 258, 830, 258, INK, 2))
    s.append(line(570, 258, 570, 186, INK, 2))
    s.append(circ(700, 210, 10, GRN, GRN, 1))
    s.append(T(700, 292, "候选被缩到很小的范围", 22, GRN))
    s.append(T(700, 320, "结论随假设成立与否而定", 20, BODY))

    # buy / not buy
    s.append(box(50, 366, 410, 140, GRNT, GRN, 14, 1.5))
    s.append(T(255, 402, "买到", 25, GRN, weight="700"))
    s.append(T(255, 440, "跨 session 的迁移与解码增益", 22, BODY))
    s.append(T(255, 474, "可在留出数据上验证", 22, BODY))

    s.append(box(500, 366, 410, 140, REDT, RED, 14, 1.5))
    s.append(T(705, 402, "买不到", 25, RED, weight="700"))
    s.append(T(705, 440, "从未同时记录的那一对", 22, BODY))
    s.append(T(705, 474, "之间的协同波动", 22, BODY))

    s.append(T(480, 542, "LFADS  →  NDT-2  →  POYO  →  MtM  →  POYO+", 24, ACCD, weight="700"))
    return 960, 566, "".join(s)


FIGS = {
    "toc": toc,
    "fig-dilemma": fig_dilemma,
    "fig-two-joins": fig_two_joins,
    "fig-joint": fig_joint,
    "fig-marginal": fig_marginal,
    "fig-three": fig_three,
    "fig-sweep": fig_sweep,
    "fig-identify": fig_identify,
    "fig-bayes": fig_bayes,
    "fig-checklist": fig_checklist,
    "fig-stitch": fig_stitch,
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
