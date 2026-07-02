---
title: "Inner speech in motor cortex and implications for speech neuroprostheses"
authors: Kunz, Abramovich Krasa, Kamdar, Avansino, Hahn, Yoon et al.
year: 2025
venue: Cell 188(17):4658-4673.e17
url: https://doi.org/10.1016/j.cell.2025.06.015
subfield: speech-decoding
tags: [imagined-speech, inner-speech, covert-speech, intracortical, motor-cortex, Stanford-BrainGate]
pmid: 40816265
pmcid: PMC12360486
---

## 解决了什么问题
当前高性能 speech BCI 主要依赖 attempted speech（患者尝试说话，产生运动皮层活动），但这会带来疲劳、速度限制和隐私问题；对部分严重瘫痪或失语患者来说，attempted speech 本身也可能很困难。本文问的是：motor cortex 中是否存在足够稳定的 inner speech 表征，能否支持实时句子解码，并且如何防止 BCI 意外读出用户不想输出的内心语言。

## 核心方法
研究分析 4 名 BrainGate2 参与者（T12、T15、T16、T17；ALS 或脑桥卒中导致严重 dysarthria/anarthria）的 motor cortex 微电极阵列记录，比较 attempted speech、inner speech、perceived speech 等条件下的神经表征。实时 BCI 部分在 3 名 dysarthric 参与者中训练 inner-speech RNN 解码器：神经特征输入 RNN，输出 39 个 phoneme 加 silence token 的概率，再由语言模型生成文字。论文还测试了 attempted-speech decoder 是否会读出 inner speech，并提出 imagery-silenced 训练与 keyword lock/unlock 来避免非预期输出。

## 关键数据
- 神经表征分析：4 名参与者的 motor cortex 中均可观察 inner speech 相关表征；inner speech 与 attempted speech 高度相关，但存在可区分的 motor-intent 维度。
- 实时 self-paced inner-speech 解码：3 名 dysarthric 参与者。
- 50 词词汇表 WER：T12 24%、T15 14%、T16 33%。
- 125,000 词词汇表 WER：T15/T16 为 26% 到 54%。
- 论文报告，attempted-speech decoder 只用 attempted speech 训练时也能在所有参与者上以高于随机的水平解码 inner speech；imagery-silenced 训练和 keyword gating 可降低非预期输出风险。

## 为什么是 milestone
这篇论文的核心贡献不是笼统地"首次解码 inner speech"：原文也承认此前已有 ECoG 与 supramarginal gyrus intracortical inner-speech decoding 工作。它更准确的位置是：在人类 motor cortex intracortical 记录中系统刻画 inner speech 表征，并演示实时 self-paced、可扩展到 125k 词汇的 inner-speech BCI proof of concept；同时把 speech BCI 的隐私问题从伦理猜想推进到可测、可防护的工程问题。它为完全依赖 attempted speech 的语音 BCI 路线补上了一个重要分支，但当前 WER 仍明显高于 attempted-speech 系统。
