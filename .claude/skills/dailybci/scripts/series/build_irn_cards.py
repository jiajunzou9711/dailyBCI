# -*- coding: utf-8 -*-
"""2026-11-28 原理期 · 读懂放大器规格表上的「输入参考噪声」 —— 卡片生成

正文从 draft.md「卡片文案（落稿）」逐节解析，保证成品与定稿一字不差（去掉 > 开头的脚注与笔记）。
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from card_generator import CardGenerator

PROJ = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", ".."))
OUT = os.path.join(PROJ, "output", "2026-11-28-input-referred-noise")
FIG = os.path.join(OUT, "figs")
DRAFT = os.path.join(OUT, "draft.md")
def f(n): return os.path.join(FIG, n + ".png")
def o(n): return os.path.join(OUT, n)

gen = CardGenerator(date="2026.11.28")
SUP = "⁰¹²³⁴⁵⁶⁷⁸⁹"

# (draft 小节标题前缀, 配图, 圈号, 图高)；配图为 None 的用纯文字卡
CARDS = [
    ("开篇卡", "f1", "①", 150),
    ("① 卡", "f2", "①", 330),
    ("①′ 卡", "f3", "①", 220),
    ("② 卡", "f4", "②", 250),
    ("②′-1 卡", "f5", "②", 240),
    ("②′-2 卡", "f6", "②", 180),
    ("②′-3 卡", "f7", "②", 220),
    ("③-1 卡", "f8", "③", 260),
    ("③-2 卡", "f9", "③", 200),
    ("④ 卡", None, "④", 0),
    ("局限卡", None, "④", 0),
]
FS = {}


def conv(t):
    return re.sub(rf"(?<=\S)([{SUP}]+)", "⁠\\1", t)


def section(prefix):
    s = open(DRAFT, encoding="utf-8").read()
    s = s[s.index("# 卡片文案"):s.index("# 参考文献")]
    m = re.search(rf"^## {re.escape(prefix)}[（ ].*?$(.*?)(?=^## |\Z)", s, re.S | re.M)
    body = m.group(1)
    title, paras, bullets, incode = None, [], [], False
    def flush():
        if bullets:
            paras.append("\n".join("· " + x for x in bullets)); bullets.clear()
    for ln in body.strip().split("\n"):
        ln = ln.strip()
        if ln.startswith("```"):
            incode = not incode; flush(); continue
        if incode:
            paras.append(ln); continue
        if ln.startswith(">"):
            break
        if title is None and ln.startswith("**") and ln.endswith("**"):
            title = ln.strip("*"); continue
        if not ln:
            flush(); continue
        if ln.startswith("- "):
            bullets.append(ln[2:]); continue
        flush(); paras.append(ln)
    flush()
    return title, [conv(x) for x in paras]


REFS = [
    "¹Intan Technologies. (2023). RHD2000 series digital electrophysiology interface chips. Datasheet.",
    "²Friis HT. (1944). Noise figures of radio receivers. Proc IRE 32(7):419–422.",
    "³Harrison RR, Charles C. (2003). A low-power low-noise CMOS amplifier for neural recording applications. IEEE J Solid-State Circuits 38(6):958–965.",
    "⁴imec. Neuropixels 1.0 probe datasheet. neuropixels.org.",
    "⁵Henze DA, et al. (2000). Intracellular features predicted by extracellular recordings in the hippocampus in vivo. J Neurophysiol 84(1):390–400.",
    "",
    "示意图均为作者自绘；标注「自算」的数值由作者按文中公式计算。",
]

ONLY = set(int(x) for x in sys.argv[1:])
def want(n): return not ONLY or n in ONLY

if want(1):
    gen.cover_card(
        "读懂放大器规格表上的",
        "「输入参考噪声」",
        "规格表上的噪声值只是放大器这一项，只在标明的频段内成立，是记录噪声的下限。",
        o("01-cover.png"),
        concept_image=f("cover"), concept_height=420,
        image_caption="主要依据 Intan RHD2000 规格书 · Harrison & Charles 2003 · Neuropixels 1.0 规格书 · Henze 2000",
    )

if want(2):
    gen.figure_card(
        f("toc"), "来源",
        ["依据 Intan RHD2000 与 Neuropixels 1.0 规格书、Harrison 与 Charles 2003（IEEE J Solid-State Circuits）、Friis 1944（Proc IRE）、Henze 等 2000（J Neurophysiol）。全部出处见末卡。"],
        o("02-toc.png"), figure_height=560,
    )

for i, (prefix, fig, num, fh) in enumerate(CARDS):
    n = i + 3
    if not want(n): continue
    title, paras = section(prefix)
    out = o(f"{n:02d}-c{i + 1}.png")
    if fig:
        gen.figure_card(f(fig), "示意", paras, out, figure_height=fh, title=title, title_num=num,
                        annot_size=FS.get(n, 30), annot_lh=1.55)
    else:
        gen.text_card(title, paras, out, title_num=num)

if want(14):
    gen.tail_card(REFS, o("14-tail.png"))
print("done")
