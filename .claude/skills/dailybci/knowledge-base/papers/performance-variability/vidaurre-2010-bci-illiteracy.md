---
title: "Towards a cure for BCI illiteracy"
authors: Vidaurre, Blankertz
year: 2010
venue: Brain Topography
url: https://doi.org/10.1007/s10548-009-0121-6
subfield: performance-variability
tags: [performance-variability, BCI-illiteracy, SMR, co-adaptive, online-adaptation, EEG-BCI]
---

## 解决了什么问题
非侵入 BCI 最棘手的现实问题之一是 "BCI illiteracy(BCI 文盲)":有相当比例的使用者无法用 BCI 实现有效控制。本文聚焦基于感觉运动节律(SMR)的系统,试图从机器学习/自适应一侧解决这一问题,而非简单把使用者归为"用不了"。

## 核心方法
人体研究(健康被试,头皮 EEG)。提出一套在线自适应方案:从一个与被试无关、只用简单特征的初始分类器起步,在同一次会话、同一反馈应用持续交互的过程中,逐步过渡到为该被试优化的分类器;前段用有监督自适应做用户-机器协同学习,后段用无监督自适应,从而给出不含偏倚、无需离线校准的性能度量。

## 关键数据
- "BCI illiteracy" 影响约 **15%–30%** 的使用者(文中估计)。
- 该方案不需任何离线校准测量,优秀被试(含一名新手)在 **3–6 分钟**自适应后即获良好表现。
- 更关键的是:此前无法获得有效反馈的使用者,借机器学习自适应获得了对系统的显著控制;其中一名被试起初没有 SMR idle 节律峰,实验过程中发展出该峰并能主动调制其幅度来控制反馈。

## 为什么是 milestone
它把"用不了 BCI"从"使用者的固有缺陷"重新定义为"机器可以适应的问题",确立了协同自适应(co-adaptive)与在线自校准这条解 inefficiency 的主线,影响深远(高被引)。与 [[jeunet-2015-predicting-mi-bci-performance]](从使用者特质侧预测)互补,共同界定非侵入侧"为什么有人用不好、怎么办"的两条路径。综合见 [[niu-2025-cognitive-state-eeg-bci-review]]。
