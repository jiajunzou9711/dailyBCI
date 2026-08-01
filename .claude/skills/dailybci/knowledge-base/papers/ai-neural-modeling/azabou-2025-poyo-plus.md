---
title: "Multi-session, multi-task neural decoding from distinct cell-types and brain regions"
authors: Azabou, Pan, Arora, Knight, Dyer, Richards
year: 2025
venue: ICLR 2025
url: https://openreview.net/forum?id=IuU0wcO0mo
subfield: ai-neural-modeling
tags: [POYO+, foundation-model, multi-session, multi-task, Allen-Institute, transformer, ICLR, calcium-imaging, unit-embedding]
---

> **2026-07-30 更正**：本条早前版本有两处错误，已修。① url 曾误填 arXiv 2310.16046——那是前作 **POYO**（Azabou et al., NeurIPS 2023, *A Unified, Scalable Framework for Neural Population Decoding*），不是 POYO+；② 模态曾误写为 "spike 数据"——POYO+ 训练在 Allen Brain Observatory 的**双光子钙成像**数据上，故它需要额外编码响应幅值。前作 POYO 才是处理动作电位的。**知识库目前尚无 POYO(2023) 独立条目**，该条目待补。

## 解决了什么问题
能否在一个 Transformer 里同时处理来自不同脑区、不同细胞类型、不同解码任务的神经数据？此前的 multi-session 方法基本局限于相同脑区、相同细胞类型的 session。更底层的障碍是**跨 session 对应问题**：传统模型把一次记录整理成固定长度的群体向量（输入维度 = 神经元个数），换一次记录后神经元个数与身份都对不上，模型直接用不了。

## 核心方法
**tokenization 沿用前作 POYO（Azabou 2023）**：放弃固定长度的群体向量，把神经活动拆成**变长的 token 序列**——每个 token 携带"是哪个神经元"（该神经元的**可学习嵌入向量**，unit embedding）与"什么时候"（时间编码）。神经元个数因此不再影响输入格式；迁移到新 session 时可冻住模型主体、只学新单元的嵌入（POYO 称 unit identification）。这与 LFADS 的 per-session 读入/读出矩阵是同一件事的两种实现，粒度从 session 级细化到神经元级。

**POYO+ 在此之上加三样**：① **幅值投影层**，以处理常规时间序列——钙成像是连续荧光强度而非离散发放时刻，故须编码"多强"；② 统一处理跨脑区、跨基因标记细胞类型的异质记录；③ **多任务联合训练**（回归 / 分类 / 分割），损失为交叉熵与均方误差的加权和。

**架构为 PerceiverIO 式三段**：cross-attention 把变长 token 序列压到固定数量的潜在 token → 潜在 token 间 self-attention → 输出端用**查询 token**（= 任务嵌入 + session 嵌入 + 输出时刻，三者相加）在任意时刻读出。

## 关键数据
- 训练于 Allen Institute Brain Observatory **双光子钙成像**数据集，**>100,000 个神经元**，小鼠 **6 个脑区**，观看不同类型视觉刺激
- 跨多个脑区与基因标记细胞类型联合建模
- 多任务（分类 / 回归 / 分割）联合训练
- 规模化训练带来持续的性能提升
- **模型潜在表征自发地区分了不同脑区与细胞类型，尽管训练时从未被告知这些区分**
- ICLR 2025

## 为什么是 milestone
neural foundation model 方向最具雄心的工作之一，正面回答了"更多数据是否带来更好的解码"——答案是肯定的，并证明跨脑区、跨细胞类型的异质数据可被统一建模。

**归位（评估这条线时先过一遍）**：POYO+ 属于 **stitching（跨 session 缝合）** 路线，与 [[ye-2023-ndt2-multi-context]]、[[azabou-2024-mtm-universal-translator]]、[[pandarinath-2018-lfads]] 同族。这条路线的信息来源是**结构假设**（存在跨 session/跨动物共享的计算结构，每个神经元的角色可用一个向量表示）**加锚点**（共同刺激/任务 + session 嵌入），**不是模型容量本身**。因此它买到的是可在留出数据上验证的迁移与解码增益；**买不到**从未同时记录的神经元对之间的协同波动——那类量（噪声相关、Granger 因果、共享潜在变异）在分次记录下不可辨识，只能靠模型推断而非测量。此边界与 [[chang-2026-neuropixels-quadbase]] 走的"加硬件、直接扩大同时记录容量"构成互补的两条解法。
