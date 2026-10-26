# -*- coding: utf-8 -*-
"""series-ising-01 · Ising 模型是什么 —— 自制示意图"""
import os, subprocess, tempfile, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from grounding2_figs import (T, box, line, circ, path, DEFS, FONT,
                             BG, ACC, ACCD, TINT, INK, BODY, GRAY, LINE,
                             RED, REDT, GRN, GRNT, CARD_L, PANEL)

SKILL_DIR = os.path.dirname(os.path.dirname(HERE))
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "series-ising-01", "ep01", "figs")
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
    subprocess.run(["npx","playwright","screenshot",f"file://{tmp.name}",out,
                    f"--viewport-size={W2},{H2}","--wait-for-timeout=500"],
                   check=True, capture_output=True, text=True)
    os.unlink(tmp.name)
    return out

def head(W, s, y=46, size=30):
    return T(W/2, y, s, size, INK, weight="700")

def spin(cx, cy, up, r=22):
    """一个格点：圆 + 箭头。+1 用蓝色向上，−1 用灰色向下。"""
    col = ACC if up else GRAY
    fill = TINT if up else "#EEEEEE"
    s = [circ(cx, cy, r, fill, col, 2.2)]
    if up:
        s.append(path(f"M{cx},{cy+13} L{cx},{cy-13}", col, 3.2))
        s.append(path(f"M{cx-7},{cy-5} L{cx},{cy-14} L{cx+7},{cy-5}", col, 3.2))
    else:
        s.append(path(f"M{cx},{cy-13} L{cx},{cy+13}", col, 3.2))
        s.append(path(f"M{cx-7},{cy+5} L{cx},{cy+14} L{cx+7},{cy+5}", col, 3.2))
    return "".join(s)

# ================================================= 目录
def toc():
    W, H = 960, 560
    s = [T(480, 70, "本期路线", 40, INK, weight="700")]
    s.append(line(120, 100, 840, 100, LINE, 1.8))
    items = [
        ("①", "Ising 模型的三条前提", "状态、能量、概率"),
        ("②", "它回答的问题", "只靠局部相互作用，能否产生相变"),
        ("③", "正问题与逆问题", "由参数求行为，或由数据求参数"),
        ("④", "两条线", "一条由人设定 J，一条从数据估计 J"),
    ]
    y = 166
    for n, t, d in items:
        s.append(circ(150, y-9, 25, TINT, ACC, 2.4))
        s.append(T(150, y+1, n, 27, ACCD, weight="700"))
        s.append(T(200, y-4, t, 31, INK, anchor="start", weight="700"))
        s.append(T(200, y+34, d, 24, BODY, anchor="start"))
        y += 100
    return W, H, "".join(s)

# ================================================= 图 0-1 二维方格
def fig01_lattice():
    W, H = 960, 420
    s = [head(W, "每个格点取 +1 或 −1，只与相邻格点相互作用")]
    grid = [[1, 1, -1, 1, 1],
            [1, 1, 1, -1, 1],
            [-1, 1, 1, 1, 1],
            [1, -1, 1, 1, -1]]
    x0, y0, d = 120, 108, 76
    rows, cols = len(grid), len(grid[0])
    # 相邻连线
    for i in range(rows):
        for j in range(cols):
            cx, cy = x0 + j*d, y0 + i*d
            if j < cols-1: s.append(line(cx, cy, cx+d, cy, LINE, 3))
            if i < rows-1: s.append(line(cx, cy, cx, cy+d, LINE, 3))
    # 高亮：取值相同的一对 (0,0)-(0,1)，取值不同的一对 (1,2)-(1,3)
    s.append(line(x0, y0, x0+d, y0, GRN, 8))
    s.append(line(x0+2*d, y0+d, x0+3*d, y0+d, RED, 8))
    for i in range(rows):
        for j in range(cols):
            s.append(spin(x0 + j*d, y0 + i*d, grid[i][j] > 0))
    # 图例
    lx = 600
    s.append(spin(lx, 118, True)); s.append(T(lx+40, 127, "+1（↑）", 26, INK, anchor="start"))
    s.append(spin(lx, 180, False)); s.append(T(lx+40, 189, "−1（↓）", 26, INK, anchor="start"))
    s.append(line(lx-24, 250, lx+24, 250, GRN, 8))
    s.append(T(lx+40, 247, "取值相同的一对", 26, GRN, anchor="start", weight="700"))
    s.append(T(lx+40, 279, "能量更低", 24, BODY, anchor="start"))
    s.append(line(lx-24, 330, lx+24, 330, RED, 8))
    s.append(T(lx+40, 327, "取值不同的一对", 26, RED, anchor="start", weight="700"))
    s.append(T(lx+40, 359, "能量更高", 24, BODY, anchor="start"))
    s.append(T(lx-24, 400, "灰线：相邻格点之间的相互作用", 22, GRAY, anchor="start"))
    return W, H, "".join(s)

