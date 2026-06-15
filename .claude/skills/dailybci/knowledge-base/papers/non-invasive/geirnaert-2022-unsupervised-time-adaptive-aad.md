---
title: "Time-Adaptive Unsupervised Auditory Attention Decoding Using EEG-Based Stimulus Reconstruction"
authors: Geirnaert, Francart, Bertrand
year: 2022
venue: IEEE Journal of Biomedical and Health Informatics
url: https://doi.org/10.1109/JBHI.2022.3162760
subfield: non-invasive
tags: [auditory-attention, EEG, unsupervised, time-adaptive, stimulus-reconstruction, deployment]
---

## 解决了什么问题
stimulus-reconstruction 的 decoder 通常需要逐被试的**有监督**训练——即需要带"此刻在听谁"标签的校准数据，这在真实佩戴场景里拿不到；而且神经响应会随时间漂移，固定 decoder 会退化。这是 AAD 落地的关键实用障碍。

## 核心方法
提出无监督、时间自适应的 AAD：不需要注意标签即可训练/更新 decoder，并让其随时间在线自适应，跟随非平稳的神经响应变化。

## 关键数据
- 无监督自适应方法的性能接近传统有监督 decoder。
- 能跟随时间漂移持续更新，避免固定 decoder 的性能衰减。

## 为什么是 milestone
直击 AAD 部署的两个核心痛点——免逐人标注校准 + 在线自适应，把 AAD 从"实验室里需标签训练"推向"可在用户耳上自我维持"。是这条线从原理验证走向真正可落地的实用化 milestone。承自基准框架 [[geirnaert-2021-aad-review-benchmark]] 与奠基方法 [[osullivan-2015-single-trial-eeg-aad]]。
