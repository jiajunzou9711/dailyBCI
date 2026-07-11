---
title: "Single-trial decoding of movement intentions using functional ultrasound neuroimaging"
authors: Norman, Maresca, Christopoulos, Griggs, Demene, Tanter, Shapiro, Andersen
year: 2021
venue: Neuron 109:1554–1566.e4
url: https://doi.org/10.1016/j.neuron.2021.03.003
subfield: functional-ultrasound
tags: [fUS, BMI, single-trial-decoding, posterior-parietal-cortex, macaque, epidural, movement-planning]
---

## 解决了什么问题
BCI 的记录模态在"侵入性 / 性能 / 空间覆盖 / 时空分辨率"之间各有取舍:皮层内微电极阵列性能最好但要穿刺皮层且通道覆盖有限;EEG 无创但空间分辨率粗、单试次信噪比低。fUS 在动物上已证明空间分辨率与灵敏度俱佳,但没人验证过它能否支撑 BCI 的**必要条件——单试次解码**(逐次试验读出意图,而不是跨试次平均)。

## 核心方法
在**猕猴**执行记忆引导运动任务时,把超声探头置于**硬膜之外**(记录时不穿刺脑组织)对**后顶叶皮层(PPC)**做 fUS 成像,分辨率约 100 µm,测量脑血容量变化。取运动**之前的延迟期(delay period)** fUS 信号,离线解码动物意图的运动**方向**与**效应器**(眼动 vs 手动)。选择 PPC 是因为该区参与空间感知、多感觉整合与运动计划(与 KB 中 [[aflalo-2015-posterior-parietal-motor-imagery]] 的人类 PPC-BCI 同一逻辑)。

## 关键数据
- 记录位置:硬膜外(outside the dura),PPC;空间分辨率 100 µm。
- 从运动前延迟期的 fUS 信号中**单试次**解出意图方向与效应器(离线解码,非闭环)。
- 论文自我定位为"迈向微创超声 BCI 的关键一步",未宣称实时控制。

## 为什么是 milestone
第一篇把 fUS 当作**BCI 记录模态**来检验的工作,并且过了单试次这一关。它划出了一个此前空缺的坐标格:一种不穿刺皮层、分辨率介于皮层内电生理与非侵入成像之间的记录方式。局限也很清楚——离线解码、血流动力学信号的秒级延迟。这两点分别由 [[griggs-2024-closed-loop-ultrasonic-bmi]](闭环)与后续人体工作推进。
