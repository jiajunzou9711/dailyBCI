"""日报 2026-08-23「语言的神经群体编码」第三期：目录卡 + 五张自制 SVG。"""
import os, subprocess, tempfile
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-08-23-langcode-03", "figs")
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


def circ(cx, cy, r, fill, stroke, sw=1.5):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


_ar = [0]
def arrow(x1, y1, x2, y2, col=GRAY, sw=2.4):
    _ar[0] += 1; i = _ar[0]
    return (f'<defs><marker id="m{i}" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            f'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="{col}"/></marker></defs>'
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" '
            f'stroke-width="{sw}" marker-end="url(#m{i})"/>')


TOC_ITEMS = [
    ("①", "连续的声音，离散的词典"),
    ("②", "中间层解决的两个问题"),
    ("③", "音素效应是怎么被找到的"),
    ("④", "对塞音有反应，也可能只是声学形状"),
    ("⑤", "这类设计分不开的两种情况"),
    ("⑥", "判据：范畴不变性"),
    ("⑦", "不给音素，只给任务"),
    ("⑧", "换一组特征，其他全都一样"),
    ("⑨", "结论是「不必」，强度到此为止"),
    ("⑩", "第二种证据：顺序对上了"),
    ("⑪", "为什么顺序对应更有分量"),
    ("⑫", "作参照的系统要满足三条"),
    ("⑬", "输出连续文本，逼出更高层表征"),
]


def toc():
    s = []; W = 1000
    col_w, row_h, gap = 488, 58, 7
    x0 = [4, 4 + col_w + gap]; y0 = 6
    for i, (num, title) in enumerate(TOC_ITEMS):
        col, row = (0, i) if i < 7 else (1, i - 7)
        x, y = x0[col], y0 + row * (row_h + gap)
        s.append(box(x, y, col_w, row_h, "#F7F9FC", CARD_L, 12, 1.4))
        s.append(circ(x + 34, y + 29, 19, TINT, ACC, 1.4))
        s.append(T(x + 34, y + 37, num, 21, ACCD, weight="700"))
        s.append(T(x + 63, y + 37, title, 21, INK, anchor="start", weight="700"))
    return W, y0 + 7 * (row_h + gap), "".join(s)


def fig_two_cases():
    """卡⑤：两种情况给出同样的观测。"""
    s = []; W, H = 1000, 470
    s.append(T(500, 36, "同一个观测，两种来源", 30, INK, weight="700"))
    s.append(box(30, 70, 380, 150, TINT, ACC))
    s.append(T(220, 112, "情况 A", 26, ACCD, weight="700"))
    s.append(T(220, 155, "皮层以音素为表征单位", 25, INK))
    s.append(T(220, 192, "范畴本身被编码", 22, GRAY))
    s.append(box(30, 250, 380, 150, WARM_T, WARM))
    s.append(T(220, 292, "情况 B", 26, WARM, weight="700"))
    s.append(T(220, 335, "皮层编码连续声学特征", 25, INK))
    s.append(T(220, 372, "音素标签与它高度相关", 22, GRAY))
    s.append(arrow(425, 145, 545, 210, ACC))
    s.append(arrow(425, 325, 545, 262, WARM))
    s.append(box(560, 160, 410, 150, NEU, NEU_S))
    s.append(T(765, 205, "实验观测", 24, GRAY, weight="700"))
    s.append(T(765, 252, "电极反应与音位标签相关", 27, INK, weight="700"))
    s.append(T(765, 290, "两条路径给出同一个结果", 22, GRAY))
    s.append(T(500, 440, "用音位标签当自变量，无法区分 A 与 B", 27, INK, weight="700"))
    return W, H, "".join(s)


def fig_criterion():
    """卡⑥：范畴不变性判据。"""
    import math
    s = []; W, H = 1000, 470
    s.append(T(500, 36, "两种情况会给出不同的反应曲线", 30, INK, weight="700"))
    x0, x1 = 120, 880
    ybase = 300
    # axis
    s.append(f'<line x1="{x0}" y1="{ybase}" x2="{x1}" y2="{ybase}" stroke="{GRAY}" stroke-width="2"/>')
    s.append(T(500, ybase + 42, "声学连续变化（同一范畴内 → 跨过范畴边界）", 23, GRAY))
    xb = (x0 + x1) // 2
    s.append(f'<line x1="{xb}" y1="80" x2="{xb}" y2="{ybase}" stroke="{GRAY}" '
             f'stroke-width="2" stroke-dasharray="7,6"/>')
    s.append(T(xb, 70, "范畴边界", 22, GRAY))
    # continuous (acoustic tuning)
    pts = []
    for i in range(61):
        t = i / 60.0
        x = x0 + t * (x1 - x0)
        y = ybase - 30 - t * 150
        pts.append(f"{x:.1f},{y:.1f}")
    s.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{WARM}" stroke-width="3.4"/>')
    s.append(T(x1 - 10, ybase - 105, "声学调谐 · 跟着声学连续变", 23, WARM, anchor="end", weight="700"))
    # step (categorical)
    step = [f"{x0},{ybase-60}", f"{xb},{ybase-60}", f"{xb},{ybase-215}", f"{x1},{ybase-215}"]
    s.append(f'<polyline points="{" ".join(step)}" fill="none" stroke="{ACC}" stroke-width="3.4"/>')
    s.append(T(x0 + 10, ybase - 82, "音素表征 · 范畴内一致", 23, ACC, anchor="start", weight="700"))
    s.append(T(500, 400, "同一个 /d/，男声女声快说慢说，反应是否一致", 25, INK))
    s.append(T(500, 440, "跨过边界时，反应是否出现突变", 25, INK))
    return W, H, "".join(s)


