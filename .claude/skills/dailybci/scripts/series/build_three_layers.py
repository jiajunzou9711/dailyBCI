"""Methodology piece — 神经活动↔行为:三层嵌套的分析选择.
Renders one nested-layers SVG schematic + 6 小红书 cards (series track).
"""
import os, sys, subprocess, tempfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))          # .claude/skills/dailybci
sys.path.insert(0, os.path.join(SKILL_DIR, "scripts"))
from card_generator import CardGenerator

FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "series-decoding-three-layers")
FIG = os.path.join(OUT, "figs")
os.makedirs(FIG, exist_ok=True)

ACC = "#2F6DB5"; ACCD = "#1E4E86"; TINT = "#E9F0F8"
INK = "#1A1A1A"; BODY = "#4A4A4A"; GRAY = "#8A8A8A"; LINE = "#D6DBE2"
CHIPF = "#F2F3F1"; CHIPL = "#DBDCD8"

DEFS = (
    '<defs><marker id="ah" markerWidth="10" markerHeight="10" refX="8" refY="3" '
    'orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="%s"/></marker></defs>' % ACC
)

def T(x, y, s, size=24, fill=INK, anchor="middle", weight="400"):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}">{s}</text>'

def box(x, y, w, h, fill, stroke, rx=12, sw=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

def arrow(x, y1, y2):
    return f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{ACC}" stroke-width="2.5" marker-end="url(#ah)"/>'

def fig_layers():
    s = []
    # Frame 1 (outer)
    s.append(box(24, 24, 872, 592, "#FCFDFE", LINE, 18, 1.5))
    s.append(T(54, 58, "第一层", 22, ACC, anchor="start", weight="700"))
    s.append(box(60, 72, 392, 78, CHIPF, CHIPL, 12, 1.2))
    s.append(T(256, 106, "编码", 25, ACCD, weight="700"))
    s.append(T(256, 137, "行为 → 神经活动", 20, BODY))
    s.append(box(472, 72, 388, 78, TINT, ACC, 12, 1.6))
    s.append(T(666, 106, "解码", 25, ACCD, weight="700"))
    s.append(T(666, 137, "神经活动 → 行为", 20, BODY))
    s.append(arrow(666, 150, 173))
    # Frame 2 (inside decoding)
    s.append(box(58, 176, 804, 424, "#FFFFFF", ACC, 16, 1.4))
    s.append(T(88, 210, "第二层 · 解码之内", 22, ACC, anchor="start", weight="700"))
    s.append(box(94, 226, 348, 80, CHIPF, CHIPL, 12, 1.2))
    s.append(T(268, 260, "描述性几何", 25, ACCD, weight="700"))
    s.append(T(268, 291, "距离 / PCA / RSA · 样本内", 19, BODY))
    s.append(box(478, 226, 360, 80, TINT, ACC, 12, 1.6))
    s.append(T(658, 260, "训练解码器", 25, ACCD, weight="700"))
    s.append(T(658, 291, "预测新 trial · 样本外", 19, BODY))
    s.append(arrow(658, 306, 329))
    # Frame 3 (inside the decoder)
    s.append(box(104, 332, 712, 256, "#F7FAFD", ACC, 16, 1.4))
    s.append(T(134, 366, "第三层 · 解码器之内", 22, ACC, anchor="start", weight="700"))
    s.append(box(142, 384, 308, 96, TINT, ACC, 12, 1.6))
    s.append(T(296, 418, "生成式", 25, ACCD, weight="700"))
    s.append(T(296, 448, "建 p(r|s) 反推", 19, BODY))
    s.append(T(296, 472, "LDA · 朴素贝叶斯 等", 18, GRAY))
    s.append(box(470, 384, 308, 96, TINT, ACC, 12, 1.6))
    s.append(T(624, 418, "判别式", 25, ACCD, weight="700"))
    s.append(T(624, 448, "直接学边界 p(s|r)", 19, BODY))
    s.append(T(624, 472, "逻辑回归 · 线性 SVM 等", 18, GRAY))
    s.append(T(460, 544, "后一层只在前一层选定后出现 · 每层各回答一个问题", 21, BODY))
    return 920, 640, "".join(s)

def render_fig(name, w, h, inner):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
           f'viewBox="0 0 {w} {h}" font-family="HeitiSC,Helvetica,Arial,sans-serif">'
           f'{DEFS}<rect width="{w}" height="{h}" fill="#FFFFFF"/>{inner}</svg>')
    page = (f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>'
            f'@font-face{{font-family:"HeitiSC";src:url("file://{FONT}");}}'
            f'*{{margin:0;padding:0}}body{{width:{w}px;height:{h}px}}</style></head>'
            f'<body>{svg}</body></html>')
    tmp = tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8")
    tmp.write(page); tmp.close()
    out = os.path.join(FIG, name + ".png")
    subprocess.run(["npx", "playwright", "screenshot", f"file://{tmp.name}", out,
                    f"--viewport-size={w},{h}", "--wait-for-timeout=600"],
                   check=True, capture_output=True, text=True)
    os.unlink(tmp.name)
    return out

# ---- render the figure ----
w, h, inner = fig_layers()
render_fig("layers", w, h, inner)

# ---- build the cards ----
gen = CardGenerator(date="2026.06.28", platform="xiaohongshu")

gen.cover_card(
    "神经活动与行为",
    "三层嵌套的分析选择",
    "编码/解码、距离/解码器、生成/判别——三组概念,层层相套。",
    os.path.join(OUT, "01-cover.png"),
    source="方法论笔记 · 续「生成式群体解码」篇。不展开方法的内部推导,梳理分析前要先想清的三层选择,以及每层各自回答什么、彼此如何互补。",
)

gen.figure_card(
    os.path.join(FIG, "layers.png"), "三层嵌套",
    [
        "上一篇梳理了生成式群体解码的内部做法。真正动手分析前,要先在三个层层嵌套的问题上各做一次选择。",
        "如上图,第一层在**编码与解码**之间选;选定解码后,第二层在**描述性几何度量与训练解码器**之间选;确定用解码器后,第三层在**生成式与判别式**之间选。三层并非并列,后一层都嵌在前一层之内。",
        "下面按第一层到第三层,逐层说清每层的两个选项各自回答什么。",
    ],
    os.path.join(OUT, "02-map.png"), figure_height=620,
)

gen.text_card(
    "第一层:编码与解码",
    [
        "第一层的选择在编码与解码之间。二者是**同一个关系的两个方向**¹。",
        "编码常用 GLM,从行为变量预测神经活动,多在单神经元层面,回答“什么在调制这个神经元”。解码方向相反,从神经活动反推行为;它**也可做单神经元,目前更多在群体层面**,回答“从这些活动能读出什么”。两者互补:解码说明信息**可读、可泛化**;编码进一步说明是**哪个变量**在起作用——解码出的变量可能被相关变量混淆,GLM 纳入全部回归量后,可估其在扣除其他变量后的独立贡献。",
        "二者有四种常见组合:**先解码后编码**(解码筛出信息、编码逐神经元解释由谁承载并查混淆,适合探索“能恢复什么”);**先编码后解码**(先刻画调谐、再证群体可读,适合已有假设);**只编码**(只问表征了什么);**只解码**(只问能否读出、读得多准,纯读出与 BCI)。确定走解码后,第二层随之而来。",
    ],
    os.path.join(OUT, "03-encode-decode.png"),
)

gen.text_card(
    "第二层:描述性几何与训练解码器",
    [
        "进入解码后,第二层在两类工具间选:刻画每类活动的几何结构,或训练一个解码器去预测。",
        "描述性的一类多在**样本内、常无监督**——距离(d′)、PCA 低维投影、表征相似性分析(RSA)等,回答“各类活动分得开吗、结构如何”。隐患在于:高维、trial 少时,即便活动与行为无关,点云也会显得有些分开,**样本内的距离因而系统性偏大**。",
        "排除这种假象要分两步,回答两个不同问题:**置换检验**(打乱标签重算)判断“分离是否超过偶然”——显著性;**交叉验证**(在没见过的 trial 上检验)给出“分离有多大、能否泛化”——无偏的效应量。",
        "解码器走的正是交叉验证这条路。把距离也做成交叉验证版本(**crossnobis**²),它便成无偏估计,而这一步在机制上**等同于训练并检验一个线性解码器**。严谨化之后二者收敛为同一回事;选择解码器时,第三层要在两条建模路线间定夺。",
    ],
    os.path.join(OUT, "04-geometry-decoder.png"),
)

gen.text_card(
    "第三层:生成式与判别式",
    [
        "确定用解码器后,第三层在生成式与判别式之间选。**差别在内部的建模路线,与最终输出无关**——两者最终都给出一个标签。",
        "生成式先对每一类活动建立分布 p(r|s),再用贝叶斯反推应判哪一类³;这类方法**如线性判别分析(LDA)、朴素贝叶斯等**,因为对 p(r|s) 建模,也能正向采样生成数据,这正是上一篇生成式群体解码所走的路线。",
        "判别式略过对每类分布的建模,直接学习类别边界 p(s|r),**如逻辑回归、线性 SVM 等**。两类各有其他方法,这里只举常见者。选择取决于权衡:样本少、需要机制、对分布假设有把握时,生成式收敛更快、可解释性更强;样本多、只看预测精度、对假设不放心时,判别式渐近误差更低⁴。",
        "至此三层选择走完。下一张把整条链收拢,标出每层对应的判断依据。",
    ],
    os.path.join(OUT, "05-generative-discriminative.png"),
)

gen.tail_card(
    [
        "¹ Kriegeskorte N, Douglas PK. 2019. Curr Opin Neurobiol 55:167–179.",
        "² Walther A, Nili H, Ejaz N, Alink A, Kriegeskorte N, Diedrichsen J. 2016. NeuroImage 137:188–200.",
        "³ Dayan P, Abbott LF. 2001. Theoretical Neuroscience. Cambridge, MA: MIT Press.",
        "⁴ Ng AY, Jordan MI. 2002. Adv Neural Inf Process Syst 14:841–848.",
    ],
    os.path.join(OUT, "06-tail.png"),
    lead_paragraphs=[
        "收拢三层:第一层在**编码与解码**间选(同一关系的两个方向);第二层在**描述性几何与训练解码器**间选——样本内的距离需置换检验判显著、交叉验证给无偏量级,交叉验证版距离(crossnobis)本身等价于线性解码器;第三层在**生成式与判别式**间选(差别在建模路线,输出相同)。",
        "三条可长期记住的判断:① 编码与解码是一个关系的两个方向,可单用、可组合,顺序由问题决定;② 描述性度量与解码器互补,严谨化后二者收敛;③ 生成式与判别式的分野在建模路线——前者建每类分布再反推,后者直接学边界。",
    ],
)

print("done →", OUT)
