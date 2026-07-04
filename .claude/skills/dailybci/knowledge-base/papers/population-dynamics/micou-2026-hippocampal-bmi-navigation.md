---
title: "Distinct hippocampal codes emerge during brain-machine interface navigation"
authors: Micou C, Ho LC, O'Leary T, Krupic J
year: 2026
venue: bioRxiv (preprint)
url: https://doi.org/10.64898/2026.05.11.724143
subfield: population-dynamics
tags: [hippocampus, CA1, brain-machine-interface, closed-loop, navigation, place-cells, calcium-imaging, virtual-reality]
---

## 解决了什么问题
海马 CA1 位置细胞通常在动物主动运动时被记录,这让研究者看到"空间如何被表示",但很难测试一个更强的问题:如果 CA1 活动本身实时改变外界反馈,位置地图会如何重组? 这篇把海马活动接入闭环 BMI,让 CA1 群体活动直接推动虚拟环境前进,用因果操纵来反问海马空间表征。

## 核心方法
小鼠在 400 cm 一维虚拟轨道中导航,奖励位置在 250 cm。作者用双光子钙成像以 30 Hz 记录 250-500 个背侧 CA1 神经元,用 SVM 解码器从单帧活动预测 10 个 40 cm 空间 bin,再把解码位置映射成虚拟环境前进速度。实验比较三种控制关系:跑轮控制、CA1-BMI 闭环控制、autopilot 被动播放;其中 autopilot 让虚拟环境按预设速度移动,跑轮和 CA1 活动都不控制移动。

## 关键数据
- **规模:** 11 只小鼠、50 个 session,Fig. 3 汇总 18,902 个神经元。
- **旧地图不足以直接控制 BMI:** 用跑轮阶段训练的解码器接入 CA1-BMI 后表现下降;用 BMI 阶段活动重新训练后,闭环控制恢复。
- **CA1 地图出现新旧并行:** Fig. 3 将细胞分为 stable、transient、modulated、no field、superposed、other;superposed 细胞占 3.1% (586/18,902),可在跑轮和 BMI 中形成两个位置场,回到跑轮后两个位置场可同时出现。
- **autopilot 对照收紧因果解释:** 被动视觉运动和跑轮/视觉不匹配不足以复制同样的 superposition 模式;关键差别在于 CA1 活动是否曾经控制下一刻外界反馈。

## 为什么是 milestone
这篇把 BCI 从"读出海马地图"推进到"改变海马活动与外界反馈的因果关系",为 hippocampal BMI 提供了一个清晰范式:让 CA1 进入闭环控制,再观察空间表征如何适应新的行动-感觉关系。它与 [[sadtler-2014-neural-constraints-learning]]、[[devicente-2026-circuit-specific-volitional-learning]] 同属"用闭环接口测试大脑学习规则"的路线,但问题焦点从运动皮层/CA3 的群体学习动力学转向 CA1 位置细胞地图的重组。
