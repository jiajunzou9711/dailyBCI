"""Neuropixels Quad Base 期(2026-07-30)自制示意图。
六张:目录 / 三种取舍 / 两类量的分界 / 两个「加」 / 8x8 针脚对覆盖矩阵 / 三条扩容路线。
"""
import os, subprocess, tempfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-07-30-quadbase", "figs")
os.makedirs(OUT, exist_ok=True)

ACC = "#2F6DB5"; ACCD = "#1E4E86"; TINT = "#E9F0F8"
INK = "#1A1A1A"; BODY = "#4A4A4A"; GRAY = "#8A8A8A"; LINE = "#D6DBE2"
RED = "#C0392B"; REDT = "#F7E9E7"; GRN = "#2E7D57"; GRNT = "#E7F2EC"
CARD_L = "#DCE5F0"; PALE = "#EFF1F4"; PALE_L = "#D9DDE3"

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


def shank(x, y, h, w, fill, stroke, sw=1.2):
    """一根针脚:细长圆角矩形。"""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{w/2}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')


# ---------- 1. 目录 ----------
def toc():
    s = []
    items = [
        ("1", "一个你做过的取舍", "通道有限:集中、摊开,还是分次拼起来"),
        ("2", "为什么跨区的量特殊", "它定义在逐试次的协同波动上"),
        ("3", "作者怎么设计这个回答", "从同一份记录里抽子集当对照"),
        ("4", "答案:一次胜过四次", "「对」是平方增长,实验次数只能线性叠加"),
        ("5", "偏差有方向", "少通道会系统性低估脑区之间的耦合"),
        ("6", "三条扩容路线的分工", "增加通道、增加视野、增加数据量"),
    ]
    y = 30
    for n, title, sub in items:
        s.append(box(30, y, 900, 78, "#F7F9FC", CARD_L, 14, 1.5))
        s.append(circ(78, y + 39, 26, TINT, ACC, 1.5))
        s.append(T(78, y + 49, n, 30, ACCD, weight="700"))
        s.append(T(126, y + 34, title, 30, INK, anchor="start", weight="700"))
        s.append(T(126, y + 64, sub, 22, GRAY, anchor="start"))
        y += 92
    return 960, y, "".join(s)


# ---------- 2. 三种取舍 ----------
def fig_tradeoff():
    s = []
    s.append(box(30, 22, 900, 58, TINT, ACC, 12, 1.5))
    s.append(T(480, 58, "同时只有 384 个通道可用,于是覆盖多个脑区只有三条路", 25, ACCD, weight="700"))

    # 三个面板
    px = [60, 375, 690]
    titles = ["集中在一根针脚", "摊到四根针脚", "分四次记录再拼"]
    subs = ["沿深度采得最密", "每根变稀", "每次换一个位置"]
    for k, x0 in enumerate(px):
        s.append(box(x0, 110, 210, 300, "#FCFCFD", LINE, 12, 1.2))
        s.append(T(x0 + 105, 148, titles[k], 25, INK, weight="700"))
        s.append(T(x0 + 105, 178, subs[k], 21, GRAY))
        if k == 0:
            for i in range(4):
                xx = x0 + 34 + i * 46
                s.append(shank(xx, 200, 180, 18, TINT if i else ACC, ACC if i == 0 else PALE_L))
            s.append(T(x0 + 105, 400, "只有 1 根在读", 21, ACCD))
        elif k == 1:
            for i in range(4):
                xx = x0 + 34 + i * 46
                s.append(shank(xx, 200, 180, 18, TINT, PALE_L))
                s.append(box(xx, 200, 18, 45, ACC, ACC, 9, 0))
            s.append(T(x0 + 105, 400, "4 根各读一小段", 21, ACCD))
        else:
            for j in range(2):
                yy = 206 + j * 94
                s.append(T(x0 + 18, yy + 44, f"第{j+1}次", 19, GRAY, anchor="start"))
                for i in range(4):
                    xx = x0 + 82 + i * 32
                    on = (i == j * 2) or (i == j * 2 + 1)
                    s.append(shank(xx, yy, 72, 14, ACC if on else TINT,
                                   ACC if on else PALE_L))
            s.append(T(x0 + 105, 400, "共四次,示意画两次", 21, GRAY))

    s.append(box(60, 432, 840, 62, "#FBF7E9", "#D9C98A", 12, 1.5))
    s.append(T(480, 458, "第三条是领域里使用最广的做法:不加硬件,靠多做几次实验换覆盖面", 22, "#8A6D1A"))
    s.append(T(480, 484, "这篇论文算清了它的代价", 22, "#8A6D1A"))
    return 960, 516, "".join(s)


