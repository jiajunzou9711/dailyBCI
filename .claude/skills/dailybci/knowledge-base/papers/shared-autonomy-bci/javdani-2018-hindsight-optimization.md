---
title: "Shared autonomy via hindsight optimization for teleoperation and teaming"
authors: Javdani, Admoni, Pellegrinelli, Srinivasa, Bagnell
year: 2018
venue: International Journal of Robotics Research, 37(7):717-742 (原发表于 RSS 2015)
url: https://doi.org/10.1177/0278364918776060
subfield: shared-autonomy-bci
tags: [shared-control, POMDP, hindsight-optimization, teleoperation]
---

## 解决了什么问题
[[dragan-2013-policy-blending]] 一类的策略混合方法需要预先假设意图预测与辅助策略的具体形式;当用户意图存在多种可能、且需要在线权衡"现在辅助"与"等更多证据再辅助"时,缺乏一个能显式处理这种不确定性的原则性框架。

## 核心方法
把共享自主问题形式化为部分可观测马尔可夫决策过程(POMDP),用户的真实目标是隐变量;提出"事后优化(hindsight optimization)"作为近似求解这一POMDP的可计算方法,让系统能在多个候选目标间按置信度动态分配辅助力度。

## 关键数据
论文在遥操作和人机协作(teaming)任务上验证了该方法的有效性,是POMDP-based共享自主框架的代表性求解方案。

## 为什么是 milestone
与 [[dragan-2013-policy-blending]] 的策略混合并列为共享自主的两大理论范式之一(概率推断/POMDP路线 vs 策略混合路线),是本领域算法设计空间的重要坐标点,后续包括强化学习路线([[reddy-2018-deep-rl-shared-autonomy]])都在与这两条路线对话。
