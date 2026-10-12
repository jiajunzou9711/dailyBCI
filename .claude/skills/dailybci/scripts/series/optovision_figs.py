# -*- coding: utf-8 -*-
"""日报 2026-10-10「光遗传视觉修复」(Sahel 2021 Nat Med)：裁图、目录卡、对照表、视网膜示意图。
源图：papers/sahel-2021-*.png（PDF 600 dpi 页面渲染裁出，或 PDF 内嵌原图）。"""
import os, subprocess, tempfile
from PIL import Image, ImageDraw

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
PAP = os.path.join(PROJECT, "papers")
OUT = os.path.join(PROJECT, "output", "2026-10-10-optogenetic-vision", "figs")
os.makedirs(OUT, exist_ok=True)
BG = "#FAFAFA"


def src(name):
    return Image.open(os.path.join(PAP, name)).convert("RGB")


def pad(im, p=24, color="white"):
    out = Image.new("RGB", (im.width + 2 * p, im.height + 2 * p), color)
    out.paste(im, (p, p))
    return out


def hcat(ims, gap=0):
    h = max(i.height for i in ims)
    out = Image.new("RGB", (sum(i.width for i in ims) + gap * (len(ims) - 1), h), "white")
    x = 0
    for i in ims:
        out.paste(i, (x, 0)); x += i.width + gap
    return out


def save(im, name, p=24):
    path = os.path.join(OUT, name)
    pad(im, p).save(path)
    print("wrote", name, Image.open(path).size)


def figs():
    ed1 = src("sahel-2021-p10-0.png")          # Extended Data Fig. 1（内嵌原图 1772×1617）
    a = ed1.crop((0, 0, 1772, 1060)).copy()
    ImageDraw.Draw(a).rectangle((0, 0, 70, 70), fill="white")      # 去面板字母 a
    save(a, "cover.png")
    b = ed1.crop((0, 1100, 1772, 1617)).copy()
    ImageDraw.Draw(b).rectangle((0, 0, 70, 90), fill="white")      # 去面板字母 b
    save(b, "ed1b.png")
    # Table 1：行名列 + 戴镜三列；去掉表题行与表注行
    t1 = src("sahel-2021-table1.png")
    save(hcat([t1.crop((0, 165, 960, 1240)), t1.crop((3135, 165, 4461, 1240))]), "t1.png", p=0)
    # Table 3：行名列 + 戴镜三列；去掉表题行
    t3 = src("sahel-2021-table3.png")
    save(hcat([t3.crop((0, 172, 640, 910)), t3.crop((3120, 172, 4461, 910))]), "t3.png", p=0)
    save(src("sahel-2021-fig2b.png"), "f2b.png", p=0)


ACC = "#2F6DB5"; ACCD = "#1E4E86"; TINT = "#E9F0F8"; INK = "#1A1A1A"; GRAY = "#666666"
CARD_L = "#DCE5F0"; AMBER = "#D98A1B"; AMBER_T = "#FBEFD9"; DEAD = "#BBBBBB"


def T(x, y, s, size=25, fill=INK, anchor="middle", weight="400"):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" font-weight="{weight}">{s}</text>')


def box(x, y, w, h, fill, stroke, rx=10, sw=1.4, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')


def arrow(x1, y1, x2, y2, color=INK, sw=2.4):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}" '
            f'marker-end="url(#ah{color[1:]})"/>')


def defs(*colors):
    m = "".join(
        f'<marker id="ah{c[1:]}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
        f'markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>'
        for c in colors)
    return f"<defs>{m}</defs>"


TOC = [
    ("①", "病坏在哪，以前怎么修", "RP 损毁感光细胞；已有方案在眼内植入电极"),
    ("②", "10 人新结果与 2021 年首例", "本周 NEJM 测安全与光敏度；物体任务要回到首例"),
    ("③", "怎么做到的", "一次眼内注射 ChrimsonR，加一副投光眼镜"),
    ("④", "三项测试的结果", "找物体、判断有无杯子、枕区脑电解码"),
    ("⑤", "和电极方案比较", "效果层级、创伤、信号从哪一级进入"),
    ("⑥", "局限性与结论边界", "一名患者能支持什么"),
]


