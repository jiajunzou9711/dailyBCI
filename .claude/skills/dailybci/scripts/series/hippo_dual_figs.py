# -*- coding: utf-8 -*-
"""日报 2026-10-17「海马建新地图」(Ren 2026 Curr Biol)：目录卡、实验时间线、BLT 三步示意。
论文裁图在 output/2026-10-17-hippocampus-dual-mode/figs/（600 dpi 页面渲染，投影定界 + 掩码去面板字母）。"""
import os, subprocess, tempfile, math
from PIL import Image

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-10-17-hippocampus-dual-mode", "figs")
os.makedirs(OUT, exist_ok=True)
BG = "#FAFAFA"
ACC = "#2F6DB5"; ACCD = "#1E4E86"; TINT = "#E9F0F8"; INK = "#1A1A1A"; GRAY = "#666666"
CARD_L = "#DCE5F0"; RED = "#C0476A"; BLUE = "#6A9BCB"; LGRAY = "#BBBBBB"


def T(x, y, s, size=25, fill=INK, anchor="middle", weight="400"):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" font-weight="{weight}">{s}</text>')


def box(x, y, w, h, fill, stroke, rx=10, sw=1.4):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')


TOC = [
    ("①", "这篇回答什么", "海马的空间地图为什么几分钟就能成形"),
    ("②", "作者的假说", "预先组织的网络与快速可塑性协同"),
    ("③", "遗留的两个问题", "两类位置野能否分开；离线活动能否提前对上"),
    ("④", "方法", "4 只大鼠 CA1 四电极记录；从休息放电推断空间偏好"),
    ("⑤", "结果", "两类位置野、三类细胞、离线对应先于位置野"),
    ("⑥", "闭环", "快速成图靠一小群预先组织好的细胞"),
    ("⑦", "局限性", "作者列出的五点"),
]


def toc():
    W = 960; row_h, gap = 84, 10; x, y0 = 4, 6; s = []
    for i, (num, title, sub) in enumerate(TOC):
        y = y0 + i * (row_h + gap)
        s.append(box(x, y, W - 8, row_h, "#F7F9FC", CARD_L, 10, 1.2))
        s.append(box(x + 14, y + 20, 62, 44, TINT, ACC, 8, 1.2))
        s.append(T(x + 45, y + 51, num, 28, ACCD, weight="700"))
        s.append(T(x + 96, y + 37, title, 30, INK, anchor="start", weight="700"))
        s.append(T(x + 96, y + 71, sub, 24, GRAY, anchor="start"))
    return W, y0 + len(TOC) * (row_h + gap), "".join(s)


def timeline():
    """卡 ④：9 段 × 30 min，笼中休息与轨道跑动交替；H0 在首次上轨道之前。"""
    segs = ["H0", "RUN1", "H1", "RUN2", "H2", "RUN3", "H3", "RUN4", "H4"]
    W, H = 1000, 300; bw, gap, x0, y = 100, 10, 7, 110; s = []
    for i, name in enumerate(segs):
        x = x0 + i * (bw + gap)
        run = name.startswith("RUN")
        fill, stroke, col = (TINT, ACC, ACCD) if run else ("#F0F0F0", LGRAY, GRAY)
        if i == 0:
            fill, stroke, col = ("#FBEFF3", RED, RED)
        s.append(box(x, y, bw, 70, fill, stroke, 8, 2 if i == 0 else 1.4))
        s.append(T(x + bw / 2, y + 44, name, 26, col, weight="700"))
        s.append(T(x + bw / 2, y + 104, "30 min", 20, GRAY))
    s.append(T(x0 + bw / 2, 60, "首次上轨道之前", 24, RED, weight="700", anchor="start"))
    s.append(f'<line x1="{x0+bw/2}" y1="70" x2="{x0+bw/2}" y2="{y-6}" stroke="{RED}" stroke-width="2"/>')
    # 图例
    ly = 270
    s.append(box(250, ly - 20, 30, 22, "#F0F0F0", LGRAY, 4)); s.append(T(290, ly - 2, "H：笼中休息", 22, GRAY, anchor="start"))
    s.append(box(520, ly - 20, 30, 22, TINT, ACC, 4)); s.append(T(560, ly - 2, "RUN：U 形轨道上往返取水", 22, GRAY, anchor="start"))
    return W, H, "".join(s)


