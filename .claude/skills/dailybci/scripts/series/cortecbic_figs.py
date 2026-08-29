# -*- coding: utf-8 -*-
"""日报 2026-08-29「CorTec Brain Interchange–BCI2000」: 目录卡 SVG。"""
import os, subprocess, tempfile
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-08-29-cortec-bic-closed-loop", "figs")
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
    ("①", "少刺激反而更好，这是闭环的理由"),
    ("②", "论文的产出是一套公用的基础设施"),
    ("③", "闭环最快 22 ms，阻抗只能看趋势"),
    ("④", "一台主机，接过三种电极配置"),
    ("⑤", "通道失效多为机械原因"),
    ("⑥", "植入两年后仍能读出任务相关响应"),
    ("⑦", "闭环怎么配：任意两个位点当触发源"),
    ("⑧", "输出越过阈值线，刺激随即发出"),
    ("⑨", "在体最好的记录配置与台架上相反"),
    ("⑩", "人体这一步验的是采集链路加软件"),
    ("⑪", "数据、代码、手术流程全部公开"),
    ("⑫", "局限性"),
]


def toc():
    W = 1240
    row_h, gap = 58, 7
    x, y0 = 4, 6
    s = []
    for i, (num, title) in enumerate(TOC_ITEMS):
        y = y0 + i * (row_h + gap)
        s.append(box(x, y, W - 8, row_h, "#F7F9FC", CARD_L, 10, 1.2))
        s.append(box(x + 14, y + 11, 62, 36, TINT, ACC, 8, 1.2))
        s.append(T(x + 45, y + 38, num, 24, ACCD, weight="700"))
        s.append(T(x + 96, y + 38, title, 26, INK, anchor="start"))
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
