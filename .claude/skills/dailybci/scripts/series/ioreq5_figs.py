# -*- coding: utf-8 -*-
"""2026-09-23 · 模拟输出（AO）接口，何时用和怎么用（电生理 IO 系列 ep05）—— 自制示意图"""
import os, sys, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from grounding2_figs import (T, box, line, circ, path, ACC, ACCD, TINT, INK, BODY,
                             GRAY, LINE, RED, REDT, GRN, GRNT, CARD_L, PANEL)
import ioreq1_figs
from ioreq2_figs import table

SKILL_DIR = os.path.dirname(os.path.dirname(HERE))
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-09-13-electrophysiology-io",
                   "ep05-2026-09-23-analog-output", "figs")
os.makedirs(OUT, exist_ok=True)
ioreq1_figs.OUT = OUT


def head(W, s, y=46, size=30):
    return T(W / 2, y, s, size, INK, weight="700")


def blk(x, y, w, h, name, sub=None, fill=PANEL, stroke=CARD_L, col=INK, size=26):
    s = [box(x, y, w, h, fill, stroke, rx=14, sw=2),
         T(x + w / 2, y + (h / 2 + 10 if not sub else h / 2 - 4), name, size, col, weight="700")]
    if sub:
        s.append(T(x + w / 2, y + h / 2 + 28, sub, 20, GRAY, weight="700"))
    return s


MK = {INK: "ahk", ACC: "ah", RED: "ahr", GRAY: "ahg"}


def arrow(x1, y1, x2, y2, stroke=INK, sw=2.6):
    return line(x1, y1, x2, y2, stroke, sw, marker=MK.get(stroke, "ahk"))


def sine(x0, y0, w, amp, cycles, stroke=ACC, sw=2.6, phase=0.0, pts=240):
    d = []
    for i in range(pts + 1):
        x = x0 + w * i / pts
        y = y0 - amp * math.sin(2 * math.pi * cycles * i / pts + phase)
        d.append(("M" if i == 0 else "L") + "%.1f,%.1f" % (x, y))
    return path("".join(d), stroke, sw)


def two_way(W, y0, title_left, sub_left, items_left, title_right, sub_right, items_right):
    s = []
    s += blk(W / 2 - 110, y0, 220, 80, "Analog Out", "模拟输出接口", TINT, ACC, ACCD)
    cx = W / 2
    s.append(path("M%d,%d L%d,%d L%d,%d" % (cx, y0 + 80, cx, y0 + 116, 250, y0 + 116), INK, 2.4))
    s.append(path("M%d,%d L%d,%d" % (cx, y0 + 116, 710, y0 + 116), INK, 2.4))
    s.append(arrow(250, y0 + 116, 250, y0 + 150))
    s.append(arrow(710, y0 + 116, 710, y0 + 150))
    for x, t, sub, items, col, fill in ((250, title_left, sub_left, items_left, GRN, GRNT),
                                        (710, title_right, sub_right, items_right, RED, REDT)):
        s.append(box(x - 200, y0 + 154, 400, 64, fill, col, rx=14, sw=2))
        s.append(T(x, y0 + 196, t, 28, col, weight="700"))
        s.append(T(x, y0 + 252, sub, 22, BODY, weight="700"))
        for i, it in enumerate(items):
            s.append(T(x, y0 + 292 + i * 32, it, 21, GRAY, weight="700"))
    return s


# ---------------------------------------------------------------- 封面
def cover_concept():
    W, H = 960, 420
    s = [box(90, 40, 780, 230, PANEL, CARD_L, rx=18, sw=2)]
    s.append(T(130, 84, "采集设备后面板", 22, GRAY, anchor="start", weight="700"))
    for i in range(4):
        cx = 230 + i * 170
        s.append(circ(cx, 160, 38, "#FFFFFF", INK, 3))
        s.append(circ(cx, 160, 12, INK, INK, 1))
        s.append(T(cx, 232, "AO %d" % (i + 1), 22, INK, weight="700"))
    s.append(T(480, 328, "这排接口，什么时候接？接什么？", 30, ACCD, weight="700"))
    s.append(T(480, 376, "监看：送出记录到的信号　　控制：送出要执行的指令", 22, BODY, weight="700"))
    return W, H, "".join(s)


