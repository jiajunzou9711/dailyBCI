---
title: "Virtual typing by people with tetraplegia using a self-calibrating intracortical brain-computer interface"
authors: Jarosiewicz, Sarma, Bacher, Masse, Simeral, Sorice, Oakley, Blabe, Pandarinath, Gilja, Cash, Eskandar, Friehs, Henderson, Shenoy, Donoghue, Hochberg
year: 2015
venue: Science Translational Medicine
url: https://doi.org/10.1126/scitranslmed.aac7328
subfield: signal-processing
tags: [self-calibration, RTI, nonstationarity, virtual-typing, intracortical-BCI, BrainGate]
---

## 解决了什么问题
人体 intracortical BCI 的神经信号会在分钟、小时、天的尺度上漂移。传统做法需要用户暂停任务，重新做校准实验；这对日常使用很不现实。问题是：能不能让 BCI 在用户正常使用过程中自己校准？

## 核心方法
作者提出 retrospective target inference（RTI）校准：用户在虚拟键盘上自发点击目标，系统事后根据用户实际选择的目标推断当时的运动意图，再用这些数据更新 decoder。系统还结合神经活动统计跟踪和 velocity bias correction，减少非平稳信号造成的漂移。

## 关键数据
- 四名四肢瘫参与者参与自校准 BCI 测试
- RTI 校准达到与标准显式校准相近的打字性能
- 支持小时到天级别的自 paced typing
- 用户不需要反复执行独立校准任务

## 为什么是 milestone
这篇论文把 decoder calibration 从“实验前准备步骤”变成了“使用过程的一部分”。对临床 BCI 来说，这个转变很关键：一个每天都要工程师重新校准的系统，很难成为日常辅助技术。RTI 证明了 decoder 可以从用户自然行为中持续学习，这是后来自适应 BCI 和长期稳定使用的重要基础。
