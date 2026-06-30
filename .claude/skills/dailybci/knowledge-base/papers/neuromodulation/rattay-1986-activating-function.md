---
title: "Analysis of models for external stimulation of axons"
authors: Rattay F
year: 1986
venue: IEEE Transactions on Biomedical Engineering
url: https://doi.org/10.1109/TBME.1986.325670
subfield: neuromodulation
tags: [activating-function, axon-stimulation, biophysics, spatial-selectivity, theory]
---

## 解决了什么问题
胞外电极刺激时，到底是哪一段神经、哪些轴突先被激活？此前缺一个能从电场分布直接预测兴奋位点的简洁判据，"刺激选择性"只能靠经验试错。

## 核心方法
把 cable 方程作用在胞外电位上，提出**"激活函数"(activating function)**：沿轴突方向胞外电位的二阶空间导数 ∂²Ve/∂x²，正比于该处膜电位的初始变化率。激活函数为正处去极化（可能产生动作电位），为负处超极化。由此可从任意电极几何 + 组织电场，直接定位最可能起兴奋的轴突段。

## 关键数据
- 激活位点由 ∂²Ve/∂x² 的空间分布决定，而非简单的电位最低点。
- 解释了为什么弯曲、分支或直径变化处更易被激活（这些几何不连续放大二阶导数）。
- 给出阴极/阳极刺激下兴奋与阻断区域的预测框架。

## 为什么是 milestone
激活函数是此后**所有**神经刺激空间选择性建模的理论地基——SCS、DBS、外周神经、ICMS 的有限元 + 轴突模型都以它判断"场会激活谁"。要谈"电流聚焦/选择性 current-steering"（如 [[capogrosso-2013-epidural-stim-model]]、[[struijk-holsheimer-1996-transverse-tripole]]、本期 ACM），都建立在用激活函数预测募集位点之上。与 Dayan & Abbott 体系中胞外场—膜电位耦合的通识一致。
