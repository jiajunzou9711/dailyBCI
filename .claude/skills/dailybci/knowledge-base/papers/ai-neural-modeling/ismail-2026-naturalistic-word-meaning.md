---
title: "Estimation of neuronal tuning for word meaning from passively recorded naturalistic speech"
authors: Ismail T, Chavez AG, Yan X, …, Hennig JA, Sheth SA, Provenza N, Hayden BY
year: 2026
venue: bioRxiv (preprint, posted 2026-06-28)
url: https://doi.org/10.64898/2026.06.23.733980
subfield: ai-neural-modeling
tags: [single-neuron, semantic-decoding, naturalistic-speech, human-intracranial, language-coding, encoding-decoding, Behnke-Fried]
---

## 解决了什么问题
研究人类神经元如何编码"词义"，过去依赖**受控实验**（念词表 / 听指定材料）——贵、样本小、罕见样本拿不到；而人类单神经元数据本就稀缺（只能来自因临床需要植入深部电极的患者）。本文问：能否跳过受控实验，**直接从患者住院期间被动录到的日常自然语音**里，估计单神经元对词义的编码。

## 核心方法
人类**侵入式深部单神经元**记录：Behnke-Fried 微丝电极（癫痫监测/EMU 患者），覆盖 6 个深部脑区（海马 / 杏仁核 / 眶额 / 丘脑中央内侧核 / 前扣带 / 后扣带）。一条**全自动流水线**：WhisperX 转录+切词、视频做说话人区分（LR-ASD diarization）、自动阈值检出动作电位，把每个词与放电对齐；**编码**用 Poisson GLM（词义=LLM embedding，gemma/GPT-2/word2vec），**解码**用 XGBoost（10 类语义）。全程无人工标注、无人工分选动作电位。

## 关键数据
- 21 患者、6+ 天/人（均 6.72）、**871.2 小时**、**5,270,665 词**（单人 4 万–52 万）。
- 编码对所有患者显著（pseudo R²>0，0.004–0.12）；10 类语义**解码准确率**平均 **20.9%**（随机 10%）。
- 自己说 vs 环境语音：编码强 **2.42×**（0.026→0.064），尽管训练数据少约 50×——注意力效应（呼应 [[mesgarani-2012-attended-speaker-cortical]]）。
- **自动化 ≈ 人工**：自动转录≈人工校对、阈上穿越≈人工分选，差异不显著。
- **编码-解码不对称**：单单元编码单日比跨天合并强 3.06×（暴露表征漂移）；群体解码靠冗余稳住、数据越多越好。
- 脑区：PCC / ACC / HPC 语义编码最高。

## 为什么是 milestone
把"神经→语言/语义"这条线从**受控刺激**推到**零控制的日常自然语音 + 百万词级规模**，并推到**人类单神经元**分辨率。纵接 [[tang-2023-semantic-language-reconstruction]]（fMRI 非侵入语义重建）、[[marin-llobet-2026-neurrator-single-cell-narration]]（小鼠单神经元→语言），与产出型语音 BCI（[[willett-2023-phoneme-rnn-language-model]] 解"发音"）正交（本篇解"意义/理解"）。核心方法学贡献：证明"规模+自动化>人工精标"，把人类单神经元语义建模的数据成本，从昂贵受控实验降到"免费的日常语音"——指向未来给说不了话者的语义 BCI。电极背景见 Behnke-Fried 微丝（Misra et al. 2014）。预印本（2026-06-28），尚未同行评议。
