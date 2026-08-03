---
title: "Optically pumped magnetometers: from quantum origins to multi-channel magnetoencephalography"
authors: Tierney TM, Holmes N, Mellor S, López JD, Roberts G, Hill RM, Boto E, Leggett J, Shah V, Brookes MJ, Bowtell R, Barnes GR
year: 2019
venue: NeuroImage 199:598-608
url: https://doi.org/10.1016/j.neuroimage.2019.05.063
subfield: non-invasive
tags: [OPM, 方法学, 综述, 源重建, 传感器几何]
---

## 解决了什么问题

OPM-MEG 的数据分析不能直接照搬常规 MEG 的流水线。差别来自三处：传感器位置和朝向可变(不像 SQUID 固定在已知刚性阵列里)、传感器贴近头皮使前向模型对位置误差更敏感、以及 OPM 通常只测一到两个方向的分量。这篇把从量子物理原理到多通道 MEG 数据处理的整条链条讲清，供实际使用者对齐做法。

## 核心方法

方法学教程/综述。覆盖 OPM 的量子物理基础(光泵浦、SERF、调制场读出)、传感器标定、**传感器位置与朝向的共配准**、前向建模与源重建在贴头皮几何下需要做的调整。

## 关键数据

方法学性质，无单一承重实验数字。（本条目未核实原文报告的具体仿真/实测指标，引用时勿编造数值。）

## 为什么是 milestone

这条线上的**方法学参考点**：它把"OPM-MEG 的源定位需要什么条件"写清楚了——其中最关键的一条是必须知道每个传感器相对头部解剖的**位置与测量方向**。这条约束在评估任何 OPM-MEG 新系统时都是硬前提：一个系统能不能做**源定位**(而不只是测到信号)，取决于它能否稳定地确定传感器几何。参见 [[brookes-2022-opm-meg-review]]、[[zhang-2020-unshielded-earth-field-meg]]（后者只做了双通道信号检测、未做源定位）。
