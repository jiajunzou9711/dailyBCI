---
title: "Representation learning for neural population activity with Neural Data Transformers"
authors: Ye, Pandarinath
year: 2021
venue: Neurons, Behavior, Data analysis, and Theory
url: https://doi.org/10.51628/001c.27358
subfield: ai-neural-modeling
tags: [NDT, transformer, BERT, neural-dynamics, non-recurrent, real-time, Pandarinath-lab]
---

## 解决了什么问题
LFADS 等基于 RNN 的模型需要顺序处理数据，推理速度慢，不适合实时 BCI 应用。能否用 Transformer 的并行处理能力来建模神经群体动力学，同时保持或超过 RNN 的性能？

## 核心方法
Neural Data Transformer（NDT）基于 BERT 编码器架构，对神经群体的 spike 数据进行 masked token 预测。将每个时间 bin 的神经活动视为一个 token，通过自注意力机制捕获时间依赖关系。不需要显式的动力学方程，而是让 Transformer 隐式学习数据中的时序结构。

## 关键数据
- 在猴运动皮层 reaching 数据上性能持平 LFADS 等 RNN 模型
- 推理速度 3.9ms，比 RNN 基线快 6 倍以上
- 成功捕获合成动力系统的已知结构
- 为 BCI 实时应用提供了可行的非递归方案

## 为什么是 milestone
首次将 Transformer 架构成功应用于神经群体 spike 数据建模。证明了 NLP 领域的 masked language model 范式可以迁移到神经科学。NDT 直接催生了 NDT-2 和后续的 neural foundation model 研究方向，是从 LFADS 到 foundation model 的关键过渡。
