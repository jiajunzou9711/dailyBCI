---
title: "High-sensitivity atomic magnetometer unaffected by spin-exchange relaxation"
authors: Allred JC, Lyman RN, Kornack TW, Romalis MV
year: 2002
venue: Physical Review Letters 89:130801
url: https://doi.org/10.1103/PhysRevLett.89.130801
subfield: non-invasive
tags: [OPM, SERF, 原子磁力计, 物理地基]
---

## 解决了什么问题

原子磁力计的灵敏度长期受**自旋交换弛豫**限制：碱金属原子之间的碰撞会破坏原子自旋之间的相干性，相干性一散，可测的信号就衰减。这是把原子磁力计推到"能测脑磁"量级(fT 级)的主要物理障碍。

## 核心方法

提出并实现 **SERF(spin-exchange relaxation-free，自旋交换弛豫自由)** 工作区：在近零磁场下把碱金属蒸气**加热**到高原子密度，使碰撞发生得极快——快到在一次进动周期内原子经历大量碰撞，自旋反而保持相干进动(只是进动变慢)，自旋交换弛豫对灵敏度的贡献被消除。

## 关键数据

该工作确立了 SERF 区的可行性，为此后 fT/√Hz 量级的小型原子磁力计铺路。（本条目未核实原文报告的具体灵敏度数值，引用时勿编造。）作为参照，后来用于 MEG 的商用 OPM 噪声本底约 **7–10 fT/√Hz**（见 [[brookes-2022-opm-meg-review]]）。

## 为什么是 milestone

这是整条 OPM-MEG 路线的**物理前提**。没有 SERF，原子磁力计达不到脑磁所需的灵敏度，"用不需要液氦的传感器做 MEG"就无从谈起。同时它也埋下了 OPM 的两个先天代价，后续所有工程工作都在处理它们：① SERF 需要**加热**蒸气室，导致传感器发热(高通道数系统的散热问题由此而来)；② SERF 只在**近零场**附近工作，动态范围极小(场变化超过约 3 nT 即失效)，这正是可穿戴 OPM-MEG 必须配主动磁屏蔽的根本原因。
