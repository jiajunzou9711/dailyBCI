---
title: "A high-performance neuroprosthesis for speech decoding and avatar control"
authors: Metzger, Littlejohn, Silva, Moses, Seaton, Wang, Dougherty, Liu, Wu, Berger, Zhuravleva, Tu-Chan, Ganguly, Anumanchipalli, Chang
year: 2023
venue: Nature
url: https://doi.org/10.1038/s41586-023-06443-4
subfield: signal-processing
tags: [speech-decoding, avatar-control, multimodal-decoder, ECoG, articulatory-decoding, Chang-lab]
---

## 解决了什么问题
文字输出能恢复通信，但自然交流还包括声音、面部表情和说话节奏。语音 BCI 能否不只输出 text，而是同时驱动语音和面部 avatar，让神经解码接近多模态表达？

## 核心方法
UCSF 团队从 ECoG high-gamma 信号中解码 attempted speech，并把神经活动映射到文本、语音相关特征和面部动画控制参数。系统利用语音运动表征的结构，让同一组皮层信号支持多个输出通道。

## 关键数据
- 约 78 词/分钟
- 支持文本输出和 avatar 面部动画控制
- 使用高密度 ECoG 记录 attempted speech 相关活动
- 证明 speech BCI 可以从单一通信通道扩展到多模态表达

## 为什么是 milestone
这篇论文的重要性在于把 decoder 的目标从“打字”扩展为“表达”。从 signal-processing 角度看，它说明神经解码不必只预测一个标签序列，也可以预测一组与发音、声音和表情相关的连续/离散变量。这为更自然的人机通信界面打开了空间。
