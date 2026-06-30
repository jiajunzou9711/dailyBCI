---
title: "Multichannel Blind Source Separation Using Convolution Kernel Compensation"
authors: Holobar, A., Zazula, D.
year: 2007
venue: IEEE Transactions on Signal Processing 55(9):4487-4496
url: https://doi.org/10.1109/TSP.2007.896108
subfield: emg-motor-unit
tags: [CKC, blind-source-separation, decomposition, HD-sEMG, methods]
---

## 解决了什么问题
表面肌电是众多运动单位动作电位序列与各自波形卷积叠加的混合信号。要无创读出单个运动单位的放电时刻，必须从这团混合中把各源分离出来——这是个欠定的卷积盲源分离难题。

## 核心方法
提出 **卷积核补偿(Convolution Kernel Compensation, CKC)**：不去显式估计每个运动单位的波形(混合矩阵)，而是直接重建各源的**放电脉冲序列(spike train)**。通过补偿卷积核，CKC 可在通道数有限、源数远多于通道的情况下稳健地恢复运动单位放电时刻，特别适配高密度表面肌电(HD-sEMG)。

## 关键数据
方法学论文(IEEE TSP 55(9):4487–4496)。CKC 及其梯度版本(gCKC)成为 HD-sEMG 运动单位分解的核心引擎，能并发分解出数十个运动单位的放电序列，并经双源验证(同步针电极)确认准确性。

## 为什么是 milestone
CKC 是让"无创读出单运动单位放电"在实践中可行的关键算法突破，把 [[deluca-1994-common-drive]] 的神经驱动概念变成**可从体表测量的量**。它是后续 [[negro-2016-convolutive-bss-decomposition]] 通用卷积盲源分解框架与今日候选所用 openhdemg 工具链的直接技术祖先；也使 [[farina-2017-manmachine-interface-motor-neurons]] 把放电时序当控制命令成为可能。
