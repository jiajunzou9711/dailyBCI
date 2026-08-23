# -*- coding: utf-8 -*-
"""日报 2026-08-23「语言的神经群体编码」第三期：16 张图卡。"""
import os, sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(SCRIPT_DIR))
from card_generator import CardGenerator

SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-08-23-langcode-03")
FIGS = os.path.join(OUT, "figs")
PAPERS = os.path.join(PROJECT, "papers")
os.makedirs(OUT, exist_ok=True)
P = lambda *a: os.path.join(*a)

gen = CardGenerator(date="2026.08.23")

# ---------- 01 封面 ----------
gen.cover_card(
    "声音先变成音素再变成词",
    "脑子未必这么切",
    "支持音素这一层的证据，来自一类分不开两种情况的实验设计。",
    P(OUT, "01-cover.png"),
    concept_image=P(PAPERS, "cover-mesg-fig1D.png"),
    concept_height=660,
    title_size=76,
    title_top=110,
)

# ---------- 02 目录 ----------
gen.figure_card(
    P(FIGS, "toc.png"), "本期路线",
    ["本期是 Neuron 观点文章《Unifying the structures of language in a neural population code》"
     "多期连载的第三期。该文 2026 年 8 月 14 日上线，作者为 Samuel A. Nastase（南加州大学心理系）、"
     "Zaid Zada、Adele Goldberg、Uri Hasson（普林斯顿大学）。",
     "本期主要材料是两篇被它引用的实证工作。Mesgarani 等 2014 年发表于 Science 的"
     "《Phonetic feature encoding in human superior temporal gyrus》：皮层表面高密度电极，"
     "六名癫痫术前患者，听自然连续语音。Kell 等 2018 年发表于 Neuron 的"
     "《A task-optimized neural network replicates human auditory behavior, predicts brain "
     "responses, and reveals a cortical processing hierarchy》：任务优化神经网络与 fMRI 对照。"],
    P(OUT, "02-toc.png"), figure_height=500, annot_size=27,
)

# ---------- 03 ① ----------
gen.figure_card(
    P(PAPERS, "fig1A-levels.png"), "Nastase et al. 2026, Neuron, Fig. 1A",
    ["听觉输入是连续的声压变化，理解一句话却要落到一本离散的词典上。中间必须发生一次转换。",
     "如上图，同一句话被六种层级依次描述：最下面是原始声波，往上依次是声谱图、国际音标、词素切分、"
     "依存树，最上面是写成共现计数向量的词义¹。**六个层级用了六种完全不同的数学对象。**",
     "传统方案是在两者之间插一层**音素**。"],
    P(OUT, "03-card1.png"), figure_height=620, title="连续的声音，离散的词典", title_num="①",
)

# ---------- 04 ② ----------
gen.text_card(
    None,
    ["这一层为什么非有不可，有两条理由。",
     "**第一，直接映射学不起来。** 若没有中间层，大脑要为每个词存下它的全部声学实现——"
     "男声女声、快说慢说、有没有口音，声谱图差别巨大。每遇到一个新说话人，整本词典都得重学一遍。"
     "插一层音素之后，只需把这个人的**约 40 个**音素对上，整本词典自动跟着适配。"
     "**约 40 个可复用的构件，拼出十万量级的词。**",
     "**第二，没听过的词也能复述。** 听到一个从未听过的词，你能当场读出来、记住、写下来。"
     "若声音直接对词典，词典里没有这一条，就没有任何表示可以存放它。"
     "所以在词之下，必然存在一个比词更小、可组合、能表示全新组合的单位。",
     "两条合起来：中间层同时解决了「学得起来」和「推得出去」。"
     "这条流水线被当成常识，靠的是它确实有真问题要解决，也确实解决了。"],
    P(OUT, "04-card2.png"), heading_lines=["② 中间层解决的两个问题"],
)

