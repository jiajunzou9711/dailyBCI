# -*- coding: utf-8 -*-
"""2026-11-25 原理期 · 从有限次 trial 估计概率（二项比例的 95% 置信区间）—— 自制示意图

全部数值为示意例子，区间与 SE 由本脚本按 Wilson / Wald 公式自算（z = 1.96）。
出处：Brown, Cai & DasGupta (2001) Statist. Sci. 16:101–133（Wald 不推荐）。
"""
import os, sys, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ising1_figs as I1
from grounding2_figs import (T, box, line, circ, path, BG, ACC, ACCD, TINT, INK,
                             BODY, GRAY, LINE, RED, REDT, GRN, GRNT, PANEL)

I1.OUT = os.path.join(I1.PROJECT, "output", "2026-11-19-binomial-ci", "figs")
os.makedirs(I1.OUT, exist_ok=True)
render = I1.render
head = I1.head
Z = 1.959964


def wilson(k, n):
    p = k / n; d = 1 + Z * Z / n
    c = (p + Z * Z / (2 * n)) / d
    h = Z * math.sqrt(p * (1 - p) / n + Z * Z / (4 * n * n)) / d
    return c - h, c + h


def wald(k, n):
    p = k / n; se = math.sqrt(p * (1 - p) / n)
    return p - Z * se, p + Z * se


def axis(x0, x1, lo, hi):
    return lambda v: x0 + (v - lo) / (hi - lo) * (x1 - x0)


def ticks(X, y, vals, fmt="{:.1f}", size=21):
    s = [line(X(vals[0]), y, X(vals[-1]), y, INK, 2)]
    for v in vals:
        s += [line(X(v), y, X(v), y + 9, INK, 2), T(X(v), y + 34, fmt.format(v), size, BODY)]
    return s


def bar(X, y, a, b, col, sw=7):
    return (line(X(a), y, X(b), y, col, sw) + line(X(a), y - 14, X(a), y + 14, col, 3)
            + line(X(b), y - 14, X(b), y + 14, col, 3))


# ================================================= 目录
def toc():
    W, H = 960, 600
    s = [T(480, 66, "本期路线", 40, INK, weight="700"), line(120, 96, 840, 96, LINE, 1.8)]
    items = [("①", "同样是 0.8", "可靠程度取决于 trial 数"),
             ("②", "p 与 p̂", "真实概率固定，观测值会变"),
             ("③", "p̂ 的波动", "标准误 SE = √(p(1−p)/n)"),
             ("④", "置信区间", "所有与观测值相容的 p"),
             ("⑤", "Wilson 与 Wald", "两种算法与失效条件"),
             ("⑥", "两条前提", "不成立时区间偏窄")]
    y = 150
    for n, t, d in items:
        s += [circ(150, y - 9, 24, TINT, ACC, 2.4), T(150, y + 1, n, 26, ACCD, weight="700"),
              T(200, y - 4, t, 30, INK, anchor="start", weight="700"),
              T(200, y + 30, d, 23, BODY, anchor="start")]
        y += 76
    return W, H, "".join(s)


