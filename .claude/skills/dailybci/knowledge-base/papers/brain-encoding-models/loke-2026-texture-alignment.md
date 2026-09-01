---
title: "Shared texture-like representations underlie deep neural network alignment with human visual processing"
authors: Loke, Sörensen, Groen, Cappaert, Scholte
year: 2026
venue: Current Biology 36:1–8
url: https://doi.org/10.1016/j.cub.2026.08.008
subfield: brain-encoding-models
tags: [encoding-model, RSA, EEG, human, texture-statistics, DNN-brain-alignment, dissociation]
---

## 解决了什么问题
DNN 能预测视觉皮层响应，通常被读作两边共享物体识别计算。但该读法已被两处观测削弱（[[linsley-2023-worse-models-of-it]]、[[conwell-2024-inductive-biases-brain-predictivity]]）。遗留问题是**成分归属**：对齐分数是多种成分叠加出的总量，究竟由哪一个成分撑着。此前无法回答，因为自然图片里纹理统计与物体形状绑在一起。作者自划边界：不是问脑有没有纹理表征（已确立），而是问对齐反映神经响应里的哪一个成分。

## 核心方法
非侵入式 **EEG**（分析用 17 个后部电极，Oz/O1…），人类 **52 人**进入统计（招募 57、排除 5；阿姆斯特丹大学）。刺激为 **200 张图**（THINGS-EEG2 留出测试集，200 个物体概念各一张）的三个版本：**原图** / **纹理合成**（由白噪声出发匹配 VGG-19 conv1_1 的 Gram 矩阵，保留局部统计、破坏全局形状）/ **只留物体**（去背景）。RSVP 呈现，每图 100 ms、SOA 200 ms、重复 20 次；任务为与内容无关的注视点变色检测（3% 试次）。模型侧 5 个架构（AlexNet、VGG-16、ResNet-18、ResNet-50、ViT-B/16）共 21 个初始化，权重冻结、取所有层激活。两侧各算 200×200 表征差异矩阵（RDM），用 weighted RSA + 岭回归比较（留出 15 名被试 + 100 张刺激、50 折），指标为 0–500 ms 内 Pearson r 的 AUC，按噪声天花板**上界**归一化（保守取法）。

## 关键数据
- 归一化后，**纹理合成约 85%** 的可解释方差 vs **原图约 44%**、**只留物体约 55%**（Friedman χ²(2)=37.68, p<0.001；两两 Wilcoxon 均 W=0, r=0.87, p<0.001，Bonferroni 校正）。五个架构一致，与其 ImageNet 准确率（约 51%→81%）无关。
- 对齐峰值在刺激后 **100–200 ms**（前馈窗口）。200 ms 之后原图与只留物体条件的噪声天花板更高，但 DNN 与之的差距更大。
- 跨条件泛化：预测原图 EEG 时，纹理特征峰值与原图特征相同（**r = 0.20 @ 138 ms**），原图特征 AUC 更高（W=17, p<0.001, r=0.78）；**纹理特征优于只留物体特征**（W=42, p=0.002, r=0.65）。
- 解码：单试次 EEG、多类 SVM 分 **200 类**（随机 0.5%），三种条件均显著高于随机。**物体信息最多的两个条件对齐反而最弱**；纹理合成落入"高对齐 / 低物体信息"象限（Fig 4）。
- 局限（作者自列）：① 100 ms RSVP + 正交任务可能偏向前馈；② 纹理合成同时打乱背景与物体纹理，无法分离两者；③ 17 个后部电极对深部（如前部下颞叶）不敏感（全电极排序不变）；④ 去掉全局形状也去掉了语义，200 ms 后的自上而下反馈可能被削弱。

## 为什么是 milestone
把"DNN–脑对齐"从程度问题改造成**成分归属**问题，并给出一个可操作的解法：造出只保留单一成分的刺激，看对齐跟着哪一个走。结论——对齐由纹理类统计撑着——同时解释了此前两处裂缝（准确率提升不带来对齐提升、未训练网络也有分）。**强度边界：削弱的是"对齐＝共享物体识别"这个解释，未证伪两边存在共同之处。** 另注：作者押纹理统计的动机之一是 DNN 的 texture bias（Geirhos 2019），而该说法已被 Burgert et al. (2025, NeurIPS Oral, arXiv:2509.20234) 用受控抑制框架提出异议（结论为 CNN 主要依赖局部形状）；本文结论不依赖该动机。
