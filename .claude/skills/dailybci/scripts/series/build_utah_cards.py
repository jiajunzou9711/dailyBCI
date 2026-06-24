# -*- coding: utf-8 -*-
# 专题① 犹他阵列 — 小红书卡片生成 (HTML+CSS+inline SVG -> headless Chrome PNG)
import os, subprocess, html

ROOT = "/Users/zoujiajun/Desktop/dailylife/dailyBCI"
HTMLDIR = os.path.join(ROOT, "papers/cards-utah")
OUTDIR = os.path.join(ROOT, "output/series-utah-array")
os.makedirs(HTMLDIR, exist_ok=True)
os.makedirs(OUTDIR, exist_ok=True)
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

INK = "#1A1A1A"; SEC = "#555555"; FAINT = "#9A9A9A"; HAIR = "#D9D9D9"; NAVY = "#2b3a67"; GREEN="#3f7d5e"
CSS = """
*{margin:0;padding:0;box-sizing:border-box;}
html,body{width:1080px;height:1440px;}
.card{width:1080px;height:1440px;background:#FFFFFF;position:relative;
 padding:96px 92px 120px 92px;
 font-family:"Helvetica Neue","PingFang SC","STHeiti SC","Heiti SC",Arial,sans-serif;
 -webkit-font-smoothing:antialiased;}
.kicker{font-size:25px;letter-spacing:3px;color:#9A9A9A;margin-bottom:34px;}
.h1{font-size:78px;line-height:1.14;color:#1A1A1A;font-weight:600;}
.h1b{font-size:50px;line-height:1.2;color:#1A1A1A;font-weight:600;margin-top:14px;}
.sub{font-size:31px;line-height:1.45;color:#555555;margin-top:26px;font-weight:400;}
.title{font-size:46px;line-height:1.28;color:#1A1A1A;font-weight:600;margin-bottom:40px;}
.p{font-size:31px;line-height:1.62;color:#2a2a2a;margin-bottom:24px;font-weight:400;}
.p.sec{color:#555555;}
.lead{font-size:31px;line-height:1.6;color:#1A1A1A;margin-bottom:22px;font-weight:600;}
.trans{font-size:30px;line-height:1.58;color:#555555;margin-top:26px;font-weight:400;}
.note{font-size:25px;line-height:1.5;color:#9A9A9A;margin-top:22px;}
.ref{font-size:23px;line-height:1.5;color:#9A9A9A;}
.cite{font-size:24px;color:#9A9A9A;}
.foot{position:absolute;left:92px;right:92px;bottom:54px;display:flex;justify-content:space-between;
 font-size:23px;color:#BBBBBB;}
.svgwrap{margin:8px 0 8px 0;}
ul{list-style:none;} li{margin-bottom:18px;}
b{font-weight:600;color:#1A1A1A;}
"""

def page(idx, inner):
    foot = f'<div class="foot"><span>小邹 × Claude · BCI 专题①</span><span>{idx} / 8</span></div>'
    return ("<!doctype html><html><head><meta charset='utf-8'><style>"+CSS+
            "</style></head><body><div class='card'>"+inner+foot+"</div></body></html>")

cards = {}

# 01 封面
cards["01-cover"] = page(1, """
<div class="kicker">BCI 专题① · 人 · 技术 · 商业</div>
<div class="h1">犹他阵列</div>
<div class="h1b">撑起人类脑机接口的那片电极</div>
<div class="sub">它从哪来,又为什么开始被取代<br>——从一篇 2026 新研究的小细节切入</div>
<div style="position:absolute;left:92px;bottom:150px;font-size:26px;color:#BBB;letter-spacing:2px;">小邹 × Claude · 2026.06</div>
""")

