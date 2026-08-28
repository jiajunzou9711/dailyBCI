# -*- coding: utf-8 -*-
"""日报 2026-08-28「语言的神经群体编码」第八期(终): 目录卡 + 自制对照 SVG。"""
import os, subprocess, tempfile
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-08-28-langcode-08", "figs")
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


def panel(x, y, w, h, title, col, tint):
    return (box(x, y, w, h, tint, col, 14, 1.8) +
            T(x + w / 2, y + 40, title, 26, col, weight="700"))


TOC_ITEMS = [
    ("①", "起点", "「AI 像不像大脑」被当成一道是非题"),
    ("②", "相同的部分", "表征格式与学习目标"),
    ("③–⑧", "不同的部分", "五条学习条件：数据量／模态／干预／目标／效率"),
    ("⑨", "作者给的方向", "互补记忆系统、控制系统、生态约束"),
    ("⑩–⑬", "收束", "同一批计算原理、黑箱之辩、结论与评估"),
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


# ④ 数据量
def fig_data():
    W, H = 1000, 400
    s = []
    s.append(panel(20, 14, 460, 370, "人", WARM, WARM_T))
    s.append(box(180, 150, 140, 100, "#FFFFFF", WARM, 10, 2))
    s.append(T(250, 214, "一个童年", 30, WARM, weight="700"))
    s.append(T(250, 300, "开始流利使用语言之前", 21, INK))
    s.append(T(250, 332, "接触到的语言输入量有限", 21, INK))

    s.append(panel(520, 14, 460, 370, "大语言模型", ACC, TINT))
    s.append(box(590, 150, 320, 100, "#FFFFFF", ACC, 10, 2))
    s.append(T(750, 214, "数千年的阅读量", 30, ACCD, weight="700"))
    s.append(T(750, 300, "一个人要读完新一代 GPT 的", 21, INK))
    s.append(T(750, 332, "训练文本，需要数千年", 21, INK))
    return W, H, "".join(s)


# ⑤ 模态
def fig_modality():
    W, H = 1000, 400
    s = []
    s.append(panel(20, 14, 460, 370, "人：多模态", WARM, WARM_T))
    labs = ["语音", "视觉场景", "动作", "触觉", "表情与指向"]
    for i, lab in enumerate(labs):
        x = 60 + (i % 3) * 130; y = 110 + (i // 3) * 78
        s.append(box(x, y, 116, 56, "#FFFFFF", WARM, 10, 1.6))
        s.append(T(x + 58, y + 36, lab, 21, WARM, weight="700"))
    s.append(T(250, 330, "词的意义在与世界的接触中锚定", 21, INK))

    s.append(panel(520, 14, 460, 370, "模型：只有文本", ACC, TINT))
    s.append(box(690, 130, 120, 56, "#FFFFFF", ACC, 10, 1.6))
    s.append(T(750, 166, "文本", 21, ACCD, weight="700"))
    s.append(T(750, 250, "意义完全由词与词之间的", 21, INK))
    s.append(T(750, 282, "共现关系确定", 21, INK))
    return W, H, "".join(s)


# ⑥ 观察 vs 干预
def fig_intervene():
    W, H = 1000, 420
    s = []
    s.append(panel(20, 14, 460, 390, "婴儿：干预", WARM, WARM_T))
    s.append(f'<circle cx="150" cy="200" r="34" fill="#FFFFFF" stroke="{WARM}" stroke-width="2.6"/>')
    s.append(T(150, 262, "婴儿", 21, INK))
    s.append(f'<circle cx="350" cy="200" r="34" fill="#FFFFFF" stroke="{WARM}" stroke-width="2.6"/>')
    s.append(T(350, 262, "环境", 21, INK))
    s.append(arrow(190, 186, 310, 186, WARM, 3))
    s.append(T(250, 168, "扰动", 20, WARM, weight="700"))
    s.append(arrow(310, 220, 190, 220, GRAY, 2.4))
    s.append(T(250, 244, "观察后果", 20, GRAY))
    s.append(T(250, 336, "能分离出因果方向", 22, WARM, weight="700"))

    s.append(panel(520, 14, 460, 390, "模型：只能观察", ACC, TINT))
    s.append(f'<circle cx="650" cy="200" r="34" fill="#FFFFFF" stroke="{ACC}" stroke-width="2.6"/>')
    s.append(T(650, 262, "模型", 21, INK))
    s.append(f'<circle cx="850" cy="200" r="34" fill="#FFFFFF" stroke="{ACC}" stroke-width="2.6"/>')
    s.append(T(850, 262, "文本", 21, INK))
    s.append(arrow(810, 200, 690, 200, ACC, 3))
    s.append(T(750, 178, "被动接收", 20, ACCD, weight="700"))
    s.append(T(750, 336, "只能得到相关", 22, ACCD, weight="700"))
    return W, H, "".join(s)


# ⑨ 三个方向
def fig_directions():
    W, H = 1000, 310
    s = []
    items = [("互补记忆系统", "海马快速记单次事件", "新皮层慢速沉淀统计规律"),
             ("控制系统", "在表征之上再加一层", "负责选择、门控与抽象关系"),
             ("更生态的约束", "给网络设置先天结构", "而不是全部从零学起")]
    for i, (t, a, b) in enumerate(items):
        x = 20 + i * 327
        s.append(box(x, 14, 306, 282, TINT, ACC, 14, 1.8))
        s.append(box(x + 118, 36, 70, 46, "#FFFFFF", ACC, 10, 1.6))
        s.append(T(x + 153, 68, f"{i+1}", 26, ACCD, weight="700"))
        s.append(T(x + 153, 136, t, 26, ACCD, weight="700"))
        s.append(T(x + 153, 204, a, 21, INK))
        s.append(T(x + 153, 240, b, 21, INK))
    return W, H, "".join(s)


# ⑫ 相同两处 / 不同五条
def fig_summary():
    W, H = 1000, 440
    s = []
    s.append(box(20, 14, 960, 170, TINT, ACC, 14, 1.8))
    s.append(T(60, 58, "相同的两处", 28, ACCD, anchor="start", weight="700"))
    for i, (k, v) in enumerate([("表征格式", "语言的各个层级是同一空间里的方向"),
                                ("学习目标", "预测序列里的下一个输入")]):
        y = 106 + i * 42
        s.append(T(80, y, k, 23, ACCD, anchor="start", weight="700"))
        s.append(T(260, y, v, 22, INK, anchor="start"))

    s.append(box(20, 202, 960, 176, WARM_T, WARM, 14, 1.8))
    s.append(T(60, 246, "不同的五条", 28, WARM, anchor="start", weight="700"))
    conds = ["数据量", "模态", "能否干预", "学习目标的丰富度", "数据效率"]
    for i, c in enumerate(conds):
        x = 60 + (i % 3) * 300; y = 286 + (i // 3) * 52
        s.append(box(x, y, 270, 40, "#FFFFFF", WARM, 8, 1.4))
        s.append(T(x + 135, y + 28, c, 22, WARM, weight="700"))
    s.append(T(500, 416, "学习条件", 22, GRAY))
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
    for name, fn in [("toc.png", toc), ("fig-data.png", fig_data),
                     ("fig-modality.png", fig_modality), ("fig-intervene.png", fig_intervene),
                     ("fig-directions.png", fig_directions), ("fig-summary.png", fig_summary)]:
        w, h, inner = fn()
        render_svg(name, w, h, inner)


if __name__ == "__main__":
    main()
