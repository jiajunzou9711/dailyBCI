# -*- coding: utf-8 -*-
"""日报 2026-08-26「语言的神经群体编码」第六期：16 张图卡。"""
import os, sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(SCRIPT_DIR))
from card_generator import CardGenerator

SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-08-26-langcode-06")
FIGS = os.path.join(OUT, "figs")
PAPERS = os.path.join(PROJECT, "papers")
os.makedirs(OUT, exist_ok=True)
P = lambda *a: os.path.join(*a)
SELF = "自制示意图"
NS = "Nastase et al. 2026, Neuron, Fig. 3"
ZD = "Zada et al. 2025, arXiv:2506.20489"

gen = CardGenerator(date="2026.08.26")

# ---------- 01 封面 ----------
gen.cover_card(
    "人能和 AI 对话",
    "靠的是同一件事",
    "两个人对上的是表征几何——词与词之间的相对结构。",
    P(OUT, "01-cover.png"),
    concept_image=P(PAPERS, "ns-fig3-full.png"),
    concept_height=420,
    concept_bleed=100,
    title_size=74,
    title_top=170,
    source=NS,
)

# ---------- 02 目录 ----------
gen.figure_card(
    P(FIGS, "toc.png"), "本期路线",
    ["本期是 Neuron 观点文章《Unifying the structures of language in a neural population code》"
     "多期连载的第六期，讲该文**原理二的第二个案例**：多个神经系统如何收敛到一套共享的表征几何。",
     "承重实证有三项：Zada 等 2025 年的三语 fMRI 工作（arXiv 预印本）、"
     "Zada 等 2024 年发表于 Neuron 的双人颅内工作、"
     "Zada 等 2026 年发表于 Neuron 的 fMRI 超扫描工作。"],
    P(OUT, "02-toc.png"), figure_height=600, annot_size=27,
)

# ---------- 03 ① ----------
gen.text_card(
    "① 一件日常到不必解释的事",
    ["两个人说同一种语言，就能听懂对方。这件事日常到不需要理由。",
     "把它放到神经层面，问题立刻变了样：**你脑中关于 queen 的活动，和我脑中关于 queen 的活动，"
     "凭什么是同一回事？**",
     "这一期讲这个问题的答案，以及三项实验是怎么把它测出来的。"],
    P(OUT, "03-card1.png"),
)

# ---------- 04 ② 嵌入 ----------
gen.figure_card(
    P(FIGS, "fig-embedding.png"), SELF,
    ["模型处理词的第一步是把词变成数。one-hot 的做法是每个词一个 5 万维向量，只有一位是 1。"
     "**这种编码里任意两个词的距离都相等**——queen 到 king，等于 queen 到 refrigerator。",
     "嵌入把它压到几百到几千维的稠密向量，每一维是实数，压缩方式由训练决定。训练目标是预测下一个词，"
     "用法相近的词落在相近位置才预测得准。",
     "**原文提醒这个平行四边形是为画图做的极度简化**：真实嵌入随语境变化。"],
    P(OUT, "04-card2.png"), figure_height=500,
    title="嵌入是什么", title_num="②",
)

# ---------- 05 ③ ----------
gen.text_card(
    "③ 对齐发生在表征几何这一层",
    ["两个人之间有一个硬事实：**没有神经元到神经元的对应。**就算能把我的脑活动原样传给你，"
     "也没有办法把它映射到你那套独特的神经元配置上。",
     "哪个神经元调谐到什么，由发育、经历和随机性共同决定。我的第 1000 号神经元和你的第 1000 号之间，"
     "不存在任何约定。",
     "能对上的是**相对关系**：king 与 queen 之间的差、man 与 woman 之间的差，在各自空间里方向一致。"
     "这套不依赖神经元编号的结构，就是**表征几何**。",
     "〔Haxby, Guntupalli, Nastase & Feilong 2020, eLife 9:e56601〕"],
    P(OUT, "05-card3.png"),
)

# ---------- 06 ④ ----------
gen.text_card(
    "④ 把这个断言变成能做的实验",
    ["如果对齐发生在几何这一层，那么语音、文字、语法这些表层形式应当不参与。",
     "于是有了一个可操作的问题：**怎么把表层形式彻底剥掉，只留下内容？**",
     "一个直接的手段是**换语言**。同一个故事，用三种语言讲给三组母语者听。"
     "三个版本的音、字、语法完全不同，共同剩下的只有内容。"],
    P(OUT, "06-card4.png"),
)

