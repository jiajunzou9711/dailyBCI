---
title: "Key role of coupling, delay, and noise in resting brain fluctuations"
authors: Deco, Jirsa, McIntosh, Sporns, Kötter
year: 2009
venue: PNAS 106:10302–10307
url: https://doi.org/10.1073/pnas.0901831106
subfield: brain-encoding-models
tags: [whole-brain-model, resting-state, conduction-delay, noise, stochastic-resonance]
---

## 解决了什么问题
静息态波动此前多被当作有待解释的"功能现象"。这篇问的是更基础的一层：这些缓慢的自发波动能否直接由网络本身的物理属性——耦合强度、传导延迟、噪声——生成，而不必赋予它特定的认知功能。

## 核心方法
用 **38 个**耦合振子构成的全脑模型，耦合矩阵取自灵长类皮层-皮层通路的长度与强度数据，因此传导延迟由真实纤维长度决定。再系统扫描耦合强度、传导速度与噪声水平三个参数，看什么条件下会涌现出与实测静息态相似的慢波动。

## 关键数据
- 灵长类连接数据 + 仿真，38 节点。
- 基于真实通路长度与强度的时延耦合导致出现**两组 40 Hz 振子**，各自呈现特征性的同步模式。
- 网络响应性在传导速度 **1–2 m/s**、耦合强度接近下限时最优。
- 存在一个特征性的噪声尺度，使网络出现**随机共振**，从而能检测弥散反馈活动中的细微变化。

## 为什么是 milestone
给出静息态波动的一种结构性解释：它可以是连接组、延迟与噪声共同作用的必然产物。这条结论对解读任何"自发活动的功能意义"都是必须先排除的零假设。方法上，它把传导延迟与噪声正式确立为全脑模型不可省略的参数（此前常被忽略），后续 The Virtual Brain 一类平台即建立在这套参数化之上。
