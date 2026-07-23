# -*- coding: utf-8 -*-
"""Build 小红书 cards for series ① — EEG 工频/阻抗均衡 (line noise)."""
import sys, os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(SCRIPT_DIR))  # scripts/
from card_generator import CardGenerator

PROJECT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "series-eeg-impedance-01-linenoise")
FIG = os.path.join(OUT, "figs")
os.makedirs(OUT, exist_ok=True)

gen = CardGenerator(date="2026.07.23")

# 01 封面
gen.cover_card(
    "阻抗全绿",
    "EEG 照样满屏 50 Hz",
    "决定工频的,是各通道阻抗齐不齐,不是够不够低。",
    os.path.join(OUT, "01-cover.png"),
    source="本期是脑电(EEG,头皮记录)采集的原理专题,从第一性原理推导工频干扰这条链,不解读单篇新论文。依据经典生物电位放大器理论(Huhta & Webster 1973;Webster《Medical Instrumentation》)与真实实验反馈。",
)

# 02 问题量级
gen.text_card(
    "先看一个悬殊的量级差",
    [
        "我们要从头皮上测的脑电,幅度只有 **10–100 µV**(微伏,百万分之一伏)。这是全篇一切困难的起点:它太微弱了。",
        "小到什么程度——环境里的工频干扰,可以比它大 **十万倍**。先把脑电这个 µV 量级记住,后面每个数字都要回来和它比。",
        "工频从哪来、为什么这么大,下一张从墙里的电线讲起。",
    ],
    os.path.join(OUT, "02-magnitude.png"),
)

# 03 电容耦合(图)
gen.figure_card(
    os.path.join(FIG, "fig3-coupling.png"),
    "图 1 · 火线与人体之间的电容耦合",
    [
        "干扰的头号来源是墙里的交流电线。它没有和你相连,却能隔空影响你——**任何两个被绝缘隔开的导体之间都存在电容**,墙里的火线和你的身体正是这样一对。",
        "电容 **C = Q/V**:每加一伏能感应出多少电荷,只由几何决定——距离越近、正对面积越大,C 越大。所以离电源线远一点能减干扰,本质是减小 C₁。",
        "但只有电容还不够。为什么偏偏是 50 Hz 交流成了敌人、直流不会?看下一张。",
    ],
    os.path.join(OUT, "03-coupling.png"),
    figure_height=520,
)

# 04 为什么交流
gen.text_card(
    "为什么是交流,不是直流",
    [
        "电容里的电流,只由 **电压的变化速率** 驱动:**I = C × (ΔV/Δt)**。",
        "电压不变(直流),ΔV/Δt = 0,电流为零——电容对直流是断路。电压一变就有电流,且变得越快电流越大。换成频率 f 的交流,电流幅度正比于 **C × V × f**。",
        "所以电源线是头号干扰源:不只电压高(220V),更因为它一刻不停在 50 Hz 上摆动,持续把位移电流灌进人体。这股电流会把人抬到多高?下一张算。",
    ],
    os.path.join(OUT, "04-why-ac.png"),
)

# 05 量级(图)
gen.figure_card(
    os.path.join(FIG, "fig5-magnitude.png"),
    "图 2 · 干扰与脑电的量级对比",
    [
        "把人放进电路:火线经一个 **小电容**(几 pF)连到人体,人体又经一个 **大电容**(对地几百 pF)连回大地,人体是两者串联的中间节点,电位由容抗分压定:**V = 220 × C₁/(C₁+C₂)**。",
        "完全浮空(没接任何电极泄流)时,这个电位达 **几十伏**,比脑电的 10–100 µV 大约 **十万倍**。想测的信号被彻底淹没。",
        "对付它的第一道防线,是把人体电位先拉回来。",
    ],
    os.path.join(OUT, "05-magnitude.png"),
    figure_height=560,
)

# 06 GND 旁路(图)
gen.figure_card(
    os.path.join(FIG, "fig6-gnd-path.png"),
    "图 3 · GND 电极:给电流开一条低阻旁路",
    [
        "放大器要工作,输入必须落在它的 **共模输入范围** 内;几十伏直接顶到供电上限,输出成一条打满的直线(railed)。",
        "灌进人体的电流几乎固定 **≈ 3.8 µA**——它 = 火线电压 ÷ 那个小电容的容抗:**240V ÷ (1/2πfC) ≈ 240V ÷ 64MΩ ≈ 3.8 µA**,被巨大的容抗锁死。GND 电极给这股电流开一条 **5 kΩ** 的低阻旁路,取代原来 **10 MΩ** 的对地路。",
        "同一股电流走小 2000 倍的阻抗,压降就小 2000 倍——人体从 **38 V 塌到 20 mV**。但 GND 到底连到哪里?下一张有个必须纠正的误解。",
    ],
    os.path.join(OUT, "06-gnd-path.png"),
    figure_height=545,
)

