# -*- coding: utf-8 -*-
"""series-grounding-02 · 生物电记录里的零点 —— 自制示意图"""
import os, subprocess, tempfile, math

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "series-grounding-02", "figs")
os.makedirs(OUT, exist_ok=True)

BG   = "#FAFAFA"
ACC  = "#2F6DB5"; ACCD = "#1E4E86"; TINT = "#E9F0F8"
INK  = "#1A1A1A"; BODY = "#4A4A4A"; GRAY = "#8A8A8A"; LINE = "#D6DBE2"
RED  = "#C0392B"; REDT = "#F7E9E7"; GRN = "#2E7D57"; GRNT = "#E7F2EC"
CARD_L = "#DCE5F0"; PANEL = "#F3F5F8"

DEFS = (
    '<defs>'
    f'<marker id="ah" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="{ACC}"/></marker>'
    f'<marker id="ahr" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="{RED}"/></marker>'
    f'<marker id="ahg" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="{GRAY}"/></marker>'
    f'<marker id="ahk" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="{INK}"/></marker>'
    f'<marker id="ahn" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="{GRN}"/></marker>'
    '</defs>'
)

def T(x, y, s, size=26, fill=INK, anchor="middle", weight="400", style=""):
    st = f' font-style="{style}"' if style else ""
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}"{st}>{s}</text>'

