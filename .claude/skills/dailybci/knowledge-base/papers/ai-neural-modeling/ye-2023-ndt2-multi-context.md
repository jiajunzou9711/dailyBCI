---
title: "Neural Data Transformer 2: Multi-context pretraining for neural spiking activity"
authors: Ye, Shelber, Pandarinath
year: 2023
venue: NeurIPS 2023
url: https://arxiv.org/abs/2306.15560
subfield: ai-neural-modeling
tags: [NDT-2, transformer, multi-context, pretraining, transfer-learning, foundation-model]
---

## 解决了什么问题
NDT-1 只能在单个 session 的数据上训练和应用。但真正有用的 neural foundation model 需要能跨 session、跨被试、甚至跨任务迁移。如何让 Transformer 从多个不同实验 context 的神经数据中学习通用表征？

## 核心方法
NDT-2 扩展了 NDT 架构，支持 multi-context pretraining——在来自不同 session、不同任务、甚至不同被试的神经数据上联合预训练。通过 context token 和改进的 tokenization 方案处理不同 session 之间的神经元对应问题。预训练后可以 fine-tune 到新的 session。

## 关键数据
- 跨多个 session 和任务的联合预训练
- 在新 session 上 fine-tune 后性能优于从零训练
- 证明预训练可以捕获跨 context 的共享神经动力学结构
- NeurIPS 2023 发表

## 为什么是 milestone
从"单 session 模型"到"跨 session 预训练模型"的关键一步，是 neural foundation model 的早期实现。证明了 NLP 中的"预训练+微调"范式在神经数据上同样有效，为后续更大规模的 POYO+ 等工作奠定了基础。
