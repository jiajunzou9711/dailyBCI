# -*- coding: utf-8 -*-
"""series-ising-01 · 第一期 Ising 模型是什么 —— 卡片生成"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from card_generator import CardGenerator

PROJ = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", ".."))
OUT = os.path.join(PROJ, "output", "series-ising-01", "ep01")
FIG = os.path.join(OUT, "figs")
def f(n): return os.path.join(FIG, n + ".png")
def o(n): return os.path.join(OUT, n)

gen = CardGenerator(date="2026.10.25")

gen.cover_card(
    "Ising 模型",
    "从铁磁到神经元",
    "同时记录几十个神经元时，描述它们共同放电的常用模型之一，来自一百多年前对铁磁性的研究。本期讲清这个模型由什么组成，以及它为什么能用在神经数据上。",
    o("01-cover.png"),
    concept_image=os.path.join(PROJ, "papers", "series-ising", "schneidman-2006-fig1ab-cover.png"),
    concept_height=600, title_size=92, title_top=40, subtitle_size=30,
    image_caption="Schneidman E, et al. (2006). Weak pairwise correlations imply strongly correlated\nnetwork states in a neural population. Nature 440:1007–1012, Fig. 1a–b.",
)

gen.figure_card(
    f("toc"), "本期路线",
    ["同时记录许多神经元时，我们关心的往往是它们怎样一起放电。2006 年，Schneidman 等人在蝾螈视网膜上同时记录了 40 个神经节细胞，发现只刻画两两相关的模型，就能定量描述这群神经元的集体放电。这类模型称为最大熵模型（maximum entropy model），它与 Ising 模型等价¹。在理论方面，Hopfield 网络这类记忆模型，也与 Ising 模型同构²。因此，读群体编码或记忆网络的文献时，常会遇到这个模型。",
     "来源：本篇只讲原理，不针对某一篇具体论文做解读。本篇主要参考的文献如下：Schneidman 2006、Hopfield 1982、Lenz 1920、Ising 1925、Onsager 1944。"],
    o("02-toc.png"), figure_height=520,
)

C = [
 dict(n="①", t="Ising 模型为解释铁磁相变而提出", fig="fig01-lattice", lab="图 1", fh=385, out="03-c1.png", a=[
   "铁在居里温度（Curie temperature）以下会自发带上磁性；温度一升过这个点，磁性突然消失。性质在某个温度突然改变，称为相变（phase transition）。物理学家要回答：每个原子磁矩只和身边的原子相互作用，为什么能整体排齐，又为什么会在同一个温度突然失序？",
   "1920 年，Lenz 给出了一个尽量简化的模型³，交给学生 Ising 求解⁴。上图对应它的前两条前提：",
   "· 每个格点取 +1（↑）或 −1（↓），所有格点的取值合起来，称为一种排列 σ；\n· 只有相邻格点之间有相互作用，取值相同时能量更低。",
   "第三条前提规定怎样由能量得到概率，下一张展开。"]),
 dict(n="①", t="排列决定能量，能量决定概率", fig="fig02-three-sites", lab="图 2", fh=330, out="04-c2.png", a=[
   "能量的算法来自第二条前提。每一对相邻格点贡献一项 −J σ_{i}σ_{j}：两者取值相同时，乘积 σ_{i}σ_{j} = +1，这一项为 −J；取值不同时，乘积为 −1，这一项为 +J。把所有相邻格点对的贡献加起来，就是系统在排列 σ 下的能量：**E(σ) = −J Σ σ_{i}σ_{j}**³⁴。J 是相互作用的强度。",
   "第三条前提规定：温度为 T 时，系统处在 σ 的概率为 **P(σ) = exp(−E(σ)/kT) / Z**，这称为玻尔兹曼分布（Boltzmann distribution）。Z 是所有排列的 exp(·) 之和，称为配分函数（partition function），它保证所有概率加起来等于 1。",
   "· 「+ + +」两对都相同，能量为 −2J，最低；\n· 「+ − +」两对都不同，能量为 +2J，最高。",
   "能量越低的排列，出现的概率越高。给定 J 和 T，每种排列的能量和概率就都唯一确定了。"]),
 dict(n="②", t="一维没有相变，二维有", fig="fig03-low-high", lab="图 3", fh=365, out="05-c3.png", a=[
   "温度决定能量差对概率的影响有多大。如上图，低温下，概率集中在能量最低的有序排列，大片格点取值相同；高温下，各种排列的概率接近，取值杂乱。",
   "这个模型要检验的是：只靠局部相互作用加上热扰动，能否产生相变。这里的「求解」是正向计算：给定 J 和 T，算出平均磁化，即所有格点取值的平均，看它在格点数趋于无穷时，是否会在某个温度突然从非零变为零。",
   "维数指格点怎样排列。一维是格点排成一条链，每个格点只有左右两个邻居；二维是格点铺成平面方格，像上图那样，每个格点有上下左右四个邻居。Ising 在 1924 年的博士论文里解出了一维链：一维没有相变⁴。Onsager 在 1944 年解出了二维方格：二维存在相变⁵。由此，**这三条最简单的前提，在二维中足以产生宏观相变。**"]),
 dict(n="③", t="同一个模型，可以正着用，也可以反过来用", fig="fig04-forward-inverse", lab="图 4", fh=340, out="06-c4.png", a=[
   "如上表，同一个模型有两种用法：",
   "· **正问题**：J 和 T 已知，求各种排列的概率和宏观行为。物理就是这样用的，比如计算平均磁化怎样随温度变化。神经科学里构建记忆网络时，J 由人设定，也属于这一类。\n· **逆问题**（inverse Ising problem）：已知记录到的放电数据，反推参数，也就是每对神经元之间的 J，以及每个神经元自身的 h。h 表示神经元本身偏向放电还是偏向不放电，对应物理里的外加磁场。",
   "逆问题之所以可行，是因为第三条前提可以反过来读：出现得越频繁的排列，能量越低。因此在逆问题里，「能量」是由概率定义的统计量，与神经元消耗的代谢能量无关，通常直接取 kT = 1。"]),
 dict(n="④", t="Ising 模型沿两条线进入神经科学", fig="fig05-two-lines", lab="图 5", fh=400, out="07-c5.png", a=[
   "按 J 从哪里来，神经科学里用到 Ising 模型的工作可以分成两条线，如上图：",
   "· **第一条线**：把它用作神经网络的动力学与记忆模型。J 由人设定，属于正问题，代表工作是 Hopfield 1982 年提出的记忆网络²。\n· **第二条线**：把它用作神经数据的统计描述。J 从记录到的数据中估计，属于逆问题，导语提到的 Schneidman 2006 属于这一条¹。",
   "下一期先讲第一条线：Ising 模型怎样用来回答「由简单神经元组成的网络，能否存储并提取记忆」。"]),
]

for c in C:
    gen.figure_card(f(c["fig"]), c["lab"], c["a"], o(c["out"]),
                    figure_height=c["fh"], title=c["t"], title_num=c["n"])

gen.tail_card([
  "1. Schneidman E, et al. (2006). Weak pairwise correlations imply strongly correlated network states in a neural population. Nature 440:1007–1012.",
  "2. Hopfield JJ. (1982). Neural networks and physical systems with emergent collective computational abilities. Proceedings of the National Academy of Sciences USA 79:2554–2558.",
  "3. Lenz W. (1920). Beitrag zum Verständnis der magnetischen Erscheinungen in festen Körpern. Physikalische Zeitschrift 21:613–615.",
  "4. Ising E. (1925). Beitrag zur Theorie des Ferromagnetismus. Zeitschrift für Physik 31:253–258.",
  "5. Onsager L. (1944). Crystal statistics. I. A two-dimensional model with an order-disorder transition. Physical Review 65:117–149.",
  "",
  "图 3 为自制模拟：48 × 48 方格，J = 1，Metropolis 更新。二维方格的相变温度为 kT ≈ 2.27 J⁵，低温与高温两幅分别取在它的两侧。",
], o("08-tail.png"), lead_paragraphs=[
  "至此，Ising 模型本身已经交代清楚：三条前提给出了每种排列的概率；只靠局部相互作用，二维格点就能出现相变；同一个模型既可以由参数求行为，也可以由数据求参数。",
  "下一期从第一条线讲起：阈值神经元、Hebb 规则与 Hopfield 网络。",
])
print("done")
