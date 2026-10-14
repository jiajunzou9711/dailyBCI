# -*- coding: utf-8 -*-
"""日报 2026-10-14 · 小鼠 M2 的觅食决策变量储备库（Cazettes 2023 Nat Neurosci）—— 卡片生成，上下两篇
用法：python3 build_foraging_dv_cards.py [上|下] [卡片文件名 ...]"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from card_generator import CardGenerator

PROJ = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", ".."))
EP = os.path.join(PROJ, "output", "2026-10-14-foraging-dv-reservoir")
FIG = os.path.join(EP, "figs")
def f(n): return os.path.join(FIG, n + ".png")

args = sys.argv[1:]
parts = [a for a in args if a in ("上", "下")] or ["上", "下"]
only = set(a for a in args if a not in ("上", "下"))
def want(name): return not only or name in only

gen = CardGenerator(date="2026.10.14")

TITLE = {"上": ("小鼠没用的策略", "M2 也在计算"), "下": ("用与不用的策略", "M2 都在编码")}
CORE = {"上": "小鼠觅食时主要依赖一种决策变量，次级运动皮层（M2）却同时编码了多种，编码好坏与是否被采用无关¹。",
        "下": "小鼠没采用的决策变量，在次级运动皮层（M2）里同样能读出，读出好坏与是否被采用无关¹。"}
SRC = "2023 年 4 月 Nature Neuroscience《A reservoir of foraging decision variables in the mouse brain》· Cazettes, Renart & Mainen"
TOC_SRC = [
    "2023 年 4 月，Nature Neuroscience 论文《A reservoir of foraging decision variables in the mouse brain》。一作 Fanny Cazettes，Alfonso Renart 与 Zachary F. Mainen 共同通讯，均在葡萄牙里斯本 Champalimaud 基金会。Mainen 组 2020 年在 Neuron 上发表过同一觅食任务的前作，发现抑制眶额皮层会影响推断型决策。",
    "方法：头部固定小鼠，Neuropixels 1.0 硅探针急性记录 M2、OFC、OLF 的神经元群体（10 只小鼠、11 个 session），另以光遗传抑制 M2。"]

UP = [
 dict(n=None, t="小鼠 M2 同时编码多种决策变量", out="03.png", a=[
   "觅食时，小鼠要决定何时离开当前的觅食点。可用的策略不止一种，而行为上每段时间主要只用其中一种。没被采用的策略所对应的决策变量（DV），大脑还算不算？",
   "2023 年 Nature Neuroscience 上，Champalimaud 基金会 Mainen 组与 Renart 组的这项工作，把 Neuropixels 硅探针插入头部固定小鼠的皮层内，记录神经元群体的活动。结论是：次级运动皮层（M2）同时编码多种 DV，包括行为上没有采用的那些；一个 DV 在 M2 里编码得多好，与它能多好地预测当前行为无关¹。",
   "作者在讨论里给出的推论是：既然多套计算已经并行存在，动物切换策略时，只需改变下游对 M2 活动的线性读出，不必新建计算¹。",
   "下一张先看这个结论要纠正的旧认知。"]),
 dict(n="①", t="通常的假定：大脑只计算当前策略所用的那一个 DV", out="04.png", a=[
   "同一串观测可以加工出多种决策变量（DV），对应不同的策略。作者在摘要里指出，领域通常假定大脑只计算当前行为策略所用的那一个 DV¹。",
   "支持这一假定的证据主要来自人类行为实验：两路感觉证据只能轮流并入 DV，处理是串行的²⁻⁴。",
   "电生理上有不同的观测：大鼠额顶叶皮层（fronto-parietal cortex）的神经元以多种时间尺度累积同一份证据⁵，猴皮层的局部环路中也存在多样的时间常数⁶。作者认为，这可能是一种简单形式的计算多路复用。",
   "于是问题收敛为：针对不同证据流的不同计算，能否在同一批神经元里并行进行？下一张展开。"]),
 dict(n="②", t="任务：小鼠要判断何时离开当前的出水管", fig="fig1a", lab="Fig. 1a：任务示意与一个回合的时间轴", fh=440, out="05.png", a=[
   "沿图 a 的时间轴从左往右读。头部固定的小鼠站在跑步机上，嘴前有一根出水管，它一口一口地舔。每一舔的结果画在 Lick 行：绿色是得到一滴水，紫色是没有水（失败）。",
   "左右两根出水管里，同一时刻只有一根会出水。这根管每被舔一次，有 0.9 的概率出水；同时也有 0.3 的概率让出水的一侧换到另一根管，每个回合只换一次¹（图中 State 两条线跳变的那条虚线）。换过之后，嘴前这根管再舔也不出水，Lick 行只剩紫色。",
   "下一张看小鼠何时离开。"]),
 dict(n="②", t="最后一次舔就是离开决策，一个回合到此结束", fig="fig1a-run", lab="Fig. 1a（节选）：Bout、Run、Lick 三行", fh=420, out="06.png", a=[
   "小鼠看不到出水的一侧何时切换，只能从得水与失败的序列去判断。它在某一舔之后停下，这就是最后一次舔（Last lick），也就是它做出的离开决策。随后它在跑步机上跑一段距离（Run 行抬高），面前的管移开，另一根移到嘴前（上排中、右图），它又开始舔。如果切换还没发生就离开，另一根管不会出水¹。",
   "从第一次舔到最后一次舔，构成一个**觅食回合（bout）**，即 Bout 行抬高的那一段。后文的分析都以舔为单位，每一舔都要回答：这是不是本回合的最后一次舔？",
   "下一张看这串结果可以怎样加工。"]),
 dict(n="②", t="同一串奖励与失败，可以算出两种决策变量", fig="fig1bc", lab="Fig. 1b–c：两种 DV 随同一串舔的结果变化", fh=330, out="07.png", a=[
   "作者选这两种 DV 各有来由：连续失败数对应这个任务的最优解，也就是推断当前点是否已转为不活跃；负价值是前作中训练早期小鼠的行为更符合的策略⁷。在作者比较过的其他策略里，这两种对离开时刻的预测最好¹。",
   "· **连续失败数**（图 b 粉线）：失败加 1，一次奖励就清零（Reset），因为奖励能确证当前点仍然活跃。\n· **负价值**（图 c 蓝线）：失败加 1，奖励减 1，持续累积（Integration），不考虑隐状态。作者称之为 stimulus-bound 策略。",
   "两条线都由上方同一排舔的结果算出。回合内 DV 越过阈值时，小鼠离开。下一张看小鼠实际用的是哪一种。"]),
 dict(n="②", t="不同小鼠、不同 session 采用不同的策略", fig="fig1gh", lab="Fig. 1g–h：奖励次数与离开前容忍的失败次数", fh=280, out="08.png", a=[
   "两种策略的差别在于奖励记不记入。按连续失败数离开时，之前得过几次奖励，不影响离开前能容忍几次连续失败；按负价值离开时，得过的奖励越多，能容忍的失败越多。",
   "图 g 的横轴是本回合内已得到的奖励次数，纵轴是本回合离开前的连续失败次数，两条线各是一个示例 session：粉线是平的，蓝线随奖励数上升。",
   "图 h 把这个关系量化。对每个 session，用奖励次数对连续失败次数做线性回归，得到的斜率（横轴）表示每多得一次奖励，离开前多容忍几次失败。斜率接近 0 符合推断策略，明显大于 0 符合 stimulus-bound 策略；纵轴是 session 数。21 只小鼠的 42 个 session 在斜率 0.5 附近出现低谷，以此为界，**23 个**偏推断，**19 个**偏 stimulus-bound¹。下一张看大脑里记录到了什么。"]),
 dict(n="③", t="三个脑区中，M2 对离开决策的预测最好", fig="fig2af", lab="Fig. 2a、2f：探针路径与三个脑区的解码效果", fh=360, out="09.png", a=[
   "记录用的是 Neuropixels 1.0：一根单杆硅探针，带数百个记录位点。每次记录时，探针穿过硬脑膜插入皮层，属于侵入式的皮层内急性记录¹。探针竖直穿过三个脑区（图 a）：次级运动皮层（M2）、它下方的眶额皮层（orbitofrontal cortex, OFC），以及作为对照的嗅皮层（olfactory cortex, OLF）。10 只小鼠共记录 11 个 session，每个 session 平均同时记录 151 个神经元¹。",
   "作者取每次舔前后 200 ms 内的群体活动，用逻辑回归预测这一舔是不是本回合的最后一次舔。图 f 的纵轴 deviance explained 衡量预测效果：0 为随机水平，1 为完美预测。M2 显著高于 OFC 和 OLF¹。",
   "下一张检验这个信号是否只是起跑前的运动准备。"]),
 dict(n="③", t="离开决策与起跑，在 M2 里可以分开读出", fig="fig3acg", lab="Fig. 3a、3c、3g：拆开最后一次舔与起跑", fh=320, out="10.png", a=[
   "最后一次舔之后，小鼠常常紧接着起跑，所以能预测「最后一次舔」的信号，也可能只是起跑前的运动准备。如图 a，作者只取最后一次舔与起跑间隔超过 1 s 的回合（Late run），把两件事在时间上分开¹。",
   "图 c：在这些回合里，M2 仍能预测离开决策，且显著好于 OFC 和 OLF（P = 0.002）¹。",
   "作者再分别求出预测离开和预测起跑的两条解码轴。图 g 的纵轴是两条轴的夹角，三个脑区都接近 90°，即两条轴接近正交：同一批神经元里，离开决策与起跑是两个可以分开读出的信号¹。下一张用光遗传检验 M2 是否必需。"]),
 dict(n="③", t="抑制 M2 后，两个 DV 对离开时刻的预测变差", fig="fig4ac", lab="Fig. 4a、4c：双侧抑制 M2 与给光前后的预测效果", fh=290, out="11.png", a=[
   "作者用光遗传学抑制双侧 M2（图 a）。所用的 VGAT-ChR2 小鼠中，蓝光会激活抑制性 GABA 能神经元，从而压低局部活动。实验随机选出 30% 的回合，从第一次舔开始给光，到最后一次舔停止，共 6 只小鼠、43 个 session¹。",
   "图 c 每个点是一个 session。横轴是不给光的回合里，两个 DV 对离开决策的预测效果（deviance explained）；纵轴是给光的回合里的同一指标。点落在对角线下方，表示给光后预测变差。抑制组（紫）多数点在对角线下方，混合模型估计给光使 deviance explained 平均下降 **0.04**（P = 0.021）¹。对照组（红，不表达光敏蛋白的同窝小鼠）也出现同方向的变化，接近显著（P = 0.054）¹。",
   "下一张把这个效应拆开看。"]),
 dict(n="③", t="抑制 M2 主要削弱连续失败数的作用，并降低离开倾向", fig="fig4eg", lab="Fig. 4e、4g：给光前后的连续失败数解释方差与离开倾向", fh=360, out="12.png", a=[
   "两张图的每个点仍是一个 session，横轴不给光，纵轴给光；紫色为抑制组，红色为对照组。",
   "图 e 是连续失败数单独解释的行为方差：抑制组给光后平均下降 0.054（P = 0.032），对照组无显著变化（P = 0.22）¹。负价值的变化不显著（P = 0.35）¹。",
   "图 g 是逻辑回归的截距，反映不论 DV 多大、小鼠离开的基础倾向：抑制组给光后下降（P < 10⁻⁶），对照组不变（P = 0.24）¹。动作时序没有明显改变，舔的频率略有下降¹。",
   "这些结果提示 M2 处在 DV 影响行为的通路上。"]),
]
UP_REFS = [
    "1. Cazettes F, et al. (2023). A reservoir of foraging decision variables in the mouse brain. Nat Neurosci 26:840–849.",
    "2. Pashler H. (1984). Processing stages in overlapping tasks: evidence for a central bottleneck. J Exp Psychol Hum Percept Perform 10:358–377.",
    "3. Sigman M, Dehaene S. (2005). Parsing a cognitive task: a characterization of the mind's bottleneck. PLoS Biol 3:e37.",
    "4. Kang YH, et al. (2021). Multiple decisions about one object involve parallel sensory acquisition but time-multiplexed evidence incorporation. eLife 10:e63721.",
    "5. Scott BB, et al. (2017). Fronto-parietal cortical circuits encode accumulated evidence with a diversity of timescales. Neuron 95:385–398.",
    "6. Bernacchia A, et al. (2011). A reservoir of time constants for memory traces in cortical neurons. Nat Neurosci 14:366–372.",
    "7. Vertechi P, et al. (2020). Inference-based decisions in a hidden state foraging task: differential contributions of prefrontal cortical areas. Neuron 106:166–176.",
]
UP_LEAD = ["上篇交代了任务、两种 DV，以及 M2 在离开决策中的作用。下篇回答核心问题：小鼠没采用的那种 DV，M2 里是否同样被编码，这一编码的边界又在哪里。"]

DOWN = [
 dict(n=None, t="上篇回顾：任务、两种 DV 与 M2", out="03.png", a=[
   "这项研究要检验的说法是：同一串观测可以加工出多种决策变量（DV），领域通常假定大脑只计算当前策略所用的那一个¹。",
   "任务：头部固定的小鼠舔出水管取水。左右两根管同一时刻只有一根出水，出水的一侧会随机换到另一根。小鼠要从得水与失败的序列判断何时离开；从第一次舔到最后一次舔为一个觅食回合（bout），最后一次舔即离开决策¹。",
   "同一串结果可以算出两种 DV：连续失败数（失败加 1，奖励清零，对应推断隐状态的策略）与负价值（失败加 1、奖励减 1，持续累积，即 stimulus-bound 策略）。不同小鼠、不同 session 主要依赖其中一种¹。",
   "用 Neuropixels 硅探针记录三个脑区，次级运动皮层（M2）对离开决策的预测最好；光遗传抑制 M2 后，DV 对离开时刻的预测变差¹。",
   "下篇回答核心问题：小鼠没采用的那种 DV，M2 里是否同样被编码。"]),
 dict(n="④", t="小鼠只用一种策略时，M2 里两个 DV 都能读出", fig="fig5abde", lab="Fig. 5a–b、d–e：从 M2 群体活动拟合两种 DV", fh=280, out="04.png", a=[
   "作者用 M2 群体活动的加权和，逐舔拟合 DV 的数值（图 a）。",
   "图 b、d 来自同一个 session。这只小鼠当时几乎只用推断策略：连续失败数对行为的方差解释为 0.164，负价值仅 0.004¹。M2 活动的加权和（黑线）能拟合连续失败数（粉线，deviance explained 0.74），也能拟合没被采用的负价值（蓝线，0.41）¹。",
   "图 e 汇总 11 个 session：两个 DV 都能从 M2 读出，连续失败数平均更好一些。作者认为这可能是因为多数 session（11 个中的 8 个）的小鼠主要用推断策略¹。两个 DV 的解码权重相关（r = 0.56），说明承载它们的是重叠的同一批神经元¹。",
   "那么，一个 DV 在 M2 里读出的好坏，与小鼠用不用它有没有关系？下一张展开。"]),
 dict(n="④", t="DV 在 M2 里读出的好坏，与小鼠用不用它无关", fig="fig5fg", lab="Fig. 5f–g：DV 对行为的预测 vs. M2 对 DV 的读出", fh=280, out="05.png", a=[
   "图 g 中每个点是某个 session 里的一个 DV（粉＝连续失败数，蓝＝负价值）。横轴是这个 DV 单独预测离开决策的效果（图 f），代表小鼠在多大程度上依赖它；纵轴是 M2 群体活动拟合这个 DV 的效果。",
   "如果 M2 只表征被采用的 DV，点应从左下向右上排列。实际的回归线是平的，r² < 10⁻³（P = 0.9）¹。小鼠依赖得多的 DV，在 M2 里不一定读得更好；几乎不被依赖的 DV，同样能读出。",
   "作者据此认为：M2 的活动对执行决策策略是重要的，但它的活动模式并没有专门适配当前执行的那个 DV，反映的是更大范围的一组策略¹。",
   "两个 DV 在小鼠实际经历的序列中相关系数达 0.79¹，下一张检验这是不是没被采用的 DV 能读出的原因。"]),
 dict(n="④", t="扣掉两个 DV 的共同成分后，M2 仍能读出各自余下的部分", fig="fig6efg", lab="Fig. 6e–g：残差分析（M2 与 OFC）", fh=340, out="06.png", a=[
   "作者用两种办法检验「相似所以能读出」这个解释。",
   "第一种是残差（图 e）。用负价值对连续失败数做线性回归，扣掉能被负价值解释的部分，剩下的灰线与负价值不相关，称为连续失败数的残差。反过来，可以得到负价值的残差。再看 M2 群体活动能否拟合这两条残差。",
   "图 f：M2 中两条残差都能读出（P = 0.00098）¹。图 g 是对照：OFC 只能读出连续失败数的残差，负价值的残差读不出（P = 0.52）¹，这与 OFC 参与推断策略的前作一致²。",
   "下一张看第二种办法。"]),
 dict(n="④", t="只保留两个 DV 几乎不相关的序列，结论不变", fig="fig6hi", lab="Fig. 6h–i：去相关子序列上的读出", fh=400, out="07.png", a=[
   "第二种办法是挑选序列：只保留两个 DV 几乎不相关的舔序列（相关系数中位数 0.03）¹。",
   "图 h：在这些序列上，两个 DV 仍能从 M2 读出¹。图 i 的横轴是 DV 单独预测离开决策的效果，纵轴是 M2 对 DV 的读出效果；读出好坏与行为依赖程度依旧无关（r² = 0.02，P = 0.6）¹。",
   "所以，没被采用的 DV 能读出，不能用它与被采用 DV 的相关来解释。还剩一种可能：小鼠在一个 session 内来回换策略，整段平均下来，两个 DV 就都显得被编码了。下一张检验这一点。"]),
 dict(n="④", t="小鼠在 session 内会换策略，M2 对两个 DV 的编码不随之改变", fig="fig7ce", lab="Fig. 7c、7e：策略状态的切换与各状态下的读出", fh=280, out="08.png", a=[
   "作者用隐马尔可夫模型（hidden Markov model, HMM）推断小鼠在每个回合处于哪种策略状态。模型分出三种状态：stimulus-bound（蓝）、持续型推断（粉）和冲动型推断（黄）¹。",
   "图 c 是一个示例 session，纵轴是每个回合属于各状态的后验概率。小鼠在一种状态里连续停留几十个回合，然后切换到另一种；11 个 session 中有 8 个出现过切换¹。",
   "图 e 把每个 session 按状态分段，分别解码两个 DV，底色对应状态。无论小鼠当时处于哪种策略，两个 DV 的读出都没有显著差异（P > 0.05）¹。在不采用某个 DV 的状态里，它的残差也仍能读出¹。",
   "因此，多路编码不是策略切换平均出来的结果。下一张看 M2 还能编码哪些 DV。"]),
 dict(n="⑤", t="同一条更新规则能生成多种 DV，M2 编码其中一族", fig="fig8ac", lab="Fig. 8a、8c：INTEGRATE-AND-RESET 模型与四条基序列的读出", fh=360, out="09.png", a=[
   "作者注意到，两种 DV 可以写成同一条更新规则：x(t+1) = g · x(t) + c。其中 x 是累计量；g 决定这一舔之后累计量保留（g = 1）还是清零（g = 0）；c 决定这一舔给累计量加多少（+1、−1 或 0）。g 和 c 对奖励、失败各取一个值。作者称之为 INTEGRATE-AND-RESET 模型（图 a，方括号里是这四个取值）¹。",
   "g 和 c 取离散值时，这个模型给出四条基序列：连续失败数、负价值、连续奖励数（奖励加 1，失败清零）、总计数（奖励和失败都加 1）。图 c 显示，去相关之后四条都能从 M2 读出，其中连续奖励数最弱¹。",
   "这一族计算有没有边界，下一张检验。"]),
 dict(n="⑤", t="与任务无关的同类时间序列，M2 读不出", fig="ed8bd", lab="Extended Data Fig. 8b、8d：错位的 DV 与功率谱匹配的随机信号", fh=320, out="10.png", a=[
   "按储备池计算（reservoir computing）框架的预测，循环网络几乎能表征由过去输入组合出的任何信号¹。作者因此检验 M2 能否读出与任务无关的序列：它们在起伏快慢上与 DV 一致，数值却不再由小鼠实际得到的奖励与失败算出。",
   "图 d 是其中一种：随机信号，功率谱与 DV 相同，也就是各频率成分的强度一样，具体数值是随机的。两种 DV 对应的随机信号都读不出，deviance explained 在 0 附近¹。一组覆盖 DV 起伏时间尺度的余弦波同样读不出¹。",
   "图 b 把 DV 本身沿时间错开 3、6、9、12 舔：错开越多读出越差，错开超过 DV 的自相关时长后接近 0¹。",
   "所以，M2 编码的是一族由觅食结果算出的计算，不是任意的时间序列。下一张回到这项研究要检验的旧认知。"]),
 dict(n="⑥", t="回到旧认知：在这个任务里，小鼠 M2 并行计算多种 DV", out="11.png", a=[
   "这项研究要检验的旧认知是：大脑只计算当前策略所用的那一个 DV¹。这篇的证据逐条回应了它。",
   "· 行为上，小鼠在每段时间主要依赖一种 DV；\n· M2 中，被采用和未被采用的 DV 都能读出，读出好坏与小鼠是否依赖它无关；\n· 这一结果不能用两个 DV 相关来解释，也不是 session 内策略切换平均出来的；\n· M2 能读出的 DV，都能由同一条规则生成：每一舔之后，累计量要么保留、要么清零，再按这一舔是奖励还是失败加上 +1、−1 或 0。起伏快慢与 DV 相同、但不由奖励与失败算出的随机信号和余弦波，M2 读不出。",
   "下一张把这些结果放回已有研究中。"]),
 dict(n="⑥", t="与已有研究的关系：多种计算可以并行", out="12.png", a=[
   "此前在大鼠与猴上的电生理研究发现，皮层神经元以多种时间尺度累积证据³⁴。这篇的数据显示，M2 里并行存在的除了时间常数不同的积分，还有「清零」和「持续累积」这两种性质不同的计算¹。",
   "关于串行瓶颈，作者指出，人类实验要求被试同时用两路证据完成任务；这里的小鼠不需要同时用两个 DV，M2 却同时算出了两个。作者认为，这与「证据可以并行积分、串行限制发生在临近动作的环节」这类模型相容¹。",
   "这些结论能推到多远，下一张说明。"]),
 dict(n="⑦", t="局限性：能读出 DV，不等于 DV 被下游使用", out="13.png", a=[
   "本研究的证据强度有三处需要注意。",
   "1. 线性解码只说明 DV 的信息存在于 M2 的群体活动中，没有说明下游脑区实际读取了它。作者推论「切换策略只需改变对 M2 的线性读出」¹，这篇没有直接检验。",
   "2. 光遗传抑制的效应量小：DV 对行为的预测平均只下降 0.04，对照组同向变化也接近显著（P = 0.054）¹。此外，抑制覆盖整个回合，因此 M2 是在计算 DV，还是在把 DV 转成离开动作，这个实验无法区分。这一条是我的分析，论文没有这样划分。",
   "3. 样本量：神经记录来自 10 只小鼠的 11 个 session；光遗传实验为抑制组 4 只、对照组 2 只¹。",
   "下一张说明结论的适用范围。"]),
 dict(n="⑦", t="局限性：结论限于 M2 和这个觅食任务", out="14.png", a=[
   "4. 这个任务不要求同时使用两个 DV。作者自己也指出，这与人类串行瓶颈实验的情境不同¹，所以不能直接据此否定那类实验中观察到的串行限制。",
   "5. 多路编码只在 M2 观察到。OFC 只编码连续失败数¹。",
   "6. 储备库只覆盖 INTEGRATE-AND-RESET 这一族计算。换一种任务结构，M2 是否仍保有相应的计算，这篇没有检验。"]),
]
DOWN_REFS = [
    "1. Cazettes F, et al. (2023). A reservoir of foraging decision variables in the mouse brain. Nat Neurosci 26:840–849.",
    "2. Vertechi P, et al. (2020). Inference-based decisions in a hidden state foraging task: differential contributions of prefrontal cortical areas. Neuron 106:166–176.",
    "3. Scott BB, et al. (2017). Fronto-parietal cortical circuits encode accumulated evidence with a diversity of timescales. Neuron 95:385–398.",
    "4. Bernacchia A, et al. (2011). A reservoir of time constants for memory traces in cortical neurons. Nat Neurosci 14:366–372.",
]
DOWN_LEAD = ["如果多套计算已经并行存在，动物学会新策略时，变化发生在 M2 的表征，还是下游对它的读出？回答它需要在学习过程中同时记录 M2 和它的下游脑区。"]

for part in parts:
    OUT = os.path.join(EP, f"cards-{part}"); os.makedirs(OUT, exist_ok=True)
    cards, refs, lead = (UP, UP_REFS, UP_LEAD) if part == "上" else (DOWN, DOWN_REFS, DOWN_LEAD)
    if want("01-cover.png"):
        gen.cover_card(*TITLE[part], CORE[part], os.path.join(OUT, "01-cover.png"),
                       concept_image=f("cover"), concept_height=420, title_size=120, title_top=70,
                       source=SRC + f"（{part}篇）")
    if want("02-toc.png"):
        gen.figure_card(f("toc1" if part == "上" else "toc2"), f"本期路线（{part}篇）", TOC_SRC,
                        os.path.join(OUT, "02-toc.png"), figure_height=600, annot_size=27)
    for c in cards:
        if not want(c["out"]):
            continue
        o = os.path.join(OUT, c["out"])
        if c.get("fig"):
            gen.figure_card(f(c["fig"]), c["lab"], c["a"], o, figure_height=c["fh"],
                            title=c["t"], title_num=c["n"])
        else:
            head = c["t"] if c["n"] is None else f'{c["n"]} {c["t"]}'
            gen.text_card(None, c["a"], o, heading_lines=[head])
    tail = f"{len(cards) + 3:02d}-tail.png"
    if want(tail):
        gen.tail_card(refs, os.path.join(OUT, tail), lead_paragraphs=lead)
