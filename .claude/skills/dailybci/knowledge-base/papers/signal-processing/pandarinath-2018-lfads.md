---
title: "Inferring single-trial neural population dynamics using sequential auto-encoders"
authors: Pandarinath, O'Shea, Collins, Jozefowicz, Stavisky, Kao, Trautmann, Kaufman, Ryu, Hochberg, Henderson, Shenoy, Abbott, Sussillo
year: 2018
venue: Nature Methods
url: https://doi.org/10.1038/s41592-018-0109-9
subfield: signal-processing
tags: [LFADS, sequential-autoencoder, latent-dynamics, neural-population, denoising, RNN]
---

## 解决了什么问题
神经群体记录是稀疏、有噪声、单 trial 变化很大的。传统 BCI decoder 往往直接从 spike counts 或 firing rates 解码，但这些观测信号混入了大量采样噪声。能否先恢复潜在神经动力学，再用更干净的表征进行分析或解码？

## 核心方法
LFADS（Latent Factor Analysis via Dynamical Systems）使用 sequential variational autoencoder 从神经 spike trains 中推断低维潜在动力学。模型包含 encoder RNN 和 generator RNN，把单 trial 神经活动解释为潜在动态系统生成的发放率，再从这些发放率重构观测 spikes。

## 关键数据
- 在非人灵长类和 BrainGate 人体运动皮层数据上验证
- 从 noisy spike counts 中恢复平滑 single-trial firing rates
- 支持跨 session 的 dynamic neural stitching
- 改善对神经群体动态的解释和下游解码基础

## 为什么是 milestone
LFADS 不是一个传统意义上的 BCI 控制器，但它改变了神经信号处理的底层思路：先学习神经群体的潜在动态，再做解释或解码。后来的神经表征学习、自监督 neural foundation models、低维 latent decoder，都可以看作沿着这个方向发展。
