---
title: "Neural networks and physical systems with emergent collective computational abilities"
authors: Hopfield
year: 1982
venue: Proceedings of the National Academy of Sciences USA 79:2554–2558
url: https://doi.org/10.1073/pnas.79.8.2554
subfield: population-dynamics
tags: [Hopfield-network, attractor, content-addressable-memory, associative-memory, Ising-model, energy-function, Hebb-rule, theory, forward-problem]
---

## 解决了什么问题
由大量简单的二值神经元组成的网络，能否作为集体性质，实现内容可寻址记忆（content-addressable memory）：只给出一段记忆的部分内容，网络能否恢复出完整的那段记忆。

## 核心方法
二值神经元，每个神经元随机、异步地比较输入之和与阈值，再更新自身状态；连接强度按存储的模式以 Hebb 型规则设定。在 T_ij 对称的条件下定义能量 E，并证明异步更新使 E 单调下降，直到停在局部极小；存储的记忆对应这些极小点。用计算机模拟检验存储容量与提取效果。

## 关键数据
- T_ij 对称时，异步更新使 E 单调下降，直到到达（局部）极小；作者写明这一情形与 Ising 模型同构（isomorphic）。
- 约 0.15 N 个状态可以同时被记住，超过后提取误差迅速增加。
- 与 Little 1974 的同步更新模型只有「有限的形式相似」（limited formal similarity）。
- 非对称的 T_ij 也被讨论：可能导致网络不停在极小点。

## 为什么是 milestone
确立了「记忆是能量极小点（吸引子）」这一网络层面的框架，使统计力学方法可以用于神经网络的记忆问题。它属于正问题：J 由人按存储规则设定，结论来自推导与模拟，不拟合神经数据。后续工作：Amit、Gutfreund & Sompolinsky 1985 用统计力学算出容量约 0.138 N；Wills et al. 2005（大鼠海马）报告离散吸引子样的位置细胞切换；Ramsauer et al. 2020 指出现代 Hopfield 网络的更新规则等价于 Transformer 注意力；2024 年诺贝尔物理学奖授予 Hopfield 与 Hinton。引用时注意：纯理论与模拟、无实验数据；对称连接与真实突触不对应。

## 本项目使用
series-ising-01 第一期（2026-10-25）导语与卡 7「第一条线」代表工作；第二期主体。
