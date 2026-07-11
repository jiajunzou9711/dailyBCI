"""Methodology piece — 神经解码四轴 first-principles schematics.
Self-made SVG diagrams (series track), rendered to PNG via playwright chromium.
"""
import os, subprocess, tempfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))      # .claude/skills/dailybci
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "series-decoding-four-axes", "figs")
os.makedirs(OUT, exist_ok=True)

ACC = "#2F6DB5"; ACCD = "#1E4E86"; TINT = "#E9F0F8"
INK = "#1A1A1A"; BODY = "#4A4A4A"; GRAY = "#8A8A8A"; LINE = "#D6DBE2"
CARDF = "#F7F9FC"; CARDL = "#DCE5F0"; CHIPF = "#F2F3F1"; CHIPL = "#DBDCD8"

DEFS = (
    '<defs><marker id="ah" markerWidth="10" markerHeight="10" refX="8" refY="3" '
    'orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="%s"/></marker>'
    '<marker id="ahg" markerWidth="10" markerHeight="10" refX="8" refY="3" '
    'orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="%s"/></marker></defs>' % (ACC, GRAY)
)

def T(x, y, s, size=25, fill=INK, anchor="middle", weight="400"):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}">{s}</text>'

def box(x, y, w, h, fill, stroke, rx=12, sw=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

# ---------- Fig 0: four-axis overview ----------
def fig0():
    cols = [("A 信号模态","从什么信号读"),("B 解码目标","读出什么对象"),
            ("C 编码层级","信息住在哪层"),("D 模型类别","映射什么形式")]
    chips = [["侵入 · 皮层内","ECoG · 皮层表面","EEG · 头皮","fMRI · 血氧"],
             ["连续 → 回归","离散 → 分类","序列 → 文本","重建 → 生成"],
             ["单神经元 · 调谐","群体 · 流形"],
             ["线性","非线性"]]
    xs = [30, 255, 480, 705]; w = 210; cx = [x + w/2 for x in xs]
    s = []
    for i,(t,sub) in enumerate(cols):
        s.append(box(xs[i], 24, w, 66, TINT, ACC, 12, 1.5))
        s.append(T(cx[i], 54, t, 27, ACCD, weight="700"))
        s.append(T(cx[i], 80, sub, 20, ACC))
    for i,col in enumerate(chips):
        for j,c in enumerate(col):
            y = 106 + j*70
            s.append(box(xs[i], y, w, 56, CHIPF, CHIPL, 10, 1.2))
            s.append(T(cx[i], y+35, c, 24, BODY))
    s.append(T(480, 415, "任何解码器 = 四条轴上各取一个点 · 四轴互相独立、自由组合", 25, GRAY))
    return 960, 440, "".join(s)

# ---------- Fig A: distance -> resolution gradient ----------
def figA():
    s = []
    s.append(T(480, 40, "电活动这一支:离神经元越远 → 从单神经元退到大群体", 26, INK, weight="700"))
    s.append(f'<line x1="80" y1="72" x2="884" y2="72" stroke="{ACC}" stroke-width="3" marker-end="url(#ah)"/>')
    cards = [("皮层内微电极","空间 ~50–150 µm","编码层:单神经元"),
             ("ECoG 皮层表面","空间 ~1–5 mm","编码层:局部群体"),
             ("EEG 头皮","空间 ~cm","编码层:大群体")]
    xs = [70, 355, 640]; w = 250
    for i,(a,b,c) in enumerate(cards):
        x = xs[i]; cxv = x + w/2
        s.append(box(x, 100, w, 188, CARDF, CARDL, 14, 1.5))
        s.append(T(cxv, 148, a, 27, ACCD, weight="700"))
        s.append(f'<line x1="{x+30}" y1="170" x2="{x+w-30}" y2="170" stroke="{CARDL}" stroke-width="1.5"/>')
        s.append(T(cxv, 210, b, 25, BODY))
        s.append(T(cxv, 256, c, 25, BODY))
    s.append(box(70, 322, 820, 96, CHIPF, CHIPL, 14, 1.2))
    s.append(T(480, 360, "另一支 · 血流(fMRI / fNIRS / fUS):空间可细到 µm–mm,", 24, BODY))
    s.append(T(480, 394, "但时间被血流响应锁在 ~秒级 —— 所以做不了快速实时控制", 24, BODY))
    return 960, 450, "".join(s)

# ---------- Fig B: regression vs classification ----------
def figB():
    s = []
    # left panel
    s.append(box(40, 28, 420, 350, "#FCFCFB", CHIPL, 14, 1.2))
    s.append(T(250, 64, "回归 · 输出有度量", 27, ACCD, weight="700"))
    s.append(f'<line x1="95" y1="200" x2="420" y2="200" stroke="{GRAY}" stroke-width="2"/>')
    for tx in [95,160,225,290,355,420]:
        s.append(f'<line x1="{tx}" y1="194" x2="{tx}" y2="206" stroke="{GRAY}" stroke-width="2"/>')
    s.append(f'<circle cx="225" cy="200" r="8" fill="{GRAY}"/>')
    s.append(f'<circle cx="340" cy="200" r="8" fill="{ACC}"/>')
    s.append(T(225, 240, "ŷ 预测", 22, GRAY))
    s.append(T(340, 240, "y 真值", 22, ACCD))
    s.append(f'<line x1="225" y1="165" x2="340" y2="165" stroke="{ACC}" stroke-width="2" marker-end="url(#ah)" marker-start="url(#ah)"/>')
    s.append(T(282, 152, "‖y − ŷ‖ 距离", 22, ACCD))
    s.append(T(250, 300, "能说『差多远』", 24, INK, weight="700"))
    s.append(T(250, 336, "→ 用距离打分(平方误差)", 23, BODY))
    # right panel
    s.append(box(500, 28, 420, 350, "#FCFCFB", CHIPL, 14, 1.2))
    s.append(T(710, 64, "分类 · 标签无度量", 27, ACCD, weight="700"))
    labs = [("左",560),("右",690),("其他",820)]
    for t,x in labs:
        s.append(box(x-40, 84, 80, 48, CHIPF, CHIPL, 10, 1.2))
        s.append(T(x, 115, t, 24, BODY))
    s.append(T(710, 162, "标签之间没有距离", 22, GRAY))
    # prob bars
    base = 300; bx = [560,690,820]; bh = [38,128,64]; bl=["左","右","其他"]
    for i,x in enumerate(bx):
        col = ACC if i==1 else "#C4D4E8"
        s.append(f'<rect x="{x-32}" y="{base-bh[i]}" width="64" height="{bh[i]}" rx="6" fill="{col}"/>')
        s.append(T(x, base+26, bl[i], 22, BODY))
    s.append(T(755, 200, "信心", 20, ACCD))
    s.append(T(710, 362, "→ 量压在真标签上的概率(交叉熵)", 23, BODY))
    # bottom unifying strip
    s.append(box(40, 398, 880, 86, TINT, ACC, 14, 1.5))
    s.append(T(480, 432, "同一原理:估计 p(y|x),最大化对真答案的信心(极大似然)", 25, ACCD, weight="700"))
    s.append(T(480, 466, "回归的『距离』= 高斯噪声下『信心』的特例 · 一个原理两副面孔", 23, ACCD))
    return 960, 504, "".join(s)

# ---------- Fig C: two coexisting levels (single-neuron tuning & population manifold) ----------
def figC():
    s = []
    # left panel: single-neuron tuning
    s.append(box(40, 28, 420, 358, "#FCFCFB", CHIPL, 14, 1.2))
    s.append(T(250, 60, "单神经元 · 调谐", 26, ACCD, weight="700"))
    s.append(f'<line x1="110" y1="300" x2="110" y2="112" stroke="{GRAY}" stroke-width="2" marker-end="url(#ahg)"/>')
    s.append(f'<line x1="110" y1="300" x2="430" y2="300" stroke="{GRAY}" stroke-width="2" marker-end="url(#ahg)"/>')
    s.append(T(150, 108, "放电率", 18, GRAY, anchor="start"))
    s.append(T(408, 324, "刺激方向", 18, GRAY, anchor="end"))
    s.append(f'<path d="M122,292 Q270,118 418,292" fill="none" stroke="{ACCD}" stroke-width="3"/>')
    s.append(f'<circle cx="270" cy="205" r="6" fill="{ACC}"/>')
    s.append(T(270, 188, "偏好方向", 19, ACCD))
    s.append(T(250, 350, "加权求和(群体矢量)即可解码", 22, BODY))
    s.append(T(250, 380, "V1 朝向 / M1 方向 · 历史奠基", 22, BODY))
    # right panel: population manifold
    s.append(box(500, 28, 420, 358, "#FCFCFB", CHIPL, 14, 1.2))
    s.append(T(710, 60, "群体 · 低维流形", 26, ACCD, weight="700"))
    s.append(T(710, 110, "整群瞬时活动 = N 维空间一个点", 21, BODY))
    s.append(f'<path d="M575,288 C660,205 805,205 885,260 C805,325 660,335 575,288 Z" fill="{TINT}" stroke="{ACC}" stroke-width="2"/>')
    s.append(f'<path d="M600,278 C670,236 775,238 858,262" fill="none" stroke="{ACCD}" stroke-width="3"/>')
    for (px,py) in [(600,278),(662,250),(725,240),(795,245),(858,262)]:
        s.append(f'<circle cx="{px}" cy="{py}" r="5" fill="{ACCD}"/>')
    s.append(T(728, 190, "低维流形", 22, ACCD, weight="700"))
    s.append(T(710, 358, "因神经元高度相关而被压低维", 22, BODY))
    # bottom balanced caption
    s.append(T(480, 422, "两层都真实、互补;能否下到单神经元层,取决于模态(需皮层内)与脑区——", 24, BODY))
    s.append(T(480, 454, "非侵入信号物理上只能停在群体层。", 24, BODY))
    return 960, 478, "".join(s)

# ---------- Fig D: do you even need nonlinearity, and where does it live ----------
def figD():
    s = []
    def node(x,y,w,h,lines,fill,stroke,tc=BODY):
        r = [box(x,y,w,h,fill,stroke,12,1.5)]
        n=len(lines); cyv=y+h/2
        for i,ln in enumerate(lines):
            r.append(T(x+w/2, cyv-(n-1)*14+i*28+7, ln, 21, tc))
        return "".join(r)
    def arrow(x1,x2,y):
        return f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{ACC}" stroke-width="2.5" marker-end="url(#ah)"/>'
    h = 60
    # row 1 — no nonlinearity needed
    s.append(T(40, 52, "① 已线性可读 → 不需要非线性变换", 24, ACCD, anchor="start", weight="700"))
    y = 66
    s.append(node(40,y,200,h,["原始特征","(如发放率)"],CHIPF,CHIPL))
    s.append(arrow(245,300,y+h/2))
    s.append(node(305,y,200,h,["线性解码器","(直接读)"],CHIPF,CHIPL))
    s.append(arrow(510,565,y+h/2))
    s.append(T(615,y+h/2+7,"输出",23,INK))
    # row 2 — nonlinearity in the feature transform
    s.append(T(40, 188, "② 信息藏在高阶结构 → 非线性住『特征』里", 24, ACCD, anchor="start", weight="700"))
    y = 202
    s.append(node(40,y,185,h,["原始信号","(如 EEG)"],CHIPF,CHIPL))
    s.append(arrow(230,278,y+h/2))
    s.append(node(283,y,255,h,["固定非线性变换","算功率 / 协方差"],TINT,ACC,ACCD))
    s.append(arrow(543,591,y+h/2))
    s.append(node(596,y,165,h,["线性分类器"],CHIPF,CHIPL))
    s.append(arrow(766,814,y+h/2))
    s.append(T(862,y+h/2+7,"输出",23,INK))
    # row 3 — nonlinearity in the trained model
    s.append(T(40, 324, "③ 非线性住『模型』里", 24, ACCD, anchor="start", weight="700"))
    y = 338
    s.append(node(40,y,185,h,["原始信号"],CHIPF,CHIPL))
    s.append(arrow(230,288,y+h/2))
    s.append(node(293,y,250,h,["非线性网络(训练)"],TINT,ACC,ACCD))
    s.append(arrow(548,596,y+h/2))
    s.append(T(644,y+h/2+7,"输出",23,INK))
    # note
    s.append(box(40,418,880,72,TINT,ACC,14,1.5))
    s.append(T(480,452,"先问:需不需要非线性?信息已线性可读就不必(①);",24,ACCD))
    s.append(T(480,480,"需要时,它可住在固定特征变换(②)或训练模型(③)里。",24,ACCD))
    return 960, 510, "".join(s)

FIGS = {"fig0-overview": fig0, "figA-gradient": figA, "figB-reg-vs-clf": figB,
        "figC-manifold": figC, "figD-nonlinearity": figD}

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
