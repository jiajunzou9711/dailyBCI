---
title: "Effects of transcranial focused ultrasound stimulation to human lateral geniculate nucleus on visual perception and steady-state visual evoked potentials"
authors: Scott MTW, Limon PN, Mohammadjavadi M, Kop BR, Chen NF, Feredoes EA, Vildavski V, Popelka GR, Norcia AM, Butts Pauly K, Ash RT
year: 2026
venue: bioRxiv 2026.07.30.741804
url: https://doi.org/10.64898/2026.07.30.741804
subfield: neuromodulation
tags: [TUS, human, LGN, PRF, SSVEP, null-result, auditory-confound, frequency-tagging, study-design]
---

## 解决了什么问题

TUS 这条线十五年来悬着一个问题：效应方向不可预测（自 [[yoo-2011-region-specific-modulation-fmri]] 起就知道是双向的），没有参数能可靠地预测兴奋还是抑制。**脉冲重复频率（PRF）是目前最有物理机制支撑的候选**——占空比固定时 PRF 决定单个脉冲的时长，而长短脉冲会引出不同比例的**声辐射力**与**分子位移**两个机械成分；[[nandi-2024-parameters-effects-review]]（未入库，Brain Stimul 17:1216–1228）汇总的初步证据提示长脉冲偏兴奋、短脉冲偏抑制。本文在人身上把 PRF 拉开 100 倍来检验它。

## 核心方法

**人类，n=25 健康被试。** 靶点为左侧外侧膝状体核（LGN）——选它是因为它小（直径 <0.5 cm，与焦斑同量级）、深（>6 cm，临床相关深度）、把视网膜信息中继到 V1（效应可在枕叶用 EEG 读出）、且**解剖上侧化**（右半视野→左 LGN），因而天然自带被试内对照。

设备：NeuroFUS Pro CTX-500，500 kHz、4 阵元环形、深度可调 30–70 mm，实测焦斑 0.5 × 0.5 × 2 cm（FWHM）。自由场 ISPPA **68 W/cm²**（1.4 MPa）；BabelBrain 仿真估计的**脑内原位 ISPPA 16.2 ± 3.6 W/cm²**（范围 8.5–20.5），峰值负压 0.69 ± 0.33 MPa。占空比 **10%**，12 秒声照串与视觉刺激同步。**PRF 逐试次随机取 4.875 / 48.75 / 487.5 Hz**（对应脉冲时长约 20.5 / 2.05 / 0.205 ms）。脉冲首尾各 5% 线性斜坡以降低可听度。

**作者自列的四项设计创新（这篇最值得学的部分）：**
1. **频率不重叠**——频率标记的视觉刺激（左半视野全周期 3 Hz、右半视野 3.75 Hz，神经反应在 2F 即 6.0 / 7.5 Hz），其频率及谐波刻意避开三档 PRF 及其谐波，使 TUS 诱发的听觉/体感反应与电学伪迹**在频谱上就落不进读数**；
2. **同侧未受声半视野作内部对照**，用于检出非特异效应；
3. **对照条件改焦点深度而非关机**——70 mm（LGN）vs 30 mm（浅层听皮层与皮层下白质），配平了外周伴随刺激却避开主要视觉通路；
4. **高效白噪声掩蔽**使多数被试听不见 TUS，实现被试与实验者双盲。

## 关键数据

- **三个读数均未检出效应**：SSVEP 幅度、SSVEP 潜伏期、对比增量检测行为。
- **靶向精度与活动变化之间无相关**。
- 声学仿真（基于 Brainsight 实测换能器位置）显示 **FWHM 声束体与 LGN 重合，除两名被试外**；作者诚实指出 70 mm 转向深度**略偏浅**，焦点峰值相对 LGN 稍浅。
- 检出力：**N=25、α=.05、80% 功效下可检出的被试内交互效应量为 f ≥ 0.264**（假定重复测量相关 r=.591）。
- 未受声半视野在 PRF 487.5 Hz 下出现过一点反应变慢的趋势，作者按事先判据（真实效应应更明显地出现在受声的对侧半视野）判定其不支持真实效应。

## 为什么是 milestone

**这条线上第一份"三关全过"的人体阴性结果。** 用本知识库为 TUS 线定的三关衡量：① 听觉对照——掩蔽 + 包络斜坡 + 频率不重叠，三重；② 剂量与靶点——报告自由场与**脑内原位**估计，并用仿真核实焦斑落点（符合 [[martin-2024-itrusst-reporting-standards]]）；③ 读数与样本——三个独立读数 + 被试内侧化对照 + 明确的检出力下限。**因此它很难被"漏了某个对照"解释掉**，质疑只能落到检出力、剂量或焦点略偏浅上。

**必须与三项同靶点工作并读，缺一不可：**
- [[fry-1958-reversible-cns-changes-ultrasound]]（猫，**去掉颅骨**，同一核团可逆抑制）——说明隔着完整人颅骨是另一个问题；
- [[mohammadjavadi-2022-sheep-lgn-vep]]（**同实验室**，绵羊，同族读数，测到可逆抑制且与 MR-ARFI 位移相关）——纵向前作；
- [[martin-2025-256-element-human-lgn]]（人，同靶点，256 阵元相控阵 + 实时 fMRI，报告显著且可重复的效应）——横向对照。

**"为什么一个有一个没有"要落到可指认的差别上**：换能器（4 阵元 vs 256 阵元相控阵）、读数（SSVEP+心理物理 vs fMRI BOLD）、靶点验证（事后声学仿真 vs 实时 fMRI）、以及声学参数。不要笼统说"结果不一致"。

方法学价值超出超声本身：**三层对照的递进结构（频率标记 → 解剖侧化的被试内对照 → 改深度而非关机）是可迁移的实验设计范式**，每一层专门堵住上一层堵不住的一类替代解释。2026-08-05 日报即以此为主线。
