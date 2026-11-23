# -*- coding: utf-8 -*-
"""2026-11-23 原理期 · 脑电芯片的增益和 ADC 设置 —— 自制示意图

参数：Intan RHD2000 datasheet（2023-12-08 更新）；TI ADS1299 SBAS499C（2017）。
示意参数（3 位 ADC、0–8 mV、增益 20 等）与派生数值为自算，正文已注明。
"""
import os, sys, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ising1_figs as I1
from grounding2_figs import (T, box, line, circ, path, BG, ACC, ACCD, TINT, INK,
                             BODY, GRAY, LINE, RED, REDT, PANEL, CARD_L)

I1.OUT = os.path.join(I1.PROJECT, "output", "2026-11-18-amplify-before-adc", "figs")
os.makedirs(I1.OUT, exist_ok=True)
render = I1.render
head = I1.head


def arrow(x1, y1, x2, y2, col=GRAY, sw=2.6):
    ang = math.atan2(y2 - y1, x2 - x1)
    a, L = 0.45, 14
    p1 = (x2 - L * math.cos(ang - a), y2 - L * math.sin(ang - a))
    p2 = (x2 - L * math.cos(ang + a), y2 - L * math.sin(ang + a))
    return (line(x1, y1, x2 - 6 * math.cos(ang), y2 - 6 * math.sin(ang), col, sw)
            + path(f"M{p1[0]:.1f},{p1[1]:.1f} L{x2},{y2} L{p2[0]:.1f},{p2[1]:.1f} Z", col, 1, fill=col))


def chip(x, y, w, h, txt, kind="acc", size=26):
    fill, st, col = {"acc": (TINT, ACC, ACCD), "red": (REDT, RED, RED),
                     "gray": ("#EEEEEE", GRAY, BODY), "ink": ("#FFFFFF", INK, INK)}[kind]
    return box(x, y, w, h, fill, st, rx=10, sw=2) + T(x + w / 2, y + h / 2 + size * 0.36, txt, size, col, weight="700")


# ================================================= 目录
def toc():
    W, H = 960, 600
    s = [T(480, 66, "本期路线", 40, INK, weight="700"), line(120, 96, 840, 96, LINE, 1.8)]
    items = [("①", "ADC 做什么", "把电压转换成所在档的编号"),
             ("②", "放大器做什么", "把电压乘以增益"),
             ("③", "为什么先放大", "取整丢掉的差别无法恢复"),
             ("④", "大增益，挡掉直流", "Intan RHD2000"),
             ("⑤", "小增益，高位数", "TI ADS1299")]
    y = 152
    for n, t, d in items:
        s += [circ(150, y - 9, 25, TINT, ACC, 2.4), T(150, y + 1, n, 27, ACCD, weight="700"),
              T(200, y - 4, t, 31, INK, anchor="start", weight="700"),
              T(200, y + 32, d, 24, BODY, anchor="start")]
        y += 90
    return W, H, "".join(s)


# ================================================= 卡 4 ADC 分档
def fig_adc():
    W, H = 960, 400
    s = [head(W, "3.2 mV 与 3.7 mV 落在同一档，都输出 3", y=44)]
    x0, x1, yb = 80, 880, 230
    bw = (x1 - x0) / 8
    for k in range(8):
        hi = k == 3
        s.append(box(x0 + k * bw, yb - 60, bw, 60, REDT if hi else TINT, RED if hi else ACC, rx=0, sw=2))
        s.append(T(x0 + k * bw + bw / 2, yb - 20, str(k), 28, RED if hi else ACCD, weight="700"))
    for v in range(9):
        x = x0 + v * bw
        s.append(line(x, yb, x, yb + 10, INK, 2))
        s.append(T(x, yb + 38, str(v), 22, BODY))
    s.append(T(x1 + 2, yb + 70, "输入电压（mV）", 21, GRAY, anchor="end"))
    s.append(T(x0 - 6, yb - 72, "ADC 输出", 21, GRAY, anchor="start"))
    for v, col in [(3.2, RED), (3.7, RED), (6.9, ACC)]:
        x = x0 + v * bw
        s.append(arrow(x, 112, x, yb - 64, col, 2.6))
        s.append(T(x, 104, f"{v}", 22, col, weight="700"))
    s.append(T(480, 380, "3 位 ADC，量程 0–8 mV，档宽 1 mV（示意参数）", 22, GRAY))
    return W, H, "".join(s)


