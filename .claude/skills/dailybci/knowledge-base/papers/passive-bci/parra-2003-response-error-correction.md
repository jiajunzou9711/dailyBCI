---
title: "Response error correction — a demonstration of improved human-machine performance using real-time EEG monitoring"
authors: Parra LC, Spence CD, Gerson AD, Sajda P
year: 2003
venue: IEEE Transactions on Neural Systems and Rehabilitation Engineering 11(2):173-177
url: https://doi.org/10.1109/TNSRE.2003.814446
subfield: passive-bci
tags: [error-related-negativity, ERN, single-trial, EEG, human-machine-performance, passive-BCI]
---

## 解决了什么问题
人机交互中操作者会犯错,而大脑在察觉自己犯错时会产生错误相关负波(ERN,error-related negativity)。此前 ERN 多在事后平均信号里研究,能否**单试次**实时检出、并用它当场纠正操作者的错误,尚未在闭环里证明。

## 核心方法
在一个视觉辨别任务中,用自适应线性预处理 + 分类算法对单试次 EEG 做实时检测,把检出的 ERN 当作"操作者自认为答错了"的估计;一旦检出,系统自动翻转/纠正该次响应。这是把内源错误信号作为隐式输入、无需用户额外指令的早期演示(passive BCI 的前身范式)。

## 关键数据
- 通过自动纠错,受试者整体绩效**平均提升约 21%**(人类 EEG)。
- 证明 ERN 可在单试次层面实时解码并即刻用于改善人机绩效。

## 为什么是 milestone
最早在闭环里把"读取内源错误信号→当场纠错"跑通的工作之一,是 Ferrez & Millán (2008) 交互错误电位、以及 Zander (2016) 神经自适应闭环的直接前驱,奠定 passive BCI"利用隐式脑状态增强人机绩效"的可行性。
