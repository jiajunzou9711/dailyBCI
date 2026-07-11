---
title: "Coherent plane-wave compounding for very high frame rate ultrasonography and transient elastography"
authors: Montaldo, Tanter, Bercoff, Benech, Fink
year: 2009
venue: IEEE Transactions on Ultrasonics, Ferroelectrics, and Frequency Control 56:489–506
url: https://doi.org/10.1109/TUFFC.2009.1067
subfield: functional-ultrasound
tags: [ultrafast-ultrasound, plane-wave, beamforming, method-enabler]
---

## 解决了什么问题
常规超声成像逐条发射聚焦声束扫描视野,帧率被"扫描线数×往返飞行时间"锁死在几十 Hz 量级,无法捕捉快速的组织力学波或血流动态。已有的超快成像方案改为一次发射一整个平面波,帧率可达每秒数千帧,但发射端不再聚焦、只在接收端做波束合成,图像的分辨率与对比度显著劣化。

## 核心方法
提出**相干平面波复合(coherent plane-wave compounding)**:以若干不同倾角发射平面波,对各角度重建出的低质量图像做**相干**(带相位)叠加,在接收端合成出等效于发射聚焦的图像质量。作者给出对比度、信噪比、分辨率的理论模型,并预测所需发射次数比常规 B 模式少约一个数量级(文中给出"约低 10 倍"的估计),从而在保住高帧率的同时恢复图像质量。

## 关键数据
- 数据采集率可达每秒数千帧(thousands of images per second)量级,支撑实时观察生物组织中传播的剪切波。
- 理论模型预测:达到与常规 B 模式可比的图像质量,所需发射次数约低 10 倍;文中以体模/在体实验验证该预测。
- 论文本身面向瞬态弹性成像,并非神经成像研究。

## 为什么是 milestone
这是 fUS 的**物理前提**,不是神经科学结果。fUS 依赖以千赫兹量级帧率追踪红细胞散射体的微弱多普勒信号,这一点在"逐线扫描"的常规超声下不可能实现。相干平面波复合把"高帧率"与"可用画质"这对矛盾解开,后续 [[mace-2011-functional-ultrasound-brain]] 才可能在 rat 脑上把血容量变化成像出来。凡是讨论 fUS 空间/时间分辨率来源的工作,追溯到底都落在这篇的成像范式上。
