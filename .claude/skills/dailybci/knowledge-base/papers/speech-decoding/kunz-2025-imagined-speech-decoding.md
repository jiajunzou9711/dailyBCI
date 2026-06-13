---
title: "Decoding inner speech from intracortical neural activity"
authors: Kunz, Abramovich Krasa, Meschede-Krasa, Kamdar, Avansino, Willett et al.
year: 2025
venue: Cell
url: https://doi.org/10.1016/j.cell.2025.07.xxx
subfield: speech-decoding
tags: [imagined-speech, inner-speech, covert-speech, intracortical, motor-cortex, Stanford-BrainGate]
---

## 解决了什么问题
到目前为止所有成功的 speech BCI 都基于 attempted speech（患者尝试说话，产生运动皮层活动）。但很多患者（如完全 locked-in）甚至无法做出"尝试说话"的动作。理想状态是解码 imagined speech（纯粹在脑中想的语言），但之前普遍认为 imagined speech 的神经信号太弱、太不稳定，无法可靠解码。

## 核心方法
让植入 intracortical 电极的瘫痪患者不做任何尝试发声的动作，仅在脑中"想"完整句子。用针对 imagined speech 优化的解码器从运动皮层活动中提取信号。关键发现：运动皮层在 imagined speech 时确实有可解码的活动，虽然信号模式与 attempted speech 不同但有足够的结构。

## 关键数据
- 50 词词汇表：词错误率 14-33%
- 125,000 词词汇表：词错误率 26-54%
- 实时在线解码（非离线分析）
- 首次证明 imagined speech 可以从运动皮层实时解码

## 为什么是 milestone
打破了"imagined speech 不可解码"的普遍假设。虽然性能远低于 attempted speech（Card 2024 的 2.5% WER vs 这里的 14-54%），但它证明了这条路是走得通的。对于完全 locked-in 患者（不能做任何运动尝试），这可能是唯一的通信路径。同时揭示了运动皮层在无运动输出时的 covert activity 结构，有重要的基础神经科学意义。
