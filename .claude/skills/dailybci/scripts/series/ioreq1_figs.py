# -*- coding: utf-8 -*-
"""2026-09-13 · 电生理采集系统配置的前序准备 —— 自制示意图"""
import os, subprocess, tempfile, sys, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from grounding2_figs import (T, box, line, circ, path, wave, DEFS, FONT,
                             BG, ACC, ACCD, TINT, INK, BODY, GRAY, LINE,
                             RED, REDT, GRN, GRNT, CARD_L, PANEL)

SKILL_DIR = os.path.dirname(os.path.dirname(HERE))
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-09-13-electrophysiology-io", "ep01-2026-09-13-requirements", "figs")
os.makedirs(OUT, exist_ok=True)


def render(name, w, h, inner, scale=2):
    W2, H2 = w*scale, h*scale
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W2}" height="{H2}" '
           f'viewBox="0 0 {w} {h}" font-family="HeitiSC,Helvetica,Arial,sans-serif">'
           f'{DEFS}<rect width="{w}" height="{h}" fill="{BG}"/>{inner}</svg>')
    html = (f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>'
            f'@font-face{{font-family:"HeitiSC";src:url("file://{FONT}");}}'
            f'*{{margin:0;padding:0}}body{{width:{W2}px;height:{H2}px;background:{BG}}}</style></head>'
            f'<body>{svg}</body></html>')
    tmp = tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8")
    tmp.write(html); tmp.close()
    out = os.path.join(OUT, name + ".png")
    subprocess.run(["npx", "playwright", "screenshot", f"file://{tmp.name}", out,
                    f"--viewport-size={W2},{H2}", "--wait-for-timeout=500"],
                   check=True, capture_output=True, text=True)
    os.unlink(tmp.name)
    return out


def head(W, s, y=46, size=30):
    return T(W/2, y, s, size, INK, weight="700")


def arrow(x1, y1, x2, y2, c=ACC, m="ah", sw=2.8):
    return line(x1, y1, x2, y2, c, sw, marker=m)


# ================================================= 封面：先写清单，再接设备
def cover_concept():
    W, H = 960, 540
    s = []
    # 左：需求清单
    s.append(box(70, 50, 390, 440, "#FFFFFF", CARD_L, rx=18, sw=2))
    s.append(T(265, 110, "需求清单", 34, INK, weight="700"))
    s.append(line(110, 134, 420, 134, LINE, 1.8))
    rows = ["输入", "神经活动", "输出", "时间对应"]
    y = 196
    for r in rows:
        s.append(T(110, y+9, r, 27, ACCD, anchor="start", weight="700"))
        for k in range(3):
            s.append(box(262 + k*54, y-19, 38, 38, TINT, ACC, rx=6, sw=2))
        y += 80
    # 箭头
    s.append(arrow(488, 270, 574, 270, ACC, "ah", 4))
    # 右：采集设备
    s.append(box(600, 130, 290, 280, PANEL, CARD_L, rx=18, sw=2))
    s.append(T(745, 186, "采集设备", 32, INK, weight="700"))
    ports = [("AI", 690, 262), ("AO", 800, 262), ("DI", 690, 352), ("DO", 800, 352)]
    for lab, x, yy in ports:
        s.append(circ(x, yy-16, 24, "#FFFFFF", GRAY, 2.4))
        s.append(circ(x, yy-16, 8, GRAY, GRAY, 1))
        s.append(T(x, yy+34, lab, 22, GRAY, weight="700"))
    return W, H, "".join(s)


# ================================================= 目录
def toc():
    W, H = 960, 740
    s = [T(480, 70, "本期路线", 40, INK, weight="700")]
    s.append(line(120, 100, 840, 100, LINE, 1.8))
    items = [
        ("①", "要测什么", "各部分之间的关系，加上时间对应"),
        ("②", "测量偏离", "系统误差、随机误差、失效"),
        ("③", "输入", "先生成再测量；时间、强度、部位"),
        ("④", "神经活动", "距离决定分辨与覆盖；四种测法"),
        ("⑤", "输出", "离散事件与连续量；三个测量位置"),
        ("⑥", "时间对应", "三类对齐偏差；三种同步做法"),
        ("⑦", "需求清单", "搭系统之前先填完的一张表"),
    ]
    y = 156
    for n, t, d in items:
        s.append(circ(150, y-9, 24, TINT, ACC, 2.4))
        s.append(T(150, y+1, n, 26, ACCD, weight="700"))
        s.append(T(200, y-2, t, 30, INK, anchor="start", weight="700"))
        s.append(T(200, y+32, d, 23, BODY, anchor="start"))
        y += 84
    return W, H, "".join(s)


