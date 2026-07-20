---
title: "Stabilization of a brain–computer interface via the alignment of low-dimensional spaces of neural activity"
authors: Degenhart, et al.
year: 2020
venue: Nature Biomedical Engineering 4:672–685
url: https://doi.org/10.1038/s41551-020-0542-9
subfield: population-dynamics
tags: [unsupervised-alignment, BCI-stability, latent-space, recalibration-free]
---

## 解决了什么问题
记录不稳（通道更替、编码漂移）会让固定解码器逐渐失准。传统解法是让用户定期做**带标签的重新校准**，既打断使用又依赖用户配合。能否不要标签？

## 核心方法
利用一个关键事实：单神经元层面在变，但群体活动的**低维潜在空间结构**保持稳定。方法是把当天记录的神经活动重新**对齐**到参考日的低维空间——依据两者的统计/因子结构本身进行匹配，而**不使用新的行为或意图标签**，随后沿用原有解码器。

## 关键数据
- 在记录不稳定的条件下，该稳定器无需重新校准即可维持 BCI 性能。
- 属性：**无监督**——只用神经数据的内部结构，不需要新标签。

## 为什么是 milestone
它把"漂移可救"从原理变成可部署的工程方案，并划清了一条重要界线：**第三层（编码漂移）可靠对齐救回，第二层（物理包裹）救不回来。** 与 [[gallego-2020-long-term-stability-dynamics]]（流形长期稳定）互为表里：前者给出稳定的对象，后者给出对齐的方法。
