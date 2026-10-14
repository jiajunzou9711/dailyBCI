# -*- coding: utf-8 -*-
"""日报 2026-10-14「小鼠 M2 的觅食决策变量储备库」(Cazettes 2023 Nat Neurosci)：目录卡、论文裁图归档。
源图：papers/cazettes-2023-*.png（600 dpi 页面渲染后按墨迹包围盒裁出、必要时拼版）。"""
import os, shutil, subprocess, tempfile
from PIL import Image

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
PAP = os.path.join(PROJECT, "papers")
OUT = os.path.join(PROJECT, "output", "2026-10-14-foraging-dv-reservoir", "figs")
os.makedirs(OUT, exist_ok=True)
BG = "#FAFAFA"
ACC = "#2F6DB5"; ACCD = "#1E4E86"; TINT = "#E9F0F8"; INK = "#1A1A1A"; GRAY = "#666666"
CARD_L = "#DCE5F0"

CROPS = ["cover", "fig1a", "fig1a-run", "fig1bc", "fig1gh", "fig2af", "fig3acg", "fig4ac", "fig4eg",
         "fig5abde", "fig5fg", "fig6efg", "fig6hi", "fig7ce", "fig8ac", "ed8bd"]


def T(x, y, s, size=25, fill=INK, anchor="middle", weight="400"):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" font-weight="{weight}">{s}</text>')


def box(x, y, w, h, fill, stroke, rx=10, sw=1.4):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')


TOC1 = [
    ("①", "旧认知", "大脑只计算当前策略所用的那一个 DV"),
    ("②", "任务与行为", "同一串结果可算出两种 DV，小鼠各用其一"),
    ("③", "记录与抑制", "M2 编码离开决策，抑制 M2 后预测变差"),
]
TOC2 = [
    ("回顾", "上篇要点", "任务、两种 DV 与 M2"),
    ("④", "核心结果", "被采用与未被采用的 DV 都在 M2 中被编码"),
    ("⑤", "边界", "M2 编码一族觅食计算，任意信号读不出"),
    ("⑥", "闭环", "回到旧认知，与已有研究的关系"),
    ("⑦", "局限性", "证据强度与适用范围"),
]


def toc(TOC):
    W = 960; row_h, gap = 84, 10; x, y0 = 4, 6; s = []
    for i, (num, title, sub) in enumerate(TOC):
        y = y0 + i * (row_h + gap)
        s.append(box(x, y, W - 8, row_h, "#F7F9FC", CARD_L, 10, 1.2))
        s.append(box(x + 14, y + 20, 62, 44, TINT, ACC, 8, 1.2))
        s.append(T(x + 45, y + 51, num, 28 if len(num) == 1 else 24, ACCD, weight="700"))
        s.append(T(x + 96, y + 37, title, 30, INK, anchor="start", weight="700"))
        s.append(T(x + 96, y + 71, sub, 24, GRAY, anchor="start"))
    return W, y0 + len(TOC) * (row_h + gap), "".join(s)


def render_svg(name, w, h, inner):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{2*w}" height="{2*h}" '
           f'viewBox="0 0 {w} {h}"><rect width="{w}" height="{h}" fill="{BG}"/>{inner}</svg>')
    html = (f'<html><head><meta charset="utf-8"><style>'
            f'@font-face{{font-family:HS;src:url("file://{FONT}");}}'
            f'*{{font-family:Helvetica,HS,Arial,sans-serif;}}'
            f'body{{margin:0;background:{BG};}}</style></head><body>{svg}</body></html>')
    tmp = tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8")
    tmp.write(html); tmp.close()
    out = os.path.join(OUT, name)
    subprocess.run(["npx", "playwright", "screenshot", "--full-page",
                    f"--viewport-size={2*w},{2*h}", f"file://{tmp.name}", out],
                   check=True, capture_output=True)
    os.unlink(tmp.name)
    print("wrote", out, Image.open(out).size)


if __name__ == "__main__":
    for c in CROPS:
        shutil.copy(os.path.join(PAP, f"cazettes-2023-{c}.png"), os.path.join(OUT, f"{c}.png"))
    render_svg("toc1.png", *toc(TOC1))
    render_svg("toc2.png", *toc(TOC2))
