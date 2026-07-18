---
title: "Approach Angle Affects Accuracy in Robotic Stereoelectroencephalography Lead Placement"
authors: Iordanou JC, Camara D, Ghatan S, Panov F
year: 2019
venue: World Neurosurgery
url: https://doi.org/10.1016/j.wneu.2019.04.143
subfield: invasive-recording
tags: [sEEG, robot-assisted, ROSA, approach-angle, skew, implantation-accuracy, human]
---

## 解决了什么问题

机器人辅助 sEEG 的整体精度已经清楚（[[gonzalez-martinez-2016-robot-assisted-seeg]]：靶点误差中位数 1.7 mm），但那是**平均值**。实际规划时外科医生要在具体轨迹上做取舍：为了避开血管或到达深部靶点，有时必须用很斜的进针角度。斜进针会不会更不准？本文把**进针角度**单独拎出来作为变量检验。

## 核心方法

**电极模态：侵入式深部电极（sEEG）**，ROSA 机器人辅助植入（Mount Sinai）。把轨迹按**规划进针角度**分成两组——**斜行组（oblique，>30°）** 与**正交组（orthogonal，<30°）**——比较两组的**径向误差（radial error）**。

## 关键数据

- *World Neurosurg* 128:e322–e328（2019 年 8 月），DOI 10.1016/j.wneu.2019.04.143，PMID 31028981
- **斜行组（>30°）径向误差 2.05 mm vs 正交组（<30°）1.45 mm，P < 0.001**（相差约 41%）
- 作者建议：规划时应避免大偏斜角；若无法避免，须留更大的安全裕度

## 为什么是 milestone

它是这条线上**第一篇把"精度取决于轨迹几何"落成硬数字的工作**——机器人不是一个精度恒定的黑盒，它的误差随进针角度系统性变化。物理机制直白：电极斜着穿过颅骨时，钻头/导管在骨面上更容易打滑（skew），而角度越斜，同样的横向滑移会造成越大的靶点偏移。

这个发现在 2026 年被大规模独立复现：Thurairajah 等在 3176 条轨迹上发现靶点误差与**植入角度**正相关（同时还与头皮厚度、颅骨厚度、轨迹长度正相关，肥胖患者误差更高）——这四个变量其实指向同一个力学图景：**电极在进入脑组织前要穿过的软硬组织越厚、越斜，累积偏移越大**。

对 BCI 的推论：任何要求精确到达特定解剖靶点的植入（深部核团、特定皮层区），其可达精度部分由**该靶点所需的轨迹几何**决定，而不只由设备精度决定。
