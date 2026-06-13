---
title: "Fine grained two-dimensional cursor control with epidural minimally invasive brain-computer interface"
authors: Tsinghua (Hong Bo group) & Neuracle Technology et al.
year: 2025
venue: medRxiv (preprint)
url: https://www.medrxiv.org/content/10.1101/2025.10.06.25337264v1
subfield: invasive-recording
tags: [epidural-ECoG, minimally-invasive, 2D-cursor, bilateral-representation, multi-effector, NEO, ITR, degrees-of-freedom]
---

## 解决了什么问题

硬膜外微创 BCI 已证明可做二元抓握检测（见 [[neo-2024-epidural-minimally-invasive-bci]]），但开关式指令自由度太低。单侧 8 触点硬膜外场电位能否支撑**连续二维控制**这种更高自由度的任务，是这条半侵入路线能否走向实用的关键瓶颈。本研究（**人体**，同一例颈髓损伤瘫痪患者）针对此展开。

## 核心方法

在右侧感觉运动皮层手区硬膜外放置 8 个 Pt-Ir 电极记录场电位。关键发现：硬膜外信号**同时编码对侧与同侧运动**，呈现双侧表征结构；当两个效应器（如手与肘）同时运动时，神经模式相对单动作呈**非线性（非叠加）变化**。据此提出"双侧单/双动作"解码方案，把有限的可区分动作组合映射为二维目标控制，从而在不增加电极的前提下扩展自由度（DoF）与信息传输率（ITR）。

## 关键数据

- 二维 center-out 任务：Fitts' ITR 均值 **36.7 bpm**；web-grid 任务 **30.0 bpm**；命中率均 **>91%**。
- 神经记录稳定 **>18 个月**；解码器免重校准稳定 **>6 个月**。
- 仅用单侧 8 触点硬膜外电极实现，无穿透皮层。

## 为什么是 milestone

证明硬膜外半侵入 BCI 不止能做开关式抓握，还能支撑精细二维光标控制，把该路线的性能上限显著上移。它揭示了硬膜外场电位的双侧/多效应器表征结构，为"用少量电极换更多自由度"提供了可复用的解码思路。与 [[neo-2024-epidural-minimally-invasive-bci]]（临床锚点）和 [[neuracle-2026-neo-nmpa-approval]]（监管里程碑）共同构成中国硬膜外 BCI 路线的证据链。对照 KB 中皮层内二维/高维控制（[[gilja-2012-refit-kalman-filter]]、[[collinger-2013-7dof-robotic-arm]]），它展示了用低侵入硬件逼近实用控制性能的可能。
