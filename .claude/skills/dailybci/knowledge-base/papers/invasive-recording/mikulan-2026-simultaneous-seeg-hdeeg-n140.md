---
title: "Simultaneous recordings link intracranial and scalp correlates of somatosensory awareness in humans"
authors: Mikulan, Zauli, Russo, Mannini, Del Vecchio, Albertini, d'Orio, Nobili, Sartori, Massimini, Avanzini, Pigorini
year: 2026
venue: bioRxiv
url: https://doi.org/10.64898/2026.10.03.756393
subfield: invasive-recording
tags: [sEEG, hdEEG, simultaneous-recording, N140, SAN, somatosensory-awareness, parietal-operculum, posterior-insula, BHA, LFP, volume-conduction, source-localization]
source_review: "DailyBCI 2026-10-13 日报选题（bioRxiv 48h 扫描）"
---

## 解决了什么问题
头皮 EEG 的 N140（正中神经刺激后约 140 ms 的负波，近年被重新解读为体感觉察负波 SAN）的颅内来源长期只靠源定位估计；颅内文献里岛盖–后岛叶的 tonic BHA（50–150 Hz）也被当作触觉觉察标记，但两者从未在同一被试、同一时刻直接对照。据作者检索，此前唯一同被试对照是 Allison 1992，低密度且多在术中麻醉下记录。

## 核心方法
人类，8 名癫痫术前评估患者（10 个 session），256 通道头皮 hdEEG（EGI）与立体定向深部电极 sEEG（DIXI，共 1306 触点）同步记录，两台放大器均 1000 Hz、由电刺激器向两台同时发 trigger 离线对齐；阈上（运动阈 110%）、不报告的腕部正中神经刺激。每人取 tonic BHA 最强的一个触点，比较 BHA、LFP 与对侧额颞头皮 EEG 的峰潜伏期、波形互相关与触点深度；头皮源定位前 15% 与 Avanzini 2016 的 99 人颅内 BHA 分布图做 Dice 比较；另重分析 Schröder 2021（24 名被试）近阈值头皮数据。

## 关键数据
- 27/1306 触点（2.06%）出现 tonic BHA，每人 1–7 个
- 峰潜伏期：BHA 96±19 ms → LFP 124±28 ms ≈ EEG 125±35 ms；BHA 早于 LFP 约 28 ms（t(7)=−3.19，校正 p=0.03），LFP–EEG 差约 1 ms 不显著
- LFP–EEG 互相关均值 0.76±0.17，触点每深 1 cm 降 0.27（p=0.02，n=8）；峰时差随深度二次增大（R²adj=0.63）
- 源定位与颅内 BHA 图 Dice=0.34（p=0.03，保留空间自相关的置换检验）；重叠还含一大片内侧面
- 近阈值重分析：感到 vs 没感到在 95–175 ms 有差异簇（p=0.017），只有感到条件偏离基线
- 单试次可检出：BHA 95±3%，LFP 74±16%（Wilcoxon p=0.0019）

## 为什么是 milestone
把一个从 1977 年起只靠源定位推定来源的头皮 ERP 成分，与颅内 LFP 在同一时刻逐毫秒对齐，给出 BHA → LFP → 头皮 EEG 的时间序列，并给出「触点越深、头皮越不像」的实测关系。**强度边界**：8 人、每人一个触点、位置由临床决定；证据为时程/波形/空间一致，属相关性，不排除其他来源（内侧面重叠、Allison 提出的额叶与内侧中央皮层）；本数据阈上无报告，N140=SAN 依赖跨数据集比较；单试次与感知的对应未测。对 BCI 的连接（作者未提）：头皮 >30 Hz 特征来源需核；岛盖 LFP / SAN 或可作人工触觉是否被感到的客观读数（推论）。利益相关：Massimini 为 Intrinsic Powers 联合创始人。
