---
title: "Deep image reconstruction from human brain activity"
authors: Shen, Horikawa, Majima, Kamitani
year: 2019
venue: PLOS Computational Biology
url: https://doi.org/10.1371/journal.pcbi.1006633
subfield: ai-neural-modeling
tags: [visual-reconstruction, fMRI, DNN-features, generative-prior, imagery, optimization]
---

## 解决了什么问题
Horikawa & Kamitani 2017 能把脑活动映射到 DNN 特征并识别类别，但还不能由此**生成一幅自然图像**。如何从解码到的层级特征反推出逼真的图像本身，是下一步。

## 核心方法
先从 fMRI 解码出 DNN 多层特征，再**优化一幅图像，使其经同一 DNN 提取的各层特征逼近解码值**；并引入深度生成网络（DGN）作自然图像先验，约束结果落在自然图像流形上，避免对抗噪声式的解。配套有端到端版本（[[Shen 2019b, Front Comput Neurosci]]）。

## 关键数据
- 能重建被试**所见**的自然图像、人造形状与字母；也能重建**想象**的图形（重建质量低于所见）。
- 跨层特征联合约束 + 自然图像先验，明显提升可辨识度。

## 为什么是 milestone
把视觉重建从"拼对比图案"推进到"由层级深度特征 + 生成先验合成自然图像"，确立了"神经→特征→生成模型"的现代三段式管线。它是潜在扩散重建（[[ozcelik-2023-latent-diffusion-scene-reconstruction]]、[[takagi-2023-stable-diffusion-reconstruction]]）到来前的关键过渡。
