# -*- coding: utf-8 -*-
"""日报 2026-09-01「DNN–脑对齐由纹理统计驱动（上）」: 目录卡 SVG。"""
import os, subprocess, tempfile
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-09-01-texture-alignment", "figs")
os.makedirs(OUT, exist_ok=True)

ACC = "#2F6DB5"; ACCD = "#1E4E86"; TINT = "#E9F0F8"
INK = "#1A1A1A"; CARD_L = "#DCE5F0"; BG = "#FAFAFA"


def T(x, y, s, size=25, fill=INK, anchor="middle", weight="400"):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" font-weight="{weight}">{s}</text>')


def box(x, y, w, h, fill, stroke, rx=10, sw=1.4):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')


TOC_ITEMS = [
    ("①", "网络与皮层的相似，比的是表征几何"),
    ("②", "两个观测撑不住「共享物体识别计算」"),
    ("③", "识别准确率与脑预测力基本脱钩"),
    ("④", "权重完全没训练的网络，也能预测出一部分脑响应"),
    ("⑤", "对齐分数是一个总量，问题在于哪个成分撑着它"),
    ("⑥", "把两种成分拆开，看对齐跟着哪一个走"),
    ("⑦", "三种图片，每种只保留一部分成分"),
    ("⑧", "被试只是看图，模型只是被跑一遍"),
    ("⑨", "两边都换算成「这 200 张图彼此有多不像」"),
    ("⑩", "AUC 要除以噪声天花板才能读"),
    ("⑪", "答案是纹理统计，但要说清它否掉了什么"),
]


def toc():
    W = 1240
    row_h, gap = 54, 6
    x, y0 = 4, 6
    s = []
    for i, (num, title) in enumerate(TOC_ITEMS):
        y = y0 + i * (row_h + gap)
        s.append(box(x, y, W - 8, row_h, "#F7F9FC", CARD_L, 10, 1.2))
        s.append(box(x + 14, y + 10, 58, 34, TINT, ACC, 8, 1.2))
        s.append(T(x + 43, y + 35, num, 23, ACCD, weight="700"))
        s.append(T(x + 90, y + 35, title, 25, INK, anchor="start"))
    return W, y0 + len(TOC_ITEMS) * (row_h + gap), "".join(s)


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


if __name__ == "__main__":
    render_svg("toc.png", *toc())
