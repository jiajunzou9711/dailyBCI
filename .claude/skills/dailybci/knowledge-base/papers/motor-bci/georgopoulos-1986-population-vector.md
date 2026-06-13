---
title: "Neuronal population coding of movement direction"
authors: Georgopoulos, Schwartz, Kettner
year: 1986
venue: Science
url: https://doi.org/10.1126/science.3749885
subfield: motor-bci
tags: [population-vector, direction-tuning, motor-cortex, theoretical-foundation]
---

## 解决了什么问题
在此之前，人们知道运动皮层神经元与运动有关，但不清楚如何从神经元群体活动中"读出"运动方向。单个神经元的调谐曲线太宽、太嘈杂，无法精确编码方向。

## 核心方法
让猕猴执行中心向外的 reaching 任务，记录运动皮层神经元活动。发现每个神经元对特定方向（preferred direction）反应最强，响应强度随偏离角度呈余弦衰减。关键创新：提出 population vector——将每个神经元视为一个指向其 preferred direction 的矢量，长度正比于放电率，所有神经元的矢量加权求和即可精确预测运动方向。

## 关键数据
- 单神经元调谐曲线呈余弦分布
- Population vector 方向与实际运动方向高度吻合
- 仅需几十个神经元即可实现精确方向预测

## 为什么是 milestone
这是所有 motor BCI 解码算法的理论起点。Population vector 证明了运动意图可以从神经群体活动中数学地"读出"，而不需要找到某个"指令神经元"。后续几乎所有 BCI 解码方法——从线性滤波到 Kalman filter 到深度学习——都建立在"从群体活动解码"这一范式之上。
