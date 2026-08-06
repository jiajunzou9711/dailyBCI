"""期二「一个阴性结果」自制示意图 (2026-08-06)。"""
import os, math, subprocess, tempfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-08-06-tus-null", "figs")
os.makedirs(OUT, exist_ok=True)

ACC = "#2F6DB5"; ACCD = "#1E4E86"; TINT = "#E9F0F8"
INK = "#1A1A1A"; BODY = "#4A4A4A"; GRAY = "#8A8A8A"; LINE = "#D6DBE2"
RED = "#C0392B"

DEFS = ('<defs><marker id="ah" markerWidth="10" markerHeight="10" refX="8" refY="3" '
        'orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="%s"/>'
        '</marker>'
        '<marker id="ahr" markerWidth="10" markerHeight="10" refX="8" refY="3" '
        'orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="#C0392B"/>'
        '</marker></defs>' % GRAY)


def T(x, y, s, size=25, fill=INK, anchor="middle", weight="400"):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" font-weight="{weight}">{s}</text>')


# ---------- 封面概念图：打进去了，三个读数都没动 ----------
def cover_concept():
    W, H = 980, 520
    s = []
    # ---- 左：轴位头部轮廓 + 换能器 + 会聚声束 + 靶点 ----
    hx, hy, rx, ry = 250, 262, 168, 200
    s.append(f'<ellipse cx="{hx}" cy="{hy}" rx="{rx}" ry="{ry}" fill="#FBFCFD" '
             f'stroke="{LINE}" stroke-width="3"/>')
    # 换能器（贴左侧）
    tx, ty = hx - rx - 6, hy - 26
    s.append(f'<rect x="{tx-26}" y="{ty-34}" width="26" height="68" rx="6" '
             f'fill="{TINT}" stroke="{ACC}" stroke-width="2.5"/>')
    # 会聚声束：从换能器面收敛到焦点
    fx, fy = hx + 34, hy + 6
    s.append(f'<polygon points="{tx},{ty-32} {tx},{ty+32} {fx},{fy}" '
             f'fill="{ACC}" opacity="0.16"/>')
    s.append(f'<polygon points="{tx},{ty-14} {tx},{ty+14} {fx},{fy}" '
             f'fill="{ACC}" opacity="0.22"/>')
    # 靶点
    s.append(f'<circle cx="{fx}" cy="{fy}" r="13" fill="{ACCD}"/>')
    s.append(f'<circle cx="{fx}" cy="{fy}" r="26" fill="none" stroke="{ACCD}" '
             f'stroke-width="2" opacity="0.45"/>')

    # ---- 中：引出箭头 ----
    s.append(f'<line x1="{fx+40}" y1="{fy}" x2="548" y2="{fy}" stroke="{GRAY}" '
             f'stroke-width="2.5" marker-end="url(#ah)"/>')

    # ---- 右：三条平直读数 ----
    rows = [("脑电幅度", 138), ("脑电潜伏期", 264), ("知觉行为", 390)]
    x0, x1 = 600, 946
    for lab, y in rows:
        s.append(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{LINE}" '
                 f'stroke-width="2" stroke-dasharray="5,5"/>')
        pts = []
        n = 56
        for i in range(n + 1):
            xx = x0 + i * (x1 - x0) / n
            yy = y + 1.3 * math.sin(i * 1.7) + 0.8 * math.sin(i * 0.6)
            pts.append(f"{xx:.1f},{yy:.1f}")
        s.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{INK}" '
                 f'stroke-width="2.6" stroke-linejoin="round"/>')
        s.append(T(x0, y - 18, lab, 21, GRAY, anchor="start"))
    return W, H, "".join(s)


def box(x, y, w, h, fill, stroke, rx=12, sw=1.5):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')


def circ(cx, cy, r, fill, stroke="none", sw=0):
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke != "none" else ""
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"{st}/>'


