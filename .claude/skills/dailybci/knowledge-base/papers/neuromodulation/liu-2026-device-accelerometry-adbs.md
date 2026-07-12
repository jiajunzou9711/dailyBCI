---
title: "Device-embedded accelerometry complements neural signals for tracking parkinsonian motor states"
authors: Liu T, Yao J, Abdi-Sargezeh B, ..., Denison T, Tan H, Neumann WJ, Starr PA, Little S, Oswal A
year: 2026
venue: bioRxiv 2026.07.08.737286
url: https://doi.org/10.64898/2026.07.08.737286
subfield: neuromodulation
tags: [adaptive-DBS, closed-loop, STN, beta-biomarker, aperiodic, accelerometry, Parkinson, RC+S, human]
---

## 解决了什么问题
自适应 DBS(aDBS)靠生理生物标志物实时推断运动状态、调节刺激；十余年来标准控制信号是 STN beta 功率(见 [[little-2013-adaptive-dbs-human]])。但该神经标志物有两个独立缺陷：① 关刺激时"总 beta"就混叠了方向相反的两个成分；② 开刺激后 beta 会被刺激本身改变。本文系统检验：植入器自带的加速度计能否作更稳健的控制信号。

## 核心方法
11 名特发性帕金森患者(UCSF)双侧 STN DBS，用研究级感知型系统 Medtronic Summit RC+S 记录 STN + 感觉运动皮层场电位(LFP) + 胸前 IPG 内置三轴加速度计，>1900 小时家庭日常记录(986h 无刺激 + 915h 持续刺激)；腕式 PKG(经 UPDRS 校准的客观器械)每 2 分钟给动作迟缓/异动评分作真值。用 FOOOF 把功率谱分解为周期/非周期成分；Random Forest 等回归从各特征集解码症状严重度。8/11 有植入加速度计数据。

## 关键数据
- **总 STN beta 是混叠信号**：周期 beta 随动作迟缓加重而升、非周期(1/f)offset 随之降，两者在总功率里部分抵消；周期 beta 单独才稳健追踪症状。
- **加速度计解码优于神经特征**：动作迟缓 Acc R≈0.49 vs 全部神经特征 0.44；异动 0.56 vs 0.47；两者合并最好(0.54/0.59)。绝对解码力 R²≈0.24–0.35(Random Forest)。
- **刺激下差异化退化**：持续 STN 刺激下，周期 beta 与症状相关性大幅缩水、跨半球符号翻转(解耦)；而 STN 非周期成分、皮层周期功率、皮层-STN 相干相对稳定；加速度计几乎不受影响，刺激下仍 Acc > 神经。

## 为什么是 milestone
首个在大规模人体慢性数据上系统指出 aDBS 的经典神经标志物(STN beta)同时存在"构造性混叠(关刺激即有，可用周期 beta 补救)"与"刺激致解耦(开刺激特有，无神经侧解法)"两个独立失效，并提出植入器自带加速度计作为**不受刺激污染的行为学(运动学)标志物**。把 [[little-2013-adaptive-dbs-human]] 确立的 beta-aDBS 范式往"控制信号该选什么"这一步推进；与 [[rosin-2011-closed-loop-dbs-superior]] 同属"闭环该读什么信号"的探索。局限：仅 11 人、真值(PKG)与胜出信号同为加速度学(存在同源性)。发生在 FDA 2025-02 批准首个商用 aDBS(Medtronic Percept/BrainSense，依赖 beta)之后，属对该获批范式的再审视。