# ================================================= 卡3 三个部分 + 时间
def fig_system():
    W, H = 960, 470
    s = [head(W, "三个部分都随时间变化，靠同一条时间轴对应")]
    x0, x1 = 230, 900
    lanes = [("输入", "刺激", 130), ("神经活动", "电位、钙信号等", 240), ("输出", "运动与生理反应", 350)]
    for name, sub, y in lanes:
        s.append(T(40, y-4, name, 28, INK, anchor="start", weight="700"))
        s.append(T(40, y+28, sub, 20, GRAY, anchor="start"))
        s.append(line(x0, y+34, x1, y+34, LINE, 1.4))
    t_on = 470
    # 输入：一个方波刺激
    y = 130
    s.append(path(f"M{x0},{y+20} L{t_on},{y+20} L{t_on},{y-30} L{t_on+120},{y-30} L{t_on+120},{y+20} L{x1},{y+20}", ACC, 3))
    # 神经活动：刺激后幅度增大的振荡
    y = 240
    pts = []
    for i in range(301):
        t = i/300; x = x0 + (x1-x0)*t
        u = x - (t_on + 20)
        amp = 8 + (26*(1 - math.exp(-u/18))*math.exp(-u/170) if u > 0 else 0)
        yy = y - amp*math.sin(2*math.pi*22*t)
        pts.append(("M" if i == 0 else "L") + f"{x:.1f},{yy:.1f}")
    s.append(path(" ".join(pts), GRN, 2.4))
    # 输出：延迟后的运动
    y = 350
    t_out = t_on + 170
    s.append(path(f"M{x0},{y+20} L{t_out},{y+20} C{t_out+40},{y+20} {t_out+40},{y-28} {t_out+90},{y-28} L{x1},{y-28}", RED, 3))
    # 同一时刻
    s.append(line(t_on, 80, t_on, 400, GRAY, 2, dash="7 6"))
    s.append(line(x0, 420, x1, 420, INK, 2.4, marker="ahk"))
    s.append(T(x1, 452, "时间", 22, INK, anchor="end", weight="700"))
    s.append(T(t_on, 452, "同一时刻", 22, GRAY, weight="700"))
    return W, H, "".join(s)


# ================================================= 卡5 三部分细分表
def table_parts():
    W, H = 960, 590
    s = [head(W, "每个部分先定一条划分标准，再细分")]
    X = [30, 190, 400, 930]
    top, hh, rh = 78, 56, 148
    s.append(box(X[0], top, X[3]-X[0], hh + 3*rh, "#FFFFFF", CARD_L, rx=12, sw=1.8))
    s.append(box(X[0], top, X[3]-X[0], hh, PANEL, CARD_L, rx=12, sw=1.8))
    for x, lab in [(X[0], "部分"), (X[1], "划分标准"), (X[2], "细分")]:
        s.append(T(x+20, top+37, lab, 24, GRAY, anchor="start", weight="700"))
    rows = [
        ("输入", "是否经过感受器",
         ["① 经感受器：环境刺激、本体感觉、内感受", "② 不经感受器：光遗传、电刺激、药物"]),
        ("神经活动", "物理化学性质",
         ["① 电活动：膜电位、动作电位、LFP", "② 化学活动：钙等离子浓度、神经递质", "③ 代谢与血流"]),
        ("输出", "效应器通路",
         ["① 躯体运动：骨骼肌带来的运动、发声、呼吸", "② 自主神经：瞳孔、心率、腺体分泌", "③ 神经内分泌：激素"]),
    ]
    y = top + hh
    for i, (p, std, subs) in enumerate(rows):
        if i:
            s.append(line(X[0], y, X[3], y, CARD_L, 1.6))
        s.append(T(X[0]+20, y+rh/2+10, p, 28, ACCD, anchor="start", weight="700"))
        s.append(T(X[1]+20, y+rh/2+9, std, 24, INK, anchor="start"))
        n = len(subs); gap = 38
        y0 = y + rh/2 - (n-1)*gap/2 + 8
        for k, sub in enumerate(subs):
            s.append(T(X[2]+20, y0 + k*gap, sub, 23, BODY, anchor="start"))
        y += rh
    for x in X[1:3]:
        s.append(line(x, top, x, top+hh+3*rh, CARD_L, 1.6))
    return W, H, "".join(s)


