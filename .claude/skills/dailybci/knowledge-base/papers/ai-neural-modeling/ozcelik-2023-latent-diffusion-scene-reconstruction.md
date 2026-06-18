---
title: "Natural scene reconstruction from fMRI signals using generative latent diffusion"
authors: Ozcelik, VanRullen
year: 2023
venue: Scientific Reports
url: https://doi.org/10.1038/s41598-023-42891-8
subfield: ai-neural-modeling
tags: [visual-reconstruction, fMRI, latent-diffusion, NSD, CLIP, brain-decoding]
---

## 解决了什么问题
深度重建已能合成自然图像，但在复杂自然场景上同时还原**低层结构（轮廓/布局）与高层语义（物体/场景含义）**仍困难。扩散模型的强生成力能否被引入脑解码，成为问题。

## 核心方法
用生成式潜在扩散模型（Versatile Diffusion）作生成器，把 fMRI 分别映射到两路潜在：一路低层（VDVAE 潜在，管结构/布局），一路高层语义（CLIP 图像与文本嵌入，管内容）。两路条件共同驱动扩散采样。数据用大规模 Natural Scenes Dataset（NSD，7T fMRI）。

## 关键数据
- 在 NSD 上同时改善低层保真与高层语义一致性，重建自然场景的物体与布局。
- 论文报告其在多项图像相似度/语义指标上优于同期方法。

## 为什么是 milestone
把"扩散时代"正式带入视觉脑解码，确立"低层潜在 + CLIP 语义"双路条件的实用配方，并把 NSD 树立为该线的标准基准。与同年 [[scotti-2023-mindeye-fmri-to-image]]、[[takagi-2023-stable-diffusion-reconstruction]] 共同定义 2023 年 fMRI-to-image 的扩散范式。