# 02 由头
cards["02-hook"] = page(2, """
<div class="title">从一个被忽略的细节说起</div>
<div class="lead">一篇 2026 的人体 BCI 研究里,藏着一个容易被忽略的细节。</div>
<div class="p">匹兹堡 Collinger 组让两名四肢瘫痪者用皮层内 BCI 控制光标,同时做一个费神的记忆任务,测“分心会不会让控制变差”——结论是基本不会。<span class="cite">¹</span></div>
<div class="p">但两人当中,植入约 <b>8 年</b>的那片电极信号质量更差、也更容易被分心影响;只植入 <b>6 个月</b>的那片很稳。</div>
<div class="trans">同样的电极,差别只在“植进去多久”。顺着这片电极,牵出二十多年来人体 BCI 中使用最广泛的一块硬件。</div>
""")

# 03 剖面示意图
svg03 = f"""
<svg class="svgwrap" width="896" height="560" viewBox="0 0 896 560" xmlns="http://www.w3.org/2000/svg">
  <!-- cortex band -->
  <rect x="120" y="250" width="660" height="250" rx="10" fill="#F2F1EE"/>
  <text x="138" y="290" font-size="22" fill="#9A9A9A">大脑皮层</text>
  <!-- base plate -->
  <rect x="250" y="196" width="400" height="26" rx="4" fill="{NAVY}"/>
  <text x="450" y="176" font-size="23" fill="{INK}" text-anchor="middle">硅基板(针床,约 4×4mm)</text>
  <!-- needles -->
  {''.join(f'<line x1="{x}" y1="222" x2="{x}" y2="410" stroke="{NAVY}" stroke-width="5"/><circle cx="{x}" cy="412" r="5" fill="{NAVY}"/>' for x in range(280,651,37))}
  <!-- neuron dots near tips -->
  {''.join(f'<circle cx="{x+14}" cy="{430+((x)%3)*16}" r="6" fill="none" stroke="#B24A3A" stroke-width="2.5"/>' for x in range(280,640,74))}
  <!-- depth bracket -->
  <line x1="700" y1="222" x2="700" y2="412" stroke="#9A9A9A" stroke-width="2"/>
  <line x1="694" y1="222" x2="706" y2="222" stroke="#9A9A9A" stroke-width="2"/>
  <line x1="694" y1="412" x2="706" y2="412" stroke="#9A9A9A" stroke-width="2"/>
  <text x="716" y="324" font-size="23" fill="#555">针长约<tspan x="716" dy="28">1–1.5mm</tspan></text>
  <text x="450" y="540" font-size="23" fill="#B24A3A" text-anchor="middle">○ 尖端记录单个神经元的放电</text>
</svg>
"""
cards["03-anatomy"] = page(3, f"""
<div class="title">它长什么样</div>
<div class="lead">先看清它是什么。</div>
{svg03}
<div class="p">如上图,犹他阵列是一片 <b>10×10=100 根硅微针</b>的“针床”,整片约 4×4mm;每根针长约 1–1.5mm,扎进大脑皮层,尖端记录<b>单个神经元</b>的放电。</div>
<div class="trans">它是二十多年来人体皮层内 BCI 中使用最广泛的记录硬件。但它最初并不是为“读取运动意图”设计的——这要从 1991 年说起。</div>
""")

# 04 时间线  (desc 可为多行列表,SVG 不自动换行)
nodes = [
 ("1991",["犹他大学诞生 · Normann 团队初衷之一是给盲人做“视觉假体”","(刺激视觉皮层、诱发光点),也长期用于动物研究 ²"]),
 ("2001",["被 Cyberkinetics 公司商业化"]),
 ("2004",["首次植入人脑(→ Hochberg 2006, Nature)³"]),
 ("2009",["公司清盘 · 裂成两半"]),
 ("2010s",["分出两条人体研究主线"]),
 ("2020s",["新一代公司纷纷另起炉灶"]),
]
rows=[]
y=66
for yr,lines in nodes:
    rows.append(f'<circle cx="40" cy="{y}" r="11" fill="{NAVY}"/>')
    rows.append(f'<text x="78" y="{y-4}" font-size="30" fill="{INK}" font-weight="600">{yr}</text>')
    for j,ln in enumerate(lines):
        rows.append(f'<text x="78" y="{y+30+j*30}" font-size="24" fill="#555">{ln}</text>')
    y+=124
