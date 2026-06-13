---
title: "Long-term stability of cortical population dynamics underlying consistent behavior"
authors: Gallego, Perich, Chowdhury, Solla, Miller
year: 2020
venue: Nature Neuroscience (23:260–270)
url: https://www.nature.com/articles/s41593-019-0555-4
subfield: population-dynamics
tags: [neural-manifold, latent-dynamics, long-term-stability, decoder-stability, macaque, motor-cortex]
---

## 解决了什么问题
BCI 长期可用的最大障碍之一是**记录到的单个神经元在不断变化**（电极漂移、细胞换批），导致基于单神经元的解码器随时间退化。是否存在一个更稳定的层次，能跨月、跨年支撑一致的行为？

## 核心方法
在恒河猴前运动、初级运动与体感皮层长期记录（reaching 任务，最长约 **2 年**），尽管记录到的神经元稳定换批，提取群体活动的**低维潜在动力学（latent dynamics）**，检验其跨时间的稳定性，并用稳定的潜在动力学构建跨时间一致的解码。

## 关键数据
- 在长达 **~2 年** 的时间里，尽管单个记录神经元持续变化，**低维潜在动力学保持稳定**。
- 基于稳定 latent dynamics 的解码可在不同日期间保持一致，无需依赖追踪同一批神经元。

## 为什么是 milestone
证明"流形/潜在动力学"是比单神经元更**长期稳定**的层次，为 BCI 跨日跨月免重校准提供了群体动力学依据。与 [[gallego-2017-neural-manifolds-movement]] 的框架、[[sadtler-2014-neural-constraints-learning]] 的学习约束互补：流形既约束学习，又提供长期稳定的底座。和知识库中 [[chestek-2011-long-term-signal-stability]]、[[flint-2013-lfp-long-term-bmi]] 一起构成"BCI 长期稳定性"的多层证据。
