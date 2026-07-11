"""Methodology piece — 群体 spike 解码 · 生成式脊柱 first-principles schematics.
Self-made SVG diagrams (series track), rendered to PNG via playwright chromium.
"""
import os, subprocess, tempfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))      # .claude/skills/dailybci
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "series-spike-population-decoding", "figs")
os.makedirs(OUT, exist_ok=True)

ACC = "#2F6DB5"; ACCD = "#1E4E86"; TINT = "#E9F0F8"
INK = "#1A1A1A"; BODY = "#4A4A4A"; GRAY = "#8A8A8A"; LINE = "#D6DBE2"
CARDF = "#F7F9FC"; CARDL = "#DCE5F0"; CHIPF = "#F2F3F1"; CHIPL = "#DBDCD8"

DEFS = (
    '<defs><marker id="ah" markerWidth="10" markerHeight="10" refX="8" refY="3" '
    'orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="%s"/></marker>'
    '<marker id="ahg" markerWidth="10" markerHeight="10" refX="8" refY="3" '
    'orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="%s"/></marker>'
    '<marker id="ahd" markerWidth="10" markerHeight="10" refX="8" refY="3" '
    'orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="%s"/></marker></defs>'
    % (ACC, GRAY, ACCD)
)

def T(x, y, s, size=25, fill=INK, anchor="middle", weight="400"):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}">{s}</text>'

