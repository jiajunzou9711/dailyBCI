---
title: "Driving and suppressing the human language network using large language models"
authors: Tuckute, Sathe, Srikant, Taliaferro, Wang, Schrimpf, Kay, Fedorenko
year: 2024
venue: Nature Human Behaviour 8:544–561
url: https://doi.org/10.1038/s41562-023-01783-7
subfield: brain-encoding-models
tags: [encoding-model, closed-loop, language-network, fMRI, stimulus-synthesis, control]
---

## 解决了什么问题
编码模型一直只被当作**描述**工具：拟合得好，说明模型表征与脑表征对齐。但一个真正好的前向模型应当能被**反用**——由它挑出的新刺激，应该可以按预期调高或调低目标脑区的响应。这一步此前在人类高级皮层未被验证。

## 核心方法
先用 GPT 类模型的表征在 **1000 个**多样句子的 fMRI 响应上拟合编码模型，验证它能预测每个句子引起的响应幅度。再把编码模型当作搜索目标，从大规模句子池中挑出模型预测会**最大化**或**最小化**语言网络响应的新句子，拿到**新的被试**身上实测，看预测是否兑现。

## 关键数据
- 人类 fMRI；建模阶段 1000 个句子，验证阶段为未参与建模的新个体。
- 模型选出的新句子确实在新被试身上强烈驱动或抑制语言网络的活动。
- 对被选中句子的系统分析显示，**意外性（surprisal）与语言良构性**是决定语言网络响应强度的主要因素。

## 为什么是 milestone
把编码模型从"解释已记录的数据"推进到"**用非侵入手段控制高级皮层活动**"，这是编码模型能力的一次性质变化，也是本线与 BCI 主线最接近的一格：BCI 的输入侧（如何选刺激去驱动特定回路）此前几乎没有可计算的设计工具。评估任何"用模型指导刺激设计"的新工作时，这是应先过一遍的基准。
