# -*- coding: utf-8 -*-
"""series-amp-01 · 如何采到准确的脑电 —— 自制示意图"""
import os, subprocess, tempfile, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from grounding2_figs import (T, box, line, circ, ell, path, gnd, cap_v, res_v,
                             elec, wave, DEFS, FONT,
                             BG, ACC, ACCD, TINT, INK, BODY, GRAY, LINE,
                             RED, REDT, GRN, GRNT, CARD_L, PANEL)

SKILL_DIR = os.path.dirname(os.path.dirname(HERE))
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "series-amp-01", "figs")
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

# ================================================= 封面概念图
def cover_concept():
    W, H = 960, 560
    s = [box(24, 20, 912, 516, "#FFFFFF", CARD_L, rx=18)]
    s.append(T(480, 90, "两个比值，同一个分母", 34, INK, weight="700"))
    s.append(line(140, 120, 820, 120, LINE, 1.6))
    # 左：幅度损失
    s.append(box(96, 158, 340, 200, TINT, ACC, rx=16))
    s.append(T(266, 206, "幅度损失的比例", 27, ACCD, weight="700"))
    s.append(T(266, 268, "R e", 40, INK, weight="700"))
    s.append(line(196, 288, 336, 288, INK, 3))
    s.append(T(266, 336, "Z in", 40, ACC, weight="700"))
    # 右：共模漏进
    s.append(box(524, 158, 340, 200, REDT, RED, rx=16))
    s.append(T(694, 206, "共模漏进的比例", 27, RED, weight="700"))
    s.append(T(694, 268, "阻抗失配", 34, INK, weight="700"))
    s.append(line(624, 288, 764, 288, INK, 3))
    s.append(T(694, 336, "Z in", 40, ACC, weight="700"))
    # 底部归属
    s.append(T(266, 402, "分子在电极这一侧", 25, BODY))
    s.append(T(694, 402, "分子也在电极这一侧", 25, BODY))
    s.append(box(160, 436, 640, 66, PANEL, CARD_L))
    s.append(T(480, 478, "分母同为放大器输入阻抗", 29, INK, weight="700"))
    return W, H, "".join(s)

# ================================================= 目录
def toc():
    W, H = 960, 700
    s = [T(480, 76, "本期路线", 40, INK, weight="700")]
    s.append(line(120, 106, 840, 106, LINE, 1.8))
    items = [
        ("①", "记录的目标", "把头皮上的电压差原样搬进文件"),
        ("②", "接上仪器就有损失", "R e 与 Z in 分压，为什么要 GΩ"),
        ("③", "差分放大", "只放大两端之差，它看电压不看来源"),
        ("④", "电极接触不一致", "共模经不同 R e 漏成差模，代数字"),
        ("⑤", "回到采集", "两条要求都是同一个分母上的比值"),
    ]
    y = 168
    for n, t, d in items:
        s.append(circ(150, y-9, 25, TINT, ACC, 2.4))
        s.append(T(150, y+1, n, 27, ACCD, weight="700"))
        s.append(T(200, y-4, t, 31, INK, anchor="start", weight="700"))
        s.append(T(200, y+34, d, 24, BODY, anchor="start"))
        y += 100
    return W, H, "".join(s)

# ================================================= 卡① 两片电极
def fig1_two_electrodes():
    W, H = 960, 480
    s = [head(W, "一个通道对应两片电极，记的是它们之间的电压差")]
    # 头部轮廓
    s.append(ell(320, 246, 170, 118, "#FFFFFF", GRAY, 2.4))
    s.append(T(320, 300, "头", 30, GRAY, weight="700"))
    # 电极
    s.append(elec(238, 140, 96, 22, ACC))
    s.append(T(238, 118, "测量电极", 24, ACCD, weight="700"))
    s.append(elec(408, 134, 96, 22, GRN))
    s.append(T(408, 112, "参考电极", 24, GRN, weight="700"))
    # 导线
    s.append(path("M238,140 L238,196 L640,196", ACC, 2.6))
    s.append(path("M408,134 L408,232 L640,232", GRN, 2.6))
    s.append(box(640, 164, 250, 100, PANEL, CARD_L))
    s.append(T(765, 202, "差分放大器", 28, INK, weight="700"))
    s.append(T(765, 240, "只放大两端之差", 22, BODY))
    # 两条要求
    s.append(box(80, 372, 380, 90, TINT, ACC, rx=14))
    s.append(T(270, 410, "幅度不能变", 30, ACCD, weight="700"))
    s.append(T(270, 444, "µV 量级，禁不起损失", 23, BODY))
    s.append(box(500, 372, 380, 90, REDT, RED, rx=14))
    s.append(T(690, 410, "不能混进别的东西", 30, RED, weight="700"))
    s.append(T(690, 444, "干扰比信号大得多", 23, BODY))
    return W, H, "".join(s)

