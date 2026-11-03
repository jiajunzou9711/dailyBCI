# -*- coding: utf-8 -*-
"""series-ising-01 · 第二期 Ising 怎样进入神经网络 —— 卡片生成

卡 3–15 的正文直接从 ep02/draft.md 解析（取到「备注：」为止，跳过表格与【图】行），
保证成品与定稿一字不差；只在 SWAP 里登记因版面所需的改动。
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from card_generator import CardGenerator

PROJ = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", ".."))
OUT = os.path.join(PROJ, "output", "series-ising-01", "ep02")
FIG = os.path.join(OUT, "figs")
DRAFT = os.path.join(OUT, "draft.md")
def f(n): return os.path.join(FIG, n + ".png")
def o(n): return os.path.join(OUT, n)

gen = CardGenerator(date="2026.10.31")
# 用户 10-31 定：字号调小。默认注文 30 / 文字卡 32、行高 1.62；本期行高统一 1.55，
# 每张卡取放得下的最大字号（measure_overflow.py 实测），只有卡 6/7/11/12 低于 30
FS = {6: 24, 7: 24, 11: 28, 12: 26}
LH = {7: 1.5}

# 字体缺 ᵢ ⱼ ₁… 等字形，统一换成 _{x} / ^{x}
SUB = {"ᵢ": "i", "ⱼ": "j", "₁": "1", "₂": "2", "₃": "3", "₄": "4", "ₜ": "t"}
def conv(t):
    t = t.replace("ξᵢ^μ ξⱼ^μ", "ξ_{i}^{μ} ξ_{j}^{μ}").replace("Σ_μ", "Σ_{μ}")
    t = t.replace("(1 − 2a)^t", "(1 − 2a)^{t}")
    # 角标前加 word joiner，避免角标单独折到下一行
    t = re.sub(r"(?<=\S)([⁰¹²³⁴⁵⁶⁷⁸⁹]+)", "\u2060\\1", t)
    t = re.sub("[ᵢⱼ₁₂₃₄ₜ]+", lambda m: "_{" + "".join(SUB[c] for c in m.group(0)) + "}", t)
    return t

# 版面所需的改动（图在上方，正文改指「上图」）
SWAP = {
    6: [("按上一张的公式 Jᵢⱼ = ξᵢ ξⱼ 计算：", "按上一张的公式 Jᵢⱼ = ξᵢ ξⱼ 计算，结果如上图。")],
    8: [("它的转移矩阵是：", "它的转移矩阵如上图。")],
}

def card_body(n):
    s = open(DRAFT, encoding="utf-8").read()
    m = re.search(rf"^### 卡 {n} · (.+?)$(.*?)(?=^### )", s, re.S | re.M)
    head, body = m.group(1), m.group(2)
    title = re.sub(r"（2026.*?）$", "", head).strip()
    num = None
    if title[0] in "①②③④⑤":
        num, title = title[0], title[1:].strip()
    body = body.split("\n备注：")[0]
    for a, b in SWAP.get(n, []):
        assert a in body, (n, a); body = body.replace(a, b)
    paras, bullets = [], []
    def flush():
        if bullets:
            paras.append("\n".join("· " + x for x in bullets)); bullets.clear()
    for ln in body.strip().split("\n"):
        ln = ln.strip()
        if not ln or ln.startswith("|") or ln.startswith("【图") or ln.startswith("图注："):
            flush(); continue
        if re.match(r"^(- |\d+\. )", ln):
            bullets.append(re.sub(r"^(- |\d+\. )", "", ln)); continue
        flush(); paras.append(ln)
    flush()
    # 公式行与前后两句并成一段，只换行不加段距（省版面，不改字）
    merged = []
    glue = False
    for p in paras:
        if p.startswith(("J₁", "J₄", "E = ")) and merged:
            merged[-1] += "\n" + p; glue = True; continue
        if glue:
            merged[-1] += "\n" + p; glue = False; continue
        merged.append(p)
    return num, conv(title), [conv(p) for p in merged]

# ---------------------------------------------------------------- 卡 1 封面
gen.cover_card(
    "Ising 模型",
    "从相变到联想记忆",
    "从一点线索想起完整的记忆，神经网络怎样才能做到？1970 到 80 年代，研究者把神经网络写成 Ising 模型，给出了一种数学上可行的机制。本期讲清这个机制，以及它能支持什么、不能支持什么。",
    o("01-cover.png"),
    concept_image=os.path.join(PROJ, "papers", "series-ising", "wills-2005-fig2-cells1-12-cover.png"),
    concept_height=560, title_size=92, title_top=40, subtitle_size=30,
    image_caption="Wills TJ, et al. (2005). Attractor dynamics in the hippocampal representation\nof the local environment. Science 308:873–876, Fig. 2.",
)

# ---------------------------------------------------------------- 卡 2 导语 + 目录
gen.figure_card(
    f("toc"), "本期路线",
    ["Ising 模型是为解释铁磁相变提出的统计物理模型。神经科学里用到它的工作可以分成两条线，本期讲其中一条：连接强度 J 由研究者设定，用来研究神经网络怎样存储记忆。",
     "这条线上最有代表性的是 Hopfield 1982 年提出的网络：记住的模式是网络状态的稳定点，从附近的状态出发，网络会回到这个点。有这种性质的网络统称吸引子网络（attractor network），Hopfield 网络是其中一种。2005 年，大鼠海马实验观察到了与这种动力学一致的群体活动；2024 年，Hopfield 因人工神经网络方面的奠基性工作获得诺贝尔物理学奖。",
     "来源：本篇只讲原理，不针对某一篇具体论文做解读。本篇主要参考的文献：McCulloch & Pitts 1943；Amari 1972；Little 1974；Hopfield 1982（完整列表见卡 16）。"],
    o("02-toc.png"), figure_height=440,
)

# ---------------------------------------------------------------- 卡 3–14
FIGCARDS = {3: ("figA1-threshold", "图 1", 330), 6: ("fig6-jtable", "图 2", 250),
            7: ("figA3-rows", "图 3", 180), 8: ("fig8-matrix", "图 4", 240),
            12: ("figA5-landscape", "图 5", 260)}
for n in range(3, 15):
    num, title, paras = card_body(n)
    out = o(f"{n:02d}-c{n-2}.png")
    if n in FIGCARDS:
        fig, lab, fh = FIGCARDS[n]
        gen.figure_card(f(fig), lab, paras, out, figure_height=fh, title=title, title_num=num, annot_size=FS.get(n, 30), annot_lh=LH.get(n, 1.55))
    else:
        gen.text_card(title, paras, out, title_num=num, para_size=FS.get(n, 30), para_lh=LH.get(n, 1.55))

# ---------------------------------------------------------------- 卡 15 尾卡 + 卡 16 参考文献
_, _, lead = card_body(15)
gen.text_card("小结", lead, o("15-summary.png"))

REFS = re.search(r"### 卡 16 · .*?\n\n(.*?)\n\n署名", open(DRAFT, encoding="utf-8").read(), re.S).group(1)
gen.tail_card([r.strip() for r in REFS.strip().split("\n")], o("16-tail.png"))
print("done")
