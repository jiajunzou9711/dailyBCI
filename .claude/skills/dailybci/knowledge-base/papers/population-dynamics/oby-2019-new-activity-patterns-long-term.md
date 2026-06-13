---
title: "New neural activity patterns emerge with long-term learning"
authors: Oby, Golub, Hennig, Degenhart, Tyler-Kabara, Yu, Chase, Batista
year: 2019
venue: PNAS (116:15210–15215)
url: https://doi.org/10.1073/pnas.1820296116
subfield: population-dynamics
tags: [neural-manifold, BCI-learning, outside-manifold, long-term-learning, plasticity, macaque]
---

## 解决了什么问题
[[sadtler-2014-neural-constraints-learning]] 显示流形**外**的模式在单次实验里学不会。但这是绝对的天花板，还是只是时间不够？如果给足训练时间，神经群体能否长出流形外的新活动模式？这关系到学习的根本极限。

## 核心方法
在恒河猴皮层内 BCI 上施加**流形外（outside-manifold）扰动**，但把训练从单日延长到**多日/多周**，持续追踪群体活动结构随训练的变化，观察是否出现原流形中不存在的新协方差模式。

## 关键数据
- 经过**长期（多日）训练**，猴子确实**长出了新的神经活动模式**——原本流形外、学不会的模式逐渐变得可生成。
- 与流形内的即时学习相比，流形外学习**慢得多**，需要网络结构层面的重塑而非简单重配。

## 为什么是 milestone
补上了流形约束学习的"另一半"：流形外并非绝对禁区，而是**需要长期可塑性**才能突破。把 [[sadtler-2014-neural-constraints-learning]] 的"短期约束"与真正的长期学习区分开，定义了"快=流形内重配 / 慢=流形外重塑"这一对核心对照——也是评估 2026 Yale 人类 fMRI 结果（<1 小时即学会，故属流形内）时必须对照的基准。