# ================================================= 图 0-2 三格点
def fig02_three_sites():
    W, H = 960, 400
    s = [head(W, "3 个格点排成一行：相同的对越多，能量越低")]
    rows = [((1, 1, 1), "两对都相同", "−2J", "最低", GRN),
            ((1, 1, -1), "一对相同，一对不同", "0", "", INK),
            ((1, -1, 1), "两对都不同", "+2J", "最高", RED)]
    s.append(T(230, 104, "排列", 26, GRAY, weight="700"))
    s.append(T(520, 104, "相邻的两对", 26, GRAY, weight="700"))
    s.append(T(790, 104, "能量 E", 26, GRAY, weight="700"))
    s.append(line(80, 122, 880, 122, LINE, 1.8))
    y = 170
    for sp, desc, e, tag, col in rows:
        xs = [150, 230, 310]
        for k in range(2):
            same = sp[k] == sp[k+1]
            s.append(line(xs[k], y, xs[k+1], y, GRN if same else RED, 6))
        for x, v in zip(xs, sp):
            s.append(spin(x, y, v > 0))
        s.append(T(520, y+9, desc, 26, BODY))
        s.append(T(790, y+11, e, 34, col, weight="700"))
        if tag:
            s.append(T(860, y+9, tag, 22, col, anchor="start"))
        s.append(line(80, y+42, 880, y+42, LINE, 1.2))
        y += 84
    return W, H, "".join(s)

# ================================================= 图 0-3 低温 / 高温（自制模拟）
def simulate(T_, L=48, sweeps=600, start=None, seed=0):
    rng = np.random.default_rng(seed)
    S = np.ones((L, L), int) if start == "up" else rng.choice([-1, 1], (L, L))
    ii, jj = np.indices((L, L))
    masks = [(ii + jj) % 2 == 0, (ii + jj) % 2 == 1]
    for _ in range(sweeps):
        for m in masks:
            nb = (np.roll(S, 1, 0) + np.roll(S, -1, 0) +
                  np.roll(S, 1, 1) + np.roll(S, -1, 1))
            dE = 2 * S * nb          # J = 1，k = 1
            acc = rng.random((L, L)) < np.exp(-dE / T_)
            S = np.where(m & acc, -S, S)
    return S

def lattice_svg(S, x0, y0, size):
    L = S.shape[0]; c = size / L
    s = [f'<rect x="{x0}" y="{y0}" width="{size}" height="{size}" fill="#EEEEEE"/>']
    for i in range(L):
        for j in range(L):
            if S[i, j] > 0:
                s.append(f'<rect x="{x0+j*c:.2f}" y="{y0+i*c:.2f}" width="{c+0.3:.2f}" '
                         f'height="{c+0.3:.2f}" fill="{ACC}"/>')
    s.append(f'<rect x="{x0}" y="{y0}" width="{size}" height="{size}" fill="none" stroke="{CARD_L}" stroke-width="2"/>')
    return "".join(s)

