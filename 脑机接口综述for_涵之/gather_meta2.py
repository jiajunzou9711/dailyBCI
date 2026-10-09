# -*- coding: utf-8 -*-
"""联网查期刊元数据(Crossref),输出 GB/T 7714 所需字段到 refs_meta_full.json"""
import re, json, time
import requests

HDR = {"User-Agent": "DailyBCI-review/1.0 (mailto:review@example.com)"}
results = json.load(open("refs_meta.json", encoding="utf-8"))

def ncbi_idconv(ids):
    """把 pmid/pmcid 转成 doi"""
    url = f"https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/?ids={ids}&format=json&tool=bcireview&email=review@example.com"
    try:
        r = requests.get(url, headers=HDR, timeout=20)
        rec = r.json().get("records", [])
        for x in rec:
            if x.get("doi"):
                return x["doi"]
    except Exception as e:
        import sys; print("  idconv err:", e, flush=True)
    return None

def cr_by_doi(doi):
    r = requests.get(f"https://api.crossref.org/works/{doi}", headers=HDR, timeout=20)
    return r.json()["message"]

def cr_by_title(title):
    r = requests.get("https://api.crossref.org/works",
                     params={"query.bibliographic": title, "rows": 3}, headers=HDR, timeout=20)
    items = r.json()["message"]["items"]
    return items

def extract_doi(url):
    # 直接 doi.org
    m = re.search(r'doi\.org/(10\.\S+)', url)
    if m: return m.group(1).rstrip('/')
    # nature.com/articles/XXXX -> 10.1038/XXXX
    m = re.search(r'nature\.com/articles/(s\d{3}\d{2}-\d{3}\d{2}-\d{4,5}[\w\-]+)', url)
    if m: return "10.1038/" + m.group(1)
    # nejm.org/doi/10.XXX
    m = re.search(r'nejm\.org/doi/(?:full/|abs/)?(10\.\S+)', url)
    if m: return m.group(1).rstrip('/')
    # plos
    m = re.search(r'id=(10\.1371/journal\.pone\.\d+)', url)
    if m: return m.group(1)
    # elifesciences
    m = re.search(r'elifesciences\.org/articles/(\d+)', url)
    if m: return f"10.7554/eLife.{m.group(1)}"
    # frontiersin: 10.XXXX/fnbot.2022.XXXX/full
    m = re.search(r'(10\.\d{4,5}/fn\w+\.\d{4}\.\d+)/full', url)
    if m: return m.group(1)
    # frontiersin alt: 10.3389/...
    m = re.search(r'/articles/(10\.3389/\S+?)/full', url)
    if m: return m.group(1)
    # jamanetwork
    m = re.search(r'jamaneurology/fullarticle/(\d+)', url)
    if m:
        # JAMA Neurology 2023 2799839 -> 10.1001/jamaneurol.2022.4847
        # 无法直接由 id 推 doi，交给 title 查询
        return None
    # pnas, sciencemag, etc. 走 title
    return None

def get_meta(rec):
    """从 Crossref message 提取字段"""
    a = rec.get("author", [])
    authors = []
    for x in a:
        if "family" in x:
            g = x.get("given", "")
            initials = " ".join(w[0] for w in g.replace("-", " ").split() if w)
            authors.append(f"{x['family']} {initials}".strip())
        elif "name" in x:
            authors.append(x["name"])
    title = rec.get("title", [""])
    title = title[0] if title else ""
    journal = rec.get("container-title", [""])
    journal = journal[0] if journal else ""
    vol = rec.get("volume", "")
    issue = rec.get("issue", "")
    page = rec.get("page", "")
    # 年份
    year = ""
    for k in ("published-print", "published-online", "published", "issued"):
        d = rec.get(k, {})
        if d and d.get("date-parts"):
            year = d["date-parts"][0][0]
            break
    return {"authors": authors, "title": title, "journal": journal,
            "volume": vol, "issue": issue, "page": page, "year": year,
            "doi": rec.get("DOI", "")}

out = []
for rec in results:
    num = rec["num"]
    if rec["cls"] != "JOURNAL":
        out.append(rec)
        continue
    url = rec["url"]
    doi = extract_doi(url)
    if not doi and rec.get("pmid"):
        doi = ncbi_idconv(rec["pmid"])
    if not doi and rec.get("pmcid"):
        doi = ncbi_idconv(rec["pmcid"])
    meta = None
    if doi:
        try:
            meta = get_meta(cr_by_doi(doi))
        except Exception as e:
            import sys; print(f"[{num}] doi={doi} 失败: {e}", flush=True)
    if meta is None:
        # 用标题查询
        t = rec["title"]
        # 去掉 "作者 et al. " 前缀和 ", 期刊, 年份" 后缀
        t = re.sub(r'^[A-Z][\w\'\-]*(?: et al\.| & [A-Z][\w\'\-]*)+\.?\s+', '', t)
        t = re.sub(r'\.\s*[A-Z][^,]*,\s*\d{4}.*$', '', t)
        try:
            items = cr_by_title(t)
            if items:
                meta = get_meta(items[0])
        except Exception as e:
            import sys; print(f"[{num}] 标题查询失败: {e}", flush=True)
    rec["meta"] = meta
    out.append(rec)
    # 打印进度
    if meta:
        au = ", ".join(meta["authors"][:3])
        import sys; print(f"[{num}] {au} et al. {meta['journal']} {meta['year']} {meta['volume']}({meta['issue']}):{meta['page']}", flush=True)
    else:
        import sys; print(f"[{num}] 未查到: {rec['title'][:50]}", flush=True)
    time.sleep(0.2)

json.dump(out, open("refs_meta_full.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
import sys; print("完成，保存 refs_meta_full.json", flush=True)
