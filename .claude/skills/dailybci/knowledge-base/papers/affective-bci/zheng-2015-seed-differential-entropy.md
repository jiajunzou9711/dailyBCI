---
title: "Investigating Critical Frequency Bands and Channels for EEG-based Emotion Recognition with Deep Neural Networks"
authors: Zheng, W.-L., Lu, B.-L.
year: 2015
venue: IEEE Transactions on Autonomous Mental Development 7(3):162-175
url: https://doi.org/10.1109/TAMD.2015.2431497
subfield: affective-bci
tags: [SEED, differential-entropy, critical-bands, deep-belief-network, benchmark]
---

## 解决了什么问题
EEG 情绪识别中"哪些频段、哪些电极真正承载情绪信息"长期靠经验。本文用数据驱动方式系统回答这一问题，并发布 SEED 数据集——后来最常用的 EEG 情绪 benchmark 之一。

## 核心方法
- 提出 **微分熵(differential entropy, DE)** 特征及其对称电极组合(DASM/RASM)，相比传统能量谱更稳定地刻画情绪相关的 EEG 频谱特性。
- 用深度信念网络(DBN)训练并检视其权重，反推哪些频段/电极对情绪判别贡献最大。
- 发布 SEED：15 名被试观看约 4 分钟电影片段，诱发 negative/neutral/positive 三类情绪。

## 关键数据
- SEED：15 被试，三分类(正/中/负)，每被试多次 session。
- 关键发现：**gamma 频段(31–50 Hz)与情绪状态的相关性强于其他频段**；DE 特征优于传统能量谱特征。
- DE 自此成为 EEG 情绪识别最常用的输入特征之一。

## 为什么是 milestone
SEED + 微分熵把 EEG 情绪识别的特征与 benchmark 都标准化，与 [[koelstra-2012-deap-dataset]] 并列为本子领域两大公开数据集。它确立的 DE 特征是后续图神经网络([[song-2018-dgcnn-eeg-emotion]])与跨被试迁移([[zheng-2016-transfer-learning-affective]])工作的共同输入起点；frontal/gamma 的情绪相关性也呼应 [[davidson-1992-frontal-asymmetry-emotion]] 的神经生理框架。
