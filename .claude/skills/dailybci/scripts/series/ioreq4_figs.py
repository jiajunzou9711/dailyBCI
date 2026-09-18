# -*- coding: utf-8 -*-
"""2026-09-18 · 电极上的电压，怎样成为文件里的数据（电生理 IO 系列 ep04）—— 自制示意图"""
import os, sys, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from grounding2_figs import (T, box, line, circ, path, wave, ACC, ACCD, TINT, INK, BODY,
                             GRAY, LINE, RED, REDT, GRN, GRNT, CARD_L, PANEL)
import ioreq1_figs
from ioreq2_figs import table

SKILL_DIR = os.path.dirname(os.path.dirname(HERE))
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-09-13-electrophysiology-io",
                   "ep04-2026-09-18-analog-input", "figs")
os.makedirs(OUT, exist_ok=True)
ioreq1_figs.OUT = OUT


def head(W, s, y=46, size=30):
    return T(W / 2, y, s, size, INK, weight="700")


def blk(x, y, w, h, name, sub=None, fill=PANEL, stroke=CARD_L, col=INK):
    s = [box(x, y, w, h, fill, stroke, rx=14, sw=2),
         T(x + w / 2, y + (h / 2 + 10 if not sub else h / 2 - 4), name, 26, col, weight="700")]
    if sub:
        s.append(T(x + w / 2, y + h / 2 + 30, sub, 20, GRAY, weight="700"))
    return s


def arrow(x1, y1, x2, y2, stroke=INK, sw=2.6):
    return line(x1, y1, x2, y2, stroke, sw, marker="arrow")


def sine(x0, y0, w, amp, cycles, stroke=ACC, sw=2.6, phase=0.0, pts=240):
    d = []
    for i in range(pts + 1):
        x = x0 + w * i / pts
        y = y0 - amp * math.sin(2 * math.pi * cycles * i / pts + phase)
        d.append(("M" if i == 0 else "L") + "%.1f,%.1f" % (x, y))
    return path("".join(d), stroke, sw)


# ---------------------------------------------------------------- 封面
def cover_concept():
    W, H = 960, 420
    s = []
    s.append(T(140, 86, "电极上的电压", 26, ACCD, weight="700"))
    s.append(sine(55, 170, 190, 34, 2.2, ACC, 3))
    s.append(T(140, 250, "连续变化", 22, GRAY, weight="700"))
    xs = [280, 440, 600]
    for x, (n, sub) in zip(xs, [("放大 · 滤波", "调到可测范围"),
                                ("采样", "时间上取点"),
                                ("量化", "幅值上归档")]):
        s += blk(x, 120, 140, 100, n, sub)
    for a, b in ((252, 276), (424, 436), (584, 596), (744, 782)):
        s.append(arrow(a, 170, b, 170))
    s.append(T(852, 86, "文件里的数据", 26, ACCD, weight="700"))
    for i, v in enumerate(["1204", "1231", "1198"]):
        s.append(T(852, 150 + i * 36, v, 26, INK, weight="700"))
    s.append(T(852, 250, "有限个整数", 22, GRAY, weight="700"))
    s.append(line(60, 320, 900, 320, LINE, 1.6))
    s.append(T(480, 366, "每一步改变了什么，什么信息在这一步丢掉", 26, BODY, weight="700"))
    return W, H, "".join(s)


# ---------------------------------------------------------------- 目录
def toc():
    W, H = 960, 560
    s = [T(480, 66, "本期路线", 40, INK, weight="700"), line(120, 96, 840, 96, LINE, 1.8)]
    items = [
        ("①", "测的是哪两个点之差", "单端测量与差分测量"),
        ("②", "调到可测量的范围", "增益、削顶、放大器的位置、滤波"),
        ("③", "采样与量化", "混叠、档宽、实际分辨力由谁决定"),
        ("④", "换算回物理量", "整数怎样变回微伏，三种典型失败"),
    ]
    y = 170
    for n, t, d in items:
        s.append(circ(150, y - 9, 26, TINT, ACC, 2.4))
        s.append(T(150, y + 1, n, 28, ACCD, weight="700"))
        s.append(T(204, y - 2, t, 32, INK, anchor="start", weight="700"))
        s.append(T(204, y + 36, d, 24, BODY, anchor="start"))
        y += 96
    s.append(line(120, 520, 840, 520, LINE, 1.6))
    s.append(T(480, 548, "本期不解读文献，从基础原理梳理模拟输入", 22, GRAY, weight="700"))
    return W, H, "".join(s)


