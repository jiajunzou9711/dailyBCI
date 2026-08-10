"""2026-08-08「电场与轴突生长」自制示意图。"""
import os, math, random, subprocess, tempfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-08-08-efield-axon", "figs")
os.makedirs(OUT, exist_ok=True)

ACC = "#2F6DB5"; ACCD = "#1E4E86"; TINT = "#E9F0F8"
INK = "#1A1A1A"; BODY = "#4A4A4A"; GRAY = "#8A8A8A"; LINE = "#D6DBE2"
RED = "#C0392B"; WARM = "#B8860B"

DEFS = ('<defs>'
        '<marker id="ah" markerWidth="10" markerHeight="10" refX="8" refY="3" '
        f'orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="{GRAY}"/></marker>'
        '<marker id="ahb" markerWidth="10" markerHeight="10" refX="8" refY="3" '
        f'orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="{ACC}"/></marker>'
        '<marker id="ahr" markerWidth="10" markerHeight="10" refX="8" refY="3" '
        f'orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="{RED}"/></marker>'
        '</defs>')


def T(x, y, s, size=25, fill=INK, anchor="middle", weight="400"):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" font-weight="{weight}">{s}</text>')


def box(x, y, w, h, fill, stroke, rx=12, sw=1.5):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')


def circ(cx, cy, r, fill, stroke="none", sw=0):
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke != "none" else ""
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"{st}/>'


# ---------------------------------------------------------------- 目录卡
def toc():
    items = [
        ("1", "一篇新论文换了供电方式", "可降解压电材料替代椎体,大鼠"),
        ("2", "电极过去放哪,这次放哪", "硬膜外腔与椎体的位置关系"),
        ("3", "培养皿里,电场能导向生长", "150 mV/mm 下轨迹整片偏向阴极"),
        ("4", "转向和长得快是两件事", "50-60 与 70 mV/mm 两个阈值"),
        ("5", "活体里,轴突长到哪里", "长到断面,没有一根穿过"),
        ("6", "人身上做到什么程度", "2005 年 I 期 10 例,此后未获批"),
    ]
    s = []; y = 24
    for n, title, sub in items:
        s.append(box(28, y, 904, 78, "#F7F9FC", "#DCE5F0", 14, 1.5))
        s.append(circ(74, y + 39, 25, TINT, ACC, 1.5))
        s.append(T(74, y + 49, n, 29, ACCD, weight="700"))
        s.append(T(122, y + 34, title, 28, INK, anchor="start", weight="700"))
        s.append(T(122, y + 63, sub, 21, GRAY, anchor="start"))
        y += 91
    return 960, y + 8, "".join(s)


# ------------------------------------------- 图1:神经突与电场下的轨迹分布
def neurite():
    """三格:无场 / 有场 / 阻断信号通路。轨迹从同一胞体辐射。"""
    W, H = 980, 620
    s = []
    # 上方:单根神经突的结构说明
    s.append(box(24, 16, 932, 118, "#F7F9FC", "#DCE5F0", 14, 1.5))
    cx, cy = 130, 76
    s.append(circ(cx, cy, 24, TINT, ACCD, 2.5))
    s.append(f'<path d="M{cx+24},{cy} C240,{cy} 320,{cy-16} 430,{cy-6}" fill="none" '
             f'stroke="{ACCD}" stroke-width="4"/>')
    # 生长锥:扇形 + 伪足
    gx, gy = 430, 70
    s.append(f'<path d="M{gx},{gy-16} L{gx+52},{gy-30} L{gx+62},{gy} L{gx+52},{gy+30} '
             f'L{gx},{gy+16} Z" fill="{TINT}" stroke="{ACCD}" stroke-width="2.5"/>')
    for ang in (-40, -14, 12, 38):
        ex = gx + 62 + 26 * math.cos(math.radians(ang))
        ey = gy + 26 * math.sin(math.radians(ang))
        s.append(f'<line x1="{gx+58}" y1="{gy + 12*math.sin(math.radians(ang)):.1f}" '
                 f'x2="{ex:.1f}" y2="{ey:.1f}" stroke="{ACCD}" stroke-width="2.4"/>')
    s.append(T(cx, cy + 56, "胞体", 22, GRAY))
    s.append(T(280, cy - 26, "神经突", 24, INK, weight="700"))
    s.append(T(560, cy - 26, "生长锥", 24, INK, anchor="start", weight="700"))
    s.append(T(560, cy + 8, "决定往哪儿长", 21, GRAY, anchor="start"))

    # 下方三格
    panels = [("无电场", None, "#FFFFFF"), ("150 mV/mm", "left", "#FFFFFF"),
              ("同样电场 + 阻断信号通路", None, "#FFFFFF")]
    px0, pw, gap = 24, 300, 16
    top, ph = 172, 328
    random.seed(11)
    for i, (lab, bias, bg) in enumerate(panels):
        x0 = px0 + i * (pw + gap)
        s.append(box(x0, top, pw, ph, bg, LINE, 12, 1.5))
        ccx, ccy = x0 + pw / 2, top + ph / 2
        n = 34
        for k in range(n):
            a = random.uniform(0, 2 * math.pi)
            if bias == "left":
                # 朝左(阴极)偏置:角度向 180 度收拢
                a = math.pi + (a - math.pi) * 0.42 + random.gauss(0, 0.22)
                L = random.uniform(58, 122)
            else:
                L = random.uniform(42, 84)
            x1 = ccx + L * math.cos(a); y1 = ccy + L * math.sin(a)
            mx = ccx + L * 0.55 * math.cos(a + random.gauss(0, 0.35))
            my = ccy + L * 0.55 * math.sin(a + random.gauss(0, 0.35))
            s.append(f'<path d="M{ccx:.0f},{ccy:.0f} Q{mx:.0f},{my:.0f} {x1:.0f},{y1:.0f}" '
                     f'fill="none" stroke="{INK}" stroke-width="1.7" opacity="0.85"/>')
        s.append(circ(ccx, ccy, 9, "#BBBBBB"))
        s.append(T(ccx, top + ph + 30, lab, 23, INK, weight="700"))
    # 电场极性标注(中间格)
    mx0 = px0 + (pw + gap)
    s.append(T(mx0 + 16, top + 30, "−", 40, ACC, anchor="start", weight="700"))
    s.append(T(mx0 + pw - 16, top + 30, "+", 36, GRAY, anchor="end", weight="700"))
    s.append(T(mx0 + 34, top + 56, "阴极", 19, ACC, anchor="start"))
    s.append(T(mx0 + pw - 34, top + 56, "阳极", 19, GRAY, anchor="end"))
    s.append(T(490, 592, "同一胞体处叠加多个神经元,画出 5 小时的生长轨迹", 22, GRAY))
    return W, H, "".join(s)


