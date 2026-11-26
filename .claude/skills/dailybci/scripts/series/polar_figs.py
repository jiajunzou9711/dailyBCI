# -*- coding: utf-8 -*-
"""2026-11-25 原理期 · 电极材料怎样影响记录到的电位 —— 自制示意图

依据：Merrill 2005（定义、Ag/AgCl、纯银）；Tallgren 2005（恒流极化、导电膏、慢信号）；
Dymond 1970 / Babb 1984 / Locht 2011（银毒性）；Quian Quiroga 2007、Jun 2017、Intan RHD2000（频段与芯片）。
曲线均为示意，不是原始数据。
"""
import os, sys, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ising1_figs as I1
from grounding2_figs import (T, box, line, circ, path, BG, ACC, ACCD, TINT, INK,
                             BODY, GRAY, LINE, RED, REDT, PANEL)

I1.OUT = os.path.join(I1.PROJECT, "output", "series-electrode-polarization-drift", "figs")
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


def vsrc(cx, cy, r=30, col=RED, label="E"):
    """电位源：圆 + 正负号。"""
    return (circ(cx, cy, r, "#FFFFFF", col, 2.6) + T(cx, cy - 6, "+", 22, col, weight="700")
            + T(cx, cy + 20, "−", 22, col, weight="700") + T(cx - r - 14, cy + 9, label, 26, col, anchor="end", weight="700"))


def resistor_h(x, y, w=90, h=30, col=INK):
    return box(x, y - h / 2, w, h, "#FFFFFF", col, rx=4, sw=2.4)


def cap_h(x, y, gap=16, hh=34, col=INK):
    return line(x, y - hh / 2, x, y + hh / 2, col, 3.2) + line(x + gap, y - hh / 2, x + gap, y + hh / 2, col, 3.2)


# ================================================= 封面概念图
def cover():
    W, H = 960, 420
    s = []
    # 左：组织；右：放大器；中间：电极界面（电位源 + 阻抗）
    s.append(box(40, 90, 200, 240, REDT, RED, rx=16, sw=2))
    s.append(T(140, 205, "组织", 34, RED, weight="700"))
    s.append(T(140, 248, "生物相容性", 22, RED))
    s.append(box(720, 90, 200, 240, TINT, ACC, rx=16, sw=2))
    s.append(T(820, 205, "放大器", 34, ACCD, weight="700"))
    s.append(T(820, 248, "记录到的电位", 22, ACCD))
    y = 210
    s.append(line(240, y, 330, y, INK, 3))
    s.append(vsrc(380, y, 34, RED, ""))
    s.append(T(380, y + 76, "界面电位 E", 24, RED, weight="700"))
    s.append(line(414, y, 500, y, INK, 3))
    s.append(resistor_h(500, y, 110, 34, GRAY))
    s.append(T(555, y + 76, "阻抗 Z", 24, GRAY, weight="700"))
    s.append(line(610, y, 720, y, INK, 3))
    s.append(box(300, 120, 360, 190, "none", LINE, rx=18, sw=2, dash="8 6"))
    s.append(T(480, 108, "电极材料", 26, INK, weight="700"))
    return W, H, "".join(s)


# ================================================= 目录
def toc():
    items = ["电极材料要同时满足组织和信号两方面的要求",
             "电极界面上存在电位，它的缓慢变化就是漂移",
             "电流穿过界面只有两种方式",
             "两类电极：可极化与不可极化",
             "可极化电极更容易漂移",
             "Ag/AgCl 接近不可极化，铂和不锈钢偏可极化",
             "银对脑组织有毒",
             "头皮 EEG 与植入电极各自怎么选材",
             "植入电极的漂移用高通滤波去掉",
             "高通滤波生效的两个前提"]
    W, H = 960, 120 + 62 * len(items)
    s = [T(480, 62, "本期目录", 40, INK, weight="700"), line(100, 92, 860, 92, LINE, 1.8)]
    y = 146
    nums = "①②③④⑤⑥⑦⑧⑨⑩"
    for i, t in enumerate(items):
        s += [circ(132, y - 9, 22, TINT, ACC, 2.2), T(132, y + 0, nums[i], 24, ACCD, weight="700"),
              T(176, y, t, 28, INK, anchor="start")]
        y += 62
    return W, H, "".join(s)


