---
title: "Performance-optimized deep neural networks are evolving into worse models of inferotemporal visual cortex"
authors: Linsley, Rodriguez, Fel, Arcaro, Sharma, Livingstone, Serre
year: 2023
venue: NeurIPS 36:28873–28891
url: https://arxiv.org/abs/2306.03779
subfield: brain-encoding-models
tags: [encoding-model, brain-score, IT-cortex, macaque, task-optimization, negative-result]
---

## 解决了什么问题
[[yamins-2014-performance-optimized-models]] 确立的核心相关——物体识别性能越高、对 IT 的预测力越强——是整条任务优化路线的合法性来源。深度学习规模化之后，这条相关是否还成立，此前没有被系统重测。

## 核心方法
两条互补证据。① 直接取 Brain-Score 官网上三个公开 IT 数据集（刺激为灰度渲染物体图与自然图），评测 **104 个 DNN**。② 换一套**空间分辨**的新记录：两只猕猴，先用 fMRI 定位下颞叶（IT）的中外侧 ML 与后外侧 PL 面孔斑块，慢性植入 **32 通道多电极阵列**（猴 1：ML 32 + PL 31 个神经元；猴 2：ML 32 个）；高分辨率彩色自然图（各 14 张），每张在 16×16 或 7×7 的注视点网格上反复呈现 200 ms，得到每张图的空间激活图。神经数据取自 Arcaro, Ponce & Livingstone (2020, eLife, "The neurons that mistook a hat for a face")。按 Brain-Score 评测法（偏最小二乘回归、留出图评估、取模型最佳层）评 **135 个 DNN**。作者特意指出第二批刺激的统计分布比以往 IT 研究更接近 ImageNet，以排除"刺激分布不匹配"这一解释。

## 关键数据
- 两批数据方向一致：**随 ImageNet 准确率上升，对 IT 的预测准确率下降**，构成一条帕累托前沿式的取舍。
- 该取舍**不因**换更多训练数据、换 Transformer 架构、换自监督、或优化对抗鲁棒性而缓解。
- 用 neural harmonizer（把模型的特征重要性图对齐到人类 ClickMe 行为数据）训练的 6 个模型打破了这一取舍。

## 为什么是 milestone
它把 2014 年那条奠基相关在**当代模型跨度上反号**这件事做成了可复现的观测，是"对齐分数到底测什么"这一整条追问的起点之一。与 [[conwell-2024-inductive-biases-brain-predictivity]]（人类 fMRI，得到"无相关"）**强度不同、不可互换**：本篇是负相关。评价任何"更强的模型更像脑"的说法时先过这一条。
