---
title: "Reconstructing the mind's eye: fMRI-to-image with contrastive learning and diffusion priors (MindEye)"
authors: Scotti, Banerjee, Goode, Shabalin, Nguyen, et al.
year: 2023
venue: NeurIPS 36
url: https://arxiv.org/abs/2305.18274
subfield: ai-neural-modeling
tags: [visual-reconstruction, fMRI, contrastive-learning, diffusion-prior, CLIP, NSD, retrieval]
---

## 解决了什么问题
扩散重建已可用，但如何把 fMRI 同时做到**高精度图像检索**（在大图库里找回正确的那张）与**高质量图像重建**，并最大化对齐到 CLIP 表征空间，仍有提升空间。

## 核心方法
MindEye 用两条管线：高层语义管线把 fMRI 经 MLP backbone + **对比学习**映射进 CLIP 图像嵌入空间，再接一个**扩散先验**（diffusion prior，借鉴 DALL·E 2）把脑导出的嵌入"提纯"到可生成的 CLIP 空间；低层管线经变分自编码重建 blurry 初稿。两者结合送入扩散生成器。数据用 NSD。

## 关键数据
- 论文报告在 NSD 上图像检索与重建多项指标刷新当时 SOTA；脑→CLIP 检索准确率显著高于此前方法。
- 对比学习 + 扩散先验的组合是性能关键。

## 为什么是 milestone
把**对比学习对齐**确立为脑解码的核心训练目标（与 2026 候选"对齐胜过复杂度"的 fMRI 解码主张呼应），并示范"脑→CLIP→扩散生成"的强基线。后续 MindEye2 进一步推向少量数据跨被试。对比解码这条线另见 [[defossez-2023-meta-meg-speech]]。
