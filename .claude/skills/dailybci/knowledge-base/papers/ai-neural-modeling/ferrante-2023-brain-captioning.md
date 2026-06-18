---
title: "Brain Captioning: Decoding human brain activity into images and text"
authors: Ferrante, Boccato, Ozcelik, VanRullen, Toschi
year: 2023
venue: arXiv (preprint)
url: https://arxiv.org/abs/2305.11560
subfield: ai-neural-modeling
tags: [brain-captioning, fMRI, neural-to-text, CLIP, ControlNet, NSD, image-text]
---

## 解决了什么问题
视觉重建主要产出"图像"。但很多语义内容更适合用**文字描述**表达。能否把脑活动直接解码成一段**自然语言 caption**（而不只是图像），并用文本反过来引导更好的图像重建，是这条线向语言侧的延伸。

## 核心方法
Toschi/VanRullen 组（与今天候选 2 "Retrieval-Based Brain Decoding" 同一 Toschi 线）。用正则化线性回归把 fMRI 映射到图像/文本特征，接一个图像描述（captioning）模型生成文字 caption；图像侧再用 ControlNet 引入深度图引导、配 Stable Diffusion 生成布局更合理的图像。数据用 NSD。

## 关键数据
- 论文报告其 brain captioning 在描述质量指标上优于当时对比方法；图像重建在空间关系上更合理。
- 文本 caption 与图像重建互为补充（文字补语义、深度图补结构）。

## 为什么是 milestone
把"神经→文本 caption"作为独立产物确立下来——是 2026 年 NEURRATOR"把神经活动旁白成自由文本"在视觉侧最直接的祖先（NEURRATOR 把它从人类 fMRI/体素级推进到小鼠**单神经元**级 + 细胞类型探针 + 零语言端训练）。语言侧的非侵入祖先见 [[tang-2023-semantic-language-reconstruction]]。