# ================================================= 卡7 输入：生成段与测量段
def fig_input():
    W, H = 960, 400
    s = [head(W, "实验者施加的输入：先生成，再测量")]
    names = ["指令", "驱动", "执行器", "物理刺激"]
    bw, gap, x = 170, 50, 65
    y1, y2 = 140, 210
    xs = []
    for i, n in enumerate(names):
        fill, st = (TINT, ACC) if i < 3 else ("#FFFFFF", ACC)
        s.append(box(x, y1, bw, y2-y1, fill, st, rx=12, sw=2.4))
        s.append(T(x+bw/2, y1+45, n, 27, ACCD, weight="700"))
        xs.append(x)
        if i < 3:
            s.append(arrow(x+bw+4, (y1+y2)/2, x+bw+gap-6, (y1+y2)/2))
        x += bw + gap
    s.append(path(f"M{xs[0]},{y1-16} L{xs[0]},{y1-28} L{xs[3]+bw},{y1-28} L{xs[3]+bw},{y1-16}", ACC, 2.2))
    s.append(T((xs[0]+xs[3]+bw)/2, y1-40, "生成段：实际刺激与设定值相差多少", 23, ACC, weight="700"))
    # 测量段
    cx = xs[3] + bw/2
    y3, y4 = 280, 350
    s.append(line(cx, y2+4, cx, y3-8, GRN, 2.8, marker="ahn"))
    s.append(box(xs[3], y3, bw, y4-y3, GRNT, GRN, rx=12, sw=2.4))
    s.append(T(cx, y3+45, "传感器", 27, GRN, weight="700"))
    s.append(line(xs[3]-4, (y3+y4)/2, xs[2]+bw-40+8, (y3+y4)/2, GRN, 2.8, marker="ahn"))
    s.append(box(xs[1]+40, y3, xs[2]+bw-40-(xs[1]+40), y4-y3, GRNT, GRN, rx=12, sw=2.4))
    s.append(T((xs[1]+40 + xs[2]+bw-40)/2, y3+45, "与神经信号一起记录", 26, GRN, weight="700"))
    s.append(T(xs[0], (y3+y4)/2+9, "测量段", 25, GRN, anchor="start", weight="700"))
    return W, H, "".join(s)


# ================================================= 卡9 神经活动：距离的取舍
def fig_neural():
    W, H = 960, 460
    s = [head(W, "离神经元越远，分辨越粗、覆盖越广")]
    cols = [(360, "胞外微电极"), (590, "皮层脑电 ECoG"), (820, "头皮脑电 EEG")]
    rows = [("信号幅值", [170, 105, 45], ACC), ("来源区分", [170, 105, 45], ACC), ("覆盖范围", [45, 105, 170], GRN)]
    y = 120
    for lab, lens, c in rows:
        s.append(T(40, y+10, lab, 27, INK, anchor="start", weight="700"))
        for (cx, _), L in zip(cols, lens):
            s.append(box(cx-90, y-14, 180, 30, "#FFFFFF", LINE, rx=6, sw=1.4))
            s.append(box(cx-90, y-14, L, 30, TINT if c == ACC else GRNT, c, rx=6, sw=2))
        y += 80
    ya = 380
    s.append(line(240, ya, 920, ya, INK, 2.4, marker="ahk"))
    s.append(T(920, ya+64, "离神经元的距离", 22, INK, anchor="end", weight="700"))
    for cx, name in cols:
        s.append(circ(cx, ya, 7, INK, INK, 1))
        s.append(T(cx, ya-22, name, 23, BODY, weight="700"))
    s.append(T(40, ya+64, "条形长度仅示意趋势", 20, GRAY, anchor="start"))
    return W, H, "".join(s)