def box(x, y, w, h, fill=PANEL, stroke=CARD_L, rx=14, sw=1.6, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'

def line(x1,y1,x2,y2,stroke=INK,sw=2.4,dash=None,marker=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    m = f' marker-end="url(#{marker})"' if marker else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"{d}{m}/>'

def circ(cx, cy, r, fill=TINT, stroke=ACC, sw=2):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

def ell(cx, cy, rx, ry, fill="none", stroke=ACC, sw=2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'

def path(d, stroke=INK, sw=2.4, fill="none", dash=None, marker=None):
    ds = f' stroke-dasharray="{dash}"' if dash else ""
    m = f' marker-end="url(#{marker})"' if marker else ""
    return f'<path d="{d}" stroke="{stroke}" stroke-width="{sw}" fill="{fill}"{ds}{m}/>'

def gnd(x, y, scale=1.0, stroke=INK, sw=3):
    s = scale
    o = [line(x, y, x, y+20*s, stroke, sw)]
    for i, w in enumerate((40, 24, 10)):
        yy = y + 20*s + i*8*s
        o.append(line(x-w*s/2, yy, x+w*s/2, yy, stroke, sw))
    return "".join(o)

def cap_v(x, y, s=1.0, stroke=GRAY):
    """竖向串联的电容（两块横板），(x,y) 中心"""
    return (line(x-26*s, y-7*s, x+26*s, y-7*s, stroke, 4)
          + line(x-26*s, y+7*s, x+26*s, y+7*s, stroke, 4))

def res_v(x, y, h=56, w=22, stroke=INK, fill="#FFFFFF"):
    """竖向电阻（矩形），(x,y) 中心"""
    return f'<rect x="{x-w/2}" y="{y-h/2}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" stroke-width="2.4"/>'

def elec(x, y, w=54, h=16, fill=ACC):
    """电极片"""
    return f'<rect x="{x-w/2}" y="{y-h/2}" width="{w}" height="{h}" rx="5" fill="{fill}"/>'

def wave(x0, y0, w, amp, n=3, stroke=ACC, sw=2.6, phase=0.0, pts=120, noise=0.0):
    d = []
    for i in range(pts+1):
        t = i/pts
        x = x0 + w*t
        y = y0 - amp*math.sin(2*math.pi*n*t + phase)
        if noise:
            y -= noise*math.sin(2*math.pi*n*7.3*t + 1.1)
        d.append(("M" if i == 0 else "L") + f"{x:.1f},{y:.1f}")
    return path(" ".join(d), stroke, sw)

def render(name, w, h, inner, scale=2):
    W2, H2 = w*scale, h*scale
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W2}" height="{H2}" '
           f'viewBox="0 0 {w} {h}" font-family="HeitiSC,Helvetica,Arial,sans-serif">'
           f'{DEFS}<rect width="{w}" height="{h}" fill="{BG}"/>{inner}</svg>')
    html = (f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>'
            f'@font-face{{font-family:"HeitiSC";src:url("file://{FONT}");}}'
            f'*{{margin:0;padding:0}}body{{width:{W2}px;height:{H2}px;background:{BG}}}</style></head>'
            f'<body>{svg}</body></html>')
    tmp = tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8")
    tmp.write(html); tmp.close()
    out = os.path.join(OUT, name + ".png")
    subprocess.run(["npx","playwright","screenshot",f"file://{tmp.name}",out,
                    f"--viewport-size={W2},{H2}","--wait-for-timeout=500"],
                   check=True, capture_output=True, text=True)
    os.unlink(tmp.name)
    return out

# ============================================================ 图 1 体积导体
def fig1():
    W, H = 960, 540
    s = [T(W/2, 48, "电流在组织里流动，组织里就出现电位分布", 30, INK, weight="700")]
    cx, cy = 360, 296
    for i, (rx, ry) in enumerate(((246,134),(188,102),(128,70))):
        s.append(ell(cx, cy, rx, ry, "none", ACC, 1.8, "7 7"))
    s.append(T(cx-246, cy-152, "等位线", 22, GRAY, anchor="middle"))
    # 细胞
    s.append(ell(cx, cy, 74, 40, TINT, ACCD, 2.6))
    s.append(T(cx, cy+9, "细胞", 25, ACCD, weight="700"))
    # 电流流出 / 流回
    s.append(path(f"M{cx-56},{cy-28} C {cx-140},{cy-104} {cx+114},{cy-130} {cx+60},{cy-30}", RED, 3, marker="ahr"))
    s.append(T(cx+4, cy-118, "胞外电流", 24, RED, weight="700"))
    # 电极
    ex = 760
    s.append(line(ex, 120, ex, 300, GRAY, 8))
    s.append(f'<circle cx="{ex}" cy="308" r="11" fill="{INK}"/>')
    s.append(T(ex+16, 150, "电极", 25, INK, anchor="start", weight="700"))
    s.append(T(ex+16, 184, "读到的是这一点", 22, BODY, anchor="start"))
    s.append(T(ex+16, 212, "所在的电位", 22, BODY, anchor="start"))
    s.append(box(60, 452, 840, 62, PANEL, CARD_L))
    s.append(T(W/2, 490, "细胞外液不是理想导体，电流流过它就产生电位差（U = I · R）", 26, INK))
    return W, H, "".join(s)

# ============================================================ 图 2 必然两点
def fig2():
    W, H = 960, 480
    s = [T(W/2, 48, "一根电极读不出数，两根才有读数", 30, INK, weight="700")]
    # 左
    s.append(box(50, 90, 390, 330, "#FFFFFF", CARD_L))
    s.append(T(245, 132, "只有一根", 26, GRAY, weight="700"))
    s.append(elec(245, 200))
    s.append(line(245, 208, 245, 268, GRAY, 3))
    s.append(T(245, 320, "?", 72, RED, weight="700"))
    s.append(T(245, 372, "读数无定义", 26, RED, weight="700"))
    # 右
    s.append(box(520, 90, 390, 330, "#FFFFFF", CARD_L))
    s.append(T(715, 132, "两根", 26, ACCD, weight="700"))
    s.append(elec(630, 200)); s.append(elec(800, 200, fill=GRN))
    s.append(T(630, 178, "i", 24, ACCD, weight="700"))
    s.append(T(800, 178, "ref", 24, GRN, weight="700"))
    s.append(line(630, 208, 630, 268, ACC, 3)); s.append(line(800, 208, 800, 268, GRN, 3))
    s.append(box(590, 268, 250, 62, TINT, ACC))
    s.append(T(715, 308, "V i  −  V ref", 30, ACCD, weight="700"))
    s.append(T(715, 372, "这才是一个物理量", 26, ACCD, weight="700"))
    s.append(T(W/2, 452, "电位是省略句，只有两点之间的差与零点无关", 25, BODY))
    return W, H, "".join(s)

# ============================================================ 图 3 参考电极自己也在动
def fig3():
    W, H = 960, 540
    s = [T(W/2, 48, "参考电极泡在同一片电位场里，它自己也在动", 30, INK, weight="700")]
    # 头
    hx, hy = 250, 230
    s.append(f'<path d="M{hx-120},{hy+70} A 120,120 0 0 1 {hx+120},{hy+70} Z" fill="{PANEL}" stroke="{CARD_L}" stroke-width="2"/>')
    s.append(line(hx-120, hy+70, hx+120, hy+70, CARD_L, 2))
    s.append(elec(hx-58, hy-52, 48, 14))
    s.append(elec(hx+70, hy+62, 48, 14, GRN))
    s.append(T(hx-58, hy-72, "i", 24, ACCD, weight="700"))
    s.append(T(hx+70, hy+94, "ref", 24, GRN, weight="700"))
    # 波形
    s.append(box(430, 108, 470, 130, "#FFFFFF", CARD_L))
    s.append(T(452, 140, "V i (t)", 24, ACCD, anchor="start", weight="700"))
    s.append(wave(470, 190, 400, 30, 3.2, ACC, 2.6, 0.3, noise=6))
    s.append(box(430, 262, 470, 130, "#FFFFFF", CARD_L))
    s.append(T(452, 294, "V ref (t)", 24, GRN, anchor="start", weight="700"))
    s.append(wave(470, 344, 400, 22, 2.1, GRN, 2.6, 1.4, noise=4))
    s.append(box(60, 424, 840, 84, REDT, RED))
    s.append(T(W/2, 460, "身体上没有电位为零的地方", 27, RED, weight="700"))
    s.append(T(W/2, 492, "V ref 不是 0，也不是常数，是一条完整的时间序列", 25, INK))
    return W, H, "".join(s)

# ============================================================ 图 4 一条信号进了所有通道
def fig4():
    W, H = 960, 540
    s = [T(W/2, 48, "同一条 V ref 被减进每一个通道", 30, INK, weight="700")]
    ys = [130, 250, 370]
    for i, y in enumerate(ys):
        s.append(elec(110, y, 60, 18))
        s.append(T(110, y+42, f"V {i+1}", 23, ACCD, weight="700"))
        s.append(line(150, y, 300, y, ACC, 2.6, marker="ah"))
        s.append(box(300, y-32, 96, 64, TINT, ACC))
        s.append(T(348, y+10, "−", 34, ACCD, weight="700"))
        s.append(line(396, y, 500, y, ACC, 2.6, marker="ah"))
        s.append(box(500, y-38, 380, 76, "#FFFFFF", CARD_L))
        s.append(wave(516, y, 348, 20, 3.0, ACC, 2.4, 0.5*i, noise=5))
        # 共同成分
        s.append(wave(516, y, 348, 13, 1.0, RED, 2.2, 1.4))
    # V_ref 汇入
    s.append(elec(110, 470, 60, 18, GRN))
    s.append(T(110, 508, "V ref", 23, GRN, weight="700"))
    s.append(path("M150,470 C 230,470 250,470 250,430 L250,150", GRN, 2.8))
    for y in ys:
        s.append(line(250, y, 296, y, GRN, 2.8, marker="ahn"))
    s.append(T(700, 480, "三个通道里那条一模一样的成分，来自参考点", 25, RED, weight="700"))
    return W, H, "".join(s)

# ============================================================ 图 5 1/r 与两种参考
def fig5():
    W, H = 960, 560
    s = [T(W/2, 46, "电位随距离按 1/r 衰减", 30, INK, weight="700")]
    ox, oy, aw, ah = 110, 400, 400, 280
    s.append(line(ox, oy, ox+aw+20, oy, INK, 2.4, marker="ahk"))
    s.append(line(ox, oy, ox, oy-ah-20, INK, 2.4, marker="ahk"))
    s.append(T(ox+aw+30, oy+26, "r", 24, INK, anchor="end"))
    s.append(T(ox-14, oy-ah-24, "V", 24, INK, anchor="end"))
    # 曲线 V = k/r
    pts = []
    for i in range(200):
        r = 0.6 + i*(9.4/199)
        x = ox + (r/10.0)*aw
        y = oy - (1.0/r)*ah*0.62
        if y < oy-ah: continue
        pts.append(("M" if not pts else "L") + f"{x:.1f},{y:.1f}")
    s.append(path(" ".join(pts), ACC, 3.2))
    s.append(T(ox+aw*0.55, oy-ah*0.72, "V(r) = I / (4πσr)", 26, ACCD, weight="700"))
    for r, lab, col, dy in ((1.0,"1 mm",ACCD,28), (2.0,"2 mm",GRN,58)):
        x = ox + (r/10.0)*aw; y = oy - (1.0/r)*ah*0.62
        s.append(f'<circle cx="{x}" cy="{y}" r="7" fill="{col}"/>')
        s.append(line(x, y, x, oy+dy-20, col, 1.8, "5 5"))
        s.append(T(x, oy+dy, lab, 22, col, weight="700"))
    # 右侧柱状
    bx = 600
    s.append(box(bx, 92, 300, 330, "#FFFFFF", CARD_L))
    s.append(T(bx+150, 130, "1 mm 处那一点的幅度", 23, GRAY, weight="700"))
    s.append(T(bx+150, 160, "还剩多少", 23, GRAY, weight="700"))
    for i,(lab, frac, col) in enumerate((("参考放 2 mm", 0.50, GRN), ("参考放 100 mm", 0.99, ACC))):
        y = 200 + i*104
        s.append(T(bx+22, y+6, lab, 22, INK, anchor="start", weight="700"))
        s.append(f'<rect x="{bx+22}" y="{y+22}" width="256" height="26" rx="6" fill="{LINE}"/>')
        s.append(f'<rect x="{bx+22}" y="{y+22}" width="{256*frac:.0f}" height="26" rx="6" fill="{col}"/>')
        s.append(T(bx+278, y+72, f"{int(frac*100)}%", 24, col, anchor="end", weight="700"))
    s.append(box(600, 444, 300, 78, PANEL, CARD_L))
    s.append(T(750, 478, "减掉的是两端共有", 24, INK, weight="700"))
    s.append(T(750, 508, "的那一份", 24, INK, weight="700"))
    s.append(T(300, 522, "r 翻一倍，电位掉一半", 27, INK, weight="700"))
    return W, H, "".join(s)

# ============================================================ 图 6 重参考
def fig6():
    W, H = 960, 520
    s = [T(W/2, 46, "换参考，每一道波形都真的变了", 30, INK, weight="700")]
    rows = [("以 a 为参考", 0.0, ACC), ("以 b 为参考", 1.6, GRN)]
    for i,(lab, ph, col) in enumerate(rows):
        y = 96 + i*140
        s.append(box(50, y, 860, 118, "#FFFFFF", CARD_L))
        s.append(T(72, y+32, lab, 24, col, anchor="start", weight="700"))
        for k in range(3):
            s.append(wave(230, y+42+k*26, 640, 9, 3.0+k*0.7, col, 2.2, ph+k*0.9, noise=3))
        s.append(T(180, y+70, "3 个通道", 21, GRAY))
    s.append(box(50, 384, 420, 108, TINT, ACC))
    s.append(T(260, 420, "变了", 26, ACCD, weight="700"))
    s.append(T(260, 456, "每个通道显示成什么样", 23, INK))
    s.append(box(490, 384, 420, 108, GRNT, GRN))
    s.append(T(700, 420, "没变", 26, GRN, weight="700"))
    s.append(T(700, 456, "任意两电极之差 V i − V j", 23, INK))
    return W, H, "".join(s)

# ============================================================ 图 7 放大器先各自感知
def fig7():
    W, H = 960, 556
    s = [T(W/2, 46, "放大器不能直接感知差，它必须先分别感知两端", 30, INK, weight="700")]
    s.append(box(230, 100, 500, 300, "#FFFFFF", ACC, sw=2.4))
    s.append(T(480, 136, "放大器芯片", 25, ACCD, weight="700"))
    # 输入
    s.append(elec(96, 190, 60, 18)); s.append(T(96, 168, "V +", 23, ACCD, weight="700"))
    s.append(elec(96, 300, 60, 18, GRN)); s.append(T(96, 340, "V −", 23, GRN, weight="700"))
    s.append(line(136, 190, 226, 190, ACC, 2.8, marker="ah"))
    s.append(line(136, 300, 226, 300, GRN, 2.8, marker="ahn"))
    # 内部两步
    s.append(box(262, 168, 220, 56, TINT, ACC))
    s.append(T(372, 204, "a = V + − V amp0", 24, ACCD, weight="700"))
    s.append(box(262, 276, 220, 56, GRNT, GRN))
    s.append(T(372, 312, "b = V − − V amp0", 24, GRN, weight="700"))
    s.append(line(482, 196, 540, 232, INK, 2.4, marker="ahk"))
    s.append(line(482, 304, 540, 268, INK, 2.4, marker="ahk"))
    s.append(box(548, 214, 160, 72, PANEL, INK, sw=2))
    s.append(T(628, 260, "G · (a − b)", 26, INK, weight="700"))
    s.append(line(708, 250, 800, 250, INK, 2.8, marker="ahk"))
    s.append(T(830, 258, "输出", 25, INK, weight="700"))
    # V_amp0 端子
    s.append(line(700, 400, 700, 424, INK, 3))
    s.append(gnd(700, 424, 0.9))
    s.append(T(806, 448, "V amp0", 24, INK, weight="700"))
    s.append(T(806, 478, "仪器自己的零点", 21, BODY))
    s.append(T(806, 506, "属于机器不属于身体", 21, BODY))
    s.append(box(46, 424, 570, 96, REDT, RED))
    s.append(T(331, 460, "它在结果里消掉了", 25, RED, weight="700"))
    s.append(T(331, 496, "但 a、b 是芯片内部真实的电压", 24, INK, weight="700"))
    return W, H, "".join(s)

# ============================================================ 图 8 人体为什么漂 + 越界
def fig8():
    W, H = 960, 600
    s = [T(W/2, 44, "身体是浮的，它会被市电抬起来", 30, INK, weight="700")]
    # 左：回路
    s.append(box(46, 78, 470, 420, "#FFFFFF", CARD_L))
    x = 150
    s.append(T(x, 122, "火线 220 V / 50 Hz", 23, RED, weight="700"))
    s.append(line(x, 136, x, 176, RED, 2.8))
    s.append(cap_v(x, 190, 1.0, GRAY)); s.append(T(x+52, 198, "C₁ = 1 pF", 22, INK, anchor="start"))
    s.append(line(x, 204, x, 250, GRAY, 2.8))
    s.append(box(x-88, 250, 176, 76, TINT, ACC))
    s.append(T(x, 296, "人体", 27, ACCD, weight="700"))
    s.append(line(x, 326, x, 372, GRAY, 2.8))
    s.append(cap_v(x, 386, 1.0, GRAY)); s.append(T(x+52, 394, "C₂ = 100 pF", 22, INK, anchor="start"))
    s.append(line(x, 400, x, 436, GRAY, 2.8))
    s.append(gnd(x, 436, 1.1))
    s.append(T(280, 470, "两个电容串成分压器", 23, BODY, anchor="start"))
    # 右：结果
    s.append(box(546, 78, 368, 200, PANEL, CARD_L))
    s.append(T(730, 122, "V body = V m × C₁/(C₁+C₂)", 25, INK, weight="700"))
    s.append(T(730, 166, "= 220 × 1/101", 25, BODY))
    s.append(T(730, 224, "≈ 2.2 V", 40, RED, weight="700"))
    s.append(T(730, 258, "全身一起摆，摆得一样多", 22, BODY))
    # 电源轨
    s.append(box(546, 296, 368, 202, "#FFFFFF", CARD_L))
    ry0, ry1 = 396, 470
    s.append(f'<rect x="590" y="{ry0}" width="280" height="{ry1-ry0}" rx="8" fill="{GRNT}" stroke="{GRN}" stroke-width="2"/>')
    s.append(T(730, 424, "共模输入范围 0 – 3.3 V", 22, GRN, weight="700"))
    s.append(line(590, ry1, 870, ry1, GRN, 2))
    s.append(f'<circle cx="700" cy="{ry0-24}" r="8" fill="{RED}"/>')
    s.append(f'<circle cx="760" cy="{ry0-24}" r="8" fill="{RED}"/>')
    s.append(T(730, 334, "身体带着 2.2 V 摆", 22, RED, weight="700"))
    s.append(T(730, 362, "a、b 被顶到范围外", 22, RED, weight="700"))
    s.append(box(46, 518, 868, 62, REDT, RED))
    s.append(T(W/2, 556, "差还是那个差，一点没错。可它算不出来了。", 27, RED, weight="700"))
    return W, H, "".join(s)

# ============================================================ 图 9 地电极换掉下臂
def fig9():
    W, H = 960, 580
    s = [T(W/2, 44, "地电极把分压器的下臂换掉了", 30, INK, weight="700")]
    for i,(title, lower, val, col, tint) in enumerate((
        ("没有地电极", "C₂  31.8 MΩ", "2.2 V", RED, REDT),
        ("接上地电极", "R e  10 kΩ", "0.69 mV", GRN, GRNT))):
        bx = 46 + i*470
        s.append(box(bx, 80, 420, 380, "#FFFFFF", CARD_L))
        x = bx + 150
        s.append(T(bx+210, 116, title, 26, col, weight="700"))
        s.append(T(x, 156, "火线", 22, RED))
        s.append(line(x, 168, x, 196, RED, 2.6))
        s.append(cap_v(x, 210, 0.9, GRAY)); s.append(T(x+46, 218, "C₁", 21, INK, anchor="start"))
        s.append(line(x, 224, x, 262, GRAY, 2.6))
        s.append(box(x-76, 262, 152, 62, TINT, ACC))
        s.append(T(x, 302, "人体", 25, ACCD, weight="700"))
        s.append(line(x, 324, x, 352, GRAY, 2.6))
        if i == 0:
            s.append(cap_v(x, 366, 0.9, GRAY))
            s.append(line(x, 380, x, 408, GRAY, 2.6))
        else:
            s.append(res_v(x, 372, 52, 22, GRN))
            s.append(line(x, 398, x, 408, GRN, 2.6))
        s.append(T(x+46, 374, lower, 21, col, anchor="start", weight="700"))
        s.append(gnd(x, 408, 0.9))
        s.append(f'<rect x="{bx+250}" y="150" width="150" height="86" rx="10" fill="{tint}" stroke="{col}" stroke-width="2"/>')
        s.append(T(bx+325, 204, val, 32, col, weight="700"))
    s.append(box(46, 484, 868, 78, PANEL, CARD_L))
    s.append(T(W/2, 520, "下臂阻抗降 3200 倍，共模就降 3200 倍", 27, INK, weight="700"))
    s.append(T(W/2, 550, "磨皮、涂导电膏、按紧电极，全是在降 R e", 24, BODY))
    return W, H, "".join(s)

# ============================================================ 图 10 五种模态地电极位置
def fig10():
    W, H = 960, 500
    s = [T(W/2, 44, "那根线的另一头，具体接在哪", 30, INK, weight="700")]
    items = [
        ("心电", "右腿 / 右髋", "离心脏", "电轴最远"),
        ("体表肌电", "骨性突起", "腕骨 鹰嘴", "髌骨"),
        ("头皮脑电", "前额 / 乳突", "BioSemi 另用", "CMS + DRL"),
        ("皮层表面", "颅骨螺钉", "或非记录区", "电极条"),
        ("皮层内阵列", "颅骨螺钉", "地线在术中", "绕三圈以上"),
    ]
    cw = 172
    for i,(a,b,c,d) in enumerate(items):
        x = 46 + i*(cw+10)
        s.append(box(x, 92, cw, 268, "#FFFFFF", CARD_L))
        s.append(T(x+cw/2, 132, a, 25, ACCD, weight="700"))
        s.append(line(x+24, 152, x+cw-24, 152, LINE, 1.8))
        s.append(elec(x+cw/2, 196, 62, 18, GRN))
        s.append(T(x+cw/2, 250, b, 24, INK, weight="700"))
        s.append(T(x+cw/2, 292, c, 20, BODY))
        s.append(T(x+cw/2, 320, d, 20, BODY))
    s.append(box(46, 384, 868, 84, GRNT, GRN))
    s.append(T(W/2, 420, "共同的道理只有一条", 25, GRN, weight="700"))
    s.append(T(W/2, 452, "既导电，又尽量不产生你要记录的那种信号", 26, INK, weight="700"))
    return W, H, "".join(s)

# ============================================================ 图 11 接地 vs 浮地
def fig11():
    W, H = 960, 560
    s = [T(W/2, 44, "同一根线，既是共模的解药，也是漏电流的通道", 30, INK, weight="700")]
    for i,(title, col, tint) in enumerate((("仪器零点接大地", RED, REDT), ("浮地 / 隔离", GRN, GRNT))):
        bx = 46 + i*470
        s.append(box(bx, 82, 420, 344, "#FFFFFF", CARD_L))
        s.append(T(bx+210, 118, title, 26, col, weight="700"))
        # 人体
        s.append(box(bx+40, 150, 150, 70, TINT, ACC))
        s.append(T(bx+115, 192, "人体", 25, ACCD, weight="700"))
        # 仪器
        s.append(box(bx+240, 150, 140, 70, PANEL, INK, sw=2))
        s.append(T(bx+310, 192, "仪器", 25, INK, weight="700"))
        s.append(line(bx+190, 185, bx+238, 185, GRN, 3))
        s.append(T(bx+214, 168, "R e", 20, GRN, weight="700"))
        # 故障源
        s.append(T(bx+115, 138, "碰到带电体", 21, RED))
        s.append(line(bx+115, 150, bx+115, 122, RED, 2.6))
        # 下行到地
        s.append(line(bx+310, 220, bx+310, 288, INK, 2.8))
        if i == 0:
            s.append(gnd(bx+310, 288, 1.0))
            s.append(path(f"M{bx+115},220 L{bx+115},330 L{bx+310},330", RED, 3.2, dash="8 6", marker="ahr"))
            s.append(T(bx+210, 366, "回路成立，电流经人体", 23, RED, weight="700"))
            s.append(T(bx+210, 398, "CF 型限值 10 µA / 50 µA", 22, INK, weight="700"))
        else:
            s.append(cap_v(bx+310, 300, 0.9, GRAY))
            s.append(line(bx+310, 314, bx+310, 344, GRAY, 2.8))
            s.append(gnd(bx+310, 344, 0.9))
            s.append(T(bx+364, 306, "C₃", 21, INK, anchor="start"))
            s.append(T(bx+210, 400, "只剩几十 MΩ，电流压到 µA 以下", 22, GRN, weight="700"))
    s.append(box(46, 452, 868, 90, PANEL, CARD_L))
    s.append(T(W/2, 490, "浮地时人和仪器一起相对大地摆", 26, INK, weight="700"))
    s.append(T(W/2, 522, "这个摆动放大器完全看不见，它只看两者之间的差", 24, BODY))
    return W, H, "".join(s)

# ============================================================ 图 12 DRL 反馈环
def fig12():
    W, H = 960, 540
    s = [T(W/2, 44, "DRL 是一个把身体圈进去的负反馈环", 30, INK, weight="700")]
    # 身体
    s.append(box(60, 150, 190, 240, TINT, ACC))
    s.append(T(155, 280, "身体", 30, ACCD, weight="700"))
    # 电极组
    s.append(elec(250, 200, 40, 14)); s.append(elec(250, 236, 40, 14)); s.append(elec(250, 272, 40, 14))
    s.append(T(258, 168, "测量电极", 22, ACCD, weight="700"))
    # 求平均
    s.append(line(272, 200, 340, 236, ACC, 2.4)); s.append(line(272, 236, 340, 236, ACC, 2.4))
    s.append(line(272, 272, 340, 236, ACC, 2.4))
    s.append(box(340, 204, 150, 64, PANEL, ACC))
    s.append(T(415, 232, "电阻网络", 22, ACCD, weight="700"))
    s.append(T(415, 258, "求平均", 22, ACCD, weight="700"))
    s.append(T(415, 300, "第一步  测", 22, GRAY, weight="700"))
    # 运放
    s.append(line(490, 236, 560, 236, ACC, 2.6, marker="ah"))
    s.append(f'<path d="M560,180 L560,292 L660,236 Z" fill="#FFFFFF" stroke="{INK}" stroke-width="2.4"/>')
    s.append(T(582, 208, "−", 28, INK, anchor="start", weight="700"))
    s.append(T(582, 278, "+", 26, INK, anchor="start"))
    s.append(T(604, 330, "第二步  反相放大", 22, GRAY, weight="700"))
    # 输出 -> 限流 -> DRL 电极
    s.append(line(660, 236, 720, 236, INK, 2.6))
    s.append(res_v(720, 236, 22, 56, INK))
    s.append(T(720, 200, "限流", 21, RED, weight="700"))
    s.append(path("M748,236 L800,236 L800,430 L155,430 L155,392", INK, 2.8, marker="ahk"))
    s.append(elec(155, 402, 60, 18, GRN))
    s.append(T(300, 466, "第三步  经 DRL 电极灌回身体", 24, INK, anchor="start", weight="700"))
    s.append(box(60, 92, 840, 44, GRNT, GRN))
    s.append(T(W/2, 122, "往上飘就被拉下来，往下掉就被推上去", 25, GRN, weight="700"))
    s.append(T(W/2, 510, "身体本身就是这个反馈环的一段", 24, BODY))
    return W, H, "".join(s)

# ============================================================ 图 13 阻抗失配
def fig13():
    W, H = 960, 560
    s = [T(W/2, 44, "两边阻抗不等，共模就漏成差模", 30, INK, weight="700")]
    for i,(title, z1, z2, err, col, tint) in enumerate((
        ("Z₁ = Z₂", "5 kΩ", "5 kΩ", "仍是纯共模，被减掉", GRN, GRNT),
        ("Z₁ ≠ Z₂", "5 kΩ", "505 kΩ", "差出来的那点就是差模", RED, REDT))):
        bx = 46 + i*470
        s.append(box(bx, 80, 420, 330, "#FFFFFF", CARD_L))
        s.append(T(bx+210, 116, title, 27, col, weight="700"))
        s.append(T(bx+210, 152, "V cm 加在身体上", 22, BODY))
        s.append(line(bx+210, 164, bx+210, 186, GRAY, 2.6))
        s.append(line(bx+110, 186, bx+310, 186, GRAY, 2.6))
        for k,(zx, zl) in enumerate(((bx+110, z1), (bx+310, z2))):
            s.append(line(zx, 186, zx, 214, GRAY, 2.6))
            s.append(res_v(zx, 240, 52, 22, col))
            s.append(T(zx-32, 248, zl, 21, col, anchor="end", weight="700"))
            s.append(line(zx, 266, zx, 300, GRAY, 2.6))
            s.append(f'<circle cx="{zx}" cy="308" r="8" fill="{INK}"/>')
            s.append(T(zx, 340, "＋" if k==0 else "−", 24, INK, weight="700"))
        s.append(f'<rect x="{bx+70}" y="{356}" width="280" height="38" rx="8" fill="{tint}" stroke="{col}" stroke-width="2"/>')
        s.append(T(bx+210, 382, err, 22, col, weight="700"))
    s.append(box(46, 430, 868, 118, PANEL, CARD_L))
    s.append(T(W/2, 466, "误差 ≈ V cm × (Z₁ − Z₂) / Z in", 28, INK, weight="700"))
    s.append(T(W/2, 502, "实际湿电极失配约 5 kΩ，Z in 1 GΩ  →  3.5 nV，可以忘掉", 23, GRN, weight="700"))
    s.append(T(W/2, 532, "干电极失配约 500 kΩ，Z in 100 MΩ  →  3.45 µV，和脑电同量级", 23, RED, weight="700"))
    return W, H, "".join(s)

# ============================================================ 封面概念图 + 目录图
def cover_concept():
    W, H = 960, 500
    s = []
    # 两片电极 + 一片被划出来的第三片
    s.append(box(60, 70, 840, 360, "#FFFFFF", CARD_L))
    s.append(T(480, 128, "三片金属，只有两片进入波形", 30, INK, weight="700"))
    labs = [("测量电极", ACC, "进减法"), ("参考电极", GRN, "进减法"), ("地电极", RED, "不进减法")]
    for i,(lab, col, note) in enumerate(labs):
        x = 200 + i*280
        s.append(elec(x, 208, 108, 30, col))
        s.append(T(x, 268, lab, 26, col, weight="700"))
        s.append(T(x, 306, note, 23, BODY))
    s.append(line(200, 336, 480, 336, ACC, 2.4, "7 6"))
    s.append(T(340, 372, "V i − V ref", 26, ACCD, weight="700"))
    s.append(T(760, 372, "保证减法能发生", 24, RED, weight="700"))
    return W, H, "".join(s)

def toc_fig():
    W, H = 960, 620
    s = [T(W/2, 54, "本期路线", 32, INK, weight="700")]
    items = [
        "① 信号从哪来 —— 电流在组织里造成电位分布",
        "② 参考电极是什么 —— 一条被减进每个通道的信号",
        "③ 怎么选参考 —— 两条方向相反的判据",
        "④ 地电极是什么 —— 它不进减法，它保证减法能发生",
        "⑤ 它的两面 —— 同一根线，共模的解药与漏电流的通道",
        "⑥ 把共模压到底 —— DRL 与 CMRR，瓶颈在电极",
    ]
    for i, it in enumerate(items):
        y = 118 + i*82
        s.append(box(56, y, 848, 64, "#FFFFFF", CARD_L))
        s.append(T(84, y+42, it, 26, INK, anchor="start"))
    return W, H, "".join(s)

FIGS = {
 "fig1-volume-conductor": fig1, "fig2-two-points": fig2, "fig3-ref-moves": fig3,
 "fig4-ref-into-all": fig4, "fig5-one-over-r": fig5, "fig6-rereference": fig6,
 "fig7-amp-three-steps": fig7, "fig8-body-floats": fig8, "fig9-lower-arm": fig9,
 "fig10-where-ground": fig10, "fig11-earth-vs-float": fig11, "fig12-drl-loop": fig12,
 "fig13-mismatch": fig13, "cover-concept": cover_concept, "toc": toc_fig,
}

if __name__ == "__main__":
    import sys
    names = sys.argv[1:] or list(FIGS)
    for n in names:
        w, h, inner = FIGS[n]()
        print(render(n, w, h, inner))
