---
title: "High-speed spelling with a noninvasive brain-computer interface"
authors: Chen, Wang, Nakanishi, Gao, Jung, Gao
year: 2015
venue: Proceedings of the National Academy of Sciences (PNAS)
url: https://doi.org/10.1073/pnas.1508080112
subfield: non-invasive
tags: [SSVEP, speller, high-speed, Tsinghua, frequency-phase-modulation, ITR-record]
---

## 解决了什么问题
非侵入式 BCI 的通信速率一直远低于侵入式系统。P300 speller 约 2-5 字符/分钟，motor imagery BCI 更慢。能否大幅提升 EEG-BCI 的速度，接近实用通信水平？

## 核心方法
提出了联合频率-相位调制（joint frequency-phase modulation）方法，用 0.5 秒的闪烁信号编码 40 个字符。利用 SSVEP（稳态视觉诱发电位）的频率和相位高度一致性，通过 TRCA（task-related component analysis）实现极短时间窗内的高准确率检测。

## 关键数据
- 信息传输率：5.32 bits/sec（当时所有 BCI 中最高，包括侵入式）
- 拼写速率：60 字符/分钟
- 40 个字符选项，0.5 秒刺激时间
- 175 名被试的 MEG/EEG 数据验证

## 为什么是 milestone
创下非侵入式 BCI 信息传输率的世界纪录，甚至超过了当时许多侵入式 BCI 系统。证明了在特定任务（离散选择型通信）上，非侵入式方法可以达到极高速率。SSVEP + TRCA 的组合成为后续高速 BCI 研究的标准方法。发表在 PNAS。