# ---------------------------------------------------------------- 目录
def toc():
    W, H = 960, 470
    s = [T(480, 66, "本期路线", 40, INK, weight="700"), line(120, 96, 840, 96, LINE, 1.8)]
    items = [
        ("①", "监看", "实验当下看波形、听声音；数字怎样变回电压"),
        ("②", "控制", "同样 1 V 代表不同的量；什么时候才需要模拟输出"),
        ("③", "怎么连、怎么选", "接收端确认两件事；需求对应哪种口"),
    ]
    y = 170
    for n, t, d in items:
        s.append(circ(150, y - 9, 26, TINT, ACC, 2.4))
        s.append(T(150, y + 1, n, 28, ACCD, weight="700"))
        s.append(T(204, y - 2, t, 32, INK, anchor="start", weight="700"))
        s.append(T(204, y + 36, d, 24, BODY, anchor="start"))
        y += 96
    s.append(line(120, 430, 840, 430, LINE, 1.6))
    s.append(T(480, 458, "本期不解读文献，从基础原理梳理模拟输出", 22, GRAY, weight="700"))
    return W, H, "".join(s)


# ---------------------------------------------------------------- 图 1 两类用途
def fig_two_uses():
    W, H = 960, 440
    s = [head(W, "按电压交给谁、代表什么，用途只有两类")]
    s += two_way(W, 76, "监看", "电压 = 已经发生的信号",
                 ["接示波器看波形", "接音箱听声音", "送另一台设备记录"],
                 "控制", "电压 = 要执行的指令",
                 ["光源驱动器 → 光强", "刺激隔离器 → 刺激电流", "膜片钳放大器 → 钳制电压"])
    return W, H, "".join(s)


# ---------------------------------------------------------------- 图 2 软件监听 vs 硬件输出
def fig_paths():
    W, H = 960, 420
    s = [head(W, "软件监听要经过电脑，模拟输出直接从采集设备送出")]
    s += blk(40, 176, 150, 76, "采集设备")
    # 上路：软件
    s.append(T(120, 150, "电极信号已在这里数字化", 19, GRAY, weight="700"))
    s.append(path("M190,200 L240,200 L240,130 L270,130", INK, 2.4, marker="ahk"))
    s += blk(270, 96, 150, 68, "电脑软件")
    s.append(arrow(420, 130, 470, 130))
    s += blk(470, 96, 150, 68, "声卡")
    s.append(arrow(620, 130, 670, 130))
    s += blk(670, 96, 150, 68, "音箱")
    s.append(T(545, 196, "路径一：经过电脑的处理与缓冲", 21, GRAY, weight="700"))
    # 下路：硬件
    s.append(path("M190,228 L240,228 L240,300 L270,300", ACC, 3, marker="ah"))
    s += blk(270, 266, 150, 68, "模拟输出", None, TINT, ACC, ACCD)
    s.append(line(420, 300, 670, 300, ACC, 3, marker="ah"))
    s += blk(670, 266, 200, 68, "示波器或音箱", size=24)
    s.append(T(545, 362, "路径二：不经过电脑，延迟更低，示波器等仪器只接电压", 21, ACCD, weight="700"))
    s.append(T(480, 404, "只看和听时，路径一多数时候已经够用", 22, BODY, weight="700"))
    return W, H, "".join(s)