line=f'<line x1="40" y1="66" x2="40" y2="{66+124*(len(nodes)-1)}" stroke="{HAIR}" stroke-width="3"/>'
svg04=f'<svg class="svgwrap" width="896" height="{66+124*(len(nodes)-1)+60}" viewBox="0 0 896 {66+124*(len(nodes)-1)+60}" xmlns="http://www.w3.org/2000/svg">{line}{"".join(rows)}</svg>'
cards["04-timeline"] = page(4, f"""
<div class="title">它的起点,和今天的用途并不一样</div>
{svg04}
<div class="trans">这条线里最容易让人糊涂的,是 2009 那次“裂变”。</div>
""")

# 05 裂变
svg05 = f"""
<svg class="svgwrap" width="896" height="620" viewBox="0 0 896 620" xmlns="http://www.w3.org/2000/svg">
  <rect x="298" y="20" width="300" height="92" rx="10" fill="#FFFFFF" stroke="{NAVY}" stroke-width="2.5"/>
  <text x="448" y="58" font-size="27" fill="{INK}" text-anchor="middle" font-weight="600">Cyberkinetics</text>
  <text x="448" y="90" font-size="23" fill="#555" text-anchor="middle">2001 · 做出 “BrainGate” 系统</text>
  <line x1="448" y1="112" x2="448" y2="168" stroke="{HAIR}" stroke-width="3"/>
  <text x="448" y="152" font-size="23" fill="#9A9A9A" text-anchor="middle">2009 清盘,资产一分为二</text>
  <line x1="448" y1="168" x2="200" y2="208" stroke="{HAIR}" stroke-width="3"/>
  <line x1="448" y1="168" x2="696" y2="208" stroke="{HAIR}" stroke-width="3"/>
  <!-- left: hardware -->
  <rect x="44" y="212" width="380" height="150" rx="10" fill="#F2F1EE"/>
  <text x="70" y="252" font-size="25" fill="{NAVY}" font-weight="600">硬件</text>
  <text x="70" y="292" font-size="24" fill="{INK}">NeuroPort / 犹他阵列</text>
  <text x="70" y="328" font-size="24" fill="#555">→ Blackrock</text>
  <text x="70" y="356" font-size="22" fill="#9A9A9A">(今天卖犹他阵列的就是它)</text>
  <!-- right: name -->
  <rect x="472" y="212" width="380" height="150" rx="10" fill="#F2F1EE"/>
  <text x="498" y="252" font-size="25" fill="{GREEN}" font-weight="600">名字</text>
  <text x="498" y="292" font-size="24" fill="{INK}">“BrainGate”</text>
  <text x="498" y="328" font-size="24" fill="#555">→ 学术临床研究联盟</text>
  <text x="498" y="356" font-size="22" fill="#9A9A9A">(不再是一家公司)</text>
</svg>
"""
cards["05-split"] = page(5, f"""
<div class="title">一家公司,裂成两个今天还在用的名字</div>
{svg05}
<div class="p sec">硬件被 Blackrock 收走;“BrainGate”这名字留给了学术界,变成跑临床试验的研究联盟。</div>
<div class="note">注:犹他阵列至今只有 &lt;30 天急性的 FDA 许可,长期植入都按“研究”做,还没有获批上市的慢性皮层内 BCI。</div>
""")

