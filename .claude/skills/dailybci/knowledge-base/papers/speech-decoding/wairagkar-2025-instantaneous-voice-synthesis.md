---
title: "A streaming brain-to-voice neuroprosthesis to restore naturalistic communication"
authors: Wairagkar, Card, Singer-Clark, Hou, Iacobacci et al.
year: 2025
venue: Nature Neuroscience
url: https://doi.org/10.1038/s41593-025-01905-6
subfield: speech-decoding
tags: [voice-synthesis, streaming, low-latency, RNN-transducer, personalized-voice, real-time, Stanford-BrainGate]
---

## 解决了什么问题
之前所有 speech BCI 输出的是文本——患者说一句话，系统等整句解码完再显示结果。这导致 1-2 秒的延迟，让自然对话（如打断、接话）不可能。真正的语音交流需要接近实时的声音输出。

## 核心方法
用 RNN-Transducer（流式端到端模型）将 intracortical 神经信号以 80ms 的时间粒度连续解码为语音。不等整句说完，而是"边说边译"，每 80ms 输出一小段合成语音。语音合成器个性化到患者受伤前的声音（基于患者的历史语音样本训练 TTS 模型）。

## 关键数据
- 解码延迟：~80ms（接近自然语音延迟）
- 流式输出：不需要等整句说完
- 个性化语音：合成语音听起来像患者自己的声音
- 大词汇量持续语音合成
- 发表于 Nature Neuroscience (2025)

## 为什么是 milestone
从 text 输出到 voice 输出是 speech BCI 的质变。80ms 的延迟意味着用户可以参与正常节奏的对话——可以打断别人，别人也不会意外打断你。加上个性化语音（听起来是"你自己的声音"），这是 speech BCI 首次触及"恢复自然交流"的目标，而非仅仅"传递信息"。
