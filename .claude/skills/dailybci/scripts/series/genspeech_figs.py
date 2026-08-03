"""Fogg 2026「A generalizable speech neuroprosthesis」日报自制示意图。
目录卡 + 失语分层 + 两条通路 + 解码路线 + 冻结/可训练参数量。
"""
import os, subprocess, tempfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-08-03-generalizable-speech", "figs")
os.makedirs(OUT, exist_ok=True)

ACC = "#2F6DB5"; ACCD = "#1E4E86"; TINT = "#E9F0F8"
INK = "#1A1A1A"; BODY = "#4A4A4A"; GRAY = "#8A8A8A"; LINE = "#D6DBE2"
RED = "#C0392B"; REDT = "#F7E9E7"; GRN = "#2E7D57"; GRNT = "#E7F2EC"
AMB = "#8A6D1A"; AMBT = "#FBF7E9"; AMBL = "#D9C98A"
CARD_L = "#DCE5F0"; GREYF = "#F2F3F1"; GREYL = "#DBDCD8"

DEFS = ('<defs>'
        '<marker id="ah" markerWidth="10" markerHeight="10" refX="8" refY="3" '
        'orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="%s"/></marker>'
        '<marker id="ahr" markerWidth="10" markerHeight="10" refX="8" refY="3" '
        'orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="%s"/></marker>'
        '<marker id="ahg" markerWidth="10" markerHeight="10" refX="8" refY="3" '
        'orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="%s"/></marker>'
        '</defs>' % (ACC, RED, GRAY))


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


# ---------- 目录卡 ----------
def toc():
    s = []
    items = [
        ("1", "这篇在回答什么", "新用户要多久才能用上解码器"),
        ("2", "说不出话，坏在哪一层", "失语症、构音障碍、声道，三种病变"),
        ("3", "卒中与渐冻症的不同机制", "一个皮层完好，一个皮层本身在退化"),
        ("4", "脑机接口只能接下面两层", "四条解码路线，音素为当前主流"),
        ("5", "六人合池的四条证据", "离线、实时、新用户、跨半球"),
        ("6", "排除混淆与边界", "深度、句子重叠、以及这条路的限制"),
    ]
    y = 30
    for n, title, sub in items:
        s.append(box(30, y, 900, 78, "#F7F9FC", CARD_L, 14, 1.5))
        s.append(circ(78, y + 39, 26, TINT, ACC, 1.5))
        s.append(T(78, y + 49, n, 30, ACCD, weight="700"))
        s.append(T(126, y + 34, title, 30, INK, anchor="start", weight="700"))
        s.append(T(126, y + 64, sub, 21, GRAY, anchor="start"))
        y += 92
    return 960, y, "".join(s)


# ---------- 图1：说不出话的三层 ----------
def fig_layers():
    s = []
    s.append(box(30, 20, 900, 56, TINT, ACC, 12, 1.5))
    s.append(T(480, 56, "「说不出话」至少分三层，是三种不同的病变", 27, ACCD, weight="700"))

    rows = [
        ("第一层 · 语言层", "失语症（布洛卡 / 韦尼克）",
         "词本身出不来，或听不懂别人的话；发音器官正常", RED, REDT, "脑机接口目前解不了"),
        ("第二层 · 言语运动层", "构音障碍 · 言语失用",
         "知道要说哪个词，但组织不出或执行不了发音动作", GRN, GRNT, "当前所有语音 BCI 的目标"),
        ("第三层 · 传导与效应器", "下运动神经元 · 喉与声道",
         "大脑与运动皮层都正常，坏在更下游", GRN, GRNT, "同属可接范围"),
    ]
    y = 100
    for title, name, desc, col, tint, tag in rows:
        s.append(box(30, y, 900, 128, tint, col, 14, 1.6))
        s.append(T(58, y + 40, title, 26, col, anchor="start", weight="700"))
        s.append(T(58, y + 78, name, 29, INK, anchor="start", weight="700"))
        s.append(T(58, y + 112, desc, 22, BODY, anchor="start"))
        s.append(box(636, y + 20, 272, 40, "#FFFFFF", col, 10, 1.3))
        s.append(T(772, y + 47, tag, 21, col, weight="700"))
        y += 146

    s.append(box(30, y + 6, 900, 62, GREYF, GREYL, 12, 1.5))
    s.append(T(480, y + 32, "区分它们的意义：坏掉的层不同，运动皮层里还有没有可读的指令就不同", 22, BODY))
    s.append(T(480, y + 58, "第一层坏的正是要被解码的那个信号源本身", 22, BODY))
    return 960, y + 92, "".join(s)