def fig_controlled():
    """卡⑧：受控对照的结构。"""
    s = []; W, H = 1000, 460
    s.append(T(500, 36, "唯一变动的是特征从哪来", 30, INK, weight="700"))
    s.append(box(30, 70, 300, 130, NEU, NEU_S))
    s.append(T(180, 112, "手工设计的特征", 25, GRAY, weight="700"))
    s.append(T(180, 155, "谱时滤波器", 27, INK, weight="700"))
    s.append(T(180, 186, "人按理论定好", 20, GRAY))
    s.append(box(30, 250, 300, 130, WARM_T, WARM))
    s.append(T(180, 292, "任务训练出的特征", 25, WARM, weight="700"))
    s.append(T(180, 335, "网络内部层激活", 27, INK, weight="700"))
    s.append(T(180, 366, "没有人设计过", 20, WARM))
    s.append(arrow(345, 135, 425, 190))
    s.append(arrow(345, 315, 425, 262, WARM))
    s.append(box(440, 150, 250, 150, TINT, ACC))
    s.append(T(565, 195, "同一套编码模型", 24, ACCD, weight="700"))
    s.append(T(565, 235, "线性回归", 25, INK))
    s.append(T(565, 272, "留出数据上算相关", 21, GRAY))
    s.append(arrow(700, 225, 775, 225, ACC))
    s.append(box(790, 150, 180, 150, NEU, NEU_S))
    s.append(T(880, 200, "同一批", 24, GRAY))
    s.append(T(880, 240, "fMRI 体素", 26, INK, weight="700"))
    s.append(T(880, 278, "同一批声音", 21, GRAY))
    s.append(T(500, 432, "结果：网络特征在整个听觉皮层都优于谱时滤波器", 27, INK, weight="700"))
    return W, H, "".join(s)


def fig_hierarchy():
    """卡⑩：网络层序与皮层层级的对应。"""
    s = []; W, H = 1000, 430
    s.append(T(500, 36, "两个独立确定的顺序", 30, INK, weight="700"))
    # network layers
    labels = ["早层", "中间层", "晚层"]
    for i, lb in enumerate(labels):
        x = 140 + i * 250
        s.append(box(x - 95, 80, 190, 86, WARM_T, WARM))
        s.append(T(x, 118, lb, 26, WARM, weight="700"))
        s.append(T(x, 150, "网络", 21, GRAY))
        if i < 2:
            s.append(arrow(x + 100, 123, x + 150, 123, WARM, 2.2))
    # cortex
    cx = [("初级听皮层", 265), ("非初级听皮层", 640)]
    for name, x in cx:
        s.append(box(x - 150, 268, 300, 86, TINT, ACC))
        s.append(T(x, 306, name, 26, ACCD, weight="700"))
        s.append(T(x, 338, "皮层", 21, GRAY))
    s.append(arrow(420, 311, 484, 311, ACC, 2.2))
    # correspondence
    s.append(f'<line x1="390" y1="170" x2="290" y2="262" stroke="{GRAY}" '
             f'stroke-width="2.6" stroke-dasharray="7,6"/>')
    s.append(f'<line x1="640" y1="170" x2="640" y2="262" stroke="{GRAY}" '
             f'stroke-width="2.6" stroke-dasharray="7,6"/>')
    s.append(T(500, 404, "初级由中间层最佳预测，非初级由晚层最佳预测", 27, INK, weight="700"))
    return W, H, "".join(s)


def fig_pathways():
    """卡⑬：两条通路的终点不同。"""
    s = []; W, H = 1000, 440
    s.append(T(500, 36, "通路走到哪里，决定能对照到哪一级", 30, INK, weight="700"))
    # Kell
    s.append(T(80, 118, "Kell 2018", 25, GRAY, anchor="start", weight="700"))
    kw = [150, 150, 200]
    for i, lb in enumerate(["声波", "网络内部", "词 / 音乐类型"]):
        x = 330 + i * 225
        w = kw[i]
        s.append(box(x - w // 2, 88, w, 62, NEU, NEU_S))
        s.append(T(x, 126, lb, 24, INK))
        if i < 2:
            s.append(arrow(x + w // 2 + 8, 119, x + 225 - kw[i + 1] // 2 - 10, 119))
    s.append(T(500, 190, "能对照的手工特征只到声学一级", 23, GRAY))
    # Whisper
    s.append(T(80, 300, "Whisper", 25, WARM, anchor="start", weight="700"))
    for i, lb in enumerate(["声波", "音频编码器", "文本解码器", "连续文本"]):
        x = 300 + i * 200
        s.append(box(x - 78, 270, 156, 62, WARM_T, WARM))
        s.append(T(x, 308, lb, 23, INK))
        if i < 3:
            s.append(arrow(x + 84, 301, x + 200 - 84, 301, WARM))
    s.append(T(500, 372, "编码器一侧对照音素，解码器一侧对照词性", 23, WARM))
    s.append(T(500, 418, "同一套对照逻辑，换一层手工特征", 27, INK, weight="700"))
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
    for name, fn in [("toc.png", toc), ("fig-two-cases.png", fig_two_cases),
                     ("fig-criterion.png", fig_criterion), ("fig-controlled.png", fig_controlled),
                     ("fig-hierarchy.png", fig_hierarchy), ("fig-pathways.png", fig_pathways)]:
        w, h, inner = fn()
        render_svg(name, w, h, inner)


if __name__ == "__main__":
    main()
