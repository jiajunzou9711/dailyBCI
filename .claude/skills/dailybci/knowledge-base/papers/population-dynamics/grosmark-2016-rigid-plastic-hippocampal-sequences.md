---
title: "Diversity in neural firing dynamics supports both rigid and learned hippocampal sequences"
authors: Grosmark, Buzsáki
year: 2016
venue: Science 351:1440–1443
url: https://doi.org/10.1126/science.aad1935
subfield: population-dynamics
tags: [hippocampus, CA1, place-cells, replay, preplay, rigid-plastic, firing-rate, sharp-wave-ripples, rat]
---

## 解决了什么问题
replay 通常被当作同质神经元群体的现象来研究，但 preplay 提示序列可能部分来自经验前已存在的动力学。本文在单细胞层面区分：新环境中形成的序列，哪些成分在经验前后保持不变，哪些成分由经验改变。

## 核心方法
4 只大鼠，CA1 锥体细胞单单元同步记录；8 个新环境探索 session（直轨或环形轨），前后各有家笼睡眠（PRE / POST）。用跑动期 491 个位置细胞建立贝叶斯位置解码器，解码 PRE、MAZE、POST 的候选涟漪事件，以加权相关的 z 分数作序列得分。用细胞特异打乱定义每个细胞对序列的贡献（per cell contribution, PCC）；对序列贡献显著的细胞按 PRE→POST 贡献变化（ΔPCC）的 session 中位数分为 rigid（低于中位数）与 plastic（高于中位数）。

## 关键数据
- 216 个细胞对 PRE 或 POST 序列贡献显著；其中贡献 PRE 序列的细胞 73% 也贡献 POST 序列。
- 打乱或剔除 ΔPCC 最高的 10–20% 细胞，POST>PRE 的 replay 增量消失；剔除最低的 75% 后仍保留。
- plastic 细胞：位置特异性更高、位置野更少，且在跑动中特异性持续上升；rigid 细胞特异性不随学习上升。
- rigid 细胞 session 整体发放率更高；plastic 细胞的涟漪相关放电、burst 与成对共激活更高。PRE 睡眠中共激活以快发放细胞为主且延续到 POST；慢发放细胞 PRE→POST 共激活增幅最大。
- 按离线发放率二分：低发放组中位数 0.39 Hz、高发放组 1.12 Hz；低发放组每个动作电位携带的空间信息更多，PRE→POST 对序列的贡献上升，高发放组不上升。
- 作者强调快、慢发放细胞在发放率上构成连续分布，不是离散两类。

## 为什么是 milestone
把"预先配置"与"经验可塑"从网络层面的二选一，变为同一网络内不同细胞的分工：以快发放、低空间特异性的 rigid 细胞为既有骨架，慢发放的 plastic 细胞在经验中加入并获得高空间特异性。这是后续"骨干细胞 + 经验依赖细胞"类工作（如 Ren 2026）的直接比较基准。数据公开于 CRCNS，并被 Maboudi 2024 作为三套数据集之一复用。引用时注意：rigid/plastic 是按中位数切分的相对标签；动物在 PRE 之前是否有其他轨道经验，需查补充材料，本条目未核。
