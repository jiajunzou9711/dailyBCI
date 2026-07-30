# -*- coding: utf-8 -*-
"""Build 小红书 cards — 2026-07-30 Neuropixels Quad Base (Chang 2026, bioRxiv)."""
import sys, os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(SCRIPT_DIR))
from card_generator import CardGenerator

PROJECT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-07-30-quadbase")
FIG = os.path.join(OUT, "figs")
PAP = os.path.join(PROJECT, "papers")
os.makedirs(OUT, exist_ok=True)

gen = CardGenerator(date="2026.07.30")

# 01 封面
gen.cover_card(
    "脑区之间的联系",
    "只有同时记录才测得到",
    "同样的通道总量,一次八针脚同时记录检出的跨脑区关联,超过四次连续双针脚记录的总和。",
    os.path.join(OUT, "01-cover.png"),
    source="2026 年 7 月 · bioRxiv 预印本《Neuropixels 1536 Channel Quad Base probe reveals "
           "brain-wide communication underlying flexible sensorimotor sequences》。"
           "Johns Hopkins University、HHMI Janelia 与 imec 合作,资深作者 Daniel O'Connor 与 "
           "Timothy Harris(Harris 是 2017 年 Neuropixels 原始论文的资深作者)。"
           "方法:清醒小鼠双探针 3072 通道同时记录,并把同一份数据抽成标准探针的通道子集作对照。",
)

# 02 目录
gen.figure_card(
    os.path.join(FIG, "toc.png"),
    "本期路线",
    ["顺着这六步走,你会看到通道数决定的不只是测得准不准,而先是哪些问题存在可测量的形式。"],
    os.path.join(OUT, "02-toc.png"),
    figure_height=640,
)

# 03 钩子 + 为什么重要
gen.figure_card(
    os.path.join(FIG, "fig-tradeoff.png"),
    "图 1 · 通道有限时的三种取舍",
    [
        "做多脑区记录的人都遇到过同一个取舍。",
        "侵入式、穿刺进脑组织的高密度硅探针,针身上有 **5120** 个电极点,但同一时刻只有 "
        "**384** 个能被读出。于是覆盖更多脑区只有三条路:把通道集中在一根针脚上、沿深度密集采样;"
        "摊到四根针脚上、每根变稀;或者分几次记录、每次换一个位置,事后按任务事件对齐拼起来。"
        "第三条是领域里使用最广的做法。",
        "这篇论文把第三条路的代价算清楚了,而结论有一个明确的方向:分次拼接会让脑区之间的耦合"
        "看起来比实际更弱。",
    ],
    os.path.join(OUT, "03-tradeoff.png"),
    figure_height=530,
)

# 04 两类量的分界
gen.figure_card(
    os.path.join(FIG, "fig-twokinds.png"),
    "图 2 · 两类量的分界",
    [
        "这个代价只落在一类问题上。",
        "第一类问题只需要每个神经元各自的平均反应:单神经元调谐曲线、试次平均的群体几何、"
        "按条件解码。这类量与「谁和谁被同时记录」无关,分次记录再拼完全够用。",
        "第二类问题问的是两个神经元在同一时刻是否一起波动:**Granger 因果**"
        "(用一个神经元的过去,能否显著改善对另一个神经元当前活动的预测)、跨脑区共享的潜在维度。"
        "这类量定义在逐试次的协同波动上;两个神经元没有被同时记录,这个量就没有数值可算。",
    ],
    os.path.join(OUT, "04-twokinds.png"),
    figure_height=530,
)

# 05 两个「加」
gen.figure_card(
    os.path.join(FIG, "fig-twoadds.png"),
    "图 3 · 两个「加」不是一回事",
    [
        "说到把多次记录加起来,领域内第一反应通常是伪群体。",
        "**伪群体**(pseudo-population)把不同 session 里同一条件的试次配对,人为造出一个共同时间轴,"
        "于是分开记录的神经元可以并成一个群体。它保住了每个神经元的条件平均反应,代价是配对本身任意,"
        "跨神经元的逐试次协同波动被置为零——而那正是上一类量唯一需要的东西。",
        "这篇论文里的「加」是另一件事:四次记录各自在自己的神经元集合内部算出连接数,再把四个数字相加。"
        "每个神经元只长在一根针脚上,四份名单没有重复项,所以直接相加成立。而且这个算法对分次方案"
        "已经最宽容,它假设四次记录之间没有任何漂移损失。",
    ],
    os.path.join(OUT, "05-twoadds.png"),
    figure_height=520,
)

