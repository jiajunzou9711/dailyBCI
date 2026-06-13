---
title: "An accurate and rapidly calibrating speech neuroprosthesis"
authors: Card, Wairagkar, Iacobacci, Hou, Singer-Clark et al.
year: 2024
venue: New England Journal of Medicine
url: https://doi.org/10.1056/NEJMoa2314132
subfield: speech-decoding
tags: [intracortical, high-accuracy, large-vocabulary, rapid-calibration, long-term-stability, Stanford-BrainGate]
---

## 解决了什么问题
Willett 2023 在速度和词汇量上有巨大突破，但词错误率仍有 23.8%，而且校准过程较长。临床可用的 speech BCI 需要：接近完美的准确率、极大的词汇表、快速校准、和长期稳定性。

## 核心方法
延续 Willett 2023 的 intracortical + phoneme-level decoding 路线，但在多个关键环节改进：(1) 改进的 RNN 解码器架构，(2) 更好的语言模型集成（大规模 LM 纠错），(3) 快速校准协议（<30分钟即可使用），(4) 长期跟踪验证。125,000 词词汇表。

## 关键数据
- 词错误率：2.5%（Willett 2023 的 23.8% → 2.5%，一个数量级的提升）
- 词汇表：125,000 词
- 解码速度：32 词/分钟（牺牲了一些速度换取准确率）
- 校准时间：<30 分钟
- 长期稳定性：8 个月以上保持性能，到 session 84 仍保持 97.5% 准确率

## 为什么是 milestone
这是 speech BCI 性能首次达到"临床可用"级别：97.5% 准确率 + 125k 词汇 + 快速校准 + 8个月长期稳定。发表在 NEJM 再次标志其临床意义。准确率的跃升主要来自大规模语言模型的整合——这提示 speech BCI 的未来瓶颈可能不在神经解码本身，而在如何更好地利用语言先验知识。
