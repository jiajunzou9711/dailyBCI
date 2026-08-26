---
title: "Linguistic coupling between neural systems for speech production and comprehension during real-time dyadic conversations"
authors: Zada, Nastase, Speer, Mwilambwe-Tshilobo, Tsoi, Burns, Falk, Hasson, Tamir
year: 2026
venue: Neuron 114:774
url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12927206/
subfield: brain-encoding-models
tags: [fMRI, hyperscanning, dyadic-conversation, GPT-2, encoding-model, brain-to-brain-coupling, theory-of-mind, default-mode-network]
---

## 解决了什么问题
被动听预先录好的材料这一类范式里，说话人一侧不存在。语言的基本形态是对话——两人轮流当说者与听者、实时调整。本文问：产出与理解是否共用一套编码，以及真实对话调动的是哪些脑区。

## 核心方法
**30 对被试（N = 60）**，同步 fMRI 实时对话，5 个 run，每次约 3 分 21 秒，提示语设计为逐步提高亲密度。词嵌入取自 **GPT-2 XL**。

把两个脑子连起来的做法：用被试 A **说话时**的数据训练体素/顶点级编码模型，**不重新训练**，直接生成预测序列，逐顶点去对被试 B **听的时候**的实际活动求相关。检验的是「A 在产出侧的编码模型能否预测 B 在理解侧的活动」。另做跨区域对的时间互相关。

## 关键数据
- 显著的说者—听者耦合出现在**右侧 pSTG 并延伸进 TPJ、MFG**，以及**双侧楔前叶/后内侧皮层（PMC）**。
- **右半球的说者—听者耦合强于左半球**——与语言加工通常的左侧优势相反。
- 多数区域对的耦合峰值在 **lag 0 ± 3 秒**。两处不对称：说者的**左侧 MFG 与 SMA 早于**听者的活动；说者的**右侧 aSTG、pSTG 晚于**听者。
- 上下文嵌入捕捉到的耦合超出经典语言网络，落在社会认知区域。

## 为什么是 milestone
它把脑—脑耦合从「两人被同一刺激同时驱动」推进到**模型化的、产出与理解之间的耦合**，并给出一个与被动听范式相反的空间格局：真实对话最强的对齐发生在右侧 TPJ 与 PMC 这类社会认知区域。作者的解读是，对话要求双方持续推测对方的想法和意图，这会调动社会脑，而传统范式调动不到。是 [[nastase-2026-language-population-code]] Case 4 的承重实证之一，与 [[zada-2025-crosslanguage-shared-space]] 互补（前者证明几何共享，本文刻画对齐发生在哪些区域）。

**⛔ 强度边界（必读）**：这是**模型相关性质的耦合**，不是因果证据。「右侧 TPJ 与心理化相关」来自既有文献的功能归属，本研究**没有单独检验心理化**。作者 Zada、Nastase、Hasson 与该 Perspective 作者重合，属自引。
