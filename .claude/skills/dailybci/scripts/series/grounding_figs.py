"""接地第一性原理 (series-grounding-01) 自制示意图。
Self-made SVG diagrams, rendered to PNG via playwright chromium.
"""
import os, subprocess, tempfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "series-grounding-01", "figs")
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
    f'<marker id="ahs" markerWidth="10" markerHeight="10" refX="1" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M8,0 L0,3 L8,6 Z" fill="{INK}"/></marker>'
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

def path(d, stroke=INK, sw=2.4, fill="none", dash=None, marker=None):
    ds = f' stroke-dasharray="{dash}"' if dash else ""
    m = f' marker-end="url(#{marker})"' if marker else ""
    return f'<path d="{d}" stroke="{stroke}" stroke-width="{sw}" fill="{fill}"{ds}{m}/>'

def gnd(x, y, scale=1.0, stroke=INK, sw=3):
    """接地符号：竖线 + 三条递减横线。(x,y) 为竖线顶端。"""
    s = scale
    o = [line(x, y, x, y+20*s, stroke, sw)]
    for i, w in enumerate((40, 24, 10)):
        yy = y + 20*s + i*8*s
        o.append(line(x-w*s/2, yy, x+w*s/2, yy, stroke, sw))
    return "".join(o)

def battery(x, y, s=1.0, stroke=INK):
    """电池符号（横向），(x,y) 为中心。长板在左=正极，短板在右=负极。"""
    o = [line(x-14*s, y-24*s, x-14*s, y+24*s, stroke, 3),
         line(x+2*s,  y-13*s, x+2*s,  y+13*s, stroke, 6)]
    return "".join(o)

def cap(x, y, s=1.0, stroke=GRAY):
    """电容符号（竖向两板），(x,y) 中心。"""
    return (line(x-30*s, y-7*s, x+30*s, y-7*s, stroke, 4)
          + line(x-30*s, y+7*s, x+30*s, y+7*s, stroke, 4))

def xmark(x, y, r=16, stroke=RED, sw=4):
    return (line(x-r, y-r, x+r, y+r, stroke, sw) + line(x-r, y+r, x+r, y-r, stroke, sw))

# ============================================================ 图 1
def fig1():
    W, H = 960, 540
    s = []
    s.append(T(W/2, 52, "把电荷 q 从 A 搬到 B", 30, INK, weight="700"))
    ax, ay, bx, by = 190, 400, 770, 210
    s.append(path(f"M{ax},{ay} C 340,300 520,430 {bx},{by}", ACC, 3.2, marker="ah"))
    s.append(circ(ax, ay, 22, "#FFFFFF", INK, 2.6)); s.append(T(ax-40, ay+12, "A", 32, INK, anchor="end", weight="700"))
    s.append(circ(bx, by, 22, "#FFFFFF", INK, 2.6)); s.append(T(bx, by-42, "B", 32, INK, weight="700"))
    s.append(circ(455, 352, 17, ACC, ACCD, 2)); s.append(T(455, 400, "q", 27, ACCD, weight="700"))
    s.append(T(470, 168, "W ＝ 沿这条路所做的功", 28, ACCD, weight="700"))
    s.append(box(70, 442, 430, 74, TINT, CARD_L))
    s.append(T(285, 490, "U ＝ W / q", 36, ACCD, weight="700"))
    s.append(T(740, 478, "W 有起点和终点，", 26, BODY))
    s.append(T(740, 512, "所以 U 也有", 26, BODY))
    return W, H, "".join(s)

