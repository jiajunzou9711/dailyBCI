---
title: "EEG Foundation Models: Progresses, Benchmarking, and Open Problems"
authors: Liu, Chen, Wu et al.
year: 2026
venue: arXiv 2601.17883 (Jan 2026)
url: https://arxiv.org/abs/2601.17883
subfield: ai-neural-modeling
tags: [benchmark, EEG, foundation-model, evaluation, cross-subject, few-shot, BCI, scaling]
---

## 解决了什么问题
EEG 基础模型（EEG-FM）数量激增，但各论文用不同预处理、不同评估协议，结果无从横向比较。哪个模型真的好？更大的模型真的更强吗？这些基本问题没有客观答案，阻碍了领域判断力。

## 核心方法
系统性综述 **50 个**代表性 EEG-FM，归纳统一的分类学框架（数据标准化 / 模型架构 / 自监督策略）。在统一协议下实测 **12 个开源 EEG-FM** + 竞争性专家基线，覆盖 **13 个数据集 × 9 种 BCI 范式**。评估维度：跨被试泛化（leave-one-subject-out）+ 快速校准（within-subject few-shot）；比较 full fine-tuning vs. linear probing；检验模型规模与性能的关系。

## 关键数据
- 综述涵盖 50 个模型，系统评测 12 个开源 FM × 13 数据集 × 9 范式
- 关键发现 1：**linear probing 普遍不足**——预训练表征在 EEG 上迁移性弱于 NLP/CV
- 关键发现 2：**从头训练的专家模型在多数任务仍有竞争力**
- 关键发现 3：**更大的 EEG-FM ≠ 更好的泛化**——当前数据规模和训练实践下 scaling 效益有限

## 为什么是 milestone
这是 EEG-FM 领域迄今最全面的"诚实体检"——它不鼓吹，它量化瓶颈。三个关键发现（linear probing 弱、专家模型仍强、scaling 效益有限）直接指出了 EEGDash 要解决的根本问题：**现有 EEG-FM 的局限源于训练数据不足、数据来源单一、跨数据集标准不统一**——而 EEGDash 提供的 700+ 数据集正是针对这三点的系统性回应。读这篇才能理解 EEGDash 的必要性。
