"""日报 2026-08-18 第二期：语言的神经群体编码 ② —— 把大语言模型拆开当探针。

主文章 Nastase et al. 2026, Neuron (Perspective)；本期讲透它引用的实证工作
Kumar et al. 2024, Nat Commun。16 张卡。
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.dirname(HERE)
PROJECT = os.path.abspath(os.path.join(SCRIPTS, "..", "..", "..", ".."))
sys.path.insert(0, SCRIPTS)
from card_generator import CardGenerator  # noqa: E402

OUT = os.path.join(PROJECT, "output", "2026-08-18-langcode-02")
FIGS = os.path.join(OUT, "figs")
PAPERS = os.path.join(PROJECT, "papers")
os.makedirs(OUT, exist_ok=True)

gen = CardGenerator(date="2026.08.18")
P = lambda *a: os.path.join(*a)


def main():
    # ---------- 01 封面 ----------
    gen.cover_card(
        "把大语言模型拆开当探针",
        "发现语境梯度",
        "模型里的分工与皮层上的分布对得上，对上的方式是一条连续的梯度。",
        P(OUT, "01-cover.png"),
        concept_image=P(PAPERS, "cover-fig4E.png"),
        concept_height=620,
        title_size=78,
        title_top=95,
    )

    # ---------- 02 目录卡 ----------
    gen.figure_card(
        P(FIGS, "toc.png"), "本期路线",
        ["2026 年 8 月 · **Neuron** 观点文章《Unifying the structures of language in a neural "
         "population code》。一作 Samuel A. Nastase(南加州大学心理系 / 计算语言科学中心)，"
         "通讯 Uri Hasson(普林斯顿神经科学研究所)。**本系列第二期。**",
         "本期讲透的实证工作是它引用的 **Kumar 等人 2024 年**《Nat Commun》研究：**63 名被试**"
         "听自然口语故事时做 **fMRI**，把 BERT 的 **144 个注意力头**逐个取出，去预测 "
         "**1000 个皮层分区**的活动。",
         "该组 2022 年在《Nature Neuroscience》立起「人脑与语言模型共享计算原则」这条线，"
         "本篇是其方法学延伸(引用 87 次，Semantic Scholar 2026-08-18 读数；"
         "2022 年那篇 525 次)——**扎实的一步，不是范式级转折**。"],
        P(OUT, "02-toc.png"), figure_height=440, annot_size=27,
    )

    # ---------- 03 ① ----------
    gen.figure_card(
        P(FIGS, "fig-ivar.png"), "",
        ["上一期停在一个阴性结果：句法与语义在皮层上找不到分离。它拆掉了旧答案，"
         "**分不开的话它们究竟以什么形式在一起**，仍然悬着。",
         "补这一条的难处在于，大脑没法拆开逐个部件检查。作者的做法是**换一个自变量**："
         "以往用来解释脑活动的是刺激的某个属性(成分长度、语义内容)，这次改用 "
         "**BERT 内部的计算部件**¹。BERT 同样能处理语言，而它的内部结构完全透明，"
         "每个部件都可以单独取出来。",
         "两种自变量能给出的结论形式不同：前者只能回答敏感性的分布重不重叠，"
         "后者能回答**哪个部件对应哪片皮层、部件之间怎么排列**。"],
        P(OUT, "03-card1.png"), figure_height=430,
        title="换一个自变量", title_num="①",
    )

    # ---------- 04 ② ----------
    gen.figure_card(
        P(PAPERS, "kumar-fig1B.png"), "Kumar et al. 2024, Nat Commun · Fig 1B",
        ["BERT-base 的部件叫**注意力头**，12 层 × 每层 12 个，**共 144 个**¹。",
         "一层内的 12 个头**并行**工作：同时处理同一个词，各算各的权重、各自输出一段结果，"
         "再把 12 份结果一起加回中间那条 residual stream(这个词当前的表示，768 维)。"
         "层与层之间**串行**：这一层的输出送进下一层，由新的 12 个头再处理一遍，重复 12 次。"
         "**各层的参数彼此独立**，都是训练时各自学出来的。",
         "图上红色的 z₁…z₁₂ 就是这 12 个头各自的输出，作者称之为**变换**——"
         "**这正是后面要拿去预测 fMRI 的东西**。蓝色的 embeddings 是加完之后的结果，"
         "属于另一套特征。"],
        P(OUT, "04-card2.png"), figure_height=480,
        title="一层 12 个头，一共 12 层", title_num="②",
    )

    # ---------- 05 ③ ----------
    gen.figure_card(
        P(PAPERS, "kumar-fig1C.png"), "Kumar et al. 2024 · Fig 1C（把其中一个头拆开）",
        ["自下而上四步：句中每个词各算一个**键向量 K**；当前词额外算一个**查询向量 Q**；"
         "Q 与各个 K 相乘得到一组权重(图上线条越粗权重越大)；每个词再各算一个**值向量 V**，"
         "按这组权重加权求和，得到这个头的输出 **z**。",
         "BERT-base 每个词位的表示是 768 维，这 768 维被 12 个头**均分**，"
         "每个头分到 768 ÷ 12 = **64 维**，所以 z 就是 **64 个数**¹。",
         "**「这个头在看哪个词」，就体现在第三步那组权重上**——图上这个头把权重压在了 secret 上。"
         "不同的头分配权重的标准不同，这是训练中自己分化出来的。另外 BERT 是**双向**的²。"],
        P(OUT, "05-card3.png"), figure_height=470,
        title="一个头怎么算出它的输出", title_num="③",
    )

    # ---------- 06 ④ ----------
    gen.figure_card(
        P(FIGS, "fig-align.png"), "",
        ["接上的方式是**同一条时间轴**。被试听自然口语故事时做 fMRI(**63 名被试**)¹。"
         "fMRI 每隔一小段时间拍一张全脑图，这个间隔叫 **TR**，本研究是 **1.5 秒**¹。",
         "同一段故事的文字送进 BERT，某个头在每个词位吐出 64 个数；一个 TR 里通常落着好几个词，"
         "于是把这些词的向量取平均，得到每个 TR 一个 64 维向量。脑侧把皮层切成 **1000 个分区**，"
         "每个分区每个 TR 一个数。于是两边都成了同一条时间轴上的序列。",
         "**用回归拿模型那 64 列去预测脑区那 1 列**——权重在训练段拟合，相关在**留出段**计算。"
         "这个相关值就是「这个头 × 这个分区」的分数¹。"],
        P(OUT, "06-card4.png"), figure_height=460,
        title="一个头怎么对上一块脑区", title_num="④",
    )

    # ---------- 07 ⑤ ----------
    gen.figure_card(
        P(PAPERS, "kumar-fig4A.png"), "Kumar et al. 2024 · Fig 4A",
        ["一个头有 64 个特征、就有 64 个权重，取 **L2 范数**压成 1 个数。矩阵于是缩成 "
         "**144 行 × 1000 列**——每一行是一个头的**皮层指纹**：它在皮层上哪里权重大、哪里小¹。",
         "这张表直接看不出结构，于是做**主成分分析**。它的含义是：144 张指纹彼此不同，"
         "但差异并非随机，大部分可以用**两张基本指纹的加权组合**近似。"
         "**前两个主成分解释了 92% 的方差**，前九个解释 95%¹。",
         "于是每个头只保留两个坐标，成为平面上的一个点——**位置完全由它的皮层指纹决定**。"
         "右上角那 144 个灰点就是这么来的。"],
        P(OUT, "07-card5.png"), figure_height=430,
        title="144 个头 × 1000 个分区", title_num="⑤",
    )

    # ---------- 08 ⑥ ----------
    gen.figure_card(
        P(PAPERS, "kumar-fig4BC.png"), "Kumar et al. 2024 · Fig 4B、4C（PC1 与 PC2 涂回皮层）",
        ["一次主成分分析同时给出两样东西。**对头而言**，每个头拿到两个系数，当作坐标，"
         "就是那张 144 个点的散点图。**对脑而言**，每个主成分本身是一个 **1000 维的向量**——"
         "每个分区一个权重，把这些数涂回皮层，就是上面这两张红蓝图¹。",
         "红蓝的含义要连着散点图读：某个分区在 PC1 上是红色，意思是**散点图上 PC1 坐标越靠右的头，"
         "在这块分区预测得越好**；蓝色则相反。",
         "具体而言，PC1 的红色主要在**双侧后颞叶与左外侧前额叶**，蓝色大片在**内侧前额叶**；"
         "PC2 的红色在**前额叶与左前颞叶**¹。"],
        P(OUT, "08-card6.png"), figure_height=380,
        title="主成分的双重身份", title_num="⑥",
    )

    # ---------- 09 ⑦ ----------
    gen.figure_card(
        P(PAPERS, "kumar-fig4E-only.png"), "Kumar et al. 2024 · Fig 4E（144 个头，按回看距离上色）",
        ["这张图上，**点的位置由脑数据决定，颜色由模型自身属性决定**——两个互不相干的来源。",
         "颜色编的是**回看距离**：每个头的注意力权重平均落在当前词之前多少个 token，"
         "计算时完全不涉及大脑。色标是对数刻度，10⁰ 到 10²——深紫约只看前一个词，"
         "浅黄可达几十上百个词。**颜色沿纵轴 PC2 从下到上由深变浅**，横轴 PC1 看不出规律；"
         "定量上 **PC2 与回看距离相关 r=0.65**，远高于 PC1 的 0.20¹。",
         "头的注意力距离**上四分位数超过 30 个 token**，已跨越多个句子¹。PC2 正端对应的皮层区域是"
         "**前额叶和左前颞叶**——**皮层上整合跨度长的一端落在这里**。"],
        P(OUT, "09-card7.png"), figure_height=470,
        title="皮层的分化沿语境跨度排列", title_num="⑦",
    )

    # ---------- 10 ⑧ ----------
    gen.figure_card(
        P(PAPERS, "kumar-fig4F.png"), "Kumar et al. 2024 · Fig 4F（红点为已知的句法特化头）",
        ["红点是 Clark 等人 2019 年报告过的、**专攻某种句法依存关系**的头³，各自注明依存类型"
         "(ccomp 从句补语、dobj 直接宾语、nsubj 主语、amod 形容词修饰等)，灰点是其余的头。",
         "**其一，红点全部落在整体点云内部**，没有占据一个独立的角落——句法特化不构成一个"
         "与其他头分离的类别。**其二，它们横跨 PC1、集中在 PC2 的负端**¹，对应中间层、"
         "且回看距离偏短。唯独 **ccomp**(跨度最长的那类依存)落在 PC1 的最左端。",
         "**句法特化确实存在，它是这个连续空间里的一个区域。**"],
        P(OUT, "10-card8.png"), figure_height=470,
        title="句法特化不占独立分区", title_num="⑧",
    )

    # ---------- 11 ⑨ ----------
    gen.figure_card(
        P(PAPERS, "kumar-fig5A.png"), "Kumar et al. 2024 · Fig 5A（每个散点图 144 个点＝144 个头）",
        ["作者对「共享功能专门化」的**操作性定义**要更严：**在句法上更擅长的头，"
         "是不是也更能预测某个特定脑区**¹。",
         "这需要给每个头打两个分。**依存预测分**：这个头的注意力权重能多好地还原某一种句法依存"
         "关系，共查了 **12 种**。**脑预测分**：这个头的变换能多好地预测某个脑区的活动。"
         "然后固定一种依存、固定一个脑区，把 **144 个头画成 144 个点**，横轴取依存分、"
         "纵轴取脑分，算这些点的相关。",
         "同一种依存在不同脑区差别很大：**nsubj 对中额回 r=0.38，对背内侧前额叶只有 −0.03；"
         "dobj 对角回 r=0.37，对腹内侧前额叶 0.10**¹。"],
        P(OUT, "11-card9.png"), figure_height=420,
        title="给每个头打两个分", title_num="⑨",
    )

    # ---------- 12 ⑩ ----------
    gen.figure_card(
        P(PAPERS, "kumar-fig5BC.png"), "Kumar et al. 2024 · Fig 5B、5C（黑框为显著）",
        ["左边是 12 种依存 × 10 个脑区的相关矩阵，黑框表示显著(双尾置换检验，FDR 控制在 p<0.05)¹。",
         "最醒目的是**中额回(MFG)那一整列**：几乎所有 12 种依存关系在这里都显著。右边把每个"
         "脑区在 12 种依存上取平均，**MFG 最高约 0.30，腹内侧前额叶接近 0**¹。",
         "所以**脑区之间确有差别，但不存在「一种句法关系对应一个专属脑区」**——是同一个脑区对"
         "整批依存关系都对应得好。**边界：相关最高只有约 0.30。**"],
        P(OUT, "12-card10.png"), figure_height=470,
        title="对应有选择性，但不按句法种类分", title_num="⑩",
    )

    # ---------- 13 ⑪ ----------
    gen.figure_card(
        P(FIGS, "fig-controls.png"), "",
        ["作者做了两个对照，都跑在同一个对应分析上。",
         "**其一，把变换特征在每一层内跨头打乱。** 特征一个不少，只是不再按头组织。结果脑预测分"
         "和依存预测分双双下降，两者的对应**基本消失**¹。这说明起作用的是**特征按头组织的方式**，"
         "不只是特征的数量。**其二，换成未训练的 BERT。** 架构完全相同、刺激完全相同，"
         "只是权重随机，对应同样消失¹——说明它依赖模型**学到了真实语言的统计结构**。",
         "作者还在 GPT-2 上重跑了整套分析：对应值更高(尤其在额下回)，但跨脑区的特异性更低¹。"],
        P(OUT, "13-card11.png"), figure_height=400,
        title="排除拟合硬拗出来的可能", title_num="⑪",
    )

    # ---------- 14 ⑫ ----------
    gen.figure_card(
        P(FIGS, "fig-frame.png"), "",
        ["结论只到**表征格式**这一层，到不了机制。编码模型对得上，证明的是**模型捕捉到的某些信息"
         "同样编码在神经信号里**；它推不出大脑用了相似的架构或算法⁴。",
         "Perspective 的作者自己写死了这条边界：LLM 与大脑在电路架构、学习规则、目标函数、"
         "训练数据上差别巨大，他们要辩护的主张更窄——**两个系统收敛到相似的表征格式**⁴。"
         "所以模型在这里的角色是**参照系**：它提供一套可测量的属性(层深、语境跨度)，"
         "用来索引 BOLD 在皮层上的空间差异，**给的是索引**。",
         "**须一并说明**：本期主文献的作者列中包含 Nastase 与 Hasson，与这篇 Perspective 的作者"
         "重合，属自引；该组 2022 年在《Nature Neuroscience》立起这条线⁵。"],
        P(OUT, "14-card12.png"), figure_height=400,
        title="这套证据能说到哪一步", title_num="⑫",
    )

    # ---------- 15 尾卡（评论 + 下期预告） ----------
    gen.text_card(
        None,
        ["这一期把一件事讲透了：**模型里的分工与皮层上的分布对得上，而对上的方式是一条连续的"
         "梯度**——沿语境跨度排列，不按句法种类切块。",
         "它同时划出了这套证据的边界：对上的是表征格式，不是运算机制。**模型是参照系，"
         "没有填补脑内看不见的那一段。**",
         "**下一期 · 从句法语义，到音素词性**",
         "下一期换一批数据：皮层表面电极(ECoG)，约 100 小时开放式日常对话，"
         "模型换成语音转文本的 Whisper。要回答三个问题：",
         "· 声学、语音、语言三层嵌入，各自对应皮层的哪一片？",
         "· 音素和词性能从模型里解码出来——它们在模型内部真的存在吗？",
         "· 如果不存在，语音 BCI 的解码目标该定在哪一层？"],
        P(OUT, "15-tail1.png"),
        heading_lines=["分工对得上", "对上的方式是梯度"],
    )

    # ---------- 16 尾卡（参考文献） ----------
    gen.tail_card(
        ["¹ Kumar S, Sumers TR, Yamakoshi T, et al. (2024). Shared functional specialization "
         "in transformer-based language models and the human brain. Nat Commun 15:5523.",
         "² Devlin J, Chang M-W, Lee K, Toutanova K. (2019). BERT: pre-training of deep "
         "bidirectional transformers for language understanding. NAACL-HLT 2019:4171–4186.",
         "³ Clark K, Khandelwal U, Levy O, Manning CD. (2019). What does BERT look at? "
         "An analysis of BERT's attention. BlackboxNLP 2019:276–286.",
         "⁴ Nastase SA, Zada Z, Goldberg AE, Hasson U. (2026). Unifying the structures of "
         "language in a neural population code. Neuron 114. doi:10.1016/j.neuron.2026.07.024.",
         "⁵ Goldstein A, Zada Z, Buchnik E, et al. (2022). Shared computational principles for "
         "language processing in humans and deep language models. Nat Neurosci 25:369–380."],
        P(OUT, "16-tail2.png"),
    )

    print("done ->", OUT)


if __name__ == "__main__":
    main()
