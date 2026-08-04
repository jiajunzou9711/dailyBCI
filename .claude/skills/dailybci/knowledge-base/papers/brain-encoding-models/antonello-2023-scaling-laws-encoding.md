---
title: "Scaling laws for language encoding models in fMRI"
authors: Antonello, Vaidya, Huth
year: 2023
venue: NeurIPS 2023 (arXiv:2305.11863)
url: https://arxiv.org/abs/2305.11863
subfield: brain-encoding-models
tags: [encoding-model, scaling-law, fMRI, language-model, speech-model]
---

## 解决了什么问题
此前脑编码研究几乎都用 GPT-2 量级的模型，没人知道模型规模继续放大后脑预测能力会怎样：是很快饱和，还是像其他领域的缩放规律一样持续提升。这直接决定了"堆模型"是不是提升编码性能的有效路径。

## 核心方法
在同一套自然语音收听 fMRI 数据上，系统扫过 OPT 与 LLaMA 系列从 **125M 到 30B 参数**的模型，各自取表征做岭回归编码模型，测留出集相关。同时对**训练数据量**做同样的扫描，并把该分析扩展到声学模型（HuBERT、WavLM、Whisper）。

## 关键数据
- 人类 fMRI，**3 名**被试，自然语音（Moth Radio Hour 类叙事）。
- 脑预测性能随模型规模呈**对数线性**提升，125M→30B 区间内编码性能（留出集相关）提升约 **15%**。
- 把 fMRI **训练集规模**放大也观察到类似的对数线性行为。
- 声学编码模型随模型规模的提升幅度与语言侧相当。

## 为什么是 milestone
把"更大的模型是否更像大脑"从直觉变成一条可外推的定量规律，并同时指出**数据量**与模型规模是两条并行的提升轴。它是判断任何新编码模型工作的基线：如果一项工作的增益能被"换更大的骨干"解释掉，那它就不构成方法学增量。与 [[jiang-2024-labram]] 之后 EEG 侧 "larger≠better" 的发现形成对照——不同模态的缩放行为不能互相假定。