# 07 GND 不是接地(安全)
gen.text_card(
    "GND 不是接大地",
    [
        "必须纠正一个被译名误导的点:**GND 电极连的不是大地,是放大器电路内部的公共基准节点**。叫它「地电极」有误导性。",
        "为什么刻意不接大地——**安全**。电流只在闭合回路里流。若把人硬接到大地,一旦别的设备漏电、人又碰到它,回路就借人体闭合:带电体→人体→大地→回电网,几十毫安穿过胸腔,足以致命。",
        "所以现代医疗设备(IEC 60601 一族)要求接触人体的前端与大地 **隔离**(隔离电路或电池供电)。GND 把人拉到放大器自己的浮地基准上——既定了共模基准,又不给人体铺那条对地回路。安全与测量,是同一个设计的两面。",
    ],
    os.path.join(OUT, "07-not-earth.png"),
)

# 08 差分与 CMRR
gen.text_card(
    "脑电靠一次减法",
    [
        "人体残留的 20 mV 共模仍比脑电大,怎么去掉?靠 **差分放大器**:把两个电极相减、再放大这个差。两电极共有的部分(共模)在相减时理应相消——**抑制工频靠的是减法本身,不是放大器聪明**。",
        "它做得多干净,用 **CMRR = 差模增益 / 共模增益** 衡量。标 **100 dB 即抑制十万倍**——共模被压低十万倍,但没到零,残漏 = 共模 ÷ CMRR。",
        "这是 **第一条漏源**(放大器内部的不完美)。真正每天污染数据的是 **第二条**,它藏在信号进放大器之前。接下来两张揭开它。",
    ],
    os.path.join(OUT, "08-cmrr.png"),
)

# 09 第二处分压
gen.text_card(
    "信号进放大器前,先被分压一次",
    [
        "信号不是被放大器直接看到的,它要先穿过 **电极接触阻抗 Z_e**,才到达输入端;放大器量的是落在自己 **输入阻抗 Z_in** 上的那部分。这是一次串联分压:**V_read = V_signal × Z_in / (Z_e + Z_in)**。",
        "Z_in 远大于 Z_e(如 1000 GΩ 对 10 kΩ):分数≈1,信号几乎无损读到;Z_in 与 Z_e 相当:信号被砍掉一半。所以放大器输入阻抗必须做到极高,否则电极阻抗会把信号吃掉。",
        "记住这个分压结构——下一张把它用到共模上,整篇最重点的公式就出来了。",
    ],
    os.path.join(OUT, "09-divider.png"),
)

# 10 共模漏成差模(图)
gen.figure_card(
    os.path.join(FIG, "fig10-leak.png"),
    "图 4 · 共模怎么漏成差模(全篇核心)",
    [
        "同一个 20 mV 共模,从两个电极各自穿过接触阻抗:**V_A = V_cm·Z_in/(Z_A+Z_in)**、**V_R = V_cm·Z_in/(Z_R+Z_in)**。两式结构相同,只差 Z_A 与 Z_R。",
        "相减后在 Z_in 远大于 Z_A、Z_R 时约简为:**V_diff ≈ V_cm × (Z_A − Z_R) / Z_in**。Z_A = Z_R 时差为 0,共模减得干干净净;Z_A ≠ Z_R 时,剩下的残差就是没减掉的共模——它变成了差模。",
        "盯住分子的 **(Z_A − Z_R)**:决定漏出的是两电极的阻抗差。下一张用数字验证它。",
    ],
    os.path.join(OUT, "10-leak.png"),
    figure_height=560,
)

# 11 齐 vs 低(图)
gen.figure_card(
    os.path.join(FIG, "fig11-match.png"),
    "图 5 · 要齐,不是要低",
    [
        "代数字(取 V_cm=20mV):两个都 **10 kΩ 但相等** → 差为 0 → 残差 **0**,一点不漏;你把一个 **拼命降到 2 kΩ**、另一个还是 10 kΩ → 差 8 kΩ → 反而漏得更多。",
        "所以对工频这条漏源,真正该做的是让各电极阻抗 **互相接近**,把 (Z_A − Z_R) 逼近零。分母 Z_in 越大漏得越少,这也是干电极(接触阻抗几百 kΩ)要等到 GΩ 级输入阻抗前端才成立的原因。",
        "一个限定:**降低绝对阻抗仍然有用**——高阻抗会增加低频噪声(尤其暖湿环境,Kappenman & Luck 2010)。所以准确说法是:对工频要齐,对低频噪声要低,两者都做。",
    ],
    os.path.join(OUT, "11-match.png"),
    figure_height=500,
)

