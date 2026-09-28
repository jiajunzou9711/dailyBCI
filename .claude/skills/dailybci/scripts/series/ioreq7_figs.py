# -*- coding: utf-8 -*-
"""2026-09-28 · 采样率和滤波怎么设（上/下）（电生理 IO 系列 ep07）—— 自制示意图"""
import os, sys, math
import numpy as np
import scipy.signal as ss
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from grounding2_figs import (T, box, line, circ, path, ACC, ACCD, TINT, INK, BODY,
                             GRAY, LINE, RED, REDT, GRN, GRNT, CARD_L, PANEL)
import ioreq1_figs
from ioreq2_figs import table

SKILL_DIR = os.path.dirname(os.path.dirname(HERE))
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-09-13-electrophysiology-io",
                   "ep07-2026-09-28-sampling-filter", "figs")
os.makedirs(OUT, exist_ok=True)
ioreq1_figs.OUT = OUT

MK = {INK: "ahk", ACC: "ah", RED: "ahr", GRAY: "ahg", GRN: "ahn"}
ORG = "#C77B1E"


def head(W, s, y=46, size=30):
    return T(W / 2, y, s, size, INK, weight="700")


def arrow(x1, y1, x2, y2, stroke=INK, sw=2.6):
    return line(x1, y1, x2, y2, stroke, sw, marker=MK.get(stroke, "ahk"))


def curve(xs, ys, x0, y0, w, h, xmin, xmax, ymin, ymax, stroke=INK, sw=2.4, dash=None):
    """把数据 (xs, ys) 画进左上角 (x0,y0)、宽 w 高 h 的框里；超出纵轴范围的点截断。"""
    pts = []
    for x, y in zip(xs, ys):
        y = min(max(y, ymin), ymax)
        px = x0 + (x - xmin) / (xmax - xmin) * w
        py = y0 + h - (y - ymin) / (ymax - ymin) * h
        pts.append("%.1f,%.1f" % (px, py))
    return path("M" + " L".join(pts), stroke, sw, dash=dash)


def spike_wave(t):
    return -1.0 * np.exp(-(t / 0.00015) ** 2 / 2) + 0.3 * np.exp(-((t - 0.0005) / 0.0003) ** 2 / 2)


FS = 30000


# ================================================================ 上篇
def cover1():
    W, H = 960, 420
    s = []
    s.append(box(60, 50, 400, 250, REDT, RED, rx=18, sw=2.4))
    s.append(T(260, 98, "记录前定 · 不可逆", 26, RED, weight="700"))
    for i, t in enumerate(("采样率", "采集端高通", "抗混叠低通")):
        s.append(T(260, 152 + i * 44, t, 24, INK, weight="700"))
    s.append(box(500, 50, 400, 250, GRNT, GRN, rx=18, sw=2))
    s.append(T(700, 98, "记录后调 · 可撤销", 26, GRN, weight="700"))
    for i, t in enumerate(("软件滤波的截止", "陡度", "是否移位")):
        s.append(T(700, 152 + i * 44, t, 24, BODY, weight="700"))
    s.append(T(480, 356, "上篇：左边这一栏，记录结束后就补不回来", 26, ACCD, weight="700"))
    s.append(T(480, 396, "下篇：右边这一栏", 20, GRAY, weight="700"))
    return W, H, "".join(s)


def toc1():
    W, H = 960, 520
    s = [T(480, 62, "上篇路线", 40, INK, weight="700"), line(120, 92, 840, 92, LINE, 1.8)]
    items = [("①", "要留下什么", "以动作电位为例：时刻与形状"),
             ("②", "三条要求", "频段不被削 · 不混进假频率 · 不变形不移位"),
             ("③", "截止频率", "由要保留的频段决定"),
             ("④", "设在哪一端", "采集端宜宽；硬件滤波怎样实现"),
             ("⑤", "采样率", "要比频段上限高出多少")]
    y = 150
    for n, t, d in items:
        s.append(circ(150, y - 9, 24, TINT, ACC, 2.4))
        s.append(T(150, y + 1, n, 24, ACCD, weight="700"))
        s.append(T(200, y - 2, t, 30, INK, anchor="start", weight="700"))
        s.append(T(200, y + 32, d, 22, BODY, anchor="start"))
        y += 72
    s.append(line(120, 486, 840, 486, LINE, 1.6))
    s.append(T(480, 512, "下篇：软件滤波的陡度与相位，以及怎样检查", 21, GRAY, weight="700"))
    return W, H, "".join(s)


