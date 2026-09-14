# -*- coding: utf-8 -*-
"""2026-09-14 · 电生理采集的信息通路概览（电生理 IO 系列 ep02）—— 自制示意图"""
import os, sys, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from grounding2_figs import (T, box, line, circ, path, BG, ACC, ACCD, TINT, INK, BODY,
                             GRAY, LINE, RED, REDT, GRN, GRNT, CARD_L, PANEL)
import ioreq1_figs

SKILL_DIR = os.path.dirname(os.path.dirname(HERE))
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-09-13-electrophysiology-io",
                   "ep02-2026-09-14-system-paths", "figs")
os.makedirs(OUT, exist_ok=True)
ioreq1_figs.OUT = OUT  # 复用 ep01 的渲染函数，输出改到 ep02


def head(W, s, y=46, size=30):
    return T(W/2, y, s, size, INK, weight="700")


def arrow(x1, y1, x2, y2, c=ACC, m="ah", sw=2.8, dash=None):
    return line(x1, y1, x2, y2, c, sw, dash=dash, marker=m)


def table(W, title, widths, header, rows, top=80, hh=56, lh=34, pad=30, first_color=ACCD,
          x0=None, size=23, head_fill=None):
    """rows: list of list-of-cells; each cell is a list of lines."""
    s = [head(W, title)] if title else []
    x0 = x0 if x0 is not None else (W - sum(widths)) / 2
    total = sum(widths)
    heights = [max(len(c) for c in r) * lh + pad for r in rows]
    Htot = hh + sum(heights)
    s.append(box(x0, top, total, Htot, "#FFFFFF", CARD_L, rx=12, sw=1.8))
    s.append(box(x0, top, total, hh, head_fill or PANEL, CARD_L, rx=12, sw=1.8))
    x = x0
    for w, lab in zip(widths, header):
        s.append(T(x + 18, top + 37, lab, 23, GRAY, anchor="start", weight="700"))
        x += w
    y = top + hh
    for r, h in zip(rows, heights):
        s.append(line(x0, y, x0 + total, y, CARD_L, 1.6))
        x = x0
        for j, (w, cell) in enumerate(zip(widths, r)):
            n = len(cell)
            y0 = y + h/2 - (n-1)*lh/2 + 8
            for k, txt in enumerate(cell):
                bold = txt.startswith("**")
                txt = txt.strip("*")
                col = first_color if j == 0 else (RED if bold else BODY)
                wt = "700" if (j == 0 or bold) else "400"
                s.append(T(x + 18, y0 + k*lh, txt, size if j else size + 2, col, anchor="start", weight=wt))
            x += w
        y += h
    x = x0
    for w in widths[:-1]:
        x += w
        s.append(line(x, top, x, top + Htot, CARD_L, 1.6))
    return s, top + Htot


# ================================================= 封面：判断放在哪一边
def cover_concept():
    W, H = 960, 520
    s = []
    # 采集设备
    s.append(box(60, 70, 330, 250, PANEL, CARD_L, rx=18, sw=2))
    s.append(T(225, 122, "采集设备", 32, INK, weight="700"))
    s.append(box(130, 170, 190, 100, "#FFFFFF", ACC, rx=12, sw=2.6, dash="9 7"))
    s.append(T(225, 215, "判断？", 30, ACCD, weight="700"))
    s.append(T(225, 250, "FPGA / DSP", 20, GRAY, weight="700"))
    # 电脑
    s.append(box(570, 70, 330, 250, PANEL, CARD_L, rx=18, sw=2))
    s.append(T(735, 122, "电脑", 32, INK, weight="700"))
    s.append(box(640, 170, 190, 100, "#FFFFFF", ACC, rx=12, sw=2.6, dash="9 7"))
    s.append(T(735, 215, "判断？", 30, ACCD, weight="700"))
    s.append(T(735, 250, "软件", 20, GRAY, weight="700"))
    # 数据
    s.append(arrow(392, 195, 566, 195, ACC, "ah", 3.4, dash="10 7"))
    s.append(T(480, 180, "数据", 22, ACC, weight="700"))
    # 光源
    s.append(box(360, 400, 240, 80, "#FFFFFF", RED, rx=14, sw=2.6))
    s.append(T(480, 450, "光源驱动", 28, RED, weight="700"))
    s.append(path("M225,322 C225,380 300,440 356,440", RED, 3.2, marker="ahr"))
    s.append(path("M735,322 C735,380 660,440 604,440", RED, 3.2, marker="ahr"))
    return W, H, "".join(s)


