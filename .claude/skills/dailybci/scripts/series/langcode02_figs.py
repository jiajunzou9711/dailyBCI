"""日报 2026-08-18「语言的神经群体编码」第二期：目录卡 + 四张自制 SVG。"""
import os, subprocess, tempfile
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-08-18-langcode-02", "figs")
os.makedirs(OUT, exist_ok=True)

ACC = "#2F6DB5"; ACCD = "#1E4E86"; TINT = "#E9F0F8"
INK = "#1A1A1A"; GRAY = "#8A8A8A"; CARD_L = "#DCE5F0"
WARM = "#C2542F"; WARM_T = "#F7EAE4"; BG = "#FAFAFA"


def T(x, y, s, size=25, fill=INK, anchor="middle", weight="400"):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" font-weight="{weight}">{s}</text>')


def box(x, y, w, h, fill, stroke, rx=12, sw=1.5):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')


def circ(cx, cy, r, fill, stroke, sw=1.5):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def arrow(x1, y1, x2, y2, col=GRAY, sw=2.4):
    return (f'<defs><marker id="a{abs(hash((x1,y1,x2,y2)))%9999}" markerWidth="9" markerHeight="9" '
            f'refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="{col}"/></marker></defs>'
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{sw}" '
            f'marker-end="url(#a{abs(hash((x1,y1,x2,y2)))%9999})"/>')


TOC_ITEMS = [
    ("①", "换一个自变量"),
    ("②", "一层 12 个头，一共 12 层"),
    ("③", "一个头怎么算出它的输出"),
    ("④", "一个头怎么对上一块脑区"),
    ("⑤", "144 个头 × 1000 个分区"),
    ("⑥", "主成分的双重身份"),
    ("⑦", "皮层的分化沿语境跨度排列"),
    ("⑧", "句法特化不占独立分区"),
    ("⑨", "给每个头打两个分"),
    ("⑩", "对应有选择性，但不按句法种类分"),
    ("⑪", "排除拟合硬拗出来的可能"),
    ("⑫", "这套证据能说到哪一步"),
]


def toc():
    s = []; W = 1000
    col_w, row_h, gap = 488, 64, 8
    x0 = [4, 4 + col_w + gap]; y0 = 6
    for i, (num, title) in enumerate(TOC_ITEMS):
        col, row = i // 6, i % 6
        x, y = x0[col], y0 + row * (row_h + gap)
        s.append(box(x, y, col_w, row_h, "#F7F9FC", CARD_L, 12, 1.4))
        s.append(circ(x + 36, y + 32, 21, TINT, ACC, 1.4))
        s.append(T(x + 36, y + 40, num, 23, ACCD, weight="700"))
        s.append(T(x + 68, y + 40, title, 23, INK, anchor="start", weight="700"))
    return W, y0 + 6 * (row_h + gap), "".join(s)


