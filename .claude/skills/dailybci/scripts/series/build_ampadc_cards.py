# -*- coding: utf-8 -*-
"""2026-11-23 原理期 · 脑电芯片的增益和 ADC 设置 —— 卡片生成

卡 3–12 正文直接从 draft.md「卡片文案」解析，保证成品与定稿一字不差。
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from card_generator import CardGenerator

PROJ = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", ".."))
OUT = os.path.join(PROJ, "output", "2026-11-18-amplify-before-adc")
FIG = os.path.join(OUT, "figs")
DRAFT = os.path.join(OUT, "draft.md")
def f(n): return os.path.join(FIG, n + ".png")
def o(n): return os.path.join(OUT, n)

gen = CardGenerator(date="2026.11.23")
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
        "脑电芯片的",
        "增益和 ADC 设置",
        "先放大，再做模数转换：取整丢掉的差别之后无法恢复。增益和 ADC 位数怎样分配，决定电极端能分辨多小的变化、能容纳多大的电压。",
        o("01-cover.png"),
        concept_image=f("cover"), concept_height=380,
        image_caption="参数来源 Intan RHD2000 数据手册 · TI ADS1299 数据手册（SBAS499C）",
    )

if want(2):
    gen.figure_card(
        f("toc"), "来源",
        ["芯片参数取自 Intan RHD2000 与 TI ADS1299 数据手册；OpenBCI Cyton 信息取自其官方文档。示意参数与派生数值为作者自算。"],
        o("02-toc.png"), figure_height=700,
    )

FIGCARDS = {4: ("fig_adc", "图 1", 400), 7: ("fig_order", "图 2", 440),
            8: ("fig_intan", "图 3", 340), 9: ("fig_clip", "图 4", 380),
            11: ("fig_hp", "图 5", 420), 12: ("fig_routes", "图 6", 380)}
for n in range(3, 13):
    if not want(n): continue
    num, title, paras = card_body(n)
    out = o(f"{n:02d}-c{n-2}.png")
    if n in FIGCARDS:
        fig, lab, fh = FIGCARDS[n]
        gen.figure_card(f(fig), lab, paras, out, figure_height=fh, title=title, title_num=num,
                        annot_size=FS.get(n, 30), annot_lh=LH.get(n, 1.55))
    else:
        gen.text_card(title, paras, out, title_num=num, para_size=FS.get(n, 30), para_lh=LH.get(n, 1.55))

if want(13):
    s13 = re.search(r"### 卡 13 · .*?\n\n(.*?)\n\n参考文献\n(.*?)\n\n##", open(DRAFT, encoding="utf-8").read(), re.S)
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
    gen.tail_card([r.strip() for r in refs.strip().split("\n")], o("13-tail.png"),
                  lead_paragraphs=[conv(x) for x in lead])
print("done")