# ============================================================ 图 2
def fig2():
    W, H = 960, 520
    s = []
    s.append(T(240, 48, "我们说的", 28, GRAY, weight="700"))
    s.append(T(700, 48, "完整的意思", 28, ACCD, weight="700"))
    s.append(line(480, 76, 480, 470, LINE, 2, dash="7 7"))
    # left: pin only
    s.append(box(150, 110, 180, 110, "#FFFFFF", INK, 10, 2.4))
    s.append(T(240, 175, "引脚", 30, INK))
    s.append(T(240, 268, "3.3 V", 40, INK, weight="700"))
    s.append(T(240, 330, "只提了一个点", 26, GRAY))
    # right: pin + ground + double arrow
    s.append(box(560, 110, 180, 110, "#FFFFFF", INK, 10, 2.4))
    s.append(T(650, 175, "引脚", 30, INK))
    s.append(line(650, 220, 650, 300, INK, 2.4))
    s.append(gnd(650, 300, 1.5, INK, 3))
    s.append(line(820, 232, 820, 300, ACC, 3, marker="ah"))
    s.append(line(820, 300, 820, 232, ACC, 3, marker="ah"))
    s.append(line(650, 232, 820, 232, ACC, 2, dash="5 5"))
    s.append(line(650, 300, 820, 300, ACC, 2, dash="5 5"))
    s.append(T(846, 275, "3.3 V", 32, ACCD, anchor="start", weight="700"))
    s.append(T(700, 404, "V(引脚) − V(地)", 30, ACCD, weight="700"))
    s.append(T(700, 448, "被省掉的那一端，就是地", 26, BODY))
    return W, H, "".join(s)

# ============================================================ 图 3
def fig3():
    W, H = 960, 560
    s = []
    nodes = [("A", 0.0, -3.3), ("B", 3.3, 0.0), ("C", 5.0, 1.7), ("D", -1.2, -4.5)]
    ys = {"A": 330, "B": 200, "C": 140, "D": 420}
    for cx, title, idx, col, tint in ((250, "以 A 为零", 1, ACC, TINT), (710, "以 B 为零", 2, GRN, GRNT)):
        s.append(T(cx, 52, title, 30, INK, weight="700"))
        s.append(box(cx-190, 78, 380, 420, "#FFFFFF", LINE, 14, 1.6))
        zy = ys["A"] if idx == 1 else ys["B"]
        s.append(box(cx-182, zy-27, 300, 54, tint, "none", 10, 0))
        s.append(T(cx-198, zy+9, "零", 25, col, anchor="end", weight="700"))
        for name, va, vb in nodes:
            y = ys[name]; v = va if idx == 1 else vb
            s.append(line(cx-140, y, cx-40, y, INK, 3))
            s.append(T(cx-158, y+9, name, 27, INK, anchor="end", weight="700"))
            s.append(T(cx-20, y+9, f"{v:+.1f} V", 28, col if v == 0 else BODY,
                       anchor="start", weight="700" if v == 0 else "400"))
        s.append(line(cx+140, ys["C"], cx+140, ys["D"], RED, 2.4))
        s.append(line(cx+132, ys["C"], cx+148, ys["C"], RED, 2.4))
        s.append(line(cx+132, ys["D"], cx+148, ys["D"], RED, 2.4))
        s.append(T(cx+156, (ys["C"]+ys["D"])/2+8, "6.2 V", 27, RED, anchor="start", weight="700"))
    s.append(T(W/2, 538, "每个数字都变了，C 与 D 之间的差 6.2 V 没有变", 29, INK, weight="700"))
    return W, H, "".join(s)

# ============================================================ 图 4
def fig4():
    W, H = 960, 500
    s = []
    s.append(box(60, 90, 360, 300, PANEL, CARD_L))
    s.append(T(240, 62, "系统一", 30, INK, weight="700"))
    s.append(circ(160, 300, 16, ACC, ACCD, 2)); s.append(T(160, 348, "O₁", 30, ACCD, weight="700"))
    s.append(T(240, 160, "它的零点", 26, BODY))
    s.append(box(540, 90, 360, 300, PANEL, CARD_L))
    s.append(T(720, 62, "系统二", 30, INK, weight="700"))
    # voltmeter with two probes inside system 2
    s.append(circ(720, 175, 40, "#FFFFFF", INK, 2.6)); s.append(T(720, 187, "V", 32, INK, weight="700"))
    s.append(line(690, 208, 630, 300, INK, 2.6)); s.append(circ(630, 300, 11, INK, INK, 1))
    s.append(line(750, 208, 810, 300, INK, 2.6)); s.append(circ(810, 300, 11, INK, INK, 1))
    s.append(T(720, 348, "两根表笔都在自己内部", 25, BODY))
    # attempted reach
    s.append(path("M630,300 C 500,300 320,300 178,300", RED, 3, dash="9 8"))
    s.append(xmark(400, 300, 17))
    s.append(T(400, 258, "够不着", 29, RED, weight="700"))
    s.append(T(W/2, 472, "宣布用 O₁ 当零，与真的测得到 O₁，是两回事", 29, INK, weight="700"))
    return W, H, "".join(s)

