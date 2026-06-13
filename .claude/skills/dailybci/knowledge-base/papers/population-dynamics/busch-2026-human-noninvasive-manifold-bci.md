---
title: "Human learning of a noninvasive brain–computer interface via manifold geometry"
authors: Busch, Fincke, Lajoie, Krishnaswamy, Turk-Browne
year: 2026
venue: Nature Neuroscience (preprint bioRxiv 2025.03.29.646109)
url: https://doi.org/10.1101/2025.03.29.646109
subfield: population-dynamics
tags: [neural-manifold, BCI-learning, noninvasive, fMRI, T-PHATE, within-manifold, outside-manifold, human]
---

## 解决了什么问题
BCI 落地的一个现实障碍是用户学会控制它要花很久，过去基于实时 fMRI 的无创 BCI 往往需要多次训练、效果有限，且存在始终学不会的"non-responder"。本研究问的是更底层的问题：是不是大脑活动本身的几何结构，决定了哪些控制映射"好学"、哪些"再练也学不会"——并且这条原本只在动物皮层内验证过的规律，能否在人类、无创条件下成立。

## 核心方法
18 名健康成年人在实时 fMRI 下，通过自我调节与空间导航相关脑区的活动模式来操控一个 avatar 在虚拟导航游戏中移动（脑控信号每 ~2 s 更新一次）。用为 fMRI 优化的 **T-PHATE**（data-diffusion 降维）提取每个被试的低维**内在流形**。随后改变"脑活动→avatar 运动"的映射，制造三种条件：**IM（直觉映射）**贴合流形主方向；**WMP（流形内扰动）**换到流形内另一个仍高解释度的方向；**OMP（流形外扰动）**要求流形外、几乎不解释变异的方向。每个被试完成 4–5 次、每次 1–1.5 小时的 session 比较三者的可学习性。

## 关键数据
- 总体脑控提升（ΔBrainControl，从首到末试次）：**IM = 49.3**（P<0.0001）、**WMP = 16.4**（P=0.0002）、**OMP = −0.4**（P=0.556，不显著）。
- 两两差异均显著：IM > WMP、IM > OMP（均 P<0.001），WMP > OMP（P=0.002）。
- IM/WMP 在**单次 1–1.5 小时 session 内**即学会；OMP 同样训练量下学不会。
- 学习伴随神经层面的**沿流形重对齐**与任务信息解码增强。

## 为什么是 milestone
首次在**人类、无创（fMRI）** 条件下验证 [[sadtler-2014-neural-constraints-learning]] 在恒河猴皮层内发现的"流形约束学习"定律——流形内可学、流形外短期不可学。学得快的 IM/WMP 对应 [[golub-2018-learning-neural-reassociation]] 的"重配已有模式"，学不会的 OMP 对应 [[oby-2019-new-activity-patterns-long-term]] 的"流形外需长期重塑"。它把整条神经流形学习研究线从动物侵入式延伸到人类无创式，并提出一个可操作的 BCI 设计思路：先测量个体内在流形、再挑一个"本来就好学"的映射，而非强训练用户适应解码器。待解问题：这套基于慢、全局 fMRI 的几何能否迁移到快、局部的电极信号。
