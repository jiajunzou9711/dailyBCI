---
title: "Encoding and decoding in fMRI"
authors: Naselaris, Kay, Nishimoto, Gallant
year: 2011
venue: NeuroImage 56:400–410
url: https://doi.org/10.1016/j.neuroimage.2010.07.073
subfield: brain-encoding-models
tags: [encoding-model, decoding, fMRI, review, milestone-source]
---

## 解决了什么问题
2010 年前后，fMRI 领域的"多体素模式分析"迅速流行，但解码（从脑活动读出刺激/心理状态）与编码（从刺激预测脑活动）两类模型的关系一直含混，很多工作把解码准确率当成对表征的直接证据。这篇综述把两者放进同一个形式框架里，说清各自能回答什么问题。

## 核心方法
把两类模型都写成"刺激空间 → 特征空间 → 体素响应"的三段结构：编码模型学"特征→响应"的前向映射，解码模型学反向映射。综述指出，编码模型指定了一个完整的前向生成过程，因此原则上可以由它推出最优解码器；反过来，一个解码器并不唯一确定编码模型。作者据此主张编码模型是更一般、可证伪性更强的那一类。

## 关键数据
- 综述性文献，不报告新实验数据。
- 提出的方法学要点：特征空间的选择（而非回归器的选择）是编码模型的主要科学承载；模型必须在**留出的、训练中未出现过的**刺激上评估；identification（在大候选集中指认看的是哪一个）比分类更严格。

## 为什么是 milestone
本子领域的**milestone 抽取源**，也是"编码模型"这一提法在人类神经影像中的标准参考。它确立的评价准则（留出刺激泛化、大候选集 identification、特征空间即假设）此后被视觉、语言、语音编码模型普遍沿用。与 [[kay-2008-identifying-natural-images]] 同组，是那条路线的方法学总结。
