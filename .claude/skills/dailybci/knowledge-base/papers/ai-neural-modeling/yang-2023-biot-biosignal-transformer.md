---
title: "BIOT: Biosignal Transformer for Cross-data Learning in the Wild"
authors: Yang, Westover et al.
year: 2023
venue: NeurIPS 2023
url: https://arxiv.org/abs/2305.10351
subfield: ai-neural-modeling
tags: [foundation-model, EEG, ECG, biosignal, self-supervised, cross-data, transformer, BIOT]
---

## 解决了什么问题
不同来源的生物信号（EEG、ECG、体动）在通道数、采样率、信号长度上各不相同，传统模型只能在单个数据集上训练，无法跨数据集共享表征。迁移学习和多任务学习在文本/图像领域大获成功，但生物信号的"格式异质性"是一道硬障碍。

## 核心方法
把任意格式的生物信号 tokenize 成统一的"biosignal sentence"：将每个通道的时序段切成 patch，附上通道标识符，拼成 token 序列输入 Transformer encoder。这种设计天然兼容不同通道数和信号长度，缺失通道可以简单省略。用 masked autoencoding 做自监督预训练，再在下游任务上 fine-tune。

## 关键数据
- 跨 EEG（癫痫检测 CHB-MIT）、ECG（心律失常）、人体活动传感器三类数据集验证
- CHB-MIT 癫痫检测：vanilla BIOT 比 baseline +3% balanced accuracy；预训练版本再 +4%
- 相比单数据集训练，多数据集联合预训练在所有任务均有提升

## 为什么是 milestone
首个跨数据集、跨模态生物信号基础模型，证明"生物信号也可以像文本一样做大规模预训练"。BIOT 的 patch tokenization 策略成为后续 EEG 基础模型（LaBraM、LUNA 等）的标准起点。它定义了"生物信号基础模型"这条路线的可行性，是 LaBraM 2024 的直接先驱。
