"""专题：硬脑膜（series-dura-01）自制示意图。
SVG → PNG via playwright chromium。画布宽 960，字号按卡片可读性设计。
"""
import os, subprocess, tempfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "series-dura-01", "figs")
os.makedirs(OUT, exist_ok=True)

ACC = "#2F6DB5"; ACCD = "#1E4E86"; TINT = "#E9F0F8"
INK = "#1A1A1A"; BODY = "#4A4A4A"; GRAY = "#8A8A8A"; LINE = "#D6DBE2"
RED = "#C0392B"; REDT = "#F7E9E7"
CARD_L = "#DCE5F0"
BONE = "#E6E2D8"; BONE_E = "#A9A499"
PER = "#F0C478"; MEN = "#CE8C3C"; PERE = "#A87B32"
FIB = "#BE7A3C"; MAT = "#F4EEE2"
TOOL = "#6A7382"

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

def T(x, y, s, size=24, fill=INK, anchor="middle", weight="400"):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" font-weight="{weight}">{s}</text>')

def box(x, y, w, h, fill, stroke, rx=10, sw=1.5):
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

def poly(pts, fill, stroke="none", sw=1):
    p = " ".join(f"{a},{b}" for a, b in pts)
    return f'<polygon points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


# ---------------- 目录卡 ----------------
def toc():
    s = []
    items = [
        ("1", "一件刚发生的事", "Neuralink 第一次没切开硬脑膜"),
        ("2", "这层膜在哪、和邻居差在哪", "位置与贴合方式"),
        ("3", "它其实是两层", "外层就是颅骨的骨膜"),
        ("4", "有多厚、多硬、有没有方向性", "三组承重数字"),
        ("5", "手术里它怎么被对待", "开颅现场"),
        ("6", "动物身上不是这回事", "大鼠与人差 11 倍"),
    ]
    y = 26
    for n, title, sub in items:
        s.append(box(24, y, 912, 80, "#F7F9FC", CARD_L, 14, 1.5))
        s.append(circ(74, y + 40, 27, TINT, ACC, 1.5))
        s.append(T(74, y + 50, n, 30, ACCD, weight="700"))
        s.append(T(126, y + 35, title, 30, INK, anchor="start", weight="700"))
        s.append(T(126, y + 66, sub, 23, GRAY, anchor="start"))
        y += 94
    return 960, y + 10, "".join(s)


# ---------------- 各向异性 ----------------
def _fiber_sheet(sid, x, y, w, h, ang, nfib=9):
    """带纤维的膜片；ang=0 水平纤维，ang=90 竖直纤维。"""
    s = [f'<clipPath id="{sid}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6"/></clipPath>']
    s.append(box(x, y, w, h, MAT, "#C9C0AE", 6, 1.5))
    s.append(f'<g clip-path="url(#{sid})">')
    if ang == 0:
        step = h / (nfib + 1)
        for i in range(1, nfib + 1):
            yy = y + i * step
            s.append(line(x - 4, yy, x + w + 4, yy, FIB, 7))
    else:
        step = w / (nfib + 1)
        for i in range(1, nfib + 1):
            xx = x + i * step
            s.append(line(xx, y - 4, xx, y + h + 4, FIB, 7))
    s.append('</g>')
    return "".join(s)