# ---------------------------------------------------------------- 图 1 全链
def fig_chain():
    W, H = 960, 400
    s = [head(W, "从电极到文件：六个环节，两处不可逆")]
    s.append(sine(40, 200, 96, 24, 1.6, ACC, 2.6))
    s.append(T(88, 272, "电极电压", 22, GRAY, weight="700"))
    s.append(line(140, 200, 862, 200, LINE, 2))
    names = [("第二点", None), ("放大", None), ("滤波", None),
             ("采样", "不可逆"), ("量化", "不可逆"), ("换算", None)]
    x = 158
    for n, tag in names:
        fill = REDT if tag else PANEL
        stroke = RED if tag else CARD_L
        s += blk(x, 152, 106, 96, n, tag, fill, stroke)
        x += 118
    s.append(arrow(858, 200, 884, 200))
    s.append(T(910, 190, "1204", 22, INK, weight="700"))
    s.append(T(910, 218, "1231", 22, INK, weight="700"))
    s.append(T(910, 272, "文件", 22, GRAY, weight="700"))
    s.append(line(60, 316, 900, 316, LINE, 1.6))
    s.append(T(480, 360, "时间上取点、幅值上归档都补不回来；放大与滤波保证这两步落在合适范围内",
               24, BODY, weight="700"))
    return W, H, "".join(s)


# ---------------------------------------------------------------- 图 2 单端 / 差分
def fig_two_refs():
    W, H = 960, 430
    s = [head(W, "第二个点取在哪里，量出来就是不同的量")]
    s.append(box(40, 96, 420, 290, "#FFFFFF", CARD_L, rx=16, sw=1.8))
    s.append(T(250, 140, "单端测量", 28, ACCD, weight="700"))
    for y in (200, 250, 300):
        s.append(circ(120, y, 13, TINT, ACC, 2))
        s.append(line(133, y, 290, y, ACC, 2.4))
    s.append(T(120, 344, "各通道电极", 21, GRAY, weight="700"))
    s.append(box(290, 180, 130, 140, PANEL, CARD_L, rx=12, sw=1.8))
    s.append(T(355, 244, "设备", 24, INK, weight="700"))
    s.append(T(355, 276, "公共点", 22, GRAY, weight="700"))
    s.append(T(250, 372, "所有通道共用同一个第二点", 22, BODY, weight="700"))
    s.append(box(500, 96, 420, 290, "#FFFFFF", CARD_L, rx=16, sw=1.8))
    s.append(T(710, 140, "差分测量", 28, ACCD, weight="700"))
    s.append(circ(580, 212, 13, TINT, ACC, 2))
    s.append(T(580, 188, "电极", 20, GRAY, weight="700"))
    s.append(circ(580, 296, 13, TINT, GRN, 2))
    s.append(T(580, 334, "另一电极", 20, GRAY, weight="700"))
    s.append(line(593, 212, 744, 212, ACC, 2.4))
    s.append(line(593, 296, 744, 296, GRN, 2.4))
    s.append(box(744, 190, 130, 128, PANEL, CARD_L, rx=12, sw=1.8))
    s.append(T(809, 262, "两者之差", 24, INK, weight="700"))
    s.append(T(710, 372, "第二点是另一个电极", 22, BODY, weight="700"))
    return W, H, "".join(s)


# ---------------------------------------------------------------- 图 3 增益与档位
def fig_gain_steps():
    W, H = 960, 450
    s = [head(W, "档宽固定，增益决定信号跨过多少个档位")]
    stepw = 26.0
    for x0, title, amp, note in ((60, "增益偏小", 20, "整段只跨两档，波形成为台阶"),
                                 (510, "增益合适", 104, "跨过许多档，波形有形状")):
        s.append(box(x0, 96, 390, 258, "#FFFFFF", CARD_L, rx=16, sw=1.8))
        s.append(T(x0 + 195, 136, title, 28, ACCD, weight="700"))
        cy = 250
        k = -4
        while k <= 4:
            s.append(line(x0 + 26, cy + k * stepw, x0 + 364, cy + k * stepw, LINE, 1.2, dash="6 6"))
            k += 1
        x1, w = x0 + 36, 320
        s.append(sine(x1, cy, w, amp, 1.4, GRAY, 2.2))
        seg = 26
        d = []
        prev = None
        for i in range(seg):
            xa = x1 + w * i / seg
            xb = x1 + w * (i + 1) / seg
            yv = cy - amp * math.sin(2 * math.pi * 1.4 * (i + 0.5) / seg)
            kq = math.floor((yv - cy) / stepw + 0.5)
            yq = cy + kq * stepw
            if prev is not None and abs(prev - yq) > 0.5:
                d.append("M%.1f,%.1f L%.1f,%.1f" % (xa, prev, xa, yq))
            d.append("M%.1f,%.1f L%.1f,%.1f" % (xa, yq, xb, yq))
            prev = yq
        s.append(path("".join(d), ACC, 3))
        s.append(T(x0 + 195, 386, note, 23, BODY, weight="700"))
    s.append(T(480, 424, "灰线为输入信号，蓝线为量化后的输出，虚线间隔是同一个档宽",
               22, GRAY, weight="700"))
    return W, H, "".join(s)