# 06 工具
gen.figure_card(
    os.path.join(PAP, "qb-fig1d.png"),
    "图 1d · 14 个脑区各自拿到的单神经元数",
    [
        "Quad Base 只动了一个数。",
        "四根针脚(各 10 mm)、5120 个电极点的几何来自前两代探针¹ ²,Quad Base 全部保留,"
        "只把**同时可读的通道数从 384 提到 1536**;代价付在探针基座(宽 3.5 → 10.2 mm)与外围硬件,"
        "噪声与增益与前一代相当。实验在清醒、头部固定的**小鼠**上插两根探针,合计 8 根针脚、"
        "**3072 通道**,每次记录平均 **1139 ± 94** 个合格单神经元。",
        "如上图,横轴是 14 个脑区,每个点是一次记录在该区拿到的单神经元数(圆点为探针 1、三角为探针 2,"
        "颜色区分 session,纵轴对数)。从 M2/ALM、M1 舌-颌区一路排到中脑网状核——"
        "这些区在同一次记录里同时被采到,且多数区都在 10² 量级以上。",
    ],
    os.path.join(OUT, "06-tool.png"),
    figure_height=520,
)

# 07 对照设计
gen.figure_card(
    os.path.join(PAP, "qb-fig1a.png"),
    "图 1a · 两代探针的架构对比",
    [
        "对照组没有另做一批实验。",
        "作者从同一份 1536 通道的记录里,按标准探针的通道图抽出 384 个通道,把其余 1152 个通道的"
        "数据当作不存在,再重新走一遍完整的动作电位分选流程。分选出的单神经元从 **1139 ± 94** 降到 "
        "**285 ± 9**。时间轴上什么都没动,丢掉的只是针身上另外那些位置在同时记录到的东西。",
        "如上图,同一套四针脚布局下同时通道数从 384 变成 1536(针身下段橙色是该配置实际启用的电极点)。"
        "于是两组共用同一批动物、同一批试次、同一批神经元,唯一差别是用了多少通道——"
        "不同动物、不同天、不同插针误差这些混杂被整体排除。",
    ],
    os.path.join(OUT, "07-control.png"),
    figure_height=520,
)

# 08 任务
gen.figure_card(
    os.path.join(PAP, "qb-fig2a.png"),
    "图 2a · 序列舔水任务",
    [
        "这些神经元记录在一个需要逐次重新瞄准的舔水任务里。",
        "如上图,小鼠头部固定,面前一个电机驱动的舔水口停在七个位置之一(虚线所示,从左到右记作 "
        "L3 到 R3)。七个位置排在一段以舌根为圆心的圆弧上,所以小鼠要改的是舌头伸出的**方位角**,"
        "伸出长度基本不变。",
        "舌头碰到水口,水口立刻跳到下一站,小鼠必须把方位角重新瞄过去。连过七站之后才有一段延迟的给水,"
        "前六次舔只负责推进序列。下一个试次走同样七个位置,方向反过来。",
    ],
    os.path.join(OUT, "08-task.png"),
    figure_height=520,
)

# 09 答案
gen.figure_card(
    os.path.join(PAP, "qb-fig4d.png"),
    "图 4d · 检出的跨区 Granger 因果连接数",
    [
        "一次同时记录赢,而且赢在总通道数相同的条件下。",
        "如上图,横轴是舔水期检出的跨脑区 Granger 因果连接数,纵轴是不舔期,双对数轴。"
        "红点是单次双针脚记录(约 10² 到 1.5×10³ 条),蓝色点云是四次连续双针脚记录的总和"
        "(右界约 6×10³ 条),黑星是一次八针脚同时记录(约 10⁴ 条)。",
        "**黑星落在整团蓝点的右侧。** 四次双针脚动用的通道总量与一次八针脚相同,检出的连接数仍然更少。"
        "差距的来源是一个可以算清楚的计数问题。",
    ],
    os.path.join(OUT, "09-answer.png"),
    figure_height=540,
)

