---
title: "EEG-based detection of the locus of auditory attention with convolutional neural networks"
authors: Vandecappelle, Deckers, Das, Ansari, Bertrand, Francart
year: 2021
venue: eLife
url: https://doi.org/10.7554/eLife.56481
subfield: non-invasive
tags: [auditory-attention, EEG, CNN, spatial-attention, short-window, directional]
---

## 解决了什么问题
基于刺激包络重建的 AAD 需要较长决策窗（数十秒）才够准，太慢，跟不上注意的实时切换；而且它只判断"哪一路语音"，不直接给空间方位。助听器需要的是秒级的快速判断。

## 核心方法
人类 EEG，用卷积神经网络（CNN）从短决策窗（约 1–2 s）直接解码听觉注意的**空间方位 / locus**（如左 vs 右），不依赖刺激语音包络，转为一个空间分类问题。

## 关键数据
- 在 1–2 秒的短窗上以高于线性 stimulus-reconstruction 方法的准确率解码注意方向。
- 用极短决策窗换取实用的快速响应，缓解了"准确率—窗长"的固有权衡。

## 为什么是 milestone
标志 AAD 从慢速的 stimulus-reconstruction 转向**快速空间/方向解码**，并开启短窗深度学习 AAD 的范式（后续大量 CNN/Transformer 短窗模型如 FAConformer 等沿此路线展开）。承自 [[osullivan-2015-single-trial-eeg-aad]]。
