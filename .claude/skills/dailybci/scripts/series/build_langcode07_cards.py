# -*- coding: utf-8 -*-
"""日报 2026-08-27「语言的神经群体编码」第七期：12 张图卡。"""
import os, sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(SCRIPT_DIR))
from card_generator import CardGenerator

SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-08-27-langcode-07")
FIGS = os.path.join(OUT, "figs")
PAPERS = os.path.join(PROJECT, "papers")
os.makedirs(OUT, exist_ok=True)
P = lambda *a: os.path.join(*a)
SELF = "自制示意图"
NS1 = "Nastase et al. (2026) Neuron 观点文章：大语言模型与人脑之间的差距"

gen = CardGenerator(date="2026.08.27")

# ---------- 01 封面 ----------
gen.cover_card(
    "AI 和大脑的构造处处不同",
    "学到的东西却一样",
    "相似成立在组织方式上，与生物实现的细节无关。",
    P(OUT, "01-cover.png"),
    concept_image=P(PAPERS, "ns-fig1B-net.png"),
    concept_height=520,
    concept_bleed=100,
    title_size=62,
    title_top=180,
    source=NS1,
)

# ---------- 02 目录 ----------
gen.figure_card(
    P(FIGS, "toc.png"), "本期路线",
    ["本期讲 Neuron 观点文章（Nastase et al., 2026）里的一节。作者在文中列出**大语言模型与人脑之间的差距**，"
     "同时说明哪些东西被简化掉了、哪些被保留了下来。",
     "这些差距分两类。本期只讲第一类——**实现与加工方式**：用什么元件、怎么通信、怎么改权重、"
     "怎么组织回路、时间怎么走。第二类（学习条件：数据量、模态、能否干预、学习目标、数据效率）留到下一期。"],
    P(OUT, "02-toc.png"), figure_height=600, annot_size=27,
)

# ---------- 03 ① ----------
gen.text_card(
    "① 模型与人脑的相似已被反复测到",
    ["近几年一批工作反复发现同一件事：**大语言模型内部的表征，与人脑语言系统的活动能对上。**",
     "一个具体的量：用英语训练的脑活动编码模型，可以直接拿去预测法语和汉语听众的神经活动，"
     "跨语言与语言内的全脑成绩图相关达 **0.974**。",
     "这类结果容易被读成「大脑就是个大语言模型」。要避免这个误读，先得看清两者的实际构造。",
     "〔Zada et al. 2025, arXiv:2506.20489。该结果目前是预印本，未经同行评议，"
     "且作者与本期主文章同组。〕"],
    P(OUT, "03-card1.png"),
)

# ---------- 04 ② ----------
gen.text_card(
    "② 拆开看，两者几乎没有一样的地方",
    ["同一篇文章紧接着列出了实现层面的差距：",
     "**元件**——不尊重单个神经元的多样性与复杂性；"
     "**通信**——常把动作电位简化成率编码；"
     "**学习规则**——不严格遵守生物学的学习算法；"
     "**回路**——不反映已知的生物回路基元；"
     "**时间**——缺细粒度的时间动力学，更没有内源性振荡。",
     "作者给这一节定的口径是：**所有模型都做简化假设。**"
     "人工神经网络只保留了研究者认为最要紧的那几条性质，其余一律简化掉。",
     "下面五张卡逐条对照，看每一条被简化掉的是什么。"],
    P(OUT, "04-card2.png"),
)

# ---------- 05 ③ ----------
gen.figure_card(
    P(FIGS, "fig-units.png"), SELF,
    ["**生物怎么实现的。** 皮层神经元按形态、电生理和转录组分成许多类型——锥体细胞，"
     "以及 PV、SST、VIP 等多类中间神经元，各自的连接规则、膜时间常数、放电模式都不同。"
     "单个神经元也不是简单的加权求和器：树突分支能做局部的非线性运算。",
     "**LLM 怎么实现的。** 所有单元是同一种，共用同一个激活函数。",
     "**这条差距意味着什么。** 原文引 Perez-Nieves et al. 2021（*Nat Commun* 12:5791），"
     "结论是神经元的异质性能提升学习的鲁棒性——多样性在计算上有功能。"],
    P(OUT, "05-card3.png"), figure_height=380,
    title="生物用不同类型的元件，LLM 用同一种", title_num="③",
)