# ---------------------------------------------------------------- 图 3 DAC 三步
def fig_dac():
    W, H = 960, 430
    s = [head(W, "数模转换：按档给电压、保持到下一个数、再把台阶磨平")]
    n, cyc, amp, base0 = 12, 1.4, 3.2, 5.0
    vals = [round(base0 + amp * math.sin(2 * math.pi * cyc * (i + 0.5) / n)) for i in range(n)]
    s.append(T(150, 102, "① 一串整数", 24, ACCD, weight="700"))
    for i, v in enumerate(vals[:6]):
        s.append(T(60 + i * 36, 150, str(v), 26, INK, weight="700"))
    s.append(T(150, 188, "按固定间隔送进来", 20, GRAY, weight="700"))
    x0, w, base, stepw = 320, 280, 340, 24
    s.append(T(x0 + w / 2, 102, "② 台阶：保持到下一个数", 24, ACCD, weight="700"))
    d, prev = [], None
    for i, v in enumerate(vals):
        xa = x0 + w * i / n
        xb = x0 + w * (i + 1) / n
        y = base - v * stepw
        if prev is not None:
            d.append("M%.1f,%.1f L%.1f,%.1f" % (xa, prev, xa, y))
        d.append("M%.1f,%.1f L%.1f,%.1f" % (xa, y, xb, y))
        prev = y
    s.append(path("".join(d), ACC, 3))
    s.append(line(x0, base + 10, x0 + w, base + 10, INK, 1.6))
    s.append(arrow(612, 226, 660, 226))
    x1 = 672
    s.append(T(x1 + 130, 102, "③ 重建滤波后", 24, ACCD, weight="700"))
    pts = []
    for i in range(201):
        x = x1 + 260 * i / 200
        v = base0 + amp * math.sin(2 * math.pi * cyc * (i / 200))
        pts.append(("M" if i == 0 else "L") + "%.1f,%.1f" % (x, base - v * stepw))
    s.append(path("".join(pts), GRN, 3))
    s.append(line(x1, base + 10, x1 + 260, base + 10, INK, 1.6))
    s.append(arrow(262, 226, 306, 226))
    s.append(T(480, 404, "输出是选定通道信号的复原；复原得好不好，取决于当初采样是否够密", 23, BODY, weight="700"))
    return W, H, "".join(s)


# ---------------------------------------------------------------- 图 4 同样 1 V
def fig_one_volt():
    W, H = 960, 440
    s = [head(W, "同样的 1 V，接到不同设备上代表不同的量")]
    s += blk(50, 196, 170, 90, "1 V", "模拟输出送出", TINT, ACC, ACCD, size=34)
    rows = [(110, "光源驱动器", "电压越高，光越强"),
            (220, "刺激隔离器", "按比例转成刺激电流"),
            (330, "膜片钳放大器", "电压钳下 20 或 100 mV¹")]
    for y, name, what in rows:
        s.append(path("M220,241 L300,241 L300,%d L360,%d" % (y + 34, y + 34), INK, 2.2, marker="ahk"))
        s += blk(360, y, 220, 68, name)
        s.append(arrow(580, y + 34, 620, y + 34))
        s.append(T(630, y + 42, what, 23, BODY, anchor="start", weight="700"))
    s.append(T(480, 428, "电压本身没有单位，每伏对应多少由接收端决定", 23, ACCD, weight="700"))
    return W, H, "".join(s)