# ================================================= 目录
def toc():
    W, H = 960, 470
    s = [T(480, 66, "本期路线", 40, INK, weight="700")]
    s.append(line(120, 96, 840, 96, LINE, 1.8))
    items = [
        ("①", "系统职责", "生成、测量、判断、保存；哪些职责的位置可以选"),
        ("②", "职责分配", "只挪判断的两种方案；改变了哪条连接的用途"),
        ("③", "连接要求", "保存与控制的不同要求；两种实现、实例与差异"),
    ]
    y = 170
    for n, t, d in items:
        s.append(circ(150, y-9, 26, TINT, ACC, 2.4))
        s.append(T(150, y+1, n, 28, ACCD, weight="700"))
        s.append(T(204, y-2, t, 32, INK, anchor="start", weight="700"))
        s.append(T(204, y+36, d, 24, BODY, anchor="start"))
        y += 110
    # 递进箭头
    s.append(line(150, 200, 150, 240, CARD_L, 2.4))
    s.append(line(150, 310, 150, 350, CARD_L, 2.4))
    return W, H, "".join(s)


# ================================================= 卡3 闭环实例
def fig_loop():
    W, H = 960, 430
    s = [head(W, "检测到尖波涟漪，即给一个光脉冲")]
    # 小鼠与记录
    s.append(box(40, 110, 250, 200, PANEL, CARD_L, rx=16, sw=2))
    s.append(T(165, 150, "小鼠背侧 CA1", 25, INK, weight="700"))
    s.append(T(165, 180, "硅探针 + 光纤", 21, GRAY, weight="700"))
    # 涟漪波形
    pts = []
    x0, x1, yc = 70, 260, 250
    for i in range(241):
        t = i/240; x = x0 + (x1-x0)*t
        env = 6 + 30*math.exp(-((t-0.55)/0.12)**2)
        yy = yc - env*math.sin(2*math.pi*26*t)
        pts.append(("M" if i == 0 else "L") + f"{x:.1f},{yy:.1f}")
    s.append(path(" ".join(pts), GRN, 2.2))
    # 检测
    s.append(arrow(296, 210, 378, 210, INK, "ahk", 3))
    s.append(box(384, 150, 220, 120, "#FFFFFF", ACC, rx=14, sw=2.6))
    s.append(T(494, 202, "实时检测", 28, ACCD, weight="700"))
    s.append(T(494, 238, "涟漪", 28, ACCD, weight="700"))
    s.append(T(494, 134, "判断", 22, GRAY, weight="700"))
    # 给光
    s.append(arrow(610, 210, 692, 210, RED, "ahr", 3))
    s.append(box(698, 150, 220, 120, "#FFFFFF", RED, rx=14, sw=2.6))
    s.append(T(808, 202, "给光", 28, RED, weight="700"))
    s.append(T(808, 238, "60 ms 脉冲", 26, RED, weight="700"))
    s.append(T(808, 134, "生成", 22, GRAY, weight="700"))
    # 回到小鼠
    s.append(path("M808,272 L808,370 L165,370 L165,314", RED, 3, marker="ahr"))
    s.append(T(486, 400, "经光纤照射同一脑区", 22, RED, weight="700"))
    return W, H, "".join(s)


# ================================================= 卡4 四项职责
def fig_duties():
    W = 960
    rows = [
        [["生成"], ["数值 → 作用于动物的物理量"], ["设定值变成照到组织上的光"]],
        [["测量"], ["物理量 → 数值"], ["电位、画面、光强变成采样值"]],
        [["判断"], ["数值 → 决定后续生成的数值"], ["检测到涟漪，得出「给光」"]],
        [["保存"], ["数值 → 留存供事后分析"], ["神经数据、视频、判定记录"]],
    ]
    s, bottom = table(W, "按信息的转换方向，分出四项职责", [130, 390, 400],
                      ["职责", "转换方向", "闭环实例"], rows)
    return W, bottom + 20, "".join(s)


# ================================================= 卡6 A/B 两种方案
def fig_ab():
    W = 960
    rows = [
        [["测量"], ["采集设备"], ["采集设备"]],
        [["判断"], ["**采集设备内部完成检测"], ["**电脑上的软件完成检测"]],
        [["生成"], ["光源驱动与光源"], ["光源驱动与光源"]],
        [["保存"], ["电脑"], ["电脑"]],
    ]
    s, bottom = table(W, "其余三项固定，只改变判断的位置", [130, 395, 395],
                      ["职责", "方案 A：判断在采集设备上", "方案 B：判断在电脑上"], rows)
    return W, bottom + 20, "".join(s)


