---
title: "High-performance neuroprosthetic control by an individual with tetraplegia"
authors: Collinger, Wodlinger, Downey, Wang, Tyler-Kabara, Weber, McMorland, Vinjamuri, Crammond, Schwartz
year: 2013
venue: Lancet
url: https://doi.org/10.1016/S0140-6736(12)61816-9
subfield: motor-bci
tags: [7-DOF, robotic-arm, tetraplegia, high-dimensional-control, Schwartz, Pittsburgh]
---

## 解决了什么问题
Hochberg 2012 实现了人类 3D reach-and-grasp，但控制维度有限。日常活动需要手臂在三维空间中平移、旋转手腕、并控制抓握——总共 7 个自由度。能否从运动皮层解码出如此高维度的运动控制信号？

## 核心方法
在一名 52 岁脊髓小脑变性导致的四肢瘫患者运动皮层植入两个 96 通道 Utah 阵列，解码神经信号控制 Johns Hopkins APL 开发的模块化假肢（Modular Prosthetic Limb），具备 7 个自由度：3D 平移 + 3D 腕部旋转 + 1D 抓握。训练 13 周后，患者可执行复杂的协调动作。

## 关键数据
- 7 个自由度的同步控制
- 仅 13 周训练即达到高性能
- 在 Action Research Arm Test 中表现显著优于随机
- 患者可执行如拿起小物体、调整手腕角度等精细操作

## 为什么是 milestone
将 motor BCI 的控制复杂度推向新高——7 自由度接近人类手臂的自然运动能力。证明运动皮层包含的信息远比之前 BCI 利用的要丰富得多，关键在于解码算法能否提取。同时 13 周即达到高性能的训练速度表明，高维 BCI 控制并不需要漫长的学习过程。
