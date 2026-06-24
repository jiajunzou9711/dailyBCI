# -*- coding: utf-8 -*-
# 专题② 电极材料 Parylene-C vs Polyimide — 全 9 卡(官方 card_generator 范式 + 自制 SVG 示意图)
import os, sys, subprocess
ROOT = "/Users/zoujiajun/Desktop/dailylife/dailyBCI"
sys.path.insert(0, os.path.join(ROOT, ".claude/skills/dailybci/scripts"))
from card_generator import CardGenerator

DIAG = os.path.join(ROOT, "papers/mat2-diagrams"); os.makedirs(DIAG, exist_ok=True)
OUT = os.path.join(ROOT, "output/series-electrode-materials"); os.makedirs(OUT, exist_ok=True)
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
NAVY="#2F6DB5"; INK="#1A1A1A"; GREY="#666666"; FAINT="#9A9A9A"; HAIR="#D9D9D9"; WARM="#B5832E"; RED="#B24A3A"; METAL="#8A8F96"

def render_svg(svg, name, w, h):
    hp = os.path.join(DIAG, name+".html")
    open(hp,"w").write(f"<!doctype html><meta charset=utf-8><style>*{{margin:0}}body{{width:{w}px;height:{h}px}}"
        f"text{{font-family:'PingFang SC','Helvetica Neue',Arial}}</style>{svg}")
    out = os.path.join(DIAG, name+".png")
    subprocess.run([CHROME,"--headless","--disable-gpu","--hide-scrollbars",
        "--force-device-scale-factor=2","--window-size=%d,%d"%(w,h),
        "--screenshot="+out,"file://"+hp], capture_output=True)
    return out

W=920
def head(svg): return f'<svg width="{W}" height="{svg}" viewBox="0 0 {W} {svg}" xmlns="http://www.w3.org/2000/svg"><rect width="{W}" height="{svg}" fill="#FFFFFF"/>'
def vline(h): return f'<line x1="460" y1="36" x2="460" y2="{h-30}" stroke="{HAIR}" stroke-width="1.5" stroke-dasharray="4 6"/>'

# ---------- 03 角色总览 ----------
svg03 = f"""<svg width="920" height="470" viewBox="0 0 920 470" xmlns="http://www.w3.org/2000/svg">
<rect width="920" height="470" fill="#FFFFFF"/>{vline(470)}
<text x="230" y="50" font-size="25" fill="{NAVY}" font-weight="700" text-anchor="middle">Parylene-C</text>
<text x="230" y="84" font-size="20" fill="{GREY}" text-anchor="middle">薄外衣 · 裹在(常是刚性)电极外</text>
<rect x="206" y="120" width="48" height="240" fill="#C9CDD2"/>
<rect x="196" y="120" width="10" height="248" fill="{NAVY}" opacity="0.85"/>
<rect x="254" y="120" width="10" height="248" fill="{NAVY}" opacity="0.85"/>
<rect x="196" y="360" width="68" height="10" fill="{NAVY}" opacity="0.85"/>
<polygon points="206,120 254,120 230,96" fill="#C9CDD2"/>
<rect x="222" y="96" width="16" height="14" fill="{RED}"/>
<text x="300" y="106" font-size="19" fill="{RED}">尖端开窗露触点</text>
<text x="300" y="252" font-size="19" fill="{GREY}">整根包一层薄绝缘</text>
<text x="690" y="50" font-size="25" fill="{WARM}" font-weight="700" text-anchor="middle">Polyimide</text>
<text x="690" y="84" font-size="20" fill="{GREY}" text-anchor="middle">结构身体 · 夹住金属走线的柔性膜</text>
<rect x="520" y="180" width="340" height="22" rx="4" fill="{WARM}" opacity="0.30"/>
<rect x="520" y="202" width="340" height="16" rx="2" fill="{METAL}"/>
<rect x="520" y="218" width="340" height="22" rx="4" fill="{WARM}" opacity="0.30"/>
<text x="876" y="196" font-size="18" fill="{WARM}" text-anchor="end">PI</text>
<text x="700" y="290" font-size="18" fill="{METAL}" text-anchor="middle">金属走线</text>
<line x1="700" y1="218" x2="700" y2="278" stroke="{METAL}" stroke-width="1"/>
<text x="690" y="340" font-size="19" fill="{GREY}" text-anchor="middle">PI–金属–PI 三明治,膜本身即电极的"身体"</text>
</svg>"""