# ================================================= 卡②-1 分压回路
def fig2_divider():
    W, H = 960, 470
    s = [head(W, "电流流过接触阻抗，那一段的压降进不了放大器")]
    x0, xr, xz = 150, 430, 720
    ytop, ybot = 150, 372
    # 源
    s.append(circ(x0, (ytop+ybot)/2, 44, TINT, ACC, 2.6))
    s.append(T(x0, (ytop+ybot)/2+9, "V 头皮", 24, ACCD, weight="700"))
    # 上边导线
    s.append(line(x0, ytop-0, x0, ytop, INK, 2.6))
    s.append(path(f"M{x0},{ytop-44} L{x0},{ytop} L{xr-30},{ytop}", INK, 2.6))
    s.append(res_v(xr, ytop, h=26, w=90))
    s.append(f'<rect x="{xr-45}" y="{ytop-13}" width="90" height="26" fill="#FFFFFF" stroke="{RED}" stroke-width="2.6"/>')
    s.append(T(xr, ytop-30, "R e  接触阻抗", 24, RED, weight="700"))
    s.append(path(f"M{xr+45},{ytop} L{xz},{ytop} L{xz},{ytop+40}", INK, 2.6))
    # Z_in
    s.append(f'<rect x="{xz-52}" y="{ytop+40}" width="104" height="118" fill="#FFFFFF" stroke="{ACC}" stroke-width="2.8" rx="8"/>')
    s.append(T(xz, ytop+92, "Z in", 30, ACC, weight="700"))
    s.append(T(xz, ytop+128, "输入阻抗", 22, BODY))
    s.append(path(f"M{xz},{ytop+158} L{xz},{ybot} L{x0},{ybot} L{x0},{ybot+0}", INK, 2.6))
    s.append(line(x0, (ytop+ybot)/2+44, x0, ybot, INK, 2.6))
    # 电流箭头
    s.append(path(f"M{x0+70},{ytop-16} L{x0+210},{ytop-16}", ACC, 2.8, marker="ah"))
    s.append(T(x0+140, ytop-28, "I", 27, ACC, weight="700"))
    # 压降标注
    s.append(box(300, 404, 360, 50, REDT, RED))
    s.append(T(480, 436, "R e 上的压降 I · R e 被扣掉", 25, RED, weight="700"))
    return W, H, "".join(s)

# ================================================= 卡②-2 门槛
def fig3_threshold():
    W, H = 960, 440
    s = [head(W, "接触阻抗越大，需要的输入阻抗越高")]
    s.append(box(90, 100, 780, 62, PANEL, CARD_L))
    s.append(T(480, 140, "误差 ＝ R e / (R e ＋ Z in) ≈ R e / Z in", 30, INK, weight="700"))
    s.append(T(480, 196, "取 0.1% 作为示例的容忍度，Z in 至少是 R e 的一千倍", 25, BODY))
    rows = [("凝胶电极", "14 kΩ", "Z in 需 > 14 MΩ", ACC, TINT),
            ("干电极", "516 kΩ", "Z in 需 > 516 MΩ", RED, REDT)]
    y = 240
    for name, r, need, col, tint in rows:
        s.append(box(120, y, 720, 68, tint, col, rx=12))
        s.append(T(210, y+43, name, 27, col, anchor="middle", weight="700"))
        s.append(T(400, y+43, r, 28, INK, weight="700"))
        s.append(T(500, y+43, "→", 26, GRAY))
        s.append(T(690, y+43, need, 27, INK, weight="700"))
        y += 88
    s.append(T(480, 424, "商用设备标称 > 1000 GΩ，落在这个量级之上", 24, BODY))
    return W, H, "".join(s)

