# -*- coding: utf-8 -*-
"""日报 2026-08-27「语言的神经群体编码」第七期：目录卡 + 自制对照 SVG。"""
import os, subprocess, tempfile
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-08-27-langcode-07", "figs")
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
    ("①", "起点", "模型与人脑的相似已被反复测到"),
    ("②", "拆开看", "五条实现上的差距一次摆出"),
    ("③–⑦", "逐条对照", "元件 / 通信 / 学习规则 / 回路 / 时间"),
    ("⑧", "相似靠什么成立", "被保留下来的五条性质"),
    ("⑨", "结论", "相似成立在组织方式上"),
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


# ③ 元件的多样性
def fig_units():
    W, H = 1000, 460
    s = []
    s.append(panel(20, 14, 460, 430, "生物：多种类型", WARM, WARM_T))
    # 锥体细胞
    s.append(f'<path d="M120 300 L150 240 L180 300 Z" fill="{WARM}" stroke="{WARM}" stroke-width="2"/>')
    s.append(f'<line x1="150" y1="240" x2="150" y2="170" stroke="{WARM}" stroke-width="3"/>')
    s.append(f'<line x1="150" y1="200" x2="115" y2="165" stroke="{WARM}" stroke-width="2.2"/>')
    s.append(f'<line x1="150" y1="200" x2="185" y2="165" stroke="{WARM}" stroke-width="2.2"/>')
    s.append(f'<line x1="150" y1="300" x2="150" y2="370" stroke="{WARM}" stroke-width="2.6"/>')
    s.append(T(150, 400, "锥体细胞", 20, INK))
    # 中间神经元 ×2
    for cx, lab in ((285, "PV 细胞"), (400, "SST 细胞")):
        s.append(f'<circle cx="{cx}" cy="270" r="24" fill="#FFFFFF" stroke="{WARM}" stroke-width="2.6"/>')
        for dx, dy in ((-17, -17), (17, -17), (-17, 17), (17, 17)):
            s.append(f'<line x1="{cx+dx}" y1="{270+dy}" x2="{cx+dx*2.1}" y2="{270+dy*2.1}" stroke="{WARM}" stroke-width="2"/>')
        s.append(T(cx, 400, lab, 20, INK))
    s.append(T(250, 120, "形态、时间常数、放电模式各不相同", 21, WARM, weight="700"))
    s.append(T(250, 152, "树突分支能做局部非线性运算", 21, WARM))

    s.append(panel(520, 14, 460, 430, "LLM：同一种", ACC, TINT))
    for r in range(3):
        for c in range(5):
            cx = 585 + c * 78; cy = 210 + r * 76
            s.append(f'<circle cx="{cx}" cy="{cy}" r="22" fill="#FFFFFF" stroke="{ACC}" stroke-width="2.4"/>')
    s.append(T(750, 120, "同一个激活函数，无形态、无类型", 21, ACCD, weight="700"))
    s.append(T(750, 152, "全部差别只在权重的数值上", 21, ACCD))
    return W, H, "".join(s)


# ④ 动作电位 vs 一个实数
def fig_spike():
    W, H = 1000, 400
    s = []
    s.append(panel(20, 14, 460, 370, "生物：离散事件", WARM, WARM_T))
    s.append(f'<line x1="70" y1="250" x2="440" y2="250" stroke="{NEU_S}" stroke-width="2"/>')
    for x in (110, 138, 205, 232, 258, 330, 402):
        s.append(f'<line x1="{x}" y1="250" x2="{x}" y2="150" stroke="{WARM}" stroke-width="3.4"/>')
    s.append(f'<line x1="138" y1="128" x2="205" y2="128" stroke="{GRAY}" stroke-width="1.8"/>')
    s.append(T(171, 118, "间隔", 19, GRAY))
    s.append(T(250, 300, "发生在具体时刻", 22, WARM, weight="700"))
    s.append(T(250, 332, "率、间隔、相位都能携带信息", 21, INK))

    s.append(panel(520, 14, 460, 370, "LLM：一个实数", ACC, TINT))
    s.append(box(660, 160, 180, 92, "#FFFFFF", ACC, 12, 2))
    s.append(T(750, 220, "0.37", 46, ACCD, weight="700"))
    s.append(T(750, 300, "没有事件，没有时刻", 22, ACCD, weight="700"))
    s.append(T(750, 332, "只保留「强度」这一个量", 21, INK))
    return W, H, "".join(s)