# ---------------------------------------------------------------- 图 5 三层控制
def fig_three_modes():
    W, H = 960, 440
    s = [head(W, "作用量要不要随时间变化，决定用哪种控制")]
    cols = [(40, "设备面板设定", "强度固定，不需对时", "const"),
            (340, "数字输出（TTL）", "强度固定，开关要对齐", "ttl"),
            (640, "模拟输出", "强度本身要变化", "ao")]
    for x, t, sub, kind in cols:
        col = ACC if kind == "ao" else INK
        s.append(box(x, 90, 280, 290, "#FFFFFF", RED if kind == "ao" else CARD_L, rx=16,
                     sw=2.4 if kind == "ao" else 1.8))
        s.append(T(x + 140, 132, t, 26, RED if kind == "ao" else ACCD, weight="700"))
        base, top = 300, 200
        s.append(line(x + 24, base + 14, x + 256, base + 14, LINE, 1.4))
        if kind == "const":
            s.append(line(x + 30, 240, x + 250, 240, col, 3))
        elif kind == "ttl":
            s.append(path("M%d,%d L%d,%d L%d,%d L%d,%d L%d,%d L%d,%d L%d,%d L%d,%d L%d,%d" % (
                x + 30, base, x + 70, base, x + 70, top + 30, x + 130, top + 30, x + 130, base,
                x + 170, base, x + 170, top + 30, x + 230, top + 30, x + 230, base), col, 3))
        else:
            pts = []
            for i in range(121):
                xx = x + 30 + 220 * i / 120
                ramp = i / 120
                yy = base - (ramp * 60 + 30 * math.sin(2 * math.pi * 2.5 * i / 120) + 40)
                pts.append(("M" if i == 0 else "L") + "%.1f,%.1f" % (xx, yy))
            s.append(path("".join(pts), col, 3))
        s.append(T(x + 140, 356, sub, 22, BODY, weight="700"))
    s.append(T(480, 420, "只要开和关，第二种就够了；多数光刺激落在这里", 23, BODY, weight="700"))
    return W, H, "".join(s)


# ---------------------------------------------------------------- 图 6 怎么连
def fig_connect():
    W, H = 960, 400
    s = [head(W, "一根信号线加一根参考线；接收端先确认两件事")]
    s += blk(40, 130, 200, 90, "采集设备", "模拟输出", TINT, ACC, ACCD)
    s += blk(720, 130, 200, 90, "被控设备", "模拟输入")
    s.append(line(240, 160, 720, 160, ACC, 3))
    s.append(line(240, 192, 720, 192, INK, 3))
    s.append(T(480, 148, "信号线（BNC 同轴线的芯线）", 21, ACCD, weight="700"))
    s.append(T(480, 222, "参考线（外层）", 21, INK, weight="700"))
    for i, (t, sub) in enumerate((("① 切到外部模拟控制", "否则接上的电压不起作用"),
                                  ("② 每伏对应多少作用量", "软件里的电压 × 这个比例 = 实际施加的量"))):
        y = 290 + i * 58
        s.append(T(560, y, t, 23, RED, anchor="start", weight="700"))
        s.append(T(560, y + 26, sub, 19, GRAY, anchor="start", weight="700"))
    s.append(T(560, 252, "接收端先确认：", 21, INK, anchor="start", weight="700"))
    s.append(T(60, 290, "也有设备用多针接头或接线端子，", 20, GRAY, anchor="start", weight="700"))
    s.append(T(60, 318, "接法相同", 20, GRAY, anchor="start", weight="700"))
    return W, H, "".join(s)


# ---------------------------------------------------------------- 表 1
def fig_table():
    W = 960
    rows = [
        [["实验当下看波形、听声音"], ["软件显示与监听；", "要接示波器或另一台设备时，", "才用模拟输出"]],
        [["刺激强度固定，", "不需要和记录对时"], ["设备面板自己设定"]],
        [["刺激强度固定，", "开始与结束要跟实验对齐"], ["数字输出（TTL）"]],
        [["**刺激强度要随时间变化，**", "**或按记录实时调整**"], ["**模拟输出，**", "**接被控设备的模拟输入**"]],
    ]
    s, bottom = table(W, "你的需求，对应哪种口", [440, 440], ["需求", "用什么"], rows,
                      lh=34, pad=30, first_color=INK)
    return W, bottom + 20, "".join(s)


FIGS = {
    "cover-concept": cover_concept, "toc": toc, "fig1-two-uses": fig_two_uses,
    "fig2-paths": fig_paths, "fig3-dac": fig_dac, "fig4-one-volt": fig_one_volt,
    "fig5-three-modes": fig_three_modes, "fig6-connect": fig_connect, "fig7-table": fig_table,
}

if __name__ == "__main__":
    names = sys.argv[1:] or list(FIGS)
    for n in names:
        w, h, inner = FIGS[n]()
        print(ioreq1_figs.render(n, w, int(h), inner))
