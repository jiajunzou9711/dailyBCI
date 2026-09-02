---
title: "The origins and prevalence of texture bias in convolutional neural networks"
authors: Hermann, Chen, Kornblith
year: 2020
venue: NeurIPS 33:19000–19015
url: https://proceedings.neurips.cc/paper/2020/hash/db5f9f42a7157abe65bb145000b5871a-Abstract.html
subfield: brain-encoding-models
tags: [texture-bias, shape-bias, CNN, data-augmentation, cue-conflict, human-behavior]
---

## 解决了什么问题
[[loke-2026-texture-alignment]] 讨论「人的行为是形状偏好、模型却偏纹理」这个张力时，引的人类行为形状偏好出处就是本文。本文问的是：ImageNet 训练的 CNN 为什么会偏纹理，这个偏向来自架构、目标函数，还是训练数据的处理方式。

## 核心方法
在 cue-conflict 刺激（形状与纹理来自不同类别）上系统比较架构、目标函数与数据增广的影响，并与人类被试的判断作对照。

## 关键数据
- 报告纹理偏向的主因落在**数据增广与预处理**一侧，而非架构或目标函数本身；改变裁剪/颜色扰动等增广即可显著移动形状—纹理偏向。
- 人类在同一 cue-conflict 范式下表现出形状偏好，构成模型—人类的行为差距基准。

## 为什么是 milestone
把「CNN 偏纹理」从一个现象推进到可归因的实验问题，是 [[conwell-2024-inductive-biases-brain-predictivity]] 那条「训练用的图比架构更要紧」的近亲结论。
**⚠ 强度边界**：cue-conflict 范式本身已被 Burgert et al. (2025, NeurIPS Oral, arXiv:2509.20234) 质疑存在混淆，该文结论为 ImageNet 训练的 CNN 主要依赖局部形状。引用「CNN 有纹理偏向」时须注明这是 cue-conflict 范式下的报告，不作为已确立事实。
