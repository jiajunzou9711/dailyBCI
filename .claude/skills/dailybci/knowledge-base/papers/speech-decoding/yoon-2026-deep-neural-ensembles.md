---
title: "Neural decoding of speech using deep neural ensembles"
authors: Yoon, Avansino, Madugula, ... Pandarinath, Henderson, Willett et al.
year: 2026
venue: bioRxiv (preprint)
url: https://doi.org/10.64898/2026.06.02.729705
subfield: speech-decoding
tags: [speech-BCI, deep-ensembles, pseudoensembling, intracortical, real-time, brain-to-text, merger-LLM]
---

## 解决了什么问题
语音 BCI 当前的主要瓶颈是解码错误率，而非速度——错一个承载语义的关键词整句意思就翻车（自然语言遵循 Zipf 定律）。在公开的 Brain-to-Text '24/'25 竞赛中，深度集成（deep ensembles）贡献了相对基线最大的涨分（9 个超基线条目里 7 个用了集成），但此前只在离线刷榜验证过，从未在实时闭环中测试，且算力昂贵、在临床相关约束下的表现不明。

## 核心方法
构建实时闭环集成语音 BCI：本地部署 1 个解码器边说边出部分文本（低延迟反馈），同时神经特征经加密 VPN 流式上云，10 个从随机初始化独立训练的 RNN 解码器（各含音素解码 + 语言模型）在说完一句后并行推理，由一个微调过的 merger LLM 聚合成终稿。在 BrainGate2 被试 T12（双侧 6 片 64 通道皮层内微电极阵列，植入语音运动皮层 6v/55b）上做闭环测试。并提出 **pseudoensembling（伪集成）**：用 test-time augmentation——对单个解码器的输入注入随机高斯噪声造出多样化假设，近似整个集成，绕开多模型的算力/内存开销。

## 关键数据
- 在线闭环大词表（125k 词）WER **33.7% → 26.0%**（人类被试 T12，双侧皮层内阵列）；语速不变（~65 wpm），精度未以速度为代价
- 集成额外延迟 **5.25 秒/句**（merger LLM 占最大头 ~2.77s；神经读出 2.57s；音素解码 1.25s；LM 0.89s）
- 离线 3 被试（T12/T15/T16）、67.7 小时、4 种阵列配置，相对 WER 下降：T15 **35.0%**、T16 **31.1%**、T12 左+右 **27.6%**、T12 左 **23.1%**（均 95% CI 不重叠）
- 伪集成（单解码器）相对降错约 **9–17%**，追回完整集成收益的三到六成，算力降一个量级
- merger 聚合：更大的微调 LLM 更好，但启发式 ROVER 在算力受限时接近小 LLM；merger LLM 仅用 20 句微调数据也能超基线

## 为什么是 milestone
把语音 BCI 的优化轴从"纯精度"扩展到"可部署性"——首次把竞赛验证过的深度集成搬进真实实时闭环并诚实摊开算力/延迟代价，又用伪集成给出资源受限场景的轻量替代。相对 willett-2023（phoneme 路线可扩展）、card-2024（快速校准高准确率）这条"追精度"主线，这篇代表了下一步："如何把已有解码器组合到极致、并真正落到床旁。"
