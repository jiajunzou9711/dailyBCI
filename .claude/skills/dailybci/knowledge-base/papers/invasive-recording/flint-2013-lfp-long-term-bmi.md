---
title: "Long term, stable brain machine interface performance using local field potentials and multiunit spikes"
authors: Flint, Wright, Scheid, Slutzky
year: 2013
venue: Journal of Neural Engineering
url: https://doi.org/10.1088/1741-2560/10/5/056005
subfield: invasive-recording
tags: [LFP, multiunit-spikes, long-term-stability, BMI-performance, chronic-decoding, Slutzky]
source_review: "Restoring Speech Using Brain-Computer Interfaces (Annual Reviews of Bioengineering 2025, ref 47 context); intracortical BCI reviews"
---

## 解决了什么问题
Chestek 2011证明了sorted spike信号会随时间退化。LFP（局部场电位）被认为可能更稳定，但能否用LFP驱动BMI达到与spike相当的控制性能？这种性能能否长期维持？

## 核心方法
在猕猴运动皮层植入Utah阵列，分别用LFP特征和multiunit spike (MSP) 特征训练BMI解码器进行闭环光标控制。系统比较两种信号源的解码性能、长期稳定性，以及是否需要重新训练。

## 关键数据
- LFP-based BMI性能与spike-based BMI相当
- LFP信号在11个月内保持稳定，无需重新训练解码器
- MSP-based BMI性能在6个月内保持稳定
- 两种信号源均显著优于sorted单元方案的长期表现
- 在线闭环验证（非仅离线分析）

## 为什么是 milestone
提供了"LFP替代spike"策略的关键实证。之前的证据多为离线分析，Flint 2013首次在长达11个月的在线闭环BMI中证明LFP可以持续提供稳定的高性能控制。这对临床BCI的长期可用性有重大意义——如果可以用LFP而非spike，那么即使电极周围形成胶质瘢痕导致spike消失，BMI仍然能工作。与Chestek 2011互补，共同确立了"信号类型的选择决定了BCI的使用寿命"这一核心认知。