def fig03_low_high():
    W, H = 960, 494
    s = [head(W, "低温下大片格点取值相同，高温下取值杂乱")]
    lo = simulate(1.5, start="up", seed=1)
    hi = simulate(3.5, seed=2)
    size = 320
    for x0, S, t1, t2 in [(40, lo, "低温", "kT = 1.5 J"), (600, hi, "高温", "kT = 3.5 J")]:
        s.append(lattice_svg(S, x0, 80, size))
        s.append(T(x0 + size/2, 80 + size + 40, t1, 30, INK, weight="700"))
        s.append(T(x0 + size/2, 80 + size + 74, t2, 24, BODY))
    s.append(f'<rect x="402" y="180" width="22" height="22" fill="{ACC}"/>')
    s.append(T(436, 199, "+1", 24, BODY, anchor="start"))
    s.append(f'<rect x="402" y="226" width="22" height="22" fill="#EEEEEE" stroke="{CARD_L}"/>')
    s.append(T(436, 245, "−1", 24, BODY, anchor="start"))
    s.append(T(480, 300, "48 × 48 方格", 20, GRAY))
    s.append(T(480, 328, "自制模拟", 20, GRAY))
    return W, H, "".join(s)

# ================================================= 卡 6 正问题 / 逆问题
def fig_forward_inverse():
    W, H = 960, 370
    s = [head(W, "同一个模型，已知与要求的互换")]
    s.append(T(400, 100, "已知", 28, GRAY, weight="700"))
    s.append(T(740, 100, "要求的", 28, GRAY, weight="700"))
    s.append(line(60, 118, 900, 118, LINE, 1.8))
    rows = [("正问题", "物理、记忆网络", "J、T", "各排列的概率\n宏观行为", ACC, TINT, 190),
            ("逆问题", "神经数据分析", "记录到的\n放电数据", "参数 J、h", GRN, GRNT, 304)]
    for name, sub, known, want, col, tint, y in rows:
        s.append(box(60, y-52, 840, 104, tint, col, rx=14, sw=2))
        s.append(T(150, y-6, name, 32, col, weight="700"))
        s.append(T(150, y+30, sub, 22, BODY))
        for x, txt in [(400, known), (740, want)]:
            parts = txt.split("\n")
            yy = y + 10 - 17*(len(parts)-1)
            for p in parts:
                s.append(T(x, yy, p, 28, INK, weight="700")); yy += 36
        s.append(line(500, y, 620, y, col, 3, marker="ah" if col == ACC else "ahn"))
    return W, H, "".join(s)

# ================================================= 卡 7 两条线
def fig_two_lines():
    W, H = 960, 410
    s = [head(W, "按 J 从哪里来，分成两条线")]
    s.append(box(330, 76, 300, 76, TINT, ACC, rx=16, sw=2))
    s.append(T(480, 125, "Ising 模型", 34, ACCD, weight="700"))
    lines_ = [(240, ACC, TINT, "ah", "第一条线", "神经网络的动力学与记忆模型", "J 由人设定 · 正问题", "Hopfield 1982"),
              (720, GRN, GRNT, "ahn", "第二条线", "神经数据的统计描述", "J 从数据估计 · 逆问题", "Schneidman 2006")]
    for cx, col, tint, mk, t1, t2, t3, t4 in lines_:
        s.append(path(f"M480,154 C480,190 {cx},180 {cx},206", col, 3, marker=mk))
        s.append(box(cx-220, 214, 440, 180, tint, col, rx=16, sw=2))
        s.append(T(cx, 258, t1, 32, col, weight="700"))
        s.append(T(cx, 298, t2, 24, INK))
        s.append(T(cx, 334, t3, 24, BODY))
        s.append(T(cx, 372, "代表工作：" + t4, 24, col, weight="700"))
    return W, H, "".join(s)


if __name__ == "__main__":
    for name, fn in [("toc", toc), ("fig01-lattice", fig01_lattice),
                     ("fig02-three-sites", fig02_three_sites),
                     ("fig03-low-high", fig03_low_high),
                     ("fig04-forward-inverse", fig_forward_inverse),
                     ("fig05-two-lines", fig_two_lines)]:
        W, H, inner = fn()
        print(render(name, W, H, inner))