def fig_ap():
    W, H = 960, 430
    s = [head(W, "要留下的有两样：每个动作电位出现的时刻，和它的形状")]
    rng = np.random.default_rng(3)
    t = np.arange(0, 0.05, 1 / FS)
    x = rng.normal(0, 0.08, t.size)
    times = [0.008, 0.019, 0.027, 0.041]
    for tt in times:
        x += spike_wave(t - tt)
    s.append(box(40, 80, 600, 250, "#FFFFFF", CARD_L, rx=12, sw=1.6))
    s.append(curve(t, x, 60, 100, 560, 170, 0, 0.05, -1.3, 0.6, INK, 1.4))
    for tt in times:
        px = 60 + tt / 0.05 * 560
        s.append(line(px, 285, px, 312, RED, 3))
    s.append(T(340, 356, "红色竖线：出现的时刻", 21, RED, weight="700"))
    s.append(T(60, 322, "50 ms", 18, GRAY, anchor="start"))
    # 形状
    s.append(box(670, 80, 250, 250, "#FFFFFF", CARD_L, rx=12, sw=1.6))
    tz = np.linspace(-0.001, 0.002, 300)
    s.append(curve(tz, spike_wave(tz), 690, 110, 210, 170, -0.001, 0.002, -1.1, 0.45, ACC, 3))
    s.append(T(795, 318, "单个波形放大（3 ms）", 18, GRAY, weight="700"))
    s.append(T(795, 356, "形状：用于分选", 21, ACCD, weight="700"))
    s.append(T(480, 410, "合成示意波形，非真实记录", 18, GRAY, weight="700"))
    return W, H, "".join(s)


def fig_bands():
    W, H = 960, 400
    s = [head(W, "截止频率要把目标信号所在的频段完整包在里面")]
    x0, x1, y = 70, 900, 250
    lg = lambda f: x0 + (math.log10(f) - (-1)) / (math.log10(30000) - (-1)) * (x1 - x0)
    s.append(line(x0, y, x1, y, INK, 2))
    for f, lab in ((0.1, "0.1"), (1, "1"), (10, "10"), (100, "100"), (1000, "1 k"), (10000, "10 k")):
        s.append(line(lg(f), y, lg(f), y + 10, INK, 2))
        s.append(T(lg(f), y + 34, lab, 20, BODY))
    s.append(T(x1, y + 34, "Hz", 20, BODY, anchor="end"))
    s.append(box(lg(0.5), 150, lg(250) - lg(0.5), 60, TINT, ACC, rx=8, sw=1.6))
    s.append(T((lg(0.5) + lg(250)) / 2, 188, "局部场电位等慢变化", 21, ACCD, weight="700"))
    s.append(box(lg(300), 150, lg(3000) - lg(300), 60, GRNT, GRN, rx=8, sw=2.4))
    s.append(T((lg(300) + lg(3000)) / 2, 188, "保留段", 20, GRN, weight="700"))
    s.append(T((lg(300) + lg(3000)) / 2, 120, "300–3000 Hz：动作电位分选的一种常见设置", 19, GRN, weight="700"))
    s.append(box(lg(3500), 150, lg(28000) - lg(3500), 60, PANEL, CARD_L, rx=8, sw=1.6))
    s.append(T((lg(3500) + lg(28000)) / 2, 188, "主要是噪声", 19, GRAY, weight="700"))
    s.append(line(lg(300), 140, lg(300), y, RED, 2, dash="6 5"))
    s.append(line(lg(3000), 140, lg(3000), y, RED, 2, dash="6 5"))
    s.append(T(lg(300) - 8, 232, "高通截止", 18, RED, anchor="end", weight="700"))
    s.append(T(lg(3000) + 8, 232, "低通截止", 18, RED, anchor="start", weight="700"))
    s.append(T(480, 336, "离目标太近：削到目标自身　　离目标太远：留下不要的成分", 21, BODY, weight="700"))
    s.append(T(480, 376, "各成分所在区段为示意；300–3000 Hz 出自 Quian Quiroga 2007", 17, GRAY, weight="700"))
    return W, H, "".join(s)