# ---------- 07 ⑤ ----------
gen.figure_card(
    P(PAPERS, "zd-fig2A.png"), ZD + ", Fig. 2A",
    ["公开数据集 Le Petit Prince fMRI Corpus：同一本《小王子》有声书的三个语言版本——"
     "英语 94 分钟 15,375 词，汉语 99 分钟 16,008 词，法语 97 分钟 15,390 词，按句子对齐共 1,650 句。",
     "三组母语者各听各的版本：英 49 人、汉 35 人、法 28 人，共 112 人。",
     "词嵌入取自三个**只在单一语言上训练**的 BERT，各用各的语言。"],
    P(OUT, "07-card5.png"), figure_height=470,
    title="同一本《小王子》，三种语言", title_num="⑤",
)

# ---------- 08 ⑥ ----------
gen.figure_card(
    P(PAPERS, "zd-fig2CD.png"), ZD + ", Fig. 2C–D",
    ["**训练**：用英语嵌入预测英语被试的 BOLD，8 个 run 拟合出权重。",
     "**检验**：把权重原样搬过来，在留出的第 9 个 run 上生成**预测的脑活动序列**。"
     "这条序列既拿去对英语被试（语言内），也拿去对汉语和法语被试（跨语言）。"
     "**英语模型全程没有见过法语或汉语的嵌入。**",
     "三个版本里词出现的时刻各不相同，所以比较前把预测与实际都按句子降采样——"
     "句子是三者唯一的共同时间轴。"],
    P(OUT, "08-card6.png"), figure_height=330,
    title="迁移的是预测出来的脑活动", title_num="⑥",
)

# ---------- 09 ⑦ ----------
gen.figure_card(
    P(PAPERS, "zd-fig3BC.png"), ZD + ", Fig. 3B–C",
    ["左：语言内编码成绩。右：跨语言编码成绩。两张未阈值化全脑图的相关 **r = 0.974**。",
     "跨语言整体略低，显著低的位置集中在**早期听觉皮层与颞上回**——正是处理各语言特有语音的地方。",
     "**两个方向指向同一个结论**：能跨语言迁移的部分与表层形式无关，掉下去的部分正是表层形式所在。"],
    P(OUT, "09-card7.png"), figure_height=470,
    title="跨语言的成绩图，和语言内几乎一样", title_num="⑦",
)

# ---------- 10 ⑧ ----------
gen.figure_card(
    P(PAPERS, "zd-fig3A.png"), ZD + ", Fig. 3A",
    ["三个 BERT 架构相同、参数量相近，差别只在训练语料。它们的嵌入空间朝向是任意的，"
     "所以用**仅含旋转**的变换去对齐：旋转保持内部的距离与夹角，能不能转上就是结构是否相同的检验。"
     "一半句子（825 句）学旋转，另一半检验。",
     "相似度沿层加深上升：第 1 层 r = 0.054，中晚层最高 0.154，最后一层回落到 0.116，全层平均 0.115。"
     "英–法高于英–汉与法–汉。",
     "**绝对值不高**：共享结构确实存在，但只占一部分。"],
    P(OUT, "10-card8.png"), figure_height=470,
    title="三个单语模型之间也有共享结构", title_num="⑧",
)

# ---------- 11 ⑨ ----------
gen.figure_card(
    P(FIGS, "fig-timing.png"), SELF,
    ["前面所有实验里被试都在**被动听**录好的材料，说话人这一侧不存在。语言的基本形态是对话。",
     "Zada 等 2024：两个癫痫病人同时植入颅内电极，面对面自由对话，两边同步记录。"
     "同一段对话的 GPT-2 嵌入同时预测两个人的活动。",
     "结果：内容**先在说者脑中出现**（发音之前），随后**在听者脑中重现**（词起始之后），逐词如此。",
     "这条时间顺序排除了一个替代解释：若两人只是被同一个声音同时驱动，两条曲线应当同步。"],
    P(OUT, "11-card9.png"), figure_height=350,
    title="换成真实对话，看内容怎么传过去", title_num="⑨",
)

# ---------- 12 ⑩ ----------
gen.text_card(
    "⑩ 共享的是声音、词，还是内容",
    ["同一句话「她就是那个 queen」，四种特征给出四种编码：**发音特征**只区分声音；"
     "**词汇特征**只区分是哪个词；**句法特征**只区分结构位置；**上下文嵌入**随语境变化。",
     "「英国的 queen」与「Freddie Mercury 的 Queen」，前三种给出的编码几乎相同，"
     "只有上下文嵌入把两者放在空间里不同的位置。",
     "实测：捕捉说者—听者共享成分最好的是上下文嵌入。**共享的是语境化的内容。**",
     "跨语言那项用换语言把表层剥掉，这一项用特征对照把表层筛掉。两条路指向同一结论。"],
    P(OUT, "12-card10.png"),
)