def fig_ivar():
    """卡①：两种自变量。"""
    s = []; W, H = 1000, 470
    s.append(T(500, 34, "用什么去解释脑活动", 30, INK, weight="700"))
    # row 1
    s.append(box(30, 62, 300, 150, "#F4F4F4", "#CFCFCF"))
    s.append(T(180, 100, "旧做法 · 刺激的属性", 25, GRAY, weight="700"))
    s.append(T(180, 143, "一次只有一个数", 24, INK))
    s.append(T(180, 180, "成分长度 · 语义内容", 22, GRAY))
    s.append(arrow(345, 137, 415, 137))
    s.append(box(430, 62, 540, 150, "#F7F9FC", CARD_L))
    s.append(T(700, 105, "能回答的问题", 24, GRAY, weight="700"))
    s.append(T(700, 152, "两种敏感性的分布重不重叠", 27, INK, weight="700"))
    s.append(T(700, 188, "答案落在「在哪里」这一层", 22, GRAY))
    # row 2
    s.append(box(30, 250, 300, 180, WARM_T, WARM))
    s.append(T(180, 288, "新做法 · 模型的部件", 25, WARM, weight="700"))
    for i in range(24):
        s.append(box(52 + (i % 8) * 32, 312 + (i // 8) * 26, 24, 18, "#FFFFFF", WARM, 4, 1.1))
    s.append(T(180, 412, "144 个注意力头，逐个取出", 22, WARM))
    s.append(arrow(345, 330, 415, 330, WARM))
    s.append(box(430, 250, 540, 180, WARM_T, WARM))
    s.append(T(700, 292, "能回答的问题", 24, WARM, weight="700"))
    s.append(T(700, 340, "哪个部件对应哪片皮层", 27, INK, weight="700"))
    s.append(T(700, 378, "部件之间按什么排列", 27, INK, weight="700"))
    s.append(T(700, 412, "答案落到「以什么形式」这一层", 22, WARM))
    return W, H, "".join(s)


def fig_align():
    """卡④：一个头怎么对上一块脑区（同一条时间轴）。"""
    import math
    s = []; W, H = 1000, 500
    x0, x1 = 90, 950
    s.append(T(500, 34, "同一条时间轴上的两条序列", 30, INK, weight="700"))
    # train / test bands
    split = x0 + int((x1 - x0) * 0.67)
    s.append(f'<rect x="{x0}" y="70" width="{split-x0}" height="330" fill="#F2F5F9"/>')
    s.append(f'<rect x="{split}" y="70" width="{x1-split}" height="330" fill="#FBF2EC"/>')
    s.append(T((x0 + split) // 2, 96, "训练段 · 拟合线性映射的权重", 23, GRAY))
    s.append(T((split + x1) // 2, 96, "留出段 · 算相关", 23, WARM))
    # two covarying curves
    pts_a, pts_b = [], []
    for i in range(87):
        t = i / 86.0
        v = (math.sin(t * 11.5) * 0.55 + math.sin(t * 4.1 + 1.2) * 0.45)
        x = x0 + t * (x1 - x0)
        pts_a.append(f"{x:.1f},{190 - v*52:.1f}")
        pts_b.append(f"{x:.1f},{330 - v*48 + math.sin(t*23)*5:.1f}")
    s.append(f'<polyline points="{" ".join(pts_a)}" fill="none" stroke="{ACC}" stroke-width="3"/>')
    s.append(f'<polyline points="{" ".join(pts_b)}" fill="none" stroke="{WARM}" stroke-width="3"/>')
    s.append(T(x0 - 8, 150, "模型侧", 23, ACC, anchor="end", weight="700"))
    s.append(T(x0 - 8, 178, "头 z", 21, ACC, anchor="end"))
    s.append(T(x0 - 8, 296, "脑侧", 23, WARM, anchor="end", weight="700"))
    s.append(T(x0 - 8, 324, "BOLD", 21, WARM, anchor="end"))
    s.append(f'<line x1="{x0}" y1="400" x2="{x1}" y2="400" stroke="{GRAY}" stroke-width="2"/>')
    for k in range(7):
        x = x0 + k * (x1 - x0) / 6
        s.append(f'<line x1="{x:.0f}" y1="400" x2="{x:.0f}" y2="410" stroke="{GRAY}" stroke-width="2"/>')
    s.append(T(500, 438, "每格 1 个 TR = 1.5 秒", 23, GRAY))
    s.append(T(500, 478, "回归只问一件事：这两条曲线同不同步", 27, INK, weight="700"))
    return W, H, "".join(s)


def fig_controls():
    """卡⑪：三种条件下的对应。"""
    s = []; W, H = 1000, 430
    cols = [
        ("原样", "144 个头按原本的分组", "对应成立", ACC, TINT, True),
        ("层内打乱头", "特征一个不少，只是不再按头组织", "对应基本消失", WARM, WARM_T, False),
        ("未训练模型", "架构与刺激相同，权重随机", "对应基本消失", WARM, WARM_T, False),
    ]
    cw = 300; gx = 25; x0 = 25
    s.append(T(500, 36, "两个对照排除了拟合硬拗的可能", 30, INK, weight="700"))
    for i, (name, how, res, col, tint, ok) in enumerate(cols):
        x = x0 + i * (cw + gx)
        s.append(box(x, 66, cw, 320, tint, col, 14, 1.8))
        s.append(T(x + cw // 2, 108, name, 28, col, weight="700"))
        s.append(f'<line x1="{x+30}" y1="128" x2="{x+cw-30}" y2="128" stroke="{col}" stroke-width="1.2"/>')
        # small head grid
        for k in range(12):
            fill = "#FFFFFF" if ok else ("#FFFFFF" if i == 1 else "#EFEFEF")
            s.append(box(x + 42 + (k % 6) * 36, 152 + (k // 6) * 30, 28, 22, fill, col, 4, 1.1))
        words = how.split("，")
        for j, wtxt in enumerate(words):
            s.append(T(x + cw // 2, 250 + j * 30, wtxt, 21, GRAY))
        s.append(T(x + cw // 2, 348, res, 27, col, weight="700"))
    s.append(T(500, 418, "起作用的是「按头组织」与「学过真实语言」这两件事", 25, INK, weight="700"))
    return W, H, "".join(s)


def fig_frame():
    """卡⑫：参照系 vs 替代品。"""
    s = []; W, H = 1000, 430
    s.append(T(500, 36, "模型在这里的角色", 30, INK, weight="700"))
    s.append(box(25, 66, 460, 330, "#F7F9FC", ACC, 14, 1.8))
    s.append(T(255, 110, "参照系", 30, ACCD, weight="700"))
    s.append(T(255, 148, "可以推出的结论", 22, GRAY))
    s.append(T(255, 200, "皮层的分化", 27, INK, weight="700"))
    s.append(T(255, 238, "沿语境跨度排列", 27, INK, weight="700"))
    s.append(T(255, 300, "模型给的是一套可测量的属性", 21, GRAY))
    s.append(T(255, 330, "层深 · 语境跨度", 21, GRAY))
    s.append(T(255, 372, "用来索引 BOLD 的空间差异", 22, ACCD, weight="700"))
    s.append(box(515, 66, 460, 330, "#F5F5F5", "#BDBDBD", 14, 1.8))
    s.append(T(745, 110, "替代品", 30, "#8A8A8A", weight="700"))
    s.append(T(745, 148, "推不出的结论", 22, GRAY))
    s.append(T(745, 200, "皮层在做", 27, "#9A9A9A", weight="700"))
    s.append(T(745, 238, "注意力式的加权整合", 27, "#9A9A9A", weight="700"))
    s.append(T(745, 300, "没有结果表明某个注意力头", 21, GRAY))
    s.append(T(745, 330, "对应脑内某个真实计算单元", 21, GRAY))
    s.append(T(745, 372, "编码模型只支持表征格式", 22, "#8A8A8A", weight="700"))
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
    return out


def main():
    for name, fn in [("toc.png", toc), ("fig-ivar.png", fig_ivar),
                     ("fig-align.png", fig_align), ("fig-controls.png", fig_controls),
                     ("fig-frame.png", fig_frame)]:
        w, h, inner = fn()
        render_svg(name, w, h, inner)


if __name__ == "__main__":
    main()
