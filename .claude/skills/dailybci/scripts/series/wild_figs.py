# -*- coding: utf-8 -*-
"""日报 2026-08-31「WILD 无线闭环平台」: 目录卡 SVG。"""
import os, subprocess, tempfile
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-08-31-wild-wireless-closed-loop", "figs")
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
    ("①", "因果只能靠在事件发生时打断它"),
    ("②", "能做闭环的场景与值得做的不重叠"),
    ("③", "判断必须跟着动物走"),
    ("④", "上板之后，直觉方案是滤波加阈值"),
    ("⑤", "阈值检测器在动物活动时失效"),
    ("⑥", "所以要上模型，但模型必须塞进 10 ms"),
    ("⑦", "CNN 降采样，GRU 抓时间结构"),
    ("⑧", "去噪后的在线检测接近离线水平"),
    ("⑨", "判断做出来还要能发光"),
    ("⑩", "SWR 真的被打断了"),
    ("⑪", "同一套机制，输入换成行为"),
    ("⑫", "三个预算互相牵制"),
    ("⑬", "局限性"),
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
