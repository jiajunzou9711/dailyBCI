# -*- coding: utf-8 -*-
"""日报 2026-09-01「AI 像脑这件事，可能测错了地方（上）」全套图卡。"""
import sys, os
SKILL = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, SKILL)
from card_generator import CardGenerator

PROJ = os.path.abspath(os.path.join(SKILL, "..", "..", "..", ".."))
OUT = os.path.join(PROJ, "output", "2026-09-01-texture-alignment")
FIGS = os.path.join(OUT, "figs")
os.makedirs(OUT, exist_ok=True)
P = lambda n: os.path.join(OUT, n)
FIG1B = os.path.join(PROJ, "papers", "loke-fig1B.png")

gen = CardGenerator(date="2026.09.01")

PAPER = "Shared texture-like representations underlie deep neural network alignment with human visual processing"

H = {"02-toc": 700, "09-card7": 560}

# ---------- 01 封面 ----------
gen.cover_card(
    "AI 像脑这件事", "可能测错了地方",
    "两边对上的那一段，是纹理，与识别物体未必有关。",
    P("01-cover.png"),
    source=f"2026 年 8 月 Current Biology《{PAPER}》· 本期为该文解读（上）",
    concept_image=FIG1B, concept_height=450, title_size=112, title_top=40,
)

# ---------- 02 目录 + 来源 ----------
gen.figure_card(
    os.path.join(FIGS, "toc.png"), "本期路线（上篇）",
    ["2026 年 8 月 31 日 Current Biology 在线首发《" + PAPER + "》（预印本 2025 年 8 月已公开）。"
     "阿姆斯特丹大学心理学系与 Amsterdam Brain & Cognition 中心，一作 Jessica Loke，通讯作者 H. Steven Scholte——同组 2024 年在 J Cogn Neurosci 报告过「人类视觉皮层与深度卷积网络都高度依赖物体背景」，本篇是那条线的延续；"
     "二作 Lynn K.A. Sörensen 现属 MIT McGovern 脑研究所。",
     "方法：非侵入式 **EEG**（分析用 17 个后部电极），52 名人类被试观看 200 张图的三个版本（原图 / 纹理合成 / 只留物体），"
     "与 5 个深度网络架构的各层激活做加权表征相似性分析。上篇讲旧说法为什么松动、问题该怎么问、实验怎么搭；结果与边界放下篇。"],
    P("02-toc.png"), figure_height=H["02-toc"], annot_size=27,
)

# ---------- ① ----------
gen.text_card(None, [
    "过去十年有一条固定做法：把同一批图片喂给一个在 ImageNet 上训练好的深度网络，同时也给人或猕猴看，然后比较两边的**表征几何**——网络某一层对这批图的相互距离结构，与皮层对这批图的相互距离结构，有多像。像的程度叫**神经可预测性**，也叫**对齐**。",
    "这条做法被当回事，靠的是一个推论：网络是为物体识别训练的，它能预测视觉皮层的响应，说明两边在做同一件计算——识别物体。这个推论有实证起点：Yamins 等人 2014 年在猕猴上发现，网络的物体识别性能与它对**单个 IT 单元**响应的预测力**强相关**¹。",
    "这条推论后来遇到了两个不合拍的观测。",
], P("03-card1.png"), heading_lines=["① 网络与皮层的相似，比的是表征几何"])

# ---------- ② ----------
gen.text_card(None, [
    "两个观测与这个解释不合。",
    "第一，**把网络的识别准确率做上去，脑预测性并不跟着涨**，甚至反向²。",
    "第二，**权重完全没训练过的网络，脑预测性也高于随机水平**³。识别能力是训练出来的，训练前不该具备。",
    "这两处裂缝存在多年，通常被当作「指标不够灵敏」搁置。第一条有直接的实验证据。",
], P("04-card2.png"), heading_lines=["② 两个观测撑不住", "「共享物体识别计算」"])

# ---------- ③ ----------
gen.text_card(None, [
    "两组独立工作先后测了这件事，方向一致。",
    "Linsley 等人 2023 年用猕猴数据：两只猕猴，慢性植入 **32 通道多电极阵列**记录下颞叶（inferotemporal cortex, IT）神经元，按 Brain-Score 的标准流程评测 **135 个 DNN**。随 ImageNet 准确率上升，对 IT 的预测**变差**²。",
    "Conwell 等人 2024 年用人类数据：**NSD 7T 功能磁共振**，**224 个模型**逐项受控对照。分类准确率与脑预测力之间**几乎没有关系**；把训练用的图固定住，换架构（CNN ↔ Transformer）或换训练目标（有监督分类 / 对比自监督 / 视觉—语言对齐），脑预测力也几乎不动⁴。",
    "两者强度不同，一个是负相关、一个是无相关，但都指向同一件事：这个分数不由识别能力决定。第二处裂缝把这一点推得更远。",
], P("05-card3.png"), heading_lines=["③ 识别准确率与脑预测力基本脱钩"])

