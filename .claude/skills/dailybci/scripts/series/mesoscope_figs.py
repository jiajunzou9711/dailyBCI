"""2026-08-04 日报：双光子全息中尺度显微镜 —— 自制 SVG（目录卡）。
Rendered to PNG via playwright chromium.
"""
import os, subprocess, tempfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-08-04-mesoscope", "figs")
os.makedirs(OUT, exist_ok=True)

ACC = "#2F6DB5"; ACCD = "#1E4E86"; TINT = "#E9F0F8"
INK = "#1A1A1A"; BODY = "#4A4A4A"; GRAY = "#8A8A8A"
CARD_L = "#DCE5F0"


def T(x, y, s, size=25, fill=INK, anchor="middle", weight="400"):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" font-weight="{weight}">{s}</text>')


def box(x, y, w, h, fill, stroke, rx=12, sw=1.5):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')


def circ(cx, cy, r, fill, stroke, sw=1.5):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw}"/>')


def toc():
    """封面之后的第 2 张卡：顶部来源条 + 本期路线。"""
    s = []
    W = 960

    # ---- 顶部来源条 ----
    s.append(box(30, 24, W - 60, 208, TINT, CARD_L, 14, 1.5))
    s.append(T(56, 66, "来源", 22, ACCD, anchor="start", weight="700"))
    src = [
        "2026 年 8 月 · Nature Neuroscience 29:2023–2035 · Technical Report",
        "《Probing inter-areal computations with a two-photon holographic mesoscope》",
        "UC Berkeley 神经科学系与 Helen Wills 神经科学研究所，通讯作者 Hillel Adesnik",
        "物种：小鼠。方法：双光子钙成像读出 + 双光子全息光遗传学写入",
    ]
    y = 106
    for i, ln in enumerate(src):
        size = 23 if i != 1 else 21
        fill = INK if i <= 1 else BODY
        wt = "700" if i == 0 else "400"
        s.append(T(56, y, ln, size, fill, anchor="start", weight=wt))
        y += 34

    # ---- 本期路线 ----
    s.append(T(56, 292, "本期路线", 28, INK, anchor="start", weight="700"))

    items = [
        ("1", "写，一直是脑机接口弱的那半边", "电极刺激无法指定写给谁"),
        ("2", "读已到 5 毫米，写卡在 1 毫米", "一个来自器件的物理上限"),
        ("3", "把可写的那一小块整体搬走", "写入范围扩约十倍"),
        ("4", "写进去的信息，下游读得出来", "0.65 对随机 0.5，且带着内容"),
        ("5", "本地与下游，符号相反", "净影响 −0.19 对 +0.10"),
    ]
    y = 320
    for n, title, sub in items:
        s.append(box(30, y, W - 60, 78, "#F7F9FC", CARD_L, 14, 1.5))
        s.append(circ(78, y + 39, 26, TINT, ACC, 1.5))
        s.append(T(78, y + 49, n, 30, ACCD, weight="700"))
        s.append(T(126, y + 34, title, 29, INK, anchor="start", weight="700"))
        s.append(T(126, y + 64, sub, 22, GRAY, anchor="start"))
        y += 92

    return W, y + 16, "".join(s)


FIGS = {"toc": toc}


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
        print("rendered", render(name, w, h, inner), f"({w}x{h})")
