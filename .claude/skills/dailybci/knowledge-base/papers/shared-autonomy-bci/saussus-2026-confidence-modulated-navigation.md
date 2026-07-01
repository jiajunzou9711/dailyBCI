---
title: "Shared AI-brain control for reliable intracortical BCI navigation in dynamic environments"
authors: Saussus, Song, De Schrijver, Caprara, Detry, Janssen
year: 2026
venue: bioRxiv
url: https://doi.org/10.64898/2026.03.23.713738
subfield: shared-autonomy-bci
tags: [intracortical-BCI, confidence-modulated, temporal-prior, macaque, navigation, failure-mode]
---

## 解决了什么问题
皮层内BCI连续导航任务中,解码神经指令存在瞬时波动,直接执行会导致碰撞、冲过目标点等执行层面失败。已有的共享控制方法多聚焦于"能不能帮上忙",较少刻画"什么时候会帮倒忙"。

## 核心方法
提出置信度调制的AI-brain共享控制框架(RT-V2):AI副驾驶依据"最近一小段解码历史是否一致"(用置信度指数α=1-归一化熵衡量)动态决定信任历史、还是信任当前解码指令——历史一致时把执行修得更平滑,历史杂乱时基本原样传递解码指令;另设碰撞前150ms的强制安全接管。

## 关键数据
- 2只恒河猴(3个96通道Utah阵列,M1/PMv/PMd),闭环虚拟导航
- 执行层面失败率从BCI-only的约37%降到约4%(障碍碰撞近乎清零,目标冲出误差16%→3%)
- 共享控制不改变解码方向内容,只在解码方向本身基本正确时起作用
- Respawn任务(目标中途突变)中共享控制反而使成绩从80%降到67%(p=0.01)——边界条件
- 离线回放证明:重置时间先验消除滞后、恢复基线表现,证明失灵是算法性的,非解码本身出问题

## 为什么是 milestone
这是第一篇把"共享控制什么时候会失灵"用干净的对照实验(离线回放+先验重置)机制性刻画清楚的工作,把这条方法论脉络从"验证有效性"推进到"刻画适用边界",延续了 [[muelling-2017-autonomy-infused-teleoperation-bci]] / [[downey-2016-blending-bmi-vision-guided]] 的皮层内BCI共享控制线,但从任务分工转向了置信度调制的时序仲裁。
