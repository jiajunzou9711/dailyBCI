---
title: "Shared computational principles for language processing in humans and deep language models"
authors: Goldstein, Zada, Buchnik, Schain, Price, Aubrey, Nastase, Feder, Emanuel, Cohen, et al.
year: 2022
venue: Nature Neuroscience
url: https://doi.org/10.1038/s41593-022-01026-4
subfield: brain-encoding-models
tags: [ECoG, GPT-2, GloVe, pre-onset-encoding, predictive-processing, encoding-model, contextual-embeddings, natural-listening]
---

## 解决了什么问题
「大脑会预测下一个词」长期靠 N400 一类的证据支持，而 N400 测的是词出现**之后**的反应，与两种说法都相容：大脑事先算好了预期，或大脑等词到了才做整合。本文把观测窗口移到 **word onset 之前**，检验神经活动里是否已经存在关于尚未出现的那个词的信息。

## 核心方法
颅内 **ECoG**，**九名被试、1,339 个电极**，听自然叙述（播客）。编码模型：自变量是每个词的嵌入（**50 维**），线性回归解出 50 个 β 系数得到重建信号，与实测信号求相关；**每个时间偏移、每个电极各拟合一次**，25 ms 滑窗，词的 onset 记为偏移 0，反应在 200 ms 窗口内平均后输入模型。由此得到预测相关随偏移变化的曲线。用静态嵌入（GloVe）与上下文嵌入（GPT-2）分别做。

## 关键数据
- **编码表现在 word onset 之前就开始上升**；原文把词前那一段标为 predictive signal，并指出 −100 ms 及更早的偏移只包含该词被感知之前采集到的神经信号（Fig. 3b）。
- GloVe 嵌入下达到显著相关的电极 **N=160**（Fig. 3c）；GPT-2 上下文嵌入 **N=208**（Fig. 6a）。
- **上下文嵌入（GPT-2）在词前明显优于静态嵌入（GloVe）**；把上下文嵌入按词平均、去掉局部语境后，表现降到接近静态嵌入；打乱语境后更低（Fig. 6b）。
- 词前的编码在**不含语境的静态嵌入**下同样存在——Fig. 3b 那条曲线本身就是 GloVe 的结果。

## 为什么是 milestone
它把「大脑是否在预测」这个长期靠事后成分支撑的问题，改造成一个**在词出现之前的时间窗里可测的量**，并给出了这条路线必须处理的混淆：上下文嵌入按设计就把先前词的信息编码进了当前词的向量，所以词前的相关可能**经由前文这个共同来源产生**，中间不需要任何预测。[[nastase-2026-language-population-code]] 转述了三重排除该混淆的后续分析（换用不含语境的嵌入、去掉高度可预测的双词搭配、把前面几个词的嵌入回归掉），并指出词前的编码**不能直接迁移到词后的神经活动**，因此它不是把该词的表征提前激活了一遍。

**⛔ 强度边界（必读）**：这套结论**存在正面反驳**，尚无定论。Schönmann 等 2026（eLife 14:RP106543）主张仅凭刺激依赖关系就能解释自然听觉设计中的词前脑编码，无需诉诸下一个词预测；Azizpour 等 2026（eLife）主张词前神经编码并不反映提前激活。引用本文任何词前结果时都要带上这条。**属自引提示**：Nastase 为本文作者之一。与 [[goldstein-2025-unified-embedding-space]] 同组同路线。
