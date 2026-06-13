---
title: "Speech synthesis from neural decoding of spoken sentences"
authors: Anumanchipalli, Chartier, Chang
year: 2019
venue: Nature
url: https://doi.org/10.1038/s41586-019-1119-1
subfield: speech-decoding
tags: [speech-synthesis, RNN, articulatory-kinematics, ECoG, two-stage-decoding]
---

## 解决了什么问题
之前的 speech decoding 工作要么只能解码离散的词/音素标签，要么直接从神经信号回归声学特征但效果很差。缺少一种方法能从脑信号生成连续的、可理解的完整语音。

## 核心方法
两阶段解码架构：(1) 用 bidirectional LSTM 从 ECoG 信号解码 articulatory kinematic trajectories（发音器官的运动轨迹，包括唇、舌、下颌、喉）；(2) 再用一个 decoder 将发音运动轨迹转化为声学输出（mel spectrogram → WaveNet vocoder）。关键思路：不直接从神经信号跳到声音，而是经过一个"发音运动"的中间表征，因为皮层编码的本来就是运动指令而非声学特征。

## 关键数据
- 5名癫痫患者术中 ECoG 记录
- 合成语音的可理解度：听者能在闭合选项中以显著高于随机的准确率识别合成句子
- 证明了两阶段方法（神经信号→发音运动→声音）显著优于直接方法（神经信号→声音）

## 为什么是 milestone
首次证明从人类脑活动可以合成出完整的、可理解的语音句子。更重要的是，它确立了"两阶段解码"范式（先解码运动意图，再转为声音），这个架构被后续几乎所有高性能 speech BCI 采用。Chang 实验室后续的 Moses 2021、Metzger 2023 等临床工作都延续了这个思路。
