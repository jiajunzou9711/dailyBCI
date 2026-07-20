---
title: "Modeling the spatial reach of the LFP"
authors: Lindén, Tetzlaff, Potjans, Pettersen, Grün, Diesmann, Einevoll
year: 2011
venue: Neuron 72:859–872
url: https://doi.org/10.1016/j.neuron.2011.11.006
subfield: invasive-recording
tags: [LFP, spatial-reach, volume-conduction, input-correlation, modeling]
---

## 解决了什么问题
"局部场电位到底有多局部"长期众说纷纭，文献给出的范围从数百微米到数毫米不等。分歧的根源没有被讲清。

## 核心方法
生物物理正向建模：从形态学真实的神经元与突触输入出发，计算群体活动在电极处叠加成的场电位，逐一考察神经元形态、突触输入的空间分布、以及**邻近神经元输入之间的相关性**对可及范围的影响。

## 关键数据
- 突触输入**互不相关**时，LFP 主要来自电极周围**几百微米**（视觉皮层实测量级约 250 µm、直径约 500 µm）。
- 输入**相关**（一群神经元同步）时，各自贡献**同相叠加**、衰减被大幅抵消，可及范围可撑到**毫米级**。
- 可及范围还是**频率依赖**的。

## 为什么是 milestone
它给出了那个反直觉但关键的结论：**LFP 的空间范围主要由"源同不同步"决定，而非由电极决定。** 这解释了文献分歧的来源，也意味着同一支电极听不同信号时半径差一到两个数量级（与 [[henze-2000-extracellular-spike-distance]] 的 50–140 µm 对照）。引用 LFP 空间尺度时必须同时交代相关性条件。
