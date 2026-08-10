---
title: "A biodegradable piezoelectric vertebral implant for programmable electro-neuromodulation in spinal cord injury"
authors: Liu P, Wang X, Liu Y, et al.
year: 2026
venue: Science Advances
url: https://doi.org/10.1126/sciadv.aeg0515
subfield: neuromodulation
tags: [piezoelectric, self-powered, biodegradable, spinal-cord-injury, vertebral-replacement, ultrasound, rat]
---

## 解决了什么问题
硬膜外脊髓电刺激的疗效已被反复证明（[[harkema-2011-epidural-stimulation-standing]] → [[wagner-2018-targeted-epidural-walking]] → [[lorach-2023-brain-spine-interface-human]]），卡住的是器件形态：电极 + 导线 + 植入式脉冲发生器带来手术复杂度、感染风险、电池更换与系留。本文换掉的是**供电方式**，不是刺激机制。

## 核心方法
二苯丙氨酸（FF）肽在明胶冷冻凝胶骨架上原位自组装，形成可降解的压电凝胶（Piezo Gel）。**植入位置是被切除的 T9 椎体本身**（脊髓腹侧），既作结构替代物又作换能元件——脊柱承受的压力使其形变而产电，体外超声可进一步放大。配套提出**分期方案**：急性期瘫痪无机械输入时用超声隔空驱动；亚急性期改为负重跑台训练，由动物自身踩踏供电。物种为 Sprague-Dawley **大鼠**，重度（椎体置换致伤）与轻度挫伤两个模型。

## 关键数据
- 输出：循环压缩下约 50 mV / 0.92 µA；超声功率密度 0.1→1.0 W/cm² 时输出由 1.49 mV 线性升至 106.4 mV；清醒大鼠被推动作下峰峰值 74.62 ± 41.10 mV。
- 重度 SCI（n = 12，每组 3 只）：第 8 周 BBB **13.7**，为对照组 4.3 倍；MEP 幅度升 4.3 倍但**潜伏期延长**（作者解释为多突触绕行通路）；SEP 幅度升约 3.8 倍、潜伏期缩短近 50%；膀胱壁厚 1406.4 µm（4.2 倍）。
- 轻度 SCI（n = 12，每组 6 只）：分期方案 4 周 BBB **16.3**，为对照 2 倍；摆动相占比由 10% 升至 77%。
- 转录组：599 个差异表达基因（376 上调），上调富集于离子跨膜转运与离子通道；候选分子 **PKD2L1**（TRP 家族，脑脊液接触神经元标志物，机械敏感）。

## 为什么值得入库（非 milestone，作路线标记）
它是"自供能、无植入电子器件"这条器件路线的代表作，且**把供电与康复训练合并为同一动作**——刺激强度成为动物自身运动的函数，这一点与既有硬膜外刺激线（外部供能、参数由医生设定）性质不同。

**评估时必须带的四条边界：**
1. **大鼠，每组 3–6 只**；作者自陈仅适用于需行椎体切除的爆裂骨折患者。
2. 论文明确器件**不以诱发动作电位为目标**，走的是促再生/营养层，与 EES 的即时兴奋性调控不是同一层。
3. **方法部分自述输出为交流电（AC）**，而它援引的 galvanotropism 文献（[[mccaig-2005-controlling-cell-behavior-electrically]]）全部基于持续同向直流场——机制链条在此处有缺口。
4. 50–100 mV 是**器件两端电压**，非脊髓组织内场强；未给组织内场强实测值。体外用 **PC12** 测分化，而 PC12 神经突朝**阳极**生长，该模型不检验其援引的方向性机制。
