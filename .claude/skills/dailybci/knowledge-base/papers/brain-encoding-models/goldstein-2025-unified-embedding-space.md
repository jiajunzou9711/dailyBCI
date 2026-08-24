---
title: "A unified acoustic-to-speech-to-language embedding space captures the neural basis of natural language processing in everyday conversations"
authors: Goldstein, Wang, Niekerken, Schain, Zada, Aubrey, Sheffer, Nastase, Gazula, Singh, et al.
year: 2025
venue: Nature Human Behaviour
url: https://doi.org/10.1038/s41562-025-02105-9
subfield: brain-encoding-models
tags: [ECoG, Whisper, speech-to-text, encoding-model, phonemes, part-of-speech, variance-partitioning, soft-hierarchy, natural-conversation]
---

## 解决了什么问题
经典图景把语言处理切成声波 → 音素 → 词 → 句法 → 意义这条离散流水线，各级由不同机制、不同脑区分别承担。本文用一个**内部不含任何音位或句法标注**的语音转文本模型，同时检验两件事：这条流水线的符号特征是不是描述皮层活动的合适层次；以及「符号能从表征里解码出来」能不能推出「表征以该符号为单位组织」。

## 核心方法
从 Whisper（编码器-解码器 Transformer，训练目标仅「音频 → 文本」）取三层内部表征：① **声学嵌入**——音频编码器 Transformer 块之前的早期层；② **语音嵌入**——音频编码器最后一层，即交叉注意力读取的接口；③ **上下文词嵌入**——文本解码器较晚的中间层。脑数据为约 **100 小时自然对话**的 **ECoG**，产生与理解两种状态分别评估，编码表现在**留出的对话**上计算。两条并行分析：编码模型（特征 → 神经信号）与嵌入空间内部的符号可解码性；另做逐电极的**方差分解**。

## 关键数据
- 三种嵌入都在大量电极上预测到脑活动，且**全部大幅超过**手工符号特征（音素、词性）——原文用词 dramatically outperformed。
- 空间分布有顺序：声学嵌入 → 感觉与发音相关区（产生 N=64、理解 N=46 个显著电极）；语音嵌入 → 范围最广（N=274 / N=186），理解时最强在 STG、产生时在运动区；上下文词嵌入 → 最强在 IFG 与角回（N=154 / N=135）。电极显著性 p<0.01，Bonferroni 校正。
- **双分离**：音素类别能从语音嵌入空间恢复，在语言嵌入空间里不清楚；词性类别能从语言嵌入空间恢复，在语音嵌入空间里不明显。
- 原文强度用词为 **partially recovered** 与 **approximate byproducts**——模型内部并不显式使用离散符号表征，这些类别是嵌入几何的近似副产物。
- 上下文词嵌入**纳入中层语音嵌入的信息后**，对很多电极的预测更准；方差分解显示**许多电极（many electrodes）对中层语音与高层上下文语义同时有独有贡献**，即混合调谐。

## 为什么是 milestone
它把「能读出来 ≠ 里面存在」这条主脊变成一个**构造完全已知的反例**：模型里没有任何一组单元是为音素设立的，音素却仍能从其嵌入空间里部分读出。因此「从颞上回能解出音素，所以皮层有音素这一层」这一步推论**失效**——注意强度边界，这是取消一步推论，不是证明皮层没有音素。正面结论是**软层级**：层级顺序真实存在（模型层序与皮层层级对应），但相邻层级在同一批位点上重叠、高层没有丢掉低层信息，**区域层面有分工，位点层面不干净**。与 [[kell-2018-task-optimized-auditory]] 是同一套论证在语言层级上的延伸（Kell 的对照只到声学一级），与 [[mesgarani-2014-phonetic-feature-stg.md]] 暴露的方法学边界正面对接。**属自引提示**：Nastase 为本文作者之一，本文即 [[nastase-2026-language-population-code]] Figure 2 的来源。
