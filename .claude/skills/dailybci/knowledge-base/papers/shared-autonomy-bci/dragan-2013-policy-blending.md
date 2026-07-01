---
title: "A policy-blending formalism for shared control"
authors: Dragan, Srinivasa
year: 2013
venue: International Journal of Robotics Research, 32(7):790-805
url: https://doi.org/10.1177/0278364913490324
subfield: shared-autonomy-bci
tags: [shared-control, policy-blending, intent-prediction, arbitration, teleoperation]
---

## 解决了什么问题
遥操作/共享控制中,机器人需要预测用户意图并据此提供辅助,但当时缺乏一个能统一描述"预测用户意图"与"把预测和用户输入仲裁融合"这两个环节的通用形式化框架。

## 核心方法
提出"策略混合(policy blending)"形式化:把辅助行为表示为用户输入策略与预测的自主策略之间的加权融合;意图预测问题建立在逆强化学习基础上。论文说明已有多种共享控制技术都可以看作该形式化的特例,并对预测和仲裁两个核心成分给出系统分析。

## 关键数据
在真实用户遥操作机械臂完成任务的数据上验证了该框架,证明策略混合能捕捉多种既有共享控制方法。

## 为什么是 milestone
这是共享控制/共享自主领域最广泛引用的理论基础之一,给后续几乎所有"神经信号解码+自主辅助融合"的工作(包括本领域内的 BCI 共享控制研究)提供了统一的数学语言和分析框架。
