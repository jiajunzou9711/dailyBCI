# -*- coding: utf-8 -*-
"""2026-09-15 · 电生理设备之间的电气连接（电生理 IO 系列 ep03）—— 自制示意图"""
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
                   "ep03-2026-09-15-electrical-connection", "figs")
os.makedirs(OUT, exist_ok=True)
ioreq1_figs.OUT = OUT


def head(W, s, y=46, size=30):
    return T(W/2, y, s, size, INK, weight="700")


def dev(x, y, w, h, name, sub=None):
    s = [box(x, y, w, h, PANEL, CARD_L, rx=16, sw=2), T(x+w/2, y+42, name, 28, INK, weight="700")]
    if sub:
        s.append(T(x+w/2, y+74, sub, 20, GRAY, weight="700"))
    return s


# ---------------------------------------------------------------- 封面
def cover_concept():
    W, H = 960, 480
    s = []
    s += dev(70, 80, 260, 220, "设备 A")
    s += dev(630, 80, 260, 220, "设备 B")
    s.append(line(330, 160, 630, 160, ACC, 4))
    s.append(T(480, 142, "信号线", 24, ACC, weight="700"))
    s.append(line(330, 240, 630, 240, INK, 4))
    s.append(T(480, 226, "参考线", 24, INK, weight="700"))
    s.append(path("M200,302 L200,420 L760,420 L760,302", RED, 3, dash="10 8"))
    s.append(T(480, 406, "还有一条经保护地的通路？", 24, RED, weight="700"))
    return W, H, "".join(s)


# ---------------------------------------------------------------- 目录
def toc():
    W, H = 960, 560
    s = [T(480, 66, "本期路线", 40, INK, weight="700"), line(120, 96, 840, 96, LINE, 1.8)]
    items = [
        ("①", "一条连接由什么组成", "信号线与参考线"),
        ("②", "两端能否直连", "电压范围、驱动能力、阻抗"),
        ("③", "多台设备之间的地环路", "怎样形成、怎样干扰读数、隔离及其边界"),
        ("④", "怎样证明连接成立", "接线前查说明书，接好后实测"),
    ]
    y = 160
    for i, (n, t, d) in enumerate(items):
        s.append(circ(150, y-9, 26, TINT, ACC, 2.4))
        s.append(T(150, y+1, n, 28, ACCD, weight="700"))
        s.append(T(204, y-2, t, 32, INK, anchor="start", weight="700"))
        s.append(T(204, y+36, d, 24, BODY, anchor="start"))
        if i < 3:
            s.append(line(150, y+22, 150, y+70, CARD_L, 2.4))
        y += 110
    return W, H, "".join(s)


# ---------------------------------------------------------------- 卡3 两根导体
def fig_two_wires():
    W, H = 960, 400
    s = [head(W, "信号线把电流送出，参考线让它流回")]
    s += dev(40, 80, 260, 270, "设备 A")
    s += dev(660, 80, 260, 270, "设备 B")
    for x, a in ((300, "end"), (660, "start")):
        s.append(circ(x, 170, 10, "#FFFFFF", INK, 2.4))
        s.append(circ(x, 300, 10, "#FFFFFF", INK, 2.4))
    s.append(T(284, 176, "输出引脚", 20, BODY, anchor="end", weight="700"))
    s.append(T(284, 306, "地引脚", 20, BODY, anchor="end", weight="700"))
    s.append(T(676, 176, "输入引脚", 20, BODY, anchor="start", weight="700"))
    s.append(T(676, 306, "地引脚", 20, BODY, anchor="start", weight="700"))
    s.append(line(310, 170, 650, 170, ACC, 4))
    s.append(T(480, 152, "信号线", 24, ACC, weight="700"))
    s.append(line(310, 300, 650, 300, INK, 4))
    s.append(T(480, 336, "参考线", 24, INK, weight="700"))
    s.append(line(420, 196, 540, 196, RED, 2.6, marker="ahr"))
    s.append(line(540, 274, 420, 274, RED, 2.6, marker="ahr"))
    s.append(T(480, 240, "电流回路", 22, RED, weight="700"))
    s.append(line(860, 186, 860, 284, GRAY, 2.2, dash="6 5"))
    s.append(T(790, 240, "比较两线", 20, GRAY, anchor="middle", weight="700"))
    s.append(T(790, 264, "之间的电压", 20, GRAY, anchor="middle", weight="700"))
    return W, H, "".join(s)


