---
title: "High-resolution image reconstruction with latent diffusion models from human brain activity"
authors: Takagi, Nishimoto
year: 2023
venue: CVPR
url: https://openaccess.thecvf.com/content/CVPR2023/html/Takagi_High-Resolution_Image_Reconstruction_With_Latent_Diffusion_Models_From_Human_Brain_CVPR_2023_paper.html
subfield: ai-neural-modeling
tags: [visual-reconstruction, fMRI, stable-diffusion, latent-diffusion, NSD, text-conditioning]
---

## 解决了什么问题
扩散模型生成质量高但训练/微调昂贵。能否**不重新训练生成模型**，仅用简单映射就把 fMRI 接到现成的 Stable Diffusion 上做高分辨率重建，是工程与原理上的关键问题。

## 核心方法
用线性回归把 fMRI 分别映射到 Stable Diffusion 的两类条件：(1) 早期视觉区 → 图像潜在 z（管布局/结构）；(2) 高级视觉区 → 文本条件嵌入（经图像 caption，管语义）。直接驱动**未额外训练**的 Stable Diffusion 采样。数据用 NSD。还做了"哪个脑区对应扩散模型哪个组件"的定量对应分析。

## 关键数据
- 仅用线性映射 + 现成 Stable Diffusion 即得到语义与结构兼顾的高分辨率重建。
- 通过逐区/逐组件分析，给出脑区与扩散模型潜在/条件空间的对应关系。

## 为什么是 milestone
示范"现成大生成模型 + 简单线性脑映射"的极简高效路线，极大降低视觉重建门槛，是 2023 扩散 era 最具传播力的标志性工作。与 [[ozcelik-2023-latent-diffusion-scene-reconstruction]]、[[scotti-2023-mindeye-fmri-to-image]] 共同把 NSD + 潜在扩散定为该线主流。
