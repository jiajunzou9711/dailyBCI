---
title: "Activity-dependent spinal cord neuromodulation rapidly restores trunk and leg motor functions after complete paralysis"
authors: Rowald A, Komi S, Demesmaeker R, Baaklini E, Hernandez-Charpak SD, Paoles E, et al. (Courtine G, Bloch J)
year: 2022
venue: Nature Medicine
url: https://doi.org/10.1038/s41591-021-01663-5
subfield: neuromodulation
tags: [spinal-cord-stimulation, patient-specific, spatiotemporal, current-steering, SCI, locomotion]
---

## 解决了什么问题
此前硬膜外刺激恢复行走的电极/程序多靠通用模板，针对每位完全性脊髓损伤(SCI)患者的解剖差异调参慢、起效迟。需要个体化、能快速靶向到特定躯干/腿运动池的刺激方案。

## 核心方法
**MRI/CT 个体化解剖建模 + 软件电流 steering**：为每位患者重建脊髓与背根三维解剖，用计算模型把刺激编排映射到目标脊髓节段，配合专为腰骶段背根优化布局的桨状电极阵列。在多触点上按时空序列分配电流，靶向激活产生特定运动（站、走、踏步、躯干稳定）的背根入髓区。

## 关键数据
- 3 名完全性 SCI 患者植入当天即可在刺激下产生靶向运动，**1 天内**恢复站立/行走/游泳/骑车等活动相关运动（人体，N=3）。
- 个体化建模 + 优化电极使所需调参时间大幅缩短，刺激编排可按活动切换。

## 为什么是 milestone
临床级**current-steering**的标杆：把 [[capogrosso-2013-epidural-stim-model]] 的建模引擎推到 MRI 个体化 + 软件可编程电流分配，证明"模型驱动的空间选择性刺激"能在人体快速起效。它代表了用**多触点电流编排**（而非把焦点推向深部）实现选择性的临床路线，与本期 ACM 的"深部聚焦"路线构成同一目标下的不同技术取舍——共时横向对照。承接 locomotion 库的 [[lorach-2023-brain-spine-interface-human]]。
