---
title: "Brain-to-text: decoding spoken phrases from phone representations in the brain"
authors: Herff, Heger, de Pesters, Telaar, Brunner, Schalk, Schultz
year: 2015
venue: Frontiers in Neuroscience
url: https://doi.org/10.3389/fnins.2015.00217
subfield: speech-decoding
tags: [brain-to-text, phone-decoding, ECoG, ASR-pipeline, continuous-speech, Herff]
source_review: "Restoring Speech Using Brain-Computer Interfaces (Annual Reviews of Bioengineering 2025, ref 93)"
---

## 解决了什么问题
之前的语音解码工作主要解码离散的词或音素分类。能否像自动语音识别（ASR）那样，从连续语音的皮层活动中解码出完整的文本？

## 核心方法
借鉴ASR（自动语音识别）的pipeline：用ECoG信号提取phone-level声学特征，通过语言模型约束生成文本。关键创新是将成熟的语音识别框架（phone → word → sentence）应用于脑信号解码，而非直接端到端分类。

## 关键数据
- 从ECoG信号解码连续语音为文本
- 采用phone-level表征作为中间层
- 结合语言模型提高准确率
- 在癫痫监测患者的公开朗读任务中验证

## 为什么是 milestone
首次将成熟的ASR pipeline概念应用于脑信号→文本解码。"phone → language model → text"的框架后来被Willett 2023和Card 2024继承和大幅改进。Herff 2015证明了这条技术路线的可行性——不需要为每个词单独训练，而是通过phone/phoneme的组合来覆盖大词汇。
