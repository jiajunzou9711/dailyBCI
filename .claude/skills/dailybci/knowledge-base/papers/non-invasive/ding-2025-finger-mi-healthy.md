---
title: "EEG-based brain-computer interface enables real-time robotic hand control at individual finger level"
authors: Ding, Udompanyawit, Zhang, He
year: 2025
venue: Nature Communications (16:5401)
url: https://doi.org/10.1038/s41467-025-61064-x
subfield: non-invasive
tags: [non-invasive, EEG, motor-imagery, finger-decoding, EEGNet, robotic-hand, deep-learning]
---

## 解决了什么问题
非侵入(头皮 EEG)脑机接口长期停在粗粒度手部控制——头皮 EEG 空间分辨率仅厘米级、容积导体糊化、手指在运动皮层表征高度重叠,使"逐指(individual-finger)"控制被默认是皮层内电极的专属。本研究问:**能否仅凭头皮 EEG 实时控制单根机械手指?**

## 核心方法
21 名健康、有 BCI 经验的受试者;头皮 EEG 记录运动执行与运动想象的个体手指活动,用紧凑卷积网络(EEGNet 系,见 lawhern-2018-eegnet)实时解码并驱动机械手做逐指运动,逐人 fine-tuning 提升性能。系统性分析了不同 EEG 节律对逐指解码的贡献。

## 关键数据
- 实时解码精度:2 指任务 **80.56%**、3 指任务 **60.61%**(健康熟练者)。
- 多种 EEG 节律均可贡献逐指解码;fine-tuning 进一步提升 BCI 表现。
- 证明 naturalistic、多手指级别的非侵入机械手控制可行。

## 为什么是 milestone
**首次证明非侵入头皮 EEG 可实时驱动 individual-finger 级机械手控制**,把"逐指"从皮层内电极的专属推进到非侵入路线,松动了"头皮 EEG 解不出单指"的长期共识。它是 He 组非侵入逐指线的起点,直接催生了 2026 年向 BCI-naïve 中风患者的推广(ding-2026-finger-mi-stroke,以同一范式得到 83.5%/61.4%,与本篇健康熟练者基本持平)。与皮层内逐指/手写解码线(willett-2021-handwriting-bci、willett-2024-finger-click-bci)形成"侵入 vs 非侵入"的对照锚点。
