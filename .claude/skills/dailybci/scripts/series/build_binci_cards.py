# -*- coding: utf-8 -*-
"""2026-11-25 原理期 · 从有限次 trial 估计概率 —— 卡片生成

卡 3–8 正文直接从 draft.md「卡片文案」解析，保证成品与定稿一字不差。
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from card_generator import CardGenerator

PROJ = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", ".."))
OUT = os.path.join(PROJ, "output", "2026-11-19-binomial-ci")
FIG = os.path.join(OUT, "figs")
DRAFT = os.path.join(OUT, "draft.md")
def f(n): return os.path.join(FIG, n + ".png")
def o(n): return os.path.join(OUT, n)

gen = CardGenerator(date="2026.11.25")
FS, LH = {}, {}


def conv(t):
    return re.sub(r"(?<=\S)([¹²³⁴]+)", "⁠\\1", t)


def card_body(n):
    s = open(DRAFT, encoding="utf-8").read()
    m = re.search(rf"^### 卡 {n} · (.+?)$(.*?)(?=^##)", s, re.S | re.M)
    title, body = m.group(1).strip(), m.group(2)
    num = None
    if title[0] in "①②③④⑤⑥":
        num, title = title[0], title[1:].strip()
    paras, bullets = [], []
    def flush():
        if bullets:
            paras.append("\n".join("· " + x for x in bullets)); bullets.clear()
    for ln in body.strip().split("\n"):
        ln = ln.strip()
        if not ln or ln.startswith("|"):
            flush(); continue
        if ln.startswith("- "):
            bullets.append(ln[2:]); continue
        flush(); paras.append(ln)
    flush()
    return num, title, [conv(x) for x in paras]


ONLY = set(int(x) for x in sys.argv[1:])
def want(n): return not ONLY or n in ONLY

if want(1):
    gen.cover_card(
        "从有限次 trial",
        "估计概率",
        "n 个 trial 里答对 k 个：k/n 是点估计，95% 置信区间是所有与观测值相容的 p。Wilson 区间可靠，Wald 区间在 n 小或比例接近 0、1 时失效。",
        o("01-cover.png"),
        concept_image=f("cover"), concept_height=320,
        image_caption="参考 Brown, Cai & DasGupta 2001 · Statistical Science · 示意数据为作者自算",
    )

if want(2):
    gen.figure_card(
        f("toc"), "来源",
        ["统计学结论参考 Brown, Cai & DasGupta（2001, Statistical Science）。文中例子均为示意数字，区间与标准误由作者按公式自算。"],
        o("02-toc.png"), figure_height=700,
    )

FIGCARDS = {3: ("fig_same08", "图 1", 300), 5: ("fig_sampling", "图 2", 320),
            6: ("fig_invert", "图 3", 380), 7: ("fig_wald", "图 4", 310)}
for n in range(3, 9):
    if not want(n): continue
    num, title, paras = card_body(n)
    out = o(f"{n:02d}-c{n-2}.png")
    if n in FIGCARDS:
        fig, lab, fh = FIGCARDS[n]
        gen.figure_card(f(fig), lab, paras, out, figure_height=fh, title=title, title_num=num,
                        annot_size=FS.get(n, 30), annot_lh=LH.get(n, 1.55))
    else:
        gen.text_card(title, paras, out, title_num=num, para_size=FS.get(n, 30), para_lh=LH.get(n, 1.55))

if want(9):
    s13 = re.search(r"### 卡 9 · .*?\n\n(.*?)\n\n参考文献\n(.*?)\n\n##", open(DRAFT, encoding="utf-8").read(), re.S)
    lead_raw, refs = s13.group(1), s13.group(2)
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
    gen.tail_card([r.strip() for r in refs.strip().split("\n")], o("09-tail.png"),
                  lead_paragraphs=[conv(x) for x in lead])
print("done")
