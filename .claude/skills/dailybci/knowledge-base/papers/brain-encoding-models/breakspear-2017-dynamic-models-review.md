---
title: "Dynamic models of large-scale brain activity"
authors: Breakspear
year: 2017
venue: Nature Neuroscience 20:340–352
url: https://doi.org/10.1038/nn.4497
subfield: brain-encoding-models
tags: [whole-brain-model, neural-mass, dynamical-systems, review, milestone-source]
---

## 解决了什么问题
fMRI 与 EEG 测的是成千上万神经元的集体活动，但认知神经影像的分析长期在没有底层生物物理动力学模型的情况下进行。这篇综述回答：宏观层面的神经群体活动能否像流体力学、磁学那样用平均场（mean field）方法建立数学定律，从而对脑活动的**时间演化**做预测。

## 核心方法
综述性梳理，从平均场与神经场理论的基本假设讲起，串起神经质量模型（neural mass model）、神经场模型、全脑网络模型三层，并说明模型反演（从数据估计参数与似然）这一环如何把这些模型接到实测数据上。

## 关键数据
- 综述性文献，不报告新实验数据。
- 梳理出该框架已被用于建模的现象：癫痫发作、脑病、睡眠、麻醉、静息态网络、人类 alpha 节律，以及多模态数据融合。
- 指出其推广缓慢的原因既有技术层面（模型预测难以检验），也有历史与学科文化层面。

## 为什么是 milestone
本子领域**全脑动力学半条线的 milestone 抽取源**。它与编码模型线的分工要点明确：编码模型问"给定刺激，脑活动是什么"（前向映射），动力学模型问"给定当前状态，脑活动接下来怎么演化"（时间演化）。评估任何"预测脑活动动力学"的新工作时，需要先判断它落在这两问的哪一问上，以及是否引入了生物物理约束。