# ================================================= 卡 1 等效电路
def f1():
    W, H = 960, 330
    s = [head(W, "电极–组织液界面 = 电位源 E 串联阻抗 Z", y=44)]
    y = 190
    s.append(chip(40, y - 40, 170, 80, "组织液", "gray", 28))
    s.append(line(210, y, 330, y, INK, 3))
    s.append(vsrc(380, y, 36, RED, ""))
    s.append(line(416, y, 520, y, INK, 3))
    s.append(resistor_h(520, y, 120, 36, GRAY))
    s.append(line(640, y, 750, y, INK, 3))
    s.append(chip(750, y - 40, 170, 80, "放大器", "acc", 28))
    s.append(T(380, y + 76, "E：偏置、漂移", 24, RED, weight="700"))
    s.append(T(580, y + 76, "Z：噪声、衰减", 24, GRAY))
    s.append(T(580, y - 34, "Z", 24, GRAY, weight="700"))
    s.append(T(380, y - 58, "本期", 22, RED))
    return W, H, "".join(s)


# ================================================= 卡 2 两个电极
def f2():
    W, H = 960, 400
    s = [head(W, "读数里叠加了两个电极的电位之差", y=44)]
    # 记录电极上，参考电极下，进入差分放大器
    for yy, lab, nm in [(150, "记录电极", "E₁"), (290, "参考电极", "E₂")]:
        s.append(T(90, yy + 9, lab, 26, INK, anchor="middle", weight="700"))
        s.append(line(170, yy, 300, yy, INK, 3))
        s.append(vsrc(350, yy, 32, RED, ""))
        s.append(T(350, yy - 44, nm, 24, RED, weight="700"))
        s.append(line(382, yy, 600, yy, INK, 3))
    s.append(path("M600,110 L600,330 L780,220 Z", ACC, 3, fill=TINT))
    s.append(T(640, 160, "+", 30, ACCD, weight="700"))
    s.append(T(640, 300, "−", 30, ACCD, weight="700"))
    s.append(line(780, 220, 860, 220, INK, 3))
    s.append(T(870, 212, "读数", 24, INK, anchor="start", weight="700"))
    s.append(T(870, 246, "含 E₁ − E₂", 22, RED, anchor="start"))
    s.append(T(480, 384, "E₁ − E₂ 恒定 → 直流偏置；随时间缓慢变化 → 漂移", 23, GRAY))
    return W, H, "".join(s)


# ================================================= 卡 3 两种过程
def f3():
    W, H = 960, 420
    s = [head(W, "电荷穿过界面的两种方式", y=44)]
    for k, (x0, ttl, kind) in enumerate([(40, "法拉第过程", "f"), (500, "电容性过程", "c")]):
        s.append(T(x0 + 210, 98, ttl, 28, ACCD if kind == "f" else INK, weight="700"))
        s.append(box(x0, 120, 170, 230, "#E6E6E6", GRAY, rx=6, sw=2))
        s.append(T(x0 + 85, 240, "金属", 26, INK, weight="700"))
        s.append(box(x0 + 250, 120, 170, 230, TINT, ACC, rx=6, sw=2))
        s.append(T(x0 + 335, 240, "溶液", 26, ACCD, weight="700"))
        s.append(line(x0 + 210, 120, x0 + 210, 350, INK, 2, dash="6 5"))
        if kind == "f":
            s.append(arrow(x0 + 290, 190, x0 + 130, 190, RED, 3))
            s.append(T(x0 + 210, 178, "e⁻", 24, RED, weight="700"))
            s.append(T(x0 + 210, 390, "Ag + Cl⁻ ⇌ AgCl + e⁻", 24, INK))
        else:
            for j in range(5):
                yy = 150 + j * 42
                s.append(T(x0 + 190, yy + 8, "−", 26, RED, weight="700"))
                s.append(T(x0 + 232, yy + 8, "+", 26, ACC, weight="700"))
            s.append(T(x0 + 210, 390, "电荷停在两侧：双电层充放电", 24, INK))
    return W, H, "".join(s)


# ================================================= 卡 4 两种理想电极
def f4():
    W, H = 960, 450
    s = [head(W, "法拉第过程是否畅通，决定电极属于哪一类", y=44)]
    rows = [("", "理想可极化", "理想不可极化"),
            ("电荷怎样穿过界面", "只有电容性过程", "法拉第过程畅通"),
            ("有电流时界面电位", "偏离平衡值", "保持在平衡值"),
            ("电学上表现为", "一个电容", "电位源 + 很小的电阻")]
    xs = [40, 330, 650]; ws = [290, 320, 270]
    y = 84
    for i, r in enumerate(rows):
        h = 70 if i == 0 else 92
        for j, c in enumerate(r):
            fill = (REDT if j == 1 else TINT if j == 2 else PANEL) if i == 0 else "#FFFFFF"
            st = LINE
            s.append(box(xs[j], y, ws[j], h, fill, st, rx=0, sw=1.6))
            col = RED if (j == 1 and i == 0) else ACCD if (j == 2 and i == 0) else (BODY if j == 0 else INK)
            s.append(T(xs[j] + ws[j] / 2, y + h / 2 + 9, c, 25, col, weight="700" if i == 0 or j == 0 else "400"))
        y += h
    return W, H, "".join(s)


