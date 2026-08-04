---
title: "The neural architecture of language: Integrative modeling converges on predictive processing"
authors: Schrimpf, Blank, Tuckute, Kauf, Hosseini, Kanwisher, Tenenbaum, Fedorenko
year: 2021
venue: PNAS 118:e2105646118
url: https://doi.org/10.1073/pnas.2105646118
subfield: brain-encoding-models
tags: [encoding-model, language-model, fMRI, ECoG, next-word-prediction, noise-ceiling]
---

## 解决了什么问题
语言模型能预测脑响应已有零散报告，但缺少统一比较：不同工作用不同模型、不同数据、不同指标，无法判断哪一类模型更像大脑，也无法判断"更像"来自什么属性。

## 核心方法
整合建模：把 **43 个**计算模型（从静态词嵌入到 transformer）放在同一套人类语言理解数据上统一评测，数据同时包含 **fMRI、皮层脑电（ECoG）** 与行为（自定步速阅读时间）。再把模型在各类语言任务上的能力与其脑预测力做关联，看哪种能力解释得了脑相似性。同时提出用**跨被试预测**估计噪声上限，把原始相关归一化。

## 关键数据
- 人类；fMRI + ECoG + 阅读时间。
- 表现最好的 transformer 模型可解释句子诱发神经响应中**接近 100% 的可解释方差**（即接近噪声上限）。
- 模型在**下一个词预测**任务上的能力（而非其他语言任务上的能力）预测其神经与行为拟合度。
- 模型**架构本身**对神经拟合有实质贡献（即未经训练的架构已带来部分拟合）。

## 为什么是 milestone
把语言侧的编码模型从零散报告推成**可比较的基准问题**，并给出一个具体的机制性主张——与大脑对齐的关键属性是预测下一个词。它与 [[caucheteux-2022-brains-algorithms-converge]] 相互印证。注意边界：噪声上限的估法本身影响"接近 100%"这个说法的含义，引用时应带上"可解释方差"这一限定。
