---
title: "Semantic reconstruction of continuous language from non-invasive brain recordings"
authors: Tang, LeBel, Jain, Huth
year: 2023
venue: Nature Neuroscience
url: https://doi.org/10.1038/s41593-023-01304-9
subfield: ai-neural-modeling
tags: [language-decoding, fMRI, non-invasive, GPT, semantic-decoder, brain-to-text, privacy]
---

## 解决了什么问题
此前从脑活动恢复语言主要依赖侵入式电极（皮层内/ECoG）。能否**完全非侵入**（fMRI）地从大脑活动重建出连续、有意义的语言，是开放问题——fMRI 时间分辨率低（血氧响应慢），被认为难以追上语言的速度。

## 核心方法
Huth 组（UT Austin）。先用编码模型刻画语义如何驱动各体素的血氧响应，再配一个基于 GPT 的语言模型作先验：解码时生成候选词序列、用编码模型预测其应产生的脑活动、与实测比对，beam search 迭代逼近。输出是**语义层面的复述（gist）**而非逐字还原。

## 关键数据
- 能从被试**听故事、想象讲故事、看无声视频**三种条件下重建出语义连贯的语言描述。
- 论文报告解码需被试配合（注意力转移即可显著破坏解码），并据此讨论 mental privacy——非侵入语言解码的伦理边界。

## 为什么是 milestone
首次证明**非侵入**可做到连续自然语言的语义重建，把"神经→语言"从侵入式语音 BCI（见 speech-decoding 线）扩展到 fMRI。它是 2026 年 NEURRATOR"把神经活动旁白成自由文本"在语言侧的直接祖先；也把心理隐私问题正式摆上台面。神经→caption 的视觉侧见 [[ferrante-2023-brain-captioning]]。
