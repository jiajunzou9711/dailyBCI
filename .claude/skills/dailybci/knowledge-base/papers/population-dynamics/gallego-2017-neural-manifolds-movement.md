---
title: "Neural Manifolds for the Control of Movement"
authors: Gallego, Perich, Miller, Solla
year: 2017
venue: Neuron (94:978–984, Perspective)
url: https://doi.org/10.1016/j.neuron.2017.05.025
subfield: population-dynamics
tags: [neural-manifold, population-dynamics, neural-modes, motor-control, review, framework]
---

## 解决了什么问题
运动皮层的功能长期以单神经元调谐（tuning）来描述，但单细胞视角难以解释群体层面的协同结构。领域需要一个统一的概念框架，把"成百上千神经元如何协同产生运动"讲清楚。

## 核心方法
系统提出并梳理**神经流形（neural manifold）/ 神经模式（neural modes）**框架：群体神经活动并非在全维空间自由变化，而是被约束在一个低维流形上；行为由少数潜在"神经模式"的时间演化（latent dynamics）驱动，而非单个神经元的独立放电。综述用降维（如 PCA/因子分析）方法说明如何从群体记录中提取这些模式，并论证流形是理解运动产生、学习与稳定性的恰当层次。

## 关键数据
- 属 Perspective/框架综述，核心贡献是概念与方法论统一，而非单一实验数字。
- 确立"latent dynamics 在低维流形上演化"作为后续大量实证工作的共同语言。

## 为什么是 milestone
为整条神经流形研究线提供了**定义性的术语与框架**，让 [[sadtler-2014-neural-constraints-learning]] 的"流形约束学习"、[[gallego-2020-long-term-stability-dynamics]] 的"流形长期稳定"等结果能被放进同一套语言里讨论。是理解"为什么 BCI 学习、稳定性要从群体流形而非单神经元层面看"的入门坐标。