# 10 机制
gen.figure_card(
    os.path.join(FIG, "fig-matrix.png"),
    "图 4 · 8 根针脚的配对覆盖",
    [
        "补不回来的原因在于「对」的增长方式。",
        "一条连接是一对神经元,产出单位是对而不是个。按论文报告的神经元数推算:1139 个神经元约 "
        "**64.8 万**对;四次记录各 285 个神经元、只能在各自内部数对,合计约 **16.2 万**对,差约 **4 倍**。",
        "如上图,8 根针脚两两配对共 36 类。一次同时记录可测全部 36 类;四次互不重复的双针脚只能测 "
        "12 类,缺掉的 24 类里那些神经元从未在同一时刻被记录。反过来 Bonferroni 校正随检验次数变严,"
        "把实测差距压到约 1.7 倍(以上均为推算与量级估计)。",
    ],
    os.path.join(OUT, "10-mechanism.png"),
    figure_height=470,
)

# 11 门槛效应
gen.figure_card(
    os.path.join(PAP, "qb-fig5c.png"),
    "图 5c · 达标脑区数",
    [
        "第二条证据里,损失换了一种形式。",
        "这一块用 **mDLAG**(把多个脑区的群体活动拆成「跨区共享成分」与「本区私有成分」的降维模型³)"
        "去找被多个脑区共同承载的活动成分。模型有一条硬性入场条件:一个脑区至少要有 **20** 个"
        "合格单神经元才被纳入。",
        "如上图,每条线连接同一次记录的两个值:左端是 Quad Base 达标的脑区数(单次最多 **10** 个),"
        "右端是同一份数据抽成标准通道子集后的平均值。所有线都在下降,均值从 **5** 个降到 **2** 个——"
        "脑区达不到门槛就整个掉出模型,跨这些区的问题连问都问不出来。",
    ],
    os.path.join(OUT, "11-threshold.png"),
    figure_height=520,
)

# 12 偏差有方向
gen.figure_card(
    os.path.join(PAP, "qb-fig5g.png"),
    "图 5g · 共享成分解释的方差比例",
    [
        "偏的方向是单边的。",
        "如上图,横轴是 Quad Base 记录中共享成分解释的方差比例,纵轴是同一份数据抽成标准通道子集后的"
        "对应值,虚线是对角线,共 **31** 次 session。多数点落在对角线下方。",
        "也就是说,通道抽稀之后,同一批神经活动里能被「跨脑区共享」解释的比例变小了。换个说法:"
        "用少通道做这个分析,会得出「这些脑区之间的共同波动比实际更少」的结论。这是系统性的低估,"
        "方向明确。同时记录还能回答一类关于时间先后的问题。",
    ],
    os.path.join(OUT, "12-direction.png"),
    figure_height=540,
)

# 13 跨脑区的时间先后
gen.figure_card(
    os.path.join(PAP, "qb-fig3c.png"),
    "图 3c · 标准与回退试次的可分性起始时刻",
    [
        "这类问题问的是哪个脑区先出现信号。",
        "每个 session 里有 **30%** 的试次,水口走到中点之后往回退一站,小鼠舔空一次再改向。"
        "作者在每个 2.5 ms 时间窗上,用各脑区的群体活动分类「这个试次是标准还是回退」。",
        "如上图,橙色的 M1 舌-颌区最先离开随机水平;下方给出各区起始时刻的中位数,M1 落在约 "
        "**0.19 秒**——此时舔空还在进行中,M2/ALM 约 0.25 秒,上丘与中脑网状核落在 0.28 秒附近。"
        "此前有工作把上丘视为快速触觉纠正的关键驱动者,作者把分歧归因于触发方式不同"
        "(这里由预期触觉的缺失触发),本文没有做实验检验这个解释。",
    ],
    os.path.join(OUT, "13-timing.png"),
    figure_height=530,
)

