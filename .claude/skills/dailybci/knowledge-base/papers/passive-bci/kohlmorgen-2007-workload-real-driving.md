---
title: "Improving human performance in a real operating environment through real-time mental workload detection"
authors: Kohlmorgen J, Dornhege G, Braun M, Blankertz B, Müller KR, Curio G, Hagemann K, Bruns A, Schrauf M, Kincses W
year: 2007
venue: "Toward Brain-Computer Interfacing (MIT Press), eds. Dornhege et al., pp. 409-422"
url: https://ieeexplore.ieee.org/document/6281209
subfield: passive-bci
tags: [mental-workload, adaptive-assistance, real-driving, EEG, operational-environment, passive-BCI]
---

## 解决了什么问题
passive BCI 的隐式状态解码此前多在实验室受控任务里做。能否在**真实作业环境**(真实道路驾驶)中实时检测驾驶员的高心理负荷,并据此当场调整系统行为、减轻负荷?这关系到 passive BCI 能否走出实验室。

## 核心方法
在真实交通条件下驾驶的被试佩戴 EEG,系统实时估计心理工作负荷(用 EEG 幅度、多个频段的谱功率、多通道特征),据此在负荷高时削减车载电子系统涌入的信息流(如推迟次要提示),从而缓解负荷。作者强调需要高度自适应的方法来应对神经生理信号的个体内/个体间波动。

## 关键数据
- 在真实驾驶(人类 EEG)中实时检出高工作负荷,并即时用于调整信息呈现时机以降低负荷。
- 属最早在真实操作环境里闭环运行的工作负荷型 passive BCI 之一。

## 为什么是 milestone
把工作负荷型 passive BCI 从实验室推进到真实作业环境,证明隐式状态自适应可以在生态效度高的场景中运行,为后续操作环境部署(Aricò 2016 空管自适应自动化)开路。