# ---------------------------------------------------------------- 卡6 分压
def fig_divider():
    W, H = 960, 470
    s = [head(W, "两个阻抗串联，接收端只分到其中一部分")]
    s.append(box(50, 70, 400, 320, "none", GRAY, rx=14, sw=1.8, dash="8 6"))
    s.append(box(480, 70, 430, 320, "none", GRAY, rx=14, sw=1.8, dash="8 6"))
    s.append(T(250, 374, "发送端", 22, GRAY, weight="700"))
    s.append(T(695, 374, "接收端", 22, GRAY, weight="700"))
    # 电源
    s.append(circ(130, 230, 44, "#FFFFFF", ACC, 2.8))
    s.append(T(130, 224, "设定", 20, ACCD, weight="700"))
    s.append(T(130, 250, "电压", 20, ACCD, weight="700"))
    s.append(path("M130,186 L130,120 L240,120", INK, 3))
    s.append(box(240, 96, 160, 48, REDT, RED, rx=8, sw=2.4))
    s.append(T(320, 128, "输出阻抗", 22, RED, weight="700"))
    s.append(path("M400,120 L600,120 L600,160", INK, 3))
    s.append(box(570, 160, 60, 150, TINT, ACC, rx=8, sw=2.4))
    s.append(T(646, 242, "输入阻抗", 22, ACCD, anchor="start", weight="700"))
    s.append(path("M600,310 L600,346 L130,346 L130,274", INK, 3))
    s.append(line(820, 235, 820, 168, GRN, 2.6, marker="ahn"))
    s.append(line(820, 235, 820, 302, GRN, 2.6, marker="ahn"))
    s.append(T(846, 230, "接收端", 20, GRN, anchor="start", weight="700"))
    s.append(T(846, 256, "电压", 20, GRN, anchor="start", weight="700"))
    s.append(T(480, 438, "接收端电压 = 设定电压 × 输入阻抗 ÷（输出阻抗 + 输入阻抗）", 24, INK, weight="700"))
    return W, H, "".join(s)


# ---------------------------------------------------------------- 卡8 引脚与电路地
def fig_pins():
    W, H = 960, 380
    s = [head(W, "信号线连引脚，参考线连两台设备的电路地")]
    for x0, name, pin in ((40, "设备 A", "输出引脚"), (620, "设备 B", "输入引脚")):
        s.append(box(x0, 76, 300, 260, PANEL, CARD_L, rx=16, sw=2))
        s.append(T(x0+150, 110, name, 26, INK, weight="700"))
        s.append(box(x0+80, 130, 140, 70, "#FFFFFF", GRAY, rx=10, sw=2))
        s.append(T(x0+150, 172, "内部电路", 20, BODY, weight="700"))
        s.append(line(x0+30, 290, x0+270, 290, GRN, 5))
        s.append(T(x0+150, 322, "电路地（零点）", 20, GRN, weight="700"))
        s.append(line(x0+150, 200, x0+150, 290, GRAY, 2))
    s.append(path("M260,165 L340,165", GRAY, 2))
    s.append(path("M620,165 L700,165", GRAY, 2))
    for x in (340, 620):
        s.append(circ(x, 165, 10, "#FFFFFF", INK, 2.4))
        s.append(circ(x, 290, 10, "#FFFFFF", INK, 2.4))
    s.append(line(350, 165, 610, 165, ACC, 4))
    s.append(T(480, 150, "信号线", 24, ACC, weight="700"))
    s.append(line(350, 290, 610, 290, INK, 4))
    s.append(T(480, 276, "参考线", 24, INK, weight="700"))
    s.append(T(480, 322, "把两个电路地连在一起", 20, BODY, weight="700"))
    return W, H, "".join(s)


