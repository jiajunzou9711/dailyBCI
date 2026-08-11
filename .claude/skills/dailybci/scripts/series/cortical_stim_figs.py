"""第二期:电刺激视皮层能做到什么 —— 自制 SVG 示意图。
Rendered to PNG via playwright chromium.
"""
import os, subprocess, tempfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-08-11-cortical-stim", "figs")
os.makedirs(OUT, exist_ok=True)

ACC = "#2F6DB5"; ACCD = "#1E4E86"; TINT = "#E9F0F8"
INK = "#1A1A1A"; BODY = "#4A4A4A"; GRAY = "#8A8A8A"; LINE = "#D6DBE2"
CARD_L = "#DCE5F0"; NEU = "#F1F3F5"; NEUL = "#C9CFD6"


def T(x, y, s, size=25, fill=INK, anchor="middle", weight="400"):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" font-weight="{weight}">{s}</text>')


def box(x, y, w, h, fill, stroke, rx=12, sw=1.5):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')


# ---------- 目录 ----------
def toc():
    items = [
        ("1", "电流打进 V1,人会看见一个光点", "眼睛和视神经全程不参与"),
        ("2", "坐标建立在「眼位不动」这个假定上", "光幻视随眼动整体漂移"),
        ("3", "电极排布规整,光点落点散乱", "两者之间没有一一对应"),
        ("4", "同时点亮四个,她看见三个", "电极之间并不独立"),
        ("5", "能得到什么,由皮层的结构决定", "换掉「电极即像素」这个模型"),
        ("6", "放弃「同时」,改用时间描摹", "盲人被试每分钟 86 个形状"),
        ("7", "有人体数据的,规模都是个位数", "Orion 六年随访 6 例"),
        ("8", "Neuralink 的 Blindsight 只有一项认定", "试验尚未开始"),
    ]
    s = []
    y = 24
    for n, title, sub in items:
        s.append(box(30, y, 900, 74, "#F7F9FC", CARD_L, 14, 1.5))
        s.append(f'<circle cx="76" cy="{y+37}" r="25" fill="{TINT}" stroke="{ACC}" stroke-width="1.5"/>')
        s.append(T(76, y + 47, n, 29, ACCD, weight="700"))
        s.append(T(122, y + 32, title, 29, INK, anchor="start", weight="700"))
        s.append(T(122, y + 61, sub, 21, GRAY, anchor="start"))
        y += 87
    return 960, y + 6, "".join(s)


# ---------- 卡4:眼动补偿的两笔账 ----------
def fig_eye():
    s = []
    s.append(T(480, 44, "眼睛右转 10° 的那一刻", 30, INK, weight="700"))
    cols = [(30, 250), (296, 200), (508, 170), (700, 230)]
    heads = ["", "视野中的位移", "加上眼位", "净结果"]
    y0 = 76
    for (x, w), h in zip(cols, heads):
        if h:
            s.append(T(x + w / 2, y0 + 34, h, 23, GRAY))
    rows = [
        ("正常看东西", "−10°", "+10°", "0°", "世界纹丝不动", False),
        ("光幻视", "0°", "+10°", "+10°", "跟着眼睛走", True),
    ]
    y = y0 + 54
    for label, d1, d2, d3, note, hi in rows:
        fill = TINT if hi else NEU
        stroke = ACC if hi else NEUL
        s.append(box(30, y, 900, 128, fill, stroke, 14, 1.5))
        s.append(T(cols[0][0] + 24, y + 74, label, 28, INK, anchor="start", weight="700"))
        s.append(T(cols[1][0] + cols[1][1] / 2, y + 68, d1, 44,
                   ACCD if hi else BODY, weight="700"))
        s.append(T(cols[2][0] + cols[2][1] / 2, y + 68, d2, 44, BODY, weight="700"))
        s.append(T(cols[3][0] + cols[3][1] / 2, y + 62, d3, 44,
                   ACCD if hi else BODY, weight="700"))
        s.append(T(cols[3][0] + cols[3][1] / 2, y + 100, note, 21,
                   ACCD if hi else GRAY))
        y += 144
    s.append(T(480, y + 26, "视野中的位移被电极钉死,补偿却照加不误", 24, ACCD, weight="700"))
    return 960, y + 54, "".join(s)