# ---------- 04 成膜方式 ----------
gasdots = "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="{NAVY}" opacity="0.55"/>'
    for x,y in [(150,70),(200,55),(260,75),(310,60),(180,110),(250,120),(300,105),(160,150),(290,150)])
svg04 = f"""<svg width="920" height="470" viewBox="0 0 920 470" xmlns="http://www.w3.org/2000/svg">
<rect width="920" height="470" fill="#FFFFFF"/>{vline(470)}
<text x="230" y="50" font-size="25" fill="{NAVY}" font-weight="700" text-anchor="middle">气相沉积</text>
<text x="230" y="82" font-size="20" fill="{GREY}" text-anchor="middle">室温 · 飘上去凝成共形薄膜</text>
{gasdots}
<line x1="230" y1="165" x2="230" y2="195" stroke="{NAVY}" stroke-width="2" marker-end="url(#a)"/>
<defs><marker id="a" markerWidth="8" markerHeight="8" refX="4" refY="6" orient="auto"><path d="M0,0 L4,7 L8,0" fill="{NAVY}"/></marker></defs>
<rect x="212" y="210" width="36" height="180" fill="#C9CDD2"/>
<rect x="205" y="210" width="7" height="186" fill="{NAVY}" opacity="0.85"/>
<rect x="248" y="210" width="7" height="186" fill="{NAVY}" opacity="0.85"/>
<rect x="205" y="390" width="50" height="7" fill="{NAVY}" opacity="0.85"/>
<polygon points="212,210 248,210 230,190" fill="#C9CDD2"/>
<text x="230" y="430" font-size="19" fill="{GREY}" text-anchor="middle">裹住三维针每一面</text>
<text x="690" y="50" font-size="25" fill="{WARM}" font-weight="700" text-anchor="middle">液相旋涂 + 高温固化</text>
<text x="690" y="82" font-size="20" fill="{GREY}" text-anchor="middle">摊在平整晶圆 → 烤硬成结构膜</text>
<defs><marker id="b" markerWidth="9" markerHeight="9" refX="4" refY="4" orient="auto"><path d="M0,0 L9,4 L0,8" fill="{WARM}"/></marker></defs>
<path d="M712,128 a24,24 0 1,1 -12,-20" fill="none" stroke="{WARM}" stroke-width="2.5" marker-end="url(#b)"/>
<text x="690" y="116" font-size="16" fill="{WARM}" text-anchor="middle">旋涂</text>
<ellipse cx="690" cy="170" rx="150" ry="14" fill="{WARM}" opacity="0.28"/>
<rect x="540" y="250" width="300" height="14" fill="#C9CDD2"/>
<rect x="540" y="236" width="300" height="14" rx="3" fill="{WARM}" opacity="0.55"/>
<text x="868" y="300" font-size="22" fill="{RED}" text-anchor="end">≈300°C 烤</text>
<text x="690" y="430" font-size="19" fill="{GREY}" text-anchor="middle">平整、厚、硬挺的结构膜</text>
</svg>"""

# ---------- 05 软硬 vs 耐热 ----------
def bar(x,h,color,label,val,maxlabel=None):
    y=300-h
    s=f'<rect x="{x}" y="{y}" width="70" height="{h}" rx="3" fill="{color}"/>'
    s+=f'<text x="{x+35}" y="{y-12}" font-size="20" fill="{INK}" text-anchor="middle" font-weight="700">{val}</text>'
    s+=f'<text x="{x+35}" y="332" font-size="19" fill="{GREY}" text-anchor="middle">{label}</text>'
    return s
svg05 = f"""<svg width="920" height="400" viewBox="0 0 920 400" xmlns="http://www.w3.org/2000/svg">
<rect width="920" height="400" fill="#FFFFFF"/>
<text x="230" y="40" font-size="23" fill="{INK}" font-weight="700" text-anchor="middle">刚度 · 杨氏模量 (GPa)</text>
<line x1="80" y1="300" x2="400" y2="300" stroke="{HAIR}" stroke-width="2"/>
{bar(150,150,NAVY,'Parylene-C','~3.2')}{bar(270,118,WARM,'Polyimide','~2.5')}
<text x="240" y="120" font-size="22" fill="{GREY}" text-anchor="middle">≈ 接近</text>
<path d="M170,150 q70,-26 140,0" fill="none" stroke="{FAINT}" stroke-width="1.5"/>
<text x="690" y="40" font-size="23" fill="{INK}" font-weight="700" text-anchor="middle">耐热 · 玻璃化温度 (°C)</text>
<line x1="540" y1="300" x2="860" y2="300" stroke="{HAIR}" stroke-width="2"/>
{bar(610,72,NAVY,'Parylene-C','~150')}{bar(730,170,WARM,'Polyimide','>300')}
<text x="690" y="96" font-size="22" fill="{RED}" text-anchor="middle">差距大</text>
</svg>"""

