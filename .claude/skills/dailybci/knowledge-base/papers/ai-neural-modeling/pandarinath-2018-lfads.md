---
title: "Inferring single-trial neural population dynamics using sequential auto-encoders"
authors: Pandarinath, O'Shea, Collins, Jozefowicz, Stavisky, Kao, Trautmann, Churchland, Shenoy
year: 2018
venue: Nature Methods
url: https://doi.org/10.1038/s41592-018-0109-9
subfield: ai-neural-modeling
tags: [LFADS, variational-autoencoder, neural-dynamics, single-trial, latent-factors, Shenoy-lab]
---

## 解决了什么问题
神经群体活动的 single-trial 动力学被噪声掩盖，传统方法需要在多个 trial 间平均才能提取稳定的神经轨迹。但 BCI 和行为神经科学需要逐 trial 的精确动力学估计。

## 核心方法
LFADS（Latent Factor Analysis via Dynamical Systems）是一个序列变分自编码器（sequential VAE），用双向 RNN 编码器推断初始条件和外部输入，用前向 RNN 生成器建模潜在动力系统的演化。通过变分推理从 single-trial 的 spike 数据中恢复去噪后的神经群体动力学。

## 关键数据
- 从单次 trial 的 spike 数据中恢复平滑的神经轨迹
- 在运动皮层数据上，解码性能显著优于传统方法
- 在合成数据上准确恢复已知的动力系统
- 支持推断时变的外部输入（inferred inputs）

## 为什么是 milestone
LFADS 是将深度生成模型引入计算神经科学的标志性工作。它证明了 VAE + RNN 可以从嘈杂的神经数据中发现隐藏的动力学结构。后续的 NDT、POYO 等 foundation model 都直接建立在 LFADS 开创的"用生成模型学习神经群体动力学"这一范式上。
