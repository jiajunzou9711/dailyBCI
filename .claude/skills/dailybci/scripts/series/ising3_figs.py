# -*- coding: utf-8 -*-
"""series-ising-01 · 第三期 用最大熵描述群体放电 —— 自制示意图"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ising1_figs as I1
from grounding2_figs import (T, box, line, circ, BG, ACC, ACCD, TINT, INK,
                             BODY, GRAY, LINE, RED, REDT, PANEL, CARD_L)
from ising1_figs import head
import re as _re


def TS(x, y, txt, size=26, fill=INK, anchor="middle", weight="400"):
    """转义 < > &，_{x} 下标、^{x} 上标（可嵌套一层下标）。"""
    t = txt.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = _re.sub(r"_\{([^{}]+)\}", r'<tspan baseline-shift="sub" font-size="72%">\1</tspan>', t)
    t = _re.sub(r"\^\{(.+?)\}(?=[^}]*$)", r'<tspan baseline-shift="super" font-size="68%">\1</tspan>', t)
    return T(x, y, t, size, fill, anchor, weight)

I1.OUT = os.path.join(I1.PROJECT, "output", "series-ising-01", "ep03", "figs")
os.makedirs(I1.OUT, exist_ok=True)
render = I1.render


def table(W, rows, colw, x0, y0, rh, header_fill=TINT, sizes=None, bold_first=True):
    """简单表格：rows[0] 为表头；每格可含 \\n 换行；TS 支持 _{x} 下标。"""
    s = []
    sizes = sizes or [24] * len(colw)
    y = y0
    for r, row in enumerate(rows):
        h = rh[r] if isinstance(rh, list) else rh
        x = x0
        for c, cell in enumerate(row):
            fill = header_fill if r == 0 else (PANEL if c == 0 and bold_first else "#FFFFFF")
            s.append(box(x, y, colw[c], h, fill, LINE, rx=0, sw=1.4))
            lines = cell.split("\n")
            fs = 25 if r == 0 else sizes[c]
            lh = fs * 1.35
            ty = y + h / 2 - (len(lines) - 1) * lh / 2 + fs * 0.35
            for k, ln in enumerate(lines):
                wgt = "700" if (r == 0 or (c == 0 and bold_first)) else "400"
                col = ACCD if r == 0 else (INK if c == 0 else BODY)
                s.append(TS(x + colw[c] / 2, ty + k * lh, ln, fs, col, weight=wgt))
            x += colw[c]
        y += h
    return s, y


# ================================================= 目录
def toc():
    W, H = 960, 600
    s = [T(480, 70, "本期路线", 40, INK, weight="700")]
    s.append(line(120, 100, 840, 100, LINE, 1.8))
    items = [
        ("①", "问题", "描述群体放电需要什么样的模型"),
        ("②", "为什么要用模型", "放电排列多到数不出来"),
        ("③", "为什么是 Ising", "最大熵的唯一解"),
        ("④", "拟合与检验", "两两模型解释了约 90% 的结构"),
        ("⑤", "J 的边界", "不等于相关，也不等于突触"),
    ]
    y = 160
    for n, t, d in items:
        s.append(circ(150, y - 9, 25, TINT, ACC, 2.4))
        s.append(T(150, y + 1, n, 27, ACCD, weight="700"))
        s.append(T(200, y - 4, t, 31, INK, anchor="start", weight="700"))
        s.append(T(200, y + 34, d, 24, BODY, anchor="start"))
        y += 92
    return W, H, "".join(s)


# ================================================= 卡 3 三类模型
def fig3_types():
    W = 960
    rows = [["类型", "回答的问题", "例子"],
            ["描述模型", "what\n神经活动是什么样的", "本期的 Ising 模型"],
            ["机制模型", "how\n解剖、生理和环路\n怎样产生这些活动", "LIF、发放率网络、\nRNN、Hopfield 网络"],
            ["解释模型", "why\n神经系统为什么这样运作", "用信息最大化解释感受野\n（如苍蝇大单极细胞的\n对比度响应）"]]
    s, y = table(W, rows, [180, 360, 360], 30, 20, [56, 96, 130, 130], sizes=[25, 23, 23])
    return W, int(y + 20), "".join(s)


# ================================================= 卡 6 数量对比（对数轴）
def fig6_counts():
    W, H = 960, 360
    s = [head(W, "40 个神经元：排列数远多于数据量")]
    x0, x1, yb = 300, 900, 250
    # 对数轴 10^0 … 10^12
    def X(e): return x0 + (x1 - x0) * e / 12
    s.append(line(x0, yb, x1, yb, GRAY, 2))
    for e in range(0, 13, 2):
        s.append(line(X(e), yb, X(e), yb + 8, GRAY, 2))
        lab = "1" if e == 0 else f"10<tspan baseline-shift=\"super\" font-size=\"68%\">{e}</tspan>"
        s.append(T(X(e), yb + 36, lab, 22, GRAY))
    SUP = '<tspan baseline-shift="super" font-size="68%">{}</tspan>'
    bars = [("时间窗（约 1 小时）", 5.26, ACC, ACCD, "约 1.8 × 10" + SUP.format(5)),
            ("放电排列（2" + SUP.format(40) + " 种）", 12.04, RED, RED, "约 1.1 × 10" + SUP.format(12))]
    for k, (lab, e, col, tcol, val) in enumerate(bars):
        y = 100 + k * 70
        s.append(T(x0 - 16, y + 32, lab, 23, INK, anchor="end", weight="700"))
        s.append(box(x0, y + 8, X(e) - x0, 34, col, col, rx=4, sw=0))
        if k == 0:
            s.append(T(X(e) + 12, y + 33, val, 23, tcol, anchor="start", weight="700"))
        else:
            s.append(T(X(e) - 12, y + 33, val, 23, "#FFFFFF", anchor="end", weight="700"))
    s.append(T(W / 2 + 40, H - 24, "对数刻度；数目是我按原文的约 1 小时记录与 20 ms 时间窗算的", 20, GRAY))
    return W, H, "".join(s)


# ================================================= 卡 8 两神经元 A/B 表
def fig8_ab():
    W = 960
    rows = [["分布", "00", "01", "10", "11", "额外隐含的假设"],
            ["A", "0.5", "0", "0", "0.5", "两者总是同时放电"],
            ["B", "0.25", "0.25", "0.25", "0.25", "无"]]
    s = [head(W, "两个神经元，各自的放电概率都是 0.5", y=40, size=28)]
    t, y = table(W, rows, [110, 120, 120, 120, 120, 300], 35, 70, 64, sizes=[26] * 6)
    s += t
    s.append(T(W / 2, y + 44, "两种分布都满足已知条件；B 的熵最大", 24, ACCD, weight="700"))
    return W, int(y + 70), "".join(s)


# ================================================= 卡 10 公式
def fig10_formula():
    W, H = 960, 250
    s = [box(40, 30, 880, 120, TINT, ACC, rx=16, sw=2)]
    s.append(TS(480, 104, "P(σ) = (1/Z) · exp( Σ_{i} h_{i}σ_{i} + Σ_{i<j} J_{ij}σ_{i}σ_{j} )", 36, INK, weight="700"))
    s.append(TS(330, 200, "h_{i}：40 个，来自放电率约束", 23, ACCD, weight="700"))
    s.append(TS(690, 200, "J_{ij}：780 个，来自两两约束", 23, ACCD, weight="700"))
    return W, H, "".join(s)


# ================================================= 卡 11 h、J、Z 对照
def fig11_symbols():
    W = 960
    rows = [["符号", "来自哪个约束", "在神经数据中", "在物理学中"],
            ["h_{i}", "神经元 i 的放电率", "放电倾向\nh > 0 倾向放电\n原文多数细胞 h 为负²", "外加磁场"],
            ["J_{ij}", "i、j 同时放电的概率", "一起放电的倾向\nJ > 0 倾向一起放电", "原子间的\n相互作用"],
            ["Z", "概率总和为 1", "归一化常数：全部 2^{N}\n种排列的 exp(…) 之和", "配分函数"]]
    s, y = table(W, rows, [120, 250, 350, 180], 30, 20, [56, 124, 100, 100], sizes=[28, 23, 23, 23])
    return W, int(y + 20), "".join(s)


# ================================================= 卡 12 Z 的展开
def fig12_z():
    W, H = 960, 250
    s = [head(W, "两个神经元：Z 是四种排列的权重之和")]
    labels = ["e^{0}", "e^{h_{2}}", "e^{h_{1}}", "e^{h_{1} + h_{2} + J_{12}}"]
    pats = ["00", "01", "10", "11"]
    xs, ws = [180, 340, 500, 735], [130, 130, 130, 260]
    s.append(T(70, 160, "Z =", 34, INK, weight="700"))
    for k in range(4):
        x, w = xs[k], ws[k]
        s.append(box(x - w / 2, 112, w, 76, "#FFFFFF", ACC, rx=12, sw=2))
        s.append(TS(x, 163, labels[k], 34, INK, weight="700"))
        s.append(T(x, 226, pats[k], 26, ACCD, weight="700"))
        if k < 3:
            gx = (x + w / 2 + xs[k + 1] - ws[k + 1] / 2) / 2
            s.append(T(gx, 161, "+", 32, GRAY, weight="700"))
    return W, H, "".join(s)


FIGS = {"toc": toc, "fig3-types": fig3_types, "fig6-counts": fig6_counts, "fig8-ab": fig8_ab,
        "fig10-formula": fig10_formula, "fig11-symbols": fig11_symbols, "fig12-z": fig12_z}

if __name__ == "__main__":
    only = sys.argv[1:] or list(FIGS)
    for name in only:
        W, H, inner = FIGS[name]()
        print(render(name, W, H, inner))