# ---------- 06 可图案化 ----------
windows06 = "".join(f'<rect x="{x}" y="196" width="22" height="14" fill="#FFFFFF"/><rect x="{x}" y="210" width="22" height="6" fill="{RED}"/>' for x in [150,230,310])
svg06 = f"""<svg width="920" height="470" viewBox="0 0 920 470" xmlns="http://www.w3.org/2000/svg">
<rect width="920" height="470" fill="#FFFFFF"/>{vline(470)}
<text x="230" y="50" font-size="25" fill="{WARM}" font-weight="700" text-anchor="middle">Polyimide:可光刻</text>
<text x="230" y="82" font-size="20" fill="{GREY}" text-anchor="middle">把电路一层层造进膜里</text>
<rect x="110" y="150" width="240" height="22" rx="3" fill="{WARM}" opacity="0.30"/>
<rect x="110" y="172" width="240" height="24" fill="{METAL}"/>
{windows06}
<rect x="110" y="216" width="240" height="22" rx="3" fill="{WARM}" opacity="0.30"/>
<text x="230" y="285" font-size="19" fill="{GREY}" text-anchor="middle">PI–金属–PI,精确开多个窗</text>
<text x="230" y="312" font-size="19" fill="{GREY}" text-anchor="middle">一张膜排几百上千条走线</text>
<text x="690" y="50" font-size="25" fill="{NAVY}" font-weight="700" text-anchor="middle">Parylene:整体镀 + 激光开窗</text>
<text x="690" y="82" font-size="20" fill="{GREY}" text-anchor="middle">给做好的刚性电极裹绝缘皮</text>
<rect x="666" y="150" width="48" height="200" fill="#C9CDD2"/>
<rect x="656" y="150" width="10" height="208" fill="{NAVY}" opacity="0.85"/>
<rect x="714" y="150" width="10" height="208" fill="{NAVY}" opacity="0.85"/>
<rect x="656" y="350" width="68" height="10" fill="{NAVY}" opacity="0.85"/>
<polygon points="666,150 714,150 690,126" fill="#C9CDD2"/>
<rect x="682" y="126" width="16" height="13" fill="{RED}"/>
<line x1="770" y1="146" x2="702" y2="130" stroke="{RED}" stroke-width="2" stroke-dasharray="3 3"/>
<text x="852" y="152" font-size="18" fill="{RED}" text-anchor="end">激光只开尖端一个窗</text>
</svg>"""

# ---------- 07 体液失效 ----------
drops_left = "".join(f'<circle cx="{x}" cy="{y}" r="5" fill="{NAVY}" opacity="0.5"/>' for x,y in [(250,250),(270,275),(245,295)])
drops_right = "".join(f'<circle cx="{x}" cy="{y}" r="5" fill="{WARM}" opacity="0.65"/>' for x,y in [(640,200),(700,210),(760,200),(660,250),(730,255),(700,290)])
svg07 = f"""<svg width="920" height="430" viewBox="0 0 920 430" xmlns="http://www.w3.org/2000/svg">
<rect width="920" height="430" fill="#FFFFFF"/>{vline(430)}
<text x="230" y="48" font-size="24" fill="{NAVY}" font-weight="700" text-anchor="middle">Parylene-C:翘边脱层</text>
<text x="230" y="80" font-size="20" fill="{GREY}" text-anchor="middle">吸水极低(~0.1%)但附着差</text>
<rect x="120" y="200" width="220" height="40" fill="#C9CDD2"/>
<path d="M120,200 q-26,-44 30,-60 L340,140 L340,200 Z" fill="{NAVY}" opacity="0.6"/>
<path d="M120,200 L340,200" stroke="{NAVY}" stroke-width="3"/>
{drops_left}
<text x="230" y="300" font-size="19" fill="{GREY}" text-anchor="middle">外衣从一端翘起→水钻进缝里</text>
<text x="690" y="48" font-size="24" fill="{WARM}" font-weight="700" text-anchor="middle">Polyimide:吸水溶胀</text>
<text x="690" y="80" font-size="20" fill="{GREY}" text-anchor="middle">更吸水(~1–3%,旧 Kapton ~2.8%)</text>
<rect x="560" y="170" width="260" height="60" rx="20" fill="{WARM}" opacity="0.35"/>
{drops_right}
<text x="690" y="300" font-size="19" fill="{GREY}" text-anchor="middle">膜吸水变胖、层间松动</text>
</svg>"""

