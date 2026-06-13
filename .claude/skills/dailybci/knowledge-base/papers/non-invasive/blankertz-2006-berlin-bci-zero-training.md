---
title: "The Berlin Brain-Computer Interface: EEG-based communication without subject training"
authors: Blankertz, Dornhege, Krauledat, Muller, Kunzmann, Losch, Curio
year: 2006
venue: IEEE Transactions on Neural Systems and Rehabilitation Engineering
url: https://doi.org/10.1109/TNSRE.2006.875557
subfield: non-invasive
tags: [Berlin-BCI, zero-training, machine-learning, CSP, motor-imagery, BBCI]
---

## 解决了什么问题
传统 motor imagery BCI 需要用户经过数周甚至数月的训练才能使用（如 Pfurtscheller 的 Graz-BCI）。这严重限制了 BCI 的实用性。能否让机器去适应用户的脑信号模式，而非要求用户学会调控脑信号？

## 核心方法
开发了 Berlin BCI（BBCI）系统，使用 128 通道 EEG 和先进的机器学习方法（Common Spatial Patterns + 正则化线性判别分析）来分类 motor imagery 信号。核心创新是将训练负担从用户转移到算法——只需要一次短暂的校准 session，系统就能自动学会识别该用户的脑信号模式。

## 关键数据
- 128 通道 EEG
- 无需长期用户训练（"zero-training"概念）
- 使用 CSP（Common Spatial Patterns）提取空间特征
- 在未经训练的新用户上即可达到有效性能

## 为什么是 milestone
将 BCI 的设计哲学从"训练用户"转向"训练算法"，这是一个范式转换。BBCI 团队后续推动了 BCI Competition（标准化 BCI 算法评测数据集），极大促进了 BCI 信号处理算法的发展。CSP 方法至今仍是 motor imagery BCI 的标准基线算法。
