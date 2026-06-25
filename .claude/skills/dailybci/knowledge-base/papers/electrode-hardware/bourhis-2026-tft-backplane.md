---
title: "A Thin Film Transistor Backplane for Scalable Chronic Neural Interfaces"
authors: Bourhis, Vatsyayan, Tonsfeldt, Galton, Dayeh
year: 2026
venue: bioRxiv (preprint)
url: https://doi.org/10.64898/2026.06.23.733868
subfield: electrode-hardware
tags: [flexible, active-matrix, TFT, a-IGZO, ECoG-surface, multiplexing, chronic, encapsulation]
---

## 解决了什么问题
高通道数神经接口的真正瓶颈在"引线"而非电极：被动阵列一电极一根线（O(n)），通道数上千时连接器宽度、走线密度、多层金属化与柔性力学全部爆炸。把有源电路集成进阵列可把引线降到 O(√n)，但既有"柔性有源"路线（如 Viventi 2011 在猫脑的柔性有源 ECoG）依赖把硅纳米膜**转印**到柔性衬底，工艺脆、易裂，且硅的电学性能绑死在其晶体结构上，"做软"始终是妥协。

## 核心方法
借用有源矩阵显示（AMOLED）的思路：在聚酰亚胺上**直接沉积** a-IGZO（非晶氧化物）**双栅薄膜晶体管**，每个电极正下方就地放一个晶体管（像素内跨导放大），按行列分时复用（TDMA）寻址——256 通道（16×16 铂电极）只需约 32 根引出线。"非晶氧化物"使晶体管功能与衬底力学解耦，无需转印硅。配合器件结构/接触工程协同优化与陶瓷-聚合物（Al₂O₃/聚酰亚胺）多层薄膜封装。数字反馈在每个 TIA 输入端连续扣除直流偏置电流，提升动态范围并支持逐像素校准。

## 关键数据
- 阵列：256 通道，16×16 铂电极；100% 良率；像素端到端增益 >800 V/V（~90 µA 工作电流，Fig 1）。
- 热：开到最大电流/增益（~140 µS 跨导 / ~750 V/V 系统增益）时皮层表面温升明显低于慢性植入 2°C 上限；发热元件稀疏 + 1:16 分时复用（6.25% 占空比）摊薄功率。
- 封装：388 天加速老化（50°C 盐水 + 5V 应力）→ 该条件下实测约 15.4 年，Arrhenius 加速因子 ~2.5× 外推**投影寿命 >38.5 年**；无分层/裂纹/金属腐蚀。
- 在体（大鼠，硬膜外桶状皮层）：胡须诱发响应与同规格被动阵列（Intan）可比；慢性记录稳定跨 30 天（Day 2/7/10/13/16/23 成功，Day 31 因 headstage 损坏失败）；Day 2 高伽马峰值 z≈5σ。

## 为什么是 milestone
把"有源矩阵 + 复用破引线瓶颈"这条思路，从刚性硅（Neuropixels/Obaid）和"转印硅到柔性载体"（Viventi 2011）推进到**单片氧化物 TFT 直接长在柔性衬底**，并首次为这条柔性有源路线配齐慢性植入所需的两项关键证据（热负荷 <2°C、封装投影寿命 >38 年）。它在皮层电极版图中确立"柔性有源（非转印硅）"这一格：纵向接续 [[viventi-2011-flexible-ecog]]，横向与"硅基有源"(Neuropixels [[jun-2017-neuropixels]]、[[obaid-2020-cmos-microwire]])、"柔性被动"(Layer 7 [[hettick-2025-layer7-cortical-interface]]) 形成"衬底哲学"三分。当前局限：256 通道偏少、大鼠表面、麻醉诱发；考验在通道数标度、氧化物 TFT 噪声与长期稳定、临床转化。