def fig_aniso():
    s = []
    s.append(box(24, 18, 912, 54, TINT, ACC, 10, 1.5))
    s.append(T(480, 53, "同一张膜，换个方向拉，刚度差 2.6 倍", 28, ACCD, weight="700"))

    # 上排：两种拉伸方向
    s.append(_fiber_sheet("s1", 150, 118, 210, 210, 0))
    s.append(line(70, 223, 132, 223, INK, 5, None, "ahk"))
    s.append(line(440, 223, 378, 223, INK, 5, None, "ahk"))
    s.append(T(255, 106, "沿纤维方向拉", 26, INK, weight="700"))
    s.append(T(255, 362, "力由胶原纤维承担", 23, BODY))
    s.append(T(255, 392, "193 MPa", 28, ACCD, weight="700"))

    s.append(_fiber_sheet("s2", 600, 118, 210, 210, 90))
    s.append(line(520, 223, 582, 223, INK, 5, None, "ahk"))
    s.append(line(890, 223, 828, 223, INK, 5, None, "ahk"))
    s.append(T(705, 106, "垂直纤维方向拉", 26, INK, weight="700"))
    s.append(T(705, 362, "承力的是纤维间基质", 23, BODY))
    s.append(T(705, 392, "73 MPa", 28, RED, weight="700"))

    # 下排：针的斜面取向
    s.append(box(24, 492, 912, 50, "#FBF7E9", "#D9C98A", 10, 1.5))
    s.append(T(480, 524, "同一根针，斜面刃口转 90°，穿刺力就变了（俯视）", 26, "#8A6D1A", weight="700"))

    s.append(_fiber_sheet("s3", 130, 568, 250, 180, 0))
    s.append(line(200, 658, 310, 658, TOOL, 14))
    s.append(f'<ellipse cx="255" cy="658" rx="13" ry="22" fill="#FFFFFF" stroke="{TOOL}" stroke-width="3"/>')
    s.append(T(255, 782, "刃口顺着纤维", 24, INK, weight="700"))
    s.append(T(255, 812, "更接近沿纤维间劈开，力较小", 22, BODY))

    s.append(_fiber_sheet("s4", 580, 568, 250, 180, 0))
    s.append(line(705, 600, 705, 716, TOOL, 14))
    s.append(f'<ellipse cx="705" cy="658" rx="13" ry="22" fill="#FFFFFF" stroke="{TOOL}" stroke-width="3"/>')
    s.append(T(705, 782, "刃口横切纤维", 24, RED, weight="700"))
    s.append(T(705, 812, "须切断纤维，力与功都更大", 22, BODY))

    s.append(T(480, 856, "橙色 = 胶原纤维束　深灰 = 针的斜面刃口", 21, GRAY))
    return 960, 880, "".join(s)


# ---------------- 开颅：硬膜的去向 ----------------
def _stack(x0, x1, y, with_gap=False, gap_h=0):
    """从上到下：硬膜两层 + 蛛网膜 + 脑。返回 svg 与底部 y。"""
    s = []
    yy = y
    if with_gap:
        s.append(box(x0, yy, x1 - x0, gap_h, REDT, RED, 4, 2))
        yy += gap_h
    s.append(box(x0, yy, x1 - x0, 16, PER, PERE, 3, 1.2))
    s.append(box(x0, yy + 16, x1 - x0, 18, MEN, PERE, 3, 1.2))
    s.append(box(x0, yy + 34, x1 - x0, 10, "#BBD3E6", "#7FA8C9", 3, 1.2))
    s.append(box(x0, yy + 44, x1 - x0, 74, "#E8EAE7", "#B8BCB6", 10, 1.5))
    s.append(T(x0 + 40, yy + 92, "脑", 26, "#5A5F5A"))
    return "".join(s), yy + 118


def _bone(x0, x1, y, h=62):
    s = [box(x0, y, x1 - x0, h, BONE, BONE_E, 5, 1.8)]
    xx = x0 + 18
    while xx < x1 - 14:
        s.append(f'<ellipse cx="{xx}" cy="{y+h/2}" rx="8" ry="6" fill="#CFC8B8"/>')
        xx += 30
    return "".join(s)


