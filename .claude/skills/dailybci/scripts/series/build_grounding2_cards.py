# -*- coding: utf-8 -*-
"""series-grounding-02 · 参考电极与地电极（接地系列·下）—— 卡片生成
2026-09-09 重写版：只回答「参考电极和地电极各自起什么作用」，固定头皮 EEG 场景。
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from card_generator import CardGenerator

PROJ = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", ".."))
OUT = os.path.join(PROJ, "output", "series-grounding-02")
FIG = os.path.join(OUT, "figs")
def f(n): return os.path.join(FIG, n + ".png")
def o(n): return os.path.join(OUT, n)

gen = CardGenerator(date="2026.09.09")

gen.cover_card(
    "参考电极和地电极",
    "到底差在哪",
    "参考电极定义零点，地电极定义放大器的工作条件。",
    o("01-cover.png"),
    concept_image=f("cover-concept"), concept_height=545,
    title_size=78, title_top=92,
    source="本期不解读某一篇文献，是从第一性原理讲生物电记录里的两类电极。全篇固定在头皮 EEG 场景。",
)

gen.figure_card(
    f("toc"), "本期路线",
    ["承重出处：人体对市电线路 2 pF、对地 200 pF 取自 **Bednar 等（2021）** Sensors 21:2568 的 Table 2，"
     "论文注明这些值为指示值、取决于测量方法与环境¹；电极接触阻抗取自 **Chi 等（2010）** IEEE Rev Biomed Eng 3:106–119 的 Table I，"
     "为前臂静息、未做皮肤准备的实测值²。分压结果 2.2 V 与 45 倍为自算，正文已就地注明。"],
    o("02-toc.png"), figure_height=700, annot_size=25,
)

C = [
 dict(n="①", t="记录测的是两处的电压差", fig="fig2-two-points", lab="图 1", fh=450, out="03-c1.png", a=[
   "场景固定：电极帽贴在头皮上，导线接到一台差分放大器。",
   "神经元活动时离子跨膜移动，胞外出现电流，电流在头组织里流动。组织有电阻，所以上一期那条 **U ＝ I·R** 在这里生效：电流流过有电阻的介质，介质里就出现电位差。头皮上因此存在一张随时间变化的电位分布。",
   "这张分布图能给你的，只有**任意两点之间差多少**。上一期讲过，电位是省略句，选定同一个零点之后才有数字，而两点之差与零点选在哪无关。",
   "所以头皮上必须贴两片电极。这是被测量本身的性质决定的：电压只存在于一对位置之间。**一片叫测量电极，一片叫参考电极。**"]),
 dict(n="②", t="参考位置会影响记录结果", fig="fig4-ref-into-all", lab="图 2", fh=430, out="04-c2.png", a=[
   "参考电极（reference electrode）常被理解为一个电位为零的位置。头皮上没有这样的位置。因此，一个通道记录的是 **通道 i ＝ V i (t) − V ref (t)**。",
   "V ref (t) 是一条完整的信号，它被同时减进每一个通道。换一个参考位置，减去的信号变了，每一道波形也跟着变。",
   "参考位置由此受两条方向相反的要求约束。**第一，参考不能带着我们要记录的信号**：减法会抵消两个电极共有的成分，参考离源越近，记录到的幅度越小。**第二，参考不能带着别的电活动**：参考位置附近的肌电、心电或眼动会进入每一个通道，容易被误读为一次广泛的脑活动。头面部各处都有这些电场，没有一个位置能同时满足两条。"]),
 dict(n="③", t="放大器怎么完成一次测量", fig="fig7-amp-three-steps", lab="图 3", fh=425, out="05-c3.png", a=[
   "两片电极选定了，是不是就能测到？还不行。差分放大器（differential amplifier）无法直接感知两端之差。它内部的晶体管能否工作，取决于输入端相对**芯片自己的零点**是多少伏。",
   "因此它分三步完成测量。先分别感知两端相对自身零点的电压，**a ＝ V₊ − V amp0**、**b ＝ V₋ − V amp0**；再相减，V amp0 在这一步消去，**a − b ＝ V₊ − V₋**；最后按增益 G 放大。",
   "V amp0 属于机器，不属于人体。它在结果里消掉了，但 a 和 b 是芯片内部真实存在的电压，第三步能否发生取决于前两步能否成立。",
   "**因此 a 和 b 必须落在放大器的输入电压范围内。**"]),
 dict(n="④", t="人体处在浮空状态", fig="fig8-body-floats", lab="图 4", fh=445, out="06-c4.png", a=[
   "人体的电位凭什么落在这个范围里？没有任何东西保证这一点。",
   "市电线路与人体之间存在寄生电容 C₁，人体与大地之间存在电容 C₂，而市电的中性点接地。三者构成一条闭合回路，两个电容串联成分压器：**V body ＝ V m × C₁/(C₁+C₂)**。",
   "电容越小分到的电压越大。取文献给出的指示值 C₁ ＝ 2 pF、C₂ ＝ 200 pF¹，市电按 220 V 计，得 **V body ≈ 2.2 V**（这是我按上述参数算的，原文未直接给出）。",
   "头上所有电极的电位由此一起被抬起约 2 V，幅度相同。两点之差仍然准确，而 a 和 b 跑出了放大器能处理的范围。**电压差是对的，仪器算不出来。**"]),
 dict(n="⑤", t="地电极把人体拽回可测范围", fig="fig9-lower-arm", lab="图 5", fh=415, out="07-c5.png", a=[
   "怎么把人体拉回来？办法是再贴一片电极，用一根导线把人体直接连到 V amp0。这片电极就是地电极。",
   "它把分压器的下臂换掉了。原来人体到大地只有 C₂ 这条通路，200 pF 在 50 Hz 下容抗约 16 MΩ（自算）。接上地电极后多了一条实通路，阻抗是电极的接触阻抗 R e，湿 Ag/AgCl 电极实测 350 kΩ ∥ 25 nF（前臂静息、未做皮肤准备）²。",
   "两者相差约 45 倍，共模电压按同样比例下降，a 和 b 落回可测范围（自算）。",
   "**这片电极不进入任何一个通道的减法。**它一个数据点都不贡献，波形里没有它。它做的是让前面那个减法能够发生。"]),
 dict(n="⑥", t="这个「地」并不通向大地", fig="fig11-earth-vs-float", lab="图 6", fh=450, out="08-c6.png", a=[
   "那 V amp0 又连到哪里？墙上插座的地线吗？在生物电记录设备里通常不连，原因是安全。",
   "电流要流过人体，需要一条完整的回路。人体一旦有一条低阻抗通往大地的路径，这条回路就具备了一半。设备绝缘失效、或人体另一处接触到带电物体，电流就会经人体和地电极流向大地。**流过人体的电流会造成伤害，这是设计上首先要排除的情况。**",
   "处理办法是把患者侧与市电侧在电学上切开：整机用电池供电，或用光耦、变压器隔离前端³。V amp0 因此是一个浮空的零点。",
   "**参考电极进入减法，定义信号的零点；地电极不进入减法，它让减法能够发生。**"]),
]

for c in C:
    gen.figure_card(f(c["fig"]), c["lab"], c["a"], o(c["out"]),
                    figure_height=c["fh"], title=c["t"], title_num=c["n"])

gen.tail_card([
  "1. Bednar T, et al. (2021). Common-Mode Voltage Reduction in Capacitive Sensing of Biosignal Using Capacitive Grounding and DRL Electrode. Sensors 21(7):2568.",
  "2. Chi YM, Jung TP, Cauwenberghs G. (2010). Dry-contact and noncontact biopotential electrodes: methodological review. IEEE Rev Biomed Eng 3:106–119.",
  "3. MedLink Neurology. Technical aspects of EEG. medlink.com.",
  "",
  "出处说明：文献 1 的电容值经论文注明为指示值，取决于测量方法与环境；文献 2 的阻抗为前臂静息、未做皮肤准备的实测值，不是头皮数据；文献 3 为二次文献，隔离的原始要求见 IEC 60601-1，本期未取到标准原文。",
  "",
  "自算项：V body ≈ 2.2 V，按 C₁ ＝ 2 pF、C₂ ＝ 200 pF、市电 220 V 算得；C₂ 在 50 Hz 下容抗约 16 MΩ；16 MΩ 与 350 kΩ 相差约 45 倍。以上三项原文均未直接给出。",
], o("09-tail.png"), lead_paragraphs=[
  "下一期讲放大器本身。它凭什么能放大，增益 G 从哪里来？两端相减这一步，做得干净吗？输入阻抗为什么要做到 GΩ 量级——把这个数和本期那 350 kΩ 放在一起看，答案就出来了。",
])
print("done")
