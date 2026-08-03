---
title: "An instantaneous voice-synthesis neuroprosthesis"
authors: Wairagkar M, Card NS, Singer-Clark T, Hou X, Iacobacci C, Hochberg LR, Brandman DM, Stavisky SD, et al.
year: 2025
venue: Nature 644:145-152
url: https://doi.org/10.1038/s41586-025-09127-3
subfield: speech-decoding
tags: [voice-synthesis, brain-to-voice, low-latency, closed-loop-audio, prosody, intracortical, Utah-array, ALS, BrainGate2, UC-Davis]
pmid: 40506548
---

> **⚠ 2026-08-02 更正：** 本条目此前误挂了 Littlejohn et al. (2025, Nat Neurosci 28:902-912) 的题名/期刊/DOI。二者是 **2025 年两篇不同的 brain-to-voice 论文**——本条是 UC Davis 组的皮层内路线，Littlejohn 那篇是 UCSF/Berkeley 的 ECoG 路线，见 [[littlejohn-2025-streaming-brain-to-voice]]。引用时勿混。

## 解决了什么问题

在此之前的高性能语音 BCI 输出的是**文本**，等整句解码完再显示。这条路线丢掉了语音里全部的**副语言信息**——语调、重音、语速，也就无法表达疑问、强调、情绪。而且延迟到秒级，插话、接话这类正常对话行为不可能。

## 核心方法

从植入**腹侧中央前回**的 **4 片阵列共 256 个微电极**记录皮层内活动，直接合成语音波形而不经过文本这一层，并把合成的声音**实时回放给参与者本人**（闭环音频反馈——参与者能听见自己"说"出来的话）。除音素内容外，另从神经活动中提取副语言特征。

## 关键数据

- **参与者**：人类**单被试 T15**（男性，ALS 伴严重构音障碍）。
- **延迟**：原始神经信号到合成语音样本 **10 ms 内**；端到端累计延迟约 **80–130 ms**（取决于音频驱动设置）。
- **相似度**：合成语音与目标语音的 Pearson 相关，评估会话上均值稳定 **>0.8**（956 个出声句试次）。
- **可懂度**：人类听者在**六选一**句子辨识任务中中位准确率 **100%**。**注意这是闭合选项任务，不等于开放转写**。
- **音素错误率 43.6%**；词错误率低于该参与者自身残余的构音障碍语音。
- **副语言控制**：可调**语调**（陈述 vs 疑问）、**词重音**、**三级音高**（据此唱出旋律）、**语速**。
- 覆盖任务含拟音（58 试次）、自主应答、**未训练的伪词**（79 试次）、拼写（31 试次）、感叹词（61 试次）。

## 为什么是 milestone

把语音 BCI 的输出从"打字"推向"说话"：**副语言维度首次被证明可从皮层内活动实时解出**——语调、重音、音高不是文本能承载的东西，这一步扩的是**表达带宽**而非准确率。闭环音频反馈也让参与者第一次能听见自己的声音，这对使用体验与在线调整的意义尚待系统评估。

**边界要讲清**：单被试；可懂度的强结果来自**六选一闭合任务**，开放转写的音素错误率仍有 43.6%——这一格由同队续作 [[wairagkar-2026-brain2voice2-voice-synthesis]] 推进（听者转写 WER 5.24%）。与之并行的 ECoG 路线见 [[littlejohn-2025-streaming-brain-to-voice]]。
