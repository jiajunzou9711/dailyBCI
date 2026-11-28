# -*- coding: utf-8 -*-
"""2026-11-28 原理期 · 读懂放大器规格表上的「输入参考噪声」 —— 自制示意图

数值出处：Intan RHD2000 datasheet（2.4 μVrms、增益 192、0.195 μV）；Harrison & Charles 2003
（fc = 100 Hz、21 nV/√Hz、2.2 μVrms）；Neuropixels 1.0 datasheet p.3（5.9 / 9.2 μVrms）；
Henze 2000（≥ 60 μV）；热噪声 12.9 / 2.9 μV 为 √(4kTRB) 自算。曲线形状为示意。
"""
import os, sys, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ising1_figs as I1
from grounding2_figs import (T, box, line, circ, path, BG, ACC, ACCD, TINT, INK,
                             BODY, GRAY, LINE, RED, REDT, GRN, GRNT, PANEL)

I1.OUT = os.path.join(I1.PROJECT, "output", "2026-11-28-input-referred-noise", "figs")
os.makedirs(I1.OUT, exist_ok=True)
render, head = I1.render, I1.head
U = "μ"


def arrow(x1, y1, x2, y2, col=GRAY, sw=2.6):
    ang = math.atan2(y2 - y1, x2 - x1)
    a, L = 0.45, 14
    p1 = (x2 - L * math.cos(ang - a), y2 - L * math.sin(ang - a))
    p2 = (x2 - L * math.cos(ang + a), y2 - L * math.sin(ang + a))
    return (line(x1, y1, x2 - 6 * math.cos(ang), y2 - 6 * math.sin(ang), col, sw)
            + path(f"M{p1[0]:.1f},{p1[1]:.1f} L{x2},{y2} L{p2[0]:.1f},{p2[1]:.1f} Z", col, 1, fill=col))


def chip(x, y, w, h, txt, kind="acc", size=26):
    fill, st, col = {"acc": (TINT, ACC, ACCD), "red": (REDT, RED, RED), "grn": (GRNT, GRN, GRN),
                     "gray": ("#EEEEEE", GRAY, BODY), "ink": ("#FFFFFF", INK, INK)}[kind]
    return box(x, y, w, h, fill, st, rx=10, sw=2) + T(x + w / 2, y + h / 2 + size * 0.36, txt, size, col, weight="700")


def amp(x, y, h=110, col=ACC, label=""):
    """三角形放大器，左边中点 (x, y)。"""
    s = path(f"M{x},{y - h / 2} L{x},{y + h / 2} L{x + h * 0.95},{y} Z", col, 3, fill=TINT)
    if label:
        s += T(x + h * 0.36, y + 9, label, 24, ACCD, weight="700")
    return s


def noisy(x0, y0, w, amp_, seed=1, col=GRAY, sw=2):
    import random
    r = random.Random(seed)
    pts = [f"{x0 + i * 4:.1f},{y0 + r.gauss(0, amp_ / 2.5):.1f}" for i in range(int(w / 4) + 1)]
    return path("M" + " L".join(pts), col, sw)


# ================================================= 封面：记录噪声的组成
def cover():
    W, H = 960, 430
    s = [T(480, 46, "记录到的噪声（按平方相加）", 30, INK, weight="700")]
    x0, y = 120, 120
    segs = [("放大器", 230, ACC, TINT, "规格表上的数"), ("电极热噪声", 300, RED, REDT, ""),
            ("环境干扰", 180, GRAY, "#EEEEEE", "")]
    x = x0
    for name, w, c, f, sub in segs:
        s.append(box(x, y, w, 110, f, c, rx=8, sw=2.4))
        s.append(T(x + w / 2, y + 66, name, 28, c if c != GRAY else BODY, weight="700"))
        x += w + 8
    s.append(path(f"M{x0},{y + 140} L{x0},{y + 156} L{x0 + 230},{y + 156} L{x0 + 230},{y + 140}", ACC, 2.6))
    s.append(T(x0 + 115, y + 196, "规格表只给出这一项", 26, ACCD, weight="700"))
    s.append(T(x0 + 115, y + 232, f"例：Intan RHD2000 2.4 {U}Vrms", 22, GRAY))
    s.append(T(640, y + 196, "实际记录还要加上这些", 26, BODY))
    return W, H, "".join(s)


