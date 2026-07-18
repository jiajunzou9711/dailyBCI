---
title: "Timing, timing, timing: fast decoding of object information from intracranial field potentials in human visual cortex"
authors: Liu H, Agam Y, Madsen JR, Kreiman G
year: 2009
venue: Neuron
url: https://doi.org/10.1016/j.neuron.2009.02.025
subfield: semantic-decoding
tags: [iEEG, intracranial-field-potential, category-decoding, single-trial, visual-cortex, temporal-lobe, human]
---

## 解决了什么问题

fMRI 能证明范畴信息存在于腹侧颞叶，但它的时间分辨率（秒级）完全看不到这个信息**什么时候**出现。而"何时"恰恰是分辨视觉识别理论的关键：纯前馈（feedforward）理论预测范畴信息在刺激后约 100–150 ms 就该到位，需要循环反馈（recurrent feedback）的理论则预测更晚。本文用人类颅内记录在毫秒尺度上回答这个问题。

## 核心方法

**电极模态：侵入式颅内电极（intracranial field potentials）** ——癫痫患者临床植入的颅内电极，记录场电位（覆盖视觉皮层/颞叶，非皮层内单神经元记录）。在毫秒分辨率上量化每个电极、每个时间点携带多少视觉信息，并做**单试次**范畴解码。同时检验解码对物体变换（深度旋转、尺度变化）的鲁棒性。

## 关键数据

- *Neuron* 62:281–290（2009 年 4 月 30 日），DOI 10.1016/j.neuron.2009.02.025，PMID 19409272
- 规模：**11 名人类被试、912 个电极**
- 时间：单试次即可解出物体范畴信息，**最早在刺激后 100 ms**
- 鲁棒性：解码性能对深度旋转与尺度变化稳健（robust to depth rotation and scale changes）
- 结论方向：如此快的单试次解码与前馈理论相容，并给人类视觉的计算模型提供强约束

## 为什么是 milestone

这是**颅内电位单试次解出范畴信息**的奠基实证，也是这条线上第一次把"范畴可解码"从 fMRI 的空间证据升级为电生理的时间证据。对语义 BCI 的意义在两点：第一，它证明颅内场电位里的范畴信息是**单试次可提取**的（不必跨试次平均），这是任何实时 BCI 的前提；第二，100 ms 的时间尺度说明这条信息通路快到足以支撑交互式通信——与 fMRI 血流类信号（[[lin-2026-human-cranial-window-effector-mapping]] 那种 0.6 Hz、需 block 设计）形成鲜明的模态取舍。

需要注意归位：本文解的是**视觉物体范畴**（看到了什么类别的东西），偏知觉侧；[[patterson-2007-semantic-knowledge-representation]] 意义上的模态无关概念表征是更强的要求，由 [[rupp-2017-ecog-semantic-attributes]] 和 [[nagata-2022-abstract-concrete-semantics]] 往那个方向推。
