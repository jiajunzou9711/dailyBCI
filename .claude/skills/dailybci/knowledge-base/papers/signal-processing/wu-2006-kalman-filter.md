---
title: "Bayesian population decoding of motor cortical activity using a Kalman filter"
authors: Wu, Black, Mumford, Gao, Bienenstock, Donoghue
year: 2006
venue: Neural Computation
url: https://doi.org/10.1162/089976606774841585
subfield: signal-processing
tags: [Kalman-filter, Bayesian-decoding, motor-cortex, continuous-control, population-decoding]
---

## 解决了什么问题
早期 BCI 解码常把神经活动映射到离散目标或简单方向，但连续控制需要在每个时间点估计手臂或光标的连续状态。问题是：如何把带噪声的神经群体发放转化为平滑、实时、可更新的运动轨迹？

## 核心方法
这篇论文把 motor cortical population decoding 表述为贝叶斯状态估计问题，用 Kalman filter 同时建模运动状态的时间连续性和神经发放与运动状态之间的统计关系。解码器在每个时间步根据上一时刻的运动状态预测当前状态，再用新观测到的神经发放更新估计。

## 关键数据
- 将神经解码形式化为递归贝叶斯估计
- 同时估计位置、速度等连续运动变量
- 显式利用运动轨迹的时间平滑性
- 为后续 velocity Kalman filter 和 ReFIT-KF 奠定数学基础

## 为什么是 milestone
Kalman filter 成为后续十多年 motor BCI 的默认基线算法，不是因为它最复杂，而是因为它把连续神经控制变成了一个稳定、实时、可解释的工程问题。后来 ReFIT-KF、self-calibrating BCI、cursor control 和 robotic arm control 的许多系统，都是在这个框架上修改训练目标、状态变量或闭环假设。
