---
title: "Electrical stimulation of the spinal cord: two-dimensional finite element analysis with particular reference to epidural electrodes"
authors: Coburn B
year: 1980
venue: Medical & Biological Engineering & Computing
url: https://doi.org/10.1007/BF02443129
subfield: neuromodulation
tags: [spinal-cord-stimulation, finite-element-model, epidural, dorsal-column, computational-model]
---

## 解决了什么问题
1970s 末硬膜外脊髓刺激（SCS）已用于镇痛，但"电极放哪、电流多大会激活哪条通路（背柱 vs 背根）"全靠临床摸索，缺一个能算电场分布的物理模型。

## 核心方法
建立**首个 SCS 有限元（FEM）模型**：在人体胸段中矢状面/横断面上用二维有限元表示非均质电导（脊髓灰/白质、脑脊液、硬膜外脂肪、椎骨），求解硬膜外电极产生的电位场，再结合轴突激活判据估计被募集的纤维。

## 关键数据
- 量化了脑脊液(CSF)层厚度对电场分布的强烈影响——CSF 低阻分流是 SCS 募集背柱 vs 背根的关键解剖变量。
- 给出电极—脊髓距离、电极构型如何改变激活阈值与选择性的首批模型预测。

## 为什么是 milestone
整条 SCS 计算建模线的起点。它把"刺激选择性"从经验问题变成可计算的电场—解剖问题，后续 3D、个体化模型（[[capogrosso-2013-epidural-stim-model]]、[[rowald-2022-spatiotemporal-epidural]]）都是在它确立的范式上加真实度。系统综述（Liang et al. 2023, Neuromodulation）把它列为该谱系的 2D 元祖。