# 06 两脉对照 (SVG 内不用 <b>;仅用 font-weight 属性)
svg06 = f"""
<svg class="svgwrap" width="896" height="470" viewBox="0 0 896 470" xmlns="http://www.w3.org/2000/svg">
  <rect x="20" y="20" width="412" height="430" rx="12" fill="#FFFFFF" stroke="{HAIR}" stroke-width="2"/>
  <rect x="464" y="20" width="412" height="430" rx="12" fill="#FFFFFF" stroke="{HAIR}" stroke-width="2"/>
  <!-- left -->
  <text x="50" y="76" font-size="29" fill="{NAVY}" font-weight="600">BrainGate 一脉</text>
  <text x="50" y="116" font-size="22" fill="#9A9A9A">布朗 / MGH / 斯坦福 等</text>
  <line x1="50" y1="140" x2="402" y2="140" stroke="{HAIR}" stroke-width="1.5"/>
  <text x="50" y="186" font-size="25" fill="#555">重心:把意图解码出来</text>
  <text x="50" y="244" font-size="28" fill="{INK}" font-weight="600">光标</text>
  <text x="50" y="294" font-size="28" fill="{INK}" font-weight="600">→ 手写</text>
  <text x="50" y="344" font-size="28" fill="{INK}" font-weight="600">→ 语音</text>
  <!-- right -->
  <text x="494" y="76" font-size="29" fill="{GREEN}" font-weight="600">匹兹堡 RNEL 一脉</text>
  <text x="494" y="116" font-size="22" fill="#9A9A9A">康复神经工程实验室</text>
  <line x1="494" y1="140" x2="846" y2="140" stroke="{HAIR}" stroke-width="1.5"/>
  <text x="494" y="186" font-size="25" fill="#555">重心:双向</text>
  <text x="494" y="244" font-size="28" fill="{INK}" font-weight="600">高自由度机械臂</text>
  <text x="494" y="300" font-size="28" fill="{INK}" font-weight="600">+ 体感皮层微刺激</text>
  <text x="494" y="350" font-size="28" fill="{INK}" font-weight="600">把触觉送回去</text>
</svg>
"""
cards["06-lineages"] = page(6, f"""
<div class="title">同一块电极,两条独立平行的人体主线</div>
{svg06}
<div class="p sec" style="margin-top:20px;">RNEL = 匹兹堡大学康复神经工程实验室;开头那篇研究就出自这条线。两脉独立平行,不是谁的分支。</div>
<div class="trans">学术界都在“同一块电极之上”做文章;新公司反其道而行——要换的,正是这块电极本身。</div>
""")

