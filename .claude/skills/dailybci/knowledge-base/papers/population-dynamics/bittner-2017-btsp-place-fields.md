---
title: "Behavioral time scale synaptic plasticity underlies CA1 place fields"
authors: Bittner, Milstein, Grienberger, Romani, Magee
year: 2017
venue: Science 357:1033–1036
url: https://doi.org/10.1126/science.aan3846
subfield: population-dynamics
tags: [hippocampus, CA1, place-field-formation, BTSP, plateau-potential, dendritic-calcium, synaptic-plasticity, non-Hebbian, mouse, whole-cell]
---

## 解决了什么问题
Hebb 规则依赖前后神经元在数十毫秒内的因果共激活且需要多次重复，难以解释位置野为何能在一两次经过后形成、并跨越秒级行为时间关联输入。本文直接测定 CA1 位置野形成所依赖的可塑性规则的时间窗。

## 核心方法
头固定小鼠在直线跑步机轨道上跑圈，对 CA1 锥体细胞做在体胞内（全细胞）记录。所选细胞在记录开始至少 5 min 内无位置选择性放电（沉默细胞）。之后出现自然（n=7）或人为诱发（n=20）的树突 Ca²⁺ 平台电位（plateau potential），测量其后形成的膜电位斜坡（Vm ramp）。用运动轨迹反卷积估计可塑性核；建立生物物理模型（突触局部慢信号 × 平台电位全局信号）。离体脑片中以 5 次"阈下突触刺激 + 体细胞注流平台电位"配对、改变两者间隔，测定时间窗与药理敏感性。

## 关键数据
- 诱导期含平台电位的圈数：自然 1.4±0.22，诱发 5.1±0.32；位置野可在单次诱导后出现。
- Vm ramp 起点平均在平台电位前 3.8±0.2 s（n=27），该段位置在诱导圈中几乎无动作电位（0.1±0.05 Hz）。
- ramp 宽度随诱导圈跑速增加，斜率约 2.5 s（r²=0.76）；诱导后各圈 ramp 宽度与跑速无关（125.4 vs 126.5 cm，P=0.62）。
- 反卷积得到的可塑性核不对称：上升约 3 s、衰减约 2 s，比标准 STDP 时间窗长约两个数量级。
- 脑片（n=58 个细胞）：同时配对增强约 3 倍（3.12±0.11）；突触前在前方向 τ=1.31±0.22 s，突触后在前方向 τ=0.69±0.11 s；通路特异。
- D-APV（NMDAR 阻断）使增强降低 84%，nimodipine（L 型 Ca²⁺ 通道阻断）降低 73%；在体局部给 nimodipine 使 ramp 幅度从 6.2±1.3 mV 降到 1.3±0.4 mV。

## 为什么是 milestone
命名并定量了 BTSP：由树突平台电位触发、时间窗为秒级、单次即可形成位置野、且增强的输入无需与突触后放电因果相关，因而不符合 Hebb 公设。它给"新位置野在几圈内出现"提供了细胞层面的机制候选，是与 preplay（预先配置）解释并列的另一条主线；Ren 2026 中"经验依赖细胞逐圈并入"一类现象的机制讨论以此为基准。理论侧由 Magee & Grienberger 2020（Annu Rev Neurosci 43:95–117，同一实验室）收入可塑性形式综述。引用时注意：物种是**小鼠**、头固定；在体细胞数 n=27，动物数在正文未给出。