# ---------- 13 ⑪ ----------
gen.text_card(
    "⑪ 对齐最强的地方在社会认知区域",
    ["颅内电极装在哪由癫痫灶位置决定，做不出全脑图谱。换 fMRI：全脑覆盖，"
     "代价是时间分辨率降到秒级。",
     "Zada 等 2026：30 对被试（N = 60）同步 fMRI 实时对话。用 A **说话时**的数据训练编码模型，"
     "不重新训练，直接拿去预测 B **听的时候**的活动。",
     "显著耦合出现在右侧 pSTG 并延伸进 **TPJ**、MFG，以及双侧楔前叶/后内侧皮层；"
     "**右半球强于左半球**，与语言加工通常的左侧优势相反。多数区域对的峰值在 lag 0 ± 3 秒。",
     "作者解读：真实对话要求双方持续推测对方的想法和意图，这会调动社会脑。"],
    P(OUT, "13-card11.png"),
)

# ---------- 14 ⑫ ----------
gen.figure_card(
    P(PAPERS, "ns-fig3-full.png"), NS + "（与封面同图）",
    ["看图右侧上下两个坐标系：上为人脑的神经元坐标，下为 LLM 的单元坐标。**轴不同，四个词的相对位置关系相同。**",
     "**跨语言 · 模型侧**：LLM 是**被观测对象**。三个单语 BERT 彼此有部分共享几何。",
     "**跨语言 · 大脑侧**：LLM 是**测量工具**。嵌入是编码模型的自变量。",
     "**双人对话**：LLM 是**中介**。路径是「A 的活动 ← 嵌入 → B 的活动」。"
     "嵌入空间的几何若与两个脑子都不相容，这条路径根本传不过去。"],
    P(OUT, "14-card12.png"), figure_height=400,
    title="LLM 在三项证据里扮演三个角色", title_num="⑫",
)

# ---------- 15 ⑬ ----------
gen.text_card(
    "⑬ 落点与强度边界",
    ["**相互理解只需要表征几何足够接近，不需要神经元层面的对应。**够到什么程度算够——"
     "够到一个架构完全不同的系统也能进来对话。",
     "**边界一**：跨语言那项是 arXiv 预印本，未经同行评议，且作者即本文作者。",
     "**边界二**：三组听的是同一个故事，共享的是这一个故事的内容。",
     "**边界三**：「几何相似」在两处都是间接推出的——读到的量是编码成绩与嵌入相关，"
     "不是对两个几何的直接测量。",
     "**边界四**：原文自己指出，光靠预测下一个词不足以产生对话能力，"
     "现在的对话模型还需要大量对话数据和人类反馈。**「几何相容」与「会对话」是两件事。**"],
    P(OUT, "15-card13.png"),
)

# ---------- 16 尾卡 ----------
gen.tail_card(
    [
        "Nastase SA, Zada Z, Goldberg AE, Hasson U. (2026). Unifying the structures of language "
        "in a neural population code. Neuron 114. doi:10.1016/j.neuron.2026.07.024",
        "",
        "Zada Z, Nastase SA, Li J, Hasson U. (2025). Brains and language models converge on a "
        "shared conceptual space across different languages. arXiv:2506.20489",
        "Zada Z, Goldstein A, Michelmann S, et al. (2024). A shared model-based linguistic space "
        "for transmitting our thoughts from brain to brain in natural conversations. Neuron 112.",
        "Zada Z, Nastase SA, Speer S, et al. (2026). Linguistic coupling between neural systems "
        "for speech production and comprehension during real-time dyadic conversations. "
        "Neuron 114:774.",
        "Haxby JV, Guntupalli JS, Nastase SA, Feilong M. (2020). Hyperalignment: modeling shared "
        "information encoded in idiosyncratic cortical topographies. eLife 9:e56601.",
        "Li J, Bhattasali S, Zhang S, et al. (2022). Le Petit Prince multilingual naturalistic "
        "fMRI corpus. Scientific Data 9:530.",
    ],
    P(OUT, "16-tail.png"),
    lead_paragraphs=["**下期预告**：作者自列的差距——人工神经网络与生物神经网络之间，哪些地方对不上。"],
)

print("done")
