# -*- coding: utf-8 -*-
"""series-ising-01 · 第二期 Ising 怎样进入神经网络 —— 自制示意图"""
import os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ising1_figs as I1
from grounding2_figs import (T, box, line, circ, path, BG, ACC, ACCD, TINT, INK,
                             BODY, GRAY, LINE, RED, REDT, GRN, GRNT, CARD_L, PANEL)
from ising1_figs import head, spin

I1.OUT = os.path.join(I1.PROJECT, "output", "series-ising-01", "ep02", "figs")
os.makedirs(I1.OUT, exist_ok=True)
render = I1.render
import re as _re


def TS(x, y, txt, size=26, fill=INK, anchor="middle", weight="400"):
    """T 的变体：txt 里 _{x} 写下标（字体缺 ₁ ᵢ 等字形）。"""
    body = _re.sub(r"_\{(.+?)\}", r'<tspan baseline-shift="sub" font-size="68%">\1</tspan>', txt)
    return T(x, y, body, size, fill, anchor, weight)


# ================================================= 目录
def toc():
    W, H = 960, 600
    s = [T(480, 70, "本期路线", 40, INK, weight="700")]
    s.append(line(120, 100, 840, 100, LINE, 1.8))
    items = [
        ("①", "问题与起点", "简单神经元组成的网络，能否存储记忆"),
        ("②", "Amari 1972", "Hebb 规则让记忆成为稳定排列"),
        ("③", "Little 1974", "神经网络可以写成 Ising 问题"),
        ("④", "Hopfield 1982", "记忆是能量的极小点"),
        ("⑤", "1982 年之后", "吸引子网络、注意力机制与诺贝尔奖"),
    ]
    y = 160
    for n, t, d in items:
        s.append(circ(150, y-9, 25, TINT, ACC, 2.4))
        s.append(T(150, y+1, n, 27, ACCD, weight="700"))
        s.append(T(200, y-4, t, 31, INK, anchor="start", weight="700"))
        s.append(T(200, y+34, d, 24, BODY, anchor="start"))
        y += 92
    return W, H, "".join(s)


# ================================================= 图 A-1 阈值单元
def figA1():
    W, H = 960, 380
    s = [head(W, "阈值单元只根据输入之和决定是否放电")]
    ys = [130, 210, 290]
    for k, y in enumerate(ys):
        s.append(spin(110, y, k != 1))
        s.append(TS(110, y+52, f"σ_{{{k+1}}}", 24, BODY))
        s.append(line(140, y, 380, 214 + (y-210)*0.25, GRAY, 2.6, marker="ahg"))
        s.append(TS(250, (y + 214 + (y-210)*0.25)/2 - 14, f"J_{{{k+1}}}", 26, ACCD, weight="700"))
    s.append(circ(430, 214, 50, TINT, ACC, 2.6))
    s.append(T(430, 228, "Σ", 44, ACCD, weight="700"))
    s.append(T(430, 300, "输入加总", 22, BODY))
    s.append(line(482, 214, 560, 214, INK, 2.6, marker="ahk"))
    s.append(box(568, 164, 170, 100, PANEL, CARD_L, rx=14, sw=2))
    s.append(T(653, 206, "与阈值比较", 24, INK, weight="700"))
    s.append(T(653, 240, "高于 / 低于", 22, BODY))
    s.append(line(740, 214, 800, 214, INK, 2.6, marker="ahk"))
    s.append(spin(850, 180, True)); s.append(T(890, 189, "+1", 24, ACC, anchor="start", weight="700"))
    s.append(spin(850, 252, False)); s.append(T(890, 261, "−1", 24, GRAY, anchor="start", weight="700"))
    s.append(T(866, 310, "放电 / 不放电", 20, BODY))
    return W, H, "".join(s)


