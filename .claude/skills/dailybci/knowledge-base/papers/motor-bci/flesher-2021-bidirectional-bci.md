---
title: "A brain-computer interface that evokes tactile sensations improves robotic arm control"
authors: Flesher, Downey, Weiss, Hughes, Herber, Gaunt, Collinger, Tyler-Kabara, Bensmaia, Schwartz
year: 2021
venue: Science
url: https://doi.org/10.1126/science.abd0380
subfield: motor-bci
tags: [bidirectional-BCI, tactile-feedback, somatosensory-stimulation, robotic-arm, closed-loop, Schwartz, Bensmaia]
---

## 解决了什么问题
之前的 motor BCI 是单向的：大脑→机器。但自然运动依赖触觉反馈来调节抓握力度——没有触觉，抓取物体时要么太轻（滑落）要么太重（损坏）。能否建立双向 BCI，在解码运动的同时给大脑提供触觉反馈？

## 核心方法
在运动皮层植入 Utah 阵列解码运动意图（output），同时在体感皮层（S1）植入阵列进行微电刺激（input），模拟机器人手指接触物体时的触觉信号。刺激模式采用仿生学（biomimetic）策略，模拟自然神经系统传递触觉信息的方式。患者在执行抓取任务时同时接收运动解码和触觉反馈。

## 关键数据
- 加入触觉反馈后，临床上肢评估任务时间从中位 20.9 秒降至 10.2 秒（减半）
- 提速主要来自抓取阶段的时间缩短
- 仿生学刺激模式优于非仿生学模式
- 患者报告感受到了手指尖的触觉感知

## 为什么是 milestone
首个真正的双向 BCI 临床演示——不仅从大脑读出运动指令，还向大脑写入感觉信息。任务时间减半的数据证明触觉反馈不是"锦上添花"而是"功能必需"。这为未来的 BCI 设计确立了新方向：真正实用的神经假体必须是双向的。
