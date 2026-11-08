# -*- coding: utf-8 -*-
"""series-ising-01 · 第三期 用最大熵描述群体放电 —— 卡片生成

卡 3–17 的正文直接从 ep03/draft.md 解析（跳过表格、代码块、【图】行），
保证成品与定稿一字不差；只在 SWAP 里登记因版面所需的改动。
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from card_generator import CardGenerator

PROJ = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", ".."))
OUT = os.path.join(PROJ, "output", "series-ising-01", "ep03")
FIG = os.path.join(OUT, "figs")
PAP = os.path.join(PROJ, "papers", "series-ising")
DRAFT = os.path.join(OUT, "draft.md")
def f(n): return os.path.join(FIG, n + ".png")
def p(n): return os.path.join(PAP, n + ".png")
def o(n): return os.path.join(OUT, n)

gen = CardGenerator(date="2026.11.08")
FS, LH = {}, {}

# 字体缺 ᵢ ⱼ ₁ ₂ ₍ ₎ 及上标幂次，统一换成 _{x} / ^{x}
SUB = {"ᵢ": "i", "ⱼ": "j", "₁": "1", "₂": "2", "₃": "3", "₍": "(", "₎": ")"}
SUPD = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹", "0123456789")
def conv(t):
    t = re.sub(r"10([⁰¹²³⁴⁵⁶⁷⁸⁹]+)", lambda m: "10^{" + m.group(1).translate(SUPD) + "}", t)
    t = t.replace("2^N", "2^{N}").replace("S_N", "S_{N}").replace("I_N", "I_{N}")
    # 参考文献角标前加 word joiner，避免角标单独折行
    t = re.sub(r"(?<=\S)([¹²³⁴]+)", "⁠\\1", t)
    t = re.sub("[ᵢⱼ₁₂₃₍₎]+", lambda m: "_{" + "".join(SUB[c] for c in m.group(0)) + "}", t)
    return t

# 版面所需的改动（表格、公式移到上方的图里，正文改指「上图」）
SWAP = {
    3: [("把计算神经科学的模型分成三类¹：", "把计算神经科学的模型分成三类¹，见上图。")],
    10: [("得到的分布是：", "得到的分布如上图。")],
    12: [("两个神经元时：", "两个神经元时，Z 的展开如上图。")],
}

def card_body(n):
    s = open(DRAFT, encoding="utf-8").read()
    m = re.search(rf"^### 卡 {n} · (.+?)$(.*?)(?=^##)", s, re.S | re.M)
    head, body = m.group(1), m.group(2)
    title = re.sub(r"（2026.*?）$", "", head).strip()
    num = None
    if title[0] in "①②③④⑤":
        num, title = title[0], title[1:].strip()
    body = re.sub(r"```.*?```", "", body, flags=re.S)
    for a, b in SWAP.get(n, []):
        assert a in body, (n, a); body = body.replace(a, b)
    paras, bullets = [], []
    def flush():
        if bullets:
            paras.append("\n".join("· " + x for x in bullets)); bullets.clear()
    for ln in body.strip().split("\n"):
        ln = ln.strip()
        if not ln or ln.startswith("|") or ln.startswith("【图"):
            flush(); continue
        if re.match(r"^(- |\d+\. )", ln):
            bullets.append(re.sub(r"^(- |\d+\. )", "", ln)); continue
        flush(); paras.append(ln)
    flush()
    return num, conv(title), [conv(x) for x in paras]

# ---------------------------------------------------------------- 卡 1 封面
gen.cover_card(
    "Ising 模型",
    "用最大熵描述群体放电",
    "同时记录一群神经元，怎样描述它们的集体放电？只约束放电率和两两相关、取熵最大，得到的正好是 Ising 模型。本期讲清这个模型从哪来、怎样拟合，以及拟合出的 J 能说明什么。",
    o("01-cover.png"),
    concept_image=p("schneidman-2006-fig2a"),
    concept_height=560, title_size=82, title_top=40, subtitle_size=30,
    image_caption="2006 · Nature · Schneidman, Berry, Segev & Bialek\nWeak pairwise correlations imply strongly correlated network states in a neural population",
)

# ---------------------------------------------------------------- 卡 2 导语 + 目录
gen.figure_card(
    f("toc"), "本期路线",
    ["Ising 模型进入神经科学有两条线。一条把它当作神经网络的模型，连接强度 J 由研究者设定，Hopfield 网络属于这一条。本期讲另一条，方向反过来：从同时记录到的一群神经元的放电中，估计 Ising 模型的参数。这条线的代表性工作，是 Schneidman 等 2006 年在蝾螈视网膜上的研究。",
     "来源：本篇只讲原理，不针对某一篇具体论文做解读。主要参考的文献：Jaynes 1957；Schneidman et al. 2006；Dayan & Abbott 2001（完整列表见卡 17）。"],
    o("02-toc.png"), figure_height=500,
)

# ---------------------------------------------------------------- 卡 3–16
FIGCARDS = {3: (f("fig3-types"), "图 1", 600), 5: (p("schneidman-2006-fig1ab-cover"), "图 2", 620),
            6: (f("fig6-counts"), "图 3", 400), 8: (f("fig8-ab"), "图 4", 250),
            9: (p("schneidman-2006-fig1ef"), "图 5", 380), 10: (f("fig10-formula"), "图 6", 290),
            11: (f("fig11-symbols"), "图 7", 520), 12: (f("fig12-z"), "图 8", 220),
            13: (p("schneidman-2006-fig2a"), "图 9", 520), 14: (p("schneidman-2006-fig2c"), "图 10", 390),
            15: (p("schneidman-2006-fig3c"), "图 11", 385)}
for n in range(3, 17):
    num, title, paras = card_body(n)
    out = o(f"{n:02d}-c{n-2}.png")
    if n in FIGCARDS:
        fig, lab, fh = FIGCARDS[n]
        gen.figure_card(fig, lab, paras, out, figure_height=fh, title=title, title_num=num,
                        annot_size=FS.get(n, 30), annot_lh=LH.get(n, 1.55))
    else:
        gen.text_card(title, paras, out, title_num=num, para_size=FS.get(n, 30), para_lh=LH.get(n, 1.55))

# ---------------------------------------------------------------- 卡 17 尾卡 + 参考文献
s17 = re.search(r"### 卡 17 · .*?\n\n(.*?)\n\n参考文献\n(.*?)\n\n##", open(DRAFT, encoding="utf-8").read(), re.S)
lead_raw, refs = s17.group(1), s17.group(2)
lead, bul = [], []
for ln in lead_raw.strip().split("\n"):
    ln = ln.strip()
    if ln.startswith("- "):
        bul.append("· " + ln[2:]); continue
    if bul:
        lead.append("\n".join(bul)); bul = []
    if ln:
        lead.append(ln)
if bul:
    lead.append("\n".join(bul))
gen.tail_card([r.strip() for r in refs.strip().split("\n")], o("17-tail.png"),
              lead_paragraphs=[conv(x) for x in lead])
print("done")