def box(x, y, w, h, fill, stroke, rx=12, sw=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

def arrow(x1, y1, x2, y2, col=ACC, mk="ah", sw=2.5):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{sw}" marker-end="url(#{mk})"/>'

# ---------- Fig 01: spike trains -> binning -> rate vector ----------
def fig01():
    s = []
    s.append(T(480, 42, "原料:动作电位序列 → 分箱 → 发放率向量", 28, INK, weight="700"))
    rows = [116, 174, 232]
    names = ["神经元 1", "神经元 2", "神经元 3"]
    ticks = [[120,150,168,210,250,300,330,366,392,410,470,520],
             [135,175,230,270,315,388,430,470,520],
             [115,160,200,240,290,340,372,404,460,500,530]]
    # window highlight (behind ticks)
    s.append(box(353, 92, 66, 178, TINT, ACC, 8, 1.2))
    for i, y in enumerate(rows):
        s.append(T(98, y+7, names[i], 20, BODY, anchor="end"))
        s.append(f'<line x1="112" y1="{y}" x2="548" y2="{y}" stroke="{LINE}" stroke-width="1.5"/>')
        for tx in ticks[i]:
            s.append(f'<line x1="{tx}" y1="{y-15}" x2="{tx}" y2="{y+15}" stroke="{ACCD}" stroke-width="2.4"/>')
    # N hint
    for k, yy in enumerate([262, 270, 278]):
        s.append(f'<circle cx="74" cy="{yy}" r="2.2" fill="{GRAY}"/>')
    s.append(T(386, 292, "Δt 时间窗", 20, ACCD))
    # arrow window -> vector
    s.append(arrow(424, 175, 596, 175))
    s.append(T(510, 156, "分箱计数", 20, ACC))
    # vector box
    s.append(box(606, 104, 168, 150, CARDF, CARDL, 14, 1.5))
    s.append(T(690, 136, "发放率向量 r", 21, ACCD, weight="700"))
    vals = ["r1 = 3", "r2 = 1", "r3 = 2"]
    for j, v in enumerate(vals):
        s.append(T(690, 172+j*24, v, 21, BODY))
    for k, xx in enumerate([684, 690, 696]):
        s.append(f'<circle cx="{xx}" cy="244" r="2.2" fill="{GRAY}"/>')
    # vector -> intent
    s.append(arrow(778, 178, 838, 178))
    s.append(T(808, 160, "解码", 19, ACC))
    s.append(T(885, 185, "意图 z", 23, INK))
    # bottom strip
    s.append(box(40, 306, 880, 58, TINT, ACC, 14, 1.5))
    s.append(T(480, 342, "r(t) 是群体解码唯一的原料 · 解码 = 找一个映射 r → z", 25, ACCD, weight="700"))
    return 960, 380, "".join(s)

# ---------- Fig 03: the four-rung spine ----------
def fig03():
    s = []
    s.append(T(480, 42, "脊柱四级:每一级松开上一级的一条简化假设", 28, INK, weight="700"))
    rungs = [("贝叶斯", "+ 先验 · 不确定度"),
             ("ML", "+ 完整噪声(Poisson)"),
             ("OLE", "+ 相关结构(Q⁻¹)"),
             ("群体矢量", "只用偏好方向")]
    x = 188; w = 612; h = 64
    tops = [78, 156, 234, 312]
    for i, (nm, add) in enumerate(rungs):
        y = tops[i]
        fill = TINT if i == 0 else CARDF
        stroke = ACC if i == 0 else CARDL
        s.append(box(x, y, w, h, fill, stroke, 14, 1.5))
        s.append(T(x+34, y+h/2+8, nm, 27, ACCD, anchor="start", weight="700"))
        addcol = ACCD if i == 0 else ACC
        s.append(T(x+w-30, y+h/2+8, add, 24, addcol, anchor="end"))
    # up arrow on the left
    s.append(arrow(132, 372, 132, 70, ACCD, "ahd", 3))
    s.append(T(150, 220, "越", 20, ACCD, anchor="start"))
    s.append(T(150, 246, "往", 20, ACCD, anchor="start"))
    s.append(T(150, 272, "上", 20, ACCD, anchor="start"))
    # bottom strip
    s.append(box(40, 398, 880, 58, TINT, ACC, 14, 1.5))
    s.append(T(480, 434, "一条主线:把编码模型用得越来越足", 25, ACCD, weight="700"))
    return 960, 472, "".join(s)

# ---------- Fig 04: population vector — vote preferred directions, sum ----------
def fig04():
    s = []
    s.append(T(480, 42, "群体矢量:朝偏好方向投票 × 发放率,矢量求和", 28, INK, weight="700"))
    cx, cy = 300, 250
    s.append(f'<circle cx="{cx}" cy="{cy}" r="150" fill="none" stroke="{LINE}" stroke-width="1.5"/>')
    comps = [(372,216),(318,182),(260,164),(248,231),(322,289)]
    for (px, py) in comps:
        s.append(arrow(cx, cy, px, py, GRAY, "ahg", 2))
    # resultant
    s.append(arrow(cx, cy, 321, 83, ACCD, "ahd", 4))
    s.append(T(360, 78, "合矢量 = 解码方向", 22, ACCD, anchor="start", weight="700"))
    s.append(f'<circle cx="{cx}" cy="{cy}" r="5" fill="{INK}"/>')
    # right text
    tx = 540
    s.append(T(tx, 168, "每个神经元朝自己的偏好方向投一票,", 24, BODY, anchor="start"))
    s.append(T(tx, 206, "票的长度 = 当前发放率;", 24, BODY, anchor="start"))
    s.append(T(tx, 244, "全部相加 → 合矢量指向解码方向。", 24, BODY, anchor="start"))
    # bottom strip
    s.append(box(40, 372, 880, 64, CHIPF, CHIPL, 14, 1.5))
    s.append(T(480, 402, "暗含假设:均匀铺开 · 互不相关 · 同样可靠(Q∝I)", 24, INK, weight="700"))
    s.append(T(480, 430, "真实数据三条都破 —— 于是需要把权重选对", 23, BODY))
    return 960, 452, "".join(s)

# ---------- Fig 05: OLE — Q^-1 down-weights redundant neurons ----------
def fig05():
    s = []
    s.append(T(480, 42, "OLE:Q⁻¹ 给冗余 / 相关的神经元降权", 28, INK, weight="700"))
    def panel(x0, title, heights, group_label):
        r = [box(x0, 74, 410, 250, "#FCFCFB", CHIPL, 14, 1.2)]
        r.append(T(x0+205, 110, title, 25, ACCD, weight="700"))
        base = 300
        bx = [x0+70, x0+125, x0+180, x0+275, x0+335]
        for i, hx in enumerate(heights):
            col = "#C4D4E8" if i < 3 else ACC
            r.append(f'<rect x="{bx[i]-18}" y="{base-hx}" width="36" height="{hx}" rx="6" fill="{col}"/>')
        # bracket over first three (correlated group)
        gx0 = bx[0]-22; gx1 = bx[2]+22; gy = 150
        r.append(f'<path d="M{gx0},{gy+12} L{gx0},{gy} L{gx1},{gy} L{gx1},{gy+12}" fill="none" stroke="{GRAY}" stroke-width="1.6"/>')
        r.append(T((gx0+gx1)/2, gy-8, group_label, 19, GRAY))
        r.append(T(bx[3]+18, 316, "独立神经元", 18, BODY))
        return "".join(r)
    s.append(panel(40, "群体矢量:相关的被重复计数", [110,110,110,110,110], "相关 → 被多算"))
    s.append(panel(510, "OLE:w = Q⁻¹L", [55,55,55,110,110], "降权 · 不重复"))
    # bottom strip
    s.append(box(40, 340, 880, 64, TINT, ACC, 14, 1.5))
    s.append(T(480, 370, "L = 调谐(信号) · Q⁻¹ = 相关矩阵的逆,把冗余信息摊掉", 24, ACCD, weight="700"))
    s.append(T(480, 398, "但只用到均值与相关(二阶统计),没用噪声的真实形状", 23, ACCD))
    return 960, 420, "".join(s)

# ---------- Fig 06: ML — info on the steep flank; likelihood peak ----------
def fig06():
    s = []
    s.append(T(480, 42, "ML:信息在调谐曲线的陡坡,挑最可能的意图", 28, INK, weight="700"))
    # left panel: tuning curve
    s.append(box(40, 74, 410, 252, "#FCFCFB", CHIPL, 14, 1.2))
    s.append(T(245, 108, "调谐曲线:陡坡信息多", 24, ACCD, weight="700"))
    s.append(f'<line x1="100" y1="300" x2="430" y2="300" stroke="{GRAY}" stroke-width="2" marker-end="url(#ahg)"/>')
    s.append(f'<line x1="100" y1="300" x2="100" y2="150" stroke="{GRAY}" stroke-width="2" marker-end="url(#ahg)"/>')
    s.append(T(112, 162, "放电率", 18, GRAY, anchor="start"))
    s.append(T(420, 322, "刺激", 18, GRAY, anchor="end"))
    s.append(f'<path d="M120,296 C190,296 215,168 268,168 C321,168 350,296 420,296" fill="none" stroke="{ACCD}" stroke-width="3"/>')
    # peak marker (flat)
    s.append(f'<line x1="244" y1="168" x2="292" y2="168" stroke="{GRAY}" stroke-width="2.2"/>')
    s.append(T(300, 150, "峰顶 平 · 信息少", 18, GRAY, anchor="start"))
    # flank marker (steep)
    s.append(f'<circle cx="206" cy="214" r="5" fill="{ACC}"/>')
    s.append(f'<line x1="186" y1="252" x2="226" y2="176" stroke="{ACC}" stroke-width="2.2"/>')
    s.append(T(150, 196, "斜率大", 18, ACCD, anchor="start"))
    s.append(T(150, 220, "信息多", 18, ACCD, anchor="start"))
    # right panel: likelihood
    s.append(box(510, 74, 410, 252, "#FCFCFB", CHIPL, 14, 1.2))
    s.append(T(715, 108, "似然 p(r|s)", 24, ACCD, weight="700"))
    s.append(f'<line x1="560" y1="300" x2="900" y2="300" stroke="{GRAY}" stroke-width="2" marker-end="url(#ahg)"/>')
    s.append(T(890, 322, "s(意图)", 18, GRAY, anchor="end"))
    s.append(f'<path d="M566,296 C660,292 695,160 732,160 C769,160 804,292 898,296" fill="none" stroke="{ACCD}" stroke-width="3"/>')
    s.append(f'<line x1="732" y1="296" x2="732" y2="160" stroke="{ACC}" stroke-width="1.6" stroke-dasharray="5,5"/>')
    s.append(T(732, 146, "最可能的 s", 19, ACC))
    s.append(T(715, 296, "挑让实测放电最可能的 s", 19, BODY))
    # bottom strip
    s.append(box(40, 342, 880, 64, TINT, ACC, 14, 1.5))
    s.append(T(480, 372, "用完整 p(r|s)(Poisson)· 对放电天然非线性", 24, ACCD, weight="700"))
    s.append(T(480, 400, "数据够多时渐近逼近信息天花板(Cramér–Rao)", 23, ACCD))
    return 960, 422, "".join(s)

# ---------- Fig 07: Bayesian — posterior = likelihood x prior ----------
def fig07():
    s = []
    s.append(T(480, 42, "贝叶斯:后验 = 似然 × 先验", 28, INK, weight="700"))
    def mini(x0, w, title, path, peak=None, tcol=ACCD):
        r = [box(x0, 78, w, 218, "#FCFCFB", CHIPL, 14, 1.2)]
        r.append(T(x0+w/2, 112, title, 23, tcol, weight="700"))
        r.append(f'<line x1="{x0+30}" y1="266" x2="{x0+w-26}" y2="266" stroke="{GRAY}" stroke-width="1.8"/>')
        r.append(f'<path d="{path}" fill="none" stroke="{ACCD}" stroke-width="3"/>')
        if peak is not None:
            r.append(f'<line x1="{peak}" y1="266" x2="{peak}" y2="150" stroke="{ACC}" stroke-width="1.6" stroke-dasharray="5,5"/>')
        return "".join(r)
    s.append(mini(40, 250, "似然 p(r|s)",
                  "M70,262 C120,262 135,150 165,150 C195,150 210,262 260,262"))
    s.append(T(305, 196, "×", 40, GRAY))
    s.append(mini(340, 250, "先验 p(s)",
                  "M366,260 C420,206 500,206 562,260"))
    s.append(T(600, 196, "=", 40, GRAY))
    s.append(mini(640, 280, "后验 p(s|r)",
                  "M668,262 C726,262 748,150 778,150 C808,150 830,262 890,262", peak=778))
    s.append(T(778, 138, "峰 = MAP", 18, ACC))
    # bottom strip
    s.append(box(40, 312, 880, 64, TINT, ACC, 14, 1.5))
    s.append(T(480, 342, "取峰值 = MAP;保留整条后验 = 完整贝叶斯", 24, ACCD, weight="700"))
    s.append(T(480, 370, "后验更窄,还附带不确定度 —— 信息用到最尽", 23, ACCD))
    return 960, 392, "".join(s)

FIGS = {"fig01-material": fig01, "fig03-spine": fig03, "fig04-popvector": fig04,
        "fig05-ole": fig05, "fig06-ml": fig06, "fig07-bayes": fig07}

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
