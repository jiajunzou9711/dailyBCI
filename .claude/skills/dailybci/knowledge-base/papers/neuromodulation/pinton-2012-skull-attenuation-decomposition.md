---
title: "Attenuation, scattering, and absorption of ultrasound in the skull bone"
authors: Pinton G, Aubry JF, Bossy E, Muller M, Pernot M, Tanter M
year: 2012
venue: Medical Physics 39:299-307
url: https://doi.org/10.1118/1.3668316
subfield: neuromodulation
tags: [skull-acoustics, attenuation, absorption, scattering, mode-conversion, heating, simulation]
---

## 解决了什么问题

"颅骨衰减了多少"是可测的，但衰减由几种完全不同的机制混在一起构成：界面反射、模式转换、微结构散射、真正被吸收转成热。**其中"吸收"这一项此前没有估计值**——而它恰恰是决定颅骨发热的那一项，对安全性直接相关。本文把它们分离开。

## 核心方法

建立骨内波传播的衰减模型，据此写三维时域有限差分数值算法。用**水听器**与**光学外差干涉仪**测声场、**X 射线显微断层扫描**取骨样品的真实微结构来驱动仿真；同时用**红外相机**测声照期间的温升，再经三维热学仿真把温度与吸收联系起来，从而把吸收系数单独解出来。

## 关键数据

总衰减被拆解为四个机制：
1. **流体—骨界面上的反射**；
2. **纵波与横波之间的模式转换**（转成横波的能量基本不再有效传入脑内）；
3. **复杂内部微结构造成的散射**；
4. **被吸收并转化为热的部分**——本文首次给出纵波与横波各自的吸收系数估计。

## 为什么是 milestone

把"颅骨衰减"从一个笼统的数字变成**可分解、可分别建模的四项**。两个实际后果：

**① 讲清了能量去了哪。** 散射与模式转换的那部分能量并未变成热，而是被打乱方向；只有被吸收的那部分才让颅骨升温。谈经颅超声的热安全（[[aubry-2025-itrusst-biophysical-safety]] 的 CEM43 阈值）时，承重的是吸收系数而非总衰减。

**② 给仿真提供了机制层面的依据。** 基于影像的个体化声场仿真（[[aubry-2003-ct-based-adaptive-focusing]] 起头，今天的 BabelBrain、k-Wave 等）要预测脑内剂量，前提是模型里各项损耗机制的参数是对的。

与 [[fry-barger-1978-acoustical-properties-human-skull]] 的分工：那篇定位了**哪一层**主导损耗（板障），本篇拆解了**通过什么机制**损耗。
