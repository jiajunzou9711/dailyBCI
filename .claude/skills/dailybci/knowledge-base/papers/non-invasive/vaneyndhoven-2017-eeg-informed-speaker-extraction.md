---
title: "EEG-Informed Attended Speaker Extraction From Recorded Speech Mixtures With Application in Neuro-Steered Hearing Prostheses"
authors: Van Eyndhoven, Francart, Bertrand
year: 2017
venue: IEEE Transactions on Biomedical Engineering
url: https://doi.org/10.1109/TBME.2016.2587382
subfield: non-invasive
tags: [auditory-attention, EEG, speaker-extraction, neuro-steered-hearing, beamforming]
---

## 解决了什么问题
AAD 本身只回答"用户在听哪个说话者"，但助听器真正要做的是把那个说话者的声音**提取/增强**出来。此前两步（解码注意、分离声音）是脱节的。

## 核心方法
EEG-informed 框架：先用 AAD 判断被注意说话者，再用 multi-channel Wiener filter 等从录制的麦克风混合信号中提取该说话者语音，把"读注意"与"提目标声"耦合进一条流水线。

## 关键数据
- 在 neuro-steered hearing prosthesis 设定下，联合完成注意解码 + 被注意语音提取。
- 证明用 EEG 注意信息可驱动语音增强，而非仅做离线注意分类。

## 为什么是 milestone
把 AAD 从"判断注意对象"推进到"闭环增强目标说话者"，第一次勾勒出神经导向助听假体的完整工程流水线（解码→提取→增强）。承自 [[osullivan-2015-single-trial-eeg-aad]]，与后来无需干净源的 [[han-2019-speaker-independent-aad]] 形成对照。
