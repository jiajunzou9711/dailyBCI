# -*- coding: utf-8 -*-
# 第二期「赛博果蝇做到了什么 还差什么（下）」图卡。文案以 ../draft.md「第二期 · 已定稿」为准。
# 角标已按本期正文首次出现顺序重排：¹ Shiu ² Eckstein ³ Inagaki ⁴ Lappalainen ⁵ Mindspan ⁶ Chen
import sys, os
sys.path.insert(0, ".claude/skills/dailybci/scripts")
from card_generator import CardGenerator

OUT = "output/2026-09-19-digital-fly/issue2"
P = f"{OUT}/figs"
gen = CardGenerator(date="2026.09.22")

# 01 封面
gen.cover_card(
    "赛博果蝇做到了什么", "还差什么（下）",
    "从连接到可靠预测，还缺三类参数。",
    f"{OUT}/01-cover.png",
    source="2024 年 10 月《Nature》Shiu 等人论文 · 本期为该文与相关研究的解读",
    concept_image=f"{P}/fig1a.png", concept_height=480, title_size=96, title_top=90)

# 02 目录
gen.figure_card(f"{P}/fig-toc2.png", "目录与来源", [
    "来源：2024 年 10 月发表于《Nature》的论文《A Drosophila computational brain model reveals sensorimotor processing》，作者 Shiu、Sterne 等，末位作者 Kristin Scott（加州大学伯克利分校）。方法：用 FlyWire 成年雌果蝇全脑连接组建漏积分发放模型，预测味觉与理毛环路，再用光遗传学在活体果蝇上检验。",
    "另引用 Eckstein 2024、Inagaki 2012、Lappalainen 2024 三篇论文与 Mindspan Institute 官网。",
], f"{OUT}/02-toc.png", figure_height=760, annot_size=27)

# 03 ① 筛选（Fig. 1f）
gen.figure_card(f"{P}/shiu_fig1f.png", "Shiu et al. 2024, Fig. 1f", [
    "2024 年，Shiu 等人用一只果蝇的全脑连接组建了可运行的模型¹。如上图，激活糖味觉神经元的同时，把反应最强的 200 个神经元**逐个**沉默，读出控制伸喙（proboscis extension）的运动神经元 MN9 发放变了多少；蓝色表示沉默后发放降低¹。",
    "模型里 **127,400 个**神经元都能单独操作，一次 1 s 仿真单线程约 **5 分钟**¹；真果蝇上，那次筛查的品系库只覆盖 **106 个**可在连接组里认出的细胞类型¹。",
    "所以数字实验的用途是**筛选**，前提是预测可信。那预测是怎么算出来的？",
], f"{OUT}/03-screen.png", figure_height=420, title="① 在模型里先跑一遍，\n再决定去真果蝇上验哪几个")

# 04 ② 总览
gen.figure_card(f"{P}/fig-overview.png", "自制示意图", [
    "电镜重建只给出哪两个神经元之间有多少个突触。要算出活动，Shiu 等人另外规定了上图三件事¹。",
    "每项省掉的内容，各挡住一类实验：作用在受体或电突触上的操作；靠抑制一个抑制性神经元来放行下游的通路；同一刺激在饱、饿状态下引起的不同行为，以及学习与记忆。",
    "下面逐项展开，先看第一项：一个突触的强度从哪里来。",
], f"{OUT}/04-overview.png", figure_height=520, title="② 连接组要运行起来，\n作者补了三项默认设定")

# 05 ③-1 强度的设定
gen.figure_card(f"{P}/fig-voltage.png", "自制示意图，数值取自 Shiu 2024", [
    "模型里，上游发放一次动作电位，**每个突触**让下游膜电位变化 **0.275 mV**¹。如上图，10 个突触推动 2.75 mV，而静息 −52 mV 到阈值 −45 mV 差 7 mV¹，要靠多次输入叠加才能发放。",
    "其他参数都取自已发表的测量¹，只有这个数没有测量值可引，由作者自定，这就是**自由参数**。作者调它，直到糖味觉神经元以 100 Hz 发放时 MN9 达到最大发放率的约 **80%**¹。",
    "所以这个数是照「糖 → 伸喙」一条通路调出来的，却用到了全脑每一个突触上。它偏一点，影响有多大？",
], f"{OUT}/05-strength.png", figure_height=440, title="③ 一个突触推动多少毫伏，\n是照一条通路调出来的")