def fig_craniotomy():
    s = []
    X0, X1 = 268, 812
    s.append(box(20, 14, 1040, 52, TINT, ACC, 10, 1.5))
    s.append(T(540, 48, "掀开骨瓣时，硬膜整张留在脑这一侧", 27, ACCD, weight="700"))

    def stack(y, gap=0):
        out = []
        yy = y
        if gap:
            out.append(box(X0, yy, X1 - X0, gap, REDT, RED, 4, 2))
            yy += gap
        out.append(box(X0, yy, X1 - X0, 13, PER, PERE, 3, 1.2))
        out.append(box(X0, yy + 13, X1 - X0, 15, MEN, PERE, 3, 1.2))
        out.append(box(X0, yy + 28, X1 - X0, 8, "#BBD3E6", "#7FA8C9", 3, 1.2))
        out.append(box(X0, yy + 36, X1 - X0, 46, "#E8EAE7", "#B8BCB6", 8, 1.5))
        out.append(T(X0 + 30, yy + 66, "脑", 22, "#5A5F5A"))
        return "".join(out)

    def bone(x0, x1, y, h=42):
        out = [box(x0, y, x1 - x0, h, BONE, BONE_E, 5, 1.8)]
        xx = x0 + 16
        while xx < x1 - 12:
            out.append(f'<ellipse cx="{xx}" cy="{y+h/2}" rx="7" ry="5" fill="#CFC8B8"/>')
            xx += 28
        return "".join(out)

    # ① 正常
    s.append(T(24, 106, "① 正常状态", 24, INK, anchor="start", weight="700"))
    s.append(bone(X0, X1, 112))
    s.append(stack(154))
    s.append(T(X1 + 14, 138, "颅骨", 20, BODY, anchor="start"))
    s.append(T(X1 + 14, 166, "骨内膜层", 20, PERE, anchor="start"))
    s.append(T(X1 + 14, 190, "脑膜层", 20, PERE, anchor="start"))
    s.append(T(24, 168, "硬脑膜", 20, PERE, anchor="start"))
    s.append(T(24, 192, "两层贴合", 20, PERE, anchor="start"))

    # ② 铣刀
    s.append(T(24, 288, "② 铣刀锯骨：脚板边锯边剥离硬膜", 24, INK, anchor="start", weight="700"))
    cx = 600
    s.append(bone(X0, cx - 11, 300))
    s.append(bone(cx + 11, X1, 300))
    s.append(stack(342))
    s.append(f'<rect x="{cx-10}" y="248" width="20" height="94" fill="{TOOL}"/>')
    s.append(f'<rect x="{cx-104}" y="328" width="114" height="14" fill="{TOOL}"/>')
    s.append(poly([(cx - 104, 328), (cx - 142, 322), (cx - 142, 338), (cx - 104, 342)], "#59616E"))
    s.append(line(660, 268, 726, 268, INK, 3.5, None, "ahk"))
    s.append(T(736, 275, "铣刀前进方向", 20, BODY, anchor="start"))
    s.append(T(X1 + 14, 350, "脚板伸在骨", 20, TOOL, anchor="start"))
    s.append(T(X1 + 14, 374, "与硬膜之间", 20, TOOL, anchor="start"))

    # ③ 掀开
    s.append(T(24, 474, "③ 骨瓣取走：出现一个本不存在的腔", 24, INK, anchor="start", weight="700"))
    s.append(bone(X0 + 56, X1 - 56, 488, 40))
    s.append(line(X1 + 2, 540, X1 + 2, 494, INK, 3.5, None, "ahk"))
    s.append(T(X1 + 14, 522, "骨瓣被", 20, BODY, anchor="start"))
    s.append(T(X1 + 14, 546, "整块取走", 20, BODY, anchor="start"))
    s.append(stack(552, gap=26))
    s.append(T(24, 580, "硬膜两层", 20, PERE, anchor="start"))
    s.append(T(24, 604, "原封不动", 20, PERE, anchor="start"))
    s.append(T(X1 + 14, 588, "手术制造出来", 20, RED, anchor="start"))
    s.append(T(X1 + 14, 612, "的硬膜外腔", 20, RED, anchor="start"))
    return 1080, 672, "".join(s)


