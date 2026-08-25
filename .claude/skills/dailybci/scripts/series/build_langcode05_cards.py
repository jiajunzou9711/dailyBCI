# -*- coding: utf-8 -*-
"""日报 2026-08-25「语言的神经群体编码」第五期：18 张图卡。"""
import os, sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(SCRIPT_DIR))
from card_generator import CardGenerator

SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-08-25-langcode-05")
FIGS = os.path.join(OUT, "figs")
os.makedirs(OUT, exist_ok=True)
PAPERS = os.path.join(PROJECT, "papers")
P = lambda *a: os.path.join(*a)
SELF = "自制示意图"

gen = CardGenerator(date="2026.08.25")

# ---------- 01 封面 ----------
gen.cover_card(
    "大脑会猜下一个词",
    "这件事比听起来难证明得多",
    "词出现之前大脑确实有动作，但它不把某个具体的词提前放一遍。",
    P(OUT, "01-cover.png"),
    concept_image=P(PAPERS, "gs-fig3-curve.png"),
    concept_height=560,
    concept_bleed=70,
    title_size=64,
    title_top=300,
)

# ---------- 02 目录 ----------
gen.figure_card(
    P(FIGS, "toc.png"), "本期路线",
    ["本期是 Neuron 观点文章《Unifying the structures of language in a neural population code》"
     "多期连载的第五期。前四期讲的是该文的**原理一（表征格式）**，本期起进**原理二**——"
     "这套格式是靠在语境中做统计学习获得的，训练目标是预测序列里的下一个样本。",
     "本期只讲原理二的第一个案例：**语境驱动的预测性加工**。承重实证是 "
     "Goldstein 等 2022 年发表于 Nature Neuroscience 的"
     "《Shared computational principles for language processing in humans and deep language models》。**封面图与卡 ⑤⑥⑨ 的配图均取自该文正刊定稿**（Nat Neurosci 25:369–380）。"],
    P(OUT, "02-toc.png"), figure_height=600, annot_size=27,
)

# ---------- 03 ① ----------
gen.text_card(
    "① 听起来简单的一句话",
    ["「大脑会预测下一个词」，这句话人人接受。**它底下有一个没被回答的问题。**",
     "大脑是**在看到或听到这个词之前就已经算好了预期**，还是**等这个词出现之后才对它做处理**。",
     "两种说法都能解释我们听人说话时的流畅感受，却对大脑在做什么给出完全不同的描述。",
     "这个差别比它听起来大得多。"],
    P(OUT, "03-card1.png"),
)

# ---------- 04 ② ----------
gen.text_card(
    "② 本期的结论",
    ["**词出现之前，大脑确实有动作。**",
     "但那份动作不是把某个具体的词提前放一遍。作者主张的形式是：大脑维持一份**连续的、分布式的表征**，"
     "同时做两件事——编码当前的语境，并对**一批可能出现的后续词所共有的特征**做概率性的预期；"
     "**在词真正出现之前，不对其中任何一个作出承诺。**",
     "下面把这个结论拆成三条，逐条给理由与证据。"],
    P(OUT, "04-card2.png"),
)

# ---------- 05 ③ ----------
gen.text_card(
    "③ 为什么要去大脑里找预测",
    ["**这条路径的起点是 LLM 给出的一个存在性证明。**",
     "① 这类模型内部没有装入任何语言学单位——没有音素表、没有词性标签、没有句法树，"
     "训练目标只有预测下一个。② 它学出的表征比手工语言学特征更能解释脑活动（本连载三、四期）。"
     "③ 于是获得语言结构不必预先装入语言学规则，仅凭在语境中做统计学习就够。",
     "④ 但这只证明「可以这样做到」，没证明「大脑就是这样做的」。⑤ 所以要在大脑里找这条路径特有的痕迹——"
     "**如果大脑也靠预测来学，那么在输入到达之前，它就应当已经有所动作。**",
     "**强度边界**：即便找到痕迹，也只是让这个说法多一项支持，不等于证明大脑用的是同一套学习算法。"],
    P(OUT, "05-card3.png"),
)