# ---------- ④ ----------
gen.text_card(None, [
    "这里有两层拟合，只去掉了一层。",
    "**网络权重的训练去掉了**——权重是随机初始化的，没学过任何东西。但**「网络中间层激活 → 脑响应」这一步映射仍然要拟合**，因为网络单元与神经元之间没有天然对应关系；评估仍在留出的图片与留出的被试上做。这样测出来，随机权重网络的脑预测性**高于随机水平**³。",
    "强度要收准：**训练仍然重要**。Conwell 给每个受测架构都配了一个随机初始化的对照（**N = 64**），训练带来的提升是全篇最大、最稳的一项（cRSA **β = 0.30**、veRSA **β = 0.56**，均 p < 0.001）⁴。",
    "所以这一条说的是：**架构本身、在任何学习发生之前，就已经能换到一部分非零的脑预测性**。习得的东西不该在训练前就有，这提示撑起对齐的成分与「学会识别物体」未必有关。",
], P("06-card4.png"), heading_lines=["④ 权重完全没训练的网络，", "也能预测出一部分脑响应"])

# ---------- ⑤ ----------
gen.text_card(None, [
    "两处裂缝合起来只证明了反面：对齐分数不由识别能力决定，也不完全依赖训练。它们没有回答这个分数由什么决定。",
    "问题因此要换一种问法。脑对一批图片的响应里同时含着好几种成分——局部图像统计、物体形状、语义类别；网络的中间层激活里也同时含着这些成分。**那个分数是它们叠在一起算出来的一个总量。** 能问且可答的形式因此是：这个总量主要由哪一个成分撑着。",
    "这是**成分归属**问题，与「像不像」的程度问题不同。它此前答不了，是因为在自然图片里这些成分绑在一起：同一张企鹅照片同时携带纹理统计与物体形状，无法从观测中分离这两者。",
], P("07-card5.png"), heading_lines=["⑤ 对齐分数是一个总量，", "问题在于哪个成分撑着它"])

# ---------- ⑥ ----------
gen.text_card(None, [
    "Loke 等人 2026 年把这个问题做成了可测的实验³。",
    "论文的原问题是：DNN 与脑的对齐，反映的是两边共享对**物体相关信息**的敏感性，还是共享对**纹理类统计**的敏感性³。作者同时划了一条边界：早期与中级视觉皮层编码这类统计，这件事已确立；他们要问的是另一件事——**对齐反映的是神经响应里的哪一个成分**³。",
    "押纹理统计这个候选，是因为两边各自被报告过在编码它。网络这边，Geirhos 等人 2019 年报告 ImageNet 训练的 CNN 存在 **texture bias**，分类时对纹理的依赖强于形状⁵（这一条后续有工作提出异议）；皮层这边，早期与中级视觉皮层编码纹理类统计⁶。",
    "自然图片里两种成分绑在一起，所以解法是人工造出**只保留其中一种**的图片，看对齐跟着哪一种走。**答案是纹理统计**³。",
], P("08-card6.png"), heading_lines=["⑥ 把两种成分拆开，", "看对齐跟着哪一个走"])

# ---------- ⑦ 图卡 ----------
gen.figure_card(
    FIG1B, "Loke et al. 2026, Current Biology, Fig 1B",
    ["如上图，三行对应三种条件，**同一列是同一张图的三个版本**。",
     "**红框 · 原图**：纹理统计、物体形状、背景三者齐全。**蓝框 · 纹理合成**：从白噪声出发，只匹配 **VGG-19 conv1_1 层的 Gram 矩阵**，最小化其均方距离——看第四列，企鹅的黑、白、黄三种材质与空间尺度都留着，企鹅本身没有了。**绿框 · 只留物体**：企鹅在，雪地没有了。",
     "对齐分数在哪一排最高，就说明它由哪一种成分撑着。"],
    P("09-card7.png"), figure_height=H["09-card7"],
    title="三种图片，每种只保留一部分成分", title_num="⑦",
)

# ---------- ⑧ ----------
gen.text_card(None, [
    "两边都不做识别任务，这是设计的一部分³。",
    "**人这边**：**52 人**进入统计（招募 57、排除 5）。**200 张图**（取自 THINGS-EEG2 的留出测试集，200 个物体概念各一张）的三个版本，用 RSVP 呈现——每张图 **100 ms**，刺激起始间隔 **200 ms**，每张重复 20 次。任务与图片内容无关：注视十字有 **3%** 的时候由白变粉，被试按空格，其余时间什么都不做。被试从头到尾没有被问过任何关于图片的问题。这叫**正交任务**，作用是让人盯住中心、保持清醒。若任务改成「这是不是企鹅」，就等于人为诱导了物体识别加工。",
    "**模型这边**：网络在 ImageNet 上**预训练好、权重冻结**，测试时只把这 200 张图跑一遍、取各中间层的激活。5 个架构共 21 个初始化，**所有层**都取，输出层不参与³。",
], P("10-card8.png"), heading_lines=["⑧ 被试只是看图，", "模型只是被跑一遍"])