# ⑤ 局部规则 vs 反向传播
def fig_learning():
    W, H = 1000, 430
    s = []
    s.append(panel(20, 14, 460, 400, "生物：局部规则", WARM, WARM_T))
    s.append(f'<circle cx="140" cy="200" r="30" fill="#FFFFFF" stroke="{WARM}" stroke-width="2.6"/>')
    s.append(f'<circle cx="330" cy="200" r="30" fill="#FFFFFF" stroke="{WARM}" stroke-width="2.6"/>')
    s.append(arrow(172, 200, 296, 200, WARM, 3))
    s.append(T(234, 178, "突触", 21, WARM, weight="700"))
    s.append(T(140, 252, "前", 21, INK)); s.append(T(330, 252, "后", 21, INK))
    s.append(T(250, 300, "只看前后两个神经元自身的活动", 21, INK))
    s.append(box(70, 322, 360, 62, "#FFFFFF", WARM, 10, 1.6))
    s.append(T(250, 360, "＋ 一个全局标量信号（如多巴胺）", 21, WARM, weight="700"))

    s.append(panel(520, 14, 460, 400, "LLM：反向传播", ACC, TINT))
    ys = [120, 200, 280]
    for i, y in enumerate(ys):
        for c in range(4):
            cx = 600 + c * 80
            s.append(f'<circle cx="{cx}" cy="{y}" r="17" fill="#FFFFFF" stroke="{ACC}" stroke-width="2.2"/>')
    for y1, y2 in ((280, 200), (200, 120)):
        s.append(arrow(900, y1 - 2, 900, y2 + 22, ACCD, 3))
    s.append(T(750, 330, "误差从输出逐层回传", 22, ACCD, weight="700"))
    s.append(T(750, 362, "每个权重按它对总误差的贡献更新", 21, INK))
    return W, H, "".join(s)


# ⑦ 连续时间 vs 离散步序
def fig_time():
    import math
    W, H = 1000, 400
    s = []
    s.append(panel(20, 14, 460, 370, "生物：连续时间", WARM, WARM_T))
    pts = []
    for i in range(0, 361):
        x = 60 + i
        y = 200 + 46 * math.sin(i / 18.0) * (0.55 + 0.45 * math.sin(i / 70.0))
        pts.append(f"{x},{y:.1f}")
    s.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{WARM}" stroke-width="2.6"/>')
    s.append(T(250, 292, "不给刺激也存在的内源节律", 21, WARM, weight="700"))
    s.append(T(250, 324, "不同频段承担不同粒度的切分", 21, INK))
    s.append(T(250, 356, "theta ≈ 音节　delta ≈ 短语", 21, GRAY))

    s.append(panel(520, 14, 460, 370, "LLM：离散步序", ACC, TINT))
    for c in range(5):
        x = 566 + c * 78
        s.append(box(x, 168, 62, 62, "#FFFFFF", ACC, 10, 2))
        s.append(T(x + 31, 208, f"t{c+1}", 22, ACCD, weight="700"))
    s.append(T(750, 292, "一个 token 一步", 22, ACCD, weight="700"))
    s.append(T(750, 324, "步与步之间不对应任何时长", 21, INK))
    s.append(T(750, 356, "不给输入就没有活动", 21, GRAY))
    return W, H, "".join(s)


# ⑨ 两层地图
def fig_map():
    W, H = 1000, 470
    s = []
    s.append(box(20, 14, 960, 200, TINT, ACC, 14, 1.8))
    s.append(T(60, 56, "像", 30, ACCD, anchor="start", weight="700"))
    rows = [("表征格式", "六个语言层级是同一空间里的方向，没有分成独立模块"),
            ("学习目标", "预测序列里的下一个输入"),
            ("学到的几何", "不同系统学出的几何部分共享")]
    for i, (k, v) in enumerate(rows):
        y = 96 + i * 40
        s.append(T(150, y, k, 23, ACCD, anchor="start", weight="700"))
        s.append(T(330, y, v, 22, INK, anchor="start"))

    s.append(box(20, 232, 960, 160, WARM_T, WARM, 14, 1.8))
    s.append(T(60, 274, "不像", 30, WARM, anchor="start", weight="700"))
    rows2 = [("实现与加工方式", "元件 / 通信 / 学习规则 / 回路 / 时间"),
             ("学习条件", "数据量 / 模态 / 能否干预 / 目标 / 效率")]
    for i, (k, v) in enumerate(rows2):
        y = 314 + i * 40
        s.append(T(150, y, k, 23, WARM, anchor="start", weight="700"))
        s.append(T(400, y, v, 22, INK, anchor="start"))
    s.append(T(500, 442, "本期讲第一类", 22, GRAY))
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
    for name, fn in [("toc.png", toc), ("fig-units.png", fig_units),
                     ("fig-spike.png", fig_spike), ("fig-learning.png", fig_learning),
                     ("fig-time.png", fig_time), ("fig-map.png", fig_map)]:
        w, h, inner = fn()
        render_svg(name, w, h, inner)


if __name__ == "__main__":
    main()