# ---------- 06 ④ ----------
gen.figure_card(
    P(FIGS, "fig-two-accounts.png"), SELF,
    ["**经典证据支持不了这一条。**",
     "N400 是被试看到或听到某个词之后约 400 ms 出现的负向电位，该词越难预测，它负得越深¹。",
     "如上图，用「他很累，就睡着___」举例：**预期说**认为词出现前大脑已把「了」准备好，词来了只需比对；"
     "**事后整合说**认为词出现前什么都没准备，词来了才把它接进语境。**两者对 N400 的预期完全一样**，"
     "因为差别只体现在词出现之后。",
     "要区分它们，只能去词出现之前的时间段里找信号。"],
    P(OUT, "06-card4.png"), figure_height=430, title="经典证据与两种说法都相容", title_num="④",
)

# ---------- 07 ⑤ ----------
gen.figure_card(
    P(PAPERS, "gs-fig3-model.png"), "Goldstein et al. 2022, Nat Neurosci, Fig. 3b",
    ["**做法是把编码模型的时间轴挪一挪。**",
     "如上图，自变量是每个词的嵌入（50 维），乘上一组 β 系数得到重建的神经信号，"
     "再与实测信号求相关。**每个时间偏移、每个电极各拟合一次**，偏移取负值就是这个词出现之前。",
     "数据是九名被试、**1,339 个电极**的颅内记录；每个词的 onset 记为偏移 0，反应在 200 ms 窗口内平均后输入模型²。",
     "这必须用颅内记录——时间分辨率不够就无法区分词前与词后。"],
    P(OUT, "07-card5.png"), figure_height=580, title="把时间轴挪到词出现之前", title_num="⑤",
)

# ---------- 08 ⑥ ----------
gen.figure_card(
    P(PAPERS, "gs-fig6b.png"), "Goldstein et al. 2022, Nat Neurosci, Fig. 6b",
    ["**上下文嵌入比静态词向量更能解释词前的活动。**",
     "**静态词向量**（GloVe）一个词一个向量，与语境无关；**上下文嵌入**（GPT-2）则同一个词在不同语境里不同。",
     "如上图，品红是上下文嵌入，蓝色是静态嵌入。把上下文嵌入按词平均、去掉局部语境之后（橙），"
     "表现降到接近静态嵌入²。",
     "**要留意**：上下文嵌入有用，正是因为它把前文的信息算进了当前词的向量。这同时是后面那个混淆的来源。"],
    P(OUT, "08-card6.png"), figure_height=440, title="自变量用的是上下文嵌入", title_num="⑥",
)

# ---------- 09 ⑦ ----------
gen.figure_card(
    P(FIGS, "fig-samples.png"), SELF,
    ["**整个流程可以走一遍。**",
     "① 转写录音、强制对齐，拿到每个词的 onset；② 把开头到该词为止的文本输入 LLM，取该位置某一隐层的向量，"
     "再降到几十维；③ 神经信号取某电极的高频包络，每 25 ms 一个采样点；④ 挑一个偏移，例如 −200 ms。",
     "如上图，**一个词就是一个样本**：（该词的嵌入，该词 onset 前 200 ms 处的电极值）。"
     "⑤ 拟合并在留出的词上算预测相关；⑥ 偏移从 −1000 ms 扫到 +1000 ms，得到整条曲线。",
     "还有一处容易误解的地方要说清。"],
    P(OUT, "09-card7.png"), figure_height=400, title="一个词就是一个样本", title_num="⑦",
)

# ---------- 10 ⑧ ----------
gen.figure_card(
    P(FIGS, "fig-weights.png"), SELF,
    ["**权重只有一组，全体词共用。**",
     "这组权重定义的是嵌入空间上的一个线性函数，不是每个词各自的查找表。"
     "如上图，**不同的词得到不同的预测值，因为它们的嵌入不同，不是因为权重不同。**",
     "拟合就是找那组权重，使几千个预测值整体上最贴近实测值。"
     "若每个词各有一组权重，模型等于把每个词的答案记下来，留出的新词一个也预测不了。",
     "**所以这个相关在问**：知道即将出现的是哪个词，能不能帮我预测它出现前 200 ms 的神经活动。"],
    P(OUT, "10-card8.png"), figure_height=400, title="全体词共用一组权重", title_num="⑧",
)

