---
title: "Long-term stability of neural prosthetic control signals from silicon cortical arrays in rhesus macaque motor cortex"
authors: Chestek, Gilja, Nuyujukian, Foster, Fan, Kaufman, Churchland, Rivera-Alvidrez, Cunningham, Ryu, Shenoy
year: 2011
venue: Journal of Neural Engineering
url: https://doi.org/10.1088/1741-2560/8/4/045005
subfield: invasive-recording
tags: [chronic-stability, signal-degradation, threshold-crossing, multiunit, Utah-array, Shenoy-lab]
source_review: "Brain–Computer Interfaces with Intracortical Implants (PMC 2024 review context); Annual Reviews 2025 ref 47 context"
---

## 解决了什么问题
Utah阵列植入后，单个神经元的信号质量会随时间下降——但这种退化到底有多严重？是否意味着长期BCI不可行？不同的信号提取策略（sorted units vs. threshold crossings）对长期性能有什么影响？

## 核心方法
在3只猕猴的运动皮层植入4个Utah阵列，持续记录9.4、10.4和31.7个月。系统量化action potential振幅、sorted单元数量、threshold crossing数量随时间的变化，并评估离线解码器性能的长期稳定性。

## 关键数据
- Action potential振幅平均每月衰减2.4%
- Sorted单元数量持续下降
- 但threshold crossing（未分选spike）的解码性能在前2个月无显著损失
- 一个阵列在该期间后继续成功用于在线假肢实验超过1年
- 记录跨度达31.7个月

## 为什么是 milestone
首次系统量化了intracortical慢性记录的信号退化规律，并提出了关键的实践策略：用threshold crossing（multiunit activity）替代sorted single units，可以大幅提高长期BCI的鲁棒性。这一发现直接改变了BrainGate等临床BCI系统的信号处理策略——从追求"完美的单神经元分选"转向"阈值过阈的multiunit计数"，大大延长了BCI的有效使用寿命。