# ---------------------------------------------------------------- 图 4 削顶
def fig_clip():
    W, H = 960, 400
    s = [head(W, "超出输入范围的部分，记录里只剩一条平线")]
    top, bot, cy = 150, 310, 230
    s.append(line(120, top, 860, top, RED, 2, dash="10 8"))
    s.append(line(120, bot, 860, bot, RED, 2, dash="10 8"))
    s.append(T(96, top + 8, "上限", 22, RED, anchor="end", weight="700"))
    s.append(T(96, bot + 8, "下限", 22, RED, anchor="end", weight="700"))
    d, dd = [], []
    pts = 300
    for i in range(pts + 1):
        x = 140 + 700 * i / pts
        y = cy - 130 * math.sin(2 * math.pi * 2 * i / pts)
        d.append(("M" if i == 0 else "L") + "%.1f,%.1f" % (x, y))
        yc = min(max(y, top), bot)
        dd.append(("M" if i == 0 else "L") + "%.1f,%.1f" % (x, yc))
    s.append(path("".join(d), GRAY, 2, dash="8 7"))
    s.append(path("".join(dd), ACC, 3.4))
    s.append(T(480, 366, "灰虚线是实际信号，蓝线是记录到的；被削掉的高度没有留下痕迹",
               24, BODY, weight="700"))
    return W, H, "".join(s)


# ---------------------------------------------------------------- 图 5 放大器远近
def fig_headstage():
    W, H = 960, 470
    s = [head(W, "线上耦合的干扰是固定量，先放大再走线，它就相对很小")]
    rows = [(112, "放大器放在远端", "far", "50 µV 信号 + 100 µV 干扰", "信号与干扰 1 : 2", RED),
            (288, "放大器紧挨电极", "near", "50 mV 信号 + 100 µV 干扰", "信号与干扰 500 : 1", GRN)]
    for y0, title, pos, onwire, ratio, col in rows:
        s.append(T(44, y0 + 24, title, 26, ACCD, anchor="start", weight="700"))
        cy = y0 + 84
        s.append(circ(58, cy, 13, TINT, ACC, 2))
        s.append(T(58, cy + 44, "电极", 20, GRAY, weight="700"))
        if pos == "far":
            s.append(line(71, cy, 452, cy, ACC, 3))
            s.append(T(262, cy - 18, onwire, 22, col, weight="700"))
            s.append(T(262, cy + 36, "线缆走的是原始信号", 20, GRAY, weight="700"))
            s += blk(452, cy - 34, 124, 68, "放大器")
            s.append(line(576, cy, 620, cy, ACC, 3))
        else:
            s += blk(96, cy - 34, 124, 68, "放大器")
            s.append(line(220, cy, 620, cy, ACC, 3))
            s.append(T(420, cy - 18, onwire, 22, col, weight="700"))
            s.append(T(420, cy + 36, "线缆走的是放大后信号", 20, GRAY, weight="700"))
        s.append(box(620, cy - 34, 96, 68, PANEL, CARD_L, rx=14, sw=2))
        s.append(T(668, cy + 10, "ADC", 26, INK, weight="700"))
        s.append(T(840, cy + 8, ratio, 22, col, weight="700"))
    s.append(line(44, 268, 916, 268, LINE, 1.6))
    s.append(T(480, 444, "同样的线、同样的环境，差别只在这段线上走的信号已经放大还是没有",
               24, BODY, weight="700"))
    return W, H, "".join(s)


# ---------------------------------------------------------------- 图 6 采样
def fig_sampling():
    W, H = 960, 380
    s = [head(W, "采样：只在固定间隔的时刻取值")]
    cy = 210
    s.append(sine(110, cy, 740, 90, 2.2, GRAY, 2.4))
    pts = 19
    for i in range(pts):
        x = 110 + 740 * i / (pts - 1)
        y = cy - 90 * math.sin(2 * math.pi * 2.2 * i / (pts - 1))
        s.append(line(x, cy + 118, x, y, LINE, 1.4, dash="5 5"))
        s.append(circ(x, y, 7, ACC, ACCD, 1.6))
    s.append(line(90, cy + 118, 880, cy + 118, INK, 2))
    s.append(T(480, cy + 150, "时间", 22, GRAY, weight="700"))
    s.append(T(480, 352, "灰线是实际电压，蓝点是记录下来的值；两点之间发生了什么，文件里没有",
               24, BODY, weight="700"))
    return W, H, "".join(s)


