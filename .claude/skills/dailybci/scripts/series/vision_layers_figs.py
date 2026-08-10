"""视觉通路分层 / 各层解决程度 示意图(第一期:谁真正需要脑机接口)。
Self-made SVG diagrams, rendered to PNG via playwright chromium.
"""
import os, subprocess, tempfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-08-10-vision-layers", "figs")
os.makedirs(OUT, exist_ok=True)

ACC = "#2F6DB5"; ACCD = "#1E4E86"; TINT = "#E9F0F8"
INK = "#1A1A1A"; BODY = "#4A4A4A"; GRAY = "#8A8A8A"; LINE = "#D6DBE2"
RED = "#C0392B"; REDT = "#F7E9E7"; GRN = "#2E7D57"; GRNT = "#E7F2EC"
AMB = "#8A6D1A"; AMBT = "#FBF7E9"; AMBL = "#D9C98A"
CARD_L = "#DCE5F0"; NEU = "#EDEFF2"; NEUL = "#C9CFD6"

DEFS = (
    '<defs>'
    '<marker id="ah" markerWidth="10" markerHeight="10" refX="8" refY="3" '
    'orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="%s"/></marker>'
    '<marker id="ahg" markerWidth="10" markerHeight="10" refX="8" refY="3" '
    'orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="%s"/></marker>'
    '</defs>' % (ACC, GRAY)
)

def T(x, y, s, size=25, fill=INK, anchor="middle", weight="400"):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" font-weight="{weight}">{s}</text>')

def box(x, y, w, h, fill, stroke, rx=12, sw=1.5):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

def line(x1, y1, x2, y2, stroke=INK, sw=2, dash=None, marker=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    m = f' marker-end="url(#{marker})"' if marker else ""
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" '
            f'stroke-width="{sw}"{d}{m}/>')

def circ(cx, cy, r, fill, stroke, sw=1.5):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw}"/>')


# ---------- F1: 目录 ----------
def toc():
    s = []
    items = [
        ("1", "一块视网膜下芯片做到了什么", "当下最好的成绩,和它的前提"),
        ("2", "3360 万盲人的病因分布", "一半以上已经能治"),
        ("3", "坏的部位不在同一处", "从角膜到视神经的定位"),
        ("4", "越往通路内侧,办法越少", "生物学疗法都要求细胞还活着"),
        ("5", "眼外伤", "唯一不限于单层的病因"),
        ("6", "视神经与外侧膝状体", "至今空白的两站"),
        ("7", "只剩初级视皮层", "适应症最宽,代价也最大"),
    ]
    y = 30
    for n, title, sub in items:
        s.append(box(30, y, 900, 78, "#F7F9FC", CARD_L, 14, 1.5))
        s.append(circ(78, y + 39, 26, TINT, ACC, 1.5))
        s.append(T(78, y + 49, n, 30, ACCD, weight="700"))
        s.append(T(126, y + 34, title, 30, INK, anchor="start", weight="700"))
        s.append(T(126, y + 64, sub, 22, GRAY, anchor="start"))
        y += 92
    return 960, y, "".join(s)


# ---------- F2: 病因分布条形图 ----------
def fig_causes():
    s = []
    s.append(box(30, 22, 900, 62, TINT, ACC, 12, 1.5))
    s.append(T(480, 50, "全球 50 岁及以上盲人 3360 万的病因拆分", 26, ACCD, weight="700"))
    s.append(T(480, 74, "绿色 = 已有成熟解决办法", 21, GRN))

    rows = [
        ("白内障",        1520, "45.2%", GRN,  GRNT),
        ("其他 / 未指明",  984, "29.3%", GRAY, "#F0F1F2"),
        ("青光眼",         360, "10.7%", RED,  REDT),
        ("未矫正屈光不正",  230, "6.8%",  GRN,  GRNT),
        ("黄斑变性",       180, "5.4%",  AMB,  AMBT),
        ("糖尿病视网膜病变", 86, "2.6%",  AMB,  AMBT),
    ]
    x0, bw_max = 300, 372
    y = 112
    for name, val, pct, col, fill in rows:
        w = max(10, int(bw_max * val / 1520))
        s.append(T(284, y + 36, name, 25, INK, anchor="end"))
        s.append(box(x0, y + 12, w, 34, fill, col, 6, 1.4))
        s.append(T(x0 + w + 14, y + 37, f"{val} 万 · {pct}", 23, BODY, anchor="start"))
        y += 56
    y += 6
    s.append(box(30, y, 900, 96, GRNT, GRN, 12, 1.5))
    s.append(T(480, y + 36, "白内障 + 未矫正屈光不正 = 52.0%", 27, GRN, weight="700"))
    s.append(T(480, y + 68, "一台成熟手术和一副眼镜即可解决,限制在医疗资源可及性", 22, GRN))
    y += 108
    s.append(T(30, y + 22, "占比为按原文人数自行计算;此拆分针对 50 岁及以上人群,全年龄段盲人为 4330 万",
               19, GRAY, anchor="start"))
    return 960, y + 40, "".join(s)


