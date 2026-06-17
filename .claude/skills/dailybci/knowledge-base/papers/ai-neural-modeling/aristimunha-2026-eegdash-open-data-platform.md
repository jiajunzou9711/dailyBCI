---
title: "An open-source platform for machine learning on public neurophysiological data (EEGDash / EEG-DaSh)"
authors: Aristimunha, Dotan, Guetschel, Jaiswal, Ashkenazi, Truong, Kokate, Majumdar, Shriki, Delorme et al.
year: 2026
venue: arXiv 2606.16041 (q-bio.NC)
url: https://arxiv.org/abs/2606.16041
subfield: ai-neural-modeling
tags: [open-data, EEG, MEG, iEEG, EMG, fNIRS, BIDS, data-infrastructure, foundation-model, benchmark, repair-layer]
---

## 解决了什么问题
脑电基础模型天生跨数据集，但"喂不进去的数据就训不了"。公开神经数据虽多，把单个数据集变成可训练输入往往要上千行代码 + 领域经验；且领域原以为"符合统一标准（BIDS）就能用"，实际并不成立。

## 核心方法
把 OpenNeuro/NEMAR 的公开 BIDS 数据集做成可导入、可查询的数据类：元数据优先 + 惰性访问（只下载模型真正消费的那段信号），自动修复层修掉格式缺陷让数据集照样能加载，信号处理/加载/验证全部委托上游（MNE-Python、Braindecode、官方 BIDS validator），只自有那层无人维护的元数据注册表并把修复回馈上游、不另开分叉。

## 关键数据
- 编目 791 个公开数据集、39,778 名受试者、86,051 小时，跨 EEG/MEG/iEEG/EMG/fNIRS 五模态（61 TB）
- 审计 OpenNeuro：仅 33.2%（182/548）通过 BIDS 验证；合规与可加载几乎不相关（Spearman ρ=−0.05，n=503）；66.8% 数据集至少报一个验证错误
- 修复层把可加载率 95.0%→95.8%，剩余 35 个完全打不开 + 58 个部分可加载显式标记；每个编目数据集零自定义代码即可进 PyTorch DataLoader

## 为什么是 milestone
把"EEG 缺数据"的领域共识修正为"缺把现有数据变得可用的能力"，是脑电基础模型（[[jiang-2024-labram]]、[[yang-2023-biot]]）落地一直缺的数据基础设施一环；承接 [[jayaram-2018-moabb]] 的开放数据 + 统一评估理念并把它从"几个精选数据集"扩到全量公开档案，同时量化了"合规 ≠ 可用"这一被忽视的盲区（呼应 [[liu-2026-eeg-fm-benchmark]] 关于数据是当前最大瓶颈的结论）。
