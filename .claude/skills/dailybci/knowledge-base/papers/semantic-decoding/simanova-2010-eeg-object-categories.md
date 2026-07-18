---
title: "Identifying object categories from event-related EEG: toward decoding of conceptual representations"
authors: Simanova I, van Gerven M, Oostenveld R, Hagoort P
year: 2010
venue: PLoS ONE
url: https://doi.org/10.1371/journal.pone.0014465
subfield: semantic-decoding
tags: [EEG, non-invasive, category-decoding, single-trial, multimodal-stimuli, ERP, human]
---

## 解决了什么问题

单试次范畴解码当时的漂亮结果基本都来自 fMRI。头皮 EEG（非侵入、便宜、时间分辨率毫秒级）能不能同样解出概念范畴？而且——同一个概念经**不同输入通道**进来（看到图、听到词、读到字），解码难度是否相同？后一个问题直接检验 [[patterson-2007-semantic-knowledge-representation]] 的模态无关枢纽假说在 EEG 上留没留下可读的痕迹。

## 核心方法

**电极模态：非侵入式头皮 EEG**（事件相关电位）。同一批物体概念以三种模态呈现：物体线描图、口头说出的名称、书面名称。分类器用带多元 Laplace 先验的贝叶斯逻辑回归（Bayesian logistic regression with a multivariate Laplace prior）——该方法同时给出对分类有贡献的特征的精确时间定位。

## 关键数据

- *PLoS ONE* 5:e14465（2010 年 12 月 30 日），DOI 10.1371/journal.pone.0014465，PMID 21209937
- **不同模态间分类性能差异显著（marked differences）**：物体线描图最高，**89% 试次正确分类**
- 听觉与正字法（书面词）模态结果更低，仅在**部分被试**上显著
- 分类方法可对贡献特征做精确时间定位

## 为什么是 milestone

它把范畴解码从 fMRI 推到非侵入 EEG，是这条线的非侵入侧起点。但更有价值的是它测出的**模态落差**：图片 89%、词汇模态掉到勉强显著。这个落差提示，EEG 上单试次可读的成分很大程度上是**知觉驱动**的，而不是模态无关的概念枢纽——真正抽象的语义表征要么信噪比太低、要么在头皮上看不见。这条观察一直贯穿到今天：颅内工作（[[nagata-2022-abstract-concrete-semantics]] 的抽象/具体二分 73.1%）之所以有价值，正因为它在**词义**而非图片上做，避开了"解出来的其实是视觉特征"这个混淆。评估任何语义解码结果时，第一个要问的就是：**这个准确率到底来自概念，还是来自刺激的知觉表面属性？**
