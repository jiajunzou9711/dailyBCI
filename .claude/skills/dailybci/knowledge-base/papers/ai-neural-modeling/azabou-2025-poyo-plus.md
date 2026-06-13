---
title: "Multi-session, multi-task neural decoding from distinct cell-types and brain regions"
authors: Azabou, Pan, Arora, Knight, Dyer, Richards
year: 2025
venue: ICLR 2025
url: https://arxiv.org/abs/2310.16046
subfield: ai-neural-modeling
tags: [POYO+, foundation-model, multi-session, multi-task, Allen-Institute, transformer, ICLR]
---

## 解决了什么问题
能否在一个 Transformer 模型中同时处理来自不同脑区、不同细胞类型、不同解码任务的神经数据？之前的 multi-session 方法只能处理相同脑区和相同细胞类型的 session。

## 核心方法
POYO+ 是一个多任务 Transformer 架构，在 Allen Institute Brain Observatory 数据集的全部数据上训练。通过改进的 tokenization 方案和 session-specific 嵌入，统一处理来自不同脑区（视觉皮层各区、海马等）和不同基因标记细胞类型的 spike 数据。支持多种解码任务的联合训练。

## 关键数据
- 在 Allen Institute Brain Observatory 全量数据上训练
- 跨多个脑区和基因标记的细胞类型
- 多种解码任务（刺激分类、行为预测等）联合训练
- 规模化训练带来持续的性能提升
- ICLR 2025 发表

## 为什么是 milestone
当前 neural foundation model 方向最具雄心的工作之一。直接回答了"更多数据是否带来更好的大脑解码"这个核心问题——答案是肯定的。POYO+ 证明了跨脑区、跨细胞类型的异质数据可以被统一建模，为真正的"大脑通用模型"指明了方向。
