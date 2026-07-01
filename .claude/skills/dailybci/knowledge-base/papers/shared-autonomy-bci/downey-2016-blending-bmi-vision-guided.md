---
title: "Blending of brain-machine interface and vision-guided autonomous robotics improves neuroprosthetic arm performance during grasping"
authors: Downey, Weiss, Muelling, Venkatraman, Valois, Hebert, Bagnell, Schwartz, Collinger
year: 2016
venue: Journal of NeuroEngineering and Rehabilitation, 13(1):28
url: https://doi.org/10.1186/s12984-016-0134-9
subfield: shared-autonomy-bci
tags: [intracortical-BCI, shared-control, vision-guided-robotics, grasping, human]
---

## 解决了什么问题
BMI解码的到达(reach)运动通常可靠,但抓取(grasp)阶段的精细手部定位常因解码噪声而失败;抓取物体、尤其是相邻紧凑摆放的多个物体时,单纯依赖神经解码的手部控制不够精确。

## 核心方法
在同一匹兹堡团队的皮层内BCI平台上(与 [[muelling-2017-autonomy-infused-teleoperation-bci]] 同源),当机械手接近目标物体时,引入基于计算机视觉的自主辅助来协助手部精细定位和抓取执行,同时仍由用户的神经指令主导到达和总体决策。

## 关键数据
一名被试在两个紧邻物体中准确抓取指定目标的成功率达92%;两名被试在物体转移任务上,使用共享控制时的表现均优于纯BMI控制——动作更准确、更高效、被试自评难度更低。

## 为什么是 milestone
证明了共享控制的收益具体来自"分工":把用户擅长的意图/目标选择留给神经解码,把机器擅长的精细执行(视觉引导抓取)交给自主系统,而非试图整体提升解码精度本身,是"设计原则"层面(而非纯算法层面)的共享控制milestone。
