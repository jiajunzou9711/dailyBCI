---
title: "A model of safe levels for electrical stimulation"
authors: Shannon RV
year: 1992
venue: IEEE Transactions on Biomedical Engineering 39(4):424-426
url: https://en.wikipedia.org/wiki/Shannon_criteria
subfield: sensory-feedback
tags: [stimulation-safety, shannon-equation, charge-density, charge-per-phase, safety-limit, macroelectrode]
---

## 解决了什么问题
[[mccreery-1990-charge-density-charge-per-phase]] 证明了电荷密度与每相电荷协同决定损伤,但临床/工程需要一个**可直接套用的定量边界**,告诉设计者"给定电极面积,刺激强度的上限在哪"。

## 核心方法
把 McCreery 等人的在体损伤数据拟合成一条对数线性边界,提出 **Shannon 方程**:
- k = log(D) + log(Q),其中 D 为电荷密度(µC/cm²·phase)、Q 为每相电荷(µC/phase)。
- 在 log(Q)–log(D) 平面上,k 为一组平行直线;k=1.85 被广泛用作"安全/可能损伤"的经验分界。

## 关键数据
- k=1.85 作为损伤阈值边界:k 值越高,越可能造成组织损伤。
- 该判据**针对宏电极(macroelectrode)**导出——这一前提在微电极时代成为后续争议焦点(见 [[cogan-2016-tissue-damage-thresholds]])。

## 为什么是 milestone
Shannon 方程是刺激安全领域**被引用最广**的判据,几乎所有神经刺激器的安全设计与监管文件都用它划线。它把 McCreery 的双因子实证变成一行可计算的公式,定义了整条线的"安全语言"。局限是源于宏电极、未必外推到 ICMS 这类微电极,这正是当代再评估(Cogan 2016)与今日候选(微气泡 ICMS 安全窗)要补的缺口。
