# -*- coding: utf-8 -*-
"""组装 GB/T 7714 格式参考文献,输出 refs_final.txt 供审阅"""
import json

data = json.load(open("refs_meta_full.json", encoding="utf-8"))
by_num = {r["num"]: r for r in data}

# 期刊名规范化(原始 -> 干净全称)
JNAME = {
    "Science (New York, N.Y.)": "Science",
    "Science translational medicine": "Science Translational Medicine",
    "Amyotrophic lateral sclerosis : official publication of the World Federation of Neurology Research Group on Motor Neuron Diseases": "Amyotrophic Lateral Sclerosis",
    "Frontiers in neuroscience": "Frontiers in Neuroscience",
    "Journal of medical Internet research": "Journal of Medical Internet Research",
    "Journal of neuroengineering and rehabilitation": "Journal of NeuroEngineering and Rehabilitation",
    "JAMA psychiatry": "JAMA Psychiatry",
    "Sleep medicine": "Sleep Medicine",
    "Journal of sleep research": "Journal of Sleep Research",
    "Scientific reports": "Scientific Reports",
    "Neurorehabilitation and neural repair": "Neurorehabilitation and Neural Repair",
    "Archives of physical medicine and rehabilitation": "Archives of Physical Medicine and Rehabilitation",
    "Journal of neural engineering": "Journal of Neural Engineering",
    "Nature communications": "Nature Communications",
    "PloS one": "PLOS ONE",
    "IEEE transactions on bio-medical engineering": "IEEE Transactions on Biomedical Engineering",
    "Journal of rehabilitation research and development": "Journal of Rehabilitation Research and Development",
    "Lancet (London, England)": "The Lancet",
    "The Lancet. Neurology": "The Lancet Neurology",
    "Annals of neurology": "Annals of Neurology",
    "Clinical neurophysiology : official journal of the International Federation of Clinical Neurophysiology": "Clinical Neurophysiology",
    "Brain research bulletin": "Brain Research Bulletin",
    "Frontiers in robotics and AI": "Frontiers in Robotics and AI",
    "Bioelectronic medicine": "Bioelectronic Medicine",
    "Brain : a journal of neurology": "Brain",
    "Artificial organs": "Artificial Organs",
    "Cognitive neurodynamics": "Cognitive Neurodynamics",
    "Proceedings of the National Academy of Sciences of the United States of America": "Proceedings of the National Academy of Sciences",
    "IEEE transactions on neural systems and rehabilitation engineering : a publication of the IEEE Engineering in Medicine and Biology Society": "IEEE Transactions on Neural Systems and Rehabilitation Engineering",
    "AJOB neuroscience": "AJOB Neuroscience",
    "Frontiers in human neuroscience": "Frontiers in Human Neuroscience",
    "Biomedical engineering letters": "Biomedical Engineering Letters",
}

# 页码/文章号覆盖(efetch 缺页码时用)
PAGE_OVERRIDE = {
    9: "2421", 27: "061005", 30: "eadz9968", 35: "e18554",
    52: "918001", 83: "13", 85: "066022", 94: "051002",
}

# 年份覆盖(线上/印刷年份不一致,按原稿与证据库口径)
YEAR_OVERRIDE = {59: "2023", 64: "2025", 97: "2025"}

# 会议论文 [C]
CONF = {
    62: "2024 46th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC)",
    86: "2025 47th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC)",
}

def fmt_authors(authors):
    if len(authors) > 3:
        return ", ".join(authors[:3]) + ", et al"
    return ", ".join(authors)

def sentence_case(t):
    """把 title case 转成句首大写(保留全大写缩写)"""
    words = t.split()
    out = []
    for i, w in enumerate(words):
        if w.isupper() or (w and w[0].isupper() and len(w) > 1 and w[1:].islower() and i == 0):
            out.append(w)
        elif w.isupper():
            out.append(w)  # 全大写缩写保留
        elif i == 0:
            out.append(w.capitalize())
        else:
            # 保留专有名词缩写(含大写字母的混合词)
            if any(c.isupper() for c in w[1:]):
                out.append(w)
            else:
                out.append(w.lower())
    return " ".join(out)

ACCESS = "2026-08-22"
final = []
for n in range(1, 98):
    r = by_num[n]
    cls = r["cls"]
    if cls == "EB_OL" or cls == "DB_OL":
        final.append((n, cls, r["title"], r["url"]))
        continue
    # 期刊/会议
    meta = r.get("meta")
    if not meta or not meta.get("authors"):
        final.append((n, "MISSING", r["title"], r["url"]))
        continue
    journal = JNAME.get(meta["journal"], meta["journal"])
    authors = fmt_authors(meta["authors"])
    title = meta["title"].rstrip('.')
    year = YEAR_OVERRIDE.get(n, meta["year"])
    vol = meta["volume"]
    issue = meta["issue"]
    page = PAGE_OVERRIDE.get(n, meta["page"])
    if n in CONF:
        # 会议 [C]
        cite = f"{authors}. {title}[C]//{CONF[n]}. {year}: {page}."
    else:
        if issue:
            cite = f"{authors}. {title}[J]. {journal}, {year}, {vol}({issue}):{page}."
        else:
            cite = f"{authors}. {title}[J]. {journal}, {year}, {vol}:{page}."
    final.append((n, "J", cite, meta.get("doi", "")))

with open("refs_final.txt", "w", encoding="utf-8") as f:
    for n, typ, cite, extra in final:
        if typ in ("EB_OL", "DB_OL", "MISSING"):
            f.write(f"[{n}] ({typ}) {cite}\n    URL: {extra}\n")
        else:
            f.write(f"[{n}] {cite}\n")

print("已生成 refs_final.txt，共", len(final), "条")
print("MISSING 条目：", [n for n, t, c, e in final if t == "MISSING"])
print("非期刊条目：", [n for n, t, c, e in final if t in ("EB_OL", "DB_OL")])
