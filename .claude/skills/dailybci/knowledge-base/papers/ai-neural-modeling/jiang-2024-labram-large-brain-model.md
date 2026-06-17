---
title: "Large Brain Model for Learning Generic Representations with Tremendous EEG Data in BCI"
authors: Jiang, Zhao et al.
year: 2024
venue: ICLR 2024 (Spotlight)
url: https://arxiv.org/abs/2405.18765
subfield: ai-neural-modeling
tags: [foundation-model, EEG, LaBraM, vector-quantization, masked-prediction, pretraining, BCI, cross-task]
---

## 解决了什么问题
EEG-BCI 深度学习模型长期是"一个数据集、一个模型、一个任务"的孤立范式，规模无法扩展、泛化能力差。能否仿照大语言模型的预训练+微调路线，在海量 EEG 数据上训练一个通用基础模型，再迁移到多种 BCI 下游任务？

## 核心方法
将 EEG 信号按通道切成 patch，用**向量量化（VQ）神经频谱预测**训练一个 EEG tokenizer：先把频域表示量化成离散 code book 中的 token，再训练 Transformer 对 masked EEG patch 的 token 做预测（类似 BERT 的 masked token prediction，但针对 EEG 频谱）。预训练数据：约 **2500 小时** EEG 来自约 **20 个不同数据集**（跨任务、跨设备）。

## 关键数据
- 预训练规模：2500h EEG，~20 数据集，跨异常检测、情绪识别、运动想象等多种范式
- 下游任务（fine-tuning 后）：异常检测、事件类型分类、情绪识别、步态预测均超越各任务 SOTA
- ICLR 2024 Spotlight（约 5% 接收率），公认为 EEG FM 领域的奠基工作

## 为什么是 milestone
LaBraM 是 EEG 基础模型中**首个在规模和迁移效果上均令人信服的工作**——它证明了"跨任务 EEG 预训练 → 微调"的可行性，让整个领域开始认真对待"EEG foundation model"这个方向。VQ 神经频谱 tokenizer 这个设计后来被广泛引用和改进。EEGDash 要解决的"数据获取门槛"问题，正是 LaBraM 展示预训练可行性之后才变得紧迫的。
