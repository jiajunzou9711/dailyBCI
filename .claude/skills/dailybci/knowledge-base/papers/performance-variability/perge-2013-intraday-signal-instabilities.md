---
title: "Intra-day signal instabilities affect decoding performance in an intracortical neural interface system"
authors: Perge, Homer, Malik, Cash, Eskandar, Friehs, Donoghue, Hochberg
year: 2013
venue: Journal of Neural Engineering
url: https://doi.org/10.1088/1741-2560/10/3/036004
subfield: performance-variability
tags: [performance-variability, intracortical, BrainGate, signal-instability, firing-rate, decoder-bias, human]
---

## 解决了什么问题
皮层内神经接口要可靠,前提是"记录到的神经信号 ↔ 意图运动"的关系稳定。但在单次会话(日内)尺度上,这一关系会漂移。本文系统刻画日内神经信号变异的频率与成因,并区分其中多少来自技术伪迹、多少来自生理机制,以及它如何转化为解码性能下降。

## 核心方法
人体研究:**3 名四肢瘫患者**(BrainGate 试点临床试验,IDE),运动皮层植入硅微电极阵列。分析单次会话内、跨几分钟任务时段的放电活动与动作电位幅值波动,并用计算机仿真检验单神经元系统性放电率变化如何影响光标解码。

## 关键数据
- **84%** 的记录单元在日内出现统计显著的表观放电率变化(3.8 ± 8.71 Hz,约为均值放电率的 49%);**74%** 的单元出现显著的动作电位幅值变化(约为均值幅值的 5.5%)。
- 40% 的会话中,幅值变化跨电极显著相关,提示阵列微位移。
- 在观察到的日内放电率变化中,仅约 **15%** 源自伪迹(幅值变化/电噪声),约 **85%** 最可能来自生理机制。
- 放电率不稳定在 **56%** 的表现评估中给解码出的光标运动带来方向性"偏置"(n = 2 名参与者,两年内 108 与 20 次评估),导致这些会话表现欠佳。

## 为什么是 milestone
它是"皮层内 BCI 性能日内变异"的奠基性实证:量化了变异之普遍、并指出其主体是生理性的(而非单纯电极伪迹),把"信号不稳"从工程瑕疵上升为需要算法/神经层面理解的核心问题(高被引)。它界定了皮层内侧"信号变异"的研究起点;而"生理性放电率漂移里有多少来自注意/认知状态"正是后续 [[downey-2018-intracortical-recording-stability]] 与今日候选(主动操纵注意负荷)要追问的。框架见 [[dunlap-2020-intracortical-signal-disruptions-review]]。