# ---------- 卡7:输出由什么决定 ----------
def fig_decides():
    s = []
    s.append(T(250, 40, "「像素」模型认为由输入决定", 24, GRAY))
    s.append(T(710, 40, "实际的决定因素", 24, ACCD, weight="700"))
    rows = [
        ("光点的位置", "哪些轴突从电极旁经过"),
        ("光点的大小", "被激活的皮层面积 × 所处位置"),
        ("光点的数量与形状", "电极几何 + 彼此的相互作用"),
        ("是否落在同一平面", "同时点亮了几个"),
    ]
    y = 62
    for left, right in rows:
        s.append(box(30, y, 410, 88, NEU, NEUL, 12, 1.5))
        s.append(T(235, y + 54, left, 27, BODY, weight="700"))
        s.append(f'<path d="M456,{y+44} L484,{y+44}" stroke="{ACC}" stroke-width="2.5"/>'
                 f'<path d="M478,{y+38} L486,{y+44} L478,{y+50} Z" fill="{ACC}"/>')
        s.append(box(500, y, 430, 88, TINT, ACC, 12, 1.5))
        s.append(T(715, y + 54, right, 25, ACCD, weight="700"))
        y += 100
    s.append(T(480, y + 26, "右列全部是皮层自己的性质", 24, ACCD, weight="700"))
    return 960, y + 54, "".join(s)


# ---------- 卡9:三套有人体数据的系统 ----------
def fig_systems():
    s = []
    cols = [(30, 170), (208, 320), (536, 200), (744, 186)]
    heads = ["系统", "电极", "入组", "状态"]
    for (x, w), h in zip(cols, heads):
        s.append(T(x + w / 2, 38, h, 23, GRAY))
    rows = [
        ("Orion", "60 · 硬膜下表面", "6 例 · 已植入", "已完成 2025-03", True),
        ("CORTIVIS", "96 · 皮层内 Utah 阵列", "计划 5 例", "招募中", False),
        ("ICVP", "皮层内微电极", "计划 5 例", "招募中", False),
    ]
    y = 58
    for name, ele, n, st, hi in rows:
        s.append(box(30, y, 900, 96, TINT if hi else NEU, ACC if hi else NEUL, 12, 1.5))
        s.append(T(cols[0][0] + cols[0][1] / 2, y + 58, name, 27,
                   ACCD if hi else INK, weight="700"))
        s.append(T(cols[1][0] + cols[1][1] / 2, y + 58, ele, 23, BODY))
        s.append(T(cols[2][0] + cols[2][1] / 2, y + 58, n, 23, BODY))
        s.append(T(cols[3][0] + cols[3][1] / 2, y + 58, st, 23, BODY))
        y += 108
    s.append(T(480, y + 26, "三套系统的人体规模全部是个位数", 25, ACCD, weight="700"))
    return 960, y + 54, "".join(s)


# ---------- 卡10:Blindsight 一手 vs 官网没有的 ----------
def fig_blindsight():
    s = []
    s.append(box(30, 24, 430, 460, TINT, ACC, 14, 1.5))
    s.append(box(500, 24, 430, 460, NEU, NEUL, 14, 1.5))
    s.append(T(245, 66, "官网与 FDA 能核实的", 25, ACCD, weight="700"))
    s.append(T(715, 66, "官网上没有的", 25, GRAY, weight="700"))
    left = ["突破性设备认定 2024-09", "试验状态:尚未开始", "摄像头 + 无线传输 + 植入体",
            "适应症:眼或视神经损伤"]
    right = ["电极数量", "分辨率 / 画质", "时间表", "已植入的人数"]
    y = 128
    for a, b in zip(left, right):
        s.append(f'<circle cx="72" cy="{y-8}" r="6" fill="{ACC}"/>')
        s.append(T(96, y, a, 24, ACCD, anchor="start", weight="700"))
        s.append(f'<circle cx="542" cy="{y-8}" r="6" fill="{NEUL}"/>')
        s.append(T(566, y, b, 24, GRAY, anchor="start"))
        y += 84
    s.append(T(480, 528, "认定是加速通道,不是批准", 25, ACCD, weight="700"))
    return 960, 556, "".join(s)


FIGS = {"toc": toc, "fig-eye": fig_eye, "fig-decides": fig_decides,
        "fig-systems": fig_systems, "fig-blindsight": fig_blindsight}


def render(name, w, h, inner):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
           f'viewBox="0 0 {w} {h}" font-family="HeitiSC,Helvetica,Arial,sans-serif">'
           f'<rect width="{w}" height="{h}" fill="#FFFFFF"/>{inner}</svg>')
    html = (f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>'
            f'@font-face{{font-family:"HeitiSC";src:url("file://{FONT}");}}'
            f'*{{margin:0;padding:0}}body{{width:{w}px;height:{h}px}}</style></head>'
            f'<body>{svg}</body></html>')
    tmp = tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8")
    tmp.write(html); tmp.close()
    out = os.path.join(OUT, name + ".png")
    subprocess.run(["npx", "playwright", "screenshot", f"file://{tmp.name}", out,
                    f"--viewport-size={w},{h}", "--wait-for-timeout=600"],
                   check=True, capture_output=True, text=True)
    os.unlink(tmp.name)
    return out


if __name__ == "__main__":
    for name, fn in FIGS.items():
        w, h, inner = fn()
        p = render(name, w, h, inner)
        print("rendered", p, f"({w}x{h})")
