---
title: "A wireless and battery-less 65,536-electrode subdural brain-computer interface"
authors: Jung, Kim, Park, Choi, Lee, Seo, Jeong, BISC Collaboration
year: 2025
venue: Nature Electronics
url: https://doi.org/10.1038/s41928-025-01509-9
subfield: electrode-hardware
tags: [BISC, subdural, wireless, battery-less, high-density, 65536-electrodes, ECoG]
---

## 解决了什么问题
高密度皮层表面记录受到两个瓶颈限制：电极数量越多，引线、封装和数据传输越难；系统越复杂，植入后的供电和长期可靠性越难。能否把超大规模电极阵列、片上选择读出、无线供电和无线数据传输集成到一个可植入的柔性 subdural BCI 系统里？

## 核心方法
BISC 系统把 65,536 个电极集成在柔性 subdural interface 中，并通过片上电子系统选择其中部分通道进行同步记录。系统采用无线供电和无线数据遥测，避免传统高密度阵列需要大量穿颅引线的问题。它的核心工程思想是：不把所有电极同时读出，而是在超大规模电极平面上动态选择最有信息量的通道。

## 关键数据
- 65,536 个 subdural 电极
- 最多 1,024 个同步记录通道
- 无线供电、无电池植入式设计
- 柔性阵列覆盖皮层表面
- 通过高密度空间采样提高可选信号源数量

## 为什么是 milestone
BISC 把高密度 ECoG 推到了一个新的工程数量级。它的重要性不是简单“电极更多”，而是提出了超大电极池 + 通道选择 + 无线系统集成的架构。对于未来临床 BCI，这种路线可能缓解传统 ECoG 空间分辨率不足的问题，同时避免穿透式电极的组织损伤，是皮层表面 BCI 硬件的一条重要扩展方向。