# ================================================= 卡 7 两种顺序
def fig_order(cover=False):
    W, H = 960, 460
    s = [] if cover else [head(W, "先 ADC，差别已丢；先放大，ADC 能区分", y=44)]
    oy = -40 if cover else 0
    rows = [("先 ADC、后放大", [("ADC", "gray"), ("× 20", "gray")], ["0", "0"], ["0", "0"], "red", "分不开"),
            ("先放大、后 ADC", [("× 20", "acc"), ("ADC", "acc")], ["6.4 mV", "7.4 mV"], ["6", "7"], "acc", "能区分")]
    y = 100 + oy
    for lab, steps, mid, outv, kind, verdict in rows:
        s.append(T(60, y + 4, lab, 26, INK, anchor="start", weight="700"))
        yy = y + 30
        s.append(chip(60, yy, 150, 44, "0.32 mV", "ink", 24))
        s.append(chip(60, yy + 56, 150, 44, "0.37 mV", "ink", 24))
        s.append(arrow(220, yy + 50, 262, yy + 50))
        s.append(chip(268, yy + 22, 100, 56, steps[0][0], steps[0][1], 26))
        s.append(arrow(376, yy + 50, 418, yy + 50))
        c1 = "red" if kind == "red" else "acc"
        s.append(chip(424, yy, 130, 44, mid[0], c1 if kind == "red" else "ink", 24))
        s.append(chip(424, yy + 56, 130, 44, mid[1], c1 if kind == "red" else "ink", 24))
        s.append(arrow(562, yy + 50, 604, yy + 50))
        s.append(chip(610, yy + 22, 100, 56, steps[1][0], steps[1][1], 26))
        s.append(arrow(718, yy + 50, 760, yy + 50))
        s.append(chip(766, yy, 90, 44, outv[0], kind, 24))
        s.append(chip(766, yy + 56, 90, 44, outv[1], kind, 24))
        s.append(T(880, yy + 58, verdict, 24, RED if kind == "red" else ACCD, anchor="start", weight="700"))
        y += 170
    if not cover:
        s.append(T(480, 440, "档宽 1 mV，增益 20（示意参数）", 22, GRAY))
    return W, H, "".join(s)


# ================================================= 卡 8 Intan 电极端档宽
def fig_intan():
    W, H = 960, 430
    s = [head(W, "ADC 一档折算到电极端，要除以增益", y=44)]
    y = 110
    s.append(chip(60, y, 250, 80, "电极端 0.195 µV", "red", 27))
    s.append(arrow(320, y + 40, 400, y + 40, ACC))
    s.append(chip(410, y + 6, 140, 68, "× 192", "acc", 28))
    s.append(arrow(560, y + 40, 640, y + 40, ACC))
    s.append(chip(650, y, 250, 80, "ADC 端 37.4 µV", "acc", 27))
    s.append(T(775, y + 112, "= ADC 的一档", 22, ACCD))
    s.append(T(185, y + 112, "= 电极端档宽", 22, RED))
    # 档宽与放大器噪声对比
    yb = 330; x0 = 120; sc = 250  # px per µV
    s.append(T(60, yb - 50, "与放大器噪声对比（电极端）", 23, INK, anchor="start", weight="700"))
    s.append(box(x0 + 200, yb - 24, 0.195 * sc, 30, REDT, RED, rx=4, sw=2))
    s.append(T(x0 + 190, yb - 2, "档宽 0.195 µV", 22, RED, anchor="end"))
    s.append(box(x0 + 200, yb + 22, 2.4 * sc, 30, "#EEEEEE", GRAY, rx=4, sw=2))
    s.append(T(x0 + 190, yb + 44, "噪声 2.4 µV rms", 22, BODY, anchor="end"))
    s.append(T(480, 418, "Intan RHD2000 手册参数；37.4 µV 为按量程与位数自算；两条按同一比例画", 19, GRAY))
    return W, H, "".join(s)


# ================================================= 卡 9 削顶
def fig_clip():
    W, H = 960, 400
    s = [head(W, "放大后超出 ADC 量程的部分被削平", y=44)]
    x0, x1, yc, A, lim = 60, 740, 225, 130, 85
    s.append(line(x0, yc - lim, x1 + 20, yc - lim, GRAY, 2, dash="8 6"))
    s.append(line(x0, yc + lim, x1 + 20, yc + lim, GRAY, 2, dash="8 6"))
    s.append(T(x1 + 34, yc - lim + 8, "ADC 量程上限", 22, BODY, anchor="start"))
    s.append(T(x1 + 34, yc + lim + 8, "ADC 量程下限", 22, BODY, anchor="start"))
    ideal, clip = [], []
    for i in range(401):
        x = x0 + (x1 - x0) * i / 400
        v = A * math.sin(2 * math.pi * 2.5 * i / 400)
        ideal.append(f"{x:.1f},{yc - v:.1f}")
        clip.append(f"{x:.1f},{yc - max(-lim, min(lim, v)):.1f}")
    s.append(path("M" + " L".join(ideal), GRAY, 2.2, dash="7 6"))
    s.append(path("M" + " L".join(clip), RED, 3.2))
    s.append(T(480, 386, "红线：ADC 记录到的波形；虚线：放大后的原始波形（示意）", 21, GRAY))
    return W, H, "".join(s)