# ================================================= 卡 5 恒流下电位–时间
def f5():
    W, H = 960, 420
    s = [head(W, "恒定小电流下：铂/不锈钢电位持续上升，Ag/AgCl 几乎不变", y=44, size=26)]
    x0, y0, x1, y1 = 110, 350, 900, 100
    s.append(line(x0, y0, x1, y0, INK, 2.4)); s.append(line(x0, y0, x0, y1 - 10, INK, 2.4))
    s.append(T(x1, y0 + 36, "时间", 22, GRAY, anchor="end"))
    s.append(T(x0 - 14, y1 + 4, "界面电位", 22, GRAY, anchor="end"))
    sat = y1 + 20
    s.append(line(x0, sat, x1, sat, RED, 2, dash="8 6"))
    s.append(T(x1, sat - 10, "放大器量程上限", 21, RED, anchor="end"))
    s.append(path(f"M{x0},{y0 - 10} L{x0 + 300},{sat} L{x1},{sat}", RED, 3.4))
    s.append(T(x0 + 70, y0 - 150, "铂 / 不锈钢", 24, RED, anchor="start", weight="700"))
    s.append(path(f"M{x0},{y0 - 10} C{x0 + 200},{y0 - 16} {x0 + 500},{y0 - 14} {x1},{y0 - 18}", ACC, 3.4))
    s.append(T(x1 - 10, y0 - 34, "Ag/AgCl", 24, ACCD, anchor="end", weight="700"))
    s.append(T(480, 408, "示意，按 Tallgren 2005 的文字描述重画（±5 nA 恒流，生理盐水）", 20, GRAY))
    return W, H, "".join(s)


# ================================================= 卡 6 材料位置轴
def f6():
    W, H = 960, 330
    s = [head(W, "实际电极处在两种理想之间", y=44)]
    y = 190
    s.append(line(90, y, 870, y, INK, 3))
    s.append(T(90, y + 46, "理想可极化", 24, RED, anchor="start", weight="700"))
    s.append(T(870, y + 46, "理想不可极化", 24, ACCD, anchor="end", weight="700"))
    for x, lab, col in [(130, "纯银", GRAY), (240, "铂", RED), (350, "不锈钢", RED), (800, "Ag/AgCl", ACC)]:
        s.append(circ(x, y, 12, "#FFFFFF", col, 3))
        s.append(T(x, y - 30, lab, 26, col, weight="700"))
    s.append(T(130, y - 66, "（无 AgCl 层）", 20, GRAY))
    s.append(T(480, 312, "铂表面有可逆的氢吸附，所以铂也不是理想可极化", 22, GRAY))
    return W, H, "".join(s)


# ================================================= 卡 7 物种表
def f7():
    W, H = 960, 370
    s = [head(W, "三种动物脑内实验：银都引起组织损伤", y=44)]
    rows = [("动物", "时长", "结果"),
            ("猫", "2 个月", "13 种金属中只有银有毒"),
            ("大鼠", "11–63 天", "银有毒，不锈钢无毒"),
            ("小鼠", "7 天–9 个月", "银颗粒致组织空洞与炎症")]
    xs = [60, 220, 420]; ws = [160, 200, 480]
    y = 80
    for i, r in enumerate(rows):
        h = 56
        for j, c in enumerate(r):
            fill = PANEL if i == 0 else (REDT if j == 2 else "#FFFFFF")
            s.append(box(xs[j], y, ws[j], h, fill, LINE, rx=0, sw=1.6))
            s.append(T(xs[j] + ws[j] / 2, y + 37, c, 25, (BODY if i == 0 else RED if j == 2 else INK),
                       weight="700" if i == 0 else "400"))
        y += 56
    s.append(T(480, 352, "均为纯银植入或注入；Ag/AgCl 的毒性为转引（Dymond 1970 表 1）", 21, GRAY))
    return W, H, "".join(s)


