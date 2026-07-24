"""EEG 基线漂移 / 电极界面 first-principles schematics (series ② drift).
Self-made SVG diagrams, rendered to PNG via playwright chromium.
"""
import os, subprocess, tempfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "series-eeg-impedance-02-drift", "figs")
os.makedirs(OUT, exist_ok=True)

ACC = "#2F6DB5"; ACCD = "#1E4E86"; TINT = "#E9F0F8"
INK = "#1A1A1A"; BODY = "#4A4A4A"; GRAY = "#8A8A8A"; LINE = "#D6DBE2"
RED = "#C0392B"; REDT = "#F7E9E7"; GRN = "#2E7D57"; GRNT = "#E7F2EC"
CARD_L = "#DCE5F0"; CHIPF = "#F2F3F1"; CHIPL = "#DBDCD8"

DEFS = (
    '<defs>'
    '<marker id="ah" markerWidth="10" markerHeight="10" refX="8" refY="3" '
    'orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="%s"/></marker>'
    '<marker id="ahr" markerWidth="10" markerHeight="10" refX="8" refY="3" '
    'orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="%s"/></marker>'
    '<marker id="ahg" markerWidth="10" markerHeight="10" refX="8" refY="3" '
    'orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="%s"/></marker>'
    '</defs>' % (ACC, RED, GRAY)
)

def T(x, y, s, size=25, fill=INK, anchor="middle", weight="400"):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}">{s}</text>'

