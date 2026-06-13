---
title: "Direct cortical control of 3D neuroprosthetic devices"
authors: Taylor, Tillery, Schwartz
year: 2002
venue: Science
url: https://doi.org/10.1126/science.1070291
subfield: motor-bci
tags: [3D-control, closed-loop, neuroprosthetic, cursor, primate, Schwartz]
source_review: "Brain–Computer Interfaces with Intracortical Implants for Motor and Communication Functions Compensation (PMC 2024, ref 41)"
---

## 解决了什么问题
之前的 BMI 工作（如 Wessberg 2000）主要是"开环"预测——用神经信号预测手臂运动但猴子仍然在自己移动手臂。能否让猴子直接用脑信号在3D空间中控制虚拟光标（闭环），而不需要实际的手臂运动？

## 核心方法
在猕猴运动皮层植入电极阵列，训练猴子先用手臂移动3D光标到目标位置，然后切断手臂控制，让光标完全由皮层信号驱动。猴子必须学会通过调节神经活动来控制3D光标移动。使用 population vector algorithm 实时解码。

## 关键数据
- 猴子在闭环模式下成功控制3D空间中的光标
- 从开环（手臂控制）到闭环（纯脑控制）的无缝过渡
- 解码基于18-25个神经元
- 3D reach任务完成率显著高于随机水平

## 为什么是 milestone
首次在灵长类中实现真正的闭环3D neuroprosthetic控制。之前的工作都是开环预测（用神经信号预测已经发生的运动），Taylor 2002 证明了动物可以直接用脑信号控制外部设备，无需实际肢体运动。这从根本上验证了 BCI 的临床可行性——瘫痪患者没有肢体运动，必须依赖这种闭环控制。
