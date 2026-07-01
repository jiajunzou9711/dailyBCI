---
title: "Autonomy infused teleoperation with application to brain computer interface controlled manipulation"
authors: Muelling, Venkatraman, Valois, Downey, Weiss, Javdani, Hebert, Schwartz, Collinger, Bagnell
year: 2017
venue: Autonomous Robots (原发表于 RSS 2015)
url: https://doi.org/10.1007/s10514-017-9622-4
subfield: shared-autonomy-bci
tags: [intracortical-BCI, shared-control, teleoperation, robotic-manipulation, human]
---

## 解决了什么问题
皮层内BCI解码的运动指令噪声大、维度高,直接控制机械臂完成复杂日常任务(开门、倒液体、操作陌生物体)对使用者认知负担极重,单纯提升解码精度难以解决这一瓶颈。

## 核心方法
提出"注入自主性的遥操作(autonomy infused teleoperation)"共享控制框架,把解码出的用户神经指令与机器人自主子系统(物体识别、抓取规划、轨迹优化)融合,在保留用户意图主导权的同时接管精细执行环节。**两名植入皮层内BCI的人类被试**用该框架控制7自由度机械臂,在开门、倒液体、操作杂乱环境中的陌生物体等康复相关基准任务上测试。

## 关键数据
共享辅助显著降低了被试主观感受的任务难度,并使此前用纯BCI直接控制"完全无法完成"的任务变得可行。

## 为什么是 milestone
这是皮层内人类BCI与机器人共享自主结合的最早直接实证之一(与 Collinger 2013 同一匹兹堡团队/被试群体),把"共享控制"从抽象机器人理论(如 [[dragan-2013-policy-blending]])带入真实植入式BCI场景,是本领域内后续几乎所有"BCI+AI辅助"工作的直接学术祖先。