def resistor(x, y, horiz=True, L=70):
    if horiz:
        return box(x, y - 12, L, 24, "#FFFFFF", INK, rx=3, sw=2.4)
    return box(x - 12, y, 24, L, "#FFFFFF", INK, rx=3, sw=2.4)


def cap_h(x, y):  # 串在水平线上的电容：两条竖板
    return line(x, y - 22, x, y + 22, INK, 3.4) + line(x + 14, y - 22, x + 14, y + 22, INK, 3.4)


def cap_v(x, y):  # 竖向电容：两条横板
    return line(x - 22, y, x + 22, y, INK, 3.4) + line(x - 22, y + 14, x + 22, y + 14, INK, 3.4)


def ground(x, y):
    return (line(x, y, x, y + 16, INK, 2.4) + line(x - 20, y + 16, x + 20, y + 16, INK, 2.6)
            + line(x - 12, y + 24, x + 12, y + 24, INK, 2.6) + line(x - 5, y + 32, x + 5, y + 32, INK, 2.6))


def fig_rc():
    W, H = 960, 420
    s = [head(W, "硬件滤波：电阻加电容，频率越高，电容越容易让电流通过")]
    # 低通
    s.append(T(240, 100, "低通", 26, ACCD, weight="700"))
    y = 170
    s.append(line(60, y, 130, y, INK, 2.4)); s.append(resistor(130, y))
    s.append(line(200, y, 420, y, INK, 2.4)); s.append(circ(300, y, 5, INK, INK, 1))
    s.append(line(300, y, 300, 214, INK, 2.4)); s.append(cap_v(300, 214))
    s.append(line(300, 228, 300, 260, INK, 2.4)); s.append(ground(300, 260))
    s.append(T(60, y - 20, "输入", 20, GRAY, anchor="start", weight="700"))
    s.append(T(420, y - 20, "输出", 20, GRAY, anchor="end", weight="700"))
    s.append(T(165, y - 26, "R", 20, INK, weight="700")); s.append(T(338, 224, "C", 20, INK, anchor="start", weight="700"))
    s.append(T(240, 340, "快变化从电容流到地，留下慢成分", 20, BODY, weight="700"))
    # 高通
    s.append(T(720, 100, "高通", 26, ACCD, weight="700"))
    s.append(line(540, y, 640, y, INK, 2.4)); s.append(cap_h(640, y))
    s.append(line(654, y, 900, y, INK, 2.4)); s.append(circ(780, y, 5, INK, INK, 1))
    s.append(line(780, y, 780, 200, INK, 2.4)); s.append(resistor(780, 200, horiz=False, L=60))
    s.append(line(780, 260, 780, 270, INK, 2.4)); s.append(ground(780, 270))
    s.append(T(540, y - 20, "输入", 20, GRAY, anchor="start", weight="700"))
    s.append(T(900, y - 20, "输出", 20, GRAY, anchor="end", weight="700"))
    s.append(T(647, y - 34, "C", 20, INK, weight="700")); s.append(T(806, 236, "R", 20, INK, anchor="start", weight="700"))
    s.append(T(720, 340, "直流过不去，变化的成分能通过", 20, BODY, weight="700"))
    s.append(T(480, 392, "截止频率 = 1 ÷ (2π × R × C)；电路只能响应已到来的电压，必然是因果的", 20, ACCD, weight="700"))
    return W, H, "".join(s)


