---
title: "Connectome-constrained networks predict neural activity across the fly visual system"
authors: Lappalainen JK, Tschopp FD, Prakhya S, et al. (末位作者 Turaga SC)
year: 2024
venue: Nature 634:1132-1140
url: https://doi.org/10.1038/s41586-024-07939-3
subfield: ai-neural-modeling
tags: [connectome, Drosophila, optic-lobe, motion-detection, task-optimization, deep-mechanistic-network, connectome-constrained]
---

## 解决了什么问题

连接组能测出每个神经元连到谁，但测不出单个神经元与单个突触的动力学参数。问题是：**只凭测得的连接，加上一个任务约束，能不能反推出这些参数，并预测真实的神经活动**。

## 核心方法

用果蝇视叶运动通路中 **64 个细胞类型**的连接组搭建网络（作者称 deep mechanistic network，DMN）。神经元是被动点神经元、突触为瞬时分级释放（发放率模型，不发放动作电位）。利用细胞类型结构压缩参数：同一细胞类型共用时间常数与静息电位（每类型 2 个），每对细胞类型之间共用一个单位突触强度；突触权重 = 连接组突触数 × 单位强度 × 正负号，**正负号来自递质与受体两方面的测定**。全网只有 **734 个自由参数**（不借助连接组则需估计远超百万个连接权重）。参数用深度学习的任务优化求出：让网络从视频中检测运动（光流）。

## 关键数据

- 模型对每个细胞类型给出可检验预测，**与 26 项已发表研究的实测神经活动相符**（摘要）。
- 分析以任务表现最好的 10 个模型为准。
- 作者结论：连接稀疏时，这种「连接组 + 任务优化」策略更可能成功。

## 为什么是 milestone

与 Shiu 2024 形成对照：Shiu 全脑只有 1 个自由参数（W_syn），全脑共用一组膜参数；Lappalainen 把参数细化到**每个细胞类型、每对细胞类型**，并用任务反推其值。它给出了补足「连接之外的参数」的一条路线——参数由优化反推、再用未参与训练的实测检验；局限是这些参数本身仍未被直接测量。
