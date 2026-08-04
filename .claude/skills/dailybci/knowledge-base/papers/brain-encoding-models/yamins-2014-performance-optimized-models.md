---
title: "Performance-optimized hierarchical models predict neural responses in higher visual cortex"
authors: Yamins, Hong, Cadieu, Solomon, Seibert, DiCarlo
year: 2014
venue: PNAS 111:8619–8624
url: https://doi.org/10.1073/pnas.1403112111
subfield: brain-encoding-models
tags: [encoding-model, deep-network, IT-cortex, macaque, task-optimization]
---

## 解决了什么问题
高级视觉皮层（IT）的神经响应长期缺少能定量预测的模型：手工设计的特征（Gabor、SIFT 之类）能解释早期视区，但对 IT 的预测力很弱。问题是从哪里得到合适的特征空间。

## 核心方法
不去手工设计特征，而是把**任务性能**当作寻找模型的搜索目标：在物体识别任务上优化分层卷积网络，再用其各层激活作为编码模型的特征空间，线性映射到实测神经响应。核心检验是"识别性能高的模型是否同时更能预测神经响应"。

## 关键数据
- 猕猴（rhesus macaque），IT 与 V4 单元记录；刺激为复杂自然图像。
- 模型的物体识别性能与其对**单个 IT 单元**响应的预测能力之间存在强相关。
- 性能达到人类识别水平量级的网络，其输出层可预测 IT 的发放，单单元与群体两个层面均成立；**中间层**则预测 V4（IT 的主要输入来源）。

## 为什么是 milestone
确立"任务优化即模型搜索"这一范式：不再逐条假设神经元算什么，而是让在生态相关任务上训练出的网络自动给出候选特征空间。这条路线随后从视觉扩到语言（[[schrimpf-2021-neural-architecture-language]]）与语音，也是今天几乎所有深度编码模型的方法学起点。同时要注意其边界——层级对应关系是相关证据，不等于机制等同。