# ---------- 05 ③ ----------
gen.figure_card(
    P(PAPERS, "mesg-fig1A.png"), "Mesgarani et al. 2014, Science, Fig. 1A",
    ["支持这条流水线的神经证据，绝大多数来自一类做法：**拿音素当自变量**。",
     "最有代表性的是 Mesgarani 等人 2014 年发表于 Science 的工作²。如上图，红点是贴在皮层表面的"
     "高密度电极（**ECoG**，不穿刺皮层），密集覆盖颞上回。**六名**癫痫术前患者，"
     "每人 **37 至 102** 个位点，分析 **75–150 Hz** 的高伽马信号²。",
     "他们把自然连续语音按英语全部音位清单逐段标注，再问哪个电极对哪一类音位特征有反应。"],
    P(OUT, "05-card3.png"), figure_height=520, title="音素效应是怎么被找到的", title_num="③",
)

# ---------- 06 ④ ----------
gen.figure_card(
    P(PAPERS, "mesg-fig1B.png"), "Mesgarani et al. 2014, Science, Fig. 1B",
    ["结果很干净：单个电极对不同音位特征表现出选择性²。要看清它能说到哪一步，"
     "先要弄清「对塞音有反应」意味着什么。",
     "如上图，中间是**声谱图**——横轴时间、纵轴频率、深浅表示能量，下方是音标转写。"
     "**塞音**是近乎无声接一个突然的宽频爆发，**擦音**是持续的高频噪声，"
     "**元音**的能量稳定集中在几个频率上。",
     "所以一个「对塞音有选择性」的电极，更字面的描述是：它对某一种**谱时模式**有调谐。"
     "而所有塞音都带这个模式——音位范畴本就按发音方式定义。"],
    P(OUT, "06-card4.png"), figure_height=520, title="对塞音有反应，也可能只是声学形状", title_num="④",
)

# ---------- 07 ⑤ ----------
gen.figure_card(
    P(FIGS, "fig-two-cases.png"), "两种情况给出同一个观测",
    ["两种描述指向同一批电极，这带来一个具体的麻烦。",
     "如上图，用音位标签当自变量得到的结论是「电极反应与音位标签相关」，而这句话与两种情况都相容："
     "**情况 A**，皮层以音素为表征单位；**情况 B**，皮层编码一组连续声学特征，音位标签与它高度相关。"
     "**两条路径给出同样的实验结果。**",
     "这里没有数据问题，效应是真的；受限的是设计。同期工作是同一路数，自变量都是人手设计的特征³⁻⁵。"
     "Mesgarani 那篇自己也指出，音位特征的选择性可以直接关联到谱时声学线索的调谐，"
     "其中一些是非线性编码或多线索整合而来²。"],
    P(OUT, "07-card5.png"), figure_height=430, title="这类设计分不开的两种情况", title_num="⑤",
)

# ---------- 08 ⑥ ----------
gen.figure_card(
    P(FIGS, "fig-criterion.png"), "能把两者分开的判据",
    ["那么什么样的结果才能把两者分开。",
     "如上图，两种情况会给出形状不同的反应曲线。若真有音素这一层，应当看到**范畴不变性**："
     "同一个 /d/，男声女声快说慢说，声学差别很大而反应一致（蓝色的水平段）；"
     "跨过范畴边界时反应出现突变。若只是声学调谐，反应跟着声学连续地变（红线），边界处没有任何特殊。",
     "2014 年时缺的东西很具体：**一个能完成语音理解任务、内部确定不含音素、"
     "而且可以直接打开检查的系统。**"],
    P(OUT, "08-card6.png"), figure_height=430, title="判据：范畴不变性", title_num="⑥",
)

