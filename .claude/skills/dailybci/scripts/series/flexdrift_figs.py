# -*- coding: utf-8 -*-
"""日报 2026-10-07「柔性电极 × 表征漂移」(Shen 2026 Nat Biomed Eng)：裁图、拼版、目录卡、表格卡。
坐标按 300 dpi 整页量得，裁切在 600 dpi 页面上进行（×2）。"""
import os, subprocess, tempfile
from PIL import Image, ImageDraw, ImageFont
Image.MAX_IMAGE_PIXELS = None

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
PAP = os.path.join(PROJECT, "papers")
OUT = os.path.join(PROJECT, "output", "2026-10-07-flexible-drift", "figs")
os.makedirs(OUT, exist_ok=True)
BG = "#FAFAFA"
K = 2  # 300 dpi -> 600 dpi


def page(n):
    return Image.open(os.path.join(PAP, f"shen-fig{n}-600.png")).convert("RGB")


def crop(n, box, masks=()):
    """box/masks in 300-dpi coords; masks are painted white before cropping."""
    im = page(n).copy()
    d = ImageDraw.Draw(im)
    for m in masks:
        d.rectangle(tuple(v * K for v in m), fill="white")
    return im.crop(tuple(v * K for v in box))


def pad(im, p=24):
    out = Image.new("RGB", (im.width + 2 * p, im.height + 2 * p), "white")
    out.paste(im, (p, p))
    return out


def hcat(ims, gap=40, valign="top"):
    h = max(i.height for i in ims)
    w = sum(i.width for i in ims) + gap * (len(ims) - 1)
    out = Image.new("RGB", (w, h), "white")
    x = 0
    for i in ims:
        y = 0 if valign == "top" else (h - i.height) // 2
        out.paste(i, (x, y)); x += i.width + gap
    return out