# ============================================================ 图 5
def fig5():
    W, H = 960, 500
    s = []
    s.append(box(60, 90, 360, 280, PANEL, CARD_L))
    s.append(T(240, 62, "系统一", 30, INK, weight="700"))
    s.append(circ(200, 300, 16, ACC, ACCD, 2)); s.append(T(200, 348, "O₁", 30, ACCD, weight="700"))
    s.append(T(240, 152, "读数 3.3 V", 30, INK, weight="700"))
    s.append(box(540, 90, 360, 280, PANEL, CARD_L))
    s.append(T(720, 62, "系统二", 30, INK, weight="700"))
    s.append(circ(760, 300, 16, ACC, ACCD, 2)); s.append(T(760, 348, "O₂", 30, ACCD, weight="700"))
    s.append(T(720, 152, "读数 5.0 V", 30, INK, weight="700"))
    s.append(line(200, 300, 760, 300, ACC, 5))
    s.append(box(400, 262, 160, 76, TINT, ACC, 14, 2))
    s.append(T(480, 310, "同一个零点", 28, ACCD, weight="700"))
    s.append(T(W/2, 440, "两边的读数从此可比", 29, INK, weight="700"))
    s.append(T(W/2, 480, "5.0 − 3.3 ＝ 1.7 V", 30, GRN, weight="700"))
    return W, H, "".join(s)

# ============================================================ 图 6
def fig6():
    W, H = 960, 620
    s = []
    s.append(box(70, 60, 330, 180, PANEL, CARD_L)); s.append(T(235, 160, "系统一", 30, INK, weight="700"))
    s.append(box(560, 60, 330, 180, PANEL, CARD_L)); s.append(T(725, 160, "系统二", 30, INK, weight="700"))
    s.append(line(400, 150, 448, 150, GRAY, 3)); s.append(line(512, 150, 560, 150, GRAY, 3))
    s.append(cap(480, 150, 1.0, GRAY))
    s.append(T(480, 100, "寄生电容 C", 26, GRAY, weight="700"))
    s.append(T(480, 296, "V ＝ Q / C", 34, INK, weight="700"))
    s.append(T(250, 356, "Q 在变", 28, RED, weight="700"))
    s.append(T(250, 392, "摩擦起电、静电感应、漏电流", 24, BODY))
    s.append(T(710, 356, "C 在变", 28, RED, weight="700"))
    s.append(T(710, 392, "距离、姿态、线缆位置", 24, BODY))
    s.append(line(120, 556, 880, 556, LINE, 2))
    s.append(line(120, 556, 120, 436, LINE, 2))
    s.append(T(106, 446, "V", 26, GRAY, anchor="end"))
    s.append(path("M130,528 C 200,450 250,560 320,496 S 430,450 500,524 S 620,458 700,506 S 820,464 872,522", RED, 3))
    s.append(T(W/2, 602, "两个零点之间的差，是一个随时间自由漂移的量", 29, INK, weight="700"))
    return W, H, "".join(s)

# ============================================================ 图 7
def fig7():
    W, H = 960, 500
    s = []
    y = 250
    s.append(line(120, y, 860, y, INK, 7))
    pts = [(160, "0 mV"), (490, "3.4 mV"), (820, "6.8 mV")]
    for x, v in pts:
        s.append(gnd(x, y, 1.5, INK, 3.4))
        s.append(circ(x, y, 12, INK, INK, 1))
        s.append(T(x, y-104, v, 30, RED, weight="700"))
        s.append(line(x, y-90, x, y-14, RED, 2, dash="5 5"))
    for x in (325, 655):
        s.append(T(x, y-24, "10 cm 铜线  R ≈ 3.4 mΩ", 24, GRAY))
    s.append(line(880, y, 920, y, ACC, 3))
    s.append(T(905, y-30, "I ＝ 1 A", 28, ACCD, weight="700"))
    s.append(line(920, y, 880, y, ACC, 4, marker="ah"))
    s.append(T(W/2, 428, "三处都标着同一个接地符号", 29, INK, weight="700"))
    s.append(T(W/2, 470, "电位却各不相同", 29, RED, weight="700"))
    return W, H, "".join(s)

