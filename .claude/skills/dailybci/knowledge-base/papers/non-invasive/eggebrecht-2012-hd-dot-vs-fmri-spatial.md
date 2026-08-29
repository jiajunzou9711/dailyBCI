---
title: "A quantitative spatial comparison of high-density diffuse optical tomography and fMRI cortical mapping"
authors: Eggebrecht AT, White BR, Ferradal SL, Chen C, Zhan Y, Snyder AZ, Dehghani H, Culver JP
year: 2012
venue: Neuroimage 61:1120-1128
url: https://doi.org/10.1016/j.neuroimage.2012.01.124
subfield: non-invasive
tags: [HD-DOT, fMRI对照, 定位误差, 头模型, 里程碑]
---

## 解决了什么问题

[[zeff-2007-hd-dot-retinotopy]] 展示了 HD-DOT 的图像与 fMRI 的视网膜拓扑"一致"，但那是定性一致。缺一个**逐体素**的、与金标准 fMRI 在同一批被试上做的定量对照——不做这一步，就无法回答"HD-DOT 的定位能精到什么程度"。

## 核心方法

同一组被试(**n=5**)分别做 HD-DOT 与 fMRI 两次扫描，用匹配的视觉刺激方案。为了让两个图像空间能逐体素配准，实现了**被试特异的头模型**：纳入该被试的 MRI 解剖、细致的组织分割，以及源/探测器实际位置的配准。

## 关键数据

- 视觉响应的平均定位误差 **4.4 ± 1 mm**。
- 该误差**显著小于皮层脑回之间的平均距离**——这是判断"够不够用"的参照，而不是与某个绝对阈值比。
- 样本：人体 n=5。

## 为什么是 milestone

给出了这条线最常被引用的一个承重数字，并把它挂在一个可解释的物理参照上(脑回间距)。同时确立了**被试特异头模型**是 HD-DOT 定位精度的必要条件——光在头里的传播路径依赖具体解剖，用通用头模型会引入系统性偏移。后续任何声称"接近 fMRI 定位精度"的光学工作，都应先核它用的是被试自己的解剖还是模板。
