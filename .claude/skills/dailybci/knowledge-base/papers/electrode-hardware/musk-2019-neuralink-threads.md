---
title: "An integrated brain-machine interface platform with thousands of channels"
authors: Musk, Neuralink
year: 2019
venue: Journal of Medical Internet Research
url: https://doi.org/10.2196/16194
subfield: electrode-hardware
tags: [Neuralink, high-density, thin-film, robotic-insertion, wireless, 3072-electrodes, ASIC]
---

## 解决了什么问题
Utah 阵列已使用 30 年但仍是 100 通道级别，且需手术医生手动植入。BCI 需要更高通道数（1000+）、更细的电极（减少组织损伤）、以及全无线数据传输。需要一个集成化的下一代 BCI 硬件平台。

## 核心方法
Neuralink 开发了全集成 BCI 平台包括三个核心创新：（1）柔性聚酰亚胺薄膜电极"线"（threads），每根宽 4-6μm，远细于人发，每根线上分布多个电极位点；（2）定制手术机器人，能自动避开血管精确插入线程；（3）定制 ASIC 芯片（N1 传感器），集成 1024 通道同时放大、数字化和无线传输。

## 关键数据
- 3,072 个电极位点，分布在 96 根线程上（每根 32 个电极）
- 定制 ASIC 支持 1,024 通道同时读出
- 单根线程宽度 4-6μm（人发约 75μm）
- 手术机器人每分钟可插入 6 根线程（192 电极）
- 定制 ASIC 采样率 19.3 kHz/通道
- 全系统功耗 ~6mW（可无线供电）

## 为什么是 milestone
首次提出并实现了完整的高通道数全无线 BCI 硬件平台，将电极数从 100 提升到 3,072（1,024 通道同时读出）。手术机器人自动化植入的理念为 BCI 的规模化临床部署扫清了手术瓶颈。虽然当时未做人体试验，但这篇论文重新定义了 BCI 硬件的工程目标，推动整个领域进入"千通道时代"。
