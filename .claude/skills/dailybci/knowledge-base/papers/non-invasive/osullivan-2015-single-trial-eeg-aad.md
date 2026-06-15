---
title: "Attentional Selection in a Cocktail Party Environment Can Be Decoded from Single-Trial EEG"
authors: O'Sullivan, Power, Mesgarani, Rajaram, Foxe, Shinn-Cunningham, Slaney, Shamma, Lalor
year: 2015
venue: Cerebral Cortex
url: https://doi.org/10.1093/cercor/bht355
subfield: non-invasive
tags: [auditory-attention, EEG, stimulus-reconstruction, single-trial, cocktail-party]
---

## 解决了什么问题
此前 stimulus-reconstruction（从神经活动重建语音包络以判断注意）主要在昂贵的 ECoG / MEG 上验证。问题是：廉价、普及的头皮 EEG 能否单试次解码听觉注意？这决定了 AAD 能否走向消费级硬件。

## 核心方法
人类 EEG，两说话者竞争。训练一个 linear backward（decoder）模型，从多通道 EEG 重建被注意语音的时间包络，再比较重建包络与两路说话者各自包络的相关，相关高者即判为被注意对象。

## 关键数据
- 用单试次 EEG 即可显著高于随机地判断注意对象。
- 解码准确率随决策窗长增加而提升（长窗如约 60 s 最准；短至约 6 s 仍可用），揭示 AAD 的核心权衡：准确率 vs 决策速度。

## 为什么是 milestone
把 stimulus-reconstruction 从昂贵记录搬到头皮 EEG，是整条 EEG-AAD 路线的奠基石。其 linear decoder 成为后续几乎所有 AAD 工作的标准基线，也定义了"准确率—窗长"这一贯穿全领域的权衡。承自 [[mesgarani-2012-attended-speaker-cortical]] / [[ding-2012-auditory-object-encoding]]，下游催生 [[vandecappelle-2021-cnn-locus-attention]] 的短窗深度学习路线。
