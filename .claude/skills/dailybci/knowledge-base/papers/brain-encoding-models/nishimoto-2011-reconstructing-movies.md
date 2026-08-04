---
title: "Reconstructing visual experiences from brain activity evoked by natural movies"
authors: Nishimoto, Vu, Naselaris, Benjamini, Yu, Gallant
year: 2011
venue: Current Biology 21:1641–1646
url: https://doi.org/10.1016/j.cub.2011.08.031
subfield: brain-encoding-models
tags: [encoding-model, motion-energy, fMRI, naturalistic, hemodynamics, reconstruction]
---

## 解决了什么问题
[[kay-2008-identifying-natural-images]] 处理的是静态图像。动态刺激的困难在于时间尺度不匹配：视觉信息以几十毫秒变化，而 BOLD 血流动力学响应以秒计。此前的 fMRI 视觉工作因此基本绕开自然影片。

## 核心方法
提出**运动能量（motion-energy）编码模型**，把快速的视觉信息处理与慢速的血流动力学响应显式分成两级：前级用时空 Gabor 滤波器组提取运动能量，后级再卷积血流动力学响应函数。有了这个前向模型，再配一个以自然影片为先验的**贝叶斯解码器**做重建。

## 关键数据
- 人类 fMRI，被试观看自然影片。
- 指认分析：在超过**一百万段**候选片段的集合中，解码器把刺激时刻定位在 **±1 秒**以内的比例为 **95%**。
- 可从脑活动重建出与所看影片在内容上可辨认对应的视频。

## 为什么是 milestone
把编码模型从静态图像扩到**时间维度**，并给出处理"神经快、BOLD 慢"这一结构性错配的标准做法（两级分离）。它也是后续所有"自然主义刺激 + 编码模型"工作的直接前身；今天的自然影片 fMRI 数据集与预测模型（如脑动力学预测类工作）都建立在这套问题设定上。
