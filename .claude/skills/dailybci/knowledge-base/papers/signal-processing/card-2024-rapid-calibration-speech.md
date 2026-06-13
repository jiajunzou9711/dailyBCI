---
title: "An accurate and rapidly calibrating speech neuroprosthesis"
authors: Card, Wairagkar, Iacobacci, Hou, Singer-Clark, Willett, Kunz, Fan, Avansino, Wilson, Glasser, Hochberg, Druckmann, Shenoy, Henderson, Brandman
year: 2024
venue: New England Journal of Medicine
url: https://doi.org/10.1056/NEJMoa2314132
subfield: signal-processing
tags: [speech-decoding, rapid-calibration, online-adaptation, RNN, language-model, clinical-BCI]
---

## 解决了什么问题
高性能 speech BCI 如果需要长时间校准、频繁重训，就很难真正日常使用。问题不只是最高准确率，而是：系统能否快速校准、跨天稳定，并在使用过程中维持准确？

## 核心方法
这篇论文在 intracortical speech BCI 中结合神经网络解码、语言模型、快速校准和在线 fine-tuning。系统通过较短校准时间建立高性能 decoder，并在使用中持续适应神经信号变化，同时输出文字和个性化语音。

## 关键数据
- 125,000 词词汇表
- 报告准确率达到 97.5% 量级
- 校准时间少于 30 分钟
- 跨数月保持稳定使用
- 个性化 text-to-speech 复现参与者原始声音

## 为什么是 milestone
Card 2024 把 speech BCI 的算法问题从“能不能解码”推进到“能不能快速部署并持续可用”。它强调 calibration、online adaptation 和 language model 的组合，而不仅是离线模型结构。对临床系统来说，这比单次 demo 的峰值性能更接近产品级需求。
