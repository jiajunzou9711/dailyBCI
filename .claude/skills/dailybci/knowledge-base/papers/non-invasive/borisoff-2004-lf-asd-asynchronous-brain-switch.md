---
title: "Brain-Computer Interface Design for Asynchronous Control Applications: Improvements to the LF-ASD Asynchronous Brain Switch"
authors: Borisoff JF, Mason SG, Bashashati A, Birch GE
year: 2004
venue: IEEE Transactions on Biomedical Engineering
url: https://doi.org/10.1109/TBME.2004.827078
subfield: non-invasive
tags: [asynchronous-BCI, brain-switch, idle-state, EEG]
---

## 解决了什么问题
早期"脑开关(brain switch)"类异步BCI需要在用户完全没有外部提示(cue)的情况下,持续从背景EEG中分辨"用户想发指令"与"用户处于静息/非控制状态"，假阳性率过高是当时异步BCI实用化的主要瓶颈。

## 核心方法
在UBC团队此前的LF-ASD(Low-Frequency Asynchronous Switch Design)基础上改进特征提取与分类策略，用健康受试者数据系统评估不同参数设置下"意图控制(IC)"检测的命中率与假阳性率的权衡，目标是在尽量不打扰用户自然静息状态的前提下提高开关触发的可靠性。

## 关键数据
论文报告了不同分类阈值设置下的真阳性率/假阳性率权衡曲线(具体数值以原文Table为准);核心贡献是把假阳性率显著压低同时保持可用的命中率，而非单纯提升某个点估计的分类准确率。

## 为什么是 milestone
LF-ASD一系是"意图性脑开关"型异步BCI的早期代表工作，直接确立了"idle-state误报"是异步/自定步调BCI要解决的中心问题，是本子线(自定步调/异步控制)较早的工程实证之一。
