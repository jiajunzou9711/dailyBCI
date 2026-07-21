---
title: "Brain-Computer Interface with Inhibitory Neurons Reveals Subtype-Specific Strategies"
authors: Mitani A, Dong M, Komiyama T
year: 2018
venue: Curr Biol 28:77-83
url: https://doi.org/10.1016/j.cub.2017.11.035
subfield: optical-bci
tags: [two-photon, interneurons, cell-type, BCI, mouse, Komiyama]
---

## 解决了什么问题
此前所有 BCI 工作都不区分皮层的细胞类型，尽管不同细胞类型在皮层计算中承担不同功能，控制 BCI 的能力也可能不同。这一维度完全没有被检验过。

## 核心方法
小鼠，双光子钙成像记录表达 GCaMP6f 的三类主要皮层抑制性中间神经元（PV、SOM、VIP）；做神经元配对操作性条件反射任务——当正目标神经元（N+）的活动超过负目标神经元（N−）达到设定阈值时给予奖励；追踪训练过程中的可塑性变化。

## 关键数据
- 三种亚型上小鼠**都**能提高任务表现，但采用的策略是**亚型特异**的。
- 目标 PV 中间神经元时，N− 的活动**下降**。
- 目标 SOM 与 VIP 中间神经元时，N+ 的活动**上升**。

## 为什么是 milestone
首次把细胞类型作为 BCI 的一个自变量，并证明不同抑制性亚型走的是不同的解法路径。这是光学 BCI 相对电生理 BCI 的独有能力——电极分不清 PV/SOM/VIP。结论对神经假体设计有含义：控制策略并非由任务定义唯一决定，也取决于被接入的是哪类细胞。相关：[[clancy-2014-optical-neuroprosthetic-learning]]
