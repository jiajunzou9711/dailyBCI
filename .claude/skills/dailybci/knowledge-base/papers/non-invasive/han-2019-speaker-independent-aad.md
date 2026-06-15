---
title: "Speaker-independent auditory attention decoding without access to clean speech sources"
authors: Han, O'Sullivan, Luo, Herrero, Mehta, Mesgarani
year: 2019
venue: Science Advances
url: https://doi.org/10.1126/sciadv.aav6134
subfield: non-invasive
tags: [auditory-attention, deep-learning, speech-separation, speaker-independent, iEEG, cocktail-party]
---

## 解决了什么问题
此前 AAD 多假设能拿到各说话者的 clean source（干净音轨）来与神经重建比对，但现实里只有麦克风录到的混合信号；而且换一个没见过的说话者往往要重训。这两点是 AAD 走向真实世界的主要障碍。

## 核心方法
实时深度学习单通道 speaker separation（Mesgarani 组的 TasNet 系）先把混合分离成各路语音，再把每路与从听觉皮层响应重建的频谱图比对，选相关最高者作为被注意说话者并放大。关键在**说话者无关**——可泛化到训练中未见过的说话者。该研究使用人类 iEEG（侵入式皮层记录）。

## 关键数据
- 无需访问 clean source 即可完成 AAD（只用麦克风混合信号）。
- 系统可泛化到未见过的说话者，使用户更容易与新的人交流。

## 为什么是 milestone
把 AAD 从受控实验室条件推向真实世界可行：无干净源 + 说话者无关。是深度学习语音分离与神经注意解码结合的代表作，定义了"端到端 neuro-steered 听觉增强"的现代形态。承自 [[osullivan-2015-single-trial-eeg-aad]]，与工程化提取路线 [[vaneyndhoven-2017-eeg-informed-speaker-extraction]] 互补。
