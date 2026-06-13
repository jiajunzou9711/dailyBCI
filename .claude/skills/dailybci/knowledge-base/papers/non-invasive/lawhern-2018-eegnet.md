---
title: "EEGNet: a compact convolutional neural network for EEG-based brain-computer interfaces"
authors: Lawhern, Solon, Waytowich, Gordon, Hung, Lance
year: 2018
venue: Journal of Neural Engineering
url: https://doi.org/10.1088/1741-2552/aace8c
subfield: non-invasive
tags: [deep-learning, CNN, EEGNet, cross-paradigm, transfer-learning, Army-Research-Lab]
---

## 解决了什么问题
EEG-BCI 的传统方法（CSP、LDA 等）对每个范式需要定制不同的特征提取管道，且通常需要大量训练数据。能否设计一个通用的深度学习模型，用同一个架构处理不同类型的 EEG-BCI 任务？

## 核心方法
设计了 EEGNet——一个紧凑的卷积神经网络，使用 depthwise separable convolution 来编码 EEG 信号的时间和空间特征。关键设计：（1）temporal convolution 捕获时间动态；（2）depthwise convolution 学习空间滤波（类似 CSP）；（3）separable convolution 组合特征。参数量极小，适合小样本 EEG 数据。

## 关键数据
- 在 4 种 BCI 范式上测试：P300、ERN、MRCP、SMR
- 同一架构跨范式泛化，优于或持平于各范式的专用算法
- 在训练数据有限时优势尤为明显
- 可解释性：学到的空间滤波器与已知的 EEG 特征一致

## 为什么是 milestone
第一个成功跨 BCI 范式通用的深度学习模型。EEGNet 成为 EEG 深度学习研究的标准基线，几乎所有后续的 EEG-CNN 论文都以 EEGNet 为对比对象。证明了深度学习可以自动学习传统手工特征工程的功能（如空间滤波、频带选择）。
