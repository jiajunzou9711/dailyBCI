# -*- coding: utf-8 -*-
"""日报 2026-08-24「语言的神经群体编码」第四期：18 张图卡。"""
import os, sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(SCRIPT_DIR))
from card_generator import CardGenerator

SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-08-24-langcode-04")
FIGS = os.path.join(OUT, "figs")
PAPERS = os.path.join(PROJECT, "papers")
os.makedirs(OUT, exist_ok=True)
P = lambda *a: os.path.join(*a)

gen = CardGenerator(date="2026.08.24")
NS = "Nastase et al. 2026, Neuron, Fig. 2（改编自 Goldstein et al. 2025）"

# ---------- 01 封面 ----------
gen.cover_card(
    "语音区管语音，语义区管语义？",
    "单个电极上两者都在",
    "皮层的语言层级确实有先后，但相邻层级在同一批位点上重叠。",
    P(OUT, "01-cover.png"),
    concept_image=P(PAPERS, "ns-fig2B.png"),
    concept_height=790,
    concept_bleed=36,
    title_size=59,
    title_top=110,
)

# ---------- 02 目录 ----------
gen.figure_card(
    P(FIGS, "toc.png"), "本期路线",
    ["本期是 Neuron 观点文章《Unifying the structures of language in a neural population code》"
     "多期连载的第四期。作者为 Samuel A. Nastase、Zaid Zada、Adele Goldberg、Uri Hasson。",
     "本期主要材料是它引用的一项实证工作：Goldstein 等 2025 年发表于 Nature Human Behaviour 的"
     "《A unified acoustic-to-speech-to-language embedding space captures the neural basis of "
     "natural language processing in everyday conversations》。观点文章的 Figure 2 即改编自该研究。"
     "所用模型来自 Radford 等 2023 年的《Robust Speech Recognition via Large-Scale Weak Supervision》（Whisper）。"],
    P(OUT, "02-toc.png"), figure_height=560, annot_size=27,
)

# ---------- 03 ① 钩子 ----------
gen.text_card(
    "① 能解出音素，就说明里面有音素吗",
    ["从颅内电极记录里，可以训练一个分类器把音素读出来。这个结果通常被当作「皮层里存在音素这一层」的证据。"
     "**本期要检验的就是这一步推论。**",
     "两句话的形式并不一样。「音素可被解码」是一个存在命题：**存在某个方向，把不同音素分开。**"
     "「以音素为单位存储」是关于表征怎么组织的命题。后者成立时前者必然成立，**反过来不成立**。",
     "要检验反向能否成立，需要一个**内部构造完全已知**的系统——能直接查明里面到底有没有音素单位。"
     "大脑做不到这一点，模型可以。"],
    P(OUT, "03-card1.png"),
)

# ---------- 04 ② Whisper ----------
gen.figure_card(
    P(FIGS, "fig-whisper.png"), "自制示意图",
    ["Whisper 是编码器-解码器结构的语音转文本模型。**音频编码器**接收声谱图，"
     "**文本解码器**逐个产出文本，两侧由**交叉注意力**衔接。",
     "研究者从中取出三层：音频编码器**早期层**（声学嵌入）、音频编码器**最后一层**（语音嵌入）、"
     "文本解码器**较晚的中间层**（上下文词嵌入）。三个位置都由架构确定，不是任选的。",
     "**关键的一条事实**：训练目标只有「音频 → 文本」，标注里没有任何音位或句法标记。"
     "模型里没有任何一层、任何一组单元是为音素设立的。"],
    P(OUT, "04-card2.png"), figure_height=430, title="Whisper：编码器管语音，解码器管语言", title_num="②",
)

# ---------- 05 ③ 2A ----------
gen.figure_card(
    P(PAPERS, "ns-fig2A.png"), NS,
    ["先看一个可比较的量：把候选特征当自变量去预测 ECoG 高频活动，在**留出的对话**上算预测相关。"
     "谁解释的方差多，就说谁更接近这块皮层在算的东西。数据是约 100 小时自然对话的皮层表面电极记录。",
     "如上图，深色曲线是 Whisper 的嵌入，浅色是手工的符号特征（音素、词性）。"
     "**产生和理解两种状态下，嵌入的编码表现都大幅高于符号特征。**"],
    P(OUT, "05-card3.png"), figure_height=580, title="嵌入的编码表现大幅超过手工符号特征", title_num="③",
)

