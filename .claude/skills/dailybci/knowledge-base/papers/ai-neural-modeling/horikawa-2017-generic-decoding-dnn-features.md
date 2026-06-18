---
title: "Generic decoding of seen and imagined objects using hierarchical visual features"
authors: Horikawa, Kamitani
year: 2017
venue: Nature Communications
url: https://doi.org/10.1038/ncomms15037
subfield: ai-neural-modeling
tags: [visual-decoding, fMRI, DNN-features, generic-decoding, imagery, feature-alignment]
---

## 解决了什么问题
此前解码器只能区分训练时见过的有限类别。如何让解码器泛化到**训练集里从未出现的任意物体类别**，并解释脑活动与深度网络表征之间的对应关系，是核心难题。

## 核心方法
不直接解码"类别"，而是从 fMRI 解码出**预训练 CNN（深度网络）各层的特征向量**，再在该特征空间里用最近邻匹配到任意候选类别的特征——因此称 generic decoding（通用解码）。关键发现：脑区与 DNN 层级存在层级对应（低级视觉区↔低层特征、高级视觉区↔高层语义特征）。同一框架对**想象的物体**也成立。

## 关键数据
- 能识别训练集外的物体类别（候选集可扩展到上千类），证明特征空间解码的可迁移性。
- 看到的与想象的物体都可解码；想象解码主要依赖高层（语义）特征。

## 为什么是 milestone
确立了"把神经活动映射进**预训练网络的特征空间**、再在该空间做下游任务"这一范式——这正是后续 fMRI-to-image 扩散重建、以及 2026 年 NEURRATOR 把单神经元 spike 映射进冻结 CLIP patch 空间的概念祖先。它把视觉解码从"分类"升级为"对齐到通用表征"。延伸见 [[shen-2019-deep-image-reconstruction]]、[[scotti-2023-mindeye-fmri-to-image]]、[[defossez-2023-meta-meg-speech]]。
