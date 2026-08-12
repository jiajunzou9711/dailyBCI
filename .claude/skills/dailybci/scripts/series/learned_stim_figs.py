"""第三期:把编码交给模型去学 —— 自制 SVG 示意图。
Rendered to PNG via playwright chromium.
"""
import os, subprocess, tempfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-08-12-learned-stim", "figs")
os.makedirs(OUT, exist_ok=True)

ACC = "#2F6DB5"; ACCD = "#1E4E86"; TINT = "#E9F0F8"
INK = "#1A1A1A"; BODY = "#4A4A4A"; GRAY = "#8A8A8A"; LINE = "#D6DBE2"
CARD_L = "#DCE5F0"; NEU = "#F1F3F5"; NEUL = "#C9CFD6"
BG = "#FAFAFA"


def T(x, y, s, size=25, fill=INK, anchor="middle", weight="400"):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" font-weight="{weight}">{s}</text>')


def box(x, y, w, h, fill, stroke, rx=12, sw=1.5):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')


def arrow(x1, y1, x2, y2, color=INK, sw=2.4):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" '
            f'stroke-width="{sw}" marker-end="url(#ah)"/>')


def path(d, color=INK, sw=2.4, dash=""):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}"{da} '
            f'marker-end="url(#ah)"/>')


DEFS = ('<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" '
        'markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
        f'<path d="M 0 0 L 10 5 L 0 10 z" fill="{INK}"/></marker>'
        '<marker id="ahb" viewBox="0 0 10 10" refX="9" refY="5" '
        'markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
        f'<path d="M 0 0 L 10 5 L 0 10 z" fill="{ACC}"/></marker></defs>')


def lock(cx, cy, s=1.0):
    """小锁形,表示冻结。"""
    w, h = 20 * s, 15 * s
    x, y = cx - w / 2, cy - h / 2
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{3*s}" '
            f'fill="{GRAY}"/>'
            f'<path d="M {cx-6*s} {y} v {-6*s} a {6*s} {6*s} 0 0 1 {12*s} 0 v {6*s}" '
            f'fill="none" stroke="{GRAY}" stroke-width="{3*s}"/>')


# ---------- 目录 ----------
def toc():
    items = [
        ("1", "同一个刺激,隔天就不一样", "跨天方差显著大于同天之内"),
        ("2", "换一个问法:先问皮层进入什么状态", "同一块阵列既刺激又记录"),
        ("3", "目标是一片神经活动,求的是一组电流", "先学一个能预测后果的前向模型"),
        ("4", "冻住权重,改输入", "被梯度更新的是刺激向量本身"),
        ("5", "把「怎么解」本身学成一个网络", "一次前向传播,约 50 微秒"),
        ("6", "老做法接近随机,新方法摸到上限", "误差与重放原始刺激相当"),
        ("7", "指令有 86 维,引出的活动只有 10 维", "离流形越远越做不到"),
        ("8", "标签可从「问患者」换成「读电极」", "检测准确率 74.2% → 88.7%"),
        ("9", "解决了右半段,左半段还没有人走通", "单被试 · 54/96 通道 · 非闭环"),
    ]
    s = []
    y = 20
    for n, title, sub in items:
        s.append(box(26, y, 908, 70, "#F7F9FC", CARD_L, 14, 1.5))
        s.append(f'<circle cx="70" cy="{y+35}" r="23" fill="{TINT}" stroke="{ACC}" stroke-width="1.5"/>')
        s.append(T(70, y + 44, n, 27, ACCD, weight="700"))
        s.append(T(112, y + 31, title, 27, INK, anchor="start", weight="700"))
        s.append(T(112, y + 58, sub, 20, GRAY, anchor="start"))
        y += 82
    return 960, y + 4, "".join(s)


