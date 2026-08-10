---
title: "Multi-electrode stimulation evokes consistent spatial patterns of phosphenes and improves phosphene mapping in blind subjects"
authors: Oswalt D, Bosking W, Sun P, Sheth SA, Niketeghad S, Salas MA, Patel U, Greenberg R, Dorn J, Pouratian N, Beauchamp M, Yoshor D
year: 2021
venue: Brain Stimulation 14(5):1356–1372
url: https://pubmed.ncbi.nlm.nih.gov/34482000/
subfield: visual-prosthesis
tags: [cortical-visual-prosthesis, phosphene-mapping, blind-humans, calibration, Second-Sight, Orion]
---

## 解决了什么问题
皮层视觉假体要工作，必须先知道**每个电极对应视野中的哪个位置**（光幻视映射 / phosphene mapping）。这一步是所有后续编码的前提，但在盲人身上做映射远比在明眼人身上难——盲人没有视觉参照来指认光点在哪。

## 核心方法
对 **5 名盲人与 15 名明眼**被试的视皮层植入电极施加刺激，比较两组变量：① 固视策略——单手（一根食指按在触觉固视点）vs 双手（右手食指叠在左手食指上）；② 映射方式——**绝对映射**（每试次只刺激一个电极）vs **相对映射**（每试次刺激 3–5 个光幻视组成的序列）。

## 关键数据
- 盲人被试的映射精度**显著差于明眼被试**（2DRMS，16 ± 2.9° vs 1.9 ± 0.93°；t(18)=18，p<0.001）。
- 盲人被试中，**双手固视比单手固视稳定得多**：BS1 为 4.0 ± 2.6° vs 19 ± 4.7°（t(79)=24，p<0.001）；BS2 为 4.1 ± 2.0° vs 12 ± 2.7°（t(65)=19，p<0.001）。
- 多点相对映射的基线精度与绝对映射相当（BS1：4.7 ± 2.6° vs 3.9 ± 2.0°；BS2：4.1 ± 2.0° vs 3.2 ± 1.1°），但在扣除试次间的整体平移变异后显著改善。

## 为什么是 milestone
把**标定**这件事本身当成研究对象，而不是当作实验前的杂活。三个结论对临床部署直接有用：盲人映射误差比明眼人大近一个数量级（说明明眼人数据会系统性高估假体可达精度）；**误差的一大部分来自本体感觉固视不稳而非神经端**，靠改固视姿势就能把 19° 降到 4°；试次间的平移变异可以事后扣除。这条"逐电极手工标定既费力又不准"的结论，正是今日候选工作要用深度学习取代的对象。作者名单里有 Second Sight Medical Products（Orion 皮层假体的厂商）人员，属产学合作。