# 12 CMRR 管不到
gen.text_card(
    "为什么高 CMRR 救不了它",
    [
        "这条漏源发生在放大器 **之前**(电极分压阶段);而 CMRR 只管放大器 **内部**——它的定义就是「两输入端加相等共模时能压掉多少」。",
        "可是经过电极不平衡分压,到达两个输入端的电压已经 **不相等** 了。两个不等电压之差,数学上就是一个正常的差分信号,放大器分不清它和真脑电,照单放大。它在进放大器前就从共模变成差模,脱离了 CMRR 的管辖。",
        "所以那句困惑解开了:**买了 100 dB 设备还是满屏工频**——你买的抑制力作用在放大器内部,而干扰是从电极不平衡漏进来的。两条漏源、两种治法:内部残漏靠买设备,电极不平衡只能靠调阻抗。",
    ],
    os.path.join(OUT, "12-cmrr-cant.png"),
)

# 13 行动一
gen.text_card(
    "落到操作:追求阻抗均衡",
    [
        "由 **V_diff ∝ (Z_A − Z_R)** 直接得到第一条动作:目标是各通道阻抗 **互相接近**,不是把个别压到最低。一堆 8 kΩ 的均匀电极,优于「多数 2 kΩ 夹一个 12 kΩ」的不齐组合。",
        "社区那些经验现在有了依据:磨砂膏去角质是把大家一起拉低、也更容易拉齐;全部打完再统一看阻抗,是等分压通路稳定;补膏只针对离群的那几个,把它们拉回大部队,而不是无脑追低。",
        "阻抗齐了,还有一个共用端没处理——那是下一张,也是「先查 REF/GND」这句口诀的真身。",
    ],
    os.path.join(OUT, "13-action-balance.png"),
)

# 14 行动二 REF/GND
gen.text_card(
    "为什么先查 REF / GND",
    [
        "「先查参考电极和地电极」这条口诀,现在可以推出来。参考电极是 **所有通道共用的那一端**,它出现在每一个通道的减法里;它的阻抗一旦大幅高于其他电极,失衡就 **同时发生在每一个通道** 上——于是满屏皆红、全通道工频,而不是坏一两个。",
        "GND 同理:它决定人体共模的绝对大小(**共模 ≈ 3.8µA × GND 阻抗**)。GND 接触一差,这个基数被抬高,全通道要对付的共模一起变大。",
        "共用端一失衡是系统性的,所以永远先查 REF 和 GND,再调其他。",
    ],
    os.path.join(OUT, "14-ref-gnd.png"),
)

# 15 边界 + 预告
gen.text_card(
    "这条链解释不了什么",
    [
        "本篇只推导了 **工频** 这一条链:电容耦合 → 人体共模 → 电极阻抗不平衡 → 漏成差模。它不解释别的伪迹:眼电、肌电来自生理源,基线漂移来自电极极化电位与出汗、呼吸——那些是不同的机制,后续几期分别拆。",
        "一句话收束:你在预处理阶段花几周用 ICA 去掉的东西,很多是在戴帽子那 40 分钟里生成的。事后处理只能挽救,不能创造。",
        "理解阻抗均衡,是从源头少制造脏数据。",
    ],
    os.path.join(OUT, "15-boundary.png"),
)

# 16 尾卡 1
gen.tail_card(
    [
        "① Huhta JC, Webster JG. (1973). 60-Hz interference in electrocardiography. IEEE Trans Biomed Eng 20(2):91–101.",
        "② Metting van Rijn AC, Peper A, Grimbergen CA. (1990). High-quality recording of bioelectric events, Part 1. Med Biol Eng Comput 28(5):389–397.",
        "③ Webster JG (ed.). Medical Instrumentation: Application and Design. Wiley.",
    ],
    os.path.join(OUT, "16-tail1.png"),
    lead_paragraphs=[
        "这期没有解读某一篇新论文,是把一条埋在每台脑电设备里、却很少被讲清的物理链推了一遍。",
        "它的实用价值不在多记几条降阻妙招,而在给你一个能自己推理的判断:下次阻抗全绿数据还是脏,你会先去查阻抗齐不齐、先去查 REF/GND,而不是无差别地追低。",
    ],
)

# 17 尾卡 2
gen.tail_card(
    [
        "④ Kappenman ES, Luck SJ. (2010). The effects of electrode impedance on data quality and statistical significance in ERP recordings. Psychophysiology 47(5):888–904.",
        "⑤ Yao D, et al. (2019). Which reference should we use for EEG and ERP practice? Brain Topogr 32(4):530–549.",
        "⑥ 杂散耦合电容实测范围:Estimation of stray coupling capacitances in biopotential measurements. Med Biol Eng Comput (2011).",
        "",
        "史实/工程数值(承重量级)取自上述文献;示例计算(3.8µA / 20mV / 具体 µV)为按公开电容值的量级演算,用于说明数量级。",
    ],
    os.path.join(OUT, "17-tail2.png"),
)

print("done ->", OUT)