# --------------------------------------------------- 图2:转向 vs 长得快
def turn_speed():
    W, H = 980, 430
    s = []
    cols = [(24, "转向", "50–60 mV/mm", "已经在长的神经突改变方向,把头调向阴极", "turn"),
            (500, "长得快", "> 70 mV/mm", "方向不变,朝阴极的伸长速度约为朝阳极的 3 倍", "fast")]
    for x0, name, thr, desc, kind in cols:
        s.append(box(x0, 20, 456, 386, "#FFFFFF", LINE, 14, 1.5))
        s.append(T(x0 + 228, 62, name, 30, INK, weight="700"))
        s.append(box(x0 + 128, 78, 200, 42, TINT, ACC, 10, 1.5))
        s.append(T(x0 + 228, 107, thr, 25, ACCD, weight="700"))
        cy = 218
        if kind == "turn":
            s.append(f'<path d="M{x0+330},{cy+70} C{x0+300},{cy+30} {x0+230},{cy+10} '
                     f'{x0+120},{cy-10}" fill="none" stroke="{ACCD}" stroke-width="5" '
                     f'marker-end="url(#ahb)"/>')
            s.append(T(x0 + 66, cy - 30, "阴极", 22, ACC, weight="700"))
        else:
            s.append(f'<line x1="{x0+300}" y1="{cy-26}" x2="{x0+118}" y2="{cy-26}" '
                     f'stroke="{ACCD}" stroke-width="6" marker-end="url(#ahb)"/>')
            s.append(f'<line x1="{x0+300}" y1="{cy+42}" x2="{x0+240}" y2="{cy+42}" '
                     f'stroke="{GRAY}" stroke-width="4" marker-end="url(#ah)"/>')
            s.append(T(x0 + 66, cy - 56, "阴极", 22, ACC, weight="700"))
            s.append(T(x0 + 118, cy + 4, "朝阴极", 20, ACCD, anchor="start"))
            s.append(T(x0 + 244, cy + 72, "朝阳极", 20, GRAY, anchor="start"))
        for j, line in enumerate(_wrap(desc, 17)):
            s.append(T(x0 + 228, 328 + j * 32, line, 23, BODY))
    return W, H, "".join(s)


def _wrap(text, n):
    return [text[i:i + n] for i in range(0, len(text), n)]


