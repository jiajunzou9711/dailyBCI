# -*- coding: utf-8 -*-
"""可靠地联网查期刊元数据:PMID/PMCID 用 NCBI efetch(MEDLINE),DOI 用 Crossref"""
import re, json, time
import requests

HDR = {"User-Agent": "DailyBCI-review/1.0 (mailto:review@example.com)"}
results = json.load(open("refs_meta.json", encoding="utf-8"))

# 无易提取 ID 的期刊条目,手动指定 DOI
HARD_DOI = {
    38: "10.1001/jamaneurol.2022.4847",   # Mitchell JAMA Neurology 2023
    51: "10.1088/1741-2560/12/1/016011",  # Wodlinger J Neural Eng 2015
}

def parse_medline(text):
    """从 MEDLINE 文本提取字段(正确处理续行)"""
    fields = {}
    current = None
    for line in text.split('\n'):
        if line.startswith('      '):  # 6 空格续行
            if current and fields.get(current):
                fields[current][-1] += ' ' + line.strip()
            continue
        m = re.match(r'^([A-Z]{2,4})\s*- (.*)$', line)
        if m:
            tag, val = m.group(1), m.group(2)
            fields.setdefault(tag, []).append(val.strip())
            current = tag
    authors = []
    for fa in fields.get("FAU", []):
        if ", " in fa:
            family, given = fa.split(", ", 1)
            initials = " ".join(w[0] for w in given.replace("-", " ").split() if w)
            authors.append(f"{family} {initials}".strip())
        else:
            authors.append(fa)
    title = " ".join(fields.get("TI", [])).rstrip('.')
    jt = fields.get("JT", [])
    ta = fields.get("TA", [])
    journal = jt[0] if jt else (ta[0] if ta else "")
    vol = fields.get("VI", [""])[0]
    issue = fields.get("IP", [""])[0]
    page = fields.get("PG", [""])[0]
    dp = fields.get("DP", [""])[0]
    year = ""
    m = re.search(r'(\d{4})', dp)
    if m:
        year = m.group(1)
    return {"authors": authors, "title": title, "journal": journal,
            "volume": vol, "issue": issue, "page": page, "year": year}

def efetch_pubmed(pmid):
    url = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?"
           f"db=pubmed&id={pmid}&rettype=medline&retmode=text")
    r = requests.get(url, headers=HDR, timeout=30)
    return parse_medline(r.text)

def efetch_pmc(pmcid):
    url = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?"
           f"db=pmc&id={pmcid}&rettype=medline&retmode=text")
    r = requests.get(url, headers=HDR, timeout=30)
    return parse_medline(r.text)

def cr_by_doi(doi):
    r = requests.get(f"https://api.crossref.org/works/{doi}", headers=HDR, timeout=30)
    m = r.json()["message"]
    authors = []
    for x in m.get("author", []):
        if "family" in x:
            g = x.get("given", "")
            ini = " ".join(w[0] for w in g.replace("-", " ").split() if w)
            authors.append(f"{x['family']} {ini}".strip())
        elif "name" in x:
            authors.append(x["name"])
    title = m.get("title", [""]); title = title[0] if title else ""
    journal = m.get("container-title", [""]); journal = journal[0] if journal else ""
    year = ""
    for k in ("published-print", "published-online", "published", "issued"):
        d = m.get(k, {})
        if d and d.get("date-parts"):
            year = str(d["date-parts"][0][0]); break
    return {"authors": authors, "title": title, "journal": journal,
            "volume": m.get("volume", ""), "issue": m.get("issue", ""),
            "page": m.get("page", ""), "year": year}

def extract_doi(url):
    m = re.search(r'doi\.org/(10\.\S+)', url)
    if m: return m.group(1).rstrip('/')
    m = re.search(r'nature\.com/articles/([\w\-\.]+)', url)
    if m: return "10.1038/" + m.group(1)
    m = re.search(r'nejm\.org/doi/(?:full/|abs/)?(10\.\S+)', url)
    if m: return m.group(1).rstrip('/')
    m = re.search(r'id=(10\.1371/journal\.pone\.\d+)', url)
    if m: return m.group(1)
    m = re.search(r'elifesciences\.org/articles/(\d+)', url)
    if m: return f"10.7554/eLife.{m.group(1)}"
    m = re.search(r'frontiersin\.org/\S+?(10\.\d{4,5}/\S+?)/full', url)
    if m: return m.group(1)
    m = re.search(r'frontiersin\.org/\S+?/(fn\w+\.\d{4}\.\d+)/full', url)
    if m: return m.group(1)
    return None

out = []
for rec in results:
    num = rec["num"]
    if rec["cls"] != "JOURNAL":
        out.append(rec); continue
    url = rec["url"]
    meta = None
    # 1) PMID
    if rec.get("pmid"):
        try:
            meta = efetch_pubmed(rec["pmid"])
        except Exception as e:
            print(f"[{num}] efetch PMID 失败 {e}", flush=True)
    # 2) PMCID
    elif rec.get("pmcid"):
        try:
            meta = efetch_pmc(rec["pmcid"])
        except Exception as e:
            print(f"[{num}] efetch PMCID 失败 {e}", flush=True)
    # 3) DOI
    if meta is None or not meta["authors"]:
        doi = extract_doi(url) or HARD_DOI.get(num)
        if doi:
            try:
                meta = cr_by_doi(doi)
            except Exception as e:
                print(f"[{num}] crossref {doi} 失败 {e}", flush=True)
    rec["meta"] = meta
    out.append(rec)
    if meta and meta.get("authors"):
        au = ", ".join(meta["authors"][:3])
        print(f"[{num}] {au} | {meta['journal']} {meta['year']} {meta['volume']}({meta['issue']}):{meta['page']}", flush=True)
    else:
        print(f"[{num}] 未查到元数据 | {rec['title'][:45]}", flush=True)
    time.sleep(0.15)

json.dump(out, open("refs_meta_full.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("完成 refs_meta_full.json", flush=True)