# ---------- 09 ⑦ ----------
gen.text_card(
    None,
    ["这样一个系统随后出现了。",
     "2018 年 Kell 等人在 Neuron 上训练了一个层级神经网络，完成**语音识别与音乐识别**两个任务⁶："
     "输入声波，输出词或音乐类型。作者给出的理由是，一个完整的听觉皮层模型必须能解决生态上真实的任务。",
     "**训练里没有出现过音素**——没有音位标注，没有谱时滤波器，没有任何人手设计的中间表征。"
     "网络自己长出什么表征，就是什么。",
     "两个行为学结果：它在两个任务上**做到人的水平**，并且**犯与人相似的错误**，尽管从未为此优化过。"
     "表现最好的那个网络还呈现出早期共享处理、其后分成语音与音乐两条通路的结构⁶。"],
    P(OUT, "09-card7.png"), heading_lines=["⑦ 不给音素，只给任务"],
)

# ---------- 10 ⑧ ----------
gen.figure_card(
    P(FIGS, "fig-controlled.png"), "受控对照的结构",
    ["真正承重的结果，在它与传统模型的一次直接对照里。",
     "如上图，**要预测的东西固定**：被试听自然声音时每个 fMRI 体素的反应。**框架固定**："
     "拿一组特征经线性回归预测体素反应，在留出数据上算相关。**唯一变动的是特征从哪来**——"
     "一组是人手设计的谱时滤波器，一组是网络为完成任务自己长出来的内部层激活。",
     "结果：**网络特征在整个听觉皮层都明显优于谱时滤波器模型**⁶。"],
    P(OUT, "10-card8.png"), figure_height=430, title="换一组特征，其他全都一样", title_num="⑧",
)

# ---------- 11 ⑨ ----------
gen.text_card(
    None,
    ["这个结果能下多强的结论，需要说准。",
     "「手工设计的层级」在声学这一级的正式形态，就是**谱时滤波器模型**——"
     "几十年来解释听觉皮层反应的标准工具。这次对照把它放在自己最擅长的位置上，"
     "然后被一组没有任何人设计过、纯粹从任务里长出来的特征超过了。",
     "于是能下的结论是：**要解释皮层反应，不必先假定那些手工设计的层级。**",
     "强度到此为止——「不必」与「不存在」是两回事，这篇没有回答大脑里有没有音素。"],
    P(OUT, "11-card9.png"), heading_lines=["⑨ 结论是「不必」，强度到此为止"],
)

# ---------- 12 ⑩ ----------
gen.figure_card(
    P(FIGS, "fig-hierarchy.png"), "两个顺序的对应",
    ["Kell 那篇还有第二种证据，性质不同。",
     "第一种是标量比较——谁预测得更准。第二种比的是**顺序**。如上图，两边各有一个顺序："
     "网络的层有先后，早层、中间层、晚层；听觉皮层分**初级**（颞横回一带）与**非初级**，初级在前。"
     "做法是看每个体素被网络的哪一层预测得最好。",
     "结果：**初级听皮层由中间层最佳预测，非初级由晚层最佳预测**⁶。两个顺序对上了。"],
    P(OUT, "12-card10.png"), figure_height=420, title="第二种证据：顺序对上了", title_num="⑩",
)

# ---------- 13 ⑪ ----------
gen.text_card(
    None,
    ["「预测得更准」这条结果可以有另一种解释：网络预测得好，也许只是因为它捕捉到了"
     "自然声音的通用统计规律，与皮层的组织方式无关。",
     "**顺序对应这条结果与该解释不相容。** 皮层的先后由解剖连接和反应潜伏期确定，不依赖任何模型。"
     "事前有四种可能的结果：所有脑区被同一层预测得最好、顺序相反、顺序无规律、顺序一致。"
     "**四种里只有最后一种符合「表征阶段对应」，实测得到的是最后一种。**",
     "这条结果能支持的结论仅限于：两者的表征阶段排成了同一个顺序。它不支持「两者机制相似」——"
     "网络的学习规则、连接方式与动力学，与大脑差别很大。"],
    P(OUT, "13-card11.png"), heading_lines=["⑪ 为什么顺序对应更有分量"],
)

