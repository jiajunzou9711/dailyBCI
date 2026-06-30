---
title: "Brain-to-Text Decoding: A Non-invasive Approach via Typing (v1) / Accurate Decoding of Natural Sentences from Non-Invasive Brain Recordings (v2)"
authors: d'Ascoli, Lévy, King et al. (v1); Zhang, Lévy, King et al. (v2)
year: 2026
venue: Nature Neuroscience (v1) / Meta AI preprint (v2)
url: https://www.nature.com/articles/s41593-026-02303-2
subfield: non-invasive
tags: [MEG, typing, brain-to-text, CTC, language-model, asynchronous-decoding, scaling-law, Meta-FAIR]
---

## 解决了什么问题
非侵入解码语言产出长期落后于侵入式：信噪比低、且此前的高性能方案只能离线工作。Brain2Qwerty 这条线（Meta FAIR，资深作者 Jean-Rémi King）要回答：仅凭非侵入信号，能不能把"产出的语言"逐句解成文本，并逼近开颅植入的水平。

## 核心方法
范式：健康被试在 MEG 中把记住的句子打出来，解码"打字时的脑活动→打出的字"（信号主要来自运动皮层 + 语言/拼写规划）。打字让键盘自动提供"确切字符 + 确切时刻"的完美监督标签；想象说话无可观测标签，出声说话用肌电污染 MEG。
- **v1（同步，Nature Neuroscience）**：以每次按键时刻为中心切窗、逐窗分类字符（运行时依赖按键时刻，故只能离线）。
- **v2（异步，Meta AI preprint）**：从连续 MEG 直接转写，靠 **CTC** 去掉按键时刻依赖（每帧输出"字母或空白"、对所有能折叠成目标串的对齐求和，模型自学每字落在哪一帧）；三层架构（字/词/句）+ 微调 LLM 补语义；并用 AI coding agents 自动优化流水线。这是语音识别 CTC（Graves 2006）的同一去对齐思路。

## 关键数据
- v1：35 名健康人；MEG 字符错误率 (CER) 32%（最佳被试 19%），EEG 67%（颅骨模糊导致）。
- v2：9 名被试、每人 10 h、共 22,000 句（约 v1 的 10×）；词错误率 (WER) 39%（约 61% 词准确率），最佳被试半数句子只错 ≤1 词。
- v2：准确率随训练数据量呈**对数线性提升**（Pearson r = −0.99），未见平台。

## 为什么是 milestone
首个把非侵入语言解码从"离线、字符级"推到"在线/异步、词与句级、且开始够到侵入式水平"的工作。方法学关键贡献是用 CTC 去掉对按键时刻的依赖（同步→异步），把"模型自己在连续流里对齐"这件事跑通。纵向接 [[defossez-2023-meta-meg-speech-decoding]]（同组 MEG，解的是听到的语音）→ Brain2Qwerty（解产出的打字），把语言解码从感知端推到产出端；与 [[tang-2023-semantic-language-reconstruction]]（fMRI 只到要义、慢）形成对照。局限：MEG 是房间大小扫描仪（寄望可穿戴 OPM）；被试是健康人真打字（读的是运动信号），向不能动患者的 attempted/imagined 打字迁移未证；横向对照侵入式仍有差距（[[willett-2023-high-performance-speech]] 等）。
