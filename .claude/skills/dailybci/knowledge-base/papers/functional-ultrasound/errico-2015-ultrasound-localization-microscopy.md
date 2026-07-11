---
title: "Ultrafast ultrasound localization microscopy for deep super-resolution vascular imaging"
authors: Errico, Pierre, Pezet, Desailly, Lenkei, Couture, Tanter
year: 2015
venue: Nature 527:499–502
url: https://doi.org/10.1038/nature16066
subfield: functional-ultrasound
tags: [ULM, super-resolution, microbubbles, microvasculature, transcranial, rat]
---

## 解决了什么问题
超声的空间分辨率受衍射极限约束,在"分辨率 vs 穿透深度"之间存在长期权衡,把临床与临床前超声成像限制在亚毫米尺度。光学超分辨(如 PALM)可突破衍射极限,但光在组织中散射,只能成像表层。深部器官的微米级成像因此长期缺位。

## 核心方法
把光学定位显微的思想搬到超声:注入惰性气体**微泡**造影剂,以超快帧率(>500 帧/秒)采集,利用微泡在连续帧间的瞬态信号去相关把单个微泡逐个定位、再累积成图。作者称之为**超快超声定位显微(ultrafast ultrasound localization microscopy, ULM)**。这是结构与血流动力学成像,而非直接的功能激活成像。

## 关键数据
- 帧率 >500 帧/秒(原文 "more than 500 frames per second")。
- 在**大鼠**上实现亚波长结构成像与血流动力学定量,分辨直径 <10 µm 的脑微血管。
- 成像深度超过组织表面以下 10 mm,支持经颅全脑成像(短时采集)。

## 为什么是 milestone
把超声的空间分辨率从亚毫米推进到微米量级,证明"超声可以既深又细"。在 fUS 的坐标系里,这条线负责回答"分辨率的物理上限在哪",与 [[mace-2011-functional-ultrasound-brain]] 的功能激活成像互补;经颅可行性也为人体应用埋下伏笔。对 BCI 而言,它目前的角色是解剖/血管基底,而非解码信号源——因为需要注射造影剂、且成像的是血管结构与灌注,而非任务相关的瞬态激活。