# ---------- 06 ④ 2B ----------
gen.figure_card(
    P(PAPERS, "ns-fig2B.png"), NS,
    ["三套嵌入分别预测到哪些电极，结果有顺序：**声学嵌入**集中在感觉与发音相关区；"
     "**语音嵌入**范围宽得多，理解时最强在颞上回，产生时在运动区；"
     "**上下文词嵌入**最强在额下回与角回这类高级语言区。",
     "**模型层的先后，与皮层层级的先后对应。** 这条比单纯「预测得更准」有分量，"
     "因为皮层的先后由解剖连接确定，不依赖任何模型。"],
    P(OUT, "06-card4.png"), figure_height=560, title="模型层的先后，对上了皮层层级的先后", title_num="④",
)

# ---------- 07 ⑤ 强度边界 ----------
gen.text_card(
    "⑤ 这个胜出推不出「皮层不用音素」",
    ["它能支持的是一个关于**描述层次**的否定结论：音素、词性这类离散标签，**不足以描述**这块皮层在算的东西。",
     "推不出更强的结论，有两条理由。",
     "**第一，符号特征是粗粒化之后的摘要。** 把一段声音压成「这是 /d/」，范畴内的声学变化全部丢掉。"
     "即便皮层真以音素为单位，它的活动里也必然残留大量连续声学变化，这部分符号特征结构上无法预测。"
     "**嵌入赢，一部分来自信息量差异，不全是格式差异。**",
     "**第二，嵌入的维数远高于符号特征**，自变量更多更灵活。正则化和留出集只能部分控制这一点。",
     "所以这一条本身不构成结论。"],
    P(OUT, "07-card5.png"),
)

# ---------- 08 ⑥ 判据 ----------
gen.figure_card(
    P(FIGS, "fig-regime.png"), "自制示意图",
    ["回到开篇那一步推论。空间里 P 个点随手贴上两类标签，存不存在把两类分开的超平面，"
     "**只取决于 P 与维数 N 的比值**（Cover 1965）。",
     "如上图，这个判断里没有出现「标签是什么」。标签有没有意义、系统用不用它，都不进入计算。",
     "**一处必须收紧**：真实实验里样本数远大于维数，上界不直接适用，可分性不是自动的。"
     "计数论证给的不是「一定能解出来」，而是**解码成功所能承担的推论上限**——它只报告信息可取到，"
     "不报告信息以什么为单位组织。"],
    P(OUT, "08-card6.png"), figure_height=430, title="解码成功这件事，信息量比想的低", title_num="⑥",
)

# ---------- 09 ⑦ 取层 ----------
gen.text_card(
    "⑦ 去哪一层找音素，去哪一层找词性",
    ["下面换一个方向：不碰大脑，只看模型内部。取出嵌入向量，按对应时刻贴上标签，问标签能否从这个空间里读出来。",
     "**找音素用语音嵌入**，即音频编码器的最后一层。取它的理由是结构性的：这一层就是交给解码器的接口，"
     "交叉注意力读的正是它，是语音侧被加工到头的表征。",
     "**找词性用语言嵌入**，即文本解码器较晚的中间层，不是最后一层。最后一层紧接着投影到词表，"
     "被下一个 token 的判定主导，不再是通用的语言表征。",
     "对应关系因此很直接：**音素是语音一级的单位，就去语音侧那一层找；词性是语言一级的单位，就去语言侧那一层找。**"],
    P(OUT, "09-card7.png"),
)

