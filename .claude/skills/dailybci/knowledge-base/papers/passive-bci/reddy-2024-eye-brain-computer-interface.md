---
title: "Towards an Eye-Brain-Computer Interface: Combining Gaze with the Stimulus-Preceding Negativity for Target Selections in XR"
authors: Rajshekar Reddy GS, Proulx MJ, Hirshfield L, Ries AJ
year: 2024
venue: CHI '24 (ACM CHI Conference on Human Factors in Computing Systems)
url: https://doi.org/10.1145/3613904.3641925
subfield: passive-bci
tags: [passive-BCI, eye-brain-computer-interface, stimulus-preceding-negativity, SPN, gaze, XR, target-selection, Midas-touch, EEG]
---

## 解决了什么问题
注视交互有 Midas touch 问题:每次注视都当命令,用户没法只看不选。以往用停留时间或按键做"确认"信号,慢或需动作。能否用一个隐式、免动作的脑电信号来确认"我要选这个"。

## 核心方法
在 XR 里把注视与被动 BCI 结合(eye-brain-computer interface):利用 **Stimulus-Preceding Negativity(SPN,刺激前负波)**——用户预期选择后即将到来的反馈时产生的一个前瞻性 ERP 成分——作为隐式的选择确认信号。关键论证:SPN 由用户"想选中该目标"的意图驱动,而不是由刺激反馈本身诱发,因此可当作意图代理。

## 关键数据
- SPN 能在 VR 情境下解码指向被注视目标的选择意图(人类 EEG)。
- 证明 SPN 的驱动源是选择意图,与反馈事件可分。

## 为什么是 milestone
把"注视 + 前瞻性 ERP(SPN)"路线确立为 XR 目标选择的 passive BCI 方案,是同期 gaze+EEG 意图解码的代表性横向对照。相对 [[pan-2026-vr-gaze-intent]]:Reddy 走离线、目标选择、用 SPN;Pan 走在线闭环、take/discard 意图、用 item-onset 评价 ERP——两条路线选择不同、互为参照。
