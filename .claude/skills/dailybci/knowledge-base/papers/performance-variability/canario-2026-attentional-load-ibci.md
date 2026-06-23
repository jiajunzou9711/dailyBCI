---
title: "Intracortical BCI Performance is Robust to Changes in Attentional Load During Dual-Tasking"
authors: Canario, Shearer, Akcakaya, Weber, Chase, Collinger
year: 2026
venue: bioRxiv
url: https://doi.org/10.64898/2026.06.16.732398
subfield: performance-variability
tags: [performance-variability, intracortical, attention, dual-task, N-back, EEG, signal-quality, implant-age, human, Pittsburgh]
---

## 解决了什么问题
高性能皮层内 BCI(iBCI)正从实验室走向家庭/真实场景,而那里多任务、分心不可避免。但"注意/精神状态变化时 iBCI 还稳不稳"几乎没被系统验证——已有的注意效应研究绝大多数在头皮 EEG-BCI 上,极少有人正面测**植入式**控制对分心的鲁棒性。本文在人类 iBCI 里**主动操纵注意负荷**来回答这个问题。

## 核心方法
人体研究:**2 名四肢瘫患者**(P2: C5 ASIA B,植入约 8 年;P4: C4 ASIA A,植入约 6 个月),运动皮层植入 Blackrock NeuroPort **Utah 阵列**(P2 88 通道 / P4 96 通道,另各两片 32 通道于体感皮层)。让其完成一个**真实的 2D 光标 + 点击"搬运"任务**(reach→grab→carry→release,限时 20 秒),同时做**听觉 N-Back 工作记忆任务**(1-Back / 2-Back)以分级施加注意负荷。用同步 **16 通道头皮 EEG** 量注意相关物(额区 theta、顶区 alpha)与运动相关信号(运动区 beta),并从阵列取放电率、LFP beta、神经反应时。关键设计:测"注意"用额顶 theta/alpha,测"运动"用运动区 beta + 皮层内信号——不同脑区不同频段,彼此独立。

## 关键数据
- **负荷确被施加**:N-Back 下额区 theta、顶区 alpha 显著升高(theta P2 F=168.08 / P4 F=22.78,p<0.001);N-Back 准确率各条件均 >80%;自评心理负荷(1–10 分,Paas 1992)双任务显著更高(Fig S2,F=6.98,p=0.0005)。
- **性能基本不掉**:成功率、reach 用时**无显著差异**(成功率 P2 p=0.435 / P4 p=0.194);唯一显著的小幅下降在 **P2**(植入约 8 年、信号已衰减)——BCI+1-Back 比 BCI+2-Back 路径更长、总用时更长;**最差情况平均成功率跌 <10%**;P4(6 个月)无变化。
- **运动意图信号基本保住**:4 信号 × 2 人 = 8 项检验中 6 项无差异;仅 2 项显著(P2 的 LFP beta、P4 的放电率 23.10→23.16 Hz),幅度极小且方向是运动信号略**增强**而非减弱;神经反应时无差异。
- **跨研究对比**:头皮 EEG-BCI 高负荷下成功率常跌约 20%(Foldes & Taylor 2013;Vecchiato 2016 三任务 ηp²=.31),而本篇皮层内最差也只 <10%。

## 为什么是 milestone
它是**极少数正面测人类皮层内 BCI 控制中注意/分心影响的工作之一**(同类仅 Guthrie 2021、Stavisky 2020),且与前作不同——**主动操纵注意负荷(双任务 N-Back)** 并用**全脑 EEG** 量化注意相关物、在一个含点击拖拽的复杂任务上做。结论:iBCI 控制看起来比 EEG-BCI 更抗分心,而脆弱性跟着**信号质量/植入年限**走(衰减的 P2 vs 新鲜的 P4),而非分心本身。它把非侵入侧的注意-性能文献([[niu-2025-cognitive-state-eeg-bci-review]]、[[grosse-wentrup-2013-smr-bci-performance-variations]]、[[vidaurre-2010-bci-illiteracy]])与皮层内侧的信号变异文献([[perge-2013-intraday-signal-instabilities]]、[[downey-2018-intracortical-recording-stability]],后者同为匹兹堡 Chase/Collinger 组、被动观察过状态相关漂移)接到了一起:从"被动观察漂移"推进到"主动操纵状态看性能"。局限:n=2(皮层内试验固有)、效应小、单一实验室任务;更复杂/更高维应用未必同样鲁棒。
