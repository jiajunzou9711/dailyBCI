---
title: "A high-performance neuroprosthesis for speech decoding and avatar control"
authors: Metzger, Littlejohn, Silva, Moses, Seaton et al.
year: 2023
venue: Nature
url: https://doi.org/10.1038/s41586-023-06443-4
subfield: speech-decoding
tags: [ECoG, avatar, multimodal-output, high-speed, Chang-lab, UCSF]
---

## 解决了什么问题
Moses 2021 的 PANCHO 系统速度太慢（15 词/分钟），且只输出文本。自然交流不仅需要文字，还需要面部表情和语调——这些维度之前的 speech BCI 完全忽略。

## 核心方法
在同一名 PANCHO 患者的 ECoG 阵列上，用深度学习模型同时解码三个输出流：(1) 文本（通过 phoneme 序列解码），(2) 合成语音的声学参数，(3) 驱动虚拟头像面部动画的运动参数。训练数据来自患者的 attempted speech。1024 词词汇表。

## 关键数据
- 78 词/分钟（比 Moses 2021 提升 5 倍）
- 1024 词词汇表，词错误率 25%
- 同时驱动文本、语音和头像面部动作
- 首次实现 speech BCI 的多模态输出

## 为什么是 milestone
与 Willett 2023 同期发表在 Nature，两篇一起标志着 speech BCI 性能从"勉强可用"跃升到"接近实用"。Metzger 的独特贡献是多模态方向：证明了 ECoG 信号中不仅有语音内容，还有足够的面部运动信息可以同时驱动头像——这暗示未来的 speech BCI 可以恢复不仅仅是"说什么"，还有"怎么说"的表达维度。
