---
title: "Neural constraints on learning"
authors: Sadtler, Quick, Golub, Chase, Ryu, Tyler-Kabara, Yu, Batista
year: 2014
venue: Nature (512:423–426)
url: https://www.nature.com/articles/nature13665
subfield: population-dynamics
tags: [neural-manifold, BCI-learning, intracortical, motor-cortex, within-manifold, macaque]
---

## 解决了什么问题
学习（运动/感觉/认知）需要神经元群体产生新的活动模式。一个长期未解的问题是：是不是**所有**新模式都同样容易学会？还是说既有神经网络的结构本身限制了哪些模式可被快速生成？此前缺少能直接、因果地检验这一点的范式。

## 核心方法
在恒河猴上用**闭环皮层内 BCI** 作为可控的学习范式：猴子通过调制初级运动皮层（M1）的群体活动来控制光标。先用记录到的群体活动拟合出其低维**内在流形（intrinsic manifold）**——即神经活动自然covary的几何结构。然后人为改变解码映射（decoder），制造两类扰动：① **within-manifold**（要求的新活动模式仍落在流形内）；② **outside-manifold**（要求流形外、不符合既有协方差结构的模式）。比较两类扰动下猴子能否、以及多快学会恢复控制。

## 关键数据
- **流形内（within-manifold）扰动**：猴子能在**单次实验（数小时）内**学会，恢复接近原有的控制水平。
- **流形外（outside-manifold）扰动**：同样时间内**学不会**——神经群体难以即时生成不符合既有协方差结构的活动模式。
- 学习表现为把已有活动模式重新调配，而非凭空产生全新的协方差结构。

## 为什么是 milestone
首次用因果实验证明：**既有神经网络的结构约束了它能快速学会什么**——容易学的是落在内在流形内的模式，流形外的模式则受限。这把"神经流形"从描述性概念提升为对学习有**预测力的约束**，奠定了后续 [[golub-2018-learning-neural-reassociation]]（流形内学习机制）与 [[oby-2019-new-activity-patterns-long-term]]（流形外的长期可塑）整条研究线，也是 2026 年 Yale 把同一原理搬到人类无创 fMRI 的直接前作。