# ---------- ⑨ ----------
gen.text_card(None, [
    "换算的载体是**表征差异矩阵**（representational dissimilarity matrix, RDM）。",
    "一张 200×200 的表，第 i 行第 j 列填「对第 i 张图的响应，与对第 j 张图的响应，有多不一样」，对角线为 0。网络单元与神经元之间没有一一对应关系，但「这 200 张图彼此有多不像」两边都能算，于是变得可比³。",
    "脑这边用 **17 个后部电极**，每个时间点上一张图的响应就是一个 17 维振幅向量。比较用 **weighted RSA + 岭回归**：把各层 RDM 加权组合去拟合 EEG 的 RDM，权重是学出来的；交叉验证留出 **15 名被试 + 100 张刺激**，重复 50 折。最终指标是 **0–500 ms 内 Pearson r 曲线下面积（AUC）**³。",
    "这个 AUC 还要再除以一个上限才能读，那个上限叫噪声天花板。",
], P("11-card9.png"), heading_lines=["⑨ 两边都换算成", "「这 200 张图彼此有多不像」"])

# ---------- ⑩ ----------
gen.text_card(None, [
    "任何模型都有一个到不了的上限。",
    "EEG 响应的总方差拆成三块：**所有被试共有的成分**、**个体特有的成分**、**测量噪声**。模型对所有被试用的是同一套刺激特征，顶多能解释第一块；后两块在原理上就预测不到。第一块占的比例就叫**可解释方差**，也就是天花板³。",
    "天花板只能估、不能直接测，所以它是一个**区间**，两端差的是「留出的那名被试算不算进平均里」³。**上界**是每名被试的 RDM 与**包含他自己**的全体被试平均 RDM 的相关，属高估；**下界**是与**不含他**的训练组平均 RDM 的相关，属低估。真实值落在两者之间。",
    "**这篇除的是上界**，属保守取法：报出来的比例读作「至少拿到这么多」。三种条件的天花板本身高低不同，不归一化就会把「这个条件天花板本来就低」误读成「模型在这个条件下更强」。",
], P("12-card10.png"), heading_lines=["⑩ AUC 要除以噪声天花板才能读"])

# ---------- ⑪ ----------
gen.text_card(None, [
    "把成分拆开之后得到的答案：**对齐由局部图像统计的全局汇总撑着**，与「学会识别物体」未必有关³。",
    "强度要收准。这削弱的是「对齐 ＝ 共享物体识别计算」这个**解释**，没有证伪「网络与脑存在共同之处」。共同之处确实存在，改写的是它的**成分归属**：两边对上的那一段，是早期的统计提取那一段。",
    "上篇到此为止。支撑这个答案的四组证据——哪一种图片对齐最高、纹理特征能不能反过来预测原图的脑响应、物体信息能否从 EEG 解出来、对齐落在哪个时间窗——下一期逐条给。",
], P("13-card11.png"), heading_lines=["⑪ 答案是纹理统计，", "但要说清它否掉了什么"])

# ---------- 尾卡 ----------
gen.tail_card([
    "¹ Yamins DLK, Hong H, Cadieu CF, Solomon EA, Seibert D, DiCarlo JJ. (2014). Performance-optimized hierarchical models predict neural responses in higher visual cortex. PNAS 111:8619–8624.",
    "² Linsley D, et al. (2023). Performance-optimized deep neural networks are evolving into worse models of inferotemporal visual cortex. NeurIPS 36:28873–28891.",
    "³ Loke J, Sörensen LKA, Groen IIA, Cappaert N, Scholte HS. (2026). Shared texture-like representations underlie deep neural network alignment with human visual processing. Current Biology 36:1–8.",
    "⁴ Conwell C, Prince JS, Kay KN, Alvarez GA, Konkle T. (2024). A large-scale examination of inductive biases shaping high-level visual representation in brains and machines. Nature Communications 15:9383.",
    "⁵ Geirhos R, et al. (2019). ImageNet-trained CNNs are biased towards texture; increasing shape bias improves accuracy and robustness. ICLR.",
    "⁶ Jagadeesh AV, Gardner JL. (2022). Texture-like representation of objects in human visual cortex. PNAS 119:e2115302119.",
], P("14-tail.png"), lead_paragraphs=[
    "下一期 · 证据与边界：① 哪一种图片的对齐最高，高多少；② 纹理特征能不能反过来预测原图的脑响应；③ 物体信息能从 EEG 解出来，为什么不提高对齐；④ 对齐落在哪个时间窗，200 ms 之后发生了什么。",
])

print("done")