# ---------- 3. 两类量的分界 ----------
def fig_twokinds():
    s = []
    s.append(box(30, 22, 900, 58, TINT, ACC, 12, 1.5))
    s.append(T(480, 58, "分次记录能不能拼,取决于你要的量属于哪一类", 25, ACCD, weight="700"))

    # 第一类
    s.append(box(50, 104, 860, 168, GRNT, GRN, 12, 1.5))
    s.append(T(76, 140, "第一类:只需要每个神经元各自的平均反应", 26, GRN, anchor="start", weight="700"))
    s.append(T(76, 178, "单神经元调谐曲线 / 试次平均的群体几何 / 按条件解码", 23, BODY, anchor="start"))
    s.append(T(76, 216, "与「谁和谁被同时记录」无关", 23, BODY, anchor="start"))
    s.append(box(640, 190, 240, 56, "#FFFFFF", GRN, 10, 1.5))
    s.append(T(760, 226, "分次记录再拼可行", 23, GRN, weight="700"))

    # 第二类
    s.append(box(50, 292, 860, 200, REDT, RED, 12, 1.5))
    s.append(T(76, 328, "第二类:问两个神经元在同一时刻是否一起波动", 26, RED, anchor="start", weight="700"))
    s.append(T(76, 366, "Granger 因果 / 噪声相关 / 跨脑区共享的潜在维度", 23, BODY, anchor="start"))
    s.append(T(76, 404, "定义在逐试次的协同波动上,两者没被同时记录,", 23, BODY, anchor="start"))
    s.append(T(76, 434, "这个量就没有数值可算", 23, BODY, anchor="start"))
    s.append(box(640, 408, 240, 56, "#FFFFFF", RED, 10, 1.5))
    s.append(T(760, 444, "只能靠同时记录", 23, RED, weight="700"))
    return 960, 516, "".join(s)


# ---------- 4. 两个「加」 ----------
def fig_twoadds():
    s = []
    s.append(box(30, 22, 900, 58, TINT, ACC, 12, 1.5))
    s.append(T(480, 58, "说到「把多次记录加起来」,领域内与本文指的是两件事", 25, ACCD, weight="700"))

    # 左:伪群体
    s.append(box(50, 104, 410, 330, "#FCFCFD", LINE, 12, 1.5))
    s.append(T(255, 142, "伪群体", 28, ACCD, weight="700"))
    s.append(T(255, 174, "pseudo-population", 20, GRAY))
    s.append(T(255, 216, "把不同 session 里", 22, BODY))
    s.append(T(255, 244, "同一条件的试次配对", 22, BODY))
    s.append(T(255, 272, "造出共同时间轴", 22, BODY))
    s.append(box(76, 296, 358, 50, GRNT, GRN, 10, 1.2))
    s.append(T(255, 328, "条件平均反应保住了", 22, GRN, weight="700"))
    s.append(box(76, 356, 358, 62, REDT, RED, 10, 1.2))
    s.append(T(255, 382, "跨神经元的逐试次", 21, RED))
    s.append(T(255, 408, "协同波动被置为零", 21, RED, weight="700"))

    # 右:本文的加
    s.append(box(500, 104, 410, 330, "#FCFCFD", LINE, 12, 1.5))
    s.append(T(705, 142, "本文的「加」", 28, ACCD, weight="700"))
    s.append(T(705, 174, "把四个连接数相加", 20, GRAY))
    s.append(T(705, 216, "四次记录各自在自己的", 22, BODY))
    s.append(T(705, 244, "神经元集合内部数连接", 22, BODY))
    s.append(T(705, 272, "再把四个数字相加", 22, BODY))
    s.append(box(526, 296, 358, 50, GRNT, GRN, 10, 1.2))
    s.append(T(705, 328, "四份名单没有重复项", 22, GRN, weight="700"))
    s.append(box(526, 356, 358, 62, "#FBF7E9", "#D9C98A", 10, 1.2))
    s.append(T(705, 382, "对分次方案最宽容:", 21, "#8A6D1A"))
    s.append(T(705, 408, "假设四次之间无漂移损失", 21, "#8A6D1A", weight="700"))

    s.append(T(480, 476, "前者合并的是神经元,后者合并的是计数", 24, INK, weight="700"))
    return 960, 508, "".join(s)


