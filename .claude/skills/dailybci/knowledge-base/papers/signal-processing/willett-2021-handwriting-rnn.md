---
title: "High-performance brain-to-text communication via handwriting"
authors: Willett, Avansino, Hochberg, Henderson, Shenoy
year: 2021
venue: Nature
url: https://doi.org/10.1038/s41586-021-03506-2
subfield: signal-processing
tags: [RNN, handwriting-decoding, brain-to-text, character-decoding, language-model, motor-cortex]
---

## 解决了什么问题
传统 motor BCI 用光标逐点选择字母，速度受限于二维指针控制。人的手写动作天然包含丰富的时间结构和字符序列信息。能否直接解码“想象手写”的神经动态，把 motor cortex 信号转成文字？

## 核心方法
作者让瘫痪参与者尝试手写字符，同时记录 motor cortex 活动。解码器用 RNN 将神经时间序列映射为字符概率，并结合语言模型修正输出。关键不是解码光标轨迹，而是把复杂的运动意图序列直接转成文本。

## 关键数据
- 达到约 90 字符/分钟的 brain-to-text 速度
- 原始错误率和语言模型校正后错误率显著低于传统点选方法
- 证明手写运动意图在瘫痪多年后仍可被稳定解码
- 将 motor decoding 转化为序列识别问题

## 为什么是 milestone
这篇论文是 BCI signal processing 的重要转折：它表明高性能通信不一定要通过“控制光标”实现，也可以直接解码结构化动作序列。RNN + language model 的路线后来直接影响 speech BCI，把 BCI 从连续控制问题推进到序列到文本问题。