# ================================================= 卡 3 同样是 0.8
def fig_same08(cover=False):
    W, H = 960, 330
    s = [] if cover else [head(W, "同样是 0.8，trial 少时区间宽得多", y=44)]
    X = axis(150, 900, 0.4, 1.0)
    yb = 270
    s += [line(X(0.5), 90, X(0.5), yb, GRAY, 2, dash="8,6"), T(X(0.5), 82, "随机水平 0.5", 20, GRAY)]
    for y, (k, n), col in [(140, (8, 10), RED), (210, (800, 1000), ACC)]:
        a, b = wilson(k, n)
        s += [T(60, y + 9, f"{k}/{n}", 26, col, anchor="start", weight="700"), bar(X, y, a, b, col),
              circ(X(0.8), y, 9, col, col, 1),
              T(X(b) + 14 if b < 0.95 else X(a) - 14, y - 18, f"{a:.2f}–{b:.2f}", 21, col,
                anchor="start" if b < 0.95 else "end")]
    s += ticks(X, yb, [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    if not cover:
        s.append(T(480, H - 4, "95% Wilson 区间，作者自算", 19, GRAY))
    return W, H, "".join(s)


# ================================================= 卡 5 抽样分布
def fig_sampling():
    W, H = 960, 400
    s = [head(W, "n 越大，p̂ 的抽样分布越窄", y=44)]
    X = axis(90, 900, 0.5, 1.1)
    yb = 330
    p = 0.83
    for n, col, lab in [(10, GRAY, "n = 10"), (100, ACC, "n = 100"), (1000, RED, "n = 1000")]:
        se = math.sqrt(p * (1 - p) / n)
        peak = 1 / (se * math.sqrt(2 * math.pi))
        scale = 230 / (1 / (0.0119 * math.sqrt(2 * math.pi)))
        pts = []
        for i in range(301):
            v = 0.5 + i * 0.6 / 300
            f = math.exp(-0.5 * ((v - p) / se) ** 2) / (se * math.sqrt(2 * math.pi))
            pts.append(f"{X(v):.1f},{yb - f * scale:.1f}")
        s.append(path("M" + " L".join(pts), col, 3))
        ytop = yb - peak * scale
        lx, ly = {10: (X(0.52), yb - 50), 100: (X(0.88), ytop + 10), 1000: (X(0.86), ytop + 20)}[n]
        s.append(T(lx, ly, f"{lab}，SE ≈ {se:.3f}", 21, col, anchor="start", weight="700"))
    s += [line(X(p), 80, X(p), yb, INK, 1.6, dash="6,6"), T(X(p) - 8, 78, "p = 0.83", 20, INK, anchor="end")]
    s += ticks(X, yb, [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1], size=20)
    s.append(T(480, H - 4, "曲线为正态近似，作者自算", 19, GRAY))
    return W, H, "".join(s)


# ================================================= 卡 6 反推
def fig_invert():
    W, H = 960, 430
    s = [head(W, "0.83 落在其范围内的 p 被保留", y=44)]
    X = axis(200, 900, 0.55, 1.0)
    obs = 0.83
    rows = [(0.70, 130), (0.78, 195), (0.90, 260)]
    s += [line(X(obs), 85, X(obs), 340, INK, 2, dash="6,6"), T(X(obs), 80, "观测值 0.83", 21, INK, weight="700")]
    for p, y in rows:
        se = math.sqrt(p * (1 - p) / 100)
        a, b = p - Z * se, p + Z * se
        keep = a <= obs <= b
        col = GRN if keep else RED
        s += [T(60, y + 9, f"p = {p:.2f}", 24, col, anchor="start", weight="700"), bar(X, y, a, b, col, 6),
              circ(X(p), y, 8, col, col, 1)]
    a, b = wilson(83, 100)
    yc = 325
    s += [bar(X, yc, a, b, ACC, 8), T(60, yc + 9, "95% CI", 24, ACC, anchor="start", weight="700"),
          T(X(b) + 12, yc + 8, f"{a:.3f}–{b:.3f}", 21, ACC, anchor="start")]
    s += ticks(X, 360, [0.6, 0.7, 0.8, 0.9, 1.0], size=20)
    s.append(T(480, H - 4, "绿：保留；红：排除。横条为 p ± 1.96·SE(p)，n = 100，作者自算", 19, GRAY))
    return W, H, "".join(s)


# ================================================= 卡 7 Wald vs Wilson
def fig_wald():
    W, H = 960, 470
    s = [head(W, "n 小或 p̂ 靠边时，Wald 区间失效", y=44)]
    X = axis(230, 880, 0.4, 1.1)
    s += [line(X(1.0), 85, X(1.0), 390, RED, 2, dash="8,6"), T(X(1.0), 80, "p = 1 上限", 20, RED)]
    y = 112
    for k, n in [(83, 100), (8, 10), (10, 10)]:
        s.append(T(30, y + 30, f"{k}/{n}", 24, INK, anchor="start", weight="700"))
        for dy, (nm, f, col) in zip((0, 44), [("Wald", wald, GRAY), ("Wilson", wilson, ACC)]):
            a, b = f(k, n)
            yy = y + dy
            if b - a < 1e-6:
                s.append(circ(X(a), yy, 8, col, col, 1))
            else:
                s.append(bar(X, yy, a, b, col, 6))
            s.append(T(212, yy + 7, nm, 20, col, anchor="end", weight="700"))
        y += 105
    s += ticks(X, 400, [0.4, 0.6, 0.8, 1.0], size=20)
    s.append(T(480, H - 4, "灰：Wald；蓝：Wilson。95% 区间，作者自算", 19, GRAY))
    return W, H, "".join(s)


if __name__ == "__main__":
    only = set(sys.argv[1:])
    for name, fn in [("toc", toc), ("fig_same08", fig_same08), ("fig_sampling", fig_sampling),
                     ("fig_invert", fig_invert), ("fig_wald", fig_wald)]:
        if only and name not in only: continue
        W, H, inner = fn(); print(render(name, W, H, inner))
    if not only or "cover" in only:
        W, H, inner = fig_same08(cover=True); print(render("cover", W, 300, inner))
