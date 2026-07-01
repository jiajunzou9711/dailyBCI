---
title: "Shared Autonomy via Deep Reinforcement Learning"
authors: Reddy, Dragan, Levine
year: 2018
venue: Robotics: Science and Systems (RSS 2018)
url: https://arxiv.org/abs/1802.01744
subfield: shared-autonomy-bci
tags: [shared-control, deep-reinforcement-learning, end-to-end]
---

## 解决了什么问题
此前的共享自主方法([[dragan-2013-policy-blending]]、[[javdani-2018-hindsight-optimization]])通常需要人工预先设定用户意图空间、动力学模型或奖励结构,难以扩展到意图/环境难以手工建模的复杂场景。

## 核心方法
把共享自主问题转化为可端到端学习的深度强化学习问题:不预先假设用户意图的具体表示或系统动力学模型,而是直接从用户操作行为中学习辅助策略。

## 关键数据
论文在多个仿真与真实机器人任务上验证,证明该方法无需手工设计意图推断模块即可获得有效的共享辅助效果。

## 为什么是 milestone
标志着共享自主的方法论从"手工设计的概率推断/策略混合"转向"数据驱动的端到端学习",是深度学习渗透进共享控制/共享自主领域的代表性节点,为后续把深度学习/AI副驾驶应用到BCI共享控制(如本期候选论文)铺平了方法论道路。