# ---------- 5. 8x8 针脚对覆盖矩阵 ----------
def fig_matrix():
    s = []
    s.append(box(30, 22, 900, 58, TINT, ACC, 12, 1.5))
    s.append(T(480, 58, "8 根针脚两两配对共 36 类,分次方案只能测到 12 类", 25, ACCD, weight="700"))

    labs = ["A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4"]
    cell = 46
    x0, y0 = 250, 130
    # 表头
    for i, L in enumerate(labs):
        s.append(T(x0 + i * cell + cell / 2, y0 - 12, L, 21, ACCD if L[0] == "A" else GRN))
        s.append(T(x0 - 14, y0 + i * cell + cell / 2 + 7, L, 21,
                   ACCD if L[0] == "A" else GRN, anchor="end"))
    # 格子(上三角 + 对角线)
    covered = {(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
               (0, 4), (1, 5), (2, 6), (3, 7)}
    for r in range(8):
        for c in range(r, 8):
            xx = x0 + c * cell
            yy = y0 + r * cell
            if (r, c) in covered:
                s.append(box(xx, yy, cell - 4, cell - 4, ACC, ACCD, 6, 1.2))
            else:
                s.append(box(xx, yy, cell - 4, cell - 4, PALE, PALE_L, 6, 1.2))
    # 图例
    ly = y0 + 8 * cell + 30
    s.append(box(250, ly, 30, 30, ACC, ACCD, 6, 1.2))
    s.append(T(294, ly + 22, "四次分次记录可测:12 类", 23, INK, anchor="start"))
    s.append(box(250, ly + 44, 30, 30, PALE, PALE_L, 6, 1.2))
    s.append(T(294, ly + 66, "只有一次同时记录可测:24 类", 23, INK, anchor="start"))

    s.append(T(150, y0 + 2 * cell + 8, "探针 1", 22, ACCD))
    s.append(T(150, y0 + 6 * cell + 8, "探针 2", 22, GRN))
    return 960, ly + 110, "".join(s)


# ---------- 6. 三条扩容路线 ----------
def fig_threeroutes():
    s = []
    s.append(box(30, 22, 900, 58, TINT, ACC, 12, 1.5))
    s.append(T(480, 58, "扩大记录规模有三条路线,它们扩大的东西不同", 25, ACCD, weight="700"))

    rows = [
        ("硬件:加同时通道", "可测的神经元对数与达标脑区数", "硅面积、外围硬件、穿刺创伤", ACC, TINT),
        ("成像:换记录物理量", "神经元总数(约 100 万)", "时间分辨率不到动作电位层级", GRN, GRNT),
        ("模型:跨 session 建模", "可利用的数据量", "恢复的是潜在空间层面的结构", "#8A6D1A", "#FBF7E9"),
    ]
    y = 108
    for name, gain, cost, col, tint in rows:
        s.append(box(50, y, 860, 122, tint, col, 12, 1.5))
        s.append(T(76, y + 42, name, 26, col, anchor="start", weight="700"))
        s.append(T(76, y + 82, "扩大了", 21, GRAY, anchor="start"))
        s.append(T(150, y + 82, gain, 23, INK, anchor="start", weight="700"))
        s.append(T(76, y + 110, "代价", 21, GRAY, anchor="start"))
        s.append(T(150, y + 110, cost, 22, BODY, anchor="start"))
        y += 134

    s.append(T(480, y + 34, "选哪条,取决于你要问的量属于前面说的哪一类", 24, INK, weight="700"))
    return 960, y + 62, "".join(s)


FIGS = {"toc": toc, "fig-tradeoff": fig_tradeoff, "fig-twokinds": fig_twokinds,
        "fig-twoadds": fig_twoadds, "fig-matrix": fig_matrix,
        "fig-threeroutes": fig_threeroutes}


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
