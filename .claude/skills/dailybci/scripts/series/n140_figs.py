# -*- coding: utf-8 -*-
"""日报 2026-10-13「头皮 N140 的颅内来源」(Mikulan 2026 bioRxiv)：目录卡、逆问题示意图、论文裁图归档。
源图：papers/mikulan-fig*.png（PDF 内嵌原图按 smask 合成到白底后裁出）。"""
import os, shutil, subprocess, tempfile
from PIL import Image

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
PAP = os.path.join(PROJECT, "papers")
OUT = os.path.join(PROJECT, "output", "2026-10-13-n140-scalp-intracranial", "figs")
os.makedirs(OUT, exist_ok=True)
BG = "#FAFAFA"
ACC = "#2F6DB5"; ACCD = "#1E4E86"; TINT = "#E9F0F8"; INK = "#1A1A1A"; GRAY = "#666666"
CARD_L = "#DCE5F0"; ORANGE = "#E8940A"; BLUE = "#4A7FD0"

CROPS = ["fig1a", "fig1d", "fig2a", "fig2c", "fig2d", "fig2f", "fig2gh", "fig3c", "fig3d", "fig3f"]


def T(x, y, s, size=25, fill=INK, anchor="middle", weight="400"):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" font-weight="{weight}">{s}</text>')


def box(x, y, w, h, fill, stroke, rx=10, sw=1.4):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')


TOC = [
    ("①", "这篇回答什么", "头皮上的觉察信号对应颅内哪种信号"),
    ("②", "两个觉察标记", "头皮的 N140 / SAN 与颅内的 tonic BHA"),
    ("③", "两种颅内信号", "同一触点上的 LFP 与 BHA"),
    ("④", "方法", "8 名 sEEG 患者，头皮与颅内同时记录"),
    ("⑤", "结果", "时间、深度、空间、近阈值四项证据"),
    ("⑥", "闭环", "两条证据排成一条时间序列"),
    ("⑦", "局限性与引申", "结论的范围，对脑机接口的提示"),
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


def dipole(cx, cy, ang, L=46, col=ACCD):
    """电流偶极子：带箭头的短线段（示意）。ang 为角度（度，0 = 向上）。"""
    import math
    dx = L / 2 * math.sin(math.radians(ang)); dy = -L / 2 * math.cos(math.radians(ang))
    return (f'<line x1="{cx-dx:.1f}" y1="{cy-dy:.1f}" x2="{cx+dx:.1f}" y2="{cy+dy:.1f}" '
            f'stroke="{col}" stroke-width="5" marker-end="url(#ahd)"/>'
            f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="5" fill="{col}"/>')


def inverse():
    """卡 4：同一张头皮电压分布，可由两组不同的颅内源产生（逆问题不适定，示意）。"""
    W, H = 1000, 560; s = []
    s.append('<defs><marker id="ahd" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" '
             f'markerHeight="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{ACCD}"/></marker></defs>')
    # 同一条头皮电压曲线，两侧各画一次
    def scalp_curve(ox):
        pts = []
        import math
        for i in range(61):
            t = i / 60
            v = math.exp(-((t - 0.5) / 0.17) ** 2) * 1.0 - 0.35 * math.exp(-((t - 0.18) / 0.1) ** 2) \
                - 0.35 * math.exp(-((t - 0.82) / 0.1) ** 2)
            pts.append(f"{ox + 40 + t * 340:.1f},{150 - v * 70:.1f}")
        return f'<polyline points="{" ".join(pts)}" fill="none" stroke="{ORANGE}" stroke-width="5"/>'
    for k, ox in enumerate([30, 530]):
        s.append(T(ox + 210, 40, "头皮电压分布", 26, GRAY))
        s.append(f'<line x1="{ox+40}" y1="150" x2="{ox+380}" y2="150" stroke="#CCCCCC" stroke-width="1.5"/>')
        s.append(scalp_curve(ox))
        # 头部剖面：头皮（外弧）、颅骨、脑
        cx, cy = ox + 210, 470
        s.append(f'<path d="M{cx-190},{cy} A190,230 0 0 1 {cx+190},{cy}" fill="#F3EDE6" stroke="#B9A994" stroke-width="3"/>')
        s.append(f'<path d="M{cx-168},{cy} A168,206 0 0 1 {cx+168},{cy}" fill="#FFFFFF" stroke="#C9C9C9" stroke-width="3"/>')
        s.append(f'<path d="M{cx-150},{cy} A150,186 0 0 1 {cx+150},{cy}" fill="#EEF2F8" stroke="#9FB3CF" stroke-width="2"/>')
        if k == 0:
            s.append(dipole(cx, cy - 70, 0, L=70))
            s.append(T(cx, cy + 50, "颅内源组合 A：一个较深的源", 26, INK))
        else:
            s.append(dipole(cx - 60, cy - 120, 28, L=70))
            s.append(dipole(cx + 60, cy - 120, -28, L=70))
            s.append(T(cx, cy + 50, "颅内源组合 B：两个较浅的源", 26, INK))
    s.append(T(500, 150, "=", 56, GRAY, weight="700"))
    s.append(T(W - 6, H - 4, "示意", 22, GRAY, anchor="end"))
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
    for c in CROPS:
        shutil.copy(os.path.join(PAP, f"mikulan-{c}.png"), os.path.join(OUT, f"{c}.png"))
    render_svg("toc.png", *toc())
    render_svg("inverse.png", *inverse())
