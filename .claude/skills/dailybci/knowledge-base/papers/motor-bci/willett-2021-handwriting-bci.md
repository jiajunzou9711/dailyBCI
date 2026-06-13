---
title: "High-performance brain-to-text communication via handwriting"
authors: Willett, Avansino, Hochberg, Henderson, Shenoy
year: 2021
venue: Nature
url: https://doi.org/10.1038/s41586-021-03506-2
subfield: motor-bci
tags: [handwriting, brain-to-text, fine-motor, RNN, Stanford-BrainGate, Shenoy]
---

## 解决了什么问题
之前的 communication BCI 依赖光标逐个选择字母（point-and-click），速度上限约 40 字符/分钟。人类自然书写远快于逐字母选择——能否直接解码手写字母的精细运动意图来实现更快的文字输入？

## 核心方法
在一名 C4 脊髓损伤患者运动皮层植入 Utah 阵列，让患者尝试（attempted）手写字母和符号。用 RNN 将每个字符对应的神经活动模式直接分类为字符身份。关键洞察：虽然患者手已瘫痪多年，但运动皮层中手写字母的神经表征仍然保留且高度区分——每个字母产生独特的神经轨迹。

## 关键数据
- 在线打字速度：90 字符/分钟（之前最佳 24.4 字符/分钟，提升 3.7 倍）
- 原始准确率 94.1%，加语言模型后 >99%
- 自由书写（非抄写）：73.8 字符/分钟，错误率 2.25%（加语言模型）
- 解码 26 个字母 + 标点 + 空格

## 为什么是 milestone
开辟了一个全新的 motor BCI 范式：不再是"指向目标"，而是"直接解码精细运动轨迹"。证明瘫痪多年后大脑仍保留极其精细的运动表征（单个字母级别），且这些表征可以被高精度解码。这一范式后来被同一团队扩展到语音解码（Willett 2023），成为当前最成功的 BCI 技术路线之一。
