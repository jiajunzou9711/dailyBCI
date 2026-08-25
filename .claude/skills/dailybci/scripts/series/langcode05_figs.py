# -*- coding: utf-8 -*-
"""日报 2026-08-25「语言的神经群体编码」第五期：目录卡 + 八张自制 SVG。"""
import os, math, subprocess, tempfile
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-08-25-langcode-05", "figs")
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


def vline(x, y1, y2, col=GRAY, sw=2, dash="6,5"):
    return (f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{col}" '
            f'stroke-width="{sw}" stroke-dasharray="{dash}"/>')


# --------------------------------------------------------------------------
TOC_ITEMS = [
    ("①", "要检验的那一步", "「大脑会预测下一个词」听起来简单"),
    ("②③", "结论先给，以及为什么值得做", "词前有动作，但它是连续的、概率性的预期"),
    ("④–⑨", "分结论 A", "词出现之前，活动里确实有关于这个词的信息"),
    ("⑩–⑫", "分结论 B", "这份信息不能由前文解释"),
    ("⑬–⑮", "分结论 C", "它不是那个词被提前激活"),
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


# ④ 两种解释都相容
def fig_two_accounts():
    s = []; W, H = 1000, 430
    s.append(T(500, 38, "两种说法对 N400 的预期完全一样", 29, INK, weight="700"))
    # 时间轴
    y = 300
    s.append(f'<line x1="70" y1="{y}" x2="930" y2="{y}" stroke="{GRAY}" stroke-width="2.2"/>')
    s.append(vline(480, 90, y + 14, ACC, 2.4))
    s.append(T(480, 340, "看到或听到这个词", 22, ACCD, weight="700"))
    s.append(T(480, 368, "（word onset）", 20, GRAY))
    s.append(T(760, 340, "N400", 24, WARM, weight="700"))
    s.append(T(760, 368, "onset 后约 400 ms", 20, GRAY))
    s.append(vline(760, 250, y + 14, WARM, 2.2))
    s.append(T(140, 340, "词出现之前", 22, GRAY))

    s.append(box(70, 92, 380, 66, TINT, ACC))
    s.append(T(260, 122, "预期说：这里就开始工作", 24, ACCD, weight="700"))
    s.append(T(260, 148, "词到来前已准备好表征", 20, GRAY))

    s.append(box(510, 92, 420, 66, WARM_T, WARM))
    s.append(T(720, 122, "事后整合说：这里才开始工作", 24, WARM, weight="700"))
    s.append(T(720, 148, "词到了才接进语境", 20, GRAY))

    s.append(box(70, 186, 860, 46, NEU, NEU_S, 10, 1.4))
    s.append(T(500, 216, "两者都预测：越难预测的词，N400 负得越深", 24, INK, weight="700"))
    return W, H, "".join(s)


# ⑤ 把时间轴挪到词前
def fig_design():
    s = []; W, H = 1000, 400
    s.append(T(500, 38, "每个时间偏移各拟合一次编码模型", 29, INK, weight="700"))
    y = 210
    s.append(f'<line x1="70" y1="{y}" x2="930" y2="{y}" stroke="{GRAY}" stroke-width="2.2"/>')
    s.append(vline(620, 86, y + 60, ACC, 2.4))
    s.append(T(620, 296, "word onset", 22, ACCD, weight="700"))
    for i, lab in enumerate(["−1000", "−600", "−200", "0", "+400", "+800"]):
        x = 110 + i * 128
        s.append(f'<line x1="{x}" y1="{y-8}" x2="{x}" y2="{y+8}" stroke="{GRAY}" stroke-width="2"/>')
        s.append(T(x, y + 34, lab, 20, GRAY))
        s.append(box(x - 26, y - 62, 52, 44, TINT if x < 620 else NEU,
                     ACC if x < 620 else NEU_S, 8, 1.4))
        s.append(T(x, y - 34, "拟合", 19, INK))
    s.append(T(500, y + 66, "时间偏移（ms，相对 word onset）", 21, GRAY))

    s.append(box(70, 320, 860, 60, "#FFFFFF", CARD_L, 12, 1.4))
    s.append(T(500, 348, "自变量：这个词的嵌入　　因变量：该偏移处的神经活动", 23, INK))
    s.append(T(500, 372, "看偏移为负的区间，预测相关是否已显著高于零", 22, ACCD, weight="700"))
    return W, H, "".join(s)


# ⑦ 样本表
def fig_samples():
    s = []; W, H = 1000, 400
    s.append(T(500, 38, "一个词就是一个样本", 29, INK, weight="700"))
    cols = [(70, 150, "样本"), (220, 190, "词"), (410, 300, "该词的嵌入（示意）"),
            (710, 220, "onset−200 ms 的活动值")]
    s.append(box(70, 66, 860, 52, TINT, ACC, 10, 1.4))
    for x, w, lab in cols:
        s.append(T(x + w / 2, 99, lab, 22, ACCD, weight="700"))
    rows = [("1", "累", "(0.7, −0.2, 0.1)", "32"),
            ("2", "睡着", "(0.1, 0.9, −0.3)", "41"),
            ("3", "了", "(−0.4, 0.2, 0.8)", "27"),
            ("…", "…", "…", "…"),
            ("3000", "门", "(0.5, 0.5, 0.0)", "35")]
    for i, r in enumerate(rows):
        y = 118 + i * 46
        s.append(box(70, y, 860, 46, "#FFFFFF" if i % 2 == 0 else NEU, CARD_L, 0, 1.1))
        for (x, w, _), v in zip(cols, r):
            s.append(T(x + w / 2, y + 31, v, 22, INK))
    s.append(box(70, 356, 860, 40, WARM_T, WARM, 10, 1.4))
    s.append(T(500, 383, "语料里三千个词，就有三千个样本", 23, WARM, weight="700"))
    return W, H, "".join(s)


# ⑧ 一组权重
def fig_weights():
    s = []; W, H = 1000, 400
    s.append(T(500, 38, "全体词共用同一组权重", 29, INK, weight="700"))
    s.append(box(70, 66, 860, 52, TINT, ACC, 10, 1.4))
    s.append(T(500, 99, "预测值 = 10·x₁ + 20·x₂ + 5·x₃ + 25", 25, ACCD, weight="700"))
    rows = [("累", "(0.7, −0.2, 0.1)", "25 + 7 − 4 + 0.5", "28.5"),
            ("睡着", "(0.1, 0.9, −0.3)", "25 + 1 + 18 − 1.5", "42.5"),
            ("了", "(−0.4, 0.2, 0.8)", "25 − 4 + 4 + 4", "29")]
    for i, (w_, x_, calc, val) in enumerate(rows):
        y = 132 + i * 56
        s.append(box(70, y, 860, 50, "#FFFFFF", CARD_L, 8, 1.2))
        s.append(T(120, y + 33, w_, 23, INK))
        s.append(T(320, y + 33, x_, 22, GRAY))
        s.append(T(600, y + 33, calc, 22, INK))
        s.append(T(860, y + 33, val, 24, ACCD, weight="700"))
    s.append(box(70, 310, 860, 84, NEU, NEU_S, 12, 1.4))
    s.append(T(500, 344, "不同的词得到不同的预测值，因为它们的 x 不同", 24, INK, weight="700"))
    s.append(T(500, 376, "若每个词各有一组权重，留出的新词一个也预测不了", 22, GRAY))
    return W, H, "".join(s)


# ⑨ 结果曲线
def fig_curve():
    s = []; W, H = 1000, 420
    s.append(T(500, 38, "预测相关在 word onset 之前就开始上升", 29, INK, weight="700"))
    x0, x1, yb, yt = 110, 930, 300, 86
    s.append(f'<line x1="{x0}" y1="{yb}" x2="{x1}" y2="{yb}" stroke="{GRAY}" stroke-width="2.2"/>')
    s.append(f'<line x1="{x0}" y1="{yb}" x2="{x0}" y2="{yt}" stroke="{GRAY}" stroke-width="2.2"/>')
    xo = 560  # onset 位置
    s.append(vline(xo, yt - 4, yb, ACC, 2.4))
    s.append(T(xo, yb + 30, "word onset", 21, ACCD, weight="700"))
    s.append(T(x0 - 6, yb + 30, "−1000 ms", 20, GRAY, anchor="start"))
    s.append(T(x1, yb + 30, "+800 ms", 20, GRAY))
    s.append(T(x0 - 18, yt + 6, "r", 22, GRAY, anchor="end"))
    s.append(T(x0 - 18, yb + 6, "0", 20, GRAY, anchor="end"))
    pts = []
    for i in range(121):
        x = x0 + (x1 - x0) * i / 120
        t = (x - xo) / 200.0
        v = math.exp(-((t - 0.6) ** 2) / 1.5)
        y = yb - (yb - yt) * 0.92 * v
        pts.append(f"{x:.1f},{y:.1f}")
    s.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{WARM}" stroke-width="3.4"/>')
    # 标出词前抬起的位置
    s.append(f'<circle cx="{xo-120}" cy="{yb - (yb-yt)*0.92*math.exp(-((-120/200.0-0.6)**2)/1.5):.1f}" r="7" fill="{WARM}"/>')
    s.append(T(xo - 210, 150, "这一段已经显著", 22, WARM, weight="700"))
    s.append(T(xo - 210, 178, "高于零", 22, WARM, weight="700"))
    s.append(box(70, 366, 860, 44, WARM_T, WARM, 10, 1.4))
    s.append(T(500, 395, "曲线形状为示意，非原文数值", 22, GRAY))
    return W, H, "".join(s)


# ⑩ 虚假相关
def fig_confound():
    s = []; W, H = 1000, 400
    s.append(T(500, 38, "相关经由前文这个共同来源产生", 29, INK, weight="700"))
    s.append(box(370, 76, 260, 66, TINT, ACC))
    s.append(T(500, 106, "已出现的前文", 25, ACCD, weight="700"))
    s.append(T(500, 132, "被试刚听完的那几个词", 20, GRAY))

    s.append(box(70, 236, 320, 76, "#FFFFFF", CARD_L))
    s.append(T(230, 268, "那一刻的神经活动", 24, INK, weight="700"))
    s.append(T(230, 296, "由已出现的前文驱动", 20, GRAY))

    s.append(box(610, 236, 320, 76, "#FFFFFF", CARD_L))
    s.append(T(770, 268, "尚未出现的词的嵌入", 24, INK, weight="700"))
    s.append(T(770, 296, "与前文统计相关", 20, GRAY))

    s.append(arrow(440, 148, 260, 230, ACC))
    s.append(arrow(560, 148, 740, 230, ACC))
    s.append(f'<line x1="390" y1="274" x2="610" y2="274" stroke="{WARM}" '
             f'stroke-width="3" stroke-dasharray="8,6"/>')
    s.append(T(500, 262, "观测到的相关", 22, WARM, weight="700"))

    s.append(box(70, 336, 860, 56, WARM_T, WARM, 12, 1.4))
    s.append(T(500, 372, "中间不需要任何预测这一环", 25, WARM, weight="700"))
    return W, H, "".join(s)


# ⑪ 双词搭配
def fig_bigram():
    s = []; W, H = 1000, 420
    s.append(T(500, 38, "近乎确定的搭配也能造出相关", 29, INK, weight="700"))
    s.append(T(500, 70, "设语料里「圣诞」之后 90% 跟的是「节」", 22, GRAY))
    cols = [(70, 200, "前一个词"), (270, 150, "W"), (420, 220, "W 的嵌入"), (640, 290, "onset−200 ms 的活动值")]
    s.append(box(70, 88, 860, 48, TINT, ACC, 10, 1.4))
    for x, w, lab in cols:
        s.append(T(x + w / 2, 118, lab, 21, ACCD, weight="700"))
    rows = [("圣诞", "节", "x_节", "50"), ("圣诞", "节", "x_节", "49"),
            ("圣诞", "树", "x_树", "51"), ("昨天", "下雨", "x_下雨", "30"),
            ("我们", "出发", "x_出发", "29"), ("桌上", "有", "x_有", "31")]
    for i, r in enumerate(rows):
        y = 136 + i * 40
        s.append(box(70, y, 860, 40, "#FFFFFF" if i < 3 else NEU, CARD_L, 0, 1.1))
        for (x, w, _), v in zip(cols, r):
            s.append(T(x + w / 2, y + 27, v, 21, INK))
    s.append(box(70, 382, 860, 36, WARM_T, WARM, 10, 1.4))
    s.append(T(500, 407, "那一刻大脑在处理「圣诞」，对「节」什么都没做", 22, WARM, weight="700"))
    return W, H, "".join(s)


# ⑫ 残差
def fig_residual():
    s = []; W, H = 1000, 380
    s.append(T(500, 38, "先减掉前文能解释的部分，再问剩下的", 29, INK, weight="700"))
    s.append(box(70, 80, 400, 84, TINT, ACC))
    s.append(T(270, 114, "第一步", 24, ACCD, weight="700"))
    s.append(T(270, 146, "用前面几个词的嵌入预测活动", 21, INK))

    s.append(arrow(478, 122, 528, 122, GRAY))

    s.append(box(536, 80, 394, 84, "#FFFFFF", CARD_L))
    s.append(T(733, 114, "第二步", 24, INK, weight="700"))
    s.append(T(733, 146, "残差 = 实测活动 − 该预测值", 21, INK))

    s.append(box(70, 190, 860, 62, WARM_T, WARM))
    s.append(T(500, 228, "再用 W 的嵌入去预测这个残差", 25, WARM, weight="700"))

    s.append(box(70, 272, 420, 96, NEU, NEU_S, 12, 1.4))
    s.append(T(280, 306, "残差预测不了", 23, GRAY, weight="700"))
    s.append(T(280, 340, "效应本来就来自前文", 21, INK))
    s.append(box(510, 272, 420, 96, "#FFFFFF", ACC, 12, 1.8))
    s.append(T(720, 306, "残差仍能预测", 23, ACCD, weight="700"))
    s.append(T(720, 340, "存在前文解释不了的信息", 21, INK))
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
    for name, fn in [("toc.png", toc), ("fig-two-accounts.png", fig_two_accounts),
                     ("fig-samples.png", fig_samples),
                     ("fig-weights.png", fig_weights), ("fig-confound.png", fig_confound), ("fig-bigram.png", fig_bigram),
                     ("fig-residual.png", fig_residual)]:
        w, h, inner = fn()
        render_svg(name, w, h, inner)


if __name__ == "__main__":
    main()