# ---------- 11 ⑨ ----------
gen.figure_card(
    P(PAPERS, "gs-fig3-curve.png"), "Goldstein et al. 2022, Nat Neurosci, Fig. 3b",
    ["**分结论 A 的证据：曲线在 word onset 之前就抬起来了。**",
     "如上图，横轴是相对 word onset 的偏移，纵轴是实测与重建信号的相关。"
     "**黄色区域是词出现之前的那一段**，原文标注为 predictive signal；−100 ms 及更早的偏移，"
     "只包含这个词被感知之前采集到的神经信号²。",
     "也就是说，这个词还没有被看到或听到时，电极活动里已经带有关于它的信息。"
     "该图为单个电极，全体中有 **160 个电极**达到显著。",
     "但它单独还说明不了预测。"],
    P(OUT, "11-card9.png"), figure_height=420, title="曲线在 word onset 之前抬起", title_num="⑨",
)

# ---------- 12 ⑩ ----------
gen.figure_card(
    P(FIGS, "fig-confound.png"), SELF,
    ["**有一条完全不涉及预测的解释，能产生同样的曲线。**",
     "如上图，三者的关系是：那一刻的神经活动**由已出现的前文驱动**（被试刚听完那几个词）；"
     "而 W 的嵌入**与已出现的前文统计相关**（因为语言本身有结构）。两者之间于是出现相关，"
     "**中间不需要任何预测这一环。**",
     "这条相关经由前文这个共同来源产生，属于虚假相关。",
     "作者用三重分析逐条移除这个共同来源。"],
    P(OUT, "12-card10.png"), figure_height=400, title="曲线可能来自前文，与预测无关", title_num="⑩",
)

# ---------- 13 ⑪ ----------
gen.figure_card(
    P(FIGS, "fig-bigram.png"), SELF,
    ["**第一重：把自变量换成不带语境的静态词向量。** 其中不含任何前文信息，"
     "按前文解释的预期，词前的编码应当消失。**实际仍然存在**——卡 ⑨ 那条曲线本身就是静态 GloVe 嵌入的结果。",
     "**第二重：去掉高度可预测的双词搭配。** 第一重移除的是嵌入内部的前文信息；还有一条路径不经过模型——"
     "**W 的身份本身就能指示前文**。",
     "如上图，只要自变量取值为 x_节，因变量几乎总在 50 左右，回归学得到这条映射。"
     "而大脑在那一刻处理的是「圣诞」。信息在语料的搭配统计里，静态嵌入移不掉它。"
     "**把这类词整批去掉之后，效应仍然存在。**"],
    P(OUT, "13-card11.png"), figure_height=390, title="第一重与第二重", title_num="⑪",
)

# ---------- 14 ⑫ ----------
gen.figure_card(
    P(FIGS, "fig-residual.png"), SELF,
    ["**第三重处理的是普通语境。** 「他很累，就睡着」之后可能是「了」「吧」「呢」，没有哪个接近确定，"
     "但前文对后续词仍然携带部分信息。这类情况遍布整个语料，无法靠删词处理。",
     "如上图，做法分两步：先用前面几个词的嵌入预测那一刻的活动，再取**残差**——实测活动减去该预测值；"
     "然后用 W 的嵌入去预测这个残差。**实际结果是残差仍然能被预测。**",
     "**三重走完能说的是**：词出现之前，神经活动里存在一份关于这个词的信息，且前文解释不了它。",
     "到这里还没有说这份信息长什么样。"],
    P(OUT, "14-card12.png"), figure_height=380, title="第三重：把前文的贡献回归掉", title_num="⑫",
)