# ================================================= 卡 6 J 表
def fig6_table():
    W, H = 960, 420
    s = [TS(W/2, 46, "按 J_{ij} = ξ_{i}ξ_{j} 写出的连接强度", 30, INK, weight="700")]
    xi = [1, 1, -1, -1]
    x0, y0, c = 300, 96, 64
    # 列表头：神经元编号 + 模式取值
    s.append(T(x0 - 46, y0 + 40, "ξ", 30, GRAY, weight="700"))
    for j in range(4):
        cx = x0 + j*c + c/2
        s.append(T(cx, y0 - 8, f"{j+1}", 24, GRAY, weight="700"))
        s.append(spin(cx, y0 + 30, xi[j] > 0, r=18))
    for i in range(4):
        cy = y0 + 92 + i*c
        s.append(T(x0 - 96, cy + 8, f"{i+1}", 24, GRAY, weight="700"))
        s.append(spin(x0 - 46, cy, xi[i] > 0, r=18))
        for j in range(4):
            x = x0 + j*c
            if i == j:
                s.append(box(x+4, cy-28, c-8, c-8, "#F0F0F0", "#E2E2E2", rx=8, sw=1.2))
                s.append(T(x + c/2, cy + 12, "—", 26, GRAY))
            else:
                v = xi[i]*xi[j]
                col, fill = (GRN, GRNT) if v > 0 else (RED, REDT)
                s.append(box(x+4, cy-28, c-8, c-8, fill, col, rx=8, sw=1.6))
                s.append(T(x + c/2, cy + 13, "+1" if v > 0 else "−1", 26, col, weight="700"))
    lx = 620
    s.append(box(lx, 200, 26, 26, GRNT, GRN, rx=5)); s.append(T(lx+40, 220, "同号的一对：+1", 24, GRN, anchor="start", weight="700"))
    s.append(box(lx, 250, 26, 26, REDT, RED, rx=5)); s.append(T(lx+40, 270, "异号的一对：−1", 24, RED, anchor="start", weight="700"))
    s.append(T(lx, 320, "行、列均为神经元编号", 20, GRAY, anchor="start"))
    return W, H, "".join(s)


# ================================================= 图 A-3 周期 ↔ 晶格的行
def figA3():
    W, H = 960, 330
    s = [head(W, "网络的第 t 个周期，对应晶格的第 t 行")]
    s.append(T(200, 100, "神经网络", 22, GRAY, anchor="end"))
    s.append(T(330 + 4*76 + 60, 100, "二维晶格", 22, GRAY, anchor="start"))
    rows = [[1, 1, -1, 1, -1], [1, 1, -1, -1, -1], [1, 1, -1, -1, 1]]
    x0, y0, dx, dy = 330, 132, 76, 70
    # 相邻行之间：每个格点与上一行全部格点相互作用（只画一个格点的连线作示意）
    for r in range(len(rows) - 1):
        tx = x0 + 2*dx
        for j in range(5):
            s.append(line(x0 + j*dx, y0 + r*dy + 22, tx, y0 + (r+1)*dy - 22, LINE, 1.6))
    for r, row in enumerate(rows):
        y = y0 + r*dy
        s.append(T(200, y + 9, f"周期 {r+1}", 26, INK, anchor="end", weight="700"))
        for j, v in enumerate(row):
            s.append(spin(x0 + j*dx, y, v > 0))
        s.append(T(x0 + 4*dx + 60, y + 9, f"第 {r+1} 行", 26, ACCD, anchor="start", weight="700"))
    s.append(T(W/2, y0 + 2*dy + 60, "灰线：一个格点与上一行全部格点相互作用（只画出一个）；同一行内没有相互作用", 20, GRAY))
    return W, H, "".join(s)