# ============================================================ 图 8
def fig8():
    import math
    W, H = 960, 500
    s = []
    ecx, ecy, erx, ery = 480, 930, 900, 550
    s.append(f'<ellipse cx="{ecx}" cy="{ecy}" rx="{erx}" ry="{ery}" fill="#EDF1F6" stroke="{GRAY}" stroke-width="2.6"/>')
    s.append(T(W/2, 466, "地球", 32, BODY, weight="700"))
    for x, name in ((150, "你的设备"), (390, "别人的设备"), (620, "市电系统"), (840, "整栋建筑")):
        ey = ecy - ery*math.sqrt(max(0.0, 1-((x-ecx)/float(erx))**2))
        s.append(box(x-96, 150, 192, 76, PANEL, CARD_L, 12, 1.6))
        s.append(T(x, 196, name, 26, INK, weight="700"))
        s.append(line(x, 226, x, ey, ACC, 3))
        s.append(circ(x, ey, 9, ACC, ACCD, 1.5))
    s.append(T(W/2, 66, "任何地方往下打一根桩就接上了", 30, INK, weight="700"))
    return W, H, "".join(s)

# ============================================================ 图 9
def fig9():
    W, H = 960, 520
    s = []
    s.append(circ(190, 220, 46, TINT, ACC, 2.4))
    s.append(T(190, 128, "人体", 30, INK, weight="700"))
    s.append(T(190, 300, "C ＝ 100 pF", 28, BODY))
    s.append(T(190, 338, "V ＝ 35,000 V", 28, BODY))
    s.append(T(190, 392, "足以击穿一枚芯片", 26, RED, weight="700"))
    s.append(circ(760, 220, 150, "#EDF1F6", GRAY, 2.6))
    s.append(T(760, 214, "地球", 34, BODY, weight="700"))
    s.append(T(760, 268, "C ≈ 709 µF", 30, INK, weight="700"))
    s.append(line(250, 220, 590, 220, ACC, 4, marker="ah"))
    s.append(T(420, 190, "Q ＝ CV ＝ 3.5 µC", 29, ACCD, weight="700"))
    s.append(T(420, 258, "全部倾泻给地球", 25, BODY))
    s.append(box(540, 424, 400, 66, GRNT, GRN, 14, 2))
    s.append(T(740, 468, "ΔV ＝ Q/C ≈ 4.9 mV", 31, GRN, weight="700"))
    return W, H, "".join(s)

# ============================================================ 图 10
def fig10():
    W, H = 960, 580
    s = []
    s.append(f'<rect x="0" y="330" width="{W}" height="250" fill="#EFEBE4"/>')
    s.append(line(0, 330, W, 330, "#C9C0B2", 3))
    s.append(T(70, 370, "大地", 27, "#8A7F6D", anchor="start", weight="700"))
    for x, name in ((235, "设备 A"), (725, "设备 B")):
        s.append(box(x-115, 96, 230, 96, PANEL, CARD_L))
        s.append(T(x, 152, name, 30, INK, weight="700"))
        s.append(line(x, 192, x, 424, INK, 3))
        s.append(line(x-28, 424, x+28, 424, INK, 6))
        s.append(T(x, 462, "接地桩", 24, "#8A7F6D"))
    s.append(line(263, 424, 697, 424, RED, 2.6))
    s.append(T(480, 406, "ΔV", 30, RED, weight="700"))
    s.append(path("M120,514 C 330,544 630,544 850,514", RED, 3, dash="10 8", marker="ahr"))
    s.append(T(480, 566, "流经大地的电流", 25, RED, weight="700"))
    s.append(line(350, 144, 610, 144, INK, 3))
    s.append(T(480, 122, "信号线", 25, BODY))
    s.append(path("M370,166 C 430,196 530,196 590,166", ACC, 3, marker="ah"))
    s.append(T(480, 224, "环流", 27, ACCD, weight="700"))
    s.append(T(W/2, 62, "两个接地桩之间存在电位差", 30, INK, weight="700"))
    return W, H, "".join(s)