# ---------- 图2：两条通路 ----------
def fig_pathways():
    s = []
    s.append(box(30, 20, 900, 56, TINT, ACC, 12, 1.5))
    s.append(T(480, 56, "同样说不出话，脑桥卒中与渐冻症的机制完全不同", 27, ACCD, weight="700"))

    def col(x, head, sub, hcol, htint, items, note):
        s.append(box(x, 100, 430, 66, htint, hcol, 12, 1.6))
        s.append(T(x + 215, 128, head, 30, hcol, weight="700"))
        s.append(T(x + 215, 156, sub, 21, BODY))
        yy = 186
        for t in items:
            s.append(box(x, yy, 430, 62, "#FFFFFF", LINE, 10, 1.2))
            s.append(T(x + 18, yy + 27, t[0], 22, INK, anchor="start", weight="700"))
            s.append(T(x + 18, yy + 52, t[1], 21, BODY, anchor="start"))
            yy += 72
        s.append(box(x, yy + 6, 430, 76, htint, hcol, 12, 1.4))
        s.append(T(x + 215, yy + 36, note[0], 22, hcol, weight="700"))
        s.append(T(x + 215, yy + 62, note[1], 21, hcol))
        return yy + 90

    y1 = col(30, "脑桥卒中", "基底动脉或其穿支闭塞", ACC, TINT, [
        ("病灶", "脑桥腹侧，下行运动纤维被切断"),
        ("保留", "背侧完好，意识、感觉、认知正常"),
        ("表现", "四肢瘫痪 + 构音不能（闭锁综合征）"),
    ], ("运动皮层完好", "电极记录的是健康组织"))

    y2 = col(500, "肌萎缩侧索硬化（渐冻症）", "运动神经元进行性变性", RED, REDT, [
        ("病灶", "上、下运动神经元同时退化"),
        ("要点", "上运动神经元就在运动皮层内"),
        ("表现", "痉挛型 + 弛缓型混合构音障碍，渐进"),
    ], ("记录位点本身在病变", "且病情持续推进"))

    y = max(y1, y2)
    s.append(box(30, y + 8, 900, 66, AMBT, AMBL, 12, 1.5))
    s.append(T(480, y + 36, "本篇六名参与者：四名渐冻症（T12/T15/T17/T21），两名脑桥卒中（T16/T22）", 22, AMB))
    s.append(T(480, y + 62, "T17 已达构音不能，其单人解码器词错误率 65.63%，基本不可用", 22, AMB))
    return 960, y + 98, "".join(s)


# ---------- 图3：四条解码路线 ----------
def fig_routes():
    s = []
    s.append(box(30, 20, 900, 56, TINT, ACC, 12, 1.5))
    s.append(T(480, 56, "电极扎在腹侧中央前回，解出来的中间表征有四种选法", 27, ACCD, weight="700"))

    hdr = [(60, "中间表征"), (300, "先解成什么"), (660, "现状")]
    s.append(box(30, 92, 900, 46, GREYF, GREYL, 10, 1.3))
    for x, t in hdr:
        s.append(T(x, 122, t, 22, GRAY, anchor="start", weight="700"))

    rows = [
        ("整词", "直接分类成 N 个词之一", "大词汇量下已被取代", GRAY, "#FFFFFF"),
        ("音素", "约 40 个发音单元的概率序列", "当前主流", ACCD, TINT),
        ("发音运动学", "唇、舌、颌、喉的运动轨迹", "与皮层编码最贴合", GRAY, "#FFFFFF"),
        ("声学波形", "直接合成语音，不经过文本", "可带语调与重音", GRAY, "#FFFFFF"),
    ]
    y = 148
    for name, mid, st, col, bg in rows:
        s.append(box(30, y, 900, 74, bg, CARD_L if bg != "#FFFFFF" else LINE, 10, 1.4))
        s.append(T(60, y + 46, name, 27, col if col != GRAY else INK, anchor="start", weight="700"))
        s.append(T(300, y + 44, mid, 22, BODY, anchor="start"))
        s.append(T(660, y + 44, st, 21, col, anchor="start"))
        y += 84

    s.append(box(30, y + 8, 900, 96, GREYF, GREYL, 12, 1.5))
    s.append(T(480, y + 40, "音素成为主流的关键理由：约 40 个类别可组合出任意词，", 22, BODY))
    s.append(T(480, y + 68, "且音素标签能直接从提示文本推出——发不出声的人没有音频可作监督", 22, BODY))
    return 960, y + 122, "".join(s)


# ---------- 图4：冻结与可训练 ----------
def fig_frozen():
    s = []
    s.append(box(30, 20, 900, 56, TINT, ACC, 12, 1.5))
    s.append(T(480, 56, "新用户能改动的部分，只有整个模型的约 0.4%", 27, ACCD, weight="700"))

    base = 430
    def bar(cx, h, fill, stroke, top, sub1, sub2):
        yy = base - h
        s.append(box(cx - 105, yy, 210, h, fill, stroke, 8, 1.6))
        s.append(T(cx, yy - 18, top, 30, stroke, weight="700"))
        s.append(T(cx, base + 34, sub1, 24, INK, weight="700"))
        s.append(T(cx, base + 62, sub2, 21, BODY))

    bar(280, 300, "#E8ECF1", "#7C8794", "68.4 M", "冻结的解码器", "音素怎么解，写死在这里")
    bar(680, 12, TINT, ACC, "0.26 M", "新用户的投影层", "一个线性映射 + tanh")

    s.append(line(150, base, 880, base, GRAY, 1.5))
    s.append(T(120, base + 6, "参数量", 21, GRAY, anchor="end"))

    s.append(box(30, 520, 900, 118, GREYF, GREYL, 12, 1.5))
    s.append(T(58, 552, "投影层只能做坐标变换：把这个人的神经特征旋转、缩放、重组，", 22, BODY, anchor="start"))
    s.append(T(58, 582, "投到解码器已经建好的 512 维空间里。它无法改变解码逻辑。", 22, BODY, anchor="start"))
    s.append(T(58, 616, "所以适配成功，说明个体差异是能被一个线性变换吸收的那种差异。", 22, ACCD, anchor="start", weight="700"))
    return 960, 660, "".join(s)


FIGS = {"toc": toc, "fig-layers": fig_layers, "fig-pathways": fig_pathways,
        "fig-routes": fig_routes, "fig-frozen": fig_frozen}


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
