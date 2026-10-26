---
title: "Weak pairwise correlations imply strongly correlated network states in a neural population"
authors: Schneidman, Berry, Segev, Bialek
year: 2006
venue: Nature 440:1007–1012
url: https://doi.org/10.1038/nature04701
subfield: population-dynamics
tags: [maximum-entropy, Ising-model, inverse-Ising, pairwise-correlation, multi-information, retina, ganglion-cells, salamander, guinea-pig, multi-electrode-array]
---

## 解决了什么问题
同时记录的神经元两两之间相关很弱，单看一对，几乎可以当作独立。问题是：把「独立」外推到整群神经元是否成立；如果不成立，描述群体放电模式的最小模型要包含哪些量。

## 核心方法
蝾螈视网膜离体多电极阵列，同时记录 40 个视网膜神经节细胞对自然电影的反应；以 Δt = 20 ms 为窗把放电二值化，每个窗内的群体状态是一个二进制词。比较三类模型对放电词分布的拟合：独立模型、只约束各细胞放电率与两两相关的二阶最大熵模型（maximum entropy model）、条件独立模型。作者指出二阶最大熵模型与 Ising 模型等价，h 为各细胞的 bias（local field），J 为两两相互作用，「没有真实温度」。用 multi-information I_N 衡量全部相关结构，用 I(2)/I_N 衡量二阶模型捕获的比例。

## 关键数据
- 大多数细胞对相关很弱，同步放电概率几乎等于各自放电概率之积；但对多数相邻细胞对，相关在统计上显著。
- 独立模型外推到 40 个细胞失败：同一窗内 K 个细胞同时放电的分布 P(K) 近似指数分布，而非独立模型给出的泊松分布；K = 10 同时放电的概率比独立模型预测大约 10⁵ 倍。
- N = 10 个细胞的子群：二阶最大熵模型捕获约 90% 的 multi-information（I(2)/I_N ≈ 90%）；换自然电影、人工电影、改变 Δt 和 N、换成豚鼠视网膜，这一比例都基本保持；培养皮层神经元网络中也有相近精度。
- 250 个 10 细胞子群中有 232 个，二阶最大熵模型优于条件独立模型，尽管后者参数多约 200 倍。

## 为什么是 milestone
把 Ising 模型作为逆问题（inverse Ising problem）引入神经数据分析：从记录到的放电统计反推 h 与 J，而不是像 Hopfield 1982 那样由人设定 J。它定量地说明，弱的两两相关足以在群体层面产生强的集体状态，此后成为群体编码中最大熵/Ising 建模的起点。引用时注意：主体数据是**蝾螈**离体视网膜、40 个细胞；约 90% 的结论在 N = 10 的子群上直接计算，N = 40 依赖扰动外推；模型不说明相关的机制来源。

## 本项目使用
series-ising-01 第一期（2026-10-25）封面图（Fig. 1a–b）与导语出处。
