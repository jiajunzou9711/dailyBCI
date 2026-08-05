---
title: "Ultrasound system for precise neuromodulation of human deep brain circuits"
authors: Martin E, Roberts M, Grigoras IF, Wright O, Nandi T, Rieger SW, Campbell J, den Boer T, Cox SML, Stagg CJ, Treeby BE
year: 2025
venue: Nature Communications 16:8024
url: https://doi.org/10.1038/s41467-025-63020-1
subfield: neuromodulation
tags: [TUS, human, LGN, phased-array, 256-element, fMRI, theta-burst, offline-effects, deep-target]
---

## 解决了什么问题

人体深部 TUS 一直用**单阵元换能器**（如 [[legon-2018-human-thalamus]]），聚焦受个体颅骨畸变影响大、靶点验证只能靠仿真。本文换硬件路线：用大规模相控阵 + 立体定向 + 个体化规划 + 实时 fMRI 监测，去争取真正可控的深部聚焦。

## 核心方法

**人类**。**256 阵元头盔式相控阵，555 kHz**；立体定向定位、个体化声学规划、刺激同时做 fMRI 监测。靶点为**外侧膝状体核（LGN）**，读数为 LGN 及其相连视皮层区域的 fMRI 活动。另做 theta burst 方案与靶点特异性对照实验。

## 关键数据

- TUS 与视觉刺激同时给时，被试**视皮层活动显著升高**，且**跨个体可重复性高**。
- **theta burst TUS** 方案产生稳健的调控后效：刺激后**视皮层活动降低，持续至少 40 分钟**。
- 对照实验确认这些效应**特异于所靶向的 LGN**。

## 为什么是 milestone

人体深部 TUS 的**硬件代际更新**（单阵元 → 256 阵元相控阵 + 实时 fMRI 验证），并把 [[verhagen-2019-offline-primate]]、[[zeng-2022-theta-burst-tus]] 那条离线/可塑性路线做到了人的深部核团上（≥40 分钟后效）。

**它同时是 [[scott-2026-tus-human-lgn-null]] 最重要的横向对照：同一年前后、同一物种（人）、同一靶点（LGN），Oxford 这套系统报告显著且可重复的效应，Stanford/UCSF 那篇扫 PRF 则三个读数均未检出。** 两者的差别集中在几处可指认的地方：换能器（256 阵元相控阵 vs 4 阵元深度可调）、读数（fMRI BOLD vs SSVEP + 心理物理）、靶点验证方式（实时 fMRI vs 事后声学仿真）、以及声学参数。**做这一期时，"为什么一个有一个没有"必须落到这些具体差别上，不能笼统说"结果不一致"。**