# ================================================= 卡③-1 差分
def fig4_differential():
    W, H = 960, 450
    s = [head(W, "两端共有的成分在相减时抵消")]
    # 输入波形
    s.append(T(180, 108, "输入端 1", 25, ACCD, weight="700"))
    s.append(wave(90, 160, 190, 26, 2.0, ACC, 2.6))
    s.append(wave(90, 160, 190, 9, 9.0, RED, 2.0, phase=0.4))
    s.append(T(180, 218, "脑电 + 共模", 22, BODY))
    s.append(T(180, 262, "输入端 2", 25, GRN, weight="700"))
    s.append(wave(90, 314, 190, 12, 2.0, GRN, 2.6, phase=1.9))
    s.append(wave(90, 314, 190, 9, 9.0, RED, 2.0, phase=0.4))
    s.append(T(180, 372, "另一处脑电 + 同一份共模", 21, BODY))
    # 放大器三角
    s.append(path("M420,150 L420,336 L560,243 Z", INK, 2.6, fill="#FFFFFF"))
    s.append(T(452, 186, "＋", 26, ACC, weight="700"))
    s.append(T(452, 316, "－", 26, GRN, weight="700"))
    s.append(line(290, 176, 418, 190, ACC, 2.4))
    s.append(line(290, 314, 418, 300, GRN, 2.4))
    s.append(T(560, 128, "输出 ＝ G · (V₊ − V₋)", 26, INK, weight="700", anchor="middle"))
    # 输出
    s.append(line(560, 243, 630, 243, INK, 2.4))
    s.append(wave(636, 243, 230, 40, 2.0, ACCD, 3.0))
    s.append(box(620, 336, 270, 56, TINT, ACC))
    s.append(T(755, 372, "共模消失，差值留下", 25, ACCD, weight="700"))
    s.append(T(755, 300, "红色成分已被抵消", 22, RED))
    return W, H, "".join(s)

# ================================================= 卡③-2 两栏
def fig5_two_consequences():
    W, H = 960, 440
    s = [head(W, "减法只看电压，两个后果方向相反")]
    s.append(box(70, 100, 390, 300, TINT, ACC, rx=16))
    s.append(T(265, 148, "两端共有的脑活动", 29, ACCD, weight="700"))
    s.append(T(265, 190, "同样被减掉", 26, ACCD))
    s.append(wave(110, 250, 310, 24, 2.0, ACC, 2.6))
    s.append(line(140, 296, 390, 296, ACC, 2.4, "8 6"))
    s.append(T(265, 344, "参考越靠近信号源，", 23, BODY))
    s.append(T(265, 376, "记录到的幅度越小", 23, BODY))
    s.append(box(500, 100, 390, 300, REDT, RED, rx=16))
    s.append(T(695, 148, "只出现在一端的干扰", 29, RED, weight="700"))
    s.append(T(695, 190, "同样被完整放大", 26, RED))
    s.append(wave(540, 250, 310, 30, 3.0, RED, 2.8))
    s.append(T(695, 344, "眼动、单片电极下的肌肉活动、", 23, BODY))
    s.append(T(695, 376, "单片电极自身的电位漂移", 23, BODY))
    return W, H, "".join(s)

