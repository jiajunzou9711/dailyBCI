---
title: "A large-scale examination of inductive biases shaping high-level visual representation in brains and machines"
authors: Conwell, Prince, Kay, Alvarez, Konkle
year: 2024
venue: Nature Communications 15:9383
url: https://doi.org/10.1038/s41467-024-53147-y
subfield: brain-encoding-models
tags: [encoding-model, controlled-comparison, NSD, human-fMRI, inductive-bias, RSA]
---

## 解决了什么问题
"哪一类模型更像脑"长期靠零散比较回答，架构、训练目标、训练数据三者互相混淆。本文用受控对照把三者分开，问每一项各自对脑预测力贡献多少。

## 核心方法
人类 **NSD 7T 功能磁共振**，取所有被试共享的 **1000 张 COCO 图**、**4 名被试**（subj 01/02/05/07）。**224 个模型**逐项受控对照——其他因素固定住，只换一项：架构（CNN vs Vision Transformer）、训练目标（有监督分类 / 对比自监督 SimCLR·MoCoV2·BarlowTwins / 非对比自监督 RotNet·Jigsaw / 视觉—语言对齐 CLIP·SLIP）、训练数据（ImageNet1K vs 21K，以物体 / 场景 / 人脸为主的库）。指标为 cRSA 与 veRSA。累计 **超过 18 亿次回归**与 **5.03 万次表征相似性分析**。每个受测架构另配一个随机初始化对照（**N = 64**）。

## 关键数据
- 架构与训练目标差别极大的模型，脑预测力**近乎相同**（其他因素固定时）。
- 效应最大的一项是**训练用的图**（visual training diet）。
- 分类准确率与脑预测力之间原文表述为 **"little to no relationship"**。
- **训练本身**是全篇最大、最稳的效应（cRSA β = 0.30 [0.29, 0.31]；veRSA β = 0.56，均 p < 0.001）——未训练模型远低于训练模型，但并非零。
- 作者结论之一：许多**表征明显不同**的模型拿到同样高的脑预测力，提示把模型连到脑上的标准方法**可能太宽松**。

## 为什么是 milestone
把"脑预测力"这个指标本身变成了被检验的对象，并给出它区分能力有限的直接证据。与 [[linsley-2023-worse-models-of-it]] 是同一问题的两条独立证据链（人类 fMRI／猕猴单神经元），但**强度不同：本篇是无相关，Linsley 是负相关，引用时不得合并**。为 [[loke-2026-texture-alignment]] 的成分归属追问提供了直接动机。
