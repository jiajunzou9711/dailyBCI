# -*- coding: utf-8 -*-
"""日报 2026-09-02「ANN 潜层与 EEG 信号在纹理表征上的对齐（下）」: 目录卡 SVG。"""
import os, subprocess, tempfile
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-09-02-texture-alignment-2", "figs")
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
    ("①", "上一期停在哪个问题上"),
    ("②", "三种图片，纹理合成那一种对齐最高"),
    ("③", "纹理特征预测原图，胜过只留物体"),
    ("④", "抠掉背景没有提纯物体信号"),
    ("⑤", "先证明这份 EEG 里确实有物体信息"),
    ("⑥", "物体信息与对齐走进了相反的象限"),
    ("⑦", "对齐的峰值落在刺激后 100 到 200 毫秒"),
    ("⑧", "200 毫秒之后，模型漏掉了一块真实的信号"),
    ("⑨", "裂缝一，改进落在了不参与对齐的地方"),
    ("⑩", "裂缝二，算局部统计在初始化就已发生"),
    ("⑪", "人靠形状认东西，和纹理驱动的对齐不冲突"),
    ("⑫", "这篇削弱了什么，又没削弱什么"),
    ("⑬", "作者自己列的四条局限"),
]


def toc():
    W = 1240
    row_h, gap = 50, 5
    x, y0 = 4, 6
    s = []
    for i, (num, title) in enumerate(TOC_ITEMS):
        y = y0 + i * (row_h + gap)
        s.append(box(x, y, W - 8, row_h, "#F7F9FC", CARD_L, 10, 1.2))
        s.append(box(x + 14, y + 9, 56, 32, TINT, ACC, 8, 1.2))
        s.append(T(x + 42, y + 32, num, 22, ACCD, weight="700"))
        s.append(T(x + 88, y + 32, title, 24, INK, anchor="start"))
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
