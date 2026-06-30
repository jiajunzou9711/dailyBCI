---
title: "Personalizing EEG-based Affective Models with Transfer Learning"
authors: Zheng, W.-L., Lu, B.-L.
year: 2016
venue: Proceedings of IJCAI 2016, 2732-2739
url: https://www.ijcai.org/Abstract/16/431
subfield: affective-bci
tags: [transfer-learning, domain-adaptation, cross-subject, TPT, non-stationarity]
---

## 解决了什么问题
EEG 的个体差异 + 非平稳特性使情感模型难以跨被试泛化；为每个新用户采集大量带标签数据既贵又慢。本文问：能否在**不采集目标被试标签**的情况下，把已有被试上学到的情感模型迁移给新用户？

## 核心方法
首次把迁移学习/域适应系统引入 EEG 情绪识别：提出 **transductive parameter transfer(TPT)** 等方案，把"源被试→目标被试"建模为分布对齐问题，用无标签目标数据缩小训练-测试分布差异，从而免去逐人重新标注校准。

## 关键数据
- 在 SEED 等数据集上验证：迁移/个性化模型相比不做适应的基线显著提升跨被试准确率（具体数字见原文 IJCAI 2016, 2732–2739）。
- 比较了多种 subject-to-subject 迁移策略，确立 TPT 为该任务的早期强基线。

## 为什么是 milestone
它把 [[muhl-2014-affective-bci-survey]] 点名的核心障碍("个体差异 + EEG 非平稳")正式转化为一个**域适应问题**，开启 EEG 情绪识别的迁移学习/跨被试研究线。**今日候选(跨数据集 EEG 情绪识别、source-free 域适应 + test-time training)正是这条线十年后的延伸**——从"跨被试"推进到"跨数据集"、从需要源数据推进到 source-free。沿用 [[zheng-2015-seed-differential-entropy]] 的 SEED/DE 设定。