def fig_nyquist():
    W, H = 960, 470
    s = [head(W, "采样率要高到：到奈奎斯特频率时，过渡带里的成分已衰减得足够小")]
    x0, y0, w, h = 90, 80, 800, 200
    f = np.linspace(0, 20000, 800)
    g = 1 / np.sqrt(1 + (f / 10000) ** 12)  # 示意低通
    s.append(line(x0, y0 + h, x0 + w, y0 + h, INK, 2))
    s.append(line(x0, y0, x0, y0 + h, INK, 2))
    fx = lambda v: x0 + v / 20000 * w
    s.append(box(fx(10000), y0, fx(15000) - fx(10000), h, PANEL, "none", rx=0, sw=0))
    s.append(curve(f, g, x0, y0, w, h, 0, 20000, 0, 1.05, ACC, 3))
    s.append(line(fx(15000), y0 - 10, fx(15000), y0 + h, RED, 2.4, dash="6 5"))
    s.append(T(fx(15000) + 8, y0 + 10, "奈奎斯特频率", 19, RED, anchor="start", weight="700"))
    s.append(T(fx(15000) + 8, y0 + 34, "= 采样率 30 kHz ÷ 2", 17, RED, anchor="start", weight="700"))
    s.append(T(fx(12500), y0 + h - 16, "过渡带", 19, GRAY, weight="700"))
    s.append(T(fx(4500), y0 + 40, "抗混叠低通（截止 10 kHz）", 19, ACCD, weight="700"))
    for v in (0, 5000, 10000, 15000, 20000):
        s.append(T(fx(v), y0 + h + 26, "%d k" % (v // 1000), 18, BODY))
    s.append(T(x0 - 10, y0 + 8, "保留", 17, GRAY, anchor="end"))
    rows = [[["动作电位频段"], ["低通 10 kHz"], ["30 kHz"], ["15 kHz"]],
            [["局部场电位频段"], ["0.5–1000 Hz"], ["2.5 kHz"], ["1.25 kHz"]]]
    t, bottom = table(W, None, [230, 190, 150, 170], ["Neuropixels 两路", "保留频段", "采样率", "奈奎斯特"],
                      rows, top=328, hh=44, lh=30, pad=14, first_color=INK, size=20)
    s += t
    return W, bottom + 30, "".join(s) + T(480, bottom + 22, "曲线形状为示意；两路参数出自 Jun et al. 2017", 16, GRAY, weight="700")


# ================================================================ 下篇
def cover2():
    W, H = 960, 420
    s = []
    f = np.linspace(200, 400, 400)
    fir = ss.firwin(1501, 300, fs=FS, pass_zero=False, window="hamming")
    _, Hh = ss.freqz(fir, worN=f, fs=FS)
    s.append(box(70, 40, 820, 250, "#FFFFFF", CARD_L, rx=16, sw=1.8))
    s.append(curve(f, np.abs(Hh), 110, 70, 740, 180, 200, 400, 0, 1.05, ACC, 3.4))
    s.append(line(110 + 0.5 * 740, 60, 110 + 0.5 * 740, 250, RED, 2, dash="6 5"))
    s.append(T(110 + 0.5 * 740 + 10, 80, "截止 300 Hz", 20, RED, anchor="start", weight="700"))
    s.append(T(480, 278, "截止两侧，只能逐渐过渡", 19, GRAY, weight="700"))
    s.append(T(480, 346, "截止频率相同，结果为什么不同？", 28, ACCD, weight="700"))
    s.append(T(480, 390, "陡度决定去得多干净，相位决定波形会不会移位", 21, BODY, weight="700"))
    return W, H, "".join(s)


def toc2():
    W, H = 960, 520
    s = [T(480, 62, "下篇路线", 40, INK, weight="700"), line(120, 92, 840, 92, LINE, 1.8)]
    items = [("1", "软件滤波要做到什么", "去干净，同时不改变要留下的波形"),
             ("2", "截止附近能去多干净", "加权和 → 看的时间有限 → 过渡带；越陡越变形"),
             ("3", "波形会不会移位", "延迟从哪来；在线与离线怎样选"),
             ("4", "做完检查", "哪些能事后查，哪些只能事前查"),
             ("5", "换成事件相关电位", "同一套逻辑，参数相差几个数量级")]
    y = 150
    for n, t, d in items:
        s.append(circ(150, y - 9, 24, TINT, ACC, 2.4))
        s.append(T(150, y + 1, n, 22, ACCD, weight="700"))
        s.append(T(200, y - 2, t, 30, INK, anchor="start", weight="700"))
        s.append(T(200, y + 32, d, 22, BODY, anchor="start"))
        y += 72
    s.append(line(120, 486, 840, 486, LINE, 1.6))
    s.append(T(480, 512, "本期不解读文献，从基础原理梳理采样率与滤波的设置", 21, GRAY, weight="700"))
    return W, H, "".join(s)


def fig_movavg():
    W, H = 960, 420
    s = [head(W, "滑动平均：每个输出点取附近几个点的平均，快变化被抹平")]
    n = np.arange(60)
    rng = np.random.default_rng(7)
    slow = np.sin(2 * np.pi * n / 60) * 0.8
    x = slow + rng.normal(0, 0.35, n.size)
    y = np.convolve(x, np.ones(5) / 5, mode="same")
    for row, (sig, lab, col) in enumerate(((x, "输入：慢变化 + 快起伏", INK), (y, "输出：5 点平均", ACC))):
        y0 = 80 + row * 150
        s.append(T(60, y0 + 10, lab, 20, col, anchor="start", weight="700"))
        pts = []
        for i, v in enumerate(sig):
            px = 80 + i * 13.5
            py = y0 + 70 - v * 45
            pts.append((px, py))
            s.append(circ(px, py, 3.2, col, col, 1))
        s.append(path("M" + " L".join("%.1f,%.1f" % p for p in pts), col, 1.6))
    s.append(box(80 + 20 * 13.5 - 6, 76, 5 * 13.5, 150, "none", RED, rx=4, sw=2, dash="5 4"))
    s.append(T(80 + 22 * 13.5, 250, "这 5 个点平均 → 下方对应的 1 个点", 18, RED, anchor="start", weight="700"))
    s.append(T(480, 400, "参与计算的点越多，滤波一次能看的时间越长", 21, BODY, weight="700"))
    return W, H, "".join(s)


def fig_window():
    W, H = 960, 440
    s = [head(W, "290 Hz 和 310 Hz：1 ms 内几乎重合，50 ms 后相差整整一个周期")]
    t1 = np.linspace(0, 0.001, 200)
    s.append(box(40, 80, 280, 300, "#FFFFFF", CARD_L, rx=12, sw=1.6))
    s.append(T(180, 112, "看 1 ms", 24, INK, weight="700"))
    s.append(curve(t1, np.cos(2 * np.pi * 290 * t1), 60, 150, 240, 160, 0, 0.001, -1.1, 1.1, ACC, 3))
    s.append(curve(t1, np.cos(2 * np.pi * 310 * t1), 60, 150, 240, 160, 0, 0.001, -1.1, 1.1, RED, 2.4, dash="6 4"))
    s.append(T(180, 350, "分不出谁是谁", 20, BODY, weight="700"))
    t2 = np.linspace(0, 0.05, 3000)
    s.append(box(350, 80, 570, 300, "#FFFFFF", CARD_L, rx=12, sw=1.6))
    s.append(T(635, 112, "看 50 ms", 24, INK, weight="700"))
    s.append(curve(t2, np.cos(2 * np.pi * 290 * t2), 370, 150, 530, 160, 0, 0.05, -1.1, 1.1, ACC, 1.6))
    s.append(curve(t2, np.cos(2 * np.pi * 310 * t2), 370, 150, 530, 160, 0, 0.05, -1.1, 1.1, RED, 1.4, dash="4 3"))
    s.append(T(635, 350, "起点同步，到 25 ms 时一个在波峰、一个在波谷", 19, BODY, weight="700"))
    s.append(T(150, 416, "蓝：290 Hz　红虚线：310 Hz", 19, GRAY, anchor="start", weight="700"))
    s.append(T(900, 416, "要看的时长 ≈ 1 ÷ 频率差", 20, ACCD, anchor="end", weight="700"))
    return W, H, "".join(s)


def fig_transition():
    W, H = 960, 440
    s = [head(W, "同一个 300 Hz 高通，看得越久，过渡带越窄")]
    x0, y0, w, h = 110, 80, 760, 260
    f = np.linspace(240, 360, 600)
    s.append(line(x0, y0 + h, x0 + w, y0 + h, INK, 2)); s.append(line(x0, y0, x0, y0 + h, INK, 2))
    for n, col, lab, dash in ((31, GRAY, "看 1 ms", "6 4"), (1501, ACC, "看 50 ms", None), (15001, RED, "看 500 ms", None)):
        hh = ss.firwin(n, 300, fs=FS, pass_zero=False, window="hamming")
        _, Hh = ss.freqz(hh, worN=f, fs=FS)
        s.append(curve(f, np.abs(Hh) * 100, x0, y0, w, h, 240, 360, 0, 105, col, 3, dash=dash))
    fx = lambda v: x0 + (v - 240) / 120 * w
    fy = lambda v: y0 + h - v / 105 * h
    s.append(circ(fx(300), fy(50), 6, INK, INK, 1))
    s.append(T(fx(300) + 12, fy(50) + 6, "300 Hz：留 50%", 19, INK, anchor="start", weight="700"))
    for v in (240, 270, 300, 330, 360):
        s.append(T(fx(v), y0 + h + 26, str(v), 18, BODY))
    for v in (0, 50, 100):
        s.append(T(x0 - 10, fy(v) + 6, "%d%%" % v, 17, BODY, anchor="end"))
    s.append(T(fx(245), fy(78), "看 1 ms：处处约 70%", 18, GRAY, anchor="start", weight="700"))
    s.append(T(fx(318), fy(30), "看 50 ms", 19, ACC, anchor="start", weight="700"))
    s.append(T(fx(303), fy(92), "看 500 ms", 19, RED, anchor="start", weight="700"))
    s.append(T(480, 426, "SciPy firwin 加窗法、Hamming 窗、采样率 30 kHz 自算；横轴 Hz，纵轴为留下的幅度比例", 16, GRAY, weight="700"))
    return W, H, "".join(s)


def fig_ringing():
    W, H = 960, 440
    s = [head(W, "边界越陡，同一个动作电位的影响摊得越开")]
    t = np.arange(-0.4, 0.4, 1 / FS)
    x = spike_wave(t)
    rows = ((151, "看 5 ms（边界平缓）", ACC, 2.0), (15001, "看 500 ms（边界陡峭）", RED, 11.0))
    for r, (n, lab, col, ext) in enumerate(rows):
        hh = ss.firwin(n, 300, fs=FS, pass_zero=False, window="hamming")
        y = np.convolve(x, hh, mode="same")
        y0 = 80 + r * 160
        s.append(T(60, y0 + 6, lab, 21, col, anchor="start", weight="700"))
        m = np.abs(t) < 0.015
        s.append(box(80 + (0.015 - ext / 1000) / 0.03 * 800, y0 + 20, ext / 1000 * 2 / 0.03 * 800, 110,
                     REDT if col == RED else TINT, "none", rx=4, sw=0))
        s.append(curve(t[m], y[m], 80, y0 + 20, 800, 110, -0.015, 0.015, -0.08, 0.08, col, 1.8))
        s.append(T(880, y0 + 6, "起伏超过主峰 1%%：约 ±%g ms" % ext, 18, col, anchor="end", weight="700"))
    for v in (-15, -10, -5, 0, 5, 10, 15):
        s.append(T(80 + (v + 15) / 30 * 800, 410, "%d" % v, 17, BODY))
    s.append(T(930, 410, "ms", 17, BODY, anchor="end"))
    s.append(T(480, 432, "纵轴放大约 12 倍，主峰被截断；合成示意波形，零延迟处理", 16, GRAY, weight="700"))
    return W, H, "".join(s)


def fig_align():
    W, H = 960, 450
    s = [head(W, "形状取决于各成分的波峰对不对得齐")]
    t = np.linspace(-0.002, 0.003, 500)
    cases = (("各频率延迟相同（都晚 0.5 ms）", 0.0005, 0.0005, "叠加：高 2"),
             ("快成分晚 0.1 ms、慢成分晚 0.5 ms", 0.0001, 0.0005, "叠加：只剩约 1.81"))
    for r, (lab, df, dsl, note) in enumerate(cases):
        y0 = 80 + r * 175
        s.append(T(60, y0 + 4, lab, 21, INK, anchor="start", weight="700"))
        slow = np.cos(2 * np.pi * (t - dsl) / 0.004)
        fast = np.cos(2 * np.pi * (t - df) / 0.001)
        s.append(curve(t, slow, 60, y0 + 20, 520, 120, -0.002, 0.003, -2.2, 2.2, GRAY, 1.8, dash="5 4"))
        s.append(curve(t, fast, 60, y0 + 20, 520, 120, -0.002, 0.003, -2.2, 2.2, ACC, 1.8, dash="3 3"))
        s.append(curve(t, slow + fast, 60, y0 + 20, 520, 120, -0.002, 0.003, -2.2, 2.2, RED, 3))
        s.append(T(760, y0 + 90, note, 22, RED, weight="700"))
    s.append(T(480, 432, "灰虚线：慢成分（周期 4 ms）　蓝虚线：快成分（周期 1 ms）　红：两者之和（示意）", 17, GRAY, weight="700"))
    return W, H, "".join(s)


def fig_rcdelay():
    W, H = 960, 420
    s = [head(W, "越近权重越大：快成分的旧数据相互抵消，延迟更短")]
    s.append(T(250, 96, "RC 低通对过去数据的权重", 21, INK, weight="700"))
    for i in range(16):
        wgt = math.exp(-i / 4.0)
        x = 420 - i * 22
        s.append(box(x, 290 - wgt * 170, 16, wgt * 170, TINT, ACC, rx=2, sw=1.4))
    s.append(arrow(90, 318, 440, 318, GRAY))
    s.append(T(90, 344, "更早", 18, GRAY, anchor="start", weight="700"))
    s.append(T(440, 344, "当下", 18, GRAY, anchor="end", weight="700"))
    rows = [[["50 Hz"], ["约 0.50 ms"]], [["1000 Hz"], ["约 0.20 ms"]], [["3000 Hz"], ["约 0.08 ms"]]]
    t, bottom = table(W, None, [180, 190], ["频率", "被推后"], rows, x0=540, top=100,
                      hh=48, lh=30, pad=24, first_color=INK, size=21)
    s += t
    s.append(T(725, bottom + 34, "RC = 0.5 ms，一阶 RC 低通相位公式自算", 16, GRAY, weight="700"))
    s.append(T(480, 400, "权重对称时，两侧抵消也对称：各频率推后相同，形状不变（线性相位）", 20, ACCD, weight="700"))
    return W, H, "".join(s)


def fig_lpdelay():
    W = 960
    rows = [[["线性相位 FIR，5 ms（151 点）"], ["2.5 ms"], ["各频率相同，形状不变"]],
            [["线性相位 FIR，50 ms（1501 点）"], ["25 ms"], ["各频率相同，形状不变"]],
            [["2 阶 Butterworth 带通（IIR）"], ["约 0.16 ms（1 kHz）", "约 0.45 ms（500 Hz）"], ["**各频率不同，形状会变**"]]]
    s, bottom = table(W, "线性相位保住形状，但延迟 = 权重长度的一半", [390, 230, 280],
                      ["滤波（采样率 30 kHz）", "延迟", "形状"], rows, lh=32, pad=24, first_color=INK, size=21)
    s.append(T(480, bottom + 34, "延迟自算；线性相位延迟 (N − 1) ÷ 2 个点出自 Widmann et al. 2015", 16, GRAY, weight="700"))
    return W, bottom + 50, "".join(s)


def fig_threewave():
    W, H = 960, 420
    s = [head(W, "同一个滤波器：单向滤一次造出反弹，正反两次保住峰的时刻")]
    t = np.arange(-0.02, 0.02, 1 / FS)
    x = spike_wave(t)
    b, a = ss.butter(2, [300, 3000], btype="band", fs=FS)
    yc = ss.lfilter(b, a, x)
    yz = ss.filtfilt(b, a, x)
    m = (t > -0.001) & (t < 0.003)
    s.append(box(60, 70, 620, 300, "#FFFFFF", CARD_L, rx=12, sw=1.6))
    for sig, col, sw, dash in ((x, GRAY, 3, "6 4"), (yc, RED, 3, None), (yz, ACC, 3, None)):
        s.append(curve(t[m], sig[m], 80, 90, 580, 260, -0.001, 0.003, -1.0, 0.75, col, sw, dash=dash))
    s.append(T(80, 364, "−1", 16, BODY)); s.append(T(660, 364, "3 ms", 16, BODY, anchor="end"))
    for i, (lab, col) in enumerate((("原始", GRAY), ("单向（因果）", RED), ("正反两次（零相位）", ACC))):
        s.append(line(700, 120 + i * 50, 736, 120 + i * 50, col, 3.4, dash="6 4" if i == 0 else None))
        s.append(T(746, 127 + i * 50, lab, 20, col, anchor="start", weight="700"))
    s.append(T(700, 300, "单向：负峰缩小约四成，", 18, RED, anchor="start", weight="700"))
    s.append(T(700, 326, "峰后正向翻倍", 18, RED, anchor="start", weight="700"))
    s.append(T(480, 404, "2 阶 Butterworth 带通 300–3000 Hz，合成示意波形，自算", 16, GRAY, weight="700"))
    return W, H, "".join(s)


def fig_erp():
    W = 960
    rows = [[["要留下"], ["每个的时刻与形状"], ["刺激后几百毫秒的慢波形"]],
            [["高通截止"], ["约 300 Hz"], ["0.01–0.1 Hz"]],
            [["低通截止"], ["约 3000 Hz"], ["30 Hz"]],
            [["采样率"], ["30 kHz"], ["512 Hz"]],
            [["不能移位"], ["零相位或线性相位"], ["同左（要读潜伏期）"]]]
    s, bottom = table(W, "同一套要求，参数相差几个数量级", [200, 330, 370],
                      ["", "动作电位", "事件相关电位（P300 类）"], rows, lh=32, pad=22, first_color=INK, size=21)
    s.append(T(480, bottom + 34, "动作电位列出自 Quian Quiroga 2007、Jun et al. 2017；ERP 列出自 Tanner et al. 2015", 16, GRAY, weight="700"))
    return W, bottom + 50, "".join(s)


def fig_summary():
    W = 960
    rows = [[["目标频段不被削"], ["截止频率；陡度"], ["采集端宜宽，软件里收窄"]],
            [["不混进假频率"], ["采样率；抗混叠低通"], ["**只能在采集端，记录前定**"]],
            [["不变形、不移位"], ["滤波方式（相位）"], ["离线零相位 / 线性相位；", "在线只能因果，知道它会变形"]]]
    s, bottom = table(W, "三条要求，各落到哪个参数、在哪一端定", [240, 270, 390],
                      ["要求", "关键参数", "在哪一端、怎么设"], rows, lh=32, pad=24, first_color=INK, size=21)
    return W, bottom + 24, "".join(s)


FIGS = {
    "cover1": cover1, "toc1": toc1, "fig-ap": fig_ap, "fig-bands": fig_bands, "fig-rc": fig_rc,
    "fig-nyquist": fig_nyquist,
    "cover2": cover2, "toc2": toc2, "fig-movavg": fig_movavg, "fig-window": fig_window,
    "fig-transition": fig_transition, "fig-ringing": fig_ringing, "fig-align": fig_align,
    "fig-rcdelay": fig_rcdelay, "fig-lpdelay": fig_lpdelay, "fig-threewave": fig_threewave,
    "fig-erp": fig_erp, "fig-summary": fig_summary,
}

if __name__ == "__main__":
    names = sys.argv[1:] or list(FIGS)
    for n in names:
        w, h, inner = FIGS[n]()
        print(ioreq1_figs.render(n, w, int(h), inner))