# ================================================= 卡④-1 两条通路
def fig6_two_paths():
    W, H = 960, 460
    s = [head(W, "同一份共模经两条不同的电极通路，到两端已经不齐")]
    s.append(circ(126, 250, 52, PANEL, GRAY, 2.4))
    s.append(T(126, 244, "V cm", 26, INK, weight="700"))
    s.append(T(126, 274, "体表", 21, BODY))
    # 通路 1
    s.append(path(f"M178,222 L300,168", INK, 2.4))
    s.append(f'<rect x="300" y="146" width="104" height="42" fill="#FFFFFF" stroke="{ACC}" stroke-width="2.6" rx="6"/>')
    s.append(T(352, 175, "R e1", 26, ACC, weight="700"))
    s.append(path(f"M404,167 L560,167", INK, 2.4, marker="ahk"))
    # 通路 2
    s.append(path(f"M178,278 L300,332", INK, 2.4))
    s.append(f'<rect x="300" y="310" width="104" height="42" fill="#FFFFFF" stroke="{RED}" stroke-width="2.6" rx="6"/>')
    s.append(T(352, 339, "R e2", 26, RED, weight="700"))
    s.append(path(f"M404,331 L560,331", INK, 2.4, marker="ahk"))
    # 输入端高度不齐
    s.append(box(580, 120, 300, 240, PANEL, CARD_L))
    s.append(T(730, 156, "放大器输入端", 25, INK, weight="700"))
    s.append(line(620, 214, 840, 214, ACC, 5))
    s.append(T(730, 200, "输入端 1", 22, ACCD))
    s.append(line(620, 300, 840, 300, RED, 5))
    s.append(T(730, 334, "输入端 2", 22, RED))
    s.append(path("M866,214 L866,300", GRAY, 2.2))
    s.append(T(898, 262, "ΔV", 26, INK, weight="700"))
    s.append(box(230, 394, 500, 52, REDT, RED))
    s.append(T(480, 428, "这段差值满足「两端不同」，被当作信号放大", 25, RED, weight="700"))
    return W, H, "".join(s)

# ================================================= 卡④-2 化简
def fig7_algebra():
    W, H = 960, 480
    s = [head(W, "约分之后，判据只剩失配与输入阻抗之比")]
    steps = [
        ("相减通分", "ΔV ＝ V cm × Z in × (R e2 − R e1) / [(R e1+Z in)(R e2+Z in)]", 25),
        ("Z in ≫ R e，分母约为 Z in²", "ΔV ≈ V cm × (R e2 − R e1) / Z in", 28),
        ("两边同除 V cm", "ΔV / V cm ＝ 阻抗失配 / 输入阻抗", 30),
    ]
    y = 112
    for lab, expr, sz in steps:
        s.append(T(480, y, lab, 23, GRAY))
        s.append(box(80, y+16, 800, 62, PANEL if sz < 30 else TINT,
                     CARD_L if sz < 30 else ACC))
        s.append(T(480, y+58, expr, sz, INK if sz < 30 else ACCD, weight="700"))
        y += 108
    s.append(T(480, 456, "阻抗失配 ＝ 两片电极接触阻抗之差；贴得一样好，它就是零", 24, BODY))
    return W, H, "".join(s)

# ================================================= 卡④-3 V_cm
def fig8_vcm():
    W, H = 960, 460
    s = [head(W, "地电极的接触阻抗决定残余共模的大小")]
    x = 200
    s.append(T(x, 108, "市电 220 V", 25, INK, weight="700"))
    s.append(line(x, 124, x, 168, INK, 2.6))
    s.append(cap_v(x, 180, 1.0, GRAY))
    s.append(T(x+80, 186, "C₁ ＝ 2 pF", 24, GRAY, anchor="start"))
    s.append(line(x, 194, x, 244, INK, 2.6))
    s.append(box(x-96, 244, 192, 60, TINT, ACC))
    s.append(T(x, 284, "人体", 28, ACCD, weight="700"))
    s.append(line(x, 304, x, 350, INK, 2.6))
    s.append(f'<rect x="{x-46}" y="350" width="92" height="38" fill="#FFFFFF" stroke="{RED}" stroke-width="2.6" rx="6"/>')
    s.append(T(x, 377, "R e", 26, RED, weight="700"))
    s.append(gnd(x, 392, 0.9, INK, 2.6))
    s.append(T(x+80, 377, "地电极", 24, RED, anchor="start"))
    # 右侧两态
    s.append(T(660, 116, "V cm 由 R e 决定", 29, INK, weight="700"))
    rows = [("地电极用凝胶电极", "14 kΩ", "1.9 mV", ACC, TINT),
            ("地电极用干电极", "516 kΩ", "71 mV", RED, REDT)]
    y = 160
    for name, r, v, col, tint in rows:
        s.append(box(440, y, 460, 104, tint, col, rx=14))
        s.append(T(670, y+38, name, 25, col, weight="700"))
        s.append(T(560, y+80, r, 26, INK, weight="700"))
        s.append(T(660, y+80, "→", 24, GRAY))
        s.append(T(780, y+80, v, 30, INK, weight="700"))
        y += 124
    s.append(T(660, 428, "未接地电极时人体被抬起约 2.2 V（自算）", 23, BODY))
    return W, H, "".join(s)