# 06 ③-2 强度的局限
gen.figure_card(f"{P}/fig-efficacy.png", "自制示意图", [
    "影响不大：作者把 0.275 mV 调低、调高 30%，164 条可检验预测的准确率从 91% 变为 **85%** 与 **88%**¹。",
    "这个检验让所有突触一起变，回答不了**不同突触该不该有不同的值**。真实突触的效力还取决于受体种类与数量、释放概率、在树突上的位置，电镜分辨不出。如上图，模型里连接强弱**只由突触数之比决定**。",
    "论文只检验了取食与触角理毛两个系统¹，其他环路要逐个检验。强度之外，正负号又从哪里来？",
], f"{OUT}/06-strength-limit.png", figure_height=450, title="③ 数值偏一点影响不大，\n问题在于所有突触都用同一个值")

# 07 ③-3 正负号
gen.figure_card(f"{P}/fig-sign.png", "自制示意图", [
    "正负号同样来自电镜图像。如上图，Eckstein 等人以递质已知的细胞类型为标签，训练三维卷积网络（3D CNN），从突触前位点（presynaptic site）周围的图像块预测六种递质之一²。",
    "递质定不出正负号：方向由突触后受体决定，电镜看不到受体。果蝇里谷氨酸既可兴奋也可抑制，约 **24%** 的神经元预测为谷氨酸能¹，模型一律记为抑制。改记为兴奋后，苦味与 Ir94e 抑制取食的结果消失，筛查假阳性率从 **1%** 升到 **16%**¹。",
    "连接讲完，再看第二项：神经元本身怎样工作。",
], f"{OUT}/07-sign.png", figure_height=450, title="③ 分类器预测的是递质，\n兴奋还是抑制由受体决定")

# 08 ④-1 神经元设定（纯文字）
gen.text_card(None, [
    "第二项是神经元本身。模型里每个神经元都按漏积分发放（leaky integrate-and-fire，LIF）规则工作¹：上游每来一次动作电位，下游的输入变量就按连接权重增减；这个变量以 5 ms 的时间常数衰减，膜电位随之变化；膜电位越过阈值就发放一次动作电位，随后复位，2.2 ms 内不再发放。",
    "这条规则里有三处简化¹：",
    "1. 神经元被当成一个点：全部输入在同一处线性相加，树突形态不起作用。",
    "2. 127,400 个神经元共用同一组参数，不区分细胞类型。",
    "3. 没有输入时，每个神经元的发放率为零。",
    "三处简化中，第 3 点的后果最直接。",
], f"{OUT}/08-neuron.png", heading_lines=["④ 127,400 个神经元，", "按同一条规则发放"])

# 09 ④-2 去抑制
gen.figure_card(f"{P}/fig-disinhibition2.png", "自制示意图，据 Shiu 2024 正文", [
    "去抑制（disinhibition）指抑制性神经元抑制另一个抑制性神经元，从而放开下游，前提是被抑制的那个平时在放电。如上图，真果蝇里激活 Phantom 会引起伸喙，模型却预测不会¹。论文的解释是：模型里基础放电为零，没有其他输入时，激活抑制性神经元改变不了下游¹。",
    "第 1、2 点的后果目前只能从原理推，论文没有单独检验。前两项讲的是某一时刻怎样计算，第三项看模型随时间变不变。",
], f"{OUT}/09-neuron-limit.png", figure_height=560, title="④ 没有自发放电，\n靠去抑制起作用的通路就算不出来")

# 10 ⑤-1 时间设定（纯文字）
gen.text_card(None, [
    "前两项的设定在整个仿真过程中保持固定¹。真实大脑里有两类变化，模型都没有纳入：",
    "**1. 内部状态**：模型不包含饥饿、口渴等内部状态，也不包含长程作用的神经肽（neuropeptide）¹。多巴胺、章胺、血清素这些神经调质（neuromodulator），只按普通的兴奋性连接处理¹。",
    "**2. 经历**：连接强度只由突触数量决定，仿真中不会因为学习而更新。",
    "论文把这一项列为预测失准的可能来源：受神经调质影响的神经元，以及表达神经调质的神经元，都可能模拟得不好¹。",
    "放到 Shiu 检验过的取食通路上，会怎样？",
], f"{OUT}/10-time.png", heading_lines=["⑤ 从仿真开始到结束，", "连接和参数都不变"])