def _pe_scene(with_ref):
    s = []
    s += dev(80, 70, 240, 120, "设备 A", "电路地接保护地")
    s += dev(640, 70, 240, 120, "设备 B", "电路地接保护地")
    c = RED if with_ref else GRN
    for x in (200, 760):
        s.append(line(x, 190, x, 290, c, 4))
        s.append(box(x-45, 290, 90, 56, "#FFFFFF", GRAY, rx=8, sw=2))
        s.append(T(x, 326, "插座", 20, BODY, weight="700"))
        s.append(line(x, 346, x, 400, c, 4))
    s.append(line(200, 400, 760, 400, c, 4))
    s.append(T(480, 386, "墙里的地线", 22, c, weight="700"))
    s.append(T(212, 246, "电源线地线", 18, c, anchor="start", weight="700"))
    s.append(T(748, 246, "电源线地线", 18, c, anchor="end", weight="700"))
    return s


# ---------------------------------------------------------------- 卡9 保护地已连通
def fig_pe():
    W, H = 960, 440
    s = [head(W, "不接任何线，两台设备的电路地也可能已经连通")]
    s += _pe_scene(False)
    s.append(T(480, 136, "两台设备之间未接线", 22, GRAY, weight="700"))
    return W, H, "".join(s)


# ---------------------------------------------------------------- 卡10 地环路
def fig_loop():
    W, H = 960, 440
    s = [head(W, "参考线与保护地通路首尾相接，构成地环路")]
    s += _pe_scene(True)
    s.append(line(320, 130, 640, 130, RED, 4))
    s.append(T(480, 116, "参考线", 22, RED, weight="700"))
    s.append(T(480, 262, "地环路", 34, RED, weight="700"))
    return W, H, "".join(s)


# ---------------------------------------------------------------- 卡13 隔离
def fig_iso():
    W, H = 960, 400
    s = [head(W, "隔离器件两侧没有导线相连，只有光穿过")]
    s.append(box(50, 80, 330, 250, PANEL, CARD_L, rx=16, sw=2))
    s.append(T(215, 116, "A 侧", 26, INK, weight="700"))
    s.append(T(215, 144, "以 A 的地为参考", 20, GRAY, weight="700"))
    s.append(box(130, 180, 170, 70, "#FFFFFF", ACC, rx=10, sw=2.4))
    s.append(T(215, 222, "发光二极管", 22, ACCD, weight="700"))
    s.append(box(580, 80, 330, 250, PANEL, CARD_L, rx=16, sw=2))
    s.append(T(745, 116, "B 侧", 26, INK, weight="700"))
    s.append(T(745, 144, "以 B 的地为参考", 20, GRAY, weight="700"))
    s.append(box(660, 180, 170, 70, "#FFFFFF", ACC, rx=10, sw=2.4))
    s.append(T(745, 222, "光敏器件", 22, ACCD, weight="700"))
    s.append(T(745, 300, "由 B 侧供电", 20, GRN, weight="700"))
    s.append(line(306, 215, 652, 215, ACC, 3, dash="12 8", marker="ah"))
    s.append(T(420, 200, "光", 22, ACC, weight="700"))
    s.append(line(480, 70, 480, 340, RED, 3, dash="6 6"))
    s.append(T(480, 372, "此处无导体相连，地环路无法闭合", 22, RED, weight="700"))
    return W, H, "".join(s)


# ---------------------------------------------------------------- 卡15 核对表
def fig_check():
    W = 960
    rows = [
        [["接线之前"], ["查两端", "说明书"], ["电压：高低电平在判定阈值内、低于绝对最大值",
                                        "电流与阻抗：输入阻抗远大于输出阻抗",
                                        "地：两台设备的电路地是否都接保护地"]],
        [["接好之后"], ["在接收端", "实测"], ["示波器测输入引脚相对自身地的电压",
                                         "电平是否在阈值内，有无 50 Hz 波动"]],
    ]
    s, bottom = table(W, "两步证明一条连接成立", [150, 150, 620],
                      ["步骤", "做什么", "看什么"], rows, lh=38, pad=34)
    return W, bottom + 20, "".join(s)


FIGS = {
    "cover-concept": cover_concept, "toc": toc, "fig1-two-wires": fig_two_wires,
    "fig2-divider": fig_divider, "fig3-pins": fig_pins, "fig4-pe": fig_pe,
    "fig5-loop": fig_loop, "fig6-iso": fig_iso, "fig7-check": fig_check,
}

if __name__ == "__main__":
    names = sys.argv[1:] or list(FIGS)
    for n in names:
        w, h, inner = FIGS[n]()
        print(ioreq1_figs.render(n, w, int(h), inner))
