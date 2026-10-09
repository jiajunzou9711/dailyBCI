# -*- coding: utf-8 -*-
"""统计文字部分字数（不含引文角标、不含参考文献）"""
import re

text = open("脑机接口外设0820初稿_整理版.md", encoding="utf-8").read()
lines = text.split("\n")

CITE_RE = re.compile(r'\[[0-9]+(?:[–\-][0-9]+)?(?:,[0-9]+(?:[–\-][0-9]+)?)*\]')


def clean_line(s):
    s = re.sub(r'^#{1,3}\s+', '', s)   # 去标题 # 号
    s = s.replace('**', '')             # 去加粗标记
    s = CITE_RE.sub('', s)              # 去引文角标
    return s


def stats(s):
    t = re.sub(r'\s+', '', s)           # 去所有空白
    han = len(re.findall(r'[\u4e00-\u9fff]', t))
    # Word 风格「字数」：汉字每个计 1，英文单词计 1，数字串计 1
    cjk = len(re.findall(r'[\u4e00-\u9fff]', s))
    en_words = len(re.findall(r'[A-Za-z]+', s))
    digits = len(re.findall(r'\d+', s))
    wordcount = cjk + en_words + digits
    return len(t), han, wordcount


# 按边界划分段落
m = {}
cur = '标题'
for ln in lines:
    s = ln.strip()
    if s.startswith('# 脑机接口外设'):
        m.setdefault('标题', []).append(ln)
        cur = '总引'          # 标题之后、侵入式之前的内容归总引
    elif s.startswith('## （一）'):
        cur = '侵入式'
    elif s.startswith('## （二）'):
        cur = '非侵入式'
    elif s == '## 参考文献':
        cur = '参考文献'
    elif s.startswith('综合来看，侵入式与非侵入式'):
        cur = '结语'
    m.setdefault(cur, []).append(ln)

print("=== 各段字数（均不含引文角标、不含参考文献）===")
print("    口径：字符数=含标点/英文/数字；汉字数=仅汉字；字数=汉字+英文词+数字串")
tot_c = tot_h = tot_w = 0
for key in ['标题', '总引', '侵入式', '非侵入式', '结语']:
    txt = "\n".join(clean_line(l) for l in m.get(key, []))
    c, h, w = stats(txt)
    tot_c += c; tot_h += h; tot_w += w
    print(f"{key:6s}  字符数={c:5d}   汉字数={h:5d}   字数={w:5d}")

print("-" * 55)
print(f"正文合计(标题+总引+侵入式+非侵入式+结语)  字符数={tot_c:5d}   汉字数={tot_h:5d}   字数={tot_w:5d}")

# 侵入式 + 非侵入式 合计
ti = "\n".join(clean_line(l) for l in m['侵入式'])
tn = "\n".join(clean_line(l) for l in m['非侵入式'])
ci, hi, wi = stats(ti)
cn, hn, wn = stats(tn)
print(f"侵入式 + 非侵入式 合计                    字符数={ci+cn:5d}   汉字数={hi+hn:5d}   字数={wi+wn:5d}")
