"""EEG 工频干扰 first-principles schematics (series ① line-noise).
Self-made SVG diagrams, rendered to PNG via playwright chromium.
"""
import os, subprocess, tempfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "series-eeg-impedance-01-linenoise", "figs")
os.makedirs(OUT, exist_ok=True)

ACC = "#2F6DB5"; ACCD = "#1E4E86"; TINT = "#E9F0F8"
INK = "#1A1A1A"; BODY = "#4A4A4A"; GRAY = "#8A8A8A"; LINE = "#D6DBE2"
RED = "#C0392B"; REDT = "#F7E9E7"; GRN = "#2E7D57"; GRNT = "#E7F2EC"
CHIPF = "#F2F3F1"; CHIPL = "#DBDCD8"

DEFS = (
    '<defs>'
    '<marker id="ah" markerWidth="10" markerHeight="10" refX="8" refY="3" '
    'orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="%s"/></marker>'
    '<marker id="ahr" markerWidth="10" markerHeight="10" refX="8" refY="3" '
    'orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="%s"/></marker>'
    '</defs>' % (ACC, RED)
)

def T(x, y, s, size=25, fill=INK, anchor="middle", weight="400"):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}">{s}</text>'

def box(x, y, w, h, fill, stroke, rx=12, sw=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

def line(x1,y1,x2,y2,stroke=INK,sw=2,dash=None,marker=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    m = f' marker-end="url(#{marker})"' if marker else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"{d}{m}/>'

def cap(cx, cy, label, sub=None):
    """capacitor symbol (two horizontal plates), vertical orientation."""
    s = [line(cx-26, cy-6, cx+26, cy-6, INK, 3),
         line(cx-26, cy+6, cx+26, cy+6, INK, 3),
         T(cx+70, cy-2, label, 22, ACCD, weight="700")]
    if sub:
        s.append(T(cx+70, cy+22, sub, 18, GRAY))
    return "".join(s)

# ---------- Fig 3: 电容耦合 ----------
def fig3():
    s = []
    s.append(box(30, 26, 900, 60, TINT, ACC, 12, 1.5))
    s.append(T(480, 63, "墙里的火线并未与你相连,却隔着电容把干扰灌进身体", 26, ACCD, weight="700"))
    # mains line (left vertical bar)
    s.append(box(70, 130, 70, 330, REDT, RED, 10, 1.5))
    s.append(T(105, 300, "火", 40, RED, weight="700"))
    s.append(T(105, 345, "线", 40, RED, weight="700"))
    s.append(T(105, 500, "220V · 50Hz", 22, RED))
    # body (center)
    s.append(box(420, 150, 130, 290, CHIPF, CHIPL, 16, 1.5))
    s.append(T(485, 300, "人", 44, INK, weight="700"))
    s.append(T(485, 350, "体", 44, INK, weight="700"))
    # ground (bottom bar)
    s.append(box(360, 470, 250, 6, INK, INK, 0, 0))
    s.append(line(400,476,420,496,INK,2)); s.append(line(440,476,460,496,INK,2))
    s.append(line(480,476,500,496,INK,2)); s.append(line(520,476,540,496,INK,2))
    s.append(line(560,476,580,496,INK,2))
    s.append(T(485, 520, "大地", 22, GRAY))
    # C1 火线->人体 (small)
    s.append(cap(255, 250, "C₁ 火线–人体", "几 pF · 容抗极大"))
    s.append(line(140, 250, 229, 250, ACC, 2.5, "5,4"))
    s.append(line(281, 250, 420, 250, ACC, 2.5, "5,4", "ah"))
    # C2 人体->地 (large) — sublabel shifted right to avoid overlap with ground
    s.append(line(459, 449, 511, 449, INK, 3))
    s.append(line(459, 461, 511, 461, INK, 3))
    s.append(T(560, 447, "C₂ 人体–地", 20, ACCD, weight="700", anchor="start"))
    s.append(T(560, 468, "几百 pF", 16, GRAY, anchor="start"))
    s.append(line(485, 440, 485, 448, ACC, 2.5))
    # formula box — clean fraction layout
    s.append(box(620, 150, 310, 260, "#F7F9FC", CARD_L, 14, 1.5))
    s.append(T(775, 192, "人体电位(浮空时)", 24, ACCD, weight="700"))
    s.append(T(700, 258, "V = 220 ×", 30, INK, anchor="middle"))
    s.append(T(838, 240, "C₁", 26, ACCD, weight="700"))
    s.append(line(812, 254, 866, 254, INK, 2))
    s.append(T(838, 280, "C₁+C₂", 24, ACCD, weight="700"))
    s.append(T(775, 345, "离电线越远 → C₁ 越小", 21, BODY))
    s.append(T(775, 375, "→ 人体电位越低", 21, BODY))
    return 960, 560, "".join(s)

CARD_L = "#DCE5F0"

# ---------- Fig 5: 量级悬殊 ----------
def fig5():
    s = []
    s.append(box(30, 26, 900, 60, TINT, ACC, 12, 1.5))
    s.append(T(480, 63, "浮空人体上的工频干扰,比要测的脑电大十万倍", 26, ACCD, weight="700"))
    # log axis bars
    base = 470
    def bar(cx, h, fill, stroke, top, sub):
        y = base - h
        s.append(box(cx-70, y, 140, h, fill, stroke, 8, 1.5))
        s.append(T(cx, y-16, top, 30, stroke, weight="700"))
        s.append(T(cx, base+34, sub, 22, BODY))
    bar(200, 60, GRNT, GRN, "10–100 µV", "头皮脑电")
    bar(480, 300, REDT, RED, "≈ 几十 V", "浮空人体(无 GND)")
    bar(760, 150, TINT, ACC, "≈ 20 mV", "接 GND 后残余")
    s.append(line(120, base, 850, base, LINE, 2))
    s.append(T(480, 548, "µV → mV → V 每格差 1000 倍 · 纵轴为对数尺度示意", 22, GRAY))
    return 960, 570, "".join(s)

# ---------- Fig 6: 两条泄放路 ----------
def fig6():
    s = []
    s.append(box(30, 26, 900, 60, TINT, ACC, 12, 1.5))
    s.append(T(480, 63, "接 GND 不消除电流,是给它开一条低阻旁路", 26, ACCD, weight="700"))
    # body node
    s.append(box(410, 120, 140, 80, CHIPF, CHIPL, 14, 1.5))
    s.append(T(480, 155, "人体", 30, INK, weight="700"))
    s.append(T(480, 185, "I ≈ 3.8 µA", 20, RED))
    # path A: to ground via 10M
    s.append(line(430, 200, 250, 320, GRAY, 2.5, "6,4", "ah"))
    s.append(box(150, 320, 200, 66, "#FBFAF7", CHIPL, 12, 1.5))
    s.append(T(250, 350, "老路 · 对地电容", 22, BODY))
    s.append(T(250, 376, "≈ 10 MΩ", 24, GRAY, weight="700"))
    s.append(T(250, 440, "V = 3.8µA×10MΩ", 22, BODY))
    s.append(T(250, 470, "≈ 38 V", 30, GRAY, weight="700"))
    # path B: GND via 5k
    s.append(line(530, 200, 710, 320, ACC, 3, None, "ah"))
    s.append(box(610, 320, 200, 66, TINT, ACC, 12, 1.5))
    s.append(T(710, 350, "新路 · GND 电极", 22, ACCD, weight="700"))
    s.append(T(710, 376, "≈ 5 kΩ", 24, ACCD, weight="700"))
    s.append(T(710, 440, "V = 3.8µA×5kΩ", 22, ACCD))
    s.append(T(710, 470, "≈ 20 mV", 30, ACCD, weight="700"))
    s.append(T(480, 512, "电流优先走小阻抗的路 → 人体从 38V 塌到 20mV(差 2000 倍)", 22, GRAY))
    return 960, 545, "".join(s)

# ---------- Fig 10: 共模漏成差模 ----------
def fig10():
    s = []
    s.append(box(30, 26, 900, 58, TINT, ACC, 12, 1.5))
    s.append(T(480, 62, "两电极阻抗不等 → 同一个共模被分掉不同比例 → 相减不为零", 24, ACCD, weight="700"))
    # common mode source
    s.append(T(480, 120, "人体共模 V_cm ≈ 20 mV(两电极处相同)", 24, RED, weight="700"))
    # electrode A
    s.append(box(120, 160, 210, 70, CHIPF, CHIPL, 12, 1.5))
    s.append(T(225, 195, "电极 A", 24, INK, weight="700"))
    s.append(T(225, 220, "接触阻抗 Z_A", 20, BODY))
    # electrode R
    s.append(box(630, 160, 210, 70, CHIPF, CHIPL, 12, 1.5))
    s.append(T(735, 195, "参考电极 R", 24, INK, weight="700"))
    s.append(T(735, 220, "接触阻抗 Z_R", 20, BODY))
    # arrows to amp
    s.append(line(225, 230, 380, 300, ACC, 2.5, None, "ah"))
    s.append(line(735, 230, 580, 300, ACC, 2.5, None, "ah"))
    # amp box
    s.append(box(360, 300, 240, 70, TINT, ACC, 12, 1.5))
    s.append(T(480, 332, "差分放大器", 24, ACCD, weight="700"))
    s.append(T(480, 358, "V_A − V_R", 20, ACC))
    # formula
    s.append(box(150, 400, 660, 130, "#F7F9FC", CARD_L, 14, 1.5))
    s.append(T(480, 445, "V_diff ≈ V_cm × (Z_A − Z_R) / Z_in", 32, INK, weight="700"))
    s.append(T(480, 490, "Z_A = Z_R → 差为 0 → 一点不漏", 23, GRN, weight="700"))
    s.append(T(480, 518, "Z_A ≠ Z_R → 残差正比于两者之差 → 漏成差模", 23, RED, weight="700"))
    return 960, 560, "".join(s)

# ---------- Fig 11: 齐 vs 低 ----------
def fig11():
    s = []
    s.append(box(30, 26, 900, 58, TINT, ACC, 12, 1.5))
    s.append(T(480, 62, "决定漏出的是阻抗之差,不是阻抗之低", 26, ACCD, weight="700"))
    # scenario 1
    s.append(box(70, 120, 380, 300, GRNT, GRN, 16, 1.5))
    s.append(T(260, 165, "两个都 10 kΩ · 相等", 26, GRN, weight="700"))
    s.append(box(120, 200, 110, 130, "#FFFFFF", GRN, 8, 1.5))
    s.append(T(175, 270, "10 kΩ", 24, INK, weight="700"))
    s.append(box(290, 200, 110, 130, "#FFFFFF", GRN, 8, 1.5))
    s.append(T(345, 270, "10 kΩ", 24, INK, weight="700"))
    s.append(T(260, 372, "Z_A − Z_R = 0", 26, GRN, weight="700"))
    s.append(T(260, 405, "残差 = 0 · 不漏", 24, GRN))
    # scenario 2
    s.append(box(510, 120, 380, 300, REDT, RED, 16, 1.5))
    s.append(T(700, 165, "把一个降到 2 kΩ · 另一个 10 kΩ", 22, RED, weight="700"))
    s.append(box(560, 260, 110, 70, "#FFFFFF", RED, 8, 1.5))
    s.append(T(615, 305, "2 kΩ", 24, INK, weight="700"))
    s.append(box(730, 200, 110, 130, "#FFFFFF", RED, 8, 1.5))
    s.append(T(785, 270, "10 kΩ", 24, INK, weight="700"))
    s.append(T(700, 372, "Z_A − Z_R = 8 kΩ", 26, RED, weight="700"))
    s.append(T(700, 405, "残差反而更大 · 漏更多", 24, RED))
    s.append(T(480, 465, "把单个电极拼命降到最低,若拉大了通道间的差,是帮倒忙", 24, BODY))
    return 960, 500, "".join(s)

FIGS = {"fig3-coupling": fig3, "fig5-magnitude": fig5, "fig6-gnd-path": fig6,
        "fig10-leak": fig10, "fig11-match": fig11}

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
