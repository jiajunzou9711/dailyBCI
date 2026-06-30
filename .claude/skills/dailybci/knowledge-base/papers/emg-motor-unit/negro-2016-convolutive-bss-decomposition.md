---
title: "Multi-channel intramuscular and surface EMG decomposition by convolutive blind source separation"
authors: Negro, F., Muceli, S., Castronovo, A. M., Holobar, A., Farina, D.
year: 2016
venue: Journal of Neural Engineering 13(2):026027
url: https://doi.org/10.1088/1741-2560/13/2/026027
subfield: emg-motor-unit
tags: [decomposition, convolutive-BSS, gCKC, benchmark-method, validation, open-source]
---

## 解决了什么问题
此前 HD-sEMG 运动单位分解方法各异、可及性差,缺一个通用、可验证、可被社区直接使用的标准流程。本文给出统一的卷积盲源分解框架并广泛验证,成为当代事实标准方法。

## 核心方法
通用卷积盲源分解:先对多通道(表面或针内)EMG 做**卷积白化(convolutive sphering)**,再迭代提取各源——基于梯度卷积核补偿(gCKC)逐个恢复运动单位放电序列。论文明确给出卷积盲分离模型成立的条件,并用同步针内 EMG 做双源验证评估分解准确性。

## 关键数据
方法学论文(J. Neural Eng. 13(2):026027)。可并发分解出数十个运动单位;经双源(iEMG vs sEMG)验证放电一致性高。该方法被开源实现并广泛采用,是 openhdemg 等社区工具链的算法核心。

## 为什么是 milestone
这是把 [[holobar-2007-convolution-kernel-compensation]] 的 CKC 推广成**通用、可验证、社区标准**的运动单位分解方法,让 HD-sEMG 神经驱动研究真正可复现、可扩展。**今日候选用的 openhdemg 工具正源出这条方法学谱系**;它也是把 [[farina-negro-2015-common-synaptic-input]] 的神经驱动框架落到大样本运动单位池实证的技术前提。
