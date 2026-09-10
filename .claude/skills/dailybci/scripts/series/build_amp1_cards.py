# -*- coding: utf-8 -*-
"""series-amp-01 · 如何采到准确的脑电 —— 卡片生成"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from card_generator import CardGenerator

PROJ = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", ".."))
OUT = os.path.join(PROJ, "output", "series-amp-01")
FIG = os.path.join(OUT, "figs")
def f(n): return os.path.join(FIG, n + ".png")
def o(n): return os.path.join(OUT, n)

gen = CardGenerator(date="2026.09.10")

gen.cover_card(
    "如何采到",
    "准确的脑电",
    "两条要求，落在同一个分母上。",
    o("01-cover.png"),
    concept_image=f("cover-concept"), concept_height=545,
    title_size=78, title_top=92,
    source="本期不解读某一篇文献，是从第一性原理讲脑电采集对电极与放大器的要求。全篇固定在头皮 EEG 场景。",
)

gen.figure_card(
    f("toc"), "本期路线",
    ["承重出处：头皮电极接触阻抗取自 **Fiedler 等（2023）** Sensors 23:9745——同一顶电极帽上 64 片干电极与 64 片凝胶电极、"
     "10 名健康志愿者同步记录，凝胶 14 ± 8 kΩ、干 516 ± 429 kΩ²；输入阻抗取自 **g.tec** g.USBamp 规格页³；"
     "人体对市电线路与对地的电容取自 **Bednar 等（2021）** Sensors 21:2568 的 Table 2，论文注明为指示值⁴。"
     "V cm、漏进比例、漏进电压与 14.5 MΩ 均为自算，正文已就地注明。"],
    o("02-toc.png"), figure_height=700, annot_size=24,
)

C = [
 dict(n="①", t="记录的目标是把电压差原样搬进文件", fig="fig1-two-electrodes", lab="图 1", fh=450, out="03-c1.png", a=[
   "脑电采集要做的事，是记录头皮上两点之间的电压差。",
   "一个通道对应两片电极：测量电极与参考电极（reference electrode）。通道记录的电压，等于测量位置的电位减去参考位置的电位，头皮上测到的幅度在 10 µV 到 100 µV 之间，随节律与状态变化¹。",
   "由此，「准确」有两条具体要求：**幅度不能变，也不能混进别的东西。**",
   "电极接上放大器的那一刻，这两条都不自动成立。"]),
 dict(n="②", t="接上放大器，读到的电压就变小了", fig="fig2-divider", lab="图 2", fh=380, out="04-c2.png", a=[
   "要读出头皮上的电压，得先把电极接到放大器。这一接，读到的电压就比头皮上的小。",
   "原因在于放大器读电压时，输入端有电流流过。这股电流由整条回路决定：**I ＝ V / (R e ＋ Z in)**。R e 是电极与皮肤的接触阻抗（electrode–skin contact impedance），Z in 是放大器的输入阻抗（input impedance）。",
   "电流流过 R e 会产生压降 I · R e，这部分电压落在电极上。放大器读到的是剩下的：**V 读到 ＝ V × Z in/(R e ＋ Z in)**。",
   "Z in 出现在分母里。**Z in 越大，I 越小；R e 上的压降越小，读数越接近 V。**"]),
 dict(n="②", t="Z in 要大到什么程度", fig="fig3-threshold", lab="图 3", fh=400, out="05-c3.png", a=[
   "上一步的式子可以换个角度读。被扣掉的那部分占多大比例：**误差 ＝ R e / (R e ＋ Z in)**。当 Z in 远大于 R e 时，这个比例约等于 **R e 与 Z in 之比**。",
   "取 0.1% 作为示例的容忍度，Z in 至少要是 R e 的一千倍。代入头皮实测的接触阻抗²：凝胶电极 14 kΩ 要求 Z in > 14 MΩ，干电极 516 kΩ 要求 Z in > 516 MΩ（两项为自算）。",
   "**GΩ 这个要求由两件事决定：电极的接触阻抗有多大，以及你允许多大的幅度误差。**"]),
 dict(n="③", t="差分放大只放大两端之差", fig="fig4-differential", lab="图 4", fh=380, out="06-c4.png", a=[
   "卡 ② 处理的是「幅度不能变」。接下来处理另一条：不能混进别的东西。",
   "干扰进入记录的方式有一个特点：它同时出现在两片电极上，两边的量相差不多。市电在体表造成的电位起伏就是这样。",
   "差分放大器（differential amplifier）的输出只取决于两个输入端的差，G 为增益：**输出 ＝ G · (V₊ − V₋)**。两端共有的那部分在相减时抵消，留下的是两端不同的部分。",
   "**这套做法适合脑电：要记录的量本来就是两点之差，干扰则以共同的形式出现在两端。同一个减法把前者留下，把后者消掉。**"]),
 dict(n="③", t="减法只看电压，不看来源", fig="fig5-two-consequences", lab="图 5", fh=380, out="07-c5.png", a=[
   "那个减法依据的是两个输入端的电压关系。某一份电压来自脑、来自肌肉还是来自市电，放大器读不出来。",
   "由此有两个后果，方向相反。**两片电极共有的脑活动，同样被减掉**：参考越靠近信号源，记录到的幅度越小。**只出现在一端的干扰，同样被完整放大**：眼动、某片电极下的肌肉活动、单片电极自身的漂移都属此类。",
   "所以「差分放大抑制干扰」这句话有前提：**要记录的成分在两端不同，干扰在两端相同。** 这个前提由电极的位置和接触状况决定，放大器本身管不了。"]),
 dict(n="④", t="两端拿到的共模并不相等", fig="fig6-two-paths", lab="图 6", fh=395, out="08-c6.png", a=[
   "卡 ③ 的前提是「干扰在两端相同」。这个前提在电极这一步失效。",
   "干扰在体表是同一份共模电压 V cm。它要到达放大器的两个输入端，得各自经过一片电极，每条通路都是一次分压：**输入端 1 ＝ V cm × Z in/(R e1 ＋ Z in)**，**输入端 2 ＝ V cm × Z in/(R e2 ＋ Z in)**。",
   "分压比由各自的接触阻抗决定。R e1 与 R e2 不相等，两个输入端拿到的共模就不相等。",
   "**差出来的那部分满足「两端不同」这个条件，被当作信号放大。**"]),
 dict(n="④", t="差出来的那部分有多大", fig="fig7-algebra", lab="图 7", fh=380, out="09-c7.png", a=[
   "把两式相减、通分，得到 **ΔV ＝ V cm × Z in × (R e2 − R e1) / [(R e1+Z in)(R e2+Z in)]**。",
   "Z in 远大于两个 R e，分母里两个括号各自约等于 Z in，相乘得 Z in²。分子上的那个 Z in 与它约掉一个，分母里剩下一个 Z in：**ΔV ≈ V cm × (R e2 − R e1) / Z in**。",
   "两片电极接触阻抗之差 R e2 − R e1，称**阻抗失配**。两片贴得一样好，失配为零，ΔV 也为零。",
   "V cm 是公因子，两边同除以它即可约掉。**同一份共模里漏成差模的比例，等于阻抗失配除以输入阻抗。**"]),
 dict(n="④", t="V cm 有多大", fig="fig8-vcm", lab="图 8", fh=380, out="10-c8.png", a=[
   "判据里还剩一个量没有取值：V cm。它指的是两片电极共有的那份电压。",
   "来源是市电。市电线路与人体之间存在寄生电容，人体与大地之间也存在电容，人体串在这条回路里，整体相对仪器零点被抬起一份电压。头上每片电极共有这一份，因此是共模。",
   "取人体对市电线路 2 pF、对地 200 pF 的指示值⁴，市电按 220 V 计，人体被抬起约 2.2 V（自算）。地电极把人体连到仪器零点，回路下臂换成这片电极的接触阻抗²，分压比随之改变。",
   "**地电极用凝胶电极时 V cm 约 1.9 mV，用干电极时约 71 mV**（均为自算）。"]),
 dict(n="④", t="干电极漏进来的电压比脑电还大", fig="fig9-numbers", lab="图 9", fh=395, out="11-c9.png", a=[
   "**阻抗失配**取实测的离散程度：同一顶电极帽、10 名健康志愿者头皮同步记录，凝胶 14 ± 8 kΩ，干电极 516 ± 429 kΩ²。标准差是**同类电极彼此之间**的差异。**输入阻抗**取 14.5 MΩ³。",
   "凝胶电极：失配 8 kΩ，漏进比例 5.5×10⁻⁴，漏进 1.07 µV。干电极：失配 429 kΩ，漏进比例 3.0×10⁻²，漏进 2.11 mV（均为自算）。",
   "对照头皮 EEG 本身，β 活动 10–20 µV⁵。**干电极漏进来的 2.11 mV 是它的上百倍。**"]),
 dict(n="⑤", t="两条要求都是同一个分母上的比值", fig="fig10-two-ratios", lab="图 10", fh=385, out="12-c10.png", a=[
   "回到开头那两条要求。各自的判据都是一个比值：**幅度损失的比例 ＝ R e / Z in**，**共模漏进的比例 ＝ 阻抗失配 / Z in**。",
   "分母是同一个：放大器的输入阻抗。分子都在电极那一侧，一个是接触阻抗本身，另一个是两片电极之间的差。",
   "准确记录要两侧同时满足条件。**仪器一侧能做的是把 Z in 做大；操作一侧能做的是把每片电极贴好，并且贴得一样好。** 任何一侧不到位，另一侧再好也压不住那个比值。",
   "记录前做皮肤准备、涂导电膏、等阻抗读数降下来并趋于一致，压的就是这两个分子。"]),
]

for c in C:
    gen.figure_card(f(c["fig"]), c["lab"], c["a"], o(c["out"]),
                    figure_height=c["fh"], title=c["t"], title_num=c["n"])

gen.tail_card([
  "1. Malmivuo J, Plonsey R. (1995). Bioelectromagnetism: Principles and Applications of Bioelectric and Biomagnetic Fields. Oxford University Press, Chapter 13.",
  "2. Fiedler P, Graichen U, Zimmer E, Haueisen J. (2023). Simultaneous Dry and Gel-Based High-Density Electroencephalography Recordings. Sensors 23(24):9745.",
  "3. g.tec medical engineering. g.USBamp RESEARCH Specs & Features. gtec.at.",
  "4. Bednar T, et al. (2021). Common-Mode Voltage Reduction in Capacitive Sensing of Biosignal Using Capacitive Grounding and DRL Electrode. Sensors 21(7):2568.",
  "5. Nayak CS, Anilkumar AC. (2025). Normal EEG Waveforms. StatPearls. StatPearls Publishing.",
  "",
  "出处说明：文献 3 的规格页标称 >1000 GΩ ∥ 220 pF；正文所用的 14.5 MΩ 为按其并联电容 220 pF 在 50 Hz 下算得的容抗，厂商未给出此数，该电容的定义位置规格页也未写明。文献 4 的电容值经论文注明为指示值。",
  "",
  "自算项：Z in 门槛 14 MΩ 与 516 MΩ；V cm 约 2.2 V（无地电极）、1.9 mV（凝胶）、71 mV（干）；漏进比例 5.5×10⁻⁴ 与 3.0×10⁻²；漏进电压 1.07 µV 与 2.11 mV。原文均未直接给出。",
], o("13-tail.png"), lead_paragraphs=[
  "本期只处理了电极与放大器之间的那一段。两处留着没有展开：输入阻抗随频率变化，规格书上的大数字通常是低频值；以及主动把共模压下去的做法。",
])
print("done")
