---
title: "Functional ultrasound imaging through a human cranial window for mesoscopic mapping of motor effector encoding within the sensorimotor cortex"
authors: Lin, Callier, Heiles, Pejsa, Liu, Shapiro, Andersen
year: 2026
venue: bioRxiv 2026.07.03.735688
url: https://doi.org/10.64898/2026.07.03.735688
subfield: functional-ultrasound
tags: [fUSI, human, cranial-window, single-digit, somatotopy, single-trial-decoding, cross-session, sensorimotor-cortex]
---

## 解决了什么问题
[[rabut-2024-human-acoustic-cranial-window]] 已在装有声学透明颅骨置换物的成人被试上证明人体 fUSI 可做任务状态检测与粗粒度解码,但只到"开/关任务映射"这一级。fUSI 在人体上能否分辨精细的运动效应器(单个手指级别)、能否单试次解码、跨会话是否稳定,均未验证。这几点是它作为微创 BCI 记录模态可用性的关键缺口。

## 核心方法
在**同一名**装有 Longeviti ClearFit PMMA 声学透明颅骨植入物的成人被试(TBI 后颅骨重建,记作 J,与 Rabut 2024 同一人)上,用线性阵列超声换能器(中心频率 7.5 MHz)经皮、隔颅骨板对感觉运动皮层做 fUSI,成像率 0.6 Hz,体素 300 × 300 µm,视野 38.4 × 49.3 mm,同时覆盖 M1、S1 与缘上回(SMG)。被试做 block 设计的提示性运动任务:多身体部位(对侧腕/指、唇、舌)与单个手指(拇/食/中/环/小)。用 GLM 生成显著体素图,PCA + LDA 解码器做单试次解码,并跨不同天的会话做迁移解码;另用 Crossnobis 距离比较各 Brodmann 区的表征差异。信号层级是神经血管耦合下的脑血容量(CBV)变化,不穿刺脑组织。

## 关键数据
- 单被试(n=1);体素 300 µm,视野 3.84 × 4.93 cm。
- 多身体部位:S1 内质心从腕→指→唇→舌呈背内侧到腹外侧分布,相邻质心间距 2.39–9.67 mm,符合经典躯体拓扑;单试次解码峰值 **>90–95%**(4 类,机会水平 25%)。
- 单个手指:五指质心从小指到拇指沿背内侧→腹外侧排开,相邻间距 1.49–5.82 mm;单试次解码峰值 **约 78%**(5 类,机会水平 20%),错误集中在相邻手指;Dice-Sørensen 指数显示相邻指(尤其中/环指)表征交错重叠。
- 分区解码:S1 最高(多身体部位 97%,单指 64%),M1 次之(76%/56%),SMG 仅在多身体部位任务显著(87%)。
- 反预期:单指解码只有 **BA 1** 显著(峰值 48%),按教科书预期最强的 BA 3b 几乎解不出(手指两两 Crossnobis 距离 BA 1 峰值 0.63,BA 3b 仅 0.04);作者归因于成像平面位置,称需进一步研究。
- 跨会话:GLM 映射跨天可复现,迁移解码在多数会话对上显著高于机会水平(多身体部位对 plane 位移较鲁棒,单指更敏感)。
- 作者引既往 fMRI 单指解码峰值约 63% 作对照(此数字为论文转述,未在本库独立核实原始文献)。

## 为什么是 milestone
把人体 fUSI 从 [[rabut-2024-human-acoustic-cranial-window]] 的"任务状态检测/粗粒度解码"推进到"同一只手五根手指的躯体拓扑分辨 + 单试次 + 跨会话解码",是这条模态线在人体上第一次拿到单指粒度。它与猕猴侧的 [[norman-2021-single-trial-decoding-fus]](单试次)、[[griggs-2024-closed-loop-ultrasonic-bmi]](闭环、跨月免校准)共同勾出 fUSI-BCI 的证据链。定位仍是单被试原理验证,且受 PMMA 信噪比限制必须用 block 设计、时间分辨率受神经血管耦合(0.6 Hz)约束——这正是"血流类模态换空间、不换时间"的具体例证(Andersen/Shapiro 组,Caltech,通讯 R.A. Andersen)。
