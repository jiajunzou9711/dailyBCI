---
title: "A high-performance neural prosthesis enabled by control algorithm design"
authors: Gilja, Nuyujukian, Chestek, Cunningham, Yu, Fan, Churchland, Kaufman, Kao, Ryu, Shenoy
year: 2012
venue: Nature Neuroscience
url: https://doi.org/10.1038/nn.3265
subfield: motor-bci
tags: [ReFIT, Kalman-filter, closed-loop, cursor-control, algorithm, Shenoy, Stanford]
---

## 解决了什么问题
早期 BCI 的光标控制慢、不流畅，远不如真实手臂。核心问题不完全在于神经信号质量，而在于解码算法没有充分利用闭环反馈——传统 Kalman filter 在开环条件下训练，用于闭环控制时性能严重下降。

## 核心方法
提出 ReFIT-KF（Recalibrated Feedback Intention-Trained Kalman Filter）。核心创新：（1）区分位置和速度的解码方式——假设用户控制的是速度而非位置；（2）在闭环条件下重新校准解码器，用用户实际的闭环行为数据（而非开环训练数据）来更新模型参数。这使解码器适应了真实使用场景中的神经信号统计特性。

## 关键数据
- 光标控制性能比传统方法翻倍
- 接近真实手臂控制的速度和准确度
- 可持续使用数小时无性能下降
- 植入数年后仍保持高性能

## 为什么是 milestone
证明了 BCI 性能瓶颈不只是"硬件"（电极数量、信号质量），算法设计同样关键。ReFIT 的闭环重校准思想影响了后续几乎所有高性能 BCI 系统的算法设计。这篇论文将 motor BCI 的可用性从"勉强能用"提升到了"接近实用"的水平。
