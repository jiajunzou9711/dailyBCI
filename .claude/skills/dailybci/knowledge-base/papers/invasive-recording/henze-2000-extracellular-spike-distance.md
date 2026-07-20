---
title: "Intracellular features predicted by extracellular recordings in the hippocampus in vivo"
authors: Henze, Borhegyi, Csicsvari, Mamiya, Harris, Buzsáki
year: 2000
venue: Journal of Neurophysiology 84:390–400
url: https://doi.org/10.1152/jn.2000.84.1.390
subfield: invasive-recording
tags: [listening-radius, spike-sorting, extracellular-potential, ground-truth, rat]
---

## 解决了什么问题
胞外电极记录到的动作电位幅度与"神经元离电极多远"之间，长期缺少直接标定的地面真值。没有这条曲线，就无法回答一个最基础的问题：**一支电极究竟能听多远。**

## 核心方法
在麻醉大鼠海马 CA1 做**胞内与胞外同步记录**：胞内电极确证某个神经元确实发放，胞外电极同时记录其胞外波形，从而把"已知身份的神经元"与"它在不同距离产生的胞外幅度"一一对应，得到距离-幅度的实测标定。

## 关键数据
- 胞外动作电位幅度随距离**陡降**，快于点电流源的 1/r，实践上接近指数式衰减。
- 可被稳定分离为单个单元（single unit）的范围约在 **50 µm** 以内。
- 分离阈值的惯例为信噪比 3–4 倍、约 **50–60 µV**。
- 物种：**麻醉大鼠**，海马 CA1。

## 为什么是 milestone
它把"听力半径"从定性直觉变成可引用的实测数字，是此后所有 spike sorting 与电极设计讨论的地面真值。与 [[rey-2015-spike-sorting-review]] 的三区划分互为独立佐证。判断任何皮层内记录工作时，这条曲线是隐含前提。
