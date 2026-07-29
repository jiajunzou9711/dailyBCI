"""专题：硬脑膜第 ③ 期（series-dura-03）自制示意图。SVG → PNG via playwright chromium。"""
import os, subprocess, tempfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "series-dura-03", "figs")
os.makedirs(OUT, exist_ok=True)

ACC = "#2F6DB5"; ACCD = "#1E4E86"; TINT = "#E9F0F8"
INK = "#1A1A1A"; BODY = "#4A4A4A"; GRAY = "#8A8A8A"
RED = "#C0392B"; BLOOD = "#A11F1A"; BLOODL = "#D9534F"
BONE = "#E6E2D8"; BONE_E = "#A9A499"
PER = "#F0C478"; MEN = "#E0A757"; DBC = "#C98F45"; PERE = "#A87B32"
ARA = "#BFD9EC"; CSF = "#DCEBF7"; CSF_E = "#8FBADA"; PIA = "#8FB6D4"
CTX = "#E4E7E2"; CTX_E = "#AEB4AC"
TOOL = "#5A6570"


def T(x, y, s, size=22, fill=INK, anchor="middle", weight="400"):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" font-weight="{weight}">{s}</text>')


def box(x, y, w, h, fill, stroke, rx=8, sw=1.5):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')


def bleeds():
    W, H = 1460, 1120
    XL, XR = 60, 640
    s = []
    s.append(box(20, 14, W - 40, 56, TINT, ACC, 10, 1.5))
    s.append(T(W / 2, 51, "电极穿过哪一层，就可能在哪一层出血", 30, ACCD, weight="700"))

    # ---- 层结构 ----
    yb, hb = 120, 62                      # 颅骨
    ye = yb + hb                          # 硬膜外潜在腔顶
    he = 20
    yd = ye + he                          # 硬膜顶
    h_per, h_men, h_dbc = 20, 16, 9
    yd2 = yd + h_per + h_men              # 边界细胞层顶
    ya = yd + h_per + h_men + h_dbc       # 蛛网膜顶
    h_ara = 10
    yc = ya + h_ara                       # 蛛网膜下腔顶
    h_csf = 84
    yp = yc + h_csf                       # 软膜顶
    h_pia = 10
    ycx = yp + h_pia                      # 皮层顶
    h_ctx = 168

    s.append(box(XL, yb, XR - XL, hb, BONE, BONE_E, 4, 1.8))
    xx = XL + 22
    while xx < XR - 16:
        s.append(f'<ellipse cx="{xx}" cy="{yb+31}" rx="9" ry="6" fill="#CFC8B8"/>')
        xx += 34
    s.append(T(XL + 6, yb - 14, "颅骨", 22, BODY, anchor="start"))
    s.append(T(XR - 6, yb - 14, "（内板）", 19, GRAY, anchor="end"))

    # 硬膜外潜在腔（白）
    s.append(f'<rect x="{XL}" y="{ye}" width="{XR-XL}" height="{he}" fill="#FFFFFF"/>')

    # 硬膜三层
    s.append(box(XL, yd, XR - XL, h_per, PER, PERE, 2, 1.2))
    s.append(box(XL, yd + h_per, XR - XL, h_men, MEN, PERE, 2, 1.2))
    s.append(box(XL, yd2, XR - XL, h_dbc, DBC, PERE, 2, 1.2))
    # 蛛网膜 / 脑脊液 / 软膜 / 皮层
    s.append(box(XL, ya, XR - XL, h_ara, ARA, CSF_E, 2, 1.0))
    s.append(box(XL, yc, XR - XL, h_csf, CSF, CSF_E, 3, 1.2))
    s.append(box(XL, yp, XR - XL, h_pia, PIA, CSF_E, 2, 1.0))
    s.append(box(XL, ycx, XR - XL, h_ctx, CTX, CTX_E, 8, 1.6))
    s.append(T(XL + 24, ycx + 130, "皮层", 26, "#5A5F5A", anchor="start"))
    s.append(T(XL + 18, yc + 52, "蛛网膜下腔", 21, "#3D7CA8", anchor="start"))
    s.append(T(XL + 18, yc + 76, "（脑脊液）", 19, "#3D7CA8", anchor="start"))

    # ---- 出血 ----
    # ① 硬膜外血肿：双凸透镜形，把硬膜从骨面顶开
    s.append(f'<path d="M118,{ye+1} L292,{ye+1} Q205,{ye+19} 118,{ye+1} Z" '
             f'fill="{BLOOD}" opacity="0.9"/>')
    # ② 硬膜下血肿：新月形，位于硬膜边界细胞层内
    s.append(f'<path d="M410,{yd2+1} Q505,{yd2} 600,{yd2+1} Q505,{ya+13} 410,{yd2+1} Z" '
             f'fill="{BLOODL}" opacity="0.95"/>')
    # ③ 蛛网膜下腔出血：脑脊液里的弥散血
    s.append(f'<path d="M{XL+10},{yc+62} Q190,{yc+26} 320,{yc+42} Q430,{yc+56} 520,{yc+38} '
             f'L520,{yp-3} L{XL+10},{yp-3} Z" fill="{BLOODL}" opacity="0.5"/>')
    # ④ 脑内血肿：沿电极道
    s.append(f'<ellipse cx="352" cy="{ycx+82}" rx="40" ry="62" fill="{BLOOD}" opacity="0.85"/>')

    # ---- 电极 ----
    s.append(f'<rect x="344" y="88" width="16" height="{ycx+120-88}" fill="{TOOL}"/>')
    s.append(f'<path d="M344,{ycx+120} L360,{ycx+120} L352,{ycx+148} Z" fill="#39424B"/>')
    s.append(T(372, 104, "电极", 21, TOOL, anchor="start"))

    # ---- 层标注（右侧引线）----
    LX = 672
    def lead(ysrc, ylab, txt, col, size=21):
        return (f'<polyline points="{XR},{ysrc} {LX-34},{ysrc} {LX-14},{ylab-7}" '
                f'fill="none" stroke="{col}" stroke-width="1.5"/>'
                + T(LX, ylab, txt, size, col, anchor="start", weight="700"))

    s.append(lead(yd + 10, yd + 4, "硬膜  骨内膜层", PERE, 20))
    s.append(lead(yd + h_per + 8, yd + h_per + 30, "硬膜  脑膜层", PERE, 20))
    s.append(lead(yd2 + 5, yd2 + 52, "硬膜  边界细胞层", DBC, 20))
    s.append(lead(ya + 5, ya + 74, "蛛网膜", "#3D7CA8", 20))
    s.append(lead(yp + 5, yp + 8, "软脑膜", "#3D7CA8", 20))

    # ---- 编号圆点 ----
    marks = [("①", 205, ye + 6), ("②", 500, yd2 + 14), ("③", 210, yc + 46),
             ("④", 352, ycx + 82)]
    for n, mx, my in marks:
        s.append(f'<circle cx="{mx}" cy="{my}" r="19" fill="#FFFFFF" stroke="{BLOOD}" stroke-width="2.5"/>')
        s.append(T(mx, my + 8, n, 24, BLOOD, weight="700"))

    # ---- 右下：四类说明 ----
    RX, RY, RW = 672, 478, 762
    rows = [
        ("①", "硬膜外血肿  EDH", "颅骨内板与硬膜骨内膜层之间的潜在腔隙",
         "脑膜中动脉分支（走在硬膜层内）", "动脉血把硬膜从骨面剥开，CT 上呈双凸透镜形"),
        ("②", "硬膜下血肿  SDH", "并非真正的腔隙：血液撕开的是硬膜边界细胞层",
         "桥静脉", "血肿实际形成于硬膜之内，CT 上呈新月形"),
        ("③", "蛛网膜下腔出血  SAH", "蛛网膜与软脑膜之间，充满脑脊液的真实腔隙",
         "软膜血管、皮层表面血管", "血液混入脑脊液，可沿脑沟扩散"),
        ("④", "脑内血肿  ICH", "皮层实质内，沿电极道",
         "被切断的穿支血管", "直接破坏神经元与纤维；致死病例主要出自这一类"),
    ]
    y = RY
    for n, name, space, src, note in rows:
        s.append(box(RX, y, RW, 140, "#FFFFFF", "#E2D3D1", 10, 1.5))
        s.append(f'<circle cx="{RX+34}" cy="{y+34}" r="17" fill="{BLOOD}"/>')
        s.append(T(RX + 34, y + 42, n, 22, "#FFFFFF", weight="700"))
        s.append(T(RX + 64, y + 42, name, 24, BLOOD, anchor="start", weight="700"))
        s.append(T(RX + 22, y + 74, "位置　" + space, 19, BODY, anchor="start"))
        s.append(T(RX + 22, y + 100, "来源　" + src, 19, GRAY, anchor="start"))
        s.append(T(RX + 22, y + 126, "形态　" + note, 19, GRAY, anchor="start"))
        y += 150

    s.append(T(RX, 450, "四类出血：名称、腔隙、血管来源", 24, INK, anchor="start", weight="700"))
    CY = 560
    s.append(T(60, CY - 18, "出血之后：有名字的二级后果", 24, INK, anchor="start", weight="700"))
    conseq = [
        ("占位效应 → 中线移位 → 脑疝", "血肿体积挤压脑组织，急性致死的主要路径"),
        ("颅内压升高", "继发脑灌注压下降"),
        ("癫痫发作", "血液分解产物致痫；含铁血黄素沉积可形成慢性致痫灶"),
        ("梗死", "动脉被切断 → 供血区梗死；皮层引流静脉受伤 → 静脉性梗死"),
        ("脑积水", "血液阻塞脑脊液通路或影响蛛网膜颗粒吸收"),
        ("血管痉挛 → 迟发性脑缺血", "见于动脉瘤性 SAH（血量远大于电极道出血，不可直接外推）"),
    ]
    cy = CY
    for a, b in conseq:
        s.append(box(60, cy, 580, 58, "#FDF3F1", "#E5B9AF", 8, 1.3))
        s.append(T(78, cy + 26, a, 20, "#A03A28", anchor="start", weight="700"))
        s.append(T(78, cy + 48, b, 17, BODY, anchor="start"))
        cy += 66

    s.append(T(20 + 14, H - 24,
               "层次结构依 StatPearls《Epidural Hematoma》《Subdural Hematoma》与 Kinaci 2020；"
               "腔隙与血管来源均为该类血肿的典型情形，非唯一来源。",
               17, GRAY, anchor="start"))
    return W, H, "".join(s)



