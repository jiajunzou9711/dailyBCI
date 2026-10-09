# -*- coding: utf-8 -*-
"""解析参考文献并联网查期刊元数据(Crossref),保存到 refs_meta.json"""
import re, json, time, sys
import requests

SRC = "脑机接口外设0820初稿_整理版.md"

text = open(SRC, encoding="utf-8").read()
# 取参考文献部分
ref_part = text.split("## 参考文献")[1]
refs = []
for m in re.finditer(r'^(\d+)\.\s\[(.*)\]\((.*)\)\s*$', ref_part, re.M):
    num = int(m.group(1))
    title = m.group(2).strip()
    url = m.group(3).strip()
    refs.append((num, title, url))

print(f"共解析 {len(refs)} 条参考文献")

# 非期刊来源的 URL 特征
NON_JOURNAL = [
    "fda.gov", "neurable.com", "yjj.sh.gov.cn", "support.apple.com",
    "businesswire.com", "clinicaltrials.gov", "neuralink.com", "cmde.org.cn",
    "accessdata.fda.gov", "gtec.at", "nextsense.io", "iduntechnologies.com",
    "emotiv.com",
]

def classify(url):
    if "clinicaltrials.gov" in url:
        return "DB_OL"
    if any(k in url for k in NON_JOURNAL):
        return "EB_OL"
    return "JOURNAL"

def extract_ids(url):
    """返回 (doi, pmid, pmcid) 或 None"""
    doi = pm = pmc = None
    m = re.search(r'doi\.org/(10\.\S+)', url)
    if m:
        doi = m.group(1).rstrip('/')
    m = re.search(r'pubmed\.ncbi\.nlm\.nih\.gov/(\d+)', url)
    if m:
        pm = m.group(1)
    m = re.search(r'pmc\.ncbi\.nlm\.nih\.gov/articles/(PMC\d+)', url)
    if m:
        pmc = m.group(1)
    return doi, pm, pmc

results = []
for num, title, url in refs:
    cls = classify(url)
    doi, pm, pmc = extract_ids(url)
    results.append({"num": num, "title": title, "url": url, "cls": cls,
                    "doi": doi, "pmid": pm, "pmcid": pmc})

# 打印分类汇总
from collections import Counter
print(Counter(r["cls"] for r in results))

json.dump(results, open("refs_meta.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("已保存 refs_meta.json")
