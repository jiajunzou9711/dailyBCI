---
title: "A high-performance speech neuroprosthesis"
authors: Willett, Kunz, Fan, Avansino, Wilson et al.
year: 2023
venue: Nature
url: https://doi.org/10.1038/s41586-023-06377-x
subfield: speech-decoding
tags: [intracortical, microelectrode-array, phoneme-decoding, RNN, large-vocabulary, Stanford-BrainGate]
---

## 解决了什么问题
Moses 2021 证明了 speech decoding 在瘫痪患者身上可行，但 50 词词汇表和 15 词/分钟的速度远不够实用。需要大幅提升速度和词汇量，同时探索 intracortical 方案（而非 ECoG）能否用于 speech decoding。

## 核心方法
在 ALS 患者的 vSMC 植入两个 Utah 微电极阵列（intracortical），解码 attempted speech。核心创新：从 phoneme-level 解码，而非 word-level。用 RNN 将神经活动映射为 phoneme 概率序列，再用语言模型将 phoneme 序列转换为词和句子。因为英语只有约 39 个 phoneme，所有词都是 phoneme 的组合，所以理论上不需要为每个词单独训练。

## 关键数据
- 62 词/分钟解码速度（Moses 2021 的 4 倍）
- 125,000 词词汇表（Moses 2021 的 2500 倍）
- 词错误率：23.8%（125k 词汇）
- Phoneme 错误率：9.1%
- 使用 intracortical microelectrode arrays（非 ECoG）

## 为什么是 milestone
证明了 phoneme-level decoding 路线的可行性和巨大优势：不需要为每个新词采集训练数据，phoneme 组合自然覆盖任意大的词汇表。这彻底改变了 speech BCI 的技术路径选择。同时首次证明 intracortical 录制（之前只用于 motor BCI）也能有效解码语音，为硬件选择打开了新空间。
