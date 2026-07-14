---
title: "Error-related EEG potentials generated during simulated brain-computer interaction"
authors: Ferrez PW, Millán JdR
year: 2008
venue: IEEE Transactions on Biomedical Engineering 55(3):923-929
url: https://pubmed.ncbi.nlm.nih.gov/18334383/
subfield: passive-bci
tags: [interaction-ErrP, error-related-potential, single-trial, EEG, closed-loop, passive-BCI]
---

## 解决了什么问题
BCI 在识别用户意图时必然会出错。能否让系统自己"知道"它刚才理解错了?此前的错误电位研究多针对用户自身操作失误(response ErrP),而 BCI 场景里的错误是**机器误解了正确的用户意图**——这类"交互错误电位(interaction ErrP)"是否存在、能否单试次检出,是把错误监测用于 BCI 自校正的前提。

## 核心方法
在模拟 BCI 交互任务中,当系统给出的反馈与用户实际意图不符时记录 EEG,刻画其错误相关电位波形,并做单试次分类。刻画出的 interaction ErrP 具有额-中央区特征性成分:反馈后约 200 ms、320 ms 两个正峰,约 250 ms 的额-中央负波,以及约 450 ms 更宽的额-中央负偏转。检出的 ErrP 可作为验证信号,过滤掉 BCI 的错误输出。

## 关键数据
- 确立了区别于 response ErrP 的 **interaction ErrP**(人类 EEG),并给出可复现的波形时程与成分。
- 单试次检出的 ErrP 可用于 BCI 输出的自动验证/纠错,提升有效识别正确率。

## 为什么是 milestone
把"错误相关电位"从认知神经科学现象转化为 BCI 的隐式纠错信号,是 passive BCI 读取的核心信号机制之一。后续 neuroadaptive 闭环(Zander 2016 用 mPFC 期望违背信号驱动自适应)正是建立在"机器能实时读出自己被误解/期望被违背"这一机制之上。