# ------------------------------------------------------------ 图3:三道边界
def boundaries():
    W, H = 980, 520
    s = []
    rows = [
        ("量级", "培养皿 50–60 mV/mm", "活体到达脊髓 40–600 µV/mm", "相差约两个数量级"),
        ("细胞", "鸡胚、蛙胚、胚胎大鼠", "本来就在生长的神经元", "成年中枢神经元不在这个状态"),
        ("统计", "群体轨迹的分布偏移", "仍有神经突朝别的方向长", "不是每一根都朝阴极"),
    ]
    y = 26
    for tag, a, b, note in rows:
        s.append(box(24, y, 932, 142, "#FFFFFF", LINE, 14, 1.5))
        s.append(box(48, y + 26, 92, 44, TINT, ACC, 10, 1.5))
        s.append(T(94, y + 56, tag, 25, ACCD, weight="700"))
        s.append(T(168, y + 56, a, 25, INK, anchor="start", weight="700"))
        s.append(f'<line x1="168" y1="{y+78}" x2="908" y2="{y+78}" stroke="{LINE}" '
                 f'stroke-width="1.5"/>')
        s.append(T(168, y + 108, b, 24, BODY, anchor="start"))
        s.append(T(908, y + 108, note, 22, RED, anchor="end"))
        y += 158
    return W, H, "".join(s)


# ------------------------------------------------- 图4:在体怎么给电
def invivo():
    W, H = 980, 470
    s = []
    # 脊髓纵向
    cx0, cx1 = 120, 860
    cy = 200
    s.append(f'<rect x="{cx0}" y="{cy-46}" width="{cx1-cx0}" height="92" rx="16" '
             f'fill="#FBFCFD" stroke="{LINE}" stroke-width="3"/>')
    s.append(T(cx0 + 14, cy - 62, "脊髓", 23, GRAY, anchor="start"))
    # 损伤区
    lx0, lx1 = 452, 528
    s.append(f'<rect x="{lx0}" y="{cy-46}" width="{lx1-lx0}" height="92" '
             f'fill="#F3E4E2" stroke="{RED}" stroke-width="2.5"/>')
    s.append(T((lx0 + lx1) / 2, cy + 78, "损伤区", 23, RED, weight="700"))
    # 两个电极:在脊髓之外
    for ex, sign, col in ((300, "−", ACC), (680, "+", GRAY)):
        s.append(f'<rect x="{ex-30}" y="{cy-152}" width="60" height="46" rx="8" '
                 f'fill="{TINT}" stroke="{col}" stroke-width="2.5"/>')
        s.append(T(ex, cy - 120, sign, 32, col, weight="700"))
        s.append(f'<line x1="{ex}" y1="{cy-104}" x2="{ex}" y2="{cy-58}" stroke="{col}" '
                 f'stroke-width="3"/>')
    s.append(T(490, cy - 168, "电极都在脊髓之外", 25, INK, weight="700"))
    # 场线:两电极之间穿过损伤区
    for dy in (-22, 4, 30):
        s.append(f'<path d="M660,{cy+dy} C560,{cy+dy-16} 420,{cy+dy-16} 320,{cy+dy}" '
                 f'fill="none" stroke="{ACC}" stroke-width="2.4" opacity="0.75" '
                 f'marker-end="url(#ahb)"/>')
    # 下方两条结论
    s.append(box(60, 316, 400, 118, "#F7F9FC", "#DCE5F0", 14, 1.5))
    s.append(T(260, 352, "到达脊髓的场强", 23, GRAY))
    s.append(T(260, 396, "40–600 µV/mm", 34, ACCD, weight="700"))
    s.append(box(520, 316, 400, 118, "#F7F9FC", "#DCE5F0", 14, 1.5))
    s.append(T(720, 352, "极性每隔一段时间翻转", 23, GRAY))
    s.append(T(720, 396, "上行与下行都要长", 30, ACCD, weight="700"))
    return W, H, "".join(s)


# --------------------------------------------- 图5:轴突长到了哪里
def how_far():
    W, H = 980, 470
    s = []
    cx0, cx1, cy = 90, 890, 210
    s.append(f'<rect x="{cx0}" y="{cy-96}" width="{cx1-cx0}" height="192" rx="16" '
             f'fill="#FBFCFD" stroke="{LINE}" stroke-width="3"/>')
    lx0, lx1 = 440, 556
    s.append(f'<rect x="{lx0}" y="{cy-96}" width="{lx1-lx0}" height="192" '
             f'fill="#F3E4E2" stroke="{RED}" stroke-width="2.5" stroke-dasharray="7,5"/>')
    s.append(T((lx0 + lx1) / 2, cy - 118, "损伤区", 24, RED, weight="700"))
    s.append(f'<line x1="{lx0}" y1="{cy-96}" x2="{lx0}" y2="{cy+96}" stroke="{RED}" '
             f'stroke-width="4"/>')
    s.append(T(lx0 - 8, cy + 126, "切断平面", 22, RED, anchor="end"))

    # 多数:长到断面为止
    for dy in (-62, -34, -6):
        s.append(f'<path d="M{cx0+30},{cy+dy} C240,{cy+dy} 340,{cy+dy+6} {lx0-4},{cy+dy+4}" '
                 f'fill="none" stroke="{ACCD}" stroke-width="4"/>')
        s.append(circ(lx0 - 4, cy + dy + 4, 7, ACCD))
    s.append(T(150, cy - 84, "多数动物：长到断面为止", 23, ACCD, anchor="start", weight="700"))

    # 少数:绕到边缘
    s.append(f'<path d="M{cx0+30},{cy+56} C260,{cy+56} 360,{cy+90} {lx0-6},{cy+90} '
             f'C{lx0+40},{cy+90} {lx1-30},{cy+88} {lx1+16},{cy+74}" '
             f'fill="none" stroke="{WARM}" stroke-width="4"/>')
    s.append(circ(lx1 + 16, cy + 74, 7, WARM))
    s.append(T(150, cy + 40, "少数动物：绕到损伤边缘", 23, WARM, anchor="start", weight="700"))

    # 断面另一侧:空
    s.append(T(730, cy - 20, "没有一根", 34, RED, weight="700"))
    s.append(T(730, cy + 24, "穿过损伤区", 34, RED, weight="700"))
    s.append(T(490, 428, "成年豚鼠，辣根过氧化物酶顺行示踪，伤后 50–60 天", 22, GRAY))
    return W, H, "".join(s)