# 07 分叉 + 天花板
svg07 = f"""
<svg class="svgwrap" width="896" height="430" viewBox="0 0 896 430" xmlns="http://www.w3.org/2000/svg">
  <rect x="40" y="170" width="220" height="92" rx="10" fill="#FFFFFF" stroke="{NAVY}" stroke-width="2.5"/>
  <text x="150" y="208" font-size="26" fill="{INK}" text-anchor="middle" font-weight="600">犹他阵列</text>
  <text x="150" y="240" font-size="21" fill="#9A9A9A" text-anchor="middle">最底层的基础设施</text>
  {''.join(f'<line x1="260" y1="216" x2="470" y2="{70+i*100}" stroke="{HAIR}" stroke-width="3"/>' for i in range(3))}
  <rect x="470" y="42" width="386" height="76" rx="9" fill="#F2F1EE"/>
  <text x="492" y="78" font-size="24" fill="{INK}">Neuralink · 柔性细线</text>
  <text x="492" y="106" font-size="21" fill="#9A9A9A">机器人植入</text>
  <rect x="470" y="142" width="386" height="76" rx="9" fill="#F2F1EE"/>
  <text x="492" y="178" font-size="24" fill="{INK}">Paradromics · 微丝束</text>
  <text x="492" y="206" font-size="21" fill="#9A9A9A">高通道</text>
  <rect x="470" y="242" width="386" height="76" rx="9" fill="#F2F1EE"/>
  <text x="492" y="278" font-size="24" fill="{INK}">Precision · 不穿刺表面膜</text>
  <text x="492" y="306" font-size="21" fill="#9A9A9A">可逆 · 微创</text>
  <text x="150" y="320" font-size="21" fill="#9A9A9A" text-anchor="middle">…且不止这几家</text>
</svg>
"""
cards["07-divergence"] = page(7, f"""
<div class="title">新公司要换掉的,正是这块电极本身</div>
{svg07}
<div class="p" style="font-size:27px;margin-bottom:14px;">新一代公司判断瓶颈就在这块硬件本身,各自另做电极,共同方向:更多通道、全植入无线、减少刚性硅的长期损伤。</div>
<div class="lead" style="font-size:27px;margin-bottom:12px;">被绕开的硬限制</div>
<ul style="font-size:25px;line-height:1.46;color:#2a2a2a;">
<li>① <b>信号随时间衰减</b>:慢性记录可用电极每约 30 天降约 2%(数据主要为猕猴、含 2 名人类⁴);源于胶质瘢痕把电极与神经元隔开,加上材料退化(人体取出:尖端腐蚀、绝缘开裂脱层⁵)</li>
<li>② <b>通道封顶</b>:人体每片约 96 通道　③ <b>有线经皮基座</b>:感染风险、难全植入</li>
<li>④ <b>固定深度、4×4mm、手工植入</b>,不可规模化　⑤ <b>仅急性许可</b></li>
</ul>
<div class="note" style="margin-top:18px;">注:这只限“慢性人体 BCI”;整个神经科学研究里,Neuropixels、硅探针、微丝阵列同样主流、很多场景更优。</div>
""")

# 08 尾卡
cards["08-tail"] = page(8, """
<div class="title">一个还没解决的老问题</div>
<div class="p">回到开头那片 8 年的电极——它信号变差,正是刚性硅针在脑里多年引起的组织反应与材料退化。</div>
<div class="p">犹他阵列是迄今人体使用记录最长、被验证最多的研究级记录硬件(Blackrock 供货),沿用至今;但长期可靠性有限——信号随时间衰减、个体差异大,取出分析显示所有阵列都有材料退化。</div>
<div class="p">如今硬件这一层已不再收敛于单一标准,而是分化成细线、微丝、表面膜等多条并行路线。真正悬而未决的不是“标准件还是自研”,而是更底层的同一个问题:<b>还没有任何一种电极,能在人脑里长期(数年到数十年)稳定、安全、高带宽地工作</b>。那片 8 年电极的衰减,正是这个未解难题的缩影。</div>
<div style="position:absolute;left:92px;right:92px;bottom:150px;">
<div class="ref" style="border-top:1px solid #E6E6E6;padding-top:18px;">
¹ Canario E, et al. 2026. bioRxiv 2026.06.16.732398.<br>
² Campbell PK, et al. 1991. IEEE Trans Biomed Eng 38(8):758–768.<br>
³ Hochberg LR, et al. 2006. Nature 442:164–171.<br>
⁴ Sponheim C, et al. 2021. J Neural Eng 18(6):066044.<br>
⁵ Woeppel K, et al. 2021. Front Bioeng Biotechnol 9:759711.<br>
<span style="color:#B5B5B5;">史实(Cyberkinetics / Blackrock / NeuroPort 监管)据 FDA 510(k) 数据库及公司、新闻公开资料。</span>
</div></div>
""")

# render
for name, h in cards.items():
    hp = os.path.join(HTMLDIR, name+".html")
    with open(hp,"w") as f: f.write(h)
    out = os.path.join(OUTDIR, name+".png")
    subprocess.run([CHROME,"--headless","--disable-gpu","--hide-scrollbars",
        "--force-device-scale-factor=1","--window-size=1080,1440",
        "--screenshot="+out, "file://"+hp], capture_output=True)
    print("rendered", name, os.path.exists(out))
print("DONE ->", OUTDIR)
