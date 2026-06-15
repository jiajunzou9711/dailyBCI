import sys, os
sys.path.insert(0, ".claude/skills/dailybci/scripts")
from card_generator import CardGenerator

OUT = "output/2026-06-15-cortex-hippocampus-degeneracy"
gen = CardGenerator(date="2026.06.15", platform="xiaohongshu")

# 01 — cover
gen.cover_card(
    "学得一样好,",
    "解法却完全不同",
    "同一个“凭意念”的脑机接口任务,小鼠在运动皮层 M1 和海马 CA3 都学会了、且学得一样好——但两区的群体动力学走的是完全不同的路径。",
    os.path.join(OUT, "01-cover.png"),
    source="2026 · bioRxiv 预印本｜de Vicente、Mitelut、Mendes 等(Flavio Donato 实验室,巴塞尔大学)｜方法:实时双光子钙成像神经反馈 BCI（物种:小鼠）",
)

# 02 — the gap (hook)
gen.text_card(
    "一个没被正面回答的问题",
    [
        "我们早就知道大脑能学会“用意念”驱动脑机接口——但这件事几乎只在运动皮层研究过。",
        "于是一个根本问题悬而未决:换一个结构完全不同的脑区,它还能学会吗?是用同一套机制,还是各有各的解法?",
        "这篇把同一个 BCI 任务同时放进运动皮层(M1)和海马(CA3),正面对比,第一次给出干净的回答。",
    ],
    os.path.join(OUT, "02-gap.png"),
)

# 03 — task (Fig 1B)
gen.figure_card(
    "papers/donato-fig1loop.jpg",
    "Fig. 1B · 任务闭环",
    [
        "要回答这个问题,得先看他们怎么把“学习”搬上台:一个不靠任何动作、纯调神经活动的反馈任务。",
        "图中黑线是被选中那一小撮神经元的活动(正组−负组),它实时变成耳边的音调——越高音越高;一旦冲过阈值(紫虚线)就给水(蓝水滴)。这撮神经元本与喝水无关,小鼠纯靠试错学会主动“搓”出它。",
        "任务搭好了,真正的考验是:把它压到运动皮层和海马,谁学得会、学得怎样?",
    ],
    os.path.join(OUT, "03-task.png"),
)

# 04 — equal learning (Fig 1 C/D)
gen.figure_card(
    "papers/donato-fig1CD.jpg",
    "Fig. 1C/D · 两区学得一样好",
    [
        "答案是:两个脑区都学会了,而且学得一样好。",
        "左图命中率随训练爬升、越过随机水平(灰带),M1(蓝)与 CA3(橙)之间标注无显著差异(n.s.);右图把“高出随机多少”量化,两区相当(M1 7 只、CA3 6 只小鼠)。",
        "结果既然拉平,就能干净地追问下一步:它们是用同一种方式学会的吗?",
    ],
    os.path.join(OUT, "04-equal.png"),
)

# 05 — divergent dynamics (Fig 4H)
gen.figure_card(
    "papers/donato-fig4H.jpg",
    "Fig. 4H · 走法却不同",
    [
        "并不是——结果一样,走法却完全不同。",
        "把群体活动投影到“奖励流形”、对齐拿奖时刻(0):M1(蓝)穿过 0 后继续往上冲,是“流过”;CA3(橙)到 0 又对称退回,是“逼近—折返”。同一个奖励,两种截然不同的轨迹形状。",
        "但这还只是“看到”了差异。它从哪来——是任务逼出来的,还是脑区自己的结构决定的?",
    ],
    os.path.join(OUT, "05-dynamics.png"),
)

# 06 — causal models (Fig 5G)
gen.figure_card(
    "papers/donato-fig5G.jpg",
    "Fig. 5G · 模型给出因果",
    [
        "模型给出因果:差异来自各脑区自身的环路结构。",
        "两个 RNN 喂同样任务,只在递归结构上不同(低秩递归像 M1、对称自联想吸引子像 CA3)。图中蓝线持续走高、橙线压平,正复刻了真实数据里“流过 vs 折返”的分叉。",
        "唯一变量是架构,差异却自然涌现——于是落到一个更大的结论上。",
    ],
    os.path.join(OUT, "06-models.png"),
)

# 07 — principled degeneracy
gen.text_card(
    "原理性简并",
    [
        "这个更大的结论,作者称为 principled degeneracy:学习同一个问题,大脑没有唯一的标准解,而是每个环路用它结构所允许的方式,搓出等价但形状不同的解。",
        "以往这类“神经流形 + BCI 学习”几乎都在猴的运动皮层做;这是第一次把同一范式正面搬进架构迥异的海马。",
        "结论:“能学什么”是通用的,“怎么学成什么动力学”是各个环路自己的事。",
    ],
    os.path.join(OUT, "07-degeneracy.png"),
)

# 08 — tail
gen.tail_card(
    [
        "[1] de Vicente, Mitelut, Mendes et al., bioRxiv, 2026",
        "      (10.64898/2026.06.04.730137)",
        "",
        "[2] Sadtler et al., Nature, 2014 — 神经流形约束学习",
        "",
        "[3] Golub et al., Nat Neurosci, 2018 — 流形内学习=重配已有模式",
        "",
        "[4] Oby et al., PNAS, 2019 — 长期训练长出新模式",
    ],
    os.path.join(OUT, "08-tail.png"),
)

print("OK ->", OUT)
