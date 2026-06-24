# -*- coding: utf-8 -*-
# 专题② 电极材料 — 用官方 card_generator.py 范式出样卡(封面+示意图+尾卡)
import os, sys, subprocess
ROOT = "/Users/zoujiajun/Desktop/dailylife/dailyBCI"
sys.path.insert(0, os.path.join(ROOT, ".claude/skills/dailybci/scripts"))
from card_generator import CardGenerator

DIAG = os.path.join(ROOT, "papers/mat2-diagrams"); os.makedirs(DIAG, exist_ok=True)
OUT = os.path.join(ROOT, "output/series-electrode-materials"); os.makedirs(OUT, exist_ok=True)
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
NAVY="#2F6DB5"; INK="#1A1A1A"; GREY="#666666"; FAINT="#9A9A9A"; HAIR="#D9D9D9"; WARM="#B5832E"

def render_svg(svg, name, w, h):
    hp = os.path.join(DIAG, name+".html")
    open(hp,"w").write(f"<!doctype html><meta charset=utf-8><style>*{{margin:0}}body{{width:{w}px;height:{h}px}}"
        f"text{{font-family:'PingFang SC','Helvetica Neue',Arial}}</style>{svg}")
    out = os.path.join(DIAG, name+".png")
    subprocess.run([CHROME,"--headless","--disable-gpu","--hide-scrollbars",
        "--force-device-scale-factor=2","--window-size=%d,%d"%(w,h),
        "--screenshot="+out,"file://"+hp], capture_output=True)
    return out

# --- 示意图 03:角色总览（左 Parylene 外衣 / 右 PI 基底） ---
svg03 = f"""<svg width="920" height="470" viewBox="0 0 920 470" xmlns="http://www.w3.org/2000/svg">
<rect width="920" height="470" fill="#FFFFFF"/>
<!-- 分割 -->
<line x1="460" y1="40" x2="460" y2="430" stroke="{HAIR}" stroke-width="1.5" stroke-dasharray="4 6"/>
<!-- 左：Parylene 薄外衣裹刚性针 -->
<text x="230" y="50" font-size="25" fill="{NAVY}" font-weight="700" text-anchor="middle">Parylene-C</text>
<text x="230" y="84" font-size="20" fill="{GREY}" text-anchor="middle">薄外衣 · 裹在(常是刚性)电极外</text>
<!-- 针体 -->
<rect x="206" y="120" width="48" height="240" fill="#C9CDD2"/>
<!-- 外衣（左右两条） -->
<rect x="196" y="120" width="10" height="248" fill="{NAVY}" opacity="0.85"/>
<rect x="254" y="120" width="10" height="248" fill="{NAVY}" opacity="0.85"/>
<rect x="196" y="360" width="68" height="10" fill="{NAVY}" opacity="0.85"/>
<!-- 尖端开窗 -->
<polygon points="206,120 254,120 230,96" fill="#C9CDD2"/>
<rect x="222" y="96" width="16" height="14" fill="#B24A3A"/>
<text x="300" y="106" font-size="19" fill="#B24A3A">尖端开窗露触点</text>
<text x="300" y="250" font-size="19" fill="{GREY}">整根包一层</text>
<text x="300" y="276" font-size="19" fill="{GREY}">薄绝缘</text>
<!-- 右：PI 结构膜夹金属走线 -->
<text x="690" y="50" font-size="25" fill="{WARM}" font-weight="700" text-anchor="middle">Polyimide</text>
<text x="690" y="84" font-size="20" fill="{GREY}" text-anchor="middle">结构身体 · 夹住金属走线的柔性膜</text>
<!-- 柔性膜三明治 -->
<rect x="520" y="180" width="340" height="22" rx="4" fill="{WARM}" opacity="0.30"/>
<rect x="520" y="202" width="340" height="16" rx="2" fill="#8A8F96"/>
<rect x="520" y="218" width="340" height="22" rx="4" fill="{WARM}" opacity="0.30"/>
<text x="876" y="196" font-size="18" fill="{WARM}" text-anchor="end">PI</text>
<text x="876" y="288" font-size="18" fill="#8A8F96" text-anchor="end">金属走线</text>
<line x1="700" y1="218" x2="700" y2="280" stroke="#8A8F96" stroke-width="1"/>
<text x="690" y="340" font-size="19" fill="{GREY}" text-anchor="middle">PI–金属–PI 三明治,膜本身即电极的"身体"</text>
</svg>"""
fig03 = render_svg(svg03, "diag03", 920, 470)

gen = CardGenerator(date="2026.06 · 材料篇", platform="xiaohongshu")

# 01 封面
gen.cover_card("电极上的两种", "绝缘高分子",
    "Parylene-C 和 Polyimide,为什么一个常当“外衣”、一个常当“身体”?",
    os.path.join(OUT, "01-cover.png"),
    source="脑电极的绝缘要用高分子。这两种最常见的高分子——Parylene-C 与 Polyimide——差别在哪、各自怎么坏?一篇讲清。")

# 03 角色总览（figure_card）
gen.figure_card(fig03, "示意 · 两种角色",
    ["**主流用法**上,一个常当外衣、一个常当身体——但都不绝对。",
     "如上图,Parylene-C 共形裹在做好的(常是刚性)电极外、只在尖端开窗;Polyimide 做成柔性膜、把金属走线夹在中间,当电极的结构身体。",
     "这是**侧重、不是铁律**:Parylene-C 也有被当柔性基底的工作¹,PI 也能当绝缘层。根源在它俩怎么被“做”上去。"],
    os.path.join(OUT, "03-roles.png"))

# 09 尾卡
gen.tail_card(
    ["¹ de la Oliva N, et al. 2018. Sci Rep 8:5965.",
     "² Hassler C, Boretius T, Stieglitz T. 2011. J Polym Sci B 49(1):18–33.",
     "³ Rubehn B, Stieglitz T. 2010. Biomaterials 31(13):3449–3458.",
     "⁴ Xie X, et al. 2014. J Neural Eng 11(2):026016.",
     "⁵ Musk E & Neuralink. 2019. J Med Internet Res 21(10):e16194."],
    os.path.join(OUT, "09-tail.png"),
    lead_paragraphs=[
     "选 Parylene-C 还是 Polyimide,**由电极的几何形状决定**,不是谁更好:刚性三维针床→只有 Parylene 能共形裹上;平面高通道柔性电极→PI 当可图案化的结构膜。",
     "两者各有失效模式,且都逃不过“高分子不密封”这一根本极限——目前仍没有材料能让电极在脑内长期稳定。要真密封,得靠无机层或金属/陶瓷壳,那是另一条路了。"])

print("samples ->", OUT)