def box(x, y, w, h, fill, stroke, rx=12, sw=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

def line(x1,y1,x2,y2,stroke=INK,sw=2,dash=None,marker=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    m = f' marker-end="url(#{marker})"' if marker else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"{d}{m}/>'

def circ(cx, cy, r, fill, stroke, sw=1.5):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

# ---------- Cover TOC (used as a figure on cover area is separate; this is a standalone nav) ----------
def toc():
    s = []
    items = [
        ("1", "电极为什么不是导线", "界面自发长出一个电压"),
        ("2", "这个电压有多大", "为什么被差分抵消"),
        ("3", "它为什么随时间变", "漂移的根源"),
        ("4", "银-氯化银与导电膏", "怎样让电压稳"),
        ("5", "源头与后端各做什么", "配对、控环境、高通"),
        ("6", "对 ECG/EMG/可穿戴通用", "同一套界面物理"),
    ]
    y = 30
    for n, title, sub in items:
        s.append(box(30, y, 900, 78, "#F7F9FC", CARD_L, 14, 1.5))
        s.append(circ(78, y+39, 26, TINT, ACC, 1.5))
        s.append(T(78, y+49, n, 30, ACCD, weight="700"))
        s.append(T(126, y+34, title, 30, INK, anchor="start", weight="700"))
        s.append(T(126, y+64, sub, 22, GRAY, anchor="start"))
        y += 92
    return 960, y, "".join(s)

# ---------- Fig 3: double layer ----------
def fig_dl():
    s = []
    s.append(box(30, 24, 900, 58, TINT, ACC, 12, 1.5))
    s.append(T(480, 60, "金属泡进电解质:表面银原子溶成离子,电子留下,电荷分家", 24, ACCD, weight="700"))
    # metal block (left)
    s.append(box(90, 130, 320, 320, "#EDEFF2", "#B9C0C9", 12, 1.5))
    s.append(T(250, 120, "金属(银)", 24, INK))
    # electrolyte (right)
    s.append(box(560, 130, 320, 320, "#EAF3FA", ACC, 12, 1.2))
    s.append(T(720, 120, "电解质(导电膏/汗液)", 22, ACCD))
    # interface line
    s.append(line(485, 130, 485, 450, GRAY, 2, "6,5"))
    s.append(T(485, 476, "界面", 20, GRAY))
    # electrons on metal side (negative)
    for i,yy in enumerate([190,250,310,370,420]):
        s.append(circ(455, yy, 13, REDT, RED, 1.2)); s.append(T(455, yy+6, "−", 20, RED))
    # Ag+ ions on solution side (positive)
    for i,yy in enumerate([190,250,310,370,420]):
        s.append(circ(515, yy, 13, "#E7F0FA", ACC, 1.2)); s.append(T(515, yy+6, "+", 18, ACC))
    # an ion migrating
    s.append(circ(620, 240, 15, "#E7F0FA", ACC, 1.2)); s.append(T(620, 246, "Ag+", 16, ACC))
    s.append(line(500, 300, 600, 250, ACC, 2, None, "ah"))
    s.append(T(650, 300, "少数银原子", 20, BODY, anchor="start"))
    s.append(T(650, 328, "溶成 Ag+ 进入溶液", 20, BODY, anchor="start"))
    s.append(T(650, 356, "电子留在金属", 20, BODY, anchor="start"))
    s.append(T(250, 486, "金属侧偏负", 22, RED))
    s.append(T(720, 486, "溶液侧偏正", 22, ACC))
    s.append(T(480, 520, "正负相对排开 = 双电层", 24, INK, weight="700"))
    return 960, 545, "".join(s)

# ---------- Fig 5: magnitude ----------
def fig_mag():
    s = []
    s.append(box(30, 24, 900, 58, TINT, ACC, 12, 1.5))
    s.append(T(480, 60, "界面半电池电位约 0.22 V,比脑电大上万倍——靠差分抵消", 24, ACCD, weight="700"))
    base = 430
    def bar(cx, h, fill, stroke, top, sub):
        y = base - h
        s.append(box(cx-75, y, 150, h, fill, stroke, 8, 1.5))
        s.append(T(cx, y-16, top, 28, stroke, weight="700"))
        s.append(T(cx, base+34, sub, 21, BODY))
    bar(230, 55, GRNT, GRN, "10–100 µV", "头皮脑电")
    bar(560, 300, REDT, RED, "≈ 0.22 V", "单个电极半电池电位")
    s.append(line(120, base, 700, base, LINE, 2))
    # differential cancel note
    s.append(box(740, 150, 200, 200, "#F7F9FC", CARD_L, 12, 1.5))
    s.append(T(840, 185, "差分", 24, ACCD, weight="700"))
    s.append(T(840, 230, "两端各 0.22V", 20, BODY))
    s.append(T(840, 262, "相等则相减", 20, BODY))
    s.append(T(840, 300, "= 0", 30, GRN, weight="700"))
    s.append(T(480, 500, "两端相等→抵消;两端不等且随时间变→差值成为漂移", 22, GRAY))
    return 960, 530, "".join(s)

# ---------- Fig 7: drift mechanism ----------
def fig_drift():
    s = []
    s.append(box(30, 24, 900, 58, TINT, ACC, 12, 1.5))
    s.append(T(480, 60, "半电池电位由 Cl⁻ 浓度与温度锚定,三个因素推动它移动", 24, ACCD, weight="700"))
    # three drivers -> anchor
    drivers = [("出汗","汗含 NaCl,加氯离子\n改变浓度"),
               ("蒸发","导电膏失水\nCl⁻ 浓度升高"),
               ("温度","直接移动\n溶出/回沉平衡点")]
    xs = [80, 380, 680]
    for i,(t,d) in enumerate(drivers):
        s.append(box(xs[i], 120, 200, 110, REDT, RED, 12, 1.5))
        s.append(T(xs[i]+100, 158, t, 26, RED, weight="700"))
        for j,ln in enumerate(d.split("\n")):
            s.append(T(xs[i]+100, 190+j*26, ln, 19, BODY))
        s.append(line(xs[i]+100, 230, 480, 300, RED, 2, "5,4", "ahr"))
    # anchor box
    s.append(box(330, 300, 300, 76, TINT, ACC, 12, 1.5))
    s.append(T(480, 332, "半电池电位(锚点)", 24, ACCD, weight="700"))
    s.append(T(480, 360, "被推移", 20, ACC))
    # drifting baseline
    s.append(line(120, 460, 840, 460, LINE, 1.5))
    path = "M120,455 C260,450 300,470 430,462 C560,454 620,485 760,478 C800,476 820,482 840,485"
    s.append(f'<path d="{path}" fill="none" stroke="{RED}" stroke-width="3"/>')
    s.append(T(480, 512, "两电极不同步移动 → 差值成为缓慢爬升的基线(漂移)", 22, GRAY))
    return 960, 535, "".join(s)

# ---------- Fig 8: polarizable vs non-polarizable ----------
def fig_pol():
    s = []
    s.append(box(30, 24, 900, 58, TINT, ACC, 12, 1.5))
    s.append(T(480, 60, "电荷能不能穿过界面,决定界面电位稳不稳", 24, ACCD, weight="700"))
    # left: polarizable
    s.append(box(60, 120, 400, 340, REDT, RED, 14, 1.5))
    s.append(T(260, 158, "极化电极(金、铂)", 26, RED, weight="700"))
    s.append(T(260, 190, "电荷穿不过界面", 21, BODY))
    # interface with pileup
    s.append(line(260, 210, 260, 400, GRAY, 2, "5,4"))
    for yy in [240,270,300,330,360]:
        s.append(circ(235, yy, 11, "#FFFFFF", RED, 1.2)); s.append(T(235, yy+5, "−", 16, RED))
    s.append(line(150, 300, 218, 300, RED, 2.5, None, "ahr"))
    s.append(T(150, 285, "电流", 18, BODY, anchor="middle"))
    s.append(T(260, 428, "堆积在双电层 → 电位被推动", 20, RED, weight="700"))
    # right: non-polarizable
    s.append(box(500, 120, 400, 340, GRNT, GRN, 14, 1.5))
    s.append(T(700, 158, "非极化(银-氯化银)", 26, GRN, weight="700"))
    s.append(T(700, 190, "电荷经反应穿过界面", 21, BODY))
    s.append(line(700, 210, 700, 400, GRAY, 2, "5,4"))
    s.append(line(600, 300, 800, 300, GRN, 2.5, None, "ahg"))
    s.append(T(700, 340, "Ag + Cl⁻ ⇌ AgCl + e⁻", 22, GRN, weight="700"))
    s.append(T(700, 428, "不堆积 → 电位不动(稳)", 20, GRN, weight="700"))
    return 960, 480, "".join(s)

# ---------- Fig 13: frequency axis / highpass ----------
def fig_hp():
    s = []
    s.append(box(30, 24, 900, 58, TINT, ACC, 12, 1.5))
    s.append(T(480, 60, "漂移是贴近 0 Hz 的低频;高通挡低频、留脑电", 24, ACCD, weight="700"))
    # frequency axis
    ax_y = 340
    s.append(line(90, ax_y, 890, ax_y, INK, 2, None, "ah"))
    s.append(T(895, ax_y+28, "频率", 20, INK, anchor="start"))
    for x,lab in [(120,"0 Hz"),(300,"0.1"),(470,"1"),(640,"10"),(800,"40 Hz")]:
        s.append(line(x, ax_y-6, x, ax_y+6, GRAY, 1.5))
        s.append(T(x, ax_y+28, lab, 18, GRAY))
    # drift region (low)
    s.append(box(95, 200, 150, 130, REDT, RED, 8, 1.2))
    s.append(T(170, 250, "漂移", 24, RED, weight="700"))
    s.append(T(170, 285, "贴近 0Hz", 18, BODY))
    # EEG region
    s.append(box(360, 200, 480, 130, GRNT, GRN, 8, 1.2))
    s.append(T(600, 240, "脑电节律", 24, GRN, weight="700"))
    s.append(T(600, 275, "delta 1–4 · alpha 8–13 · beta · gamma", 19, BODY))
    # cutoff line
    s.append(line(300, 150, 300, ax_y, ACC, 2.5, "6,4"))
    s.append(T(300, 138, "高通截止 ~0.1Hz", 20, ACCD, weight="700"))
    s.append(T(300, 400, "以下削掉", 18, RED))
    s.append(T(600, 400, "以上保留", 18, GRN))
    # caveat
    s.append(box(120, 430, 720, 70, "#FBF7E9", "#D9C98A", 12, 1.5))
    s.append(T(480, 462, "代价:delta 与慢 ERP 紧邻漂移,截止设太高会连真信号一起削掉", 21, "#8A6D1A"))
    s.append(T(480, 488, "所以只能兜底——源头做好,后端才少伤真信号", 21, "#8A6D1A"))
    return 960, 520, "".join(s)

FIGS = {"toc": toc, "fig-doublelayer": fig_dl, "fig-magnitude": fig_mag,
        "fig-drift": fig_drift, "fig-polarization": fig_pol, "fig-highpass": fig_hp}

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
    subprocess.run(["npx","playwright","screenshot",f"file://{tmp.name}",out,
                    f"--viewport-size={w},{h}","--wait-for-timeout=600"],
                   check=True, capture_output=True, text=True)
    os.unlink(tmp.name)
    return out

if __name__ == "__main__":
    for name, fn in FIGS.items():
        w,h,inner = fn()
        p = render(name, w, h, inner)
        print("rendered", p, f"({w}x{h})")
