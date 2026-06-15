---
title: "Electroencephalography-Based Auditory Attention Decoding: Toward Neuro-Steered Hearing Devices"
authors: Geirnaert, Vandecappelle, Alickovic, de Cheveigné, Lalor, Meyer, Miran, Francart, Bertrand
year: 2021
venue: IEEE Signal Processing Magazine
url: https://doi.org/10.1109/MSP.2021.3075932
subfield: non-invasive
tags: [auditory-attention, review, benchmark, MESD, neuro-steered-hearing]
---

## 解决了什么问题
AAD 算法繁多（线性 stimulus-reconstruction、CCA、CSP、深度学习等），但缺一个统一、统计可靠的横向比较，以及面向实际应用（神经导向增益控制）的性能指标。各文用不同数据集、不同窗长、不同指标，难以判断谁更好。

## 核心方法
系统综述 + 统计严谨的对比研究：在公开数据集上横评主流 AAD 算法，分析信号处理层面的核心挑战，并提出面向 neuro-steered gain control 的可解释指标 **MESD（minimal expected switch duration）**，把"准确率—窗长"权衡折算成一个有实际意义的量。

## 关键数据
- 给出各类 AAD 算法在统一条件下的横向基准与权衡。
- MESD 提供单一可比指标，衡量系统跟随注意切换的实际时延。

## 为什么是 milestone
该领域的定义性综述与基准框架，统一了术语、数据集与评估方式，是 AAD 研究的标准参照（本知识库这条 AAD 线即从其参考文献中抽取 milestone）。类似 [[wolpaw-2002-bci-review]] 之于整个 BCI 领域的奠基地位。下游实用化工作见 [[geirnaert-2022-unsupervised-time-adaptive-aad]]。
