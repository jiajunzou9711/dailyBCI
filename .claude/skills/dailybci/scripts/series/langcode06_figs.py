# -*- coding: utf-8 -*-
"""日报 2026-08-26「语言的神经群体编码」第六期：目录卡 + 两张自制 SVG。"""
import os, subprocess, tempfile
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-08-26-langcode-06", "figs")
os.makedirs(OUT, exist_ok=True)

ACC = "#2F6DB5"; ACCD = "#1E4E86"; TINT = "#E9F0F8"
INK = "#1A1A1A"; GRAY = "#8A8A8A"; CARD_L = "#DCE5F0"
WARM = "#C2542F"; WARM_T = "#F7EAE4"; BG = "#FAFAFA"
NEU = "#F4F4F4"; NEU_S = "#CFCFCF"


def T(x, y, s, size=25, fill=INK, anchor="middle", weight="400"):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" font-weight="{weight}">{s}</text>')


def box(x, y, w, h, fill, stroke, rx=12, sw=1.5):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')


_ar = [0]
def arrow(x1, y1, x2, y2, col=GRAY, sw=2.4, dash=None):
    _ar[0] += 1; i = _ar[0]
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<defs><marker id="m{i}" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            f'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="{col}"/></marker></defs>'
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" '
            f'stroke-width="{sw}"{d} marker-end="url(#m{i})"/>')


TOC_ITEMS = [
    ("①②", "起点与预备", "听懂对方这件事，以及「嵌入」到底是什么"),
    ("③④", "问题定位", "对齐发生在几何这一层，怎么把它变成能做的实验"),
    ("⑤–⑧", "实验一 · 换语言", "三语版《小王子》，112 人，跨语言互相预测"),
    ("⑨–⑪", "实验二三 · 真实对话", "双人颅内同步记录与 fMRI 超扫描"),
    ("⑫⑬", "收口", "LLM 的三个角色，落点与强度边界"),
]


def toc():
    s = []; W = 1000
    row_h, gap = 96, 14
    x, y0 = 4, 6
    for i, (num, sec, desc) in enumerate(TOC_ITEMS):
        y = y0 + i * (row_h + gap)
        s.append(box(x, y, 992, row_h, "#F7F9FC", CARD_L, 12, 1.4))
        s.append(box(x + 18, y + 22, 132, 52, TINT, ACC, 10, 1.4))
        s.append(T(x + 84, y + 57, num, 24, ACCD, weight="700"))
        s.append(T(x + 170, y + 46, sec, 25, ACCD, anchor="start", weight="700"))
        s.append(T(x + 170, y + 78, desc, 23, INK, anchor="start"))
    return W, y0 + len(TOC_ITEMS) * (row_h + gap), "".join(s)


# ② 嵌入：one-hot -> 稠密向量 -> 相对结构
def fig_embedding():
    W, H = 1000, 600
    s = []
    # 左：one-hot
    s.append(box(20, 14, 400, 232, "#FFFFFF", NEU_S, 12, 1.4))
    s.append(T(220, 50, "one-hot", 25, GRAY, weight="700"))
    words = ["queen", "king", "refrigerator"]
    hot = [2, 5, 7]
    for r, (w, h) in enumerate(zip(words, hot)):
        y = 74 + r * 46
        s.append(T(138, y + 24, w, 22, INK, anchor="end"))
        for c in range(10):
            fill = ACC if c == h else "#FFFFFF"
            s.append(f'<rect x="{152 + c*25}" y="{y}" width="21" height="30" rx="3" '
                     f'fill="{fill}" stroke="{NEU_S}" stroke-width="1.2"/>')
    s.append(T(220, 232, "两两距离全部相等", 22, WARM, weight="700"))

    s.append(arrow(438, 130, 512, 130, GRAY, 3))
    s.append(T(475, 108, "训练", 20, GRAY))

    # 右：稠密向量
    s.append(box(530, 14, 450, 232, "#FFFFFF", ACC, 12, 1.6))
    s.append(T(755, 50, "嵌入（稠密向量）", 25, ACCD, weight="700"))
    vals = [["0.31", "-0.72", "0.08", "0.55", "…"],
            ["0.28", "-0.66", "0.11", "0.61", "…"],
            ["-0.44", "0.19", "0.73", "-0.02", "…"]]
    for r, (w, row) in enumerate(zip(words, vals)):
        y = 74 + r * 46
        s.append(T(648, y + 24, w, 22, INK, anchor="end"))
        for c, v in enumerate(row):
            s.append(T(682 + c * 58, y + 24, v, 20, ACCD, anchor="start"))
    s.append(T(755, 232, "距离带上了结构", 22, ACCD, weight="700"))

    # 下：平行四边形
    ox, oy = 300, 540
    s.append(arrow(ox, oy, 760, oy, INK, 2.4))
    s.append(arrow(ox, oy, ox, 292, INK, 2.4))
    s.append(T(775, oy + 8, "维度 x", 21, GRAY, anchor="start"))
    s.append(T(ox, 282, "维度 y", 21, GRAY))
    pts = {"man": (398, 452), "king": (568, 396), "woman": (466, 512), "queen": (636, 456)}
    for (a, b), col in [(("man", "king"), ACC), (("woman", "queen"), ACC),
                        (("man", "woman"), CARD_L), (("king", "queen"), CARD_L)]:
        x1, y1 = pts[a]; x2, y2 = pts[b]
        s.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" '
                 f'stroke-width="2.4" stroke-dasharray="7,5"/>')
    for name, (px, py) in pts.items():
        s.append(f'<circle cx="{px}" cy="{py}" r="8" fill="{ACCD}"/>')
        dx, dy = (14, -12) if name in ("king", "queen") else (-16, 8)
        anc = "start" if name in ("king", "queen") else "end"
        s.append(T(px + dx, py + dy, name, 23, INK, anchor=anc, weight="700"))
    s.append(box(690, 296, 296, 76, TINT, ACC, 10, 1.4))
    s.append(T(838, 328, "man→king 的方向", 21, ACCD, weight="700"))
    s.append(T(838, 356, "与 woman→queen 大致相同", 21, ACCD))
    return W, H, "".join(s)


