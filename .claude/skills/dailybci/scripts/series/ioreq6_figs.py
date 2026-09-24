# -*- coding: utf-8 -*-
"""2026-09-24 · 数字接口（DIO），怎样发指令和记事件（电生理 IO 系列 ep06）—— 自制示意图"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from grounding2_figs import (T, box, line, circ, path, ACC, ACCD, TINT, INK, BODY,
                             GRAY, LINE, RED, REDT, GRN, GRNT, CARD_L, PANEL)
import ioreq1_figs
from ioreq2_figs import table

SKILL_DIR = os.path.dirname(os.path.dirname(HERE))
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-09-13-electrophysiology-io",
                   "ep06-2026-09-24-digital-io", "figs")
os.makedirs(OUT, exist_ok=True)
ioreq1_figs.OUT = OUT

MK = {INK: "ahk", ACC: "ah", RED: "ahr", GRAY: "ahg", GRN: "ahn"}


def head(W, s, y=46, size=30):
    return T(W / 2, y, s, size, INK, weight="700")


def arrow(x1, y1, x2, y2, stroke=INK, sw=2.6):
    return line(x1, y1, x2, y2, stroke, sw, marker=MK.get(stroke, "ahk"))


def sq(x0, x1, ylo, yhi, edges, start_high=False, stroke=INK, sw=3):
    """方波：edges 为跳变处的 x 坐标列表，从 x0 画到 x1。"""
    lvl = start_high
    y = yhi if lvl else ylo
    d = "M%.1f,%.1f" % (x0, y)
    for e in edges:
        d += " L%.1f,%.1f" % (e, y)
        lvl = not lvl
        y = yhi if lvl else ylo
        d += " L%.1f,%.1f" % (e, y)
    d += " L%.1f,%.1f" % (x1, y)
    return path(d, stroke, sw)


# ---------------------------------------------------------------- 封面
def cover_concept():
    W, H = 960, 420
    s = [box(90, 40, 780, 236, PANEL, CARD_L, rx=18, sw=2)]
    s.append(T(130, 82, "采集设备的数字口", 22, GRAY, anchor="start", weight="700"))
    for row, (lab, y, col) in enumerate((("DI", 138, GRN), ("DO", 218, ACC))):
        s.append(T(150, y + 9, lab, 26, col, weight="700"))
        for i in range(8):
            cx = 230 + i * 70
            s.append(box(cx - 20, y - 20, 40, 40, "#FFFFFF", INK, rx=6, sw=2.4))
            s.append(circ(cx, y, 7, INK, INK, 1))
    s.append(arrow(840, 138, 800, 138, GRN))
    s.append(arrow(800, 218, 840, 218, ACC))
    s.append(T(480, 332, "一个事件，怎样被正确发出、正确记下？", 30, ACCD, weight="700"))
    s.append(T(480, 380, "数字输出：发指令　　　数字输入：记事件", 22, BODY, weight="700"))
    return W, H, "".join(s)


# ---------------------------------------------------------------- 目录
def toc():
    W, H = 960, 520
    s = [T(480, 66, "本期路线", 40, INK, weight="700"), line(120, 96, 840, 96, LINE, 1.8)]
    items = [
        ("①", "数字口传什么", "高低两种电平、TTL、有效极性（两类用途共用）"),
        ("A", "发指令（数字输出）", "接收端怎样执行；由谁定时；接线前核对"),
        ("B", "记事件（数字输入）", "漏记、多记、记错各从哪来；软件里设什么"),
        ("✓", "结语", "按现象倒查原因"),
    ]
    y = 166
    for n, t, d in items:
        s.append(circ(150, y - 9, 26, TINT, ACC, 2.4))
        s.append(T(150, y + 1, n, 26, ACCD, weight="700"))
        s.append(T(204, y - 2, t, 32, INK, anchor="start", weight="700"))
        s.append(T(204, y + 36, d, 24, BODY, anchor="start"))
        y += 86
    s.append(line(120, 478, 840, 478, LINE, 1.6))
    s.append(T(480, 506, "本期不解读文献，从基础原理梳理数字输入输出", 22, GRAY, weight="700"))
    return W, H, "".join(s)


# ---------------------------------------------------------------- 图 1 电平判定
def fig_levels():
    W, H = 960, 460
    s = [head(W, "TTL 输入：高于 2 V 判为高，低于 0.8 V 判为低")]
    x, w, top, bot = 330, 120, 90, 400  # 0–5 V 映射到 bot–top
    v2y = lambda v: bot - (bot - top) * v / 5.0
    s.append(box(x, v2y(5), w, v2y(2) - v2y(5), GRNT, GRN, rx=0, sw=2))
    s.append(box(x, v2y(2), w, v2y(0.8) - v2y(2), PANEL, CARD_L, rx=0, sw=2))
    s.append(box(x, v2y(0.8), w, v2y(0) - v2y(0.8), TINT, ACC, rx=0, sw=2))
    s.append(T(x + w / 2, (v2y(5) + v2y(2)) / 2 + 10, "判为高", 26, GRN, weight="700"))
    s.append(T(x + w / 2, (v2y(2) + v2y(0.8)) / 2 + 8, "不确定", 22, GRAY, weight="700"))
    s.append(T(x + w / 2, (v2y(0.8) + v2y(0)) / 2 + 9, "判为低", 24, ACCD, weight="700"))
    for v, lab in ((5, "5 V"), (2, "2 V"), (0.8, "0.8 V"), (0, "0 V")):
        s.append(line(x - 14, v2y(v), x, v2y(v), INK, 2))
        s.append(T(x - 22, v2y(v) + 8, lab, 22, INK, anchor="end", weight="700"))
    # 右侧标注
    s.append(line(x + w + 10, v2y(5), x + w + 60, v2y(5), GRAY, 1.6, dash="5 5"))
    s.append(T(x + w + 70, v2y(5) + 8, "TTL 信号的高电平：约 5 V", 22, BODY, anchor="start", weight="700"))
    s.append(line(x + w + 10, v2y(3.3), x + w + 60, v2y(3.3), GRAY, 1.6, dash="5 5"))
    s.append(T(x + w + 70, v2y(3.3) + 8, "3.3 V 设备的高电平：也高于 2 V", 22, BODY, anchor="start", weight="700"))
    s.append(line(x + w + 10, v2y(0), x + w + 60, v2y(0), GRAY, 1.6, dash="5 5"))
    s.append(T(x + w + 70, v2y(0) + 8, "TTL 信号的低电平：约 0 V", 22, BODY, anchor="start", weight="700"))
    s.append(T(480, 448, "阈值取自 TI SN7400 数据手册", 18, GRAY, weight="700"))
    return W, H, "".join(s)


# ---------------------------------------------------------------- 图 2 有效极性
def fig_polarity():
    W, H = 960, 420
    s = [head(W, "同一段电平，极性约定不同，「事件」就整体对调")]
    x0, x1 = 170, 900
    e = [420, 560]
    s.append(T(150, 138, "线上电平", 22, INK, anchor="end", weight="700"))
    s.append(sq(x0, x1, 150, 100, e, stroke=INK))
    s.append(T(x0 - 6, 104, "高", 18, GRAY, anchor="end"))
    s.append(T(x0 - 6, 156, "低", 18, GRAY, anchor="end"))
    rows = (("高电平有效", 230, [(e[0], e[1])], GRN, GRNT, "事件 = 高电平这一段"),
            ("低电平有效", 320, [(x0, e[0]), (e[1], x1)], RED, REDT, "事件 = 其余全部时间"))
    for lab, y, spans, col, fill, note in rows:
        s.append(T(150, y + 8, lab, 22, col, anchor="end", weight="700"))
        s.append(line(x0, y, x1, y, LINE, 2))
        for a, b in spans:
            s.append(box(a, y - 18, b - a, 36, fill, col, rx=6, sw=2))
        s.append(T(535, y + 50, note, 21, col, weight="700"))
    for xe in e:
        s.append(line(xe, 90, xe, 350, GRAY, 1.4, dash="4 5"))
    return W, H, "".join(s)


# ---------------------------------------------------------------- 图 3 边沿触发与门控
def fig_edge_gated():
    W, H = 960, 470
    s = [head(W, "边沿触发只看开始；门控时脉冲多宽，就执行多久")]
    cols = ((150, 460, 250, 300, "短脉冲"), (520, 830, 620, 780, "长脉冲"))
    ys = (("输入脉冲", 130, INK), ("边沿触发的输出", 250, ACC), ("门控的输出", 370, RED))
    for lab, y, col in ys:
        s.append(T(20, y - 12, lab, 21, col, anchor="start", weight="700"))
    for xa, xb, r, f, name in cols:
        s.append(T((xa + xb) / 2, 84, name, 22, GRAY, weight="700"))
        s.append(sq(xa, xb, 150, 110, [r, f], stroke=INK))
        # 边沿触发：从上升沿起输出固定长度的一串脉冲
        tr = [r + 10 + k * 28 for k in range(8)]
        s.append(sq(xa, xb, 270, 230, tr, stroke=ACC))
        # 门控：输出与输入同宽
        s.append(sq(xa, xb, 390, 350, [r, f], stroke=RED))
        s.append(line(r, 104, r, 400, GRAY, 1.2, dash="4 5"))
    s.append(T(480, 300, "两种脉冲宽度下输出相同：预设好的一段", 20, ACCD, weight="700"))
    s.append(T(480, 430, "输出宽度跟着输入宽度变", 20, RED, weight="700"))
    s.append(T(480, 458, "Pulse Pal 的触发输入两种方式都提供", 18, GRAY, weight="700"))
    return W, H, "".join(s)


# ---------------------------------------------------------------- 图 4 硬件定时与软件定时
def fig_timing():
    W, H = 960, 420
    s = [head(W, "同一个脉冲发 5 次：硬件定时的沿对齐，软件定时的沿散开")]
    panels = ((60, "硬件定时", ACC, [0] * 5, [0] * 5),
              (510, "软件定时", RED, [0, 14, 5, 26, 9], [6, 30, 2, 18, 38]))
    for x, name, col, dr, df in panels:
        s.append(box(x, 76, 390, 300, "#FFFFFF", CARD_L, rx=14, sw=1.8))
        s.append(T(x + 195, 112, name, 26, col, weight="700"))
        r0, f0 = x + 110, x + 240
        for k in range(5):
            y = 150 + k * 40
            s.append(sq(x + 30, x + 360, y + 26, y, [r0 + dr[k], f0 + df[k]], stroke=col, sw=2.6))
        s.append(line(r0, 140, r0, 350, GRAY, 1.2, dash="4 5"))
        s.append(line(f0, 140, f0, 350, GRAY, 1.2, dash="4 5"))
        s.append(T(r0, 368, "预定开始", 16, GRAY, weight="700"))
        s.append(T(f0, 368, "预定结束", 16, GRAY, weight="700"))
    s.append(T(480, 408, "门控时，开始和结束各自偏移，作用时长也跟着变", 21, BODY, weight="700"))
    return W, H, "".join(s)


# ---------------------------------------------------------------- 图 5 按间隔读取
def fig_sampling():
    W, H = 960, 400
    s = [head(W, "每 50 µs 读一次：窄脉冲可能整个落在两次读取之间")]
    x0, x1, px = 60, 900, 60  # 每 50 µs = 60 px
    ylo, yhi = 230, 150
    wide = (x0 + 2.4 * px, x0 + 6.4 * px)   # 约 200 µs
    narrow = (x0 + 9.25 * px, x0 + 9.75 * px)  # 约 25 µs，落在两次读取之间
    s.append(sq(x0, x1, ylo, yhi, [wide[0], wide[1], narrow[0], narrow[1]], stroke=INK))
    k = 0
    while x0 + k * px <= x1:
        x = x0 + k * px
        s.append(line(x, 110, x, 280, LINE, 1.4))
        inside = wide[0] <= x <= wide[1] or narrow[0] <= x <= narrow[1]
        s.append(circ(x, 300, 8, GRN if inside else "#FFFFFF", GRN if inside else GRAY, 2))
        k += 1
    s.append(T(x0, 336, "读取时刻", 20, GRAY, anchor="start", weight="700"))
    s.append(T((wide[0] + wide[1]) / 2, 136, "宽脉冲：读到 4 次", 21, GRN, weight="700"))
    s.append(T((narrow[0] + narrow[1]) / 2 + 20, 136, "窄脉冲：一次也没读到", 21, RED, weight="700"))
    s.append(T(480, 380, "脉冲宽度要明显大于读取间隔", 22, BODY, weight="700"))
    return W, H, "".join(s)


# ---------------------------------------------------------------- 图 6 触点抖动
def fig_bounce():
    W, H = 960, 440
    s = [head(W, "一次按压，抖动被读成 3 次；加去抖后只算 1 次")]
    x0, x1 = 80, 900
    ylo, yhi = 200, 120
    e = [230, 252, 264, 296, 306]
    s.append(sq(x0, x1, ylo, yhi, e, stroke=INK))
    s.append(T(x0, 104, "开关输出", 20, GRAY, anchor="start", weight="700"))
    # 每 25 px 读一次
    reads = list(range(x0, x1 + 1, 25))
    lvl = lambda x: sum(1 for t in e if t <= x) % 2 == 1
    prev = False
    rises = []
    for x in reads:
        h = lvl(x)
        s.append(circ(x, 226, 5, INK if h else "#FFFFFF", GRAY, 1.6))
        if h and not prev:
            rises.append(x)
        prev = h
    for i, x in enumerate(rises):
        s.append(line(x, 246, x, 290, RED, 3))
        s.append(T(x, 312, "%d" % (i + 1), 20, RED, weight="700"))
    s.append(T(520, 290, "不去抖：记成 %d 个事件" % len(rises), 21, RED, anchor="start", weight="700"))
    # 去抖窗口
    s.append(box(rises[0], 344, 240, 40, TINT, ACC, rx=6, sw=2))
    s.append(T(rises[0] + 120, 371, "去抖窗口：内部跳变不算", 19, ACCD, weight="700"))
    s.append(line(rises[0], 334, rises[0], 392, ACC, 3))
    s.append(T(520, 372, "去抖：只记第 1 次", 21, ACCD, anchor="start", weight="700"))
    s.append(T(480, 428, "窗口要长于抖动时长，又要短于两次真实事件的最短间隔", 20, BODY, weight="700"))
    return W, H, "".join(s)


# ---------------------------------------------------------------- 图 7 选通线
def fig_strobe():
    W, H = 960, 470
    s = [head(W, "从编号 3 换到 4：途中短暂出现 7，选通脉冲等电平稳定后才来")]
    x0, x1 = 170, 900
    t1, t2 = 430, 490            # 线 3 先变高，线 2、线 1 稍后变低
    rows = (("线 3", 110, [t1], False), ("线 2", 190, [t2], True), ("线 1", 270, [t2], True))
    s.append(box(t1, 86, t2 - t1, 226, REDT, RED, rx=0, sw=1.6))
    for lab, y, edges, hi in rows:
        s.append(T(150, y + 8, lab, 22, INK, anchor="end", weight="700"))
        s.append(sq(x0, x1, y + 22, y - 22, edges, start_high=hi, stroke=INK))
    for xc, txt, col in ((300, "编号 3", INK), ((t1 + t2) / 2, "7", RED), (700, "编号 4", INK)):
        s.append(T(xc, 338, txt, 22, col, weight="700"))
    s.append(T(150, 398, "选通线", 22, ACC, anchor="end", weight="700"))
    s.append(sq(x0, x1, 410, 370, [620, 660], stroke=ACC))
    s.append(line(640, 86, 640, 360, ACC, 1.6, dash="5 5"))
    s.append(T(640, 448, "接收端只在这里读：读到 4", 21, ACCD, weight="700"))
    s.append(T(420, 448, "跳变途中不读", 21, RED, weight="700"))
    return W, H, "".join(s)


# ---------------------------------------------------------------- 表 1 排障
def fig_table():
    W = 960
    rows = [
        [["有效和空闲整体对调"], ["两端极性约定不一致"], ["两端的极性设置"]],
        [["执行时刻忽早忽晚"], ["软件定时"], ["改用硬件定时"]],
        [["刺激时长不对"], ["门控方式下脉冲宽度不准"], ["执行方式、定时方式"]],
        [["事件漏记"], ["脉冲窄于读取间隔"], ["脉冲宽度与采样率"]],
        [["一次动作记成多次"], ["触点抖动"], ["去抖"]],
        [["记下不存在的编号"], ["没有选通线或等待不够；", "未接线的输入没有接地"], ["选通、接地"]],
        [["整路没有记录"], ["数字输入未启用"], ["采集软件设置"]],
    ]
    s, bottom = table(W, "按现象倒查", [290, 360, 250], ["现象", "原因", "查哪里"], rows,
                      lh=32, pad=22, first_color=INK, size=22)
    return W, bottom + 20, "".join(s)


FIGS = {
    "cover-concept": cover_concept, "toc": toc, "fig1-levels": fig_levels,
    "fig2-polarity": fig_polarity, "fig3-edge-gated": fig_edge_gated,
    "fig4-timing": fig_timing, "fig5-sampling": fig_sampling, "fig6-bounce": fig_bounce,
    "fig7-strobe": fig_strobe, "fig8-table": fig_table,
}

if __name__ == "__main__":
    names = sys.argv[1:] or list(FIGS)
    for n in names:
        w, h, inner = FIGS[n]()
        print(ioreq1_figs.render(n, w, int(h), inner))