# --------------------------------------------- 图6:功能恢复的量级(BBB)
def function():
    W, H = 980, 430
    s = []
    x0, x1, y = 70, 910, 150
    s.append(T(490, 52, "大鼠后肢运动评分（BBB，0–21）", 26, INK, weight="700"))
    bands = [(0, 7, "#EFEFEF", "孤立关节活动"), (8, 13, "#E4EBF3", "不协调迈步"),
             (14, 21, "#D4E2F0", "稳定的前后肢协调")]
    span = (x1 - x0) / 21
    for a, b, col, lab in bands:
        bx0 = x0 + a * span; bx1 = x0 + (b + 1) * span
        s.append(f'<rect x="{bx0:.0f}" y="{y}" width="{bx1-bx0:.0f}" height="66" '
                 f'fill="{col}" stroke="{LINE}" stroke-width="1.5"/>')
        s.append(T((bx0 + bx1) / 2, y + 42, lab, 21, BODY))
    for v in (0, 7, 13, 21):
        s.append(T(x0 + (v + 0.5) * span, y - 12, str(v), 21, GRAY))
    # 提高约 3 分的位移
    sx = x0 + 8.5 * span; ex = x0 + 11.5 * span
    s.append(f'<line x1="{sx:.0f}" y1="{y+112}" x2="{ex:.0f}" y2="{y+112}" stroke="{ACCD}" '
             f'stroke-width="6" marker-end="url(#ahb)"/>')
    s.append(T((sx + ex) / 2, y + 84, "约 3 分", 24, ACCD, weight="700"))
    s.append(T((sx + ex) / 2, y + 152, "8 项研究合并，第 8 周高出 3.00 分", 22, GRAY))
    s.append(T(490, y + 194, "位移发生在同一档内，没有跨过“能协调负重行走”这条界", 24, RED))
    s.append(box(200, y + 214, 580, 56, "#F7F9FC", "#DCE5F0", 12, 1.5))
    s.append(T(490, y + 250, "另一项成年豚鼠研究：25% 的动物一个反射恢复", 23, BODY))
    return W, H, "".join(s)


# --------------------------------------------- 图7:人体 I 期的三项改善
def human():
    W, H = 980, 466
    s = []
    s.append(T(490, 52, "2005 年 I 期试验，10 例完全性脊髓损伤，随访 1 年", 25, INK, weight="700"))
    rows = [("轻触觉", 25.5, 112), ("针刺觉", 20.4, 112), ("运动", 6.3, 100)]
    x0, xw = 250, 560
    y = 118
    for lab, val, full in rows:
        s.append(T(x0 - 24, y + 38, lab, 26, INK, anchor="end", weight="700"))
        s.append(f'<rect x="{x0}" y="{y+12}" width="{xw}" height="44" rx="6" '
                 f'fill="#F0F2F4" stroke="{LINE}" stroke-width="1.5"/>')
        w = xw * val / full
        col = ACCD if full == 112 else RED
        s.append(f'<rect x="{x0}" y="{y+12}" width="{w:.0f}" height="44" rx="6" fill="{col}"/>')
        s.append(T(x0 + xw + 18, y + 44, f"{val} / {full}", 25, col, anchor="start", weight="700"))
        y += 82
    s.append(T(490, 414, "感觉改善明显，运动改善有限；无同期对照组", 25, RED, weight="700"))
    return W, H, "".join(s)


FIGS = {"toc": toc, "fig-neurite": neurite, "fig-turn-speed": turn_speed,
        "fig-boundary": boundaries, "fig-invivo": invivo, "fig-howfar": how_far,
        "fig-function": function, "fig-human": human}


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
