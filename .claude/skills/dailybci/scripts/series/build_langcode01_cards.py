"""日报 2026-08-17 第一期：语言的神经群体编码 ① —— 句法与语义在脑中没有分开。

主文章 Nastase et al. 2026, Neuron (Perspective)；本期讲透它引用的实证工作
Shain et al. 2024, J Cogn Neurosci。14 张卡。
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.dirname(HERE)
PROJECT = os.path.abspath(os.path.join(SCRIPTS, "..", "..", "..", ".."))
sys.path.insert(0, SCRIPTS)
from card_generator import CardGenerator  # noqa: E402

OUT = os.path.join(PROJECT, "output", "2026-08-17-language-population-code")
FIGS = os.path.join(OUT, "figs")
PAPERS = os.path.join(PROJECT, "papers")
os.makedirs(OUT, exist_ok=True)

gen = CardGenerator(date="2026.08.17")
P = lambda *a: os.path.join(*a)


def main():
    # ---------- 01 封面 ----------
    gen.cover_card(
        "语言被拆成语法和词义",
        "脑中找不到这条界线",
        "语言学画出的层级边界，未必是大脑实现语言时用的边界。",
        P(OUT, "01-cover.png"),
        concept_image=P(FIGS, "cover-fig3c-3x2.png"),
        concept_height=640,
        title_size=80,
        title_top=95,
    )

    # ---------- 02 目录卡 ----------
    gen.figure_card(
        P(FIGS, "toc.png"),
        "本期路线",
        ["2026 年 8 月 · **Neuron** 观点文章《Unifying the structures of language in a "
         "neural population code》。一作 Samuel A. Nastase(南加州大学心理系 / 计算语言科学中心)，"
         "通讯 Uri Hasson(普林斯顿神经科学研究所)。",
         "本期讲透的实证工作是它引用的 **Shain 等人 2024 年** 《J Cogn Neurosci》研究"
         "(MIT，Fedorenko 组)：**三个 fMRI 实验、75 名被试**，重做 2011 年那项支持"
         "「句法与语义分处两区」的里程碑研究。"],
        P(OUT, "02-toc.png"), figure_height=470, annot_size=27,
    )

    # ---------- 03 ① ----------
    gen.text_card(
        None,
        ["语言学把语言拆成音系、句法、语义、语用四块分别建模，神经语言学照着这张拆分图去脑中找对应的分区。"
         "三十年下来，结果对不上。",
         "早期有影响的工作把句法组合定位在**额下回盖部的一个亚区**¹；近期工作报告句法处理"
         "**分布在几乎整个语言网络上**，且与词义紧密缠绕²。",
         "作者给出两层诊断。方法上，受控实验为求干净把语境剥掉——孤立的词、去语境的句子、"
         "单个句法操作；这样得到的结论内部有效，却推不到自然语言使用上。更根本的一层是，"
         "句法树、线性化这类语言学描述单位，与整合发放、长时程增强这类神经机制单位，"
         "本来就不在同一个描述层级上³。",
         "由此给出的判断是：**拆分图本身可能就是错误的前提。那些边界是我们描述语言时画的。**"],
        P(OUT, "03-card1.png"),
        heading_lines=["① 拆分建模", "拼不出一致的图景"],
    )

    # ---------- 04 ② ----------
    gen.text_card(
        None,
        ["替代主张是：**语言的所有层级，统一编码在一个高维的神经群体编码里**——六个层级对应"
         "同一个空间里的六组方向，由同一批单元承载。",
         "论证方式是拿大语言模型当存在性证明。它不内置音系、句法、语义任何一个语言学构件，"
         "却掌握了语言。作者把它的成功抽成两条：**Principle 1 管表征格式**，把各种结构编码进"
         "一个统一的高维嵌入空间；**Principle 2 管学习机制**，用语境驱动的统计学习替代规则学习。",
         "两条原理各配两个人类神经证据的案例。**本期只做 Principle 1 的第一个：句法与语义。**",
         "这是一篇观点文章，全篇没有自己的新数据，四个案例都是转引已发表工作，"
         "它的贡献在框架与编排。"],
        P(OUT, "04-card2.png"),
        heading_lines=["② 一个主张、两条原理", "四个案例"],
    )

    # ---------- 05 ③ ----------
    gen.figure_card(
        P(PAPERS, "fig1.png"), "Nastase et al. 2026, Neuron · Fig 1",
        ["左栏摆的是待整合的清单：同一句话被六种层级依次画出——声波、声谱图、音标、词素、"
         "依存树、词义向量。六种完全不同的数学对象，彼此没有共同货币。",
         "中栏是答案。那一群圆圈是神经元样的计算单元，**每个圆圈都是多色的**，颜色对应左栏"
         "六个层级：单个单元同时对语音、词素、句法、语义有分级调谐。上方曲面是这群单元的"
         "状态空间，圈出的一小块拉到右边放大。",
         "右栏是答案的形态：king–man–woman–queen 连成平行四边形，know→known→knowing 与 "
         "show→shown→showing 彼此平行，we→wheat→wet 的语音接近对应空间接近。"
         "**六个层级成了同一空间里的六组方向**⁴。"],
        P(OUT, "05-card3.png"), figure_height=430,
        title="六个层级，一个空间，六组方向", title_num="③", annot_size=27,
    )

    # ---------- 06 ④ ----------
    gen.text_card(
        None,
        ["这个区分来自一组表明二者可以互相脱钩的观察。**语义**指一个词表示什么内容，"
         "**句法**指词按什么规则组合成合法的句子。",
         "**其一，句子可以结构合法、内容荒谬。** Colorless green ideas sleep furiously，"
         "每个词都懂、合起来毫无意义，读者却能立刻判断这是个合乎语法的英语句子⁵；"
         "把词序打乱就不成句了。**结构对不对**与**有没有意义**，是两种独立的判断。",
         "**其二，同样一组词，换顺序意思就变。** John loves Mary 与 Mary loves John⁶，"
         "词与词义完全相同，意思相反。一句话的意思有两个独立来源。",
         "于是语言学建成两层：一本词典加一套语法。两层的数学形式也不同——句法画成树，"
         "语义写成图或向量。**神经科学把这个拆法照搬到了脑区一级。**"],
        P(OUT, "06-card4.png"),
        heading_lines=["④ 语义和句法", "为什么被分成两样"],
    )

    # ---------- 07 ⑤ ----------
    gen.text_card(
        None,
        ["要检验「句法中枢 / 语义中枢」这个假设，Shain 等人回到了支撑它的那项里程碑研究——"
         "Pallier、Devauchelle 与 Dehaene 2011 年发在 PNAS 的工作⁷。该研究基于 fMRI 主张，"
         "选择性加工句法的脑区与选择性加工词汇语义、组合语义的脑区之间存在分离。",
         "**这项主张的赌注不止于语言。** 若这个分工为真，实现句法所需的抽象组合运算的脑环路，"
         "可能被调用去服务其他具有类似层级结构的认知功能——数学、音乐、动作规划²。",
         "Shain 等人改了三处：严格的**被试内**设计；用**独立数据**定义脑区、再量化其反应；"
         "**在每个被试自己的脑上**功能性地定位语言区。第三条最关键——功能区位置存在个体差异，"
         "而原研究的部分主张依赖于「某些脑区没有发现某种效应」，用灵敏度较低的组分析支撑"
         "这类阴性主张并不合适。**三个 fMRI 实验，合计 75 名被试**²。"],
        P(OUT, "07-card5.png"),
        heading_lines=["⑤ 重做一个里程碑实验"],
    )

    # ---------- 08 ⑥ ----------
    gen.figure_card(
        P(PAPERS, "shain-fig1A.png"), "Shain et al. 2024, J Cogn Neurosci · Fig 1A",
        ["这套材料的精巧之处，在于**总词数被卡死**：图上每一行都是 12 个词，一个不多一个不少。",
         "**变量一，句法负担，用「块长」拨。** 色框标出块边界：c01 是 12 个互不相连的词，"
         "c04 是三个 4 词块，c12 是一整句话。**词数、呈现时间、视觉输入量全部匹配**，"
         "变的只有一次能把多少个词连成一体。",
         "**变量二，语义内容，用假词版拨。** 蓝色的 jab- 各行把实词换成假词、句法框架逐字保留"
         "(higher and higher prices → hisker and hisker cleeces)。紫色的 nc 各行则是不构成"
         "完整句法成分的块²。"],
        P(OUT, "08-card6.png"), figure_height=420,
        title="一套材料，两个变量", title_num="⑥", annot_size=27,
    )

    # ---------- 09 ⑦ ----------
    gen.figure_card(
        P(FIGS, "cover-fig3c-3x2.png"), "Shain et al. 2024 · Fig 3C（实验二，n=40；六个区重排为 3×2）",
        ["三个实验都强复现了原研究的核心发现：**语言区活动随连成一体的那一段变长而增强**——"
         "上图六个脑区的红线(真词)都在上升，另有一组独立复现⁸。",
         "争议在于它是不是只发生在某个专门的地方。看**蓝线(假词)**：完全没有词义时，"
         "**所有语言区**同样上升，唯一的例外是右下角的角回²。",
         "**若存在一个句法中枢，这个纯结构、无词义的效应就该集中在它那里。实际是遍布。**"
         "用的是阳性效应的分布范围，比「某处没测到」硬。"],
        P(OUT, "09-card7.png"), figure_height=520,
        title="效应复现，定位推翻", title_num="⑦", annot_size=27,
    )

    # ---------- 10 ⑧ ----------
    gen.figure_card(
        P(FIGS, "fig3e-two-groups.png"), "Shain et al. 2024 · Fig 3E（取其中两组，星号为显著）",
        ["**左边一组是词汇性效应**：真词强于假词，**所有语言区都显著**²。语义那一侧同样不局限，"
         "两个中枢的对称主张到此都不成立。",
         "**右边一组分量最重**——块长 × 词汇性的**交互**：真词条件下的块长效应更陡。"
         "除左后颞叶(数值接近零)与左中额回(方向一致但未达显著)外，各区都显著。"
         "**结构加工的强度取决于词有没有意义。**",
         "共处一个区域还能解释成两群神经元恰好挤在一起；**互相调制不能**。这里也与原研究正面冲突："
         "它认为额下回对块长的敏感性在真假词下相当，实测是真词下明显更强²。"],
        P(OUT, "10-card8.png"), figure_height=470,
        title="词义效应也遍布，且与结构耦合", title_num="⑧", annot_size=27,
    )

    # ---------- 11 ⑨ ----------
    gen.figure_card(
        P(FIGS, "fig3d-3x2.png"), "Shain et al. 2024 · Fig 3D（实验三，n=20；六个区重排为 3×2）",
        ["前面所有结论都默认一个等式：**块变长 ＝ 句法结构变复杂**——因为原设计里每一块"
         "都是合法的句法成分。实验三查的就是这个等式。",
         "材料换成 24 词与 30 词的刺激，块取自自然文本，其中 **86.5% 并不构成合法句法成分**。"
         "上图六个区的上升与前两个实验同形；定量比较，**任何脑区、以及整个语言网络的水平上，"
         "都没有显著差异**²。",
         "**块长效应依赖的是连续连贯文本的长度，与这一段是否切在句法成分的边界上无关²。**"
         "前面几条争的是句法中枢在哪，这一条争的是它算不算句法效应。"],
        P(OUT, "11-card9.png"), figure_height=500,
        title="这个效应算不算句法效应", title_num="⑨", annot_size=27,
    )

    # ---------- 12 ⑩ ----------
    gen.text_card(
        None,
        ["「句法中枢 / 语义中枢」这个旧答案被拆掉了，「统一的高维空间」这个新答案还没立起来。"
         "至少三件事悬着。",
         "**其一，它说了「在哪里」，没说「以什么形式」。** 一个 fMRI 体素含数百万神经元，"
         "同一个体素里可以住着两群交织的神经元各管一样——那仍然是两套机制，只是耦合着。",
         "**其二，它拆掉了一个具体假设，新假设还没立起来。** 「两个中枢不成立」与"
         "「统一的高维几何」之间，还有很多种可能。",
         "**其三，它没有涉及运算。** 它报告的是哪里对什么敏感，没有说大脑在做什么计算；"
         "而表征格式这个主张，必须落到运算上才谈得清。"],
        P(OUT, "12-card10.png"),
        heading_lines=["⑩ 这批结果", "没有回答的三件事"],
    )

    # ---------- 13 尾卡（评论 + 下期预告） ----------
    gen.text_card(
        None,
        ["把语言拆成音系、句法、语义、语用，是一件在描述层面极其成功的事——它让有限的词和"
         "有限的规则生成无限多的句子，也撑起了三十年的实验设计。这批结果说的是另一件事："
         "**这套边界未必被大脑照搬。**",
         "对神经解码来说，这个区别是实在的。**能从神经数据里解码出句法、语义或音素，"
         "并不等于大脑内部存着这三样东西**——它们可能只是我们从一个连续表征空间里读出来的投影。",
         "**下一期 · 把大语言模型拆开当探针**",
         "· 一个注意力头，怎么和一块脑区对应上？",
         "· 模型里的分工和大脑里的分工，对得上的方式是什么？"],
        P(OUT, "13-tail1.png"),
        heading_lines=["描述语言的边界", "与实现语言的边界"],
    )

    # ---------- 14 尾卡（参考文献） ----------
    gen.tail_card(
        ["¹ Zaccarella E, Friederici AD. (2015). Merge in the human brain: a sub-region "
         "based functional investigation in the left pars opercularis. Front Psychol 6:1818.",
         "² Shain C, Kean H, Casto C, et al. (2024). Distributed sensitivity to syntax and "
         "semantics throughout the language network. J Cogn Neurosci 36:1427–1471.",
         "³ Poeppel D. (2012). The maps problem and the mapping problem: two challenges for a "
         "cognitive neuroscience of speech and language. Cogn Neuropsychol 29:34–55.",
         "⁴ Nastase SA, Zada Z, Goldberg AE, Hasson U. (2026). Unifying the structures of "
         "language in a neural population code. Neuron 114. doi:10.1016/j.neuron.2026.07.024.",
         "⁵ Chomsky N. (1957). Syntactic Structures. De Gruyter Mouton.",
         "⁶ Fodor JA, Pylyshyn ZW. (1988). Connectionism and cognitive architecture: a critical "
         "analysis. Cognition 28:3–71.",
         "⁷ Pallier C, Devauchelle A-D, Dehaene S. (2011). Cortical representation of the "
         "constituent structure of sentences. Proc Natl Acad Sci USA 108:2522–2527.",
         "⁸ Giglio L, Ostarek M, Weber K, Hagoort P. (2022). Commonalities and asymmetries in "
         "the neurobiological infrastructure for language production and comprehension. "
         "Cereb Cortex 32:1405–1418."],
        P(OUT, "14-tail2.png"),
    )

    print("done ->", OUT)


if __name__ == "__main__":
    main()
