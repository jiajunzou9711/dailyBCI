---
title: "Phonetic feature encoding in human superior temporal gyrus"
authors: Mesgarani, Cheung, Johnson, Chang
year: 2014
venue: Science
url: https://doi.org/10.1126/science.1245994
subfield: brain-encoding-models
tags: [ECoG, phonetic-features, STG, spectrotemporal-tuning, speech-perception, handcrafted-features]
---

## 解决了什么问题
颞上回（STG）参与语音的高阶听觉加工，但它如何编码语音信息此前不清楚。本文用人类颅内记录，给出 STG 对**整个英语音位清单**的表征图景。

## 核心方法
**皮层表面高密度电极（ECoG，硬膜下，不穿刺皮层）**，**六名**癫痫术前评估患者，每人 37–102 个位点；听自然连续语音（500 个句子，400 名说话人）。分析 **75–150 Hz** 高伽马皮层表面场电位。把语音按音位逐段标注，估计每个电极对每个音素的平均神经反应。

## 关键数据
- **单电极层面出现对不同音位特征的选择性**（塞音、擦音、特定元音等各有偏好电极）。
- 声学属性的编码由**分布式群体反应**承载。
- 音位特征的选择性**可以直接关联到谱时声学线索的调谐**，其中一些是**非线性编码**或**多线索整合**而来。
- 作者自身的定位词是「**声学—音位**表征」，两头都留着。

## 为什么是 milestone
它是「拿音素当自变量去预测皮层活动」这条研究路线最具代表性的成果，结论至今未被推翻。**同时它也是这条路线的方法论边界样本**：用音位标签当自变量得到的结论「电极反应与音位标签相关」，与两种情况都相容——① 皮层以音素为表征单位；② 皮层编码连续声学特征而音位标签与之高度相关。两者给出同样的观测。能分开它们的判据是**范畴不变性**（范畴内声学变化下反应是否一致、跨边界是否突变），本文未回答。评估任何「颅内解出音素」类结果时，先过这条边界。与 [[kell-2018-task-optimized-auditory]]、[[nastase-2026-language-population-code]] 同线。
