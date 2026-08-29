---
title: "Brain specificity of diffuse optical imaging: improvements from superficial signal regression and tomography"
authors: Gregg NM, White BR, Zeff BW, Berger AJ, Culver JP
year: 2010
venue: Front Neuroenergetics 2:14
url: https://doi.org/10.3389/fnene.2010.00014
subfield: non-invasive
tags: [浅层信号回归, 脑特异性, HD-DOT, 方法学, 里程碑]
---

## 解决了什么问题

光学脑成像最根本的干扰：光子从源走到探测器必须两次穿过头皮与颅骨，这些浅层组织自己也有血流动力学波动(心跳、呼吸、Mayer 波、头皮血管张力)，且离探测器更近、贡献更大。**脑信号常被浅层信号盖住**——这是 [[villringer-1993-first-human-fnirs-activation]] 起就一直存在的问题。

## 核心方法

在成人人体数据上评估两条相互独立的改善路径：
1. **浅层信号回归**——原本用于稀疏阵列(靠不同源-探测器间距分离深浅)，这里把它改造到 HD-DOT 阵列上：用**多个短间距通道的平均**作为浅层估计，从深采样通道里回归掉。
2. **层析的深度分层**——DOT 的三维重建原则上就应当把不同深度的组织分开。检验它能否单独把浅层伪迹消干净。

## 关键数据

- 两种方法各自都降低噪声、提高成像一致性与血流动力学响应的可重复性。
- 关键结论：两者是**协同的**，一起用比任何一个单用都好——即层析的深度分层**没有**单独把浅层伪迹消干净。

## 为什么是 milestone

指认了这条线上一个容易被想当然的假设：**"做了三维层析重建"不等于"浅层污染已经解决"**。它把浅层回归确立为 HD-DOT 处理流程里的常规步骤，而不是稀疏 fNIRS 的遗留补丁。评估任何光学脑成像结果时，这条对应的核查问题是：报告的激活有没有做浅层回归，还是只靠重建来"自然分层"。
