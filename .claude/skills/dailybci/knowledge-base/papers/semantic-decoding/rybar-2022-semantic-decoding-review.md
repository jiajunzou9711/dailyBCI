---
title: "Neural decoding of semantic concepts: a systematic literature review"
authors: Rybář M, Daly I
year: 2022
venue: Journal of Neural Engineering
url: https://doi.org/10.1088/1741-2552/ac619a
subfield: semantic-decoding
tags: [semantic-decoding, review, systematic-review, PRISMA, milestone-extraction-source, information-transfer-rate]
---

## 解决了什么问题

语义解码（从神经记录里读出人此刻正在想的是哪个概念）此前散落在 fMRI、MEG、EEG、iEEG 各模态的文献里，没有统一的横向梳理，也没人系统量化过"这些解码器到底有多大信息带宽"。本文按 PRISMA 流程做了跨模态的系统综述，作者自陈是**该主题第一篇跨神经成像模态、且以量化解码器效能为重点的文献综述**（此为作者原文表述，非本知识库独立核实的最高级判断）。

## 核心方法

按 PRISMA 指南检索 PubMed + Google Scholar 的同行评议报告，评估纳入资格。综述沿三条线组织：具体的成像模态、实验设计、以及用于语义解码的机器学习流水线。关键的方法学贡献是用**信息传输率（information transfer rate，单位时间内解码器传递的信息量，BCI 领域的标准通信带宽指标）** 来统一衡量不同研究的解码器效能——这让 fMRI 的慢速高精度与 EEG 的快速低精度可以放在同一把尺子上比。

## 关键数据

- 发表于 *J Neural Eng* 19（2022 年 4 月 13 日），DOI 10.1088/1741-2552/ac619a，PMID 35344941
- 综述覆盖多模态（fMRI / MEG / EEG / iEEG），并讨论该领域当前的挑战与可能的解法
- 本条目是本知识库 `semantic-decoding` 子领域的 **milestone 抽取来源**：下列条目均取自本综述的引用列表——[[mitchell-2008-predicting-noun-meanings]]、[[liu-2009-fast-object-decoding-intracranial]]、[[simanova-2010-eeg-object-categories]]、[[wang-2011-ecog-semantic-decoding]]、[[huth-2016-semantic-maps]]、[[rupp-2017-ecog-semantic-attributes]]、[[pereira-2018-universal-decoder]]、[[nagata-2022-abstract-concrete-semantics]]、[[patterson-2007-semantic-knowledge-representation]]、[[ralph-2017-semantic-cognition-review]]

## 为什么是 milestone

它发在 *Journal of Neural Engineering*（BCI 领域的核心期刊）而非纯认知神经科学期刊，这个位置本身说明问题：语义解码在 2022 年已经从"认知神经科学的表征研究"被正式接编进**神经工程的解码议程**。用信息传输率作统一标尺，也把这条线的评价标准从"分类准确率显著高于随机"推向"作为通信通道够不够用"——这正是判断任何语义 BCI 候选工作的正确坐标系。
