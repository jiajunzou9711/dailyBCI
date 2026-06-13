---
title: "Machine translation of cortical activity to text with an encoder-decoder framework"
authors: Makin, Moses, Chang
year: 2020
venue: Nature Neuroscience
url: https://doi.org/10.1038/s41593-020-0608-8
subfield: speech-decoding
tags: [brain-to-text, encoder-decoder, sequence-to-sequence, ECoG, language-model]
---

## 解决了什么问题
之前的 brain-to-text 方法是逐音素或逐词分类，再拼接成句子，错误会逐步累积且无法利用语言结构。需要一种方法能直接将脑信号序列"翻译"为文本序列，类似机器翻译。

## 核心方法
将 speech decoding 重新定义为 sequence-to-sequence 翻译问题：用 encoder-decoder 架构（类似 NMT），encoder 接收 ECoG 神经信号时间序列，decoder 输出文本词序列。集成了语言模型约束，利用英语的统计规律来纠错和补全。

## 关键数据
- 4名癫痫患者术中 ECoG 数据
- 从约250个句子的限定集中解码，词错误率（WER）低至 3%
- 证明了 sequence-to-sequence 方法大幅优于逐词分类方法

## 为什么是 milestone
首次将 NLP 中的 sequence-to-sequence 框架引入 speech BCI，将问题从"分类"重构为"翻译"。这个范式转换极为重要——后来 Willett 2023 和 Card 2024 的高性能系统都采用了类似的序列到序列解码思路，并且整合了大规模语言模型进行纠错。它证明了语言模型可以显著提升 BCI 解码性能。