# ================================================= 目录
def toc():
    items = ["这个数是什么", "它怎么测，为什么随频段变", "放到实际记录中够不够", "我们能做什么"]
    W, H = 960, 120 + 78 * len(items)
    s = [T(480, 62, "本期目录", 40, INK, weight="700"), line(100, 92, 860, 92, LINE, 1.8)]
    y = 156
    nums = "①②③④"
    for i, t in enumerate(items):
        s += [circ(150, y - 10, 26, TINT, ACC, 2.2), T(150, y, nums[i], 28, ACCD, weight="700"),
              T(200, y, t, 32, INK, anchor="start")]
        y += 78
    return W, H, "".join(s)


# ================================================= 开篇：规格表一行
def f1():
    W, H = 960, 300
    s = [head(W, "Intan RHD2000 规格表中的一行（示意）", y=44)]
    y = 100
    cols = [(40, 330, "参数"), (370, 200, "典型值"), (570, 350, "备注")]
    for x, w, t in cols:
        s.append(box(x, y, w, 50, PANEL, LINE, rx=0, sw=1.6))
        s.append(T(x + w / 2, y + 34, t, 22, GRAY, weight="700"))
    vals = ["Amplifier Input-Referred Noise", f"2.4 {U}Vrms", "Typical"]
    for (x, w, _), v in zip(cols, vals):
        s.append(box(x, y + 50, w, 64, "#FFFFFF", LINE, rx=0, sw=1.6))
        s.append(T(x + w / 2, y + 92, v, 23 if x == 40 else 28, INK if x != 370 else ACCD, weight="700"))
    s.append(T(205, 260, "① 输入参考", 24, ACCD, weight="700"))
    s.append(T(470, 260, f"② {U}Vrms", 24, ACCD, weight="700"))
    s.append(T(745, 260, "③ 典型值", 24, ACCD, weight="700"))
    return W, H, "".join(s)


# ================================================= ①：折算到输入端
def f2():
    W, H = 960, 400
    s = [head(W, "输出噪声 ÷ 增益 = 输入参考噪声", y=44)]
    # 上：真实放大器
    y1 = 140
    s.append(T(70, y1 + 9, "真实放大器", 24, INK, anchor="start", weight="700"))
    s.append(line(210, y1, 330, y1, INK, 3))
    s.append(amp(330, y1, 100, ACC, "×192"))
    s.append(line(425, y1, 520, y1, INK, 3))
    s.append(noisy(530, y1, 240, 70, 3))
    s.append(T(880, y1 + 9, f"≈ 461 {U}V", 24, RED, weight="700"))
    # 下：理想放大器 + 输入噪声源
    y2 = 300
    s.append(T(70, y2 + 9, "等效模型", 24, INK, anchor="start", weight="700"))
    s.append(circ(250, y2, 30, REDT, RED, 2.6))
    s.append(T(250, y2 + 8, "~", 30, RED, weight="700"))
    s.append(T(250, y2 + 64, f"2.4 {U}V", 22, RED, weight="700"))
    s.append(line(280, y2, 330, y2, INK, 3))
    s.append(amp(330, y2, 100, ACC, "×192"))
    s.append(T(377, y2 - 64, "无噪声", 20, GRAY))
    s.append(line(425, y2, 520, y2, INK, 3))
    s.append(noisy(530, y2, 240, 70, 3))
    s.append(T(880, y2 + 9, f"≈ 461 {U}V", 24, RED, weight="700"))
    s.append(T(480, 392, "两者输出相同；461 为自算（2.4 × 192）", 20, GRAY))
    return W, H, "".join(s)


# ================================================= ①′：三级链路
def f3():
    W, H = 960, 330
    s = [head(W, "后级噪声折算回输入端时，要除以前级增益", y=44)]
    y = 160
    s.append(chip(40, y - 45, 220, 90, "放大 ×192", "acc", 28))
    s.append(arrow(260, y, 340, y, INK))
    s.append(chip(340, y - 45, 200, 90, "滤波", "gray", 28))
    s.append(arrow(540, y, 620, y, INK))
    s.append(chip(620, y - 45, 300, 90, "16 位 ADC", "gray", 28))
    s.append(T(150, y + 90, f"2.4 {U}Vrms", 30, ACCD, weight="700"))
    s.append(T(150, y + 126, "不被缩小", 22, ACCD))
    s.append(T(770, y + 90, f"约 0.056 {U}Vrms", 30, GRAY, weight="700"))
    s.append(T(770, y + 126, "折算到输入端（自算）", 22, GRAY))
    return W, H, "".join(s)