# ---------- 15 ⑬ ----------
gen.text_card(
    "⑬ 它不是那个词被提前激活",
    ["**最简单的设想在数据上不成立。**",
     "这个设想是：大脑把这个词自己的表征先放了一遍，词真的出现时只是同一份表征被输入再次驱动。"
     "它有可检验的后果——**词前建立的那套对应关系，应当能直接用到词后的活动上。**",
     "原文报告的是**不能**。所以词前的那份编码，与词出现之后的那份表征，是两个不同的东西。",
     "**边界**：内容相同与活动模式相同是两回事，所以这个结果否定的是「提前激活」这一种设想，"
     "否定不了预测本身。原文措辞也保守，称其为一条线索。"],
    P(OUT, "15-card13.png"),
)

# ---------- 16 ⑭ ----------
gen.text_card(
    "⑭ 作者给出的正面解释",
    ["**作者认为不能迁移是预料之中的。**",
     "理由写在原文里：**提前激活一个具体的词，要求大脑事先承诺唯一一个答案。** "
     "而语境通常允许多个后续，事先定下一个在多数情况下会错。",
     "他们主张的形式是：大脑维持一份连续的、分布式的表征，同时编码当前语境，"
     "并对**一批可能出现的后续词所共有的特征**做概率性的预期；在词真正出现之前，不对其中任何一个作出承诺。",
     "**模型那一侧是同样的结构**：它内部携带的是一个连续向量，直到最后一步投影到词表、采样时，"
     "才落到某个具体的词上。承诺发生在最后一刻。"],
    P(OUT, "16-card14.png"),
)

# ---------- 17 ⑮ ----------
gen.text_card(
    "⑮ 落点，以及仍在争论的部分",
    ["**大脑在词出现之前维持的是一份连续的、概率性的预期，不对任何一个具体的词作出承诺；"
     "承诺发生在词真正出现的那一刻。**",
     "作者还指出更深一层：在 LLM 里，逐时刻的预测同时**提供了驱动语言习得的反馈信号**——"
     "模型不只学会预测，还用预测来学³。预测在人类语言习得中起多大作用，原文写明仍是活跃的研究领域。",
     "**必须如实写出的争论**：词前编码的性质、以及它能在多大程度上与刺激驱动的依赖关系区分开，"
     "原文写明仍在争论中。已有研究正面主张**仅凭刺激依赖关系就能解释词前脑编码，无需诉诸下一个词预测**⁴，"
     "以及**词前编码并不反映提前激活**⁵。本期的三重分析是否真正移除了混淆，目前没有定论。",
     "**下期预告**：Case 4 与 Figure 3——两个人的神经调谐完全不同，如何收敛到相似的表征几何。"],
    P(OUT, "17-card15.png"),
)

# ---------- 18 尾卡 ----------
gen.tail_card(
    ["¹ Kutas, M., and Federmeier, K.D. (2011). Thirty years and counting: finding meaning in the "
     "N400 component of the event-related brain potential (ERP). Annu. Rev. Psychol. 62, 621–647.",
     "",
     "² Goldstein, A., Zada, Z., Buchnik, E., Schain, M., Price, A., Aubrey, B., Nastase, S.A., et al. "
     "(2022). Shared computational principles for language processing in humans and deep language "
     "models. Nat. Neurosci. 25, 369–380.",
     "",
     "³ Rabagliati, H., Gambi, C., and Pickering, M.J. (2016). Learning to predict or predicting to "
     "learn? Lang. Cogn. Neurosci. 31, 94–105.",
     "",
     "⁴ Schönmann, I., Szewczyk, J., de Lange, F.P., and Heilbron, M. (2026). Stimulus dependencies—"
     "rather than next-word prediction—can explain pre-onset brain encoding in naturalistic listening "
     "designs. eLife 14, RP106543.",
     "",
     "⁵ Azizpour, S., Westner, B.U., Szewczyk, J., Güçlü, U., and Geerligs, L. (2026). Reassessing "
     "prediction in the brain: pre-onset neural encoding during natural listening does not reflect "
     "pre-activation. eLife.",
     "",
     "本期主文章：Nastase, S.A., Zada, Z., Goldberg, A.E., and Hasson, U. (2026). Neuron 114. "
     "https://doi.org/10.1016/j.neuron.2026.07.024"],
    P(OUT, "18-tail.png"),
)

print("done")