# ---------- 10 ⑧ 双分离 ----------
gen.figure_card(
    P(PAPERS, "ns-fig2CD.png"), NS,
    ["上行是音素（2C），下行是词性（2D）；每行左侧为语音嵌入空间，右侧为语言嵌入空间。",
     "**音素能从语音嵌入里恢复，在语言嵌入里就不那么清楚；词性能从语言嵌入里恢复，在语音嵌入里则不明显。**",
     "这个双分离排除了一种常见质疑——「高维空间里什么都能解出来」。若真如此，两种标签在两侧都该读得出。"
     "所以这两类符号与模型内部的表征结构**分层**相关。"],
    P(OUT, "10-card8.png"), figure_height=540, title="两种符号，各自只在对应那一侧可读", title_num="⑧",
)

# ---------- 11 ⑨ 反例 ----------
gen.text_card(
    "⑨ 模型内部没有音素单位",
    ["这里有一个别处得不到的条件：**Whisper 的构造完全已知。** 训练目标只有音频转文本，"
     "架构里没有任何一组单元是为音素设立的。",
     "于是事实是确定的：**模型内部不存在离散的音素单位，而音素仍然可以从它的嵌入空间里部分读出来。**"
     "原文的措辞是 partially recovered 与 approximate byproducts——这些类别是嵌入几何的近似副产物，"
     "几何本身完全由预测语音和文本这个任务塑造。",
     "**对大脑那边，这取消了一步推论，而不是证否。** 此前的形态是「从颞上回能解出音素，所以皮层有音素这一层」；"
     "现在有一个确知不含音素单位、却产生同样观测的系统，该观测因此不再能区分两种情况。"],
    P(OUT, "11-card9.png"),
)

# ---------- 12 ⑩ 新张力 ----------
gen.text_card(
    "⑩ 没有符号单位，层级顺序却是真的",
    ["两个结论同时成立：内部没有离散符号单位（⑨），层级顺序确实存在（④）。**问题于是变成：层级以什么形式存在。**",
     "要回答它，不能只看两个模型各自的预测相关。对某个电极分别拟合「只用语音嵌入」和「只用语言嵌入」，"
     "两个都不错——这不能推出该电极同时携带两级信息。",
     "**原因是两组特征本身高度相关**：语言嵌入是同一模型内由语音嵌入经交叉注意力算出来的。"
     "两个模型各自成功，可能来自同一份被解释的方差。",
     "要区分，必须问一个不同的问题：**去掉另一组已经能解释的部分，每一组还剩多少独有贡献。**"],
    P(OUT, "12-card10.png"),
)

# ---------- 13 ⑪ 方差分解 ----------
gen.figure_card(
    P(FIGS, "fig-varpart.png"), "自制示意图",
    ["做法是对同一个电极拟合**三个**编码模型，都在留出数据上算解释方差。",
     "如上图，S 独有 = R²(S+L) − R²(L)，L 独有 = R²(S+L) − R²(S)，共享 = R²(S) + R²(L) − R²(S+L)。",
     "**判据落在独有那两块**：都显著大于零，才叫混合调谐。"
     "作为对照，若两组一起的 R² 与单用 S 相同，则 L 独有为零，该电极就是纯语音一级的。",
     "**结果是许多电极落在混合调谐这一类。**"],
    P(OUT, "13-card11.png"), figure_height=460, title="方差分解：独有的那部分才算数", title_num="⑪",
)

# ---------- 14 ⑫ 两条结果 ----------
gen.text_card(
    "⑫ 两条结果，分别否定流水线的两个性质",
    ["**第一条，逐电极的混合调谐。** 分区图景预测每个位点只属于一级，即只有一组特征的独有方差显著、另一组接近零。"
     "实际许多电极两块都显著。分析是逐电极做的，这不可能是跨区域平均造成的假象。",
     "**第二条，高层纳入低层后预测更准。** 经典流水线是逐级丢信息的：判定「这是 /d/」之后，"
     "范畴内的声学细节不再往下传，这是离散化的必然结果。而上下文词嵌入在纳入语音嵌入的信息之后，"
     "对很多电极预测得更准——**低层信息在高层阶段仍然存在。**",
     "**准确口径**：空间特异性是存在的，④ 已经确立三级各有预测最强的区域。混合调谐说的是相邻层级在同一批位点上重叠，"
     "不是位点之间无差别。原文只说 many electrodes，其余电极仍偏纯。"],
    P(OUT, "14-card12.png"),
)