# ⑨ 双人颅内的时间顺序
def fig_timing():
    W, H = 1000, 430
    s = []
    mx = 520
    s.append(f'<line x1="{mx}" y1="52" x2="{mx}" y2="392" stroke="{WARM}" '
             f'stroke-width="2.6" stroke-dasharray="7,5"/>')
    s.append(T(mx, 38, "这个词被说出来的时刻", 23, WARM, weight="700"))

    def bump(cx, y, col, tint):
        w = 150
        d = (f'M {cx-w} {y} C {cx-w*0.45} {y} {cx-w*0.42} {y-92} {cx} {y-92} '
             f'C {cx+w*0.42} {y-92} {cx+w*0.45} {y} {cx+w} {y} Z')
        return (f'<path d="{d}" fill="{tint}" stroke="{col}" stroke-width="2.6"/>')

    # 说者
    s.append(T(40, 130, "说者", 26, ACCD, anchor="start", weight="700"))
    s.append(f'<line x1="150" y1="196" x2="960" y2="196" stroke="{NEU_S}" stroke-width="2"/>')
    s.append(bump(430, 196, ACC, TINT))
    s.append(T(430, 226, "发音之前", 22, ACCD, weight="700"))

    # 听者
    s.append(T(40, 300, "听者", 26, WARM, anchor="start", weight="700"))
    s.append(f'<line x1="150" y1="366" x2="960" y2="366" stroke="{NEU_S}" stroke-width="2"/>')
    s.append(bump(650, 366, WARM, WARM_T))
    s.append(T(650, 396, "词起始之后", 22, WARM, weight="700"))

    s.append(T(880, 150, "时间", 21, GRAY))
    s.append(arrow(820, 158, 940, 158, GRAY, 2.2))
    return W, H, "".join(s)


def render_svg(name, w, h, inner):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
           f'viewBox="0 0 {w} {h}"><rect width="{w}" height="{h}" fill="{BG}"/>{inner}</svg>')
    html = (f'<html><head><meta charset="utf-8"><style>'
            f'@font-face{{font-family:HS;src:url("file://{FONT}");}}'
            f'*{{font-family:HS,Helvetica,Arial,sans-serif;}}'
            f'body{{margin:0;background:{BG};}}</style></head><body>{svg}</body></html>')
    tmp = tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8")
    tmp.write(html); tmp.close()
    out = os.path.join(OUT, name)
    subprocess.run(["npx", "playwright", "screenshot", "--full-page",
                    f"--viewport-size={w},{h}", f"file://{tmp.name}", out],
                   check=True, capture_output=True)
    os.unlink(tmp.name)
    print("wrote", out, Image.open(out).size)


def main():
    for name, fn in [("toc.png", toc), ("fig-embedding.png", fig_embedding),
                     ("fig-timing.png", fig_timing)]:
        w, h, inner = fn()
        render_svg(name, w, h, inner)


if __name__ == "__main__":
    main()
