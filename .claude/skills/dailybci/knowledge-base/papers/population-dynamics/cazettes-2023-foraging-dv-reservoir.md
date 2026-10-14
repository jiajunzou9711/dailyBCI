---
title: "A reservoir of foraging decision variables in the mouse brain"
authors: Cazettes, Mazzucato, Murakami, Morais, Augusto, Renart, Mainen
year: 2023
venue: Nature Neuroscience 26:840–849
url: https://doi.org/10.1038/s41593-023-01305-8
subfield: population-dynamics
tags: [decision-variable, multiplexing, foraging, M2, Neuropixels, mouse, reservoir, linear-decoding]
---

## 解决了什么问题
同一串观测可以加工出多种决策变量（DV），领域通常假定大脑只计算当前行为策略所用的那一个；人类行为实验的串行瓶颈证据支持这一假定。本文检验：没被行为采用的 DV，皮层是否同样在算。

## 核心方法
头部固定小鼠做隐状态觅食任务（每舔 0.9 概率出水、0.3 概率切换出水侧，每回合只切一次），由「最后一次舔」定义离开决策。两种 DV：连续失败数（失败 +1、奖励清零，推断型）与负价值（失败 +1、奖励 −1，stimulus-bound）。Neuropixels 1.0 急性记录 M2 / OFC / OLF（10 只小鼠 11 session），VGAT-ChR2 双侧抑制 M2（6 只 43 session）。用残差与去相关子序列排除两 DV 的相关（r = 0.79），用 LM-HMM 排除 session 内策略切换。提出 INTEGRATE-AND-RESET 模型 x(t+1) = g·x(t) + c 统一生成一族 DV。

## 关键数据
- 行为：42 session 中 23 偏推断、19 偏 stimulus-bound（斜率 0.5 为界）
- M2 预测离开决策显著优于 OFC、OLF；离开与起跑解码轴近正交（~90°）
- 抑制 M2：DV 预测 deviance explained −0.04（P = 0.021），对照同向 P = 0.054
- 示例 session：行为几乎只用推断（0.164 vs 0.004），M2 仍拟合两 DV（0.74 / 0.41）
- **M2 对 DV 的读出强度与该 DV 对行为的预测力无关**：r² < 10⁻³，P = 0.9；去相关后 r² = 0.02，P = 0.6
- 残差两条均可从 M2 读出（P = 0.00098）；OFC 只读出连续失败数残差
- 功率谱匹配随机信号、余弦波读不出（Extended Data Fig. 8）→ 储备库有边界，不是通用 reservoir computing

## 为什么是 milestone
把「群体可线性读出多种变量」（mixed selectivity，见 Rigotti 2013）推进到**跨数秒的时间扩展计算**：未被采用的策略变量同样以可线性读出的形式存在于同一群神经元。对 BCI 的含义：从运动前区群体中可能读出动物并未使用的内部变量，「可读出」与「被使用」需分开论证。局限：线性可读出不等于下游读取；光遗传效应量小；仅 M2 与单一任务。