# ---------- F3: 通路分层 ----------
def fig_pathway():
    s = []
    s.append(box(30, 22, 900, 58, TINT, ACC, 12, 1.5))
    s.append(T(480, 58, "干预只能作用在损伤的下游", 28, ACCD, weight="700"))

    stations = [
        ("角膜",       "角膜混浊 · 外伤瘢痕", GRN),
        ("晶状体",     "白内障 · 外伤性白内障", GRN),
        ("感光细胞",   "黄斑变性 · 视网膜色素变性", AMB),
        ("双极细胞",   "视网膜下假体作用于此", ACC),
        ("神经节细胞", "青光眼", RED),
        ("视神经",     "青光眼 · 外伤性视神经病变", RED),
        ("外侧膝状体", "无对应致盲病因", GRAY),
        ("初级视皮层", "皮层假体作用于此", ACC),
    ]
    y = 96
    for i, (st, dz, col) in enumerate(stations):
        s.append(box(60, y, 230, 46, "#F7F9FC", CARD_L, 10, 1.4))
        s.append(T(175, y + 31, st, 26, INK, weight="700"))
        s.append(circ(320, y + 23, 9, col, col, 0))
        s.append(T(344, y + 32, dz, 23, BODY, anchor="start"))
        if i < len(stations) - 1:
            s.append(line(175, y + 46, y * 0 + 175, y + 57, GRAY, 2, None, "ahg"))
        y += 57
    y -= 11

    s.append(box(30, y + 14, 900, 86, REDT, RED, 12, 1.5))
    s.append(T(480, y + 46, "视网膜假体的信号必须经神经节细胞、沿视神经传出", 24, RED, weight="700"))
    s.append(T(480, y + 76, "所以青光眼致盲者用不了任何一种视网膜假体", 23, RED))
    return 960, y + 118, "".join(s)


# ---------- F4: 逐层方案与成熟度 ----------
def fig_layers():
    s = []
    s.append(box(30, 22, 900, 58, TINT, ACC, 12, 1.5))
    s.append(T(480, 58, "从外向内,方案成熟度依次下降", 28, ACCD, weight="700"))

    rows = [
        ("角膜",            "角膜移植(受限于供体短缺)",        "成熟",     GRN, GRNT),
        ("晶状体",          "摘除 + 人工晶状体",               "成熟",     GRN, GRNT),
        ("感光细胞 / 色素上皮", "基因治疗 · 光遗传 · 视网膜下假体", "分情况",   AMB, AMBT),
        ("视网膜血管",       "激光 · 抗 VEGF · 玻璃体切除",     "延缓为主", AMB, AMBT),
        ("神经节细胞 / 视神经", "降眼压只能延缓,损伤不可逆",      "空白",     RED, REDT),
        ("外侧膝状体",       "仅动物实验",                      "空白",     RED, REDT),
    ]
    y = 112
    s.append(T(68, y, "损伤层", 22, GRAY, anchor="start"))
    s.append(T(360, y, "现有方案", 22, GRAY, anchor="start"))
    s.append(T(790, y, "程度", 22, GRAY, anchor="start"))
    y += 16
    for layer, plan, deg, col, fill in rows:
        s.append(box(50, y, 880, 56, fill, col, 10, 1.3))
        s.append(T(68, y + 36, layer, 24, INK, anchor="start", weight="700"))
        s.append(T(360, y + 36, plan, 23, BODY, anchor="start"))
        s.append(T(790, y + 36, deg, 23, col, anchor="start", weight="700"))
        y += 64
    y += 6
    s.append(box(30, y, 900, 88, TINT, ACC, 12, 1.5))
    s.append(T(480, y + 36, "生物学疗法的作用对象都是活细胞", 26, ACCD, weight="700"))
    s.append(T(480, y + 66, "细胞死亡后它们全部失效;假体是唯一不要求靶细胞存活的方案", 22, ACCD))
    return 960, y + 104, "".join(s)