# ================================================= 卡 8 两栏
def f8():
    W, H = 960, 330
    s = [head(W, "限制条件不同，选材不同", y=44)]
    for x0, ttl, mat, lim, kind in [(40, "头皮 EEG", "Ag/AgCl + 含氯导电膏", "不进入脑组织：毒性不构成限制", "acc"),
                                    (500, "植入电极", "铂、铂铱、钨等", "毒性一票否决：只能用无毒金属", "red")]:
        col = ACCD if kind == "acc" else RED
        fill = TINT if kind == "acc" else REDT
        s.append(box(x0, 80, 420, 220, fill, ACC if kind == "acc" else RED, rx=16, sw=2))
        s.append(T(x0 + 210, 130, ttl, 32, col, weight="700"))
        s.append(T(x0 + 210, 200, mat, 27, INK, weight="700"))
        s.append(T(x0 + 210, 260, lim, 22, BODY))
    return W, H, "".join(s)


# ================================================= 卡 9 频率轴
def f9():
    W, H = 960, 330
    s = [head(W, "漂移贴近 0 Hz，神经信号在它之上", y=44)]
    x0, x1, y = 80, 900, 230
    # log axis 0.01 Hz .. 10 kHz
    def X(f): return x0 + (math.log10(f) + 2) / 6 * (x1 - x0)
    s.append(line(x0, y, x1, y, INK, 2.6))
    for f, lab in [(0.01, "0.01"), (0.1, "0.1"), (1, "1"), (10, "10"), (100, "100"), (1000, "1k"), (10000, "10k Hz")]:
        s.append(line(X(f), y, X(f), y + 10, INK, 2)); s.append(T(X(f), y + 36, lab, 20, GRAY))
    s.append(box(x0, y - 50, X(0.05) - x0, 40, REDT, RED, rx=6, sw=2))
    s.append(T(x0 + 6, y - 62, "漂移", 22, RED, anchor="start", weight="700"))
    s.append(box(X(0.5), y - 100, X(1000) - X(0.5), 40, TINT, ACC, rx=6, sw=2))
    s.append(T((X(0.5) + X(1000)) / 2, y - 72, "LFP 0.5–1000 Hz", 22, ACCD, weight="700"))
    s.append(box(X(300), y - 50, X(3000) - X(300), 40, TINT, ACC, rx=6, sw=2))
    s.append(T(X(300) - 10, y - 22, "动作电位 300–3000 Hz", 21, ACCD, anchor="end", weight="700"))
    s.append(line(X(0.1), 80, X(0.1), y, INK, 2.4, dash="7 5"))
    s.append(T(X(0.1) + 8, 96, "高通截止（例：0.1 Hz）", 21, INK, anchor="start"))
    return W, H, "".join(s)


# ================================================= 卡 10 两个前提
def f10():
    W, H = 960, 360
    s = [head(W, "两种情况下，高通滤波救不回来", y=44)]
    # 左：削顶
    x0, y0 = 50, 300
    s.append(T(240, 92, "① 超出放大器范围：削顶", 24, RED, weight="700"))
    top = 140
    s.append(line(x0, top, 440, top, RED, 2, dash="7 5"))
    pts = []
    for i in range(0, 391, 4):
        x = x0 + i
        base = y0 - 30 - i * 0.42
        v = base - 30 * math.sin(i / 9)
        v = max(v, top)
        pts.append(f"{x:.1f},{v:.1f}")
    s.append(path("M" + " L".join(pts), ACC, 2.8))
    s.append(T(240, 340, "顶端被截平，信息丢失", 21, GRAY))
    # 右：频段重叠
    s.append(T(720, 92, "② 慢信号与漂移同频段", 24, RED, weight="700"))
    s.append(line(520, 250, 920, 250, INK, 2.4))
    s.append(box(520, 200, 140, 40, REDT, RED, rx=6, sw=2)); s.append(T(590, 228, "漂移", 21, RED, weight="700"))
    s.append(box(560, 150, 170, 40, "#FFF4E5", "#D9822B", rx=6, sw=2)); s.append(T(645, 178, "超慢振荡等", 21, "#B5651D", weight="700"))
    s.append(line(760, 120, 760, 250, INK, 2.4, dash="7 5")); s.append(T(768, 136, "高通截止", 20, INK, anchor="start"))
    s.append(T(720, 300, "截止频率以下一并去掉", 21, GRAY))
    return W, H, "".join(s)


if __name__ == "__main__":
    for name, fn in [("cover", cover), ("toc", toc), ("f1", f1), ("f2", f2), ("f3", f3), ("f4", f4),
                     ("f5", f5), ("f6", f6), ("f7", f7), ("f8", f8), ("f9", f9), ("f10", f10)]:
        if len(sys.argv) > 1 and name not in sys.argv[1:]:
            continue
        W, H, inner = fn()
        render(name, W, H, inner)
        print("ok", name)
