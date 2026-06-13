---
title: "Different Origins of Gamma Rhythm and High-Gamma Activity in Macaque Visual Cortex"
authors: Ray, Maunsell
year: 2011
venue: PLoS Biology
url: https://doi.org/10.1371/journal.pbio.1000610
subfield: invasive-recording
tags: [high-gamma, gamma-rhythm, broadband, population-firing-rate, ECoG-theory, Ray]
source_review: "Restoring Speech Using Brain-Computer Interfaces (Annual Reviews of Bioengineering 2025, ref 42 context); multiple ECoG BCI reviews"
---

## 解决了什么问题
ECoG/LFP中的"gamma频段"(>30 Hz)被广泛用于BCI解码，但gamma到底反映什么？窄带gamma振荡和宽带high-gamma (>70 Hz)功率增加是同一现象还是完全不同的信号？

## 核心方法
在猕猴视觉皮层同时记录LFP和单神经元spike，系统性地分析不同视觉刺激下narrowband gamma (30-80 Hz) 和broadband high-gamma (>70 Hz) 的行为差异，以及它们与spike活动的关系。

## 关键数据
- Narrowband gamma和broadband high-gamma具有不同的刺激选择性
- High-gamma与spike活动紧密正相关，narrowband gamma则不然
- 在某些条件下gamma和high-gamma功率呈反相关
- High-gamma反映局部神经元群体放电率，是"方便获取且可靠的群体放电指标"

## 为什么是 milestone
从根本上区分了两种长期被混淆的皮层信号：narrowband gamma是真正的神经振荡（与网络同步有关），而broadband high-gamma本质上是神经元群体放电的频域表现（非节律性）。这一发现为ECoG BCI选择high-gamma作为核心解码特征提供了坚实的生物物理理论基础——你解码的不是"振荡"，而是局部神经元群体的平均放电率。直接影响了后续所有ECoG语音/运动BCI的特征工程选择。