# ================================================= 卡7 信息通路
def fig_paths():
    W, H = 960, 560
    s = []
    s.append(T(240, 42, "方案 A：判断在采集设备上", 26, INK, weight="700"))
    s.append(T(720, 42, "方案 B：判断在电脑上", 26, INK, weight="700"))
    s.append(line(480, 20, 480, 440, LINE, 2))

    def panel(ox, judge_on_acq):
        g = []
        g.append(box(ox+10, 200, 86, 60, "#EEEEEE", GRAY, rx=10, sw=1.8))
        g.append(T(ox+53, 238, "小鼠", 22, INK, weight="700"))
        g.append(box(ox+146, 100, 150, 76, "#FFFFFF", INK, rx=10, sw=2))
        g.append(T(ox+221, 134 if judge_on_acq else 146, "采集设备", 22, INK, weight="700"))
        if judge_on_acq:
            g.append(T(ox+221, 162, "（含判断）", 19, RED, weight="700"))
        g.append(box(ox+146, 320, 150, 70, "#FFFFFF", INK, rx=10, sw=2))
        g.append(T(ox+221, 362, "光源驱动与光源", 20, INK, weight="700"))
        g.append(box(ox+346, 100, 110, 76, "#FFFFFF", INK, rx=10, sw=2))
        g.append(T(ox+401, 134 if not judge_on_acq else 146, "电脑", 22, INK, weight="700"))
        if not judge_on_acq:
            g.append(T(ox+401, 162, "（含判断）", 19, RED, weight="700"))
        g.append(box(ox+346, 320, 110, 70, "#FFFFFF", INK, rx=10, sw=2))
        g.append(T(ox+401, 362, "摄像头", 21, INK, weight="700"))
        # 物理通路
        g.append(line(ox+90, 200, ox+144, 160, GRAY, 2, marker="ahg"))
        g.append(line(ox+146, 350, ox+92, 262, GRAY, 2, marker="ahg"))
        # 视频（保存）
        g.append(line(ox+420, 320, ox+420, 180, ACC, 3, dash="8 6", marker="ah"))
        g.append(T(ox+428, 262, "视频", 19, ACC, anchor="start", weight="700"))
        if judge_on_acq:
            g.append(line(ox+221, 178, ox+221, 316, RED, 3.2, marker="ahr"))
            g.append(T(ox+230, 262, "给光指令", 19, RED, anchor="start", weight="700"))
            g.append(line(ox+298, 138, ox+342, 138, ACC, 3, dash="8 6", marker="ah"))
            g.append(T(ox+320, 88, "神经数据", 17, ACC, weight="700"))
        else:
            g.append(line(ox+298, 138, ox+342, 138, RED, 3.2, marker="ahr"))
            g.append(T(ox+320, 72, "神经数据", 17, RED, weight="700"))
            g.append(T(ox+320, 92, "控制 + 保存", 16, RED, weight="700"))
            g.append(line(ox+362, 178, ox+290, 316, RED, 3.2, marker="ahr"))
            g.append(T(ox+294, 262, "给光指令", 19, RED, anchor="end", weight="700"))
        return g

    s += panel(10, True)
    s += panel(490, False)
    # 图例
    s.append(line(40, 480, 90, 480, RED, 3.2))
    s.append(T(100, 488, "控制：要求及时送达", 21, INK, anchor="start"))
    s.append(line(340, 480, 390, 480, ACC, 3, dash="8 6"))
    s.append(T(400, 488, "保存：要求事后能对齐", 21, INK, anchor="start"))
    s.append(line(660, 480, 710, 480, GRAY, 2))
    s.append(T(720, 488, "物理通路（电极、光纤）", 21, INK, anchor="start"))
    s.append(T(480, 535, "箭头表示信息方向，不代表线缆", 20, GRAY))
    return W, H, "".join(s)