# ================================================= 卡 8 单神经元转移矩阵
def fig8_matrix():
    W, H = 960, 360
    s = [head(W, "单个神经元的转移矩阵")]
    x0, y0, cw, ch = 330, 110, 210, 84
    s.append(T(x0 + cw/2, y0 - 12, "下一刻 +1", 24, GRAY, weight="700"))
    s.append(T(x0 + cw*1.5, y0 - 12, "下一刻 −1", 24, GRAY, weight="700"))
    cells = [["1 − a", "a"], ["a", "1 − a"]]
    for i, lab in enumerate(["此刻 +1", "此刻 −1"]):
        y = y0 + i*ch
        s.append(T(x0 - 30, y + ch/2 + 9, lab, 24, GRAY, anchor="end", weight="700"))
        for j in range(2):
            stay = i == j
            s.append(box(x0 + j*cw + 4, y + 4, cw - 8, ch - 8, TINT if stay else PANEL,
                         ACC if stay else CARD_L, rx=10, sw=1.8))
            s.append(T(x0 + j*cw + cw/2, y + ch/2 + 11, cells[i][j], 32, ACCD if stay else INK, weight="700"))
    s.append(TS(480, y0 + 2*ch + 52, "特征值：λ_{1} = 1，λ_{2} = 1 − 2a", 28, INK, weight="700"))
    return W, H, "".join(s)


# ================================================= 图 A-5 能量地形
def figA5():
    W, H = 960, 440
    s = [head(W, "回忆就是网络沿能量下降，停在线索附近的极小点")]
    x0, x1, ytop, ybot = 90, 910, 90, 370
    s.append(line(x0, ybot, x1, ybot, GRAY, 2, marker="ahg"))
    s.append(line(x0, ybot, x0, ytop - 10, GRAY, 2, marker="ahg"))
    s.append(T(x1 - 4, ybot + 34, "网络的排列（示意）", 22, GRAY, anchor="end"))
    s.append(T(x0 + 14, ytop - 2, "E", 26, GRAY, anchor="start", weight="700"))
    xs = np.linspace(x0 + 10, x1 - 20, 300)
    u = (xs - x0) / (x1 - x0)
    E = (0.55 - 0.42*np.exp(-((u - 0.25)/0.08)**2) - 0.48*np.exp(-((u - 0.68)/0.09)**2)
         + 0.25*(u - 0.5)**2)
    # 直接映射：E 越大越靠上
    yy = ybot - 70 - (E - E.min()) / (E.max() - E.min()) * (ybot - ytop - 100)
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in zip(xs, yy))
    s.append(path(d, INK, 3))
    def at(uu):
        k = int(np.argmin(abs(u - uu))); return xs[k], yy[k]
    # 极小点位置
    mins = []
    for lo_, hi_ in ((0.15, 0.35), (0.58, 0.78)):
        m = (u > lo_) & (u < hi_)
        k = np.where(m)[0][np.argmax(yy[m])]
        mins.append((xs[k], yy[k]))
    for (mx, my) in mins[:2]:
        s.append(circ(mx, my - 14, 13, TINT, ACC, 2.4))
        s.append(T(mx, my + 34, "记住的模式", 22, ACCD, weight="700"))
    # 线索：在第二个极小点左上方的斜坡上
    cx, cy = at(0.56)
    s.append(circ(cx, cy - 14, 13, REDT, RED, 2.4))
    s.append(T(cx - 6, cy - 44, "线索", 22, RED, anchor="end", weight="700"))
    mx, my = mins[1]
    seg = [(x, y) for x, y in zip(xs, yy) if cx + 18 <= x <= mx - 18]
    if seg:
        dd = "M" + " L".join(f"{x:.1f},{y - 30:.1f}" for x, y in seg)
        s.append(path(dd, RED, 2.6, dash="7,6", marker="ahr"))
    return W, H, "".join(s)


if __name__ == "__main__":
    for name, fn in [("toc", toc), ("figA1-threshold", figA1), ("fig6-jtable", fig6_table),
                     ("figA3-rows", figA3), ("fig8-matrix", fig8_matrix), ("figA5-landscape", figA5)]:
        W, H, inner = fn()
        print(render(name, W, H, inner))