# ---------- 06 ④ ----------
gen.figure_card(
    P(FIGS, "fig-spike.png"), SELF,
    ["**生物怎么实现的。** 神经元之间用**动作电位**通信——全或无的离散事件，发生在具体的时刻。"
     "信息可以携带在发放率上，也可以携带在时间结构上：首个动作电位的延迟、相邻动作电位的间隔、"
     "与群体节律之间的相位关系。",
     "**LLM 怎么实现的。** 每个单元在一次前向传播里输出**一个实数**。没有事件，没有时刻，没有间隔。",
     "**这条差距意味着什么。** 一是时间编码的手段没有了：只有强度值时必须靠积分时间窗。"
     "二是能耗：动作电位稀疏、事件驱动，原文引的 Stanojevic et al. 2024（*Nat Commun* 15:6793）"
     "标题即「每神经元 0.3 个动作电位的高性能深度脉冲网络」。"],
    P(OUT, "06-card4.png"), figure_height=360,
    title="生物用动作电位，LLM 用一个实数", title_num="④",
)

# ---------- 07 ⑤ ----------
gen.figure_card(
    P(FIGS, "fig-learning.png"), SELF,
    ["**生物怎么实现的。** 突触强度的改变是局部的：一个突触变强还是变弱，取决于它前后两个神经元"
     "自身的活动（Hebbian 规则、STDP），再叠加神经调质提供的全局标量信号（如多巴胺）。",
     "**LLM 怎么实现的。** 反向传播。用链式法则把误差的偏导数逐层传回，"
     "**每个权重按它对总误差的贡献量精确更新**。",
     "**这条差距意味着什么。** 反向传播要求误差信号精确到达每个权重、反向通路用与前向相同的权重、"
     "前向活动被保留下来——**这三条在生物系统里都没有已知的实现机制**。"
     "原文引 Whittington & Bogacz 2019（*TiCS* 23:235）：已有候选机制，尚无定论。"],
    P(OUT, "07-card5.png"), figure_height=350,
    title="生物靠局部规则改突触，LLM 靠反向传播", title_num="⑤",
)

# ---------- 08 ⑥ ----------
gen.text_card(
    "⑥ 生物有定型的局部回路，LLM 只重复同一个模块",
    ["**生物怎么实现的。** 皮层有反复出现、连接规则固定的局部结构：六层皮层的层间连接有方向性"
     "（第 4 层收输入，第 5/6 层往外发），中间神经元构成前馈抑制与反馈抑制的定型回路，"
     "丘脑与皮层之间有环路。此外还有非神经元成分参与——星形胶质细胞包裹突触，影响传递效率与时程。",
     "**LLM 怎么实现的。** Transformer 的每一层结构完全相同：自注意力 + 前馈网络 + 残差连接 + 层归一化。"
     "深度靠重复同一个模块堆出来。",
     "**这条差距意味着什么。** 生物回路里的定型结构承担具体功能——前馈抑制做时间窗控制、"
     "反馈抑制做增益调节、丘脑环路做门控。这些功能在 LLM 里若存在，是靠训练在同构模块里自己长出来的，"
     "没有结构上的保证。原文引 Kozachkov et al. 2023（*PNAS* 120:e2219150120），"
     "题为「用神经元与星形胶质细胞搭建 Transformer」。"],
    P(OUT, "08-card6.png"),
)

