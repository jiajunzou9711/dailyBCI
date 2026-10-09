# -*- coding: utf-8 -*-
"""把最终 GB/T 7714 参考文献写回 Markdown 与 DOCX(仅参考文献部分)"""
import re
from docx import Document
from docx.shared import Pt, Cm
from docx.oxml.ns import qn

MD = "脑机接口外设0820初稿_整理版.md"
DOCX = "脑机接口外设0820初稿_整理版.docx"

# 读取最终 97 条
refs = []
for line in open("refs_final2.txt", encoding="utf-8"):
    line = line.strip()
    m = re.match(r'^\[(\d+)\]\s(.+)$', line)
    if m:
        refs.append((int(m.group(1)), m.group(2)))
refs.sort()
print("读取", len(refs), "条参考文献")

# ========== 1. 写回 Markdown ==========
md = open(MD, encoding="utf-8").read()
idx = md.index("## 参考文献")
head = md[:idx]
new_ref_block = "## 参考文献\n\n" + "\n".join(f"[{n}] {c}" for n, c in refs) + "\n"
open(MD, "w", encoding="utf-8").write(head + new_ref_block)
print("Markdown 已更新:", MD)

# ========== 2. 写回 DOCX(原地改参考文献部分) ==========
doc = Document(DOCX)
paras = doc.paragraphs
# 找 "参考文献" 标题段落
ref_idx = None
for i, p in enumerate(paras):
    if p.text.strip() == "参考文献":
        ref_idx = i
        break
if ref_idx is None:
    raise SystemExit("未找到参考文献标题段落")

# 删除标题之后的所有段落(旧参考文献)
body = doc.element.body
# 找到标题段落的 XML 元素之后的兄弟节点并删除
to_delete = []
for el in list(body)[ref_idx + 1:]:
    to_delete.append(el)
for el in to_delete:
    body.remove(el)
print("已删除旧参考文献段落", len(to_delete), "个")

# 追加新参考文献段落(纯文本,悬挂缩进)
SONG = "宋体"
for n, c in refs:
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.line_spacing = 1.3
    pf.space_after = Pt(2)
    pf.left_indent = Cm(1.1)
    pf.first_line_indent = Cm(-1.1)
    run = p.add_run(f"[{n}] {c}")
    run.font.name = SONG
    run._element.rPr.rFonts.set(qn('w:eastAsia'), SONG)
    run.font.size = Pt(10.5)

doc.save(DOCX)
print("DOCX 已更新:", DOCX)
