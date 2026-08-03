---
title: "A streaming brain-to-voice neuroprosthesis to restore naturalistic communication"
authors: Littlejohn KT, Cho CJ, Liu JR, Silva AB, Anumanchipalli GK, Chang EF, et al.
year: 2025
venue: Nature Neuroscience 28:902-912
url: https://doi.org/10.1038/s41593-025-01905-6
subfield: speech-decoding
tags: [voice-synthesis, brain-to-voice, streaming, RNN-transducer, personalized-voice, ECoG, pontine-stroke, BRAVO, UCSF-Berkeley]
pmid: 40164740
---

## 解决了什么问题

与 [[wairagkar-2025-instantaneous-voice-synthesis]] 同年、同目标（把语音 BCI 的输出从文本换成声音），但走的是**另一条记录路线**：Chang 组的高密度 **ECoG（皮层表面电极，不穿刺）**。此前该组的系统（[[moses-2021-neuroprosthesis-anarthria]]、[[metzger-2023-speech-avatar-neuroprosthesis]]）都要等一句说完才输出，秒级延迟使正常对话节奏无法成立。

## 核心方法

用**流式端到端的 RNN-Transducer** 从覆盖语音感觉运动皮层的高密度 ECoG 连续解码，**以 80 ms 为增量**在线输出合成语音，不等整句结束。合成器**个性化到参与者受伤前的声音**（用其伤前语音样本训练）。属 UCSF **BRAVO 临床试验**。

## 关键数据

- **参与者**：人类**单被试**，试验代号 **BRAVO-3（Ann）**，2005 年 30 岁时脑桥卒中，重度瘫痪 + anarthria。
- **记录**：高密度 **ECoG** 表面阵列（非皮层内）。
- **解码增量 80 ms**，在线大词汇量流式合成。
- （本条目未核实原文报告的可懂度/WER 具体数值，引用时勿编造。）

## 为什么是 milestone

与 Wairagkar 2025 构成 2025 年 brain-to-voice 的**两条并行路线**，一起把语音 BCI 的目标从"传递文本信息"推到"恢复出声说话"。**两篇务必区分**：本篇为 UCSF/Berkeley、ECoG、脑桥卒中患者；Wairagkar 2025 为 UC Davis、皮层内 256 电极、ALS 患者 T15。二者延迟量级相近（均约 80 ms 粒度），但记录模态、参与者病因、以及"个性化声音"的来源都不同——ECoG 覆盖面积大更稳定，皮层内信息密度更高。这组对照本身即是"信号层级如何影响可达性能"的现成材料。
