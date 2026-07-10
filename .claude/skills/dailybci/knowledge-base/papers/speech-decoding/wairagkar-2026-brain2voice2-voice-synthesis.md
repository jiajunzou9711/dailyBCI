---
title: "Brain2voice 2.0: High-performance voice synthesis brain-computer interface"
authors: Wairagkar M, Srinivasan A, Card NS, Singer-Clark T, Hou X, Iacobacci C, Miller LM, Hochberg LR, Brandman DM, Stavisky SD
year: 2026
venue: bioRxiv
url: https://doi.org/10.64898/2026.06.30.735633
subfield: speech-decoding
tags: [speech-BCI, brain-to-voice, intracortical, Utah-array, ALS, multimodal-transformer, RVQ, adversarial, LPCNet, real-time, BrainGate2]
---

## 解决了什么问题
脑-文本(brain-to-text)已能高准确率通信,但要等整句说完、由语言模型定稿再读出——延迟、需盯屏、无语调。脑-语音(brain-to-voice)直接实时合成声音,但此前合成语音**可懂度不足**:前作 SOTA(同队 Wairagkar 2025)让普通听者转写的词错率仍达 43.75%,ECoG 路线更高(54.4%–58.8%)。本文要把"实时"与"听得懂"同时做到。

## 核心方法
一个**多模态因果 Transformer**(8 层,causal masking,每 10 ms 只用过去信号),从皮层内神经特征并行预测**四路互补目标**:①连续 LPCNet 声学特征(回归,给自然音质);②离散声学 token(自定义 RVQ,8 码本×128 中心,分类,把细节钉成不可糊的类别);③音素(分类,注入语言身份);④自监督掩码重建头(免标签,在小数据下加固共享表示)。另加**多尺度判别器**(1×/4×/16×/32× = 10/40/160/320 ms)做对抗训练,专罚"糊",逼出承载可懂度的辅音等高频/短促细节。连续头 + 离散头经声码器出声。参与者 **T15**(45 岁 ALS 重度构音障碍,BrainGate2),4 块 64 通道 Utah 阵列/256 电极植于左侧腹侧语音运动皮层(v6v/d6v、M1、55b);在前作数据集(8,489 试次)上训练与评测。

## 关键数据
- **听者转写词错率(连续输出)5.24%**、PER 3.96%;**79% 句子零错(0% WER)**;相较前作 SOTA 43.75% 约降到 1/8(8× 提升)。均为 **7 名听者中位数**。
- 合成 vs 目标 波形/频谱相关 **r=0.93**(连续)/0.92(离散);客观音质 40-Mel r=0.93、MCD 0.94 dB,远优于前作(r=0.83、MCD 2.89 dB;去词间静音后计算防虚高)。
- 原始音素错误率(因果)7.03%,与脑-文本相当。
- **物种/样本:人类单被试 T15**;"实时"为**模拟实时的离线评测**(因果 800 ms 滑窗、留出 128 benchmark 试次),非在线闭环会话。

## 为什么是 milestone
把脑-语音合成的**可懂度**首次做到接近可用(听者 WER≈5%),跨过了此前一直卡住的"实时但不够可懂"这道墙,并给出一套可复现的方法学骨架(多路互补目标 + 多尺度对抗解决回归损失抹糊辅音的根本问题)。是 [[wairagkar-2025-instantaneous-voice-synthesis]](同队 80ms 流式前作)的直接续作,两者串成"脑-语音:从流式但不够可懂 → 可懂"的纵向线;与皮层表面 ECoG 路线([[metzger-2023-speech-avatar-neuroprosthesis]]、Littlejohn 2025 流式)形成模态对照,支持"皮层内更高分辨率有利于实时可懂语音"。局限:单被试、尚未在线闭环验证、跨患者/更大词表迁移未证。
