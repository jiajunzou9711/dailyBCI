---
title: "Brains and algorithms partially converge in natural language processing"
authors: Caucheteux, King
year: 2022
venue: Communications Biology 5:134
url: https://doi.org/10.1038/s42003-022-03036-1
subfield: brain-encoding-models
tags: [encoding-model, language-model, fMRI, MEG, next-word-prediction]
---

## 解决了什么问题
与 [[schrimpf-2021-neural-architecture-language]] 同期、独立地问同一个问题：深度语言模型与大脑的相似性到底由什么决定——架构、训练方式，还是任务性能？并且要把"何处相似"（皮层位置）与"何时相似"（时间进程）分开。

## 核心方法
在同一批被试上同时用 **fMRI**（空间分辨）与 **MEG**（时间分辨）记录阅读时的脑响应，再系统比较多个深度语言模型的表征，分别评估架构、训练、性能三个因素各自的独立贡献。

## 关键数据
- 人类 **102 名**被试，阅读 **400 个**孤立句子；fMRI + MEG。
- 算法与大脑的相似度主要取决于模型**从上下文预测词**的能力。
- 相似度随皮层区域呈现出知觉表征、词汇表征、组合表征的层次分布与时间上的建立-维持过程。

## 为什么是 milestone
与 Schrimpf 2021 构成两条独立证据链，共同支撑"预测下一个词是脑-模型对齐的关键属性"这一主张——两者用不同数据、不同模态、不同分析路径得到一致结论，因此该结论比任一单篇更可靠。MEG 的引入还把结论从"哪里像"扩到"什么时候像"。作者 King 与 [[defossez-2023-meta-meg-speech]]、[[brain2qwerty-2026-meg-typing-decoding]] 同组，是那条 MEG 线的方法学背景。
