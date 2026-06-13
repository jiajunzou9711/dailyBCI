---
title: "Reclaiming Hand Functions after Complete Spinal Cord Injury with Epidural Brain-Computer Interface"
authors: Liu, Shan, Wei, Li, Xu, Liang, Liu, Zhao, Hong (Dingkun Liu 一作; Bo Hong 通讯)
year: 2024
venue: medRxiv (preprint; clinical trial NCT05920174)
url: https://www.medrxiv.org/content/10.1101/2024.09.05.24313041v4
subfield: invasive-recording
tags: [epidural-ECoG, minimally-invasive, wireless, battery-free, SCI, China, NEO, Neuracle, rehabilitation]
---

## 解决了什么问题

植入式 BCI 长期面临"性能 vs 安全"的两难：皮层内微电极信号质量高，但会因电极位移和胶质瘢痕包裹而长期衰减、需频繁重校准；硬膜下 ECoG 直接压迫脑组织，有血肿、出血、水肿等风险。本研究（**人体**，一名 50 余岁、外伤致 C4 完全性脊髓损伤 AIS-A 的瘫痪患者）验证：把电极放在**硬脑膜外、不穿透硬膜**的折中路线，能否在保证长期安全的同时提供可用的解码性能，并进一步探究纯内源性神经活动能否驱动脊髓康复。

## 核心方法

NEO（Neural Electronics Opportunity）系统：硬币大小钛合金植入体嵌入颅骨凹槽，**无电池**，经皮线圈近场感应供电 + 无线双向传输 8 触点硬膜外 eECoG（采样 1 kHz，触点直径 3.2 mm、间距 8 mm）。术前用 fMRI（主动+被动抓握范式）定位手运动/感觉区规划电极，电极覆盖中央前回（BA6d）与中央后回（BA1）。解码采用空间-频谱黎曼几何（scale-invariant Riemannian）特征 + HMM 处理连续抓握的时序依赖，对长期幅值漂移和咀嚼 EMG 噪声鲁棒。BCI 解码抓握意图驱动气动手套，手套既是执行器，又把外周感觉反馈送回损伤段，构成"自上而下意图 + 自下而上感觉"的内源性脑-脊髓康复回路（不依赖外部电刺激）。

## 关键数据

- 校准仅 **10 分钟** → 解码准确率 94%（chance 77%），抓握事件 F1 0.8（chance 0.09）。
- 9 个月内抓握事件 F1 稳步升至均值 **0.91**，3 个月后超 0.9；黎曼方法长期稳定性优于线性/CSP。
- 有 BCI 辅助时 10 秒内移物成功率 **100% vs 无辅助 35%**（植入后 181–185 天）。
- eECoG 高伽马（55–95 Hz）信号 9 个月内**不衰反增**（Month1 vs Month6，p<0.001）；阻抗 15 周后稳定（<600 Ω 增幅）。
- 解码延迟 1.23±0.33 s（远低于 EEG-MI 的 2–5 s）；eECoG 抓握检测 F1 0.90 vs 同患者 EEG 仅 0.16。
- 抗咀嚼 EMG 噪声：黎曼方法误激活率 20%，线性/CSP 为 100%。
- 康复：ARAT 右手（对侧）+16 分、左手（同侧）+11 分；ISNCSCI 上肢运动 +5、感觉 +8；正中神经 SEP 早成分通道 5 增幅最大（+5.0 µV）。

## 为什么是 milestone

首个无线、无电池、硬膜外的人体植入式 BCI，把 eECoG 确立为介于头皮 EEG 与硬膜下 ECoG 之间的"第四类记录模态"（更安全且信号上限可达 200 Hz）。它首次展示仅靠患者内源性升/降神经活动即可驱动脑-脊髓康复，且在 9 个月家用中信号不降反升、免频繁重校准——直接成为后续中国 NMPA 商业获批（见 [[neuracle-2026-neo-nmpa-approval]]）的临床证据基础，并为半侵入路线扩展到高自由度控制（见 [[neo-2025-fine-grained-2d-cursor]]）铺路。对照 KB 中硬膜下/皮层内路线（[[chestek-2011-long-term-signal-stability]]、[[hochberg-2012-reach-grasp-robotic-arm]]）的长期衰减问题，提供了截然不同的安全-稳定权衡。
