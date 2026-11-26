# -*- coding: utf-8 -*-
"""2026-11-25 原理期 · 电极材料怎样影响记录到的电位 —— 卡片生成

卡 1–10 正文直接从 draft.md「正文」解析，保证成品与定稿一字不差（去掉〔配图〕与参考行）。
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from card_generator import CardGenerator

PROJ = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", ".."))
OUT = os.path.join(PROJ, "output", "series-electrode-polarization-drift")
FIG = os.path.join(OUT, "figs")
DRAFT = os.path.join(OUT, "draft.md")
def f(n): return os.path.join(FIG, n + ".png")
def o(n): return os.path.join(OUT, n)

gen = CardGenerator(date="2026.11.25")
SUP = "⁰¹²³⁴⁵⁶⁷⁸⁹"
NUMS = "①②③④⑤⑥⑦⑧⑨⑩"
FS, LH = {}, {}
FH = {1: 270, 2: 300, 7: 330, 10: 290}


def conv(t):
    # 角标前加不换行连接符，避免角标被挤到下一行行首
    return re.sub(rf"(?<=\S)([{SUP}]+)", "⁠\\1", t)


def body_text():
    s = open(DRAFT, encoding="utf-8").read()
    return s[s.index("# 正文"):]


def card_body(n):
    s = body_text()
    m = re.search(rf"^## 卡 {n}(?:（[^）]*）)?：(.+?)$(.*?)(?=^## |\Z)", s, re.S | re.M)
    title, body = m.group(1).strip(), m.group(2)
    paras, bullets = [], []
    def flush():
        if bullets:
            paras.append("\n".join("· " + x for x in bullets)); bullets.clear()
    for ln in body.strip().split("\n"):
        ln = ln.strip()
        if ln.startswith("〔") or ln.startswith("参考"):
            break
        if not ln or ln.startswith("|"):
            flush(); continue
        if ln.startswith("- "):
            bullets.append(ln[2:]); continue
        flush(); paras.append(ln)
    flush()
    return title, [conv(x) for x in paras]


def refs():
    s = body_text()
    out = []
    for ln in s.split("\n"):
        ln = ln.strip()
        if ln.startswith("参考："):
            ln = ln[3:].strip()
        if ln and ln[0] in SUP:
            out.append(ln)
    key = lambda r: int("".join(str(SUP.index(c)) for c in re.match(rf"[{SUP}]+", r).group()))
    return sorted(dict((key(r), r) for r in out).values(), key=key)


ONLY = set(int(x) for x in sys.argv[1:])
def want(n): return not ONLY or n in ONLY

if want(1):
    gen.cover_card(
        "电极材料怎样影响",
        "记录到的电位",
        "电位稳定的 Ag/AgCl 对脑组织有毒，植入电极只能用偏可极化的金属，漂移靠高通滤波去掉。",
        o("01-cover.png"),
        concept_image=f("cover"), concept_height=400,
        image_caption="主要依据 Merrill 2005 · Tallgren 2005 · Dymond 1970",
    )

if want(2):
    gen.figure_card(
        f("toc"), "来源",
        ["依据 Merrill 等 2005（J Neurosci Methods）、Tallgren 等 2005（Clin Neurophysiol）、Dymond 等 1970（J Neurosurg）等，全部出处见末卡。示意图为作者自绘。"],
        o("02-toc.png"), figure_height=760,
    )

for n in range(1, 11):
    if not want(n + 2): continue
    title, paras = card_body(n)
    gen.figure_card(f(f"f{n}"), f"图 {n}", paras, o(f"{n+2:02d}-c{n}.png"),
                    figure_height=FH.get(n, 360), title=title, title_num=NUMS[n - 1],
                    annot_size=FS.get(n, 30), annot_lh=LH.get(n, 1.55))

if want(13):
    gen.tail_card(refs(), o("13-tail.png"))
print("done")
