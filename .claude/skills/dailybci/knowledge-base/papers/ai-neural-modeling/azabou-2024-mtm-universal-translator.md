---
title: "Towards a universal translator for neural dynamics at single-cell, single-spike resolution"
authors: Azabou, Arora, Ganesh, Mao, Nachimuthu, Mendelson, Richards, Bhaskaran-Nair, Ye, Pandarinath, Dyer
year: 2024
venue: NeurIPS 2024
url: https://arxiv.org/abs/2407.14668
subfield: ai-neural-modeling
tags: [MtM, multi-task-masking, universal-translator, foundation-model, cross-region, self-supervised]
---

## 解决了什么问题
现有的 neural foundation model（如 NDT-2）仍局限于相似类型的数据（同一脑区、同一任务）。能否构建一个真正"通用"的模型，同时处理来自不同脑区、不同神经元类型、不同实验任务的 spike 数据？

## 核心方法
Multi-task Masking（MtM）方法在自监督学习中交替执行三种不同的掩码-重构任务：（1）masked time steps（时间维度预测）；（2）masked neurons（神经元维度预测）；（3）masked brain regions（脑区维度预测）。模型同时学习时间动力学、神经元间关系和跨脑区结构。

## 关键数据
- 在 Allen Institute Brain Observatory 数据集上训练
- 跨多个脑区和细胞类型的联合建模
- 性能显著超过现有 population model 基线
- 支持 single-cell、single-spike 精度的推理

## 为什么是 milestone
提出了构建 neural "universal translator" 的具体技术路径。三维度掩码的自监督方案优雅地解决了神经数据异质性问题。是 neural foundation model 从"可行性证明"走向"规模化"的重要一步，直接影响了 POYO+ 等后续工作。