# ---------- 09 ⑦ ----------
gen.figure_card(
    P(FIGS, "fig-time.png"), SELF,
    ["**生物怎么实现的。** 皮层活动带有内源性节律——不给刺激也存在的自发振荡。在语音理解里，"
     "一批工作提出不同频段承担不同粒度的切分：theta 段（约 4–8 Hz）与音节率对应，"
     "delta 段与短语、句子的速率对应。",
     "**LLM 怎么实现的。** 文本 LLM 没有连续的物理时间轴。一个 token 一步，"
     "步与步之间不对应任何时长；不给输入就没有活动。",
     "**这条差距意味着什么。** 最直接的一处是切分：生物可能靠节律把连续声流切成音节和短语，"
     "而 LLM 的切分是分词器预先做好的。原文同段还指出，人必须实时把当前输入压缩掉以便接收下一个输入，"
     "而 Transformer 在任意时刻都保有数千 token 的完整前文。"],
    P(OUT, "09-card7.png"), figure_height=360,
    title="生物在连续时间里运行，LLM 在离散步序里运行", title_num="⑦",
)

# ---------- 10 ⑧ ----------
gen.text_card(
    "⑧ 那相似靠什么成立——被保留下来的五条",
    ["五条差距讲完，问题回到开头：既然构造处处不同，相似为什么还成立？"
     "答案是它成立在另外五条性质上，这五条被完整保留了下来。",
     "1. 语言结构分布在**大量简单、互连的计算单元**上，没有专门的语法模块或语义模块。\n"
     "2. 每个单元**汇总输入，经非线性激活函数产生输出**——对应神经元的电压阈值。\n"
     "3. 网络的记忆存在**单元之间的连接权重**里——对应突触强度。\n"
     "4. 这些权重按**一条相对简单的学习规则迭代更新**——对应突触可塑性。\n"
     "5. **没有任何单个单元掌控全局**，认知与复杂行为从单元之间的动态相互作用中产生。",
     "**前面那五条差距，全部落在这五条之外。**元件是不是同一种、通信用不用离散事件、"
     "权重怎么更新、回路怎么组织、时间是不是连续——改变的是用什么实现；这五条说的是实现之后"
     "得到什么样的组织方式。"],
    P(OUT, "10-card8.png"),
)

# ---------- 11 ⑨ ----------
gen.figure_card(
    P(FIGS, "fig-map.png"), SELF,
    ["还有两个理由支持同一判断。",
     "**一、原文引的文献大多在指出替代方案已经存在。** 异质性有功能、脉冲网络能做到高性能、"
     "反向传播有生物学版本的候选理论。这一类差距是「可以补上，只是现在没补」。",
     "**二、对应本来就发生在表征层面。** 编码模型比较的是模型表征与神经活动之间的相关，"
     "不涉及模型内部用什么元件。〔这一条是本连载的判断，原文未明说。〕",
     "**结论：相似成立在组织方式上，与生物实现的细节无关。**"],
    P(OUT, "11-card9.png"), figure_height=400,
    title="结论：相似成立在组织方式上", title_num="⑨",
)

# ---------- 12 尾卡 ----------
gen.tail_card(
    [
        "Nastase SA, Zada Z, Goldberg AE, Hasson U. (2026). Unifying the structures of language "
        "in a neural population code. Neuron 114. doi:10.1016/j.neuron.2026.07.024",
        "",
        "Perez-Nieves N, Leung VCH, Dragotti PL, Goodman DFM. (2021). Neural heterogeneity "
        "promotes robust learning. Nat Commun 12:5791.",
        "Stanojevic A, Wozniak S, Bellec G, et al. (2024). High-performance deep spiking neural "
        "networks with 0.3 spikes per neuron. Nat Commun 15:6793.",
        "Whittington JCR, Bogacz R. (2019). Theories of error back-propagation in the brain. "
        "Trends Cogn Sci 23:235–250.",
        "Kozachkov L, Kastanenka KV, Krotov D. (2023). Building transformers from neurons and "
        "astrocytes. PNAS 120:e2219150120.",
        "Giraud A-L, Kleinschmidt A, Poeppel D, et al. (2007). Endogenous cortical rhythms "
        "determine cerebral specialization for speech perception and production. Neuron 56:1127.",
        "Zada Z, Nastase SA, Li J, Hasson U. (2025). Brains and language models converge on a "
        "shared conceptual space across different languages. arXiv:2506.20489",
    ],
    P(OUT, "12-tail.png"),
    lead_paragraphs=["**下期预告**：第二类差距——学习条件。人用远少的输入学到了同一套表征。"],
)

print("done")