# ================================================= 卡 11 高通幅频
def fig_hp():
    W, H = 960, 480
    s = [head(W, "截止频率处，输出幅值降到输入的约 70.7%", y=44)]
    x0, x1, top, bot = 120, 880, 90, 350
    fmin, fmax, fc = 1.0, 1e4, 250.0
    def X(f): return x0 + (math.log10(f) - math.log10(fmin)) / (math.log10(fmax) - math.log10(fmin)) * (x1 - x0)
    def Y(g): return bot - g * (bot - top)
    s.append(line(x0, bot, x1, bot, LINE, 1.8)); s.append(line(x0, top - 10, x0, bot, LINE, 1.8))
    for f, lab in [(1, "1"), (10, "10"), (100, "100"), (1000, "1 k"), (10000, "10 k")]:
        s.append(line(X(f), bot, X(f), bot + 8, INK, 1.6))
        s.append(T(X(f), bot + 32, lab, 21, BODY))
    s.append(T(x1, bot + 66, "频率（Hz，对数坐标）", 20, GRAY, anchor="end"))
    for g, lab in [(0, "0"), (0.5, "50%"), (1, "100%")]:
        s.append(T(x0 - 10, Y(g) + 7, lab, 20, BODY, anchor="end"))
    s.append(T(x0 - 10, top - 22, "输出/输入", 20, GRAY, anchor="start"))
    pts = []
    for i in range(301):
        f = 10 ** (i / 300 * 4)
        g = f / math.sqrt(f * f + fc * fc)
        pts.append(f"{X(f):.1f},{Y(g):.1f}")
    s.append(path("M" + " L".join(pts), ACC, 3.4))
    gx, gy = X(fc), Y(1 / math.sqrt(2))
    s.append(line(gx, gy, gx, bot, RED, 2, dash="6 5"))
    s.append(line(x0, gy, gx, gy, RED, 2, dash="6 5"))
    s.append(circ(gx, gy, 7, RED, RED, 1))
    s.append(T(gx + 14, gy + 34, "截止频率 250 Hz", 22, RED, anchor="start", weight="700"))
    s.append(T(x0 + 16, gy - 10, "70.7%", 21, RED, anchor="start"))
    s.append(T(480, 466, "一阶高通滤波器，截止频率按 Intan 记录动作电位时的下限 250 Hz 画（示意）", 19, GRAY))
    return W, H, "".join(s)


# ================================================= 卡 12 两种做法对照
def fig_routes():
    W, H = 960, 470
    s = [head(W, "两种做法：大增益挡直流，小增益高位数保留直流", y=44)]
    cols = [(60, 300, ""), (360, 270, "Intan RHD2000"), (630, 270, "ADS1299（增益 24）")]
    rows = [("增益", "192", "24"), ("ADC 位数", "16", "24"),
            ("电极端输入范围", "±5.0 mV", "±187.5 mV"), ("电极端档宽", "0.195 µV", "约 0.022 µV"),
            ("直流偏置", "电容挡掉", "保留")]
    y = 84
    s.append(box(360, y, 270, 52, TINT, ACC, rx=8, sw=2)); s.append(T(495, y + 35, cols[1][2], 25, ACCD, weight="700"))
    s.append(box(630, y, 270, 52, "#EEF5EF", "#2E7D57", rx=8, sw=2)); s.append(T(765, y + 35, cols[2][2], 25, "#2E7D57", weight="700"))
    y += 64
    for i, (a, b, c) in enumerate(rows):
        if i % 2 == 0:
            s.append(box(60, y, 840, 56, PANEL, PANEL, rx=6, sw=1))
        s.append(T(80, y + 37, a, 25, INK, anchor="start", weight="700"))
        s.append(T(495, y + 37, b, 26, BODY))
        s.append(T(765, y + 37, c, 26, BODY))
        y += 58
    s.append(T(480, 456, "参数取自两款芯片手册；ADS1299 的输入范围与档宽按手册公式自算", 20, GRAY))
    return W, H, "".join(s)


if __name__ == "__main__":
    for name, fn in [("toc", toc), ("fig_adc", fig_adc), ("fig_order", fig_order),
                     ("fig_intan", fig_intan), ("fig_clip", fig_clip), ("fig_hp", fig_hp),
                     ("fig_routes", fig_routes)]:
        W, H, inner = fn(); print(render(name, W, H, inner))
    W, H, inner = fig_order(cover=True); print(render("cover", W, 360, inner))
