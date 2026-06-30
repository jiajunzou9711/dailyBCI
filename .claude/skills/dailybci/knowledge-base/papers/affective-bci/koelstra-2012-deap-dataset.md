---
title: "DEAP: A Database for Emotion Analysis using Physiological Signals"
authors: Koelstra, S., Mühl, C., Soleymani, M., Lee, J.-S., Yazdani, A., Ebrahimi, T., Pun, T., Nijholt, A., Patras, I.
year: 2012
venue: IEEE Transactions on Affective Computing 3(1):18-31
url: https://doi.org/10.1109/T-AFFC.2011.15
subfield: affective-bci
tags: [DEAP, benchmark-dataset, multimodal, valence-arousal, EEG]
---

## 解决了什么问题
情感计算长期缺少公开、标准化的生理信号情绪数据集，导致各家结果不可比、方法难复现。DEAP 提供首批被广泛采用的公开多模态情绪数据集，把 EEG 情绪识别变成可 benchmark 的任务。

## 核心方法
32 名被试观看 40 段 1 分钟音乐视频，同步记录 32 通道 EEG + 外周生理(GSR、呼吸、体温、血容、肌电、眼电)；每段视频后被试在 **valence、arousal、dominance、liking** 等维度自评。其中 22 名同时录制了面部视频。情绪标注采用 [[picard-1997-affective-computing]] 的维度模型，把识别任务化为对 valence/arousal 的高低分类或回归。

## 关键数据
- 32 被试 × 40 试次，32 通道 EEG（512 Hz，公开预处理版降采样到 128 Hz）+ 8 路外周。
- 标注维度：valence/arousal/dominance/liking（连续 1–9 量表）。
- 成为情感计算引用量最高的 benchmark 之一，后续无数 EEG 情绪解码方法以它为标准评测集。

## 为什么是 milestone
DEAP 把 EEG 情绪识别从各自为政变成有公共标尺的领域，valence–arousal 标注框架成为事实标准。它与稍后的 [[zheng-2015-seed-differential-entropy]](SEED)共同构成本子领域两大基准；今日候选这类"跨数据集 EEG 情绪识别"工作，跨的正是 DEAP/SEED 这类数据集之间的分布差异。
