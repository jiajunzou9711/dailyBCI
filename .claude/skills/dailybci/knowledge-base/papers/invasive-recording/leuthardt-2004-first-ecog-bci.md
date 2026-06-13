---
title: "A brain-computer interface using electrocorticographic signals in humans"
authors: Leuthardt, Schalk, Wolpaw, Ojemann, Moran
year: 2004
venue: Journal of Neural Engineering
url: https://doi.org/10.1088/1741-2560/1/2/001
subfield: invasive-recording
tags: [ECoG, first-ECoG-BCI, 1D-control, motor-imagery, speech-imagery, Leuthardt]
source_review: "Restoring Speech Using Brain-Computer Interfaces (Annual Reviews of Bioengineering 2025, ref 44)"
---

## 解决了什么问题
EEG空间分辨率太低，intracortical电极创伤太大。ECoG（皮层表面电极）能否提供足够的信号质量用于BCI控制，同时保持比穿透式电极更低的风险？

## 核心方法
在4名接受癫痫监测手术的患者中，利用已有的ECoG电极网格记录皮层表面电位。患者通过运动想象和语音想象产生不同的ECoG模式，用于闭环1D光标控制。训练时间仅3-24分钟。

## 关键数据
- 首次证明ECoG可用于BCI闭环控制
- 4名患者在3-24分钟训练后达到74-100%准确率（1D二值任务）
- 开放实验中，高达180 Hz的ECoG信号编码了2D运动方向信息
- 运动想象和语音想象均可产生可控ECoG信号

## 为什么是 milestone
确立了ECoG作为BCI记录模态的"最优平衡点"——空间分辨率远高于EEG，创伤性远低于intracortical穿透式电极。ECoG不穿透脑组织，无胶质瘢痕问题，长期稳定性更有保障。这篇论文直接开创了后续Chang实验室的ECoG speech BCI路线（Moses 2021, Metzger 2023），也为Vansteensel 2016全植入ECoG BCI和Synchron Stentrode等提供了概念基础。
