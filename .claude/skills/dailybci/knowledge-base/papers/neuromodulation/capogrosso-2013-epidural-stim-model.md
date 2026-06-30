---
title: "A Computational Model for Epidural Electrical Stimulation of Spinal Sensorimotor Circuits"
authors: Capogrosso M, Wenger N, Raspopovic S, Musienko P, Beauparlant J, Bassi Luciani L, Courtine G, Micera S
year: 2013
venue: Journal of Neuroscience
url: https://doi.org/10.1523/JNEUROSCI.1688-13.2013
subfield: neuromodulation
tags: [spinal-cord-stimulation, epidural, computational-model, sensorimotor, recruitment, locomotion]
---

## 解决了什么问题
硬膜外刺激恢复运动的机制长期含糊：到底直接激活了什么？需要一个真实 3D 模型回答"硬膜外电极优先募集背根 afferent 还是背柱/运动通路"，才能原则化地设计靶向刺激。

## 核心方法
建立**真实解剖 3D 有限元 + 多房室轴突模型**联合框架（大鼠腰骶段，可推广到人）：FEM 算硬膜外电极电场，轴突模型判募集。系统比较电极位置/极性下背根 afferent、背柱、运动纤维的激活阈值与顺序。

## 关键数据
- 模型预测并经实验验证：硬膜外刺激**优先募集背根大直径 afferent**（而非直接驱动运动神经元），即恢复运动是经感觉传入门控的间接机制。
- 不同电极位点对应不同肌群/脊髓节段的选择性募集，给出"按位置 steering 到目标运动池"的可计算依据。

## 为什么是 milestone
靶向时空硬膜外刺激的**建模引擎**：直接支撑后续 Wagner 2018、Lorach 2023（[[wagner-2018-targeted-epidural-walking]]、[[lorach-2023-brain-spine-interface-human]]，已在 locomotion 库）的电极设计与刺激编排。把 SCS 从经验试错推进到"模型先行"的靶向刺激时代，是 [[coburn-1980-2d-scs-fem]] 之后该谱系的 3D 真实化代表，也是 [[rowald-2022-spatiotemporal-epidural]] 个体化模型的前身。为本期 ACM 的"选择性单肌募集"提供横向对照基准。
