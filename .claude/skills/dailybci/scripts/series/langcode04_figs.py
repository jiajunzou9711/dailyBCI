# -*- coding: utf-8 -*-
"""日报 2026-08-24「语言的神经群体编码」第四期：目录卡 + 三张自制 SVG。"""
import os, subprocess, tempfile
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-08-24-langcode-04", "figs")
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


# --------------------------------------------------------------------------
# 目录卡：按稿块归并,比图卡数目少,提纲挈领
# --------------------------------------------------------------------------
TOC_ITEMS = [
    ("①", "要检验的那一步推论", "能解出音素，就说明里面有音素吗"),
    ("②", "装置", "Whisper：编码器管语音，解码器管语言"),
    ("③④⑤", "线一：谁更能预测皮层", "嵌入胜出，以及这个胜出的强度边界"),
    ("⑥", "判据", "解码成功这件事，信息量比想的低"),
    ("⑦⑧⑨", "线二：符号在不在模型里", "能读出来，内部却没有符号单位"),
    ("⑩⑪⑫", "软层级", "区域层面有分工，位点层面不干净"),
    ("⑬⑭", "结论", "可读出与以该形式存储；层级是有序的梯度"),
]


def toc():
    s = []; W = 1000
    row_h, gap = 92, 12
    x, y0 = 4, 6
    for i, (num, sec, desc) in enumerate(TOC_ITEMS):
        y = y0 + i * (row_h + gap)
        s.append(box(x, y, 992, row_h, "#F7F9FC", CARD_L, 12, 1.4))
        s.append(box(x + 18, y + 20, 118, 52, TINT, ACC, 10, 1.4))
        s.append(T(x + 77, y + 55, num, 24, ACCD, weight="700"))
        s.append(T(x + 156, y + 44, sec, 25, ACCD, anchor="start", weight="700"))
        s.append(T(x + 156, y + 76, desc, 23, INK, anchor="start"))
    return W, y0 + len(TOC_ITEMS) * (row_h + gap), "".join(s)


# --------------------------------------------------------------------------
# 卡②：Whisper 架构
# --------------------------------------------------------------------------
def fig_whisper():
    s = []; W, H = 1000, 430
    s.append(T(500, 40, "编码器一侧处理语音，解码器一侧处理语言", 29, INK, weight="700"))

    # 编码器
    s.append(box(48, 84, 420, 210, TINT, ACC))
    s.append(T(258, 122, "音频编码器", 26, ACCD, weight="700"))
    s.append(box(78, 146, 160, 54, "#FFFFFF", CARD_L, 10))
    s.append(T(158, 180, "早期层", 23, INK))
    s.append(box(278, 146, 160, 54, "#FFFFFF", CARD_L, 10))
    s.append(T(358, 180, "最后一层", 23, INK))
    s.append(T(158, 226, "声学嵌入", 21, ACC))
    s.append(T(358, 226, "语音嵌入", 21, ACC))
    s.append(T(258, 268, "输入：对数梅尔声谱图", 21, GRAY))

    # 解码器
    s.append(box(532, 84, 420, 210, WARM_T, WARM))
    s.append(T(742, 122, "文本解码器", 26, WARM, weight="700"))
    s.append(box(602, 146, 200, 54, "#FFFFFF", CARD_L, 10))
    s.append(T(702, 180, "较晚的中间层", 23, INK))
    s.append(T(702, 226, "上下文词嵌入", 21, WARM))
    s.append(T(742, 268, "输出：连续文本", 21, GRAY))

    s.append(arrow(470, 190, 530, 190, GRAY))
    s.append(T(500, 328, "交叉注意力", 22, GRAY))

    s.append(box(48, 352, 904, 60, NEU, NEU_S, 12, 1.4))
    s.append(T(500, 390, "训练目标只有「音频 → 文本」，标注里没有任何音位或句法标记", 24, INK, weight="700"))
    return W, H, "".join(s)


