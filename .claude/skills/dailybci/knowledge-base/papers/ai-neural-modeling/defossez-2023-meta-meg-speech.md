---
title: "Decoding speech perception from non-invasive brain recordings"
authors: Defossez, Caucheteux, Rapin, Kabeli, King
year: 2023
venue: Nature Machine Intelligence
url: https://doi.org/10.1038/s42256-023-00714-5
subfield: ai-neural-modeling
tags: [MEG, speech-decoding, contrastive-learning, wav2vec, Meta-FAIR, cross-subject]
---

## 解决了什么问题
AI 语言模型（如 wav2vec）的表征能否帮助从非侵入式脑信号中解码语音？这个问题连接了两个领域：大规模语音 AI 和非侵入式神经科学。

## 核心方法
用对比学习将 MEG/EEG 的 3 秒时间窗映射到 wav2vec 2.0（在 56,000 小时语音上预训练）的表征空间。模型学习将脑信号和对应的语音段落的深层表征对齐。在 4 个公开数据集、175 名被试上验证。

## 关键数据
- MEG：72.5% top-10 准确率（1,594 语音片段）
- EEG：19.1% top-10 准确率（2,604 片段）
- 3 秒窗口即可解码
- 跨被试迁移可行但性能下降

## 为什么是 milestone
展示了将大规模预训练 AI 模型作为"桥梁"来理解脑信号的新范式。不是直接从脑信号解码语音波形，而是利用 AI 语言模型的表征作为中间目标。Meta FAIR 的介入也标志着大型 AI 研究机构开始系统性地进入神经科学领域。

注：此条目同时与 non-invasive 子领域相关，见 [defossez-2023-meta-meg-speech-decoding](../non-invasive/defossez-2023-meta-meg-speech-decoding.md)。