# ---------- 14 ⑫ ----------
gen.text_card(
    None,
    ["要把这套对照抬到音素这一级，需要一个新的系统，它要同时满足三条。",
     "**① 能完成完整的「声音 → 文字」任务**，把连续语音转写成文本，也就是那条流水线声称要解释的事。",
     "**② 内部不内置音素，也不内置词性**，训练目标里没有音位标注、没有句法标注。",
     "**③ 内部可以分层取出，且不同层对应不同抽象水平**，只有这样才能问哪一层对上哪片皮层。",
     "**Whisper 三条都满足。** 它是 Transformer 的编码器-解码器结构：音频编码器接收声音，"
     "文本解码器产出文字，训练目标只是转写⁷。"],
    P(OUT, "14-card12.png"), heading_lines=["⑫ 作参照的系统要满足三条"],
)

# ---------- 15 ⑬ ----------
gen.figure_card(
    P(FIGS, "fig-pathways.png"), "两条通路的终点不同",
    ["它比上一个系统多出来的东西，来自任务本身。",
     "如上图，Kell 的网络输出一个标签，通路止于「词或音乐类型」，能对照的手工特征只到声学一级。"
     "Whisper 输出**连续文本**：转写真实对话必须处理同音词、词边界，"
     "以及只有靠上下文才能定的歧义。这个任务要求模型在内部长出带语境的、词一级以上的表征。",
     "于是能取出三个抽象水平的表征，去对照**声学、音素、词性**三级手工特征。"
     "**同一套对照逻辑，换一层手工特征。**"],
    P(OUT, "15-card13.png"), figure_height=420, title="输出连续文本，逼出更高层表征", title_num="⑬",
)

# ---------- 16 尾卡 ----------
gen.tail_card(
    ["¹ Nastase SA, Zada Z, Goldberg AE, Hasson U. (2026). Unifying the structures of "
     "language in a neural population code. Neuron 114.",
     "² Mesgarani N, Cheung C, Johnson K, Chang EF. (2014). Phonetic feature encoding in "
     "human superior temporal gyrus. Science 343:1006–1010.",
     "³ Chi T, Ru P, Shamma SA. (2005). Multiresolution spectrotemporal analysis of complex "
     "sounds. J Acoust Soc Am 118:887–906.",
     "⁴ Santoro R, et al. (2014). Encoding of natural sounds at multiple spectral and temporal "
     "resolutions in the human auditory cortex. PLOS Comput Biol 10:e1003412."],
    P(OUT, "16-tail1.png"),
    lead_paragraphs=[
        "这一期只做了一件事：把「大脑里有音素这一层」所依赖的证据摆出来看清楚。"
        "结论是那类证据不够——它分不开两种情况。这没有证明大脑里没有音素；"
        "要回答那个问题，得看范畴不变性这条判据。",
        "**下一期 · 三层嵌入对上皮层。** 两个问题：三层嵌入与音素、词性，谁更能预测皮层活动？"
        "音素和词性能不能从模型内部被读出来？"],
)

gen.tail_card(
    ["⁵ de Heer WA, Huth AG, Griffiths TL, Gallant JL, Theunissen FE. (2017). The hierarchical "
     "cortical organization of human speech processing. J Neurosci 37:6539–6557.",
     "⁶ Kell AJE, Yamins DLK, Shook EN, Norman-Haignere SV, McDermott JH. (2018). A "
     "task-optimized neural network replicates human auditory behavior, predicts brain "
     "responses, and reveals a cortical processing hierarchy. Neuron 98:630–644.e16.",
     "⁷ Radford A, Kim JW, Xu T, Brockman G, Mcleavey C, Sutskever I. (2023). Robust speech "
     "recognition via large-scale weak supervision. PMLR 202:28492–28518."],
    P(OUT, "17-tail2.png"),
)

print("done")