# ---------- 卡6:冻住权重,改输入 ----------
def fig_gradient():
    s = [DEFS]
    cols = [
        (248, "训练前向模型时", "刺激", NEU, NEUL, INK, "前向模型", TINT, ACC, ACCD,
         "与「实测活动」比", "更新模型", "model"),
        (712, "梯度优化求刺激时", "刺激", TINT, ACC, ACCD, "前向模型", NEU, NEUL, INK,
         "与「目标活动」比", "更新刺激", "stim"),
    ]
    for (cx, head, n1, f1, st1, tc1, n2, f2, st2, tc2, cmp_t, ret_t, mode) in cols:
        s.append(T(cx, 46, head, 30, INK, weight="700"))
        # 刺激
        s.append(box(cx - 100, 78, 200, 58, f1, st1, 12, 2))
        s.append(T(cx, 115, n1, 28, tc1, weight="700"))
        s.append(arrow(cx, 140, cx, 178))
        # 前向模型
        s.append(box(cx - 110, 182, 220, 78, f2, st2, 12, 2))
        s.append(T(cx - 8, 230, n2, 28, tc2, weight="700"))
        if mode == "stim":
            s.append(lock(cx + 78, 221, 1.0))
        s.append(arrow(cx, 264, cx, 302))
        # 预测活动
        s.append(box(cx - 100, 306, 200, 58, NEU, NEUL, 12, 1.6))
        s.append(T(cx, 343, "预测活动", 28, INK))
        s.append(arrow(cx, 368, cx, 400))
        # 比较
        s.append(T(cx, 428, cmp_t, 26, BODY))
        # 回传
        tgt_y = 221 if mode == "model" else 107
        left = cx - 160
        s.append(path(f"M {cx-104} 420 H {left} V {tgt_y} H {cx-114 if mode=='model' else cx-104}",
                      ACC, 2.6))
        s.append(T(left, tgt_y - 26, ret_t, 23, ACCD, weight="700"))
    # 图例
    s.append(T(480, 462, "蓝色路径 = 梯度回传的去向", 23, GRAY))
    s.append(f'<line x1="60" y1="484" x2="900" y2="484" stroke="{LINE}" stroke-width="1.4"/>')
    s.append(f'<rect x="230" y="506" width="26" height="18" rx="4" fill="{TINT}" stroke="{ACC}" stroke-width="1.8"/>')
    s.append(T(268, 521, "这一栏中正在被更新的", 23, BODY, anchor="start"))
    s.append(f'<rect x="560" y="506" width="26" height="18" rx="4" fill="{NEU}" stroke="{NEUL}" stroke-width="1.8"/>')
    s.append(lock(614, 515, 0.8))
    s.append(T(634, 521, "固定不动", 23, BODY, anchor="start"))
    return 960, 550, "".join(s)


# ---------- 卡7:把「怎么解」学成一个网络 ----------
def fig_inverse():
    s = [DEFS]
    y = 150
    # 目标活动
    s.append(box(28, y - 30, 150, 62, NEU, NEUL, 12, 1.6))
    s.append(T(103, y + 8, "目标活动", 27, INK, weight="700"))
    s.append(arrow(182, y, 218, y))
    # 逆网络
    s.append(box(222, y - 40, 168, 82, TINT, ACC, 12, 2.2))
    s.append(T(306, y + 8, "逆网络", 29, ACCD, weight="700"))
    s.append(arrow(394, y, 430, y))
    # 刺激
    s.append(box(434, y - 30, 120, 62, NEU, NEUL, 12, 1.6))
    s.append(T(494, y + 8, "刺激", 27, INK, weight="700"))
    s.append(arrow(558, y, 594, y))
    # 前向模型(冻结)
    s.append(box(598, y - 40, 196, 82, NEU, NEUL, 12, 2.2))
    s.append(T(686, y + 8, "前向模型", 28, INK, weight="700"))
    s.append(lock(762, y - 22, 0.9))
    s.append(arrow(798, y, 834, y))
    # 预测活动
    s.append(box(838, y - 30, 108, 62, NEU, NEUL, 12, 1.6))
    s.append(T(892, y - 2, "预测", 25, INK))
    s.append(T(892, y + 24, "活动", 25, INK))
    # 损失
    s.append(f'<line x1="892" y1="182" x2="892" y2="224" stroke="{ACC}" stroke-width="2.6" marker-end="url(#ahb)"/>')
    s.append(T(892, 254, "损失 = 与目标活动比", 24, ACCD, weight="700"))
    # 回传:从损失出发,穿过前向模型,回到逆网络
    s.append(path("M 892 284 H 306 V 196", ACC, 2.8))
    s.append(T(560, 318, "梯度穿过冻结的前向模型,一路传回逆网络", 24, ACCD, weight="700"))
    # 刺激处无标准答案
    s.append(f'<line x1="494" y1="184" x2="494" y2="206" stroke="{GRAY}" stroke-width="1.6" stroke-dasharray="4 4"/>')
    s.append(T(494, 230, "这一处没有标准答案", 23, GRAY, weight="700"))
    # 只有逆网络在更新
    s.append(T(306, 74, "只有它在更新", 24, ACCD, weight="700"))
    s.append(f'<line x1="306" y1="84" x2="306" y2="106" stroke="{ACC}" stroke-width="1.8" marker-end="url(#ahb)"/>')
    # 图例
    s.append(f'<line x1="80" y1="352" x2="960" y2="352" stroke="{LINE}" stroke-width="1.4"/>')
    s.append(f'<rect x="290" y="374" width="26" height="18" rx="4" fill="{TINT}" stroke="{ACC}" stroke-width="1.8"/>')
    s.append(T(328, 389, "正在被更新", 23, BODY, anchor="start"))
    s.append(f'<rect x="590" y="374" width="26" height="18" rx="4" fill="{NEU}" stroke="{NEUL}" stroke-width="1.8"/>')
    s.append(lock(644, 383, 0.8))
    s.append(T(664, 389, "冻结", 23, BODY, anchor="start"))
    return 1040, 418, "".join(s)


FIGS = {"toc": toc, "fig-gradient": fig_gradient, "fig-inverse": fig_inverse}


def render(name, w, h, inner):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
           f'viewBox="0 0 {w} {h}" font-family="HeitiSC,Helvetica,Arial,sans-serif">'
           f'<rect width="{w}" height="{h}" fill="{BG}"/>{inner}</svg>')
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
