---
title: "Shared functional specialization in transformer-based language models and the human brain"
authors: Kumar, Sumers, Yamakoshi, Goldstein, Hasson, Norman, Griffiths, Hawkins, Nastase
year: 2024
venue: Nature Communications
url: https://doi.org/10.1038/s41467-024-49173-5
subfield: brain-encoding-models
tags: [attention-heads, BERT, fMRI, encoding-model, functional-specialization, naturalistic-story]
---

## 解决了什么问题
以往把 LLM 用于脑活动预测时，取的是模型生成的**内部表征**（embeddings）。本文改为**直接分析电路计算**——把计算拆成一个个注意力头各自实现的「变换」，问模型内部的功能分工与皮层上的分工对不对得上。

## 核心方法
BERT-base 共 **12 层 × 12 头 = 144 个头**。**N=63** 名被试听自然口语故事的 fMRI，降采样到 **1000 个皮层分区**；分区水平编码模型，**带状岭回归**、三折交叉验证，音素/音素率/词率/静音作混淆项，结果换算成由被试间相关估计的**噪声天花板**百分比。对每个头同时打两个分：**依存预测分**（该头的注意力模式多好地预测 12 种句法依存关系）与**脑预测分**（该头的变换多好地预测某 ROI）。

## 关键数据
- Transformer 的 embeddings 与 transformations 在多数语言 ROI 上**优于经典语言学特征**（词性 + 句法依存），p<0.005，FDR 校正。
- transformations 与 embeddings 预测水平相当，但两者本身几乎不相关（逐 TR 平均 **−0.004 ± 0.009 SD**）。
- 把各头在 1000 个分区上的权重做 PCA，**PC1+PC2 解释 92% 方差**；各头在这个低维空间里呈**梯度**分布：层深梯度（与层相关最强的是 PC9 r=0.45、PC5 r=0.40）、**回看距离梯度沿 PC2 最强（r=0.65）**，头的注意力距离上四分位数**超过 30 个 token**。
- Clark 2019 报告的「功能特化头」横跨 PC1、聚在 PC2 负端（中间层、较近回看距离）。
- 两个对照：层内跨头打乱特征、以及未训练模型，**对应关系均消失**。

## 为什么是 milestone
把「模型与大脑的对应」从表征层面推进到**电路计算层面**，并给出结论的正确形状：**分工确实对得上，但对上的方式是沿层深与语境跨度的连续梯度，而非一格一格的离散分区。** 与 [[shain-2024-distributed-syntax-semantics]] 汇成同一图景（专门化是程度之别）。**必读的边界**：从注意力头里读出类似依存语法的东西，不意味着头在执行依存语法的图运算——同一批头也受语义合理性影响；这是「能读出来 ≠ 里面存在」这条主脊的第一个实例。**属自引提示**：Nastase 与 Hasson 同为 [[nastase-2026-language-population-code]] 作者。
