---
title: "Realignment of representational drift in mouse visual cortex via flexible electrode arrays"
authors: Shen, Zhao, Marin-Llobet, Qin, Jiang, Tang, Lee, Zhang, Lee, Chen, Liu
year: 2026
venue: Nature Biomedical Engineering
url: https://doi.org/10.1038/s41551-026-01780-x
subfield: population-dynamics
tags: [representational-drift, flexible-electrode, same-neuron-tracking, GPFA, Procrustes-alignment, mouse-V1, decoder-stability]
---

## 解决了什么问题
解码器跨天变差有两个来源：记录不稳定（电极移位、记到的神经元换了）和表征漂移（同一批神经元对同一刺激的响应在变）。刚性电极难以确认跨月记的是同一个神经元，两者分不开；表征漂移此前主要靠光学成像（如 [[ziv-2013-hippocampal-place-code-drift]]）在细胞层面测到。本文用电生理记录在同一批神经元上把两者分开，并检验漂移能否被校正。预印本 bioRxiv 2024-05（10.1101/2024.05.23.595627），正刊 2026-10-06。

## 核心方法
- **电极与物种**：小鼠，侵入式皮层内柔性网状电极（SU-8 封装、Au 互连、Pt 电极，间距 30–66 µm；30/80 通道三种构型），植入 V1、V2、海马 CA1；记录单神经元动作电位。
- **同一神经元判据**：多 session 拼接后 MountainSort4 一次 sorting；ISI<1.5 ms 违例 >10% 剔除；跨 session 对平均波形 Pearson 相关 <0.9 的对 >10% 剔除；估计质心（Σaᵢ²xᵢ/Σaᵢ²）相邻 session 位移 >10 µm 剔除。
- **范式**：头固定小鼠反复看同一段 30 s 灰度电影（20 遍/次）；频繁组间隔 <8 天（4 只）vs 稀疏组 >15 天（5 只），用于区分"时间"与"观看次数"。
- **对齐**：每 session 单独拟合 GPFA（中心化去平移）→ 载荷矩阵正交 Procrustes 对齐流形（沿用 [[degenhart-2020-bci-stabilization-alignment]] 的做法，不用刺激信息）→ 潜在轨迹逐时间 bin 再做一次正交 Procrustes（**需刺激时间对齐**）+ 小偏移。
- **解码**：30 s 分 8 窗，LSTM（另用 SVM 复核）前一半 session 训练、后一半测试；比较单神经元 / 未对齐潜在 / 对齐后潜在三种输入。

## 关键数据
- 214 个 V1 稳定神经元，9 只小鼠，跨 5 个月；同神经元跨月质心位移 ≤约 10 µm，不同神经元间距主体 >20 µm（Fig 2k，读图）。
- 同日前后两半试次响应相关 0.85，隔 30 天 0.59，隔 109 天 0.01（一只频繁组小鼠，Fig 3d）。
- 按月数频繁组漂得更快（PV 相关 R：−0.65 vs −0.44）；按观看次数两组下降接近（PV −0.48 vs −0.50）→ V1 漂移主要随经历次数累积（PV、ER 成立，TC 不完全）。
- 潜在动力学：稀疏组 Pearson 相关跨月 ≥0.84 而余弦相似度快速下降 → 轨迹平移；对齐后频繁组余弦相似度隔 4 个月约 0.1 → 约 0.7（回归线），Pearson 仍缓慢下降。
- 跨月解码（频繁组，n=21 session）：单神经元、未对齐均约 0.55，对齐后约 0.80（机会 12.5%）；稀疏组三者无显著差异。
- 模拟电极不稳定 0–30%，比例越高对齐后相关越低。

## 为什么是 milestone
它在电生理层面、同一批神经元上跨月区分了"记录不稳定"与"表征漂移"，并给出漂移的一个可操作描述：群体轨迹变化的大部分是平移加旋转。与 [[gallego-2020-long-term-stability-dynamics]]（单神经元在换、低维动力学稳定）结论方向一致但前提不同：这里神经元没换，潜在动力学本身也在变。**局限**：第二步对齐用到刺激时间信息（测试 session 同样处理，论文未讨论对解码准确率的影响）；单一 30 s 电影；被动观看；Fig 7 跨动物解码与扩散模型帧重建证据初步（跨动物对齐模型以时间窗标签训练、是否含测试小鼠未写明；测试帧训练时都见过）。