# ---------- 08 为什么不密封 + 双层 ----------
chains = "".join(f'<path d="M120,{y} q30,-12 60,0 t60,0 t60,0 t60,0" fill="none" stroke="{FAINT}" stroke-width="3"/>' for y in [150,180,210])
wpass = "".join(f'<circle cx="{x}" cy="{y}" r="5" fill="{NAVY}"/>' for x,y in [(170,165),(230,195),(300,170)])
bounce = "".join(f'<circle cx="{x}" cy="{y}" r="5" fill="{NAVY}"/>' for x,y in [(610,150),(640,135),(760,150),(790,138)])
svg08 = f"""<svg width="920" height="470" viewBox="0 0 920 470" xmlns="http://www.w3.org/2000/svg">
<rect width="920" height="470" fill="#FFFFFF"/>{vline(300)}
<text x="230" y="44" font-size="23" fill="{INK}" font-weight="700" text-anchor="middle">高分子:挡不住</text>
{chains}{wpass}
<line x1="230" y1="120" x2="230" y2="244" stroke="{NAVY}" stroke-width="2" stroke-dasharray="4 4" marker-end="url(#d)"/>
<defs><marker id="d" markerWidth="8" markerHeight="8" refX="4" refY="6" orient="auto"><path d="M0,0 L4,7 L8,0" fill="{NAVY}"/></marker></defs>
<text x="230" y="276" font-size="18" fill="{GREY}" text-anchor="middle">链间有自由体积→溶解-扩散渗过</text>
<text x="690" y="44" font-size="23" fill="{INK}" font-weight="700" text-anchor="middle">致密陶瓷/金属:真挡</text>
<rect x="560" y="160" width="260" height="90" fill="#3A4250"/>
{bounce}
<text x="690" y="276" font-size="18" fill="{GREY}" text-anchor="middle">几无自由体积→水进不去</text>
<line x1="60" y1="320" x2="860" y2="320" stroke="{HAIR}" stroke-width="1"/>
<text x="460" y="358" font-size="22" fill="{INK}" font-weight="700" text-anchor="middle">犹他阵列的折中:双层封装</text>
<rect x="330" y="380" width="260" height="16" fill="#C9CDD2"/>
<rect x="330" y="368" width="260" height="12" fill="#3A4250"/>
<rect x="330" y="356" width="260" height="12" fill="{NAVY}" opacity="0.6"/>
<text x="610" y="366" font-size="17" fill="{NAVY}" text-anchor="start">Parylene</text>
<text x="610" y="380" font-size="17" fill="#3A4250" text-anchor="start">ALD-Al₂O₃</text>
<text x="460" y="424" font-size="18" fill="{GREY}" text-anchor="middle">氧化铝挡水汽 + Parylene 护住它 → 寿命约 3×</text>
</svg>"""

figs = {n: render_svg(s, n, W, int(s.split('height="')[1].split('"')[0]))
        for n,s in [("diag03",svg03),("diag04",svg04),("diag05",svg05),("diag06",svg06),("diag07",svg07),("diag08",svg08)]}

gen = CardGenerator(date="2026.06 · 材料篇", platform="xiaohongshu")

gen.cover_card("电极上的两种", "绝缘高分子",
    "Parylene-C 和 Polyimide,为什么一个常当“外衣”、一个常当“身体”?",
    os.path.join(OUT,"01-cover.png"),
    source="脑电极的绝缘要用高分子。这两种最常见的高分子——Parylene-C 与 Polyimide——差别在哪、各自怎么坏?一篇讲清。")

gen.text_card("先把两个名字分清", [
    "脑电极要在该绝缘的地方挡住电流,常用的就是高分子;其中两种最常被用到,却常被放在完全不同的位置。",
    "**Parylene-C** 多用作一层薄绝缘外衣,裹在做好的电极外面;**Polyimide** 多用作柔性电极的整个身体(基底)。",
    "先避个坑:**Parylene-C ≠ Polyimide ≠ Polyamide**。Parylene-C 是聚对氯二甲苯;Polyimide(PI)是聚酰亚胺;Polyamide 是尼龙,跟前两个不相干,别说错。",
    "同样的活儿,为什么一个常做薄外衣、一个常做骨架?往下看。"],
    os.path.join(OUT,"02-names.png"))