def toc():
    W = 960; row_h, gap = 92, 10; x, y0 = 4, 6; s = []
    for i, (num, title, sub) in enumerate(TOC):
        y = y0 + i * (row_h + gap)
        s.append(box(x, y, W - 8, row_h, "#F7F9FC", CARD_L, 10, 1.2))
        s.append(box(x + 14, y + 24, 62, 44, TINT, ACC, 8, 1.2))
        s.append(T(x + 45, y + 55, num, 28, ACCD, weight="700"))
        s.append(T(x + 96, y + 40, title, 30, INK, anchor="start", weight="700"))
        s.append(T(x + 96, y + 76, sub, 24, GRAY, anchor="start"))
    return W, y0 + len(TOC) * (row_h + gap), "".join(s)


def table10():
    """卡⑩ 三方案对照表。多行单元格用列表给出。"""
    W = 1280
    head = ["", "Argus II", "PRIMA", "光遗传（本篇）"]
    rows = [
        ("病种", ["重度外层视网膜退化", "以 RP 为主"], ["年龄相关性黄斑变性", "所致地图状萎缩"], ["晚期 RP"]),
        ("入组时残余视力", ["微弱光感或无光感"], ["中央无光感", "周边保留"], ["只剩光感"]),
        ("人数", ["30"], ["38 人植入", "32 人满 12 个月随访"], ["1（物体任务）"]),
        ("能做到什么", ["开机优于关机的受试者：", "物体定位 96%", "运动方向辨别 57%"],
         ["26/32 视力表视力", "改善 ≥0.2 logMAR"], ["戴镜后找到并摸到", "笔记本，92% 试次成功"]),
        ("视力表视力", ["最好一例 20/1260"], ["有临床意义的改善"], ["未测"]),
    ]
    cx = [16, 250, 600, 950]; lh = 38; s = []
    y = 14
    s.append(f'<line x1="4" y1="{y}" x2="{W-4}" y2="{y}" stroke="{INK}" stroke-width="2.4"/>')
    for j, c in enumerate(head):
        col = ACCD if j == 3 else INK
        s.append(T(cx[j], y + 46, c, 30, col, anchor="start", weight="700"))
    y += 68
    s.append(f'<line x1="4" y1="{y}" x2="{W-4}" y2="{y}" stroke="{INK}" stroke-width="1.2"/>')
    for i, (lab, *cells) in enumerate(rows):
        n = max(len(c) for c in cells)
        h = 22 + n * lh
        if i % 2 == 1:
            s.append(f'<rect x="4" y="{y}" width="{W-8}" height="{h}" fill="#F3F5F8"/>')
        s.append(T(cx[0], y + 12 + lh * 0.8, lab, 27, GRAY, anchor="start", weight="700"))
        for j, lines in enumerate(cells):
            for k, ln in enumerate(lines):
                col = ACCD if j == 2 else INK
                s.append(T(cx[j + 1], y + 12 + lh * (k + 0.8), ln, 27, col, anchor="start"))
        y += h
    s.append(f'<line x1="4" y1="{y}" x2="{W-4}" y2="{y}" stroke="{INK}" stroke-width="2.4"/>')
    return W, y + 8, "".join(s)


