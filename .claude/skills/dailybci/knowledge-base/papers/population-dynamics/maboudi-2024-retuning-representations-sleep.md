---
title: "Retuning of hippocampal representations during sleep"
authors: Maboudi, Giri, Miyawaki, Kemere, Diba
year: 2024
venue: Nature 629:630–638
url: https://doi.org/10.1038/s41586-024-07397-x
subfield: population-dynamics
tags: [hippocampus, CA1, place-cells, sleep, sharp-wave-ripples, BLT, bayesian-learned-tuning, preplay, representational-drift, rat]
---

## 解决了什么问题
位置野在形成后会漂移、重映射，但动物离开迷宫后无法再直接测量单个神经元的空间调谐，因此不清楚这些变化在何时、哪种脑状态下发生。本文提出在离线状态下逐细胞估计空间调谐的方法，追踪调谐在睡眠中的稳定与改变。

## 核心方法
贝叶斯学习调谐（Bayesian learned tuning, BLT / LT）：在"给定位置时各细胞 Poisson 计数条件独立"的假设下，用其余所有细胞解码出的位置后验分布，对目标细胞做动作电位触发平均，得到该细胞在任意时段（包括离线时段）的调谐曲线。与迷宫位置野求 Pearson 相关，得 LT-PF fidelity。数据：大鼠 CA1，PRE（家笼休息/睡眠）→ MAZE（新直轨取水）→ POST（长时睡眠，最长记录约 14 h），部分 session 之后再上同一轨道（reMAZE）。三套数据集：Giri（4 鼠 5 session）、Miyawaki（3 鼠 5 session）、Grosmark（4 鼠 5 session），合并分析 660 个单元。

## 关键数据
- 各离线状态中，POST 的涟漪期 LT 与迷宫位置野一致性最高；PRE 的 LT 与日后位置野**无显著一致**（PRE 稳定组 p=0.06、不稳定组 p=0.35，对照单元身份打乱）。PRE 中 replay 得分高的事件构建的 LT 同样与位置野对齐很弱。
- 按 z 分数化 LT 稳定性 >2 分组：PRE 稳定 371 / 不稳定 289；POST 稳定 454 / 不稳定 206。POST 的 LT 比 PRE 更稳定。
- POST 中 replay 得分低的涟漪事件构建的 LT 仍与位置野高度一致——不显示序列轨迹的事件也携带位置表征。
- 一致性与稳定性随 POST 睡眠推进逐渐下降，后期降到接近 PRE 水平。
- reMAZE（约 9 h POST 后，正文：2 鼠 3 session；方法部分写 4 session，两处不一致）：当 reMAZE 位置野偏离首次 MAZE 时，POST 早期 LT 预测了新位置；多元回归中 POST LT 显著、PRE LT 与 latePOST LT 不显著。
- POST LT 的来源回归：MAZE 清醒涟漪 LT 系数最大，PRE 涟漪 LT 次之，MAZE theta LT 与 MAZE 位置野亦显著。

## 为什么是 milestone
提供了在离线状态下逐细胞读出空间调谐的工具（BLT），使"睡眠中表征被重调"成为可测的单细胞量：睡眠早期涟漪既稳定迷宫表征、也提前出现日后的位置野改变。对 preplay 一线给出限制性结果：在本文数据中 PRE 的 LT 整体不对齐日后位置野，作者认为离线解码出的连续轨迹可能部分为伪迹；但 PRE 的配置对 POST 表征仍有贡献（回归系数第二大）。Ren 2026 正是用 BLT 报告骨干细胞在首次上轨前的 H0 期 fidelity 中位数 0.23，与本文 PRE 结果在细胞子集层面存在差异，比较时需注意两者细胞分类与数据集不同。