gen.figure_card(figs["diag03"], "示意 · 两种角色", [
    "**主流用法**上,一个常当外衣、一个常当身体——但都不绝对。",
    "如上图,Parylene-C 共形裹在(常是刚性)电极外、只在尖端开窗;Polyimide 做成柔性膜、把金属走线夹在中间,当电极的结构身体。",
    "这是**侧重、不是铁律**:Parylene-C 也有被当柔性基底的工作¹,PI 也能当绝缘层。根源在它俩怎么被“做”上去。"],
    os.path.join(OUT,"03-roles.png"))

gen.figure_card(figs["diag04"], "示意 · 气相 vs 液相", [
    "后面所有区别,都从这一步派生:一个用“气”、一个用“液”。",
    "如上图,Parylene-C 用**气相沉积**——原料变气体、室温飘到电极上凝成薄膜,裹住三维针每一面;Polyimide 用**液相旋涂**——液态摊在平整晶圆、再高温烤硬成结构膜。",
    "“气相薄外衣”和“液相结构膜”两条路,直接决定了谁能当骨架、谁能刻图案、各自怎么坏。"],
    os.path.join(OUT,"04-deposition.png"))

gen.figure_card(figs["diag05"], "示意 · 刚度 vs 耐热", [
    "一个常被误解的点:PI 能当骨架,不是因为更硬。",
    "如上图,论刚度(杨氏模量)两者接近,都在约 **2.5–3.2 GPa**(Parylene-C 还略高)²;真正的分水岭是**耐热**——PI 玻璃化 **>300°C**、Parylene-C 约 **150°C** 内就软²,PI 同厚度下也更韧。",
    "做柔性电极要在基底上镀金属、做多层,都经高温;PI 扛得住,才能当地基。那谁能把电路“刻”进自己身体里?"],
    os.path.join(OUT,"05-stiffness-heat.png"))

gen.figure_card(figs["diag06"], "示意 · 可图案化", [
    "高通道柔性阵列为什么偏爱 PI?答案在这。",
    "如上图,PI **可光刻**——造出“PI–金属–PI”三明治、精确开触点窗,一张膜排几百上千条走线(Neuralink 柔性细线就是 PI 基⁵);Parylene 是**整体共形镀、再激光把尖端开个窗**。",
    "不是精度差异,是“造进去 vs 最后裹一层”的角色差异。那泡在体液里,谁更扛?"],
    os.path.join(OUT,"06-patterning.png"))

gen.figure_card(figs["diag07"], "示意 · 体液里的失效", [
    "体内是 37°C 咸水,绝缘头号敌人是水/离子渗入——两者各有各的死法。",
    "如上图,Parylene-C 本身**吸水极低(约 0.1%)但附着差**、易翘边脱层(常要硅烷打底);Polyimide **更吸水(约 1–3%,旧 Kapton 可达 ~2.8%)、会溶胀**³,且层间附着差。",
    "但更底层的问题是:它俩其实**都不“密封”**。"],
    os.path.join(OUT,"07-failure.png"))

gen.figure_card(figs["diag08"], "示意 · 为什么都不密封", [
    "这是它俩(以及所有高分子绝缘)共同的天花板。",
    "如上图,高分子链间有**自由体积**,水靠**溶解-扩散**一格格渗过(不是漏针孔);致密陶瓷/金属几无自由体积,才算真密封。",
    "所以犹他阵列才在 Parylene 外叠一层 **ALD 氧化铝**——致密层挡水汽、Parylene 护住它,双层寿命约为单层的 **3 倍**⁴。"],
    os.path.join(OUT,"08-no-seal.png"))

gen.tail_card(
    ["¹ de la Oliva N, et al. 2018. Sci Rep 8:5965.",
     "² Hassler C, Boretius T, Stieglitz T. 2011. J Polym Sci B 49(1):18–33.",
     "³ Rubehn B, Stieglitz T. 2010. Biomaterials 31(13):3449–3458.",
     "⁴ Xie X, et al. 2014. J Neural Eng 11(2):026016.",
     "⁵ Musk E & Neuralink. 2019. J Med Internet Res 21(10):e16194."],
    os.path.join(OUT,"09-tail.png"),
    lead_paragraphs=[
     "选 Parylene-C 还是 Polyimide,**由电极的几何形状决定**,不是谁更好:刚性三维针床→只有 Parylene 能共形裹上;平面高通道柔性电极→PI 当可图案化的结构膜。",
     "两者各有失效模式,且都逃不过“高分子不密封”这一根本极限——目前仍没有材料能让电极在脑内长期稳定。要真密封,得靠无机层或金属/陶瓷壳,那是另一条路了。"])

print("ALL ->", OUT)
