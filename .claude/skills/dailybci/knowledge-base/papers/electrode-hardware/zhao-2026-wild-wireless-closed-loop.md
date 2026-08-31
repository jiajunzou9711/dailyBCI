---
title: "A wireless modular platform for neuro-behavioral recording and closed-loop manipulation in small animals"
authors: Zhao, Chang, Paudel, Park, Liu, Aurelio, Oliva, Fernandez-Ruiz
year: 2026
venue: bioRxiv
url: https://doi.org/10.64898/2026.08.25.747153
subfield: electrode-hardware
tags: [wireless, closed-loop, TinyML, optogenetics, datalogger, mouse, hippocampus, SWR, open-source]
---

## 解决了什么问题

闭环神经干预（检出某个神经事件后当场刺激它，以建立因果）此前只在**有线记录 + 体外计算机**的条件下做得成，而值得做闭环的行为——群体社交、大空间觅食、户外活动——多是有线做不了的。论文实测：与未植入小鼠相比，有线组的移动距离与社交互动时间显著更低（FDR 校正 p = 0.007 / 0.0342），无线组无显著差异（p = 0.109 / 0.62；每组各来自 2 只小鼠）。作者对"为什么一直没结合起来"只给一句归因：在嵌入式系统里做实时信号处理与刺激递送本身很难（未展开）。

## 核心方法

自研头戴 datalogger（WILD）把整个闭环回路收进动物头上：64 通道放大器 + microSD + 蓝牙（仅做同步与监控，**不在回路里**）+ 9 轴 IMU + 320×320 微型摄像头 + 超声麦克风 + 光遗传刺激模块；电极为柔性 parylene-C 探针（直接键合到板）或硅探针，植入海马 CA1、外侧隔核、前额叶皮层。板上跑两级：① 低延迟 DSP（低通 500 Hz → 降采样 1250 Hz → 一阶带通 → 功率包络/Hilbert 相位 → 阈值），约 5 µs；② 被 DSP 检出**触发**的 TinyML（CNN 降采样 + GRU）做去噪，只看事件前 0.5 s 窗口。另有一路持续运行的 IMU 行为分类器（更深 GRU，1 s 片段）。模型在 PC 预训练、训练后量化后编译进固件，板上只推理。

## 关键数据

- 器件 < 1.5 g（板 23.3 × 15.7 mm），含壳带电池约 4.5 g；小鼠上限约 5 g；刺激模块 0.6 g
- DSP 检测延迟约 5 µs（作者归因于去掉了数据通信）；TinyML 推理 < 10 ms、准确率 > 90%；触发刺激亚毫秒
- **SWR 在线检测 AUROC 0.717 →（加片上去噪）0.844**，Δ 0.127（95% CI 0.092–0.162，配对 bootstrap，p = 5.96e-12，n = 2,378 次 SWR），接近离线事后水平
- 闭环打断 SWR：相关放电被压到基线以下（7 个 CA1 单位）
- 续航：130 mAh 电池 64 通道 @20 kHz 约 3 h（大鼠 ~5 g 电池约 9 h）；空闲模式约 1 mW、约 300 h
- 蓝牙通信 70 m，多机同步约 1 ms
- 户外围场 38 × 15 m、9 只小鼠、15 天：夜间移动 9.56 ± 0.91 m/h vs 白天 6.20 ± 0.71（p = 1.1e-6）；夜间 NREM 更少但 SWR 发生率更高（p = 0.0066）；识别位置细胞 1,636 个

## 为什么是 milestone

在无线这条线上补的是与 [[borton-2013-wireless-broadband]]、[[simeral-2021-braingate-wireless]] 不同的一格：那两篇解决的是把数据**搬走**，这篇解决的是**在设备上判断**——首次把 TinyML 推理与光遗传刺激一起装进小动物可驮的重量，使闭环干预脱离有线与外部计算机。它也把"闭环的复杂度上限"暴露成三笔互相牵制的预算（时间由生理定、算力由处理器定、重量由动物定）。**边界**：小鼠/大鼠，非人体；闭环刺激只演示光遗传（需转基因表达 ChR2），文中未演示电刺激；高带宽连续记录仅 3–9 h。全部硬件与软件开源。