# --------------------------------------------------------------------------
# 卡⑥：解码成功能承担多少推论
# --------------------------------------------------------------------------
def fig_regime():
    s = []; W, H = 1000, 430
    s.append(T(500, 40, "能不能分开，只取决于点数与维数之比", 29, INK, weight="700"))

    # 三段区间条
    y = 96; h = 74
    segs = [(48, 300, TINT, ACC, "P ≤ N+1", "任意贴法都可分"),
            (348, 300, "#F0F4F9", ACC, "P ≈ 2N", "随机贴法仍大概率可分"),
            (648, 304, NEU, NEU_S, "P ≫ 2N", "可分性迅速消失")]
    for x, w, fill, stroke, lab, desc in segs:
        s.append(box(x, y, w, h, fill, stroke, 10, 1.6))
        s.append(T(x + w / 2, y + 34, lab, 25, INK, weight="700"))
        s.append(T(x + w / 2, y + 62, desc, 21, GRAY))
    s.append(T(500, 206, "N＝表征空间维数　　P＝样本点数", 22, GRAY))

    s.append(box(48, 236, 904, 74, "#FFFFFF", CARD_L, 12, 1.4))
    s.append(T(500, 268, "这个计算里没有出现「标签是什么」", 25, INK, weight="700"))
    s.append(T(500, 296, "标签有没有意义、系统用不用它，都不进入判断", 22, GRAY))

    s.append(box(48, 330, 904, 82, WARM_T, WARM, 12, 1.4))
    s.append(T(500, 364, "所以真实判据是：留出集上显著高于随机", 25, WARM, weight="700"))
    s.append(T(500, 394, "而它给出的推论上限，仍然只到「信息可取到」", 22, INK))
    return W, H, "".join(s)


# --------------------------------------------------------------------------
# 卡⑪：方差分解
# --------------------------------------------------------------------------
def fig_varpart():
    s = []; W, H = 1000, 460
    s.append(T(500, 40, "三个模型，拆出独有与共享", 29, INK, weight="700"))

    rows = [("只用语音嵌入 S", 0.30), ("只用语言嵌入 L", 0.25), ("两组一起 S+L", 0.35)]
    x0, bw = 320, 1500  # 1500 px per 1.0 R²
    for i, (lab, v) in enumerate(rows):
        y = 86 + i * 62
        s.append(T(300, y + 30, lab, 24, INK, anchor="end"))
        s.append(box(x0, y, v * bw, 42, TINT if i < 2 else "#D9E5F3", ACC, 8, 1.4))
        s.append(T(x0 + v * bw + 20, y + 30, f"R² = {v:.2f}", 23, ACCD, anchor="start"))
    s.append(T(500, 292, "示意数字，非原文数值", 20, GRAY))

    # 分解条
    yb = 320
    parts = [("S 独有", 0.10, TINT, ACC), ("共享", 0.20, NEU, NEU_S), ("L 独有", 0.05, WARM_T, WARM)]
    x = x0
    for lab, v, fill, stroke in parts:
        w = v * bw
        s.append(box(x, yb, w, 52, fill, stroke, 8, 1.6))
        s.append(T(x + w / 2, yb + 33, lab, 22, INK, weight="700"))
        s.append(T(x + w / 2, yb + 78, f"{v:.2f}", 21, GRAY))
        x += w
    s.append(T(300, yb + 33, "R²(S+L) 拆开", 24, INK, anchor="end"))

    s.append(box(48, 412, 904, 44, "#FFFFFF", CARD_L, 10, 1.4))
    s.append(T(500, 441, "两块独有方差都显著大于零，才叫混合调谐", 24, INK, weight="700"))
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
    for name, fn in [("toc.png", toc), ("fig-whisper.png", fig_whisper),
                     ("fig-regime.png", fig_regime), ("fig-varpart.png", fig_varpart)]:
        w, h, inner = fn()
        render_svg(name, w, h, inner)


if __name__ == "__main__":
    main()