# ================================================= 卡9 步骤与延迟构成
def fig_steps():
    W, H = 960, 600
    s = [head(W, "电脑端多出传输、调度与外接输出几步")]
    bw, gap, x0 = 138, 15, 30
    xs = [x0 + i*(bw+gap) for i in range(6)]
    # 电脑端
    y = 110
    s.append(T(x0, y-14, "判断在电脑上", 24, INK, anchor="start", weight="700"))
    names = ["数字化", "打包传输", "系统调度", "软件检测", "微控制器", "光源驱动"]
    for i, (x, n) in enumerate(zip(xs, names)):
        red = n in ("打包传输", "系统调度", "微控制器")
        s.append(box(x, y, bw, 62, REDT if red else "#FFFFFF", RED if red else ACC, rx=10, sw=2.2))
        s.append(T(x+bw/2, y+40, n, 22, RED if red else ACCD, weight="700"))
        if i < 5:
            s.append(arrow(x+bw+1, y+31, x+bw+gap-2, y+31, GRAY, "ahg", 2))
    # 采集端
    y = 250
    s.append(T(x0, y-14, "判断在采集设备上", 24, INK, anchor="start", weight="700"))
    spans = [(0, 0, "数字化"), (1, 3, "FPGA / DSP 上直接检测"), (4, 5, "自身数字输出口 → 光源驱动")]
    for a, b, n in spans:
        xa, xb = xs[a], xs[b] + bw
        s.append(box(xa, y, xb-xa, 62, "#FFFFFF", ACC, rx=10, sw=2.2))
        s.append(T((xa+xb)/2, y+40, n, 22, ACCD, weight="700"))
    for a in (0, 3):
        xa = xs[a] + bw
        s.append(arrow(xa+1, y+31, xa+gap-2, y+31, GRAY, "ahg", 2))
    s.append(T(x0, 350, "红色为电脑端多出的环节", 20, RED, anchor="start", weight="700"))
    # 总延迟
    y = 440
    s.append(T(x0, y-24, "从事件开始到光亮起的总延迟", 24, INK, anchor="start", weight="700"))
    segs = [(430, "检测延迟", TINT, ACC), (330, "系统延迟", REDT, RED), (140, "光源响应", PANEL, GRAY)]
    x = x0
    for w, n, f, c in segs:
        s.append(box(x, y, w, 64, f, c, rx=8, sw=2.2))
        s.append(T(x+w/2, y+41, n, 23, c if c != GRAY else BODY, weight="700"))
        x += w
    s.append(path(f"M{x0+430},{y+76} L{x0+430},{y+90} L{x0+760},{y+90} L{x0+760},{y+76}", RED, 2.2))
    s.append(T(x0+595, y+122, "判断放在哪里，只改变这一段", 22, RED, weight="700"))
    s.append(T(930, y+122, "长度仅示意", 18, GRAY, anchor="end"))
    return W, H, "".join(s)


# ================================================= 卡12 差异对比
def fig_compare():
    W = 960
    rows = [
        [["系统延迟"], ["可到亚毫秒", "Müller 等：最小 400 μs"], ["取决于传输方式", "Dutta 等：USB 7.5–13.8 ms", "以太网 1.35–2.6 ms"]],
        [["稳定性"], ["按固定时序执行，抖动小", "Müller 等：抖动 < 50 μs"], ["受缓冲与系统调度影响", "Open Ephys 示例：0–27 ms"]],
        [["实现难度"], ["需编写硬件描述语言", "修改算法慢"], ["用常规编程语言", "便于修改和迭代"]],
        [["可运行算法"], ["受芯片资源限制", "常见为阈值比较、滤波"], ["可运行复杂模型", "BRAND：RNN 解码 < 8 ms"]],
    ]
    s, bottom = table(W, "两种实现的差异", [170, 370, 380],
                      ["", "判断在采集设备上", "判断在电脑上"], rows, lh=33, pad=28, size=22)
    s.append(T(W/2, bottom + 38, "数值来自不同系统、样本与配置，只说明数量级差异", 20, GRAY))
    return W, bottom + 60, "".join(s)


# ================================================= 卡14 接口候选
def fig_interfaces():
    W = 960
    rows = [
        [["神经数据"], ["采集设备 → 电脑"], ["连续量，多通道"], ["通信接口（数据包）"]],
        [["行为视频"], ["摄像头 → 电脑"], ["连续量"], ["通信接口"]],
        [["给光指令"], ["→ 光源驱动"], ["离散事件"], ["数字输出 → 数字输入"]],
    ]
    s, bottom = table(W, "先看传的是什么信息，再看用什么形式传", [160, 250, 230, 290],
                      ["信息", "连接", "信息类型", "常见传输形式"], rows)
    return W, bottom + 20, "".join(s)


FIGS = {
    "cover-concept": cover_concept, "toc": toc, "fig1-loop": fig_loop,
    "fig2-duties": fig_duties, "fig3-ab": fig_ab, "fig4-paths": fig_paths,
    "fig5-steps": fig_steps, "fig6-compare": fig_compare, "fig7-interfaces": fig_interfaces,
}

if __name__ == "__main__":
    names = sys.argv[1:] or list(FIGS)
    for n in names:
        w, h, inner = FIGS[n]()
        print(ioreq1_figs.render(n, w, int(h), inner))
