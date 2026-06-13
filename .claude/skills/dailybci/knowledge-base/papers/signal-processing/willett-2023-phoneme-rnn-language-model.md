---
title: "A high-performance speech neuroprosthesis"
authors: Willett, Kunz, Fan, Avansino, Wilson, Choi, Kamdar, Glasser, Hochberg, Druckmann, Shenoy, Henderson
year: 2023
venue: Nature
url: https://doi.org/10.1038/s41586-023-06377-x
subfield: signal-processing
tags: [speech-decoding, phoneme-decoding, RNN, language-model, intracortical, high-performance]
---

## 解决了什么问题
词级分类 speech BCI 受限于固定词表，难以扩展到开放词汇。要接近自然交流速度，系统需要解码比“整词”更底层、更可组合的单位。问题是：能否从 intracortical motor signals 解码 phoneme 概率，再通过语言模型组合成大词汇文本？

## 核心方法
作者训练 RNN decoder，在每 80ms 时间步输出 phoneme probability。随后用语言模型把 phoneme 概率序列转化为最可能的词序列。这个架构把神经解码拆成两层：神经活动到 phoneme evidence，phoneme evidence 到语言输出。

## 关键数据
- 约 62 词/分钟
- 125,000 词词汇表
- 大词汇条件下约 9.8% word error rate
- RNN phoneme decoder 与语言模型结合，实现接近自然对话速度的文本输出

## 为什么是 milestone
这篇论文把 speech BCI 从“少量词分类”推进到“开放词汇序列解码”。它的关键 insight 是 phoneme 是比 word 更好的神经-语言接口：足够接近发音运动，又能通过语言模型扩展到巨大词汇表。这一路线成为后续高性能 speech BCI 的主流架构。