# ================================================= 卡④-4 数值
def fig9_numbers():
    W, H = 960, 450
    s = [head(W, "干电极漏进来的电压是 β 活动的上百倍")]
    cols = ["", "失配", "漏进比例", "漏进电压"]
    xs = [180, 390, 585, 775]
    s.append(line(90, 108, 870, 108, LINE, 1.6))
    for x, c in zip(xs, cols):
        s.append(T(x, 142, c, 25, GRAY, weight="700"))
    rows = [("凝胶电极", "8 kΩ", "5.5×10⁻⁴", "1.07 µV", ACC, TINT),
            ("干电极", "429 kΩ", "3.0×10⁻²", "2.11 mV", RED, REDT)]
    y = 166
    for name, a, b, c, col, tint in rows:
        s.append(box(90, y, 780, 74, tint, col, rx=12))
        s.append(T(xs[0], y+48, name, 27, col, weight="700"))
        s.append(T(xs[1], y+48, a, 27, INK, weight="700"))
        s.append(T(xs[2], y+48, b, 27, INK, weight="700"))
        s.append(T(xs[3], y+48, c, 29, INK, weight="700"))
        y += 92
    s.append(box(90, 356, 780, 74, PANEL, CARD_L))
    s.append(T(480, 386, "对照头皮 EEG 本身", 24, GRAY))
    s.append(T(480, 420, "β 活动 10–20 µV      全带宽上界约 100 µV", 27, INK, weight="700"))
    return W, H, "".join(s)

# ================================================= 卡⑤ 两个比值
def fig10_two_ratios():
    W, H = 960, 440
    s = [head(W, "两条要求压的是同一个分母上的两个分子")]
    s.append(box(80, 100, 360, 210, TINT, ACC, rx=16))
    s.append(T(260, 146, "幅度损失的比例", 27, ACCD, weight="700"))
    s.append(T(260, 216, "R e", 42, INK, weight="700"))
    s.append(line(190, 236, 330, 236, INK, 3))
    s.append(T(260, 288, "Z in", 42, ACC, weight="700"))
    s.append(box(520, 100, 360, 210, REDT, RED, rx=16))
    s.append(T(700, 146, "共模漏进的比例", 27, RED, weight="700"))
    s.append(T(700, 216, "阻抗失配", 34, INK, weight="700"))
    s.append(line(630, 236, 770, 236, INK, 3))
    s.append(T(700, 288, "Z in", 42, ACC, weight="700"))
    s.append(box(150, 344, 300, 72, PANEL, CARD_L))
    s.append(T(300, 376, "分子：操作一侧", 24, GRAY))
    s.append(T(300, 406, "把每片电极贴好，贴得一样好", 23, INK, weight="700"))
    s.append(box(510, 344, 300, 72, PANEL, CARD_L))
    s.append(T(660, 376, "分母：仪器一侧", 24, GRAY))
    s.append(T(660, 406, "把输入阻抗做大", 23, INK, weight="700"))
    return W, H, "".join(s)

FIGS = {
    "cover-concept": cover_concept,
    "toc": toc,
    "fig1-two-electrodes": fig1_two_electrodes,
    "fig2-divider": fig2_divider,
    "fig3-threshold": fig3_threshold,
    "fig4-differential": fig4_differential,
    "fig5-two-consequences": fig5_two_consequences,
    "fig6-two-paths": fig6_two_paths,
    "fig7-algebra": fig7_algebra,
    "fig8-vcm": fig8_vcm,
    "fig9-numbers": fig9_numbers,
    "fig10-two-ratios": fig10_two_ratios,
}

if __name__ == "__main__":
    names = sys.argv[1:] or list(FIGS)
    for n in names:
        w, h, inner = FIGS[n]()
        print(render(n, w, h, inner))