# ================================================= 卡12 输出：三个测量位置
def fig_output():
    W, H = 960, 420
    s = [head(W, "输出可以在三个位置测量")]
    items = [
        ("效应器本身", ["肌电图、心电图"], "多为连续量"),
        ("身体的运动", ["视频追踪、加速度计", "瞳孔摄像"], "多为连续量"),
        ("外部装置", ["杠杆开关、舔水传感器", "按键"], "多为离散事件"),
    ]
    bw, gap, x = 260, 60, 40
    for i, (t, ex, kind) in enumerate(items):
        s.append(box(x, 90, bw, 170, "#FFFFFF", ACC, rx=14, sw=2.4))
        s.append(T(x+bw/2, 136, t, 28, ACCD, weight="700"))
        for k, e in enumerate(ex):
            s.append(T(x+bw/2, 184 + k*34, e, 22, BODY))
        kc = GRN if i < 2 else RED
        s.append(T(x+bw/2, 296, kind, 22, kc, weight="700"))
        if i < 2:
            s.append(arrow(x+bw+6, 175, x+bw+gap-8, 175))
        x += bw + gap
    s.append(line(40, 330, 920, 330, LINE, 1.6))
    s.append(T(60, 370, "越能测到动作产生的过程", 22, BODY, anchor="start", weight="700"))
    s.append(T(900, 370, "越只剩动作的结果", 22, BODY, anchor="end", weight="700"))
    s.append(line(60, 396, 900, 396, INK, 2.4, marker="ahk"))
    s.append(path("M900,396 L60,396", INK, 2.4, marker="ahk"))
    return W, H, "".join(s)


# ================================================= 卡13 时间对应的三种偏差
def fig_time():
    W, H = 960, 470
    s = [head(W, "另一台设备记录同一组事件时的三种偏差")]
    xs = [250, 405, 560, 715, 870]
    lanes = [
        ("真实时刻", [0, 0, 0, 0, 0], INK),
        ("固定偏移", [22, 22, 22, 22, 22], RED),
        ("漂移", [4, 13, 22, 31, 40], RED),
        ("随机误差", [16, -12, 22, -6, 10], RED),
    ]
    for x in xs:
        s.append(line(x, 92, x, 410, LINE, 1.6, dash="6 6"))
    y = 120
    for lab, off, c in lanes:
        s.append(T(40, y+9, lab, 26, INK if c == INK else RED, anchor="start", weight="700"))
        s.append(line(210, y+24, 930, y+24, LINE, 1.4))
        for x, d in zip(xs, off):
            s.append(line(x+d, y-18, x+d, y+24, c, 4))
        y += 90
    s.append(T(480, 448, "偏移与漂移可以测出后校正；随机误差只能减小", 22, BODY, weight="700"))
    return W, H, "".join(s)


# ================================================= 卡15 需求清单
def checklist():
    W, H = 960, 470
    s = [head(W, "需求清单")]
    cols = ["部分", "参数", "在哪里测", "允许的偏离", "验收方法", "实现方式"]
    widths = [150, 146, 146, 150, 146, 142]
    x0, top, hh, rh = 40, 82, 60, 78
    total = sum(widths)
    s.append(box(x0, top, total, hh + 4*rh, "#FFFFFF", CARD_L, rx=12, sw=1.8))
    x = x0
    for i, (c, w) in enumerate(zip(cols, widths)):
        fill = REDT if c == "允许的偏离" else PANEL
        s.append(f'<rect x="{x}" y="{top}" width="{w}" height="{hh}" fill="{fill}" stroke="{CARD_L}" stroke-width="1.6"/>')
        s.append(T(x+w/2, top+39, c, 23, RED if c == "允许的偏离" else INK, weight="700"))
        x += w
    rows = ["输入", "神经活动", "输出", "时间对应"]
    y = top + hh
    for r in rows:
        x = x0
        for i, w in enumerate(widths):
            s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{rh}" fill="#FFFFFF" stroke="{CARD_L}" stroke-width="1.6"/>')
            x += w
        s.append(T(x0+widths[0]/2, y+rh/2+9, r, 25, ACCD, weight="700"))
        y += rh
    return W, H, "".join(s)


FIGS = {
    "cover-concept": cover_concept, "toc": toc, "fig1-system": fig_system,
    "fig2-parts-table": table_parts, "fig3-input-two-stages": fig_input,
    "fig4-neural-distance": fig_neural, "fig5-output-positions": fig_output,
    "fig6-time-deviations": fig_time, "fig7-checklist": checklist,
}

if __name__ == "__main__":
    names = sys.argv[1:] or list(FIGS)
    for n in names:
        w, h, inner = FIGS[n]()
        print(render(n, w, h, inner))
