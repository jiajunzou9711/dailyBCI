---
title: "Predicting human brain activity associated with the meanings of nouns"
authors: Mitchell TM, Shinkareva SV, Carlson A, Chang KM, Malave VL, Mason RA, Just MA
year: 2008
venue: Science
url: https://doi.org/10.1126/science.1152876
subfield: semantic-decoding
tags: [semantic-decoding, fMRI, zero-shot, corpus-statistics, encoding-model, human]
---

## 解决了什么问题

2008 年前的语义解码只能做**封闭集分类**：训练时见过哪几个概念，测试时就只能在这几个里选。想扩到成千上万个词，就得给每个词都采一遍 fMRI，不可行。本文要解决的正是这个可扩展性瓶颈：能不能预测**训练时从未采过数据的词**会诱发什么脑活动。

## 核心方法

人类 fMRI。核心构造是把词义拆成一组**语料库统计特征**：从一个万亿词级文本语料里，统计目标名词与一组基础动词的共现频率，用这个共现向量表示词义。然后训练一个线性模型，把词义向量映射到 fMRI 体素激活。因为映射建在**特征**上而非建在**词**上，训练后的模型可以给语料库里任意一个具体名词预测它的 fMRI 激活图——即使这个词从未被扫描过。这就是后来被称为 zero-shot（零样本）解码的范式（形式化见同期 Palatucci et al. 2009 的 semantic output codes）。

## 关键数据

- *Science* 320:1191–1195（2008 年 5 月 30 日），DOI 10.1126/science.1152876，PMID 18511683
- 训练数据：一个万亿词文本语料 + 数十个具体名词（several dozen concrete nouns）的实测 fMRI
- 模型训练后可为语料库中数千个其他具体名词预测 fMRI 激活；在**目前有 fMRI 数据的 60 个名词**上验证，准确率显著高于随机（原文表述为 "highly significant accuracies over the 60 nouns"）
- 限制：仅具体名词（concrete nouns）；抽象概念与句子层面由 [[pereira-2018-universal-decoder]] 接手

## 为什么是 milestone

它确立了这条线此后一直沿用的范式：**不要直接解码"是哪个词"，要解码"词义向量"，再在向量空间里检索**。这一步把语义解码从封闭集分类变成可外推的问题，也是"神经活动 → 预训练特征空间"这条更大脉络在语言侧的祖先（视觉侧的对应者是 [[horikawa-2017-generic-decoding-dnn-features]]）。今天所有把脑信号对齐到词向量/LLM 表征空间的工作（[[tang-2023-semantic-language-reconstruction]]、[[ismail-2026-naturalistic-word-meaning]]）都在这条线上。反过来看，它也框定了侵入式语义解码的短板：颅内工作至今大多仍停在**封闭集范畴分类**（[[wang-2011-ecog-semantic-decoding]]、[[nagata-2022-abstract-concrete-semantics]]），只有 [[rupp-2017-ecog-semantic-attributes]] 迈到了属性空间 + 未训练物体外推。