# ---------- F5: 外伤跨层 ----------
def fig_trauma():
    s = []
    s.append(box(30, 22, 900, 58, TINT, ACC, 12, 1.5))
    s.append(T(480, 58, "同一次事故可以同时损坏多个部位", 28, ACCD, weight="700"))

    rows = [
        ("角膜",        "瘢痕混浊",                      "角膜移植",         "可行", GRN, GRNT),
        ("晶状体",      "外伤性白内障",                  "白内障手术",       "可行", GRN, GRNT),
        ("视网膜 / 玻璃体", "脱离 · 增殖性病变",          "玻璃体视网膜手术", "不定", AMB, AMBT),
        ("视神经",      "外伤性视神经病变",              "无有效治疗",       "无",   RED, REDT),
        ("眼球",        "摘除",                          "无眼内方案",       "无",   RED, REDT),
    ]
    y = 112
    s.append(T(68, y, "受损部位", 22, GRAY, anchor="start"))
    s.append(T(268, y, "外伤后表现", 22, GRAY, anchor="start"))
    s.append(T(578, y, "方案", 22, GRAY, anchor="start"))
    s.append(T(846, y, "好用吗", 22, GRAY, anchor="start"))
    y += 16
    for part, sign, plan, ok, col, fill in rows:
        s.append(box(50, y, 880, 56, fill, col, 10, 1.3))
        s.append(T(68, y + 36, part, 24, INK, anchor="start", weight="700"))
        s.append(T(268, y + 36, sign, 22, BODY, anchor="start"))
        s.append(T(578, y + 36, plan, 22, BODY, anchor="start"))
        s.append(T(846, y + 36, ok, 22, col, anchor="start", weight="700"))
        y += 64
    y += 8
    s.append(box(30, y, 900, 116, REDT, RED, 12, 1.5))
    s.append(T(480, y + 36, "国际视神经外伤研究:视力提高超过 3 行的比例", 24, RED, weight="700"))
    s.append(T(230, y + 76, "减压手术 32%", 25, RED))
    s.append(T(480, y + 76, "激素 52%", 25, RED))
    s.append(T(742, y + 76, "单纯观察 57%", 25, RED, weight="700"))
    s.append(T(480, y + 104, "两种治疗均无确切获益", 21, RED))
    return 960, y + 136, "".join(s)


# ---------- F6: 数量级差距 ----------
def fig_scale():
    s = []
    s.append(box(30, 22, 900, 58, TINT, ACC, 12, 1.5))
    s.append(T(480, 58, "皮层电极数比神经节细胞少三到四个数量级", 28, ACCD, weight="700"))

    items = [
        ("感光细胞",   "约 9660 万",                 9660000.0, ACC,  TINT),
        ("神经节细胞", "70 万 – 150 万",             1070000.0, GRN,  GRNT),
        ("皮层电极(猕猴)", "1024",                   1024.0,    AMB,  AMBT),
        ("皮层电极(人体)", "96",                     96.0,      RED,  REDT),
    ]
    import math
    x0, bw_max = 330, 500
    lo, hi = math.log10(96.0), math.log10(9660000.0)
    y = 116
    for name, val_s, val, col, fill in items:
        frac = (math.log10(val) - lo) / (hi - lo)
        w = max(14, int(bw_max * (0.10 + 0.90 * frac)))
        s.append(T(312, y + 40, name, 24, INK, anchor="end", weight="700"))
        s.append(box(x0, y + 14, w, 40, fill, col, 6, 1.4))
        s.append(T(x0 + w + 14, y + 42, val_s, 23, BODY, anchor="start"))
        y += 66
    s.append(T(480, y + 22, "感光细胞 = 视杆 9200 万 + 视锥 460 万(人眼平均) · 横轴为对数刻度", 20, GRAY))
    y += 42
    s.append(box(30, y, 900, 126, TINT, ACC, 12, 1.5))
    s.append(T(480, y + 38, "中央凹几乎不汇聚,周边大幅汇聚", 26, ACCD, weight="700"))
    s.append(T(480, y + 70, "视网膜传出的是局部对比度,不是亮度", 24, ACCD))
    s.append(T(480, y + 102, "绕过它,这些处理全部要由软件重新合成", 24, ACCD))
    return 960, y + 146, "".join(s)


FIGS = {"toc": toc, "fig-causes": fig_causes, "fig-pathway": fig_pathway,
        "fig-layers": fig_layers, "fig-trauma": fig_trauma, "fig-scale": fig_scale}


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
        p = render(name, w, h, inner)
        print("rendered", p, f"({w}x{h})")
