---
title: "Visual image reconstruction from human brain activity using a combination of multiscale local image decoders"
authors: Miyawaki, Uchida, Yamashita, Sato, Morito, Tanabe, Sadato, Kamitani
year: 2008
venue: Neuron
url: https://doi.org/10.1016/j.neuron.2008.11.004
subfield: ai-neural-modeling
tags: [visual-reconstruction, fMRI, decoding, V1, modular-decoder, image-reconstruction]
---

## 解决了什么问题
早期视觉解码只能做"分类"（判断被试看的是哪一类刺激）。能否真正把"所见的图像本身"从脑活动里重建出来，而非从有限候选里挑一个，是当时的开放问题。

## 核心方法
把图像拆成多个空间尺度的局部图像基（multiscale local image bases），对每个局部元用 V1–V3 的 fMRI 体素活动单独训练一个解码器，再把这些局部预测线性组合还原整幅图。模块化解码 + 局部基组合，使系统能重建**训练集里从未出现过**的任意 10×10 二值对比图案。

## 关键数据
- 在 10×10 像素的对比图案（字母、几何形状）上实现逐像素重建，能拼出 "neuron"、几何形状等训练外图案。
- 主要信息来自早期视觉皮层（V1 贡献最大），证明视网膜拓扑组织可被读出。

## 为什么是 milestone
首次证明"从脑活动重建所见图像本身"可行，开创视觉图像重建（visual image reconstruction）研究方向。其"把刺激分解到一组基、对每个基单独解码再组合"的思路，是后续所有 neural→特征空间→生成 重建范式的源头。相关后续见 [[horikawa-2017-generic-decoding-dnn-features]]、[[shen-2019-deep-image-reconstruction]]。
