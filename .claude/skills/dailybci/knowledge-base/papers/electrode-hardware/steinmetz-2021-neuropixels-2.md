---
title: "Neuropixels 2.0: A miniaturized high-density probe for stable, long-term brain recordings"
authors: Steinmetz, Aydin, Lebedeva, Okun, Pachitariu, Bauza, et al.
year: 2021
venue: Science 372:eabf4588
url: https://doi.org/10.1126/science.abf4588
subfield: electrode-hardware
tags: [Neuropixels, silicon-probe, four-shank, chronic, drift-correction, high-density]
---

## 解决了什么问题
[[jun-2017-neuropixels]] 把单根探针推到 960 个电极点 / 384 个同时通道，但它是**单针脚**：一次插入只能覆盖一条深度线上的脑区，横向要靠多插针。同时，慢性植入下的**组织漂移**会让同一个神经元在不同天落到不同电极点上，长期追踪困难。

## 核心方法
四针脚版本：**4 根针脚、共 5120 个电极点**，同时读出通道数**仍为 384**（可由片上开关在 5120 个点里选）。探针体积与重量大幅缩小以适配慢性植入，并配套提出利用高密度采样做**漂移校正**、跨天追踪同一批神经元的分析方法。

## 关键数据
- **5120 个电极点 / 384 个同时通道 / 4 针脚**（针脚长 10 mm）。
- 噪声规格 **6.8 μVrms**（后续工作引用此值作对照基准）。
- 支持慢性植入与跨天单神经元追踪。

## 为什么是 milestone
它确立了此后成为事实标准的那一组规格（4 针脚 / 5120 点 / 384 通道），也把 Neuropixels 的能力从「一条深度线」扩展到「四条并排的深度线」。**它同时留下了本线的下一个瓶颈**：电极点数远多于同时通道数，用户必须在「集中一根针脚深度密采」与「摊到四根针脚覆盖面广」之间取舍。这个取舍正是 [[chang-2026-neuropixels-quad-base]] 要消掉的东西——后者保留全部几何与 5120 点不变，只把同时通道从 384 提到 1536。