# ---------- 目录卡 ----------
def toc():
    items = [
        ("1", "一个承诺：不开颅,把作用点送进丘脑", "它凭的是声波能聚焦"),
        ("2", "结果：脑电、行为、在线离线全为零", "关键的交互项 p = 0.763"),
        ("3", "会不会是没打够", "剂量与效应之间没有关系"),
        ("4", "会不会是没打中", "靶点、焦斑、导航误差都是 0.5 厘米"),
        ("5", "排完之后,剩下温度", "靶点温升被压在 0.5 摄氏度以内"),
        ("6", "这个结果否掉了什么", "以及没有否掉什么"),
    ]
    s = []; y = 26
    for n, title, sub in items:
        s.append(box(28, y, 904, 80, "#F7F9FC", "#DCE5F0", 14, 1.5))
        s.append(circ(76, y + 40, 26, TINT, ACC, 1.5))
        s.append(T(76, y + 50, n, 30, ACCD, weight="700"))
        s.append(T(126, y + 35, title, 29, INK, anchor="start", weight="700"))
        s.append(T(126, y + 65, sub, 22, GRAY, anchor="start"))
        y += 94
    return 960, y + 10, "".join(s)


# ---------- 颅骨三层：损耗主要发生在中间那层 ----------
def skull():
    s = []
    s.append(box(24, 20, 912, 54, TINT, ACC, 12, 1.5))
    s.append(T(480, 55, "损耗主要发生在中间那层多孔的骨", 27, ACCD, weight="700"))

    top, bot = 128, 372
    x1, x2, x3, x4 = 300, 362, 494, 556
    # 三层
    s.append(f'<rect x="{x1}" y="{top}" width="{x2-x1}" height="{bot-top}" '
             f'fill="#E4E8ED" stroke="#9AA4B0" stroke-width="2"/>')
    s.append(f'<rect x="{x2}" y="{top}" width="{x3-x2}" height="{bot-top}" '
             f'fill="#F6F1E4" stroke="#C9B98E" stroke-width="2"/>')
    s.append(f'<rect x="{x3}" y="{top}" width="{x4-x3}" height="{bot-top}" '
             f'fill="#E4E8ED" stroke="#9AA4B0" stroke-width="2"/>')
    # 板障的孔隙
    import random
    random.seed(7)
    for _ in range(58):
        cx = random.uniform(x2 + 10, x3 - 10)
        cy = random.uniform(top + 12, bot - 12)
        s.append(circ(round(cx, 1), round(cy, 1), round(random.uniform(4, 10), 1), "#FFFFFF",
                      "#C9B98E", 1.4))
    # 入射（粗）
    s.append(f'<line x1="70" y1="250" x2="{x1-6}" y2="250" stroke="{ACC}" '
             f'stroke-width="16" stroke-linecap="round"/>')
    s.append(T(178, 228, "入射", 24, ACCD, weight="700"))
    # 透射（细）
    s.append(f'<line x1="{x4+6}" y1="250" x2="890" y2="250" stroke="{ACC}" '
             f'stroke-width="5" stroke-linecap="round" opacity="0.85"/>')
    s.append(T(770, 228, "透射,明显减弱", 24, ACCD, weight="700"))
    # 板障内的散射
    for (ax, ay, bx, by) in [(400, 250, 452, 176), (404, 250, 448, 330),
                             (420, 240, 386, 158), (424, 262, 470, 344)]:
        s.append(f'<line x1="{ax}" y1="{ay}" x2="{bx}" y2="{by}" stroke="{RED}" '
                 f'stroke-width="2.6" marker-end="url(#ahr)"/>')
    # 层标注
    s.append(T((x1 + x2) / 2, bot + 32, "外板", 22, INK, weight="700"))
    s.append(T((x1 + x2) / 2, bot + 58, "皮质骨", 19, GRAY))
    s.append(T((x2 + x3) / 2, bot + 32, "板障", 22, "#8A7530", weight="700"))
    s.append(T((x2 + x3) / 2, bot + 58, "松质骨,多孔", 19, GRAY))
    s.append(T((x3 + x4) / 2, bot + 32, "内板", 22, INK, weight="700"))
    s.append(T((x3 + x4) / 2, bot + 58, "皮质骨", 19, GRAY))
    # 机制说明
    s.append(box(120, 468, 720, 92, "#FDF7F6", "#E3BDB6", 12, 1.5))
    s.append(T(480, 500, "散射：声波在孔隙微结构里方向被打乱", 23, RED))
    s.append(T(480, 532, "模式转换：纵波转成横波,基本不再有效传入脑内", 23, RED))
    return 960, 580, "".join(s)


FIGS = {"cover-concept": cover_concept, "toc": toc, "fig-skull": skull}


def render(name, w, h, inner):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
           f'viewBox="0 0 {w} {h}" font-family="HeitiSC,Helvetica,Arial,sans-serif">'
           f'{DEFS}<rect width="{w}" height="{h}" fill="#FFFFFF"/>{inner}</svg>')
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
