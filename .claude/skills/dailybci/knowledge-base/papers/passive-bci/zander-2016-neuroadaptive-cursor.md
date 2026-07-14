---
title: "Neuroadaptive technology enables implicit cursor control based on medial prefrontal cortex activity"
authors: Zander TO, Krol LR, Birbaumer NP, Gramann K
year: 2016
venue: PNAS 113(52):14898-14903
url: https://doi.org/10.1073/pnas.1605155114
subfield: passive-bci
tags: [neuroadaptive, implicit-control, medial-prefrontal-cortex, single-trial-ERP, expectation-violation, EEG, closed-loop, passive-BCI]
---

## 解决了什么问题
此前 passive BCI 多用于监测/预警,少有真正把隐式脑状态闭合进控制回路、让系统在**没有任何显式指令**的情况下自动逼近用户意图。能否让计算机仅凭读取用户对每一步的隐式评价,就"neuroadaptive"地自我调整、完成一个控制任务?

## 核心方法
用户仅**观看**光标的自主移动,不做任何主动控制。系统从单试次事件相关电位(ERP)解码用户对每次移动的隐式评价——这些信号主要来源于内侧前额叶皮层(mPFC),其幅度与"期望被违背的程度"近似线性对应。系统据此把光标逐步引向用户内心期望的目标,形成闭环。作者由此提出并命名 **neuroadaptive technology**:系统自动适应操作者心念的特定方面。

## 关键数据
- 无任何显式输入下实现隐式光标控制(人类 EEG)。
- 隐式评价从单试次 mPFC 起源的 ERP 解码,幅度随期望违背程度线性变化。

## 为什么是 milestone
passive BCI 从"监测状态"跃迁到"隐式闭环控制"的地标,"neuroadaptive"概念由此定名。它把 Ferrez (2008) 的错误/期望信号机制真正闭合进控制回路,是隐式意图解码(含今天 VR 被动意图这条线)的直接范式来源。
