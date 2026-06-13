---
title: "A high-performance brain-computer interface for finger pointing and clicking"
authors: Willett, Kunz, Fan, Avansino, Wilson, Choi, Kamdar, Glasser, Hochberg, Druckmann, Shenoy, Henderson
year: 2024
venue: Nature
url: https://doi.org/10.1038/s41586-024-07443-0
subfield: motor-bci
tags: [finger-click, cursor-control, web-browsing, daily-digital-tasks, Stanford]
---

## 解决了什么问题
之前的 motor BCI 在实验室任务上表现良好（中心到达、打字），但现实中人们需要的是浏览网页、发消息、使用 App——这些需要精确的光标定位和点击控制。Willett 2021 用手写解码实现了快速打字，但光标控制和点击是另一套运动模式。

## 核心方法
解码患者尝试的手指微动意图：食指控制光标移动方向和速度，拇指动作解码为"点击"。用深度学习模型将运动皮层神经活动映射为连续的二维光标轨迹和离散的点击事件。关键：将运动分解为两个独立通道（连续的指向 + 离散的点击），分别优化解码。

## 关键数据
- 光标控制性能接近健康人使用触控板的水平
- 患者可独立浏览网页、使用通讯软件、玩游戏
- 每日使用时间数小时
- 长期稳定性良好

## 为什么是 milestone
将 motor BCI 从"实验室演示"推向"日常数字生活工具"。之前的工作证明了 BCI "能做"各种事情，这篇证明了 BCI "好用到可以日常使用"——患者真正把它当作日常与数字世界交互的主要方式。这是 motor BCI 实用化的关键一步。
