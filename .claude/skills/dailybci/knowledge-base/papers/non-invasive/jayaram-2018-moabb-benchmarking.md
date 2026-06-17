---
title: "MOABB: Trustworthy algorithm benchmarking for BCIs"
authors: Jayaram, Barachant et al.
year: 2018
venue: Journal of Neural Engineering (15, 066011)
url: https://doi.org/10.1088/1741-2552/aadea0
subfield: non-invasive
tags: [benchmark, EEG, open-data, reproducibility, BCI-evaluation, MOABB]
---

## 解决了什么问题
EEG-BCI 算法研究长期存在"结果不可重复、不可比"问题——每篇论文用自己的数据、自己的预处理、自己的统计方式，导致算法优劣根本无法跨论文比较。同一算法在不同实验室报告的准确率差异可达 20% 以上，领域进展几乎无法客观衡量。

## 核心方法
将多个公开 EEG 数据集统一转换为同一格式，捆绑在开源 Python 包里（BSD 许可证）；为每个数据集定义标准化的预处理管线和评估协议；提供自动化统计比较框架，一行代码跑完多算法×多数据集×多被试的全矩阵对比，并输出 Bayesian 置信区间而非点估计。GitHub: NeuroTechX/moabb。

## 关键数据
- 初版聚合 12+ 公开 EEG 数据集，涵盖 motor imagery、P300、SSVEP 三大范式
- 项目持续维护，2024 年已扩展至 60+ 数据集、200+ 被试总量
- 统一测试后发现领域内多篇"SOTA"论文结果无法复现，揭示预处理选择对结果影响远大于算法差异

## 为什么是 milestone
EEGNet（Lawhern 2018）定义了"跨范式通用模型"的方向，MOABB 定义了"如何可信地验证它"——两者共同构成 EEG-BCI ML 研究的基础设施。EEGDash 的数据聚合逻辑直接继承自 MOABB 的 open-data + standardized-evaluation 理念，是 EEGDash 的直接前驱。没有 MOABB，就没有"700+ 数据集统一访问"的需求被清晰定义。
