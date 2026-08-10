---
title: "Dynamic stimulation of visual cortex produces form vision in sighted and blind humans"
authors: Beauchamp MS, Oswalt D, Sun P, Foster BL, Magnotti JF, Niketeghad S, Pouratian N, Bosking WH, Yoshor D
year: 2020
venue: Cell 181(4):774–783.e5
url: https://pubmed.ncbi.nlm.nih.gov/32413298/
subfield: visual-prosthesis
tags: [cortical-visual-prosthesis, dynamic-current-steering, form-vision, blind-humans, letters, encoding-strategy]
---

## 解决了什么问题
皮层视觉假体半个世纪以来的默认假设是：多个电极同时刺激产生的光幻视会像屏幕上的像素一样拼成完整图形。实践中这个假设不成立——同时刺激时单个光幻视的特征会互相干扰、丢失，拼不出可辨认的形状。

## 核心方法
换一条编码思路：**按时间顺序依次刺激一串电极，在视皮层表面"描摹"出形状的轨迹**（动态电流转向，dynamic current steering），而非同时点亮一组点。在**明眼人与盲人**被试上测试字母形状的识别。

## 关键数据
- 明眼与盲人被试都能**准确识别**由动态刺激画出的字母形状，且识别结果与大脑视网膜拓扑图预测的形状一致。
- 盲人被试的识别**又快又稳，速度达每分钟 86 个形状**。

## 为什么是 milestone
把这条路线的编码范式从"空间并行的像素阵列"改成"时间序列的轨迹描摹"，绕开了多电极同时刺激互相干扰这个长期障碍。**每分钟 86 个形状**是这条线上第一个能与实际使用速率相提并论的功能数字。它与 [[bosking-2017-phosphene-size-saturation]] 出自同一组（Yoshor/Beauchamp，Baylor→Penn），逻辑上是连续的：既然单个光幻视的大小与形状被皮层结构锁死、无法自由塑形，就改用时间维度承载形状信息。今日候选工作走的是第三条路——不预设编码方案，而是直接学习"什么刺激能把群体活动推到目标状态"。
