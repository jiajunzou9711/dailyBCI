"""日报 2026-08-17「语言的神经群体编码」第一期：目录卡 SVG + 封面配图重排。

两件事：
1. toc()  —— 本期路线的目录卡（10 条，双栏 5 行）。
2. retile_fig3c() —— 把 Shain 2024 Fig 3C 的六个区从「一字排开」(3.8:1)
   重排成 3 列 × 2 行，供封面使用（见 SKILL Step 8 黄金标准 ②(c)）。
"""
import os, subprocess, tempfile
from PIL import Image

Image.MAX_IMAGE_PIXELS = None

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-08-17-language-population-code", "figs")
os.makedirs(OUT, exist_ok=True)

ACC = "#2F6DB5"; ACCD = "#1E4E86"; TINT = "#E9F0F8"
INK = "#1A1A1A"; GRAY = "#8A8A8A"; CARD_L = "#DCE5F0"
BG = "#FAFAFA"          # 与卡面一致，避免出现白方块


def T(x, y, s, size=25, fill=INK, anchor="middle", weight="400"):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" font-weight="{weight}">{s}</text>')


def box(x, y, w, h, fill, stroke, rx=12, sw=1.5):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')


def circ(cx, cy, r, fill, stroke, sw=1.5):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw}"/>')


# 目录条目：措辞与正文卡标题逐字一致
TOC_ITEMS = [
    ("①", "拆分建模拼不出一致的图景"),
    ("②", "一个主张、两条原理、四个案例"),
    ("③", "六个层级，一个空间，六组方向"),
    ("④", "语义和句法为什么被分成两样"),
    ("⑤", "重做一个里程碑实验"),
    ("⑥", "一套材料，两个变量"),
    ("⑦", "效应复现，定位推翻"),
    ("⑧", "词义效应也遍布，且与结构耦合"),
    ("⑨", "这个效应算不算句法效应"),
    ("⑩", "这批结果没有回答的三件事"),
]


def toc():
    s = []
    W = 1000
    col_w, row_h, gap = 480, 76, 10
    x0 = [10, 10 + col_w + gap]
    y0 = 8
    for i, (num, title) in enumerate(TOC_ITEMS):
        col, row = i // 5, i % 5
        x, y = x0[col], y0 + row * (row_h + gap)
        s.append(box(x, y, col_w, row_h, "#F7F9FC", CARD_L, 13, 1.4))
        s.append(circ(x + 42, y + 38, 24, TINT, ACC, 1.4))
        s.append(T(x + 42, y + 47, num, 26, ACCD, weight="700"))
        s.append(T(x + 80, y + 47, title, 26, INK, anchor="start", weight="700"))
    h = y0 + 5 * (row_h + gap)
    return W, h, "".join(s)


def render_svg(name, w, h, inner):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
           f'viewBox="0 0 {w} {h}"><rect width="{w}" height="{h}" fill="{BG}"/>'
           f'{inner}</svg>')
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
    return out


# ---------- 封面配图：Fig 3C 六个区重排成 3×2 ----------
# 列边界由 600 dpi 页面的墨迹投影量出（相邻留白沟取中线），不是肉眼估的
COL_BOUNDS = [1206, 1732, 2250, 2766, 3283, 3801, 4300]
LABEL_BAND = (1182, 1280)   # 区域名那一行(按墨迹实测)
PLOT_BAND = (2181, 2853)    # 实验二（panel C）的六张图(按墨迹实测)
LEGEND_BAND = (3700, 3785)


def retile_fig3c(src=None, out_name="cover-fig3c-3x2.png"):
    src = src or os.path.join(PROJECT, "papers", "shain-p10-600.png")
    page = Image.open(src)
    tiles = []
    for i in range(6):
        x0, x1 = COL_BOUNDS[i], COL_BOUNDS[i + 1]
        lab = page.crop((x0, LABEL_BAND[0], x1, LABEL_BAND[1]))
        plot = page.crop((x0, PLOT_BAND[0], x1, PLOT_BAND[1]))
        t = Image.new("RGB", (x1 - x0, lab.height + plot.height), "white")
        t.paste(lab, (0, 0)); t.paste(plot, (0, lab.height))
        tiles.append(t)
    tw = max(t.width for t in tiles); th = max(t.height for t in tiles)
    gx, gy = 34, 22
    legend = page.crop((COL_BOUNDS[0], LEGEND_BAND[0], COL_BOUNDS[-1], LEGEND_BAND[1]))
    grid_w = 3 * tw + 2 * gx
    legend = legend.resize((grid_w, int(legend.height * grid_w / legend.width)))
    canvas = Image.new("RGB", (grid_w, 2 * th + gy + 16 + legend.height), "white")
    for i, t in enumerate(tiles):
        canvas.paste(t, ((i % 3) * (tw + gx), (i // 3) * (th + gy)))
    canvas.paste(legend, (0, 2 * th + gy + 16))
    out = os.path.join(OUT, out_name)
    canvas.save(out)
    print("wrote", out, canvas.size, "aspect %.2f" % (canvas.width / canvas.height))
    return out


PLOT_BAND_D = (2960, 3640)   # 实验三（panel D）的六张图


def retile_fig3d(src=None, out_name="fig3d-3x2.png"):
    """panel D 同样是 3.8:1 的一字排开，按同一套规则重排成 3×2。"""
    global PLOT_BAND
    keep = PLOT_BAND
    try:
        PLOT_BAND = PLOT_BAND_D
        return retile_fig3c(src=src, out_name=out_name)
    finally:
        PLOT_BAND = keep


# ---------- Fig 3E：只取正文用到的两组（词汇性效应 / 块长×词汇性交互） ----------
E_BAND = (3820, 4930)       # 柱状图 + 各组文字标签（不含散文图注）
E_GROUP1 = (1130, 1842)     # y 轴 + 「词汇性效应」一组
E_AXIS = (1826, 1996)       # 后四组共用的 y 轴
E_GROUP5 = (3660, 4258)     # 「块长×词汇性交互」一组
E_LEGEND = (2700, 3852, 4570, 4024)   # 脑区配色图例（原在右上角，移到下方）


def crop_fig3e(src=None, out_name="fig3e-two-groups.png"):
    from PIL import ImageDraw
    src = src or os.path.join(PROJECT, "papers", "shain-p10-600.png")
    page = Image.open(src).convert("RGB")
    legend = page.crop(E_LEGEND)
    clean = page.copy()
    ImageDraw.Draw(clean).rectangle(list(E_LEGEND), fill="white")
    a = clean.crop((E_GROUP1[0], E_BAND[0], E_GROUP1[1], E_BAND[1]))
    ax = clean.crop((E_AXIS[0], E_BAND[0], E_AXIS[1], E_BAND[1]))
    b = clean.crop((E_GROUP5[0], E_BAND[0], E_GROUP5[1], E_BAND[1]))
    gap = 60
    top_w = a.width + gap + ax.width + b.width
    canvas = Image.new("RGB", (max(top_w, legend.width), a.height + 30 + legend.height), "white")
    x = 0
    for part in (a, None, ax, b):
        if part is None:
            x += gap; continue
        canvas.paste(part, (x, 0)); x += part.width
    canvas.paste(legend, ((canvas.width - legend.width) // 2, a.height + 30))
    out = os.path.join(OUT, out_name)
    canvas.save(out)
    print("wrote", out, canvas.size, "aspect %.2f" % (canvas.width / canvas.height))
    return out


if __name__ == "__main__":
    w, h, inner = toc()
    render_svg("toc.png", w, h, inner)
    retile_fig3c()
    retile_fig3d()
    crop_fig3e()