# ---------- 15 ⑬ 落点一 ----------
gen.text_card(
    "⑬ 可读出，与以该形式为单位存储",
    ["回到开篇那一步推论，现在可以给出结论：**信息能被读出来，与信息以该形式为单位存储，是两件事。**",
     "Whisper 把这一点从抽象的逻辑关系变成了一个具体反例——在同一个系统里，"
     "音素可读出与音素单位不存在**同时成立**。",
     "这对解码类研究是一条通用的边界：**解出来了，只报告信息可取到。**"
     "要判定格式，得有独立于解码的证据。"],
    P(OUT, "15-card13.png"),
)

# ---------- 16 ⑭ 落点二 ----------
gen.text_card(
    "⑭ 层级仍在，但是有序的梯度",
    ["所以离散的音素层不是必需的。一套完全不含音位标注的模型，既更能预测皮层活动，"
     "又能在内部没有音素单位的情况下让音素被读出来。",
     "但层级本身没有被否定。声学、语音、语言三级各有预测最强的区域，先后与皮层层级对应。"
     "**变的是层与层之间的关系：许多位点同时对相邻两级有调谐，高层也没有丢掉低层的信息。**",
     "**区域层面有分工，位点层面不干净。这是一个有序的梯度，不是互不重叠的分区。**",
     "这与本连载第一期的主线一致：不同层级是同一个高维空间里的方向。"],
    P(OUT, "16-card14.png"),
)

# ---------- 17 / 18 尾卡 ----------
gen.tail_card(
    ["¹ Nastase, S.A., Zada, Z., Goldberg, A.E., and Hasson, U. (2026). Unifying the structures of "
     "language in a neural population code. Neuron 114. https://doi.org/10.1016/j.neuron.2026.07.024",
     "",
     "² Goldstein, A., Wang, H., Niekerken, L., Schain, M., Zada, Z., Aubrey, B., Sheffer, T., "
     "Nastase, S.A., Gazula, H., Singh, A., et al. (2025). A unified acoustic-to-speech-to-language "
     "embedding space captures the neural basis of natural language processing in everyday "
     "conversations. Nat. Hum. Behav. 9, 1041–1055.",
     "",
     "³ Radford, A., Kim, J.W., Xu, T., Brockman, G., McLeavey, C., and Sutskever, I. (2023). "
     "Robust speech recognition via large-scale weak supervision. ICML 40.",
     "",
     "⁴ Cover, T.M. (1965). Geometrical and statistical properties of systems of linear inequalities "
     "with applications in pattern recognition. IEEE Trans. Electron. Comput. EC-14, 326–334."],
    P(OUT, "17-tail1.png"),
    lead_paragraphs=["下一期接 Figure 3：对话中说者与听者的表征几何如何对齐。"],
)

gen.tail_card(
    ["⁵ Mesgarani, N., Cheung, C., Johnson, K., and Chang, E.F. (2014). Phonetic feature encoding "
     "in human superior temporal gyrus. Science 343, 1006–1010.",
     "",
     "⁶ Kell, A.J.E., Yamins, D.L.K., Shook, E.N., Norman-Haignere, S.V., and McDermott, J.H. (2018). "
     "A task-optimized neural network replicates human auditory behavior, predicts brain responses, "
     "and reveals a cortical processing hierarchy. Neuron 98, 630–644.",
     "",
     "⁷ Rigotti, M., Barak, O., Warden, M.R., Wang, X.-J., Daw, N.D., Miller, E.K., and Fusi, S. (2013). "
     "The importance of mixed selectivity in complex cognitive tasks. Nature 497, 585–590.",
     "",
     "图片来源：Figure 2 各面板取自 Nastase et al. 2026, Neuron（Open Access），"
     "该图改编自 Goldstein et al. 2025, Nature Human Behaviour。"],
    P(OUT, "18-tail2.png"),
)

print("done")