def chronic():
    W, H = 1500, 1080
    s = []
    s.append(box(20, 14, W - 40, 56, TINT, ACC, 10, 1.5))
    s.append(T(W / 2, 51, "慢性危害：两条不同的链，汇到同一个结局", 30, ACCD, weight="700"))

    AX, BX, CW = 70, 790, 640
    HA, HB = "#A11F1A", "#1E4E86"

    def chain(x, title, sub, col, items, y0):
        o = [box(x, y0, CW, 62, "#FFFFFF", col, 10, 2)]
        o.append(T(x + CW / 2, y0 + 30, title, 25, col, weight="700"))
        o.append(T(x + CW / 2, y0 + 53, sub, 18, GRAY))
        y = y0 + 82
        for i, (a, b) in enumerate(items):
            o.append(box(x, y, CW, 86, "#FDF3F1" if col == HA else "#EDF3FA",
                         "#E5B9AF" if col == HA else CSF_E, 8, 1.3))
            o.append(T(x + 22, y + 34, a, 21, INK, anchor="start", weight="700"))
            o.append(T(x + 22, y + 62, b, 17, BODY, anchor="start"))
            y += 86
            if i < len(items) - 1:
                o.append(f'<line x1="{x+CW/2}" y1="{y-2}" x2="{x+CW/2}" y2="{y+16}" '
                         f'stroke="{col}" stroke-width="2.5" marker-end="url(#ac)"/>')
                y += 20
        return "".join(o), y

    A = [("插入时血管破裂", "尺寸与选点决定，见前一块"),
         ("血脑屏障破坏", "血液成分进入脑实质"),
         ("纤维蛋白原漏出", "它是潜伏型 TGF-β 的载体"),
         ("星形胶质细胞 Smad2 磷酸化", "Schachtrup 2010，小鼠；去掉纤维蛋白原可减轻"),
         ("沉积硫酸软骨素蛋白聚糖 → 胶质瘢痕", "抑制神经突生长")]
    B = [("植入体持续存在", "Biran 2005：只做刺伤的对照会消退，有电极的不消退"),
         ("异物反应：小胶质活化、星形胶质增生", "电极周围形成包裹鞘"),
         ("脑膜反应：包裹与挤出", "Barrese 2013：占慢性失效的一半以上"),
         ("电极周围毛细血管密度下降、血流减少", "Solarana 2020，小鼠，OCT-A：100 µm 内 p<0.001"),
         ("神经元代谢供应受损", "作者判断：电极干扰了神经元与毛细血管床的耦合")]

    sa, ya = chain(AX, "链 A　由血管损伤起始", "急性事件，可以靠避开血管减少", HA, A, 92)
    sb, yb2 = chain(BX, "链 B　由植入体存在维持", "与是否扎中血管无关，避不开", HB, B, 92)
    s.append(sa); s.append(sb)

    ym = max(ya, yb2) + 24
    for x, col in ((AX + CW / 2, HA), (BX + CW / 2, HB)):
        s.append(f'<path d="M{x},{ym-22} L{x},{ym+6} L{W/2},{ym+6} L{W/2},{ym+30}" '
                 f'fill="none" stroke="{col}" stroke-width="2.5"/>')
    s.append(f'<path d="M{W/2-8},{ym+30} L{W/2+8},{ym+30} L{W/2},{ym+46} Z" fill="{INK}"/>')

    yo = ym + 56
    s.append(box(300, yo, 900, 82, "#F5F0E4", "#C9B98A", 10, 2))
    s.append(T(750, yo + 36, "神经元丢失", 26, "#7A5F14", weight="700"))
    s.append(T(750, yo + 64, "小鼠：电极 100 µm 内 50% 神经元丢失，发生在 137 ± 56 天（Solarana 2020）",
               19, BODY))
    s.append(f'<line x1="750" y1="{yo+84}" x2="750" y2="{yo+104}" stroke="{INK}" '
             f'stroke-width="2.5" marker-end="url(#ac)"/>')
    yo2 = yo + 108
    s.append(box(300, yo2, 900, 82, "#F5F0E4", "#C9B98A", 10, 2))
    s.append(T(750, yo2 + 36, "记录性能下降", 26, "#7A5F14", weight="700"))
    s.append(T(750, yo2 + 64,
               "高 gamma 功率与发放率的下降，同毛细血管密度与神经元存活显著正相关", 19, BODY))

    s.append(T(70, H - 46,
               "链 A 的证据：Schachtrup 2010（小鼠，机制）、Saxena 2013（大鼠，相关）、Szymanski 2021（人，尸检）",
               17, GRAY, anchor="start"))
    s.append(T(70, H - 22,
               "链 B 的证据：Biran 2005、Barrese 2013、Solarana 2020　｜　两条链各自贡献多少，目前没有定论",
               17, GRAY, anchor="start"))
    return W, H, "".join(s)


FIGS = {"fig-bleeds": bleeds, "fig-chronic": chronic}


def render(name, w, h, inner):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
           f'viewBox="0 0 {w} {h}" font-family="HeitiSC,Helvetica,Arial,sans-serif">'
           f'<defs><marker id="ac" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L7,3 L0,6 Z" fill="context-stroke"/></marker></defs>'
           f'<rect width="{w}" height="{h}" fill="#FFFFFF"/>{inner}</svg>')
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
    import sys
    for name in (sys.argv[1:] or list(FIGS)):
        w, h, inner = FIGS[name]()
        print("rendered", render(name, w, h, inner), f"({w}x{h})")
