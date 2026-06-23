---
title: "Classifying intracortical brain-machine interface signal disruptions based on system performance and applicable compensatory strategies: a review"
authors: Dunlap, Colachis IV, Meyers, Bockbrader, Friedenberg
year: 2020
venue: Frontiers in Neurorobotics
url: https://doi.org/10.3389/fnbot.2020.558987
subfield: performance-variability
tags: [performance-variability, intracortical, microelectrode-array, signal-instability, decoder-robustness, compensatory-strategies, review]
---

## 解决了什么问题
慢性植入的皮层内微电极阵列(MEA)处在动态的体内环境中,短暂或系统性的干扰会破坏神经记录、拖累 BMI 性能。此前对植入失效的分类(生物/材料/机械)讲清了"病因",但不利于判断"对 BMI 功能影响多大、能否补偿"。本文提出一个面向影响与补偿的互补分类框架。

## 核心方法
综述(人类皮层内 BMI 为主)。按"对性能的影响时长 + 是否需要/响应干预",把皮层内记录干扰分为四类,并系统回顾各类已报告的干扰来源与对应的算法/工程补偿手段。

## 关键数据
- 四类干扰框架:(1) 瞬时(transient)——分钟到小时级、可自行消退;(2) 可逆(reversible)——持续但可经适当干预修复;(3) 不可逆但可补偿(irreversible compensable)——信号持续/渐进下降但可用算法缓解;(4) 不可逆不可补偿(irreversible non-compensable)——永久丢失、无法补救。
- 补偿策略按类给出:鲁棒解码特征、数据增强、自适应模型、专门的参考方式(瞬时);统计过程控制识别可修复干扰;阻抗谱等在体诊断指导特征选择(不可逆)等。

## 为什么是 milestone
它给皮层内 BCI 的"性能变异"提供了一套以影响与补偿为中心的通用语言,把零散的失效现象组织成可操作的工程框架,是皮层内侧的定义性综述。注意:本文聚焦电极/信号层面的物理-生物干扰;而"瞬时干扰里包含的认知/生理状态波动"这一支,正是 [[perge-2013-intraday-signal-instabilities]]、[[downey-2018-intracortical-recording-stability]] 以及今日候选(在 iBCI 里操纵注意负荷)要往神经状态方向深挖的部分。非侵入侧综述见 [[niu-2025-cognitive-state-eeg-bci-review]]。