# ================================================= ②：输入为 0 测噪声
def f4():
    W, H = 960, 330
    s = [head(W, "输入接地 → 记录输出 → 除以增益 → 算 rms", y=44)]
    y = 170
    # 接地符号
    s.append(line(90, y, 160, y, INK, 3))
    s.append(line(90, y, 90, y + 40, INK, 3))
    for i, w in enumerate([44, 28, 12]):
        s.append(line(90 - w / 2, y + 40 + i * 10, 90 + w / 2, y + 40 + i * 10, INK, 3))
    s.append(T(90, y - 22, "输入 = 0", 22, INK, weight="700"))
    s.append(amp(160, y, 100, ACC, "×G"))
    s.append(line(255, y, 300, y, INK, 3))
    s.append(noisy(310, y, 220, 70, 7))
    s.append(T(420, y + 70, "只剩放大器噪声", 22, GRAY))
    s.append(arrow(550, y, 620, y, INK))
    s.append(chip(620, y - 40, 130, 80, "÷ G", "ink", 28))
    s.append(arrow(750, y, 800, y, INK))
    s.append(chip(800, y - 40, 130, 80, "rms", "acc", 28))
    s.append(T(480, 300, f"Harrison & Charles 2003：得到 2.2 {U}Vrms（0.5 Hz–50 kHz）", 21, GRAY))
    return W, H, "".join(s)


# ---- 频谱坐标轴（对数横轴）
def logx(f, fmin, fmax, x0, x1):
    return x0 + (math.log10(f) - math.log10(fmin)) / (math.log10(fmax) - math.log10(fmin)) * (x1 - x0)


# ================================================= ②′-1：面积 = 噪声功率
def f5():
    W, H = 960, 330
    s = [head(W, "噪声功率 = 谱密度曲线下的面积", y=44)]
    x0, x1, yb = 90, 900, 270
    s.append(line(x0, yb, x1, yb, INK, 2.6))
    s.append(line(x0, yb, x0, 80, INK, 2.6))
    s.append(T(x0 - 14, 96, "S(f)", 22, INK, anchor="end", weight="700"))
    s.append(T(x1, yb + 36, "f", 22, INK, weight="700"))
    ys = 150
    s.append(line(x0, ys, x1 - 20, ys, ACC, 3))
    fa, fb = 330, 690
    s.append(box(fa, ys, fb - fa, yb - ys, TINT, ACC, rx=0, sw=0))
    s.append(line(x0, ys, x1 - 20, ys, ACC, 3))
    s.append(line(fa, ys, fa, yb, ACC, 2, dash="6 5"))
    s.append(line(fb, ys, fb, yb, ACC, 2, dash="6 5"))
    s.append(T(fa, yb + 34, "f1", 22, INK, weight="700"))
    s.append(T(fb, yb + 34, "f2", 22, INK, weight="700"))
    s.append(T((fa + fb) / 2, 220, "Vrms² = S × (f2 − f1)", 26, ACCD, weight="700"))
    s.append(T((fa + fb) / 2, 132, "S 处处相同时", 20, GRAY))
    return W, H, "".join(s)


# ================================================= ②′-2：两段谱
def f6():
    W, H = 960, 360
    s = [head(W, "放大器噪声谱：fc 以下随频率降低而升高", y=44)]
    x0, x1, yb, yt = 110, 900, 290, 80
    fmin, fmax = 0.1, 100000
    s.append(line(x0, yb, x1, yb, INK, 2.6)); s.append(line(x0, yb, x0, yt, INK, 2.6))
    for f, lab in [(0.1, "0.1"), (1, "1"), (10, "10"), (100, "100"), (1000, "1k"), (10000, "10k"), (100000, "100k Hz")]:
        X = logx(f, fmin, fmax, x0, x1)
        s.append(line(X, yb, X, yb + 8, INK, 2)); s.append(T(X, yb + 32, lab, 19, GRAY))
    s.append(T(x0 - 12, yt + 14, "S(f)", 20, INK, anchor="end", weight="700"))
    s.append(T(x0 - 12, yt + 38, "对数", 17, GRAY, anchor="end"))
    # S = e²(1+fc/f), 对数纵轴
    fc = 100
    def Y(f):
        v = math.log10(1 + fc / f)       # 0 .. 3
        return yb - 50 - v / 3.2 * (yb - yt - 60)
    pts = []
    for i in range(0, 241):
        f = 10 ** (math.log10(fmin) + i / 240 * (math.log10(fmax) - math.log10(fmin)))
        pts.append(f"{logx(f, fmin, fmax, x0, x1):.1f},{Y(f):.1f}")
    s.append(path("M" + " L".join(pts), ACC, 3.4))
    Xc = logx(fc, fmin, fmax, x0, x1)
    s.append(line(Xc, yt + 10, Xc, yb, RED, 2.2, dash="7 5"))
    s.append(T(Xc + 10, yt + 30, "fc = 100 Hz", 22, RED, anchor="start", weight="700"))
    s.append(T(logx(3, fmin, fmax, x0, x1), Y(3) - 30, "1/f 噪声", 24, ACCD, weight="700"))
    s.append(T(logx(8000, fmin, fmax, x0, x1), Y(8000) - 22, "白噪声 21 nV/√Hz", 22, ACCD, weight="700"))
    s.append(T(480, 352, "Harrison & Charles 2003 实测值；曲线形状为示意", 19, GRAY))
    return W, H, "".join(s)