# ============================================================ 图 11
def fig11():
    W, H = 960, 520
    s = []
    s.append(T(W/2, 50, "电路图上的这个符号", 30, INK, weight="700"))
    s.append(box(392, 74, 176, 148, "#FFFFFF", LINE, 14, 1.6))
    s.append(gnd(480, 104, 2.0, INK, 4))
    s.append(line(470, 226, 250, 274, ACC, 3, marker="ah"))
    s.append(line(490, 226, 710, 274, ACC, 3, marker="ah"))
    s.append(box(70, 290, 340, 170, PANEL, CARD_L))
    s.append(T(240, 336, "一边通向大地", 29, INK, weight="700"))
    s.append('<rect x="86" y="374" width="308" height="70" rx="10" fill="#EFEBE4"/>')
    s.append(T(240, 418, "地球", 30, "#8A7F6D", weight="700"))
    s.append(box(550, 290, 340, 170, PANEL, CARD_L))
    s.append(T(720, 336, "一边通向电池负极", 29, INK, weight="700"))
    s.append(battery(700, 410, 1.6, INK))
    s.append(T(756, 420, "负极", 26, BODY, anchor="start"))
    s.append(T(W/2, 502, "它标出的是「我们约好这里是零」", 29, ACCD, weight="700"))
    return W, H, "".join(s)

# ============================================================ 封面图
def cover():
    W, H = 900, 470
    s = []
    s.append(gnd(450, 34, 3.0, INK, 7))
    s.append(line(450, 178, 250, 232, INK, 4))
    s.append(line(450, 178, 650, 232, INK, 4))
    s.append(T(250, 288, "？", 44, RED, weight="700"))
    s.append(T(650, 288, "？", 44, RED, weight="700"))
    s.append('<rect x="108" y="312" width="284" height="96" rx="14" fill="#EFEBE4"/>')
    s.append(T(250, 372, "地球", 34, "#8A7F6D", weight="700"))
    s.append(line(556, 360, 624, 360, INK, 4))
    s.append(battery(650, 360, 1.9, INK))
    s.append(line(656, 360, 744, 360, INK, 4))
    s.append(T(650, 450, "电池负极", 32, BODY, weight="700"))
    return W, H, "".join(s)

# ============================================================ 目录卡
def toc():
    W, H = 960, 700
    s = []
    items = [
        ("①", "电压天生是两点之间的量", "电压只存在于一对点之间 · 「3.3 V」是一句省略句"),
        ("②", "零点可以任选，但你得够得着", "零点可以任选 · 选零点是自由的，用零点要够得着"),
        ("③", "接地是强制大家共用同一个零点", "接地是强制大家共用同一个零点 · 不连线，两个零点之间的差会漂"),
        ("④", "地是一个网络，不是一个点", "导线有电阻，地不是等电位面 · 谁往地线上灌电流，谁就制造电位差"),
        ("⑤", "大地为什么被选中，又做不到什么", "唯一处处可达的公共导体 · 电容大到几乎不被扰动 · 提供稳定，不提供等电位"),
        ("⑥", "不接大地也可以，那叫浮地", "同一个符号，一边通向大地，一边通向电池负极"),
    ]
    y = 24
    for n, title, sub in items:
        s.append(box(24, y, 912, 104, "#F7F9FC", CARD_L, 14, 1.6))
        s.append(circ(78, y+52, 28, TINT, ACC, 1.8))
        s.append(T(78, y+63, n, 32, ACCD, weight="700"))
        s.append(T(130, y+46, title, 31, INK, anchor="start", weight="700"))
        s.append(T(130, y+82, sub, 22, GRAY, anchor="start"))
        y += 112
    return W, H, "".join(s)

FIGS = {"fig1-work-two-points": fig1, "fig2-omitted-end": fig2, "fig3-gauge": fig3,
        "fig4-cannot-reach": fig4, "fig5-shared-zero": fig5, "fig6-floating-drift": fig6,
        "fig7-ir-drop": fig7, "fig8-reachability": fig8, "fig9-earth-capacitance": fig9,
        "fig10-ground-loop": fig10, "fig11-floating-ground": fig11,
        "cover-concept": cover, "toc": toc}

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

if __name__ == "__main__":
    for name, fn in FIGS.items():
        w,h,inner = fn()
        p = render(name, w, h, inner)
        print("rendered", p, f"({w}x{h})")
