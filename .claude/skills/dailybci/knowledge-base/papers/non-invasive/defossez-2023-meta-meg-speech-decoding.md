---
title: "Decoding speech perception from non-invasive brain recordings"
authors: Defossez, Caucheteux, Rapin, Kabeli, King
year: 2023
venue: Nature Machine Intelligence
url: https://doi.org/10.1038/s42256-023-00714-5
subfield: non-invasive
tags: [MEG, EEG, speech-decoding, deep-learning, Meta-FAIR, contrastive-learning, wav2vec]
---

## 解决了什么问题
语音解码此前只在侵入式 BCI（ECoG、intracortical）上取得突破。非侵入式脑信号（MEG/EEG）能否也解码出听到的语音内容？如果可以，意味着语音 BCI 有可能无需开颅手术。

## 核心方法
Meta FAIR 团队训练了一个卷积神经网络，用对比学习目标（contrastive objective）将 3 秒的 MEG/EEG 信号映射到预训练语音模型（wav2vec 2.0）的深层表征空间。用 56,000 小时语音预训练的音频编码器提供监督信号。在 4 个公开数据集、175 名被试上验证。

## 关键数据
- MEG：72.5% top-10 准确率（从 1,594 个语音片段中识别），44% top-1 准确率
- EEG：19.1% top-10 准确率（从 2,604 个片段中）
- 3 秒时间窗即可解码
- 模型在被试间可迁移（但个体校准后性能更好）

## 为什么是 milestone
首次证明非侵入式脑记录可以在大规模数据上实现有意义的语音解码。虽然性能远低于侵入式方法（Card 2024 的 97.5% 准确率），但打开了"无需手术的语音 BCI"这条探索路径。Meta 这样的 AI 巨头介入 BCI 研究本身也标志着领域的变化。