# 14 三条扩容路线
gen.figure_card(
    os.path.join(FIG, "fig-threeroutes.png"),
    "图 5 · 三条扩容路线的分工",
    [
        "扩大记录规模有三条路线,它们扩大的东西不同。",
        "如上图,**硬件路线**扩大的是可测的神经元对数与达标脑区数。**成像路线**扩大的是神经元总数——"
        "高速体积成像可同时记录约 **100 万**个神经元⁴,代价是钙成像类方法的时间分辨率达不到"
        "动作电位层级、深部结构受限。**模型路线**扩大的是可利用的数据量——跨 session、跨脑区、"
        "跨细胞类型的统一建模确实随规模持续提升⁵,它恢复的是潜在空间层面的共享结构。",
        "选哪条,取决于你要问的量属于前面说的哪一类。另有两件事需要先摆清楚。",
    ],
    os.path.join(OUT, "14-routes.png"),
    figure_height=580,
)

# 15 两件注意事项
gen.text_card(
    "两件需要先摆清楚的事",
    [
        "两件事都关系到「加神经元究竟买到了什么」。",
        "**第一,承重的变量是同时性与空间分布,不是神经元总数。** 1139 个神经元全部集中在一个脑区,"
        "与分散在 10 个脑区,总数相同,但前者的跨区问题根本不存在。",
        "**第二,加神经元并非永远有收益。** 记录规模与数据规模两侧的证据都指向未见饱和⁴ ⁵,"
        "但猕猴运动皮层里与行为相关的成分只有 **7 到 13 维**⁶;本文自己也观察到舌长、舌速这类变量的"
        "解码性能接近平台,并引用**信息受限相关**(噪声相关的特定结构会给可提取的信息设上限)"
        "作为原因之一⁷。",
        "所以这篇反驳的是「通道数已经够了」这个工程判断;单区解码存在信息上限这个理论结论仍然成立。",
    ],
    os.path.join(OUT, "15-caveats.png"),
)

# 16 尾卡 A
gen.tail_card(
    [
        "¹ Jun JJ, et al. (2017). Fully integrated silicon probes for high-density recording "
        "of neural activity. Nature 551:232–236.",
        "² Steinmetz NA, et al. (2021). Neuropixels 2.0: A miniaturized high-density probe "
        "for stable, long-term brain recordings. Science 372:eabf4588.",
        "³ Gokcen E, et al. (2023). Uncovering motifs of concurrent signaling across multiple "
        "neuronal populations. Adv Neural Inf Process Syst 36.",
    ],
    os.path.join(OUT, "16-tail-a.png"),
    lead_paragraphs=[
        "这篇的通道数翻四倍本身是渐进的。值得记住的是它顺带确立的一条判据:一项分析依赖的是"
        "每个神经元各自的平均反应,还是两个神经元在同一时刻的协同波动。前者可以靠更聪明的算法和"
        "更多次实验往前推;后者只能靠那一对神经元真的被同时记录到。",
        "下一代探针再翻四倍时,这条判据仍然适用,只不过缺口会更大——可测的对数随同时通道数是"
        "超线性增长的。",
    ],
)

# 17 尾卡 B
gen.tail_card(
    [
        "⁴ Manley J, et al. (2024). Simultaneous, cortex-wide dynamics of up to 1 million "
        "neurons reveal unbounded scaling of dimensionality with neuron number. "
        "Neuron 112:1694–1709.",
        "⁵ Azabou M, et al. (2025). Multi-session, multi-task neural decoding from distinct "
        "cell-types and brain regions. Int Conf Learn Represent (ICLR) 2025.",
        "⁶ Li Y, et al. (2024). Revealing unexpected complex encoding but simple decoding "
        "mechanisms in motor cortex via separating behaviorally relevant neural signals. "
        "eLife 13:e87881.",
        "⁷ Bartolo R, et al. (2020). Information-limiting correlations in large neural "
        "populations. J Neurosci 40:1668–1678.",
    ],
    os.path.join(OUT, "17-tail-b.png"),
)

print("done ->", OUT)
