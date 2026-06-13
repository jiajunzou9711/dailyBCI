---
title: "Neuroprosthesis for decoding speech in a paralyzed person with anarthria"
authors: Moses, Metzger, Liu, Anumanchipalli, Makin, Sun, Chartier, Dougherty, Liu, Abrams, Tu-Chan, Ganguly, Chang
year: 2021
venue: New England Journal of Medicine
url: https://doi.org/10.1056/NEJMoa2027540
subfield: signal-processing
tags: [speech-decoding, word-classifier, language-model, ECoG, sequence-decoding, PANCHO]
---

## 解决了什么问题
语音 BCI 的难点在于神经信号不是一个静态分类问题：用户想说的是连续词序列，而每个词之间有语言统计结构。如何把 ECoG 中的 attempted speech 活动变成可读句子，而不是只做离线分类？

## 核心方法
UCSF 团队用 ECoG 信号训练词级分类器，并结合语言模型在句子层面约束输出。系统把每个时间窗口的神经证据与英语词序列概率结合起来，实时生成文本。这是从“神经分类器”走向“神经解码 + 语言先验”的关键一步。

## 关键数据
- 在一名 anarthria 参与者中实时解码 attempted speech
- 50 词词汇表
- 约 15 词/分钟
- 中位词错误率约 25.6%
- 证明语言模型能显著帮助神经语音解码

## 为什么是 milestone
这篇论文不仅是 speech BCI 的临床 milestone，也是 signal processing 的 milestone。它证明 BCI 解码不能只看神经信号本身，还要把任务结构纳入模型。对语言通信来说，语言模型不是后处理小工具，而是把 noisy neural evidence 转成可用文字的核心组件。