def vcat(ims, gap=30):
    w = max(i.width for i in ims)
    out = Image.new("RGB", (w, sum(i.height for i in ims) + gap * (len(ims) - 1)), "white")
    y = 0
    for i in ims:
        out.paste(i, ((w - i.width) // 2, y)); y += i.height + gap
    return out


def save(im, name):
    p = os.path.join(OUT, name)
    pad(im).save(p)
    print("wrote", name, Image.open(p).size)


def figs():
    # 封面：Fig 1b 右格（群体轨迹落在不同平面）
    save(crop(1, (1812, 895, 2345, 1498)), "cover.png")
    # 卡⑤：Fig 1b 左半（小鼠 + 两组刺激时间表），去掉面板字母 b（x<235 不入框）
    save(crop(1, (232, 862, 1168, 1536)), "f1b_left.png")
    # 卡⑥：Fig 2f（遮掉面板字母 f 与下方 Fig 2h 的顶端）
    save(crop(2, (1575, 880, 2262, 1418), masks=[(1575, 890, 1615, 932), (1575, 1404, 2148, 1418)]), "f2f.png")
    # 卡⑦：Fig 2k「Month 1 versus 5」+ 共用 y 轴 + x 轴标题 + 图例移至图外
    src = page(2)
    yax = src.crop((160 * K, 2740 * K, 284 * K, 3046 * K))
    p4 = src.crop((975 * K, 2745 * K, 1202 * K, 3046 * K))
    xl = src.crop((600 * K, 3056 * K, 866 * K, 3092 * K))
    leg = src.crop((363 * K, 2943 * K, 502 * K, 2992 * K))
    W = yax.width + p4.width + leg.width + 20
    k = Image.new("RGB", (W, p4.height + xl.height + 12), "white")
    k.paste(yax, (0, 0)); k.paste(p4, (yax.width, 0))
    k.paste(leg, (yax.width + p4.width + 20, p4.height // 2 - leg.height // 2))
    k.paste(xl, (yax.width + (p4.width - xl.width) // 2, p4.height + 12))
    save(k, "f2k.png")
    # 卡⑧：Fig 3c（遮掉面板字母 c 与右上 Fig 3b 色标标题）
    save(crop(3, (490, 1700, 1726, 2180), masks=[(1518, 1680, 1745, 1728)]), "f3c.png")
    # 卡⑨：Fig 3e | Fig 3h（遮掉字母 e、h）
    e = crop(3, (462, 2185, 985, 2650), masks=[(458, 2188, 499, 2226)])
    h = crop(3, (462, 2655, 985, 3125), masks=[(458, 2658, 499, 2700)])
    save(hcat([e, h], gap=50), "f3eh.png")
    # 卡⑩：Fig 4f 上 | Fig 4i（4f 的 y 轴标题跨上下两格，裁上格时重写同一标题）
    ftop = crop(4, (1302, 1812, 1782, 2143), masks=[(1302, 2133, 1350, 2150)])
    lab = Image.new("RGB", (ftop.height, 70), "white")
    fnt = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 40)
    dd = ImageDraw.Draw(lab)
    t = "Latent dynamics correlation"
    tw = dd.textlength(t, font=fnt)
    dd.text(((lab.width - tw) / 2, 10), t, fill=(26, 26, 26), font=fnt)
    ftop = hcat([lab.rotate(90, expand=True), ftop], gap=6)
    fi = crop(4, (1262, 2512, 1782, 3112), masks=[(1258, 2500, 1300, 2545)])
    save(hcat([ftop, fi], gap=50, valign="center"), "f4fi.png")
    # 卡⑪：Fig 5c 左 | Fig 5e（e 的 x 轴刻度与标题取自其下方共用横轴的 Fig 5g）
    c = crop(5, (160, 893, 740, 1345), masks=[(726, 980, 740, 1240)])
    ee = crop(5, (1355, 893, 1945, 1388))
    g_axis = crop(5, (1355, 2046, 1945, 2132))
    save(hcat([c, vcat([ee, g_axis], gap=0)], gap=50), "f5ce.png")


ACC = "#2F6DB5"; ACCD = "#1E4E86"; TINT = "#E9F0F8"; INK = "#1A1A1A"; GRAY = "#666666"; CARD_L = "#DCE5F0"

TOC = [
    ("①", "解码器变差的两个来源", "记录不稳定，还是表征漂移"),
    ("②", "剩下的问题", "漂移有没有可描述的规律"),
    ("③", "作者的问题与答案", "漂移的神经元里有没有稳定结构"),
    ("④", "电极、范式与两条判据", "5 个月里记的是同一批神经元"),
    ("⑤", "漂移的规律与对齐", "随观看次数累积，可用平移加旋转对齐"),
    ("⑥", "回到两个来源", "稳定记录是校正的前提"),
    ("⑦", "能支持什么，局限性在哪", "对齐用到了刺激的时间信息"),
]


def T(x, y, s, size=25, fill=INK, anchor="middle", weight="400"):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" font-weight="{weight}">{s}</text>')


def box(x, y, w, h, fill, stroke, rx=10, sw=1.4):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')


def toc():
    W = 1240; row_h, gap = 84, 10; x, y0 = 4, 6
    s = []
    for i, (num, title, sub) in enumerate(TOC):
        y = y0 + i * (row_h + gap)
        s.append(box(x, y, W - 8, row_h, "#F7F9FC", CARD_L, 10, 1.2))
        s.append(box(x + 14, y + 22, 62, 40, TINT, ACC, 8, 1.2))
        s.append(T(x + 45, y + 51, num, 26, ACCD, weight="700"))
        s.append(T(x + 96, y + 37, title, 28, INK, anchor="start"))
        s.append(T(x + 96, y + 70, sub, 22, GRAY, anchor="start"))
    return W, y0 + len(TOC) * (row_h + gap), "".join(s)


def table():
    W = 1240
    rows = [("输入", "每个时间点的内容", "降维", "跨记录对齐"),
            ("单神经元", "每个神经元的放电率", "无", "无"),
            ("未对齐", "全部记录合起来降维后的潜在动力学", "有", "无"),
            ("对齐后", "每次记录单独降维，再做平移和旋转对齐", "有", "有")]
    cx = [20, 180, 920, 1050]
    rh = 74; y0 = 20; s = []
    s.append(f'<line x1="4" y1="{y0}" x2="{W-4}" y2="{y0}" stroke="{INK}" stroke-width="2.4"/>')
    for i, r in enumerate(rows):
        y = y0 + i * rh
        for j, c in enumerate(r):
            anchor = "start" if j < 2 else "start"
            col = ACCD if (i == 3 and j == 0) else INK
            s.append(T(cx[j], y + 48, c, 28 if i else 27, col, anchor=anchor,
                       weight="700" if i == 0 or (i == 3 and j == 0) else "400"))
        if i == 0:
            s.append(f'<line x1="4" y1="{y+rh}" x2="{W-4}" y2="{y+rh}" stroke="{INK}" stroke-width="1.2"/>')
    yb = y0 + len(rows) * rh
    s.append(f'<line x1="4" y1="{yb}" x2="{W-4}" y2="{yb}" stroke="{INK}" stroke-width="2.4"/>')
    return W, yb + 10, "".join(s)


def render_svg(name, w, h, inner):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{2*w}" height="{2*h}" '
           f'viewBox="0 0 {w} {h}"><rect width="{w}" height="{h}" fill="{BG}"/>{inner}</svg>')
    html = (f'<html><head><meta charset="utf-8"><style>'
            f'@font-face{{font-family:HS;src:url("file://{FONT}");}}'
            f'*{{font-family:HS,Helvetica,Arial,sans-serif;}}'
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
    render_svg("table.png", *table())
