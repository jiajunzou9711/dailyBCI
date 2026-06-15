---
title: "Equivalent volitional learning emerges through circuit-specific population dynamics in motor cortex and hippocampus"
authors: de Vicente, Mitelut, Mendes, ... Donato
year: 2026
venue: bioRxiv (preprint)
url: https://www.biorxiv.org/content/10.64898/2026.06.04.730137v1
subfield: population-dynamics
tags: [neural-manifold, BCI-learning, hippocampus, CA3, motor-cortex, two-photon, calcium-imaging, RNN, principled-degeneracy]
---

## 解决了什么问题
神经流形约束学习这条线([[sadtler-2014-neural-constraints-learning]] → [[golub-2018-learning-neural-reassociation]] → [[oby-2019-new-activity-patterns-long-term]] → [[busch-2026-human-noninvasive-manifold-bci]])几乎只在(猴/人的)运动皮层做,隐含假设"流形学习也许是通用规律"。但一直没有正面回答:换一个**架构迥异、非运动输出**的脑区,能否被同样训练?是用同一套机制,还是各有各的解法?

## 核心方法
用实时双光子钙成像搭神经反馈 BCI:任意选一小撮神经元分正/负组(ensemble state = pE − nE),实时映射成听觉音调反馈,小鼠 30 s 内把 state 推过阈值即得水奖励(纯神经控制、无运动中介)。把**同一套任务**独立压在两个脑区:**初级运动皮层 M1**(cranial window;7 只小鼠 / 30,388 neurons / 54 sessions)与**海马 CA3**(microendoscope;6 只小鼠 / 23,168 neurons / 48 sessions)。再用两个仅在递归架构上不同的 RNN(低秩递归 ≈ M1 / 对称自联想吸引子 ≈ CA3)做因果模型。

## 关键数据
- **学得一样好:** 两区命中率随训练显著上升(混合效应 β=0.838, p<0.001),均显著高于 chance;**phase × group 交互不显著(β=−0.160, p=0.453)→ 两区学习无显著差异**。
- **动力学却分叉:** 投影到 reward manifold 上,M1 活动"流过"奖励态(flow through),CA3 "逼近—折返"(approach-and-return);该差异随训练才显现。
- **架构决定差异:** 仅差递归结构的两个 RNN 分别复现"流过 / 折返",说明分叉源于各区自身环路结构,而非任务。

## 为什么是 milestone
该线第一次把流形-BCI 学习范式正面搬出运动皮层、进入架构迥异的海马 CA3,并与 M1 头对头对比,给出干净结论:**"能不能学"是通用的(海马也行),但"学成什么动力学"由各环路自身结构决定。**作者据此提出 **principled degeneracy(原理性简并)**——学习没有唯一的标准神经解,而是多种被局部网络架构塑形的、等价但形状不同的实现。把整条线从"运动皮层专属?"推进到"跨电路的学习原理"。承自 [[oby-2019-new-activity-patterns-long-term]] 与 [[busch-2026-human-noninvasive-manifold-bci]]。