# 11 ⑤-2 饱与饿
gen.figure_card(f"{P}/fig-hunger.png", "自制示意图，据 Inagaki 2012 的结论绘制", [
    "禁食（有水）后，更低浓度的蔗糖就能引起伸喙；禁食越久效应越强，恢复进食后可逆³。Inagaki 等人找到其中一部分机制：饥饿时多巴胺经 DopEcR 受体作用于糖味觉神经元，增强糖引起的钙内流；敲除 DopEcR，禁食 6 小时的果蝇敏感性不再升高，在糖味觉神经元里补回即恢复³。",
    "模型里这条通路的强度只由突触数决定，饱与饿给出同一个预测。学习同理。缺的这些参数，能不能补？",
], f"{OUT}/11-hunger.png", figure_height=520, title="⑤ 同样的糖，饱果蝇和饿果蝇\n反应不同，模型只给一个预测")

# 12 ⑥-1 反推
gen.figure_card(f"{P}/lap_fig1a.png", "Lappalainen et al. 2024, Fig. 1a", [
    "一种补法：连接组固定结构，未知参数交给优化。如上图，Lappalainen 等人用果蝇视叶运动通路 64 个细胞类型的连接组搭建网络（图中 DMN），让它完成运动检测任务，再把预测与实测神经活动比对⁴。",
    "每个细胞类型有自己的时间常数与静息电位，每对细胞类型有自己的单位突触强度，共 **734 个**自由参数⁴；Shiu 模型只有 **1 个**¹。预测与 26 项研究的实测相符⁴。",
    "这些参数仍是反推出来的值，没有直接测量过。另一条路，是把它们测出来。",
], f"{OUT}/12-infer.png", figure_height=480, title="⑥ 缺的参数，\n可以先用任务反推出来")

# 13 ⑥-2 Mindspan
gen.figure_card(f"{P}/fig-mindspan.png", "自制示意图，据 Mindspan 官网", [
    "Mindspan Institute 是新成立的非营利研究机构，由 Ed Boyden（MIT）和 Konrad Kording（宾夕法尼亚大学）共同负责，目标是开发并规模化分析人脑分子与连接的工具⁵。",
    "如上图，研究院按一条完整流程组织，把组织一路做到「值得模拟的重建」⁵。其中膨胀显微镜（expansion microscopy）把标记锚定在可膨胀的聚合物网络上并物理放大组织，使普通光学显微镜能分辨衍射极限以下的结构⁶。",
], f"{OUT}/13-measure.png", figure_height=480, title="⑥ 另一条路：\n把这些参数直接测出来")

# 14 ⑦ 结语
gen.figure_card(f"{P}/fig-closing.png", "自制示意图", [
    "回到开头的问题：数字果蝇要成为可靠的实验工具，还缺什么？如上图，缺的是连接之外的参数，它们目前都是统一规定。",
    "在检验过的取食与触角理毛两个系统里，这些规定给出的预测 **91%** 与实验相符¹；换到别的环路、别的状态，每一条都要重新检验。",
    "所以用模型筛选之前，先看要问的问题依赖哪几类参数。依赖越多，预测越需要实验确认。",
], f"{OUT}/14-closing.png", figure_height=540, title="⑦ 缺的是连接之外的参数")

# 15 尾卡
refs = [
 "¹ Shiu PK, et al. (2024). A Drosophila computational brain model reveals sensorimotor processing. Nature 634:210–219.",
 "² Eckstein N, et al. (2024). Neurotransmitter classification from electron microscopy images at synaptic sites in Drosophila melanogaster. Cell 187:2574–2594.",
 "³ Inagaki HK, et al. (2012). Visualizing neuromodulation in vivo: TANGO-mapping of dopamine signaling reveals appetite control of sugar sensing. Cell 148:583–595.",
 "⁴ Lappalainen JK, et al. (2024). Connectome-constrained networks predict neural activity across the fly visual system. Nature 634:1132–1140.",
 "⁵ Mindspan Institute. (n.d.). Mindspan Institute 官网首页与招聘页. https://mindspan.org（2026-09-22 访问）.",
 "⁶ Chen F, Tillberg PW, Boyden ES. (2015). Expansion microscopy. Science 347:543–548.",
]
gen.tail_card(refs, f"{OUT}/15-tail.png")
print("done")