# ---------------- 悬吊线 ----------------
def fig_tackup():
    s = []
    X0, X1 = 120, 760
    SUT = "#B32020"
    s.append(box(24, 18, 912, 54, TINT, ACC, 10, 1.5))
    s.append(T(480, 53, "怎么把一张膜缝到骨头上：在骨上钻孔穿线", 28, ACCD, weight="700"))

    yb = 152
    s.append(_bone(X0, 470, yb, 78))
    s.append(_bone(530, X1, yb, 78))
    s.append(T(500, yb - 22, "开颅缝", 21, GRAY))
    s.append(line(500, yb - 14, 500, yb + 2, GRAY, 1.5))

    # 斜向骨孔
    s.append(poly([(378, yb + 2), (410, yb + 2), (462, yb + 74), (430, yb + 74)],
                  "#FFFFFF", "#8A8A8A", 2))
    s.append(T(316, yb + 44, "骨孔", 22, BODY, anchor="end"))
    s.append(line(326, yb + 38, 380, yb + 30, GRAY, 1.5))

    ys = yb + 110
    st, _ = _stack(X0, X1, ys)
    s.append(st)

    # 缝线：骨外打结 → 穿骨孔 → 硬膜内取一针 → 回穿
    s.append(f'<path d="M398,{yb-6} L452,{yb+74} L478,{ys+8}" stroke="{SUT}" stroke-width="6" fill="none"/>')
    s.append(f'<path d="M478,{ys+8} q28,26 56,0" stroke="{SUT}" stroke-width="6" fill="none"/>')
    s.append(f'<path d="M534,{ys+8} L488,{yb+74} L412,{yb-6}" stroke="{SUT}" stroke-width="6" fill="none"/>')
    s.append(circ(405, yb - 18, 16, SUT, SUT))

    s.append(T(X1 + 18, yb + 8, "缝线在骨", 21, SUT, anchor="start"))
    s.append(T(X1 + 18, yb + 32, "外面打结", 21, SUT, anchor="start"))
    s.append(line(X1 + 12, yb + 2, 424, yb - 16, SUT, 1.2))

    s.append(T(X1 + 18, ys + 12, "在硬膜厚度内", 21, SUT, anchor="start"))
    s.append(T(X1 + 18, ys + 36, "取一针，不穿透", 21, SUT, anchor="start"))
    s.append(line(X1 + 12, ys + 6, 550, ys + 14, SUT, 1.2))

    s.append(box(24, 400, 912, 92, "#FBF7E9", "#D9C98A", 10, 1.5))
    s.append(T(480, 436, "骨头不需要被缝——它只提供一个穿线的孔。", 25, "#8A6D1A", weight="700"))
    s.append(T(480, 470, "线拉紧后把硬膜边缘拽回去贴住骨内板，消灭那个腔。", 23, "#8A6D1A"))
    return 960, 514, "".join(s)


# ---------------- 物种厚度 ----------------
def fig_species():
    s = []
    s.append(box(24, 18, 912, 54, TINT, ACC, 10, 1.5))
    s.append(T(480, 53, "硬脑膜厚度：人比任何动物都厚得多", 28, ACCD, weight="700"))

    data = [("人", 564, ACC), ("马", 313, "#B9C2CC"), ("牛", 311, "#B9C2CC"),
            ("猪", 304, "#5E9E77"), ("山羊", 284, "#B9C2CC"), ("绵羊", 234, "#B9C2CC"),
            ("狗", 233, "#B9C2CC"), ("猫", 201, "#B9C2CC"), ("兔", 99, "#B9C2CC"),
            ("大鼠", 49, RED)]
    x0 = 150; maxw = 620; y = 104
    for name, v, col in data:
        w = maxw * v / 600.0
        s.append(T(132, y + 25, name, 25, INK, anchor="end"))
        s.append(f'<rect x="{x0}" y="{y}" width="{w:.1f}" height="34" rx="4" fill="{col}"/>')
        s.append(T(x0 + w + 12, y + 25, f"{v}", 24,
                   ACCD if col == ACC else (RED if col == RED else BODY), anchor="start",
                   weight="700" if col in (ACC, RED) else "400"))
        y += 46
    s.append(T(480, y + 24, "单位：µm（微米）。同一套组织学方法，34 份样本，10 个物种。", 22, GRAY))

    s.append(box(24, y + 46, 912, 92, "#FBF7E9", "#D9C98A", 10, 1.5))
    s.append(T(480, y + 80, "人 564 µm vs 大鼠 49 µm —— 差 11.5 倍", 26, "#8A6D1A", weight="700"))
    s.append(T(480, y + 114, "而且人、猪、兔可分辨出多个纤维血管层，大鼠只有单一一层。", 22, "#8A6D1A"))
    return 960, y + 156, "".join(s)


FIGS = {"toc": toc, "fig-aniso": fig_aniso, "fig-craniotomy": fig_craniotomy,
        "fig-tackup": fig_tackup, "fig-species": fig_species}


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
