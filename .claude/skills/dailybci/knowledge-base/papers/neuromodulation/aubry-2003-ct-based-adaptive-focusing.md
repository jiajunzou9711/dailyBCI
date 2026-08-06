---
title: "Experimental demonstration of noninvasive transskull adaptive focusing based on prior computed tomography scans"
authors: Aubry JF, Tanter M, Pernot M, Thomas JL, Fink M
year: 2003
venue: Journal of the Acoustical Society of America 113:84-93
url: https://doi.org/10.1121/1.1529663
subfield: neuromodulation
tags: [skull-acoustics, adaptive-focusing, phase-aberration, CT-based-simulation, individualized-planning]
---

## 解决了什么问题

颅骨对声束造成**相位与幅度的强烈畸变**，焦点被打散、位置偏移。要在颅内做出可控的焦点，必须逐阵元地补偿这个畸变。此前的补偿方式需要侵入式的参考信号（如在颅内放水听器）。本文问：能否**完全无创**地算出补偿量。

## 核心方法

从**高分辨率 CT** 反推颅骨的声学性质，输入一个考虑颅骨内部全部非均匀性的**三维有限差分**仿真，算出为了在目标点聚焦、各阵元应当发射的信号集合。整套流程随后在实验上验证。

## 关键数据

- 颅骨的声学性质**可以从 CT 影像推得**，并据此完成无创自适应聚焦。
- 完整流程经实验验证。

## 为什么是 milestone

**"基于个体影像做声场仿真与相位校正"这条路线的起点。** 今天所有经颅超声工作的标准动作——用个体解剖影像建头模型、仿真声场、据此定换能器位置与相位、并给出脑内原位剂量估计——都源自这里。

具体到本知识库：[[scott-2026-tus-human-lgn-null]] 用 BabelBrain 配合个体 SimNIBS 头模型与 **ZTE MRI 骨影像**（用能成像骨组织的 MRI 序列替代 CT，避免让健康被试接受辐射）做靶点与剂量仿真；[[martin-2025-256-element-human-lgn]] 的 256 阵元系统同样以个体化规划为前提。[[martin-2024-itrusst-reporting-standards]] 把"脑内原位暴露估计"列为必报项，可行性也建立在这条路线上。

需要记住的边界：**仿真给的是估计值，不是实测。** 不同仿真软件的结果并不一致——[[scott-2026-tus-human-lgn-null]] 就指出 BabelBrain 估计的脑内强度高于另一常用软件 K-Plan。谈剂量时应说明用的是哪套仿真。
