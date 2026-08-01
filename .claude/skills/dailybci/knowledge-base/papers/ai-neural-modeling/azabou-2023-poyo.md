---
title: "A Unified, Scalable Framework for Neural Population Decoding"
authors: Azabou, Arora, Ganesh, Mao, Nachimuthu, Mendelson, Richards, Perich, Lajoie, Dyer
year: 2023
venue: NeurIPS 2023
url: https://arxiv.org/abs/2310.16046
subfield: ai-neural-modeling
tags: [POYO, foundation-model, multi-session, spike-tokenization, unit-embedding, PerceiverIO, few-shot, transformer, NeurIPS]
---

## 解决了什么问题
把多次神经记录并进一个模型，卡在一个结构性障碍上：**每次记录来自不同动物的不同神经元，彼此没有对应关系**。传统做法把一次记录整理成固定长度的群体向量（输入维度 = 该次记录的神经元个数），于是换一次记录维度就对不上、神经元身份也无从匹配，模型无法复用。这条障碍直接堵死了"用更大模型 + 更大数据集做神经解码"这条路。

## 核心方法
**把单个动作电位当作 token。** 放弃固定长度的群体向量，改为把数据集中每一次发放拆成一个 token，token 携带两件事：**是哪个神经元发的**（该神经元的可学习嵌入向量，unit embedding，把细胞身份编码进一个共享空间）与**什么时候发的**（保留精细时间结构）。一次记录因此变成**变长的 token 序列**，神经元个数不再影响输入格式。

**再用 cross-attention + PerceiverIO 主干**把变长的发放 token 序列压成固定数量的**潜在 token**，在潜在空间里完成群体活动的表征与解码。

**迁移方式是这套框架的落点**：预训练模型可快速适配到**神经元对应关系未知**的新 session，只需少量标签即可达到 few-shot 性能——实践上等价于冻住主干、只为新单元学嵌入。

## 关键数据
- 大规模多 session 模型，训练数据来自 **7 只非人灵长类**
- 跨 **158 个以上记录 session**、**27,373 个以上神经单元**、**100 小时以上**记录
- 多个任务上验证：预训练模型可快速适配到未见过、且神经元对应未指明的新 session，少量标签即达 few-shot 性能

## 为什么是 milestone
**"跨 session 对应问题"的解法从此有了一个通用范式。** 在此之前，跨 session 建模主要靠 per-session 的读入/读出矩阵（[[pandarinath-2018-lfads]] 的 dynamic neural stitching）或 session/context 标记（[[ye-2023-ndt2-multi-context]]）；POYO 把粒度下沉到**单个神经元**——每个细胞在共享空间里有自己的嵌入向量，于是"新 session 有一批陌生神经元"退化成"给这批神经元学几个向量"。后续 [[azabou-2024-mtm-universal-translator]]（三维度掩码自监督）与 [[azabou-2025-poyo-plus]]（多任务、跨脑区与细胞类型、并扩到钙成像）都建立在这套 tokenization 之上。

**归位（评估这条线时先过一遍）**：POYO 属于 **stitching（跨 session 缝合）** 路线。这条路线的信息来源是**结构假设**（存在跨 session、跨动物共享的计算结构，每个神经元的角色可用一个向量表示）**加锚点**（共同任务/刺激、session 标记、重叠单元），**不来自模型容量本身**。因此它买到的是可在留出数据上验证的迁移与解码增益；**买不到**从未同时记录的神经元对之间的协同波动——噪声相关、Granger 因果、共享潜在变异这类量依赖联合分布中超出边缘的部分，在分次记录下**不可辨识**，只能靠模型推断而非测量。与 [[chang-2026-neuropixels-quadbase]] 那种"直接扩大同时记录容量"是互补而非替代的两条解法。
