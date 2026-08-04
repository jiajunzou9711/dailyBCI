---
title: "Identifying natural images from human brain activity"
authors: Kay, Naselaris, Prenger, Gallant
year: 2008
venue: Nature 452:352–355
url: https://doi.org/10.1038/nature06713
subfield: brain-encoding-models
tags: [encoding-model, receptive-field, fMRI, visual-cortex, identification]
---

## 解决了什么问题
在此之前的 fMRI 解码工作多是**分类**：在少数几个预先测量过的刺激或类别之间做区分，因而解码器只对训练时见过的那批刺激有效。这篇要回答的是：能否对**从未测量过的新自然图像**做指认。

## 核心方法
不训练判别器，而是先对每个体素拟合一个定量的感受野编码模型——用 Gabor 小波族描述该体素对**空间位置、朝向、空间频率**的调谐，参数由自然图像的响应估计。有了前向模型，对任意新图像都可以预测它会引起的活动模式；指认时把实测模式与候选集中每张图的预测模式比对，取最匹配者。

## 关键数据
- 人类，早期视皮层（V1/V2/V3 等）。
- 在大候选图集里可指认出被试当时看的是**哪一张全新的自然图像**；性能显著高于只用视网膜拓扑（位置）信息的模型，说明只靠空间调谐不够，朝向与空间频率承载了额外可辨识信息。
- 作者据此推断，从脑活动重建视觉经验的图像本身可能可行（该预测由 [[nishimoto-2011-reconstructing-movies]] 与后续重建工作接续）。

## 为什么是 milestone
第一次把"编码模型 + 大候选集指认"这条路线跑通，把 fMRI 解码从"在若干已知类别里选一个"推进到"对未见过的自然刺激泛化"。此后视觉、语言、语音三条编码模型线都沿用这一评估范式。