def blt():
    """卡 ⑤：BLT 三步示意（自制）。"""
    W, H = 1000, 430; s = []
    s.append('<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" '
             f'markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{GRAY}"/></marker></defs>')
    pw = 300; xs = [10, 350, 690]
    heads = [("1 · 时刻", "休息中的群体放电事件"), ("2 · 位置", "去掉细胞 i，其余细胞解码"),
             ("3 · 倾向", "按细胞 i 的放电加权")]
    for (h1, h2), x in zip(heads, xs):
        s.append(T(x + pw / 2, 34, h1, 28, ACCD, weight="700"))
        s.append(T(x + pw / 2, 68, h2, 22, GRAY))
    # 面板 1：栅格 + 事件内切成小窗
    x = xs[0]; top = 100; rows = 7
    import random
    random.seed(3)
    for r in range(rows):
        yy = top + 22 + r * 34
        lab = "i" if r == 3 else ""
        col = RED if r == 3 else INK
        if lab:
            s.append(T(x + 82, yy + 8, "i", 24, RED, weight="700"))
        for k in range(6):
            tx = x + 110 + random.random() * 120
            s.append(f'<line x1="{tx:.1f}" y1="{yy-10}" x2="{tx:.1f}" y2="{yy+10}" stroke="{col}" stroke-width="3"/>')
    s.append(f'<rect x="{x+100}" y="{top}" width="140" height="{rows*34+10}" fill="{ACC}" opacity="0.08"/>')
    for k in range(1, 7):
        lx = x + 100 + k * 20
        s.append(f'<line x1="{lx}" y1="{top}" x2="{lx}" y2="{top+rows*34+10}" stroke="{ACC}" stroke-width="1" stroke-dasharray="4,3"/>')
    s.append(T(x + 170, top + rows * 34 + 44, "一个事件切成多个小时间窗", 20, GRAY))
    # 面板 2：细胞 i 灰掉 + 每窗一条后验
    x = xs[1]
    for r in range(rows):
        yy = top + 22 + r * 34
        if r == 3:
            s.append(f'<line x1="{x+20}" y1="{yy}" x2="{x+120}" y2="{yy}" stroke="{LGRAY}" stroke-width="3" stroke-dasharray="6,4"/>')
            s.append(T(x + 70, yy - 10, "细胞 i 不参与", 18, RED))
        else:
            s.append(f'<line x1="{x+20}" y1="{yy}" x2="{x+120}" y2="{yy}" stroke="{INK}" stroke-width="3"/>')
    s.append(f'<line x1="{x+128}" y1="{top+130}" x2="{x+158}" y2="{top+130}" stroke="{GRAY}" stroke-width="2" marker-end="url(#ah)"/>')
    for k, c in enumerate([0.3, 0.55, 0.35]):
        by = top + 40 + k * 82
        pts = []
        for j in range(41):
            t = j / 40; v = math.exp(-((t - c) / 0.08) ** 2)
            pts.append(f"{x+170+t*120:.1f},{by+50-v*44:.1f}")
        s.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{ACC}" stroke-width="3"/>')
        s.append(f'<line x1="{x+170}" y1="{by+50}" x2="{x+290}" y2="{by+50}" stroke="{LGRAY}" stroke-width="1.5"/>')
    s.append(T(x + 160, top + rows * 34 + 44, "每个窗：各位置的概率", 20, GRAY))
    # 面板 3：加权求和得到离线调谐曲线
    x = xs[2]
    pts = []
    for j in range(61):
        t = j / 60; v = math.exp(-((t - 0.33) / 0.1) ** 2) * 0.9 + 0.08
        pts.append(f"{x+40+t*230:.1f},{top+230-v*170:.1f}")
    s.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{RED}" stroke-width="4"/>')
    s.append(f'<line x1="{x+40}" y1="{top+230}" x2="{x+270}" y2="{top+230}" stroke="{INK}" stroke-width="2"/>')
    s.append(T(x + 40, top + 258, "0", 20, GRAY)); s.append(T(x + 270, top + 258, "266 cm", 20, GRAY))
    s.append(T(x + 155, top + 40, "细胞 i 的离线调谐曲线", 22, RED, weight="700"))
    s.append(T(x + 155, top + rows * 34 + 44, "再按网络停留归一化", 20, GRAY))
    s.append(T(W - 6, H - 4, "示意", 20, GRAY, anchor="end"))
    return W, H, "".join(s)


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
    render_svg("toc.png", *toc())
    render_svg("timeline.png", *timeline())
    render_svg("blt.png", *blt())