# ---------------------------------------------------------------- 图 7 混叠
def fig_alias():
    W, H = 960, 410
    s = [head(W, "两个不同频率，在同一组取值点上给出同一串数")]
    cy, amp = 226, 88
    x0, w, n = 110, 740, 10
    s.append(sine(x0, cy, w, amp, 9, RED, 2))
    s.append(sine(x0, cy, w, amp, 1, ACC, 3.2, phase=math.pi))
    for i in range(n + 1):
        x = x0 + w * i / n
        y = cy - amp * math.sin(2 * math.pi * 9 * i / n)
        s.append(line(x, cy + 116, x, y, LINE, 1.4, dash="5 5"))
        s.append(circ(x, y, 7, INK, INK, 1.4))
    s.append(line(90, cy + 116, 880, cy + 116, INK, 2))
    s.append(T(230, 110, "红：900 Hz 的真实成分", 23, RED, weight="700"))
    s.append(T(720, 110, "蓝：记录里读成 100 Hz", 23, ACCD, weight="700"))
    s.append(T(480, 386, "采样率 1000 Hz 时，高于 500 Hz 的成分折回到 500 Hz 以下，事后无法分开",
               24, BODY, weight="700"))
    return W, H, "".join(s)


# ---------------------------------------------------------------- 图 8 量化
def fig_quantize():
    W, H = 960, 400
    s = [head(W, "量化：落在同一档的电压，输出同一个整数")]
    cy, amp = 224, 96
    x0, w = 170, 640
    nst = 8
    stepw = 2 * amp / nst
    for i in range(nst + 1):
        y = cy - amp + i * stepw
        s.append(line(x0 - 26, y, x0 + w + 26, y, LINE, 1.3, dash="6 6"))
    for i in range(nst):
        y = cy - amp + i * stepw + stepw / 2
        s.append(T(x0 - 42, y + 7, str(nst - i + 1200), 19, GRAY, anchor="end", weight="700"))
    s.append(T(x0 - 42, 140, "输出编号", 20, GRAY, anchor="end", weight="700"))
    s.append(sine(x0, cy, w, amp * 0.92, 1.3, GRAY, 2.2))
    seg, d, prev = 24, [], None
    for i in range(seg):
        xa = x0 + w * i / seg
        xb = x0 + w * (i + 1) / seg
        yv = cy - amp * 0.92 * math.sin(2 * math.pi * 1.3 * (i + 0.5) / seg)
        k = int((yv - (cy - amp)) // stepw)
        k = max(0, min(nst - 1, k))
        yq = cy - amp + k * stepw + stepw / 2
        if prev is not None and abs(prev - yq) > 0.5:
            d.append("M%.1f,%.1f L%.1f,%.1f" % (xa, prev, xa, yq))
        d.append("M%.1f,%.1f L%.1f,%.1f" % (xa, yq, xb, yq))
        prev = yq
    s.append(path("".join(d), ACC, 3.2))
    s.append(T(480, 366, "灰线是输入电压，蓝线是输出的整数；档宽 = 输入范围 ÷ 2 的位数次方",
               24, BODY, weight="700"))
    return W, H, "".join(s)


# ---------------------------------------------------------------- 表 1 三种失败
def fig_failures():
    W = 960
    rows = [
        [["**削顶**"], ["放大与", "输入范围"], ["波形顶部被切平，出现一段恒定值"],
         ["**只能重录**"]],
        [["**混叠**"], ["采样"], ["波形看上去正常，却多出本不存在的频率"], ["**只能重录**"]],
        [["幅度比例错误"], ["换算"], ["形状、频率、时间全对，幅度整体差一个倍数"], ["改参数重算"]],
    ]
    s, bottom = table(W, "三种典型失败，发生在哪一步", [180, 150, 420, 170],
                      ["现象", "发生在", "特征", "能否补救"], rows, lh=36, pad=34)
    return W, bottom + 20, "".join(s)


FIGS = {
    "cover-concept": cover_concept, "toc": toc,
    "fig1-chain": fig_chain, "fig2-two-refs": fig_two_refs,
    "fig3-gain-steps": fig_gain_steps, "fig4-clip": fig_clip,
    "fig5-headstage": fig_headstage, "fig6-sampling": fig_sampling,
    "fig7-alias": fig_alias, "fig8-quantize": fig_quantize,
    "fig9-failures": fig_failures,
}

if __name__ == "__main__":
    names = sys.argv[1:] or list(FIGS)
    for n in names:
        w, h, inner = FIGS[n]()
        print(ioreq1_figs.render(n, w, int(h), inner))