def retina(mode):
    """mode='rp'：三级视网膜，RP 损毁感光细胞层；mode='opto'：从玻璃体侧注射，ChrimsonR 表达在神经节细胞。
    方位：玻璃体（光进入一侧）在上，感光细胞在下——视网膜内光先经过神经节细胞层。"""
    W = 1240; s = [defs(INK, AMBER, ACC)]
    layers = [("神经节细胞（retinal ganglion cell）", "轴突汇成视神经，把动作电位送入大脑"),
              ("双极细胞（bipolar cell）", "把感光细胞的信号传给神经节细胞"),
              ("感光细胞（视杆、视锥）", "把光转成电信号")]
    x0, w = 300, 900; y0, lh, gap = 110, 120, 24
    s.append(T(150, 60, "玻璃体一侧", 26, GRAY))
    if mode == "rp":
        s.append(T(150, 96, "光由此进入", 24, GRAY))
        s.append(arrow(150, 112, 150, 104 + 3 * (lh + gap) - 30, "#999999", 2))
    else:
        s.append(box(36, 76, 230, 112, AMBER_T, AMBER, 10, 1.6))
        s.append(T(151, 116, "玻璃体内注射", 24, INK, weight="700"))
        s.append(T(151, 150, "AAV2.7m8", 22, INK))
        s.append(T(151, 178, "编码 ChrimsonR", 22, INK))
        s.append(arrow(266, 140, x0 - 8, y0 + lh / 2, AMBER, 2.6))
        s.append(T(151, 300, "595 nm 光脉冲", 24, AMBER, weight="700"))
        s.append(T(151, 332, "（来自眼镜）", 22, GRAY))
        s.append(arrow(240, 300, x0 - 8, y0 + lh / 2 + 20, AMBER, 2.6))
    for i, (name, desc) in enumerate(layers):
        y = y0 + i * (lh + gap)
        dead = (i == 2)
        hl = (mode == "opto" and i == 0)
        fill = "#F1F1F1" if dead else (AMBER_T if hl else "#F7F9FC")
        stroke = DEAD if dead else (AMBER if hl else CARD_L)
        s.append(box(x0, y, w, lh, fill, stroke, 12, 2 if hl else 1.4, "8 6" if dead else None))
        s.append(T(x0 + 30, y + 50, name, 30, GRAY if dead else INK, anchor="start", weight="700"))
        s.append(T(x0 + 30, y + 92, desc, 24, GRAY, anchor="start"))
        if dead:
            s.append(T(x0 + w - 24, y + 50, "RP 中大量死亡", 26, "#B04A3A", anchor="end", weight="700"))
        if hl:
            s.append(T(x0 + w - 24, y + 50, "表达 ChrimsonR", 26, AMBER, anchor="end", weight="700"))
    return W, y0 + 3 * (lh + gap) + 10, "".join(s)


def pathway():
    """卡⑫：左正常通路，右本篇通路。"""
    W = 1240; s = [defs(INK, AMBER)]
    colx = [40, 650]; bw = 550; bh = 78
    s.append(T(colx[0] + bw / 2, 40, "正常视觉", 30, INK, weight="700"))
    s.append(T(colx[1] + bw / 2, 40, "本篇", 30, AMBER, weight="700"))
    left = ["光", "感光细胞：光转成电信号", "双极细胞", "神经节细胞", "视神经 → 大脑"]
    right = ["595 nm 光脉冲（眼镜）", "感光细胞：跳过", "双极细胞：跳过", "神经节细胞：ChrimsonR 直接感光", "视神经 → 大脑"]
    y0, step = 70, 118
    for c, items in enumerate([left, right]):
        for i, t in enumerate(items):
            y = y0 + i * step
            skipped = (c == 1 and i in (1, 2))
            hl = (c == 1 and i in (0, 3))
            fill = "#F1F1F1" if skipped else (AMBER_T if hl else "#F7F9FC")
            stroke = DEAD if skipped else (AMBER if hl else CARD_L)
            s.append(box(colx[c], y, bw, bh, fill, stroke, 10, 1.6, "8 6" if skipped else None))
            s.append(T(colx[c] + bw / 2, y + 50, t, 27, GRAY if skipped else INK,
                       weight="700" if hl else "400"))
            if i < len(items) - 1 and not (c == 1 and i in (0, 1, 2)):
                s.append(arrow(colx[c] + bw / 2, y + bh + 4, colx[c] + bw / 2, y + step - 6))
    # 右列：光直接到神经节细胞的旁路箭头
    xr = colx[1] + bw + 22
    s.append(f'<path d="M{colx[1]+bw},{y0+bh/2} C{xr+20},{y0+bh/2} {xr+20},{y0+3*step+bh/2} '
             f'{colx[1]+bw+6},{y0+3*step+bh/2}" fill="none" stroke="{AMBER}" stroke-width="2.6" '
             f'marker-end="url(#ah{AMBER[1:]})"/>')
    yb = y0 + 5 * step + 10
    s.append(box(40, yb, W - 80, 128, "#F7F9FC", CARD_L, 10, 1.2))
    s.append(T(70, yb + 48, "随前两级一起缺失的视网膜内部处理：", 26, INK, anchor="start", weight="700"))
    s.append(T(70, yb + 96, "ON / OFF 分化 · 中心-周边拮抗 · 颜色（视锥之间的比较）", 26, GRAY, anchor="start"))
    return W, yb + 140, "".join(s)


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
    figs()
    render_svg("toc.png", *toc())
    render_svg("table10.png", *table10())
    render_svg("retina_rp.png", *retina("rp"))
    render_svg("retina_opto.png", *retina("opto"))
    render_svg("pathway.png", *pathway())
