---
title: "Simultaneous speech and gesture decoding for multimodal communication in paralysis"
authors: Brosler, Liu, Silva, Hallinan, Kurtz-Miott, Dunkel Wilker, Tu-Chan, Ganguly, Chang
year: 2026
venue: Nature Neuroscience
url: https://doi.org/10.1038/s41593-026-02446-2
subfield: speech-decoding
tags: [ECoG, multi-effector, simultaneous-decoding, gesture, avatar, Chang-lab, UCSF, BRAVO]
---

## 解决了什么问题
此前 BCI 多数一次只解码一种行为；皮层内记录已发现同时做两件事会干扰解码（Deo 2024 双手、Singer-Clark 2025 说话降低腹侧中央前回光标控制）。ECoG（场电位）上同时解码语音与上肢手势是否也受干扰、怎么处理，此前基本未检验。

## 核心方法
人类 3 名重度瘫痪者（2 脑干卒中、1 ALS；BRAVO 试验 NCT03698149），左半球感觉运动皮层硬膜下 253 触点高密度 ECoG（3 mm 间距），有线经皮基座。三种任务：只说 / 只比 / 边说边比（Bravo-6：10 短语 × 10 手势）。语音与手势为两个独立并行的卷积 + 双向 GRU 分类器，各输出 10 类 + 静息，特征为高 γ（70–150 Hz）+ 1–100 Hz 低频。比较三种训练数据（只单独做 / 只边说边比 / 混合），以及「交叉模态」静息类（另一种行为的试次标成静息）。

## 关键数据
- 两种行为都显著的触点：Bravo-6 64/170、Bravo-1r 39/146（图 2e，约 38% / 27%，自算），集中于中央前回
- 只用单独做的数据训练 → 边说边比漏检率 14.5%（Bravo-6）/ 34.9%（Bravo-1r）；混合训练后各试次漏检 0.8%–4.5%
- 静息类只用真静息 → 对另一种行为误触发 30.6% / 76.0%；交叉模态训练后 0.0%
- 情境匹配效应在训练量相同时仍成立（补充 S5）；混合训练的数据总量未说明
- 未见过的短语–手势组合：手势 66.7% vs 65.8%（P=0.29），语音 80.0% vs 79.3%（P=0.35），仅 Bravo-6
- 实时（Bravo-6）：只比 81.8%；边说边比手势 66.0% / 语音 70.0%（离线 68.8% / 77.5%）；对话范式 85.0% / 75.0%（仅 20 试次）；机会 9.1%

## 为什么是 milestone
把「多效应器同时解码会互相干扰」从皮层内延伸到 ECoG，并给出只改训练数据（情境混合 + 交叉模态静息标签）即可压低漏检与误触发的做法；是 Metzger 2023（语音 + 面部化身）之后同组把输出扩到上肢手势与全身化身的一步。边界：同时解码只 2 名被试、实时只 1 名；词表最多 10×10；按开始信号的试次制分类，非连续自主解码；Bravo-6 手势为想象。