# ================================================= ②′-3：每个十倍频程贡献相同
def f7():
    W, H = 960, 340
    s = [head(W, "1/f 噪声：每个十倍频程贡献的功率相同", y=44)]
    x0, x1, yb = 110, 880, 250
    fmin, fmax = 0.1, 1000
    s.append(line(x0, yb, x1, yb, INK, 2.6))
    for f, lab in [(0.1, "0.1"), (1, "1"), (10, "10"), (100, "100"), (1000, "1000 Hz")]:
        X = logx(f, fmin, fmax, x0, x1)
        s.append(line(X, yb, X, yb + 8, INK, 2)); s.append(T(X, yb + 32, lab, 20, GRAY))
    for i, (a, b) in enumerate([(0.1, 1), (1, 10), (10, 100), (100, 1000)]):
        xa, xb = logx(a, fmin, fmax, x0, x1), logx(b, fmin, fmax, x0, x1)
        s.append(box(xa + 6, 130, xb - xa - 12, yb - 130, TINT, ACC, rx=4, sw=2))
        s.append(T((xa + xb) / 2, 196, "K·ln10", 22, ACCD, weight="700"))
    s.append(T(480, 106, "横轴为对数刻度，四段面积相等", 21, GRAY))
    s.append(T(480, 322, "Vrms² = K × ln(f2 / f1)", 24, INK, weight="700"))
    return W, H, "".join(s)


# ---- 柱状对比
def bars(title, items, vmax, unit_note):
    W, H = 960, 150 + 62 * len(items)
    s = [head(W, title, y=44)]
    x0 = 300
    y = 100
    for name, v, kind, lab in items:
        c, f = {"acc": (ACC, TINT), "red": (RED, REDT), "grn": (GRN, GRNT), "gray": (GRAY, "#EEEEEE")}[kind]
        w = v / vmax * 420
        s.append(T(x0 - 16, y + 34, name, 24, INK, anchor="end", weight="700"))
        s.append(box(x0, y + 8, w, 40, f, c, rx=4, sw=2))
        s.append(T(x0 + w + 12, y + 37, lab, 24, c, anchor="start", weight="700"))
        y += 62
    s.append(T(480, H - 16, unit_note, 19, GRAY))
    return W, H, "".join(s)


def f8():
    return bars("动作电位频段（0.3–10 kHz）", [
        ("放大器", 5.9, "acc", f"5.9 {U}Vrms"),
        ("1 MΩ 电极热噪声", 12.9, "red", f"12.9 {U}V"),
        ("两者合计", 14.2, "gray", f"14.2 {U}V"),
        ("动作电位幅度", 60, "grn", f"≥ 60 {U}V（大鼠）"),
    ], 80, "放大器：Neuropixels 1.0 规格书；热噪声与合计为自算（37 °C）")


def f9():
    return bars("LFP 频段（0.5–500 Hz）", [
        ("放大器", 9.2, "acc", f"9.2 {U}Vrms"),
        ("1 MΩ 电极热噪声", 2.9, "red", f"2.9 {U}V"),
    ], 16, "放大器：Neuropixels 1.0 规格书；热噪声为自算，假设阻抗在各频率均为 1 MΩ")


if __name__ == "__main__":
    for name, fn in [("cover", cover), ("toc", toc), ("f1", f1), ("f2", f2), ("f3", f3), ("f4", f4),
                     ("f5", f5), ("f6", f6), ("f7", f7), ("f8", f8), ("f9", f9)]:
        if len(sys.argv) > 1 and name not in sys.argv[1:]:
            continue
        W, H, inner = fn()
        render(name, W, H, inner)
        print("ok", name)
