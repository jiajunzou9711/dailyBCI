---
title: "Decoding motor plans using a closed-loop ultrasonic brain–machine interface"
authors: Griggs, Norman, Deffieux, Segura, Osmanski, Chau, Christopoulos, Liu, Tanter, Shapiro, Andersen
year: 2024
venue: Nature Neuroscience 27:196–207
url: https://doi.org/10.1038/s41593-023-01500-7
subfield: functional-ultrasound
tags: [fUS, closed-loop, BMI, posterior-parietal-cortex, macaque, epidural, cross-session-stability]
---

## 解决了什么问题
[[norman-2021-single-trial-decoding-fus]] 证明 fUS 能离线单试次解码运动意图,但 BCI 的定义性检验是**闭环**:被试实时看到解码输出并据此调整,解码器与大脑互相适应。此外,BCI 的实用性取决于跨天稳定性——每天重新校准是皮层内 BCI 的长期痛点。fUS 在这两点上都未经检验。

## 核心方法
在 2 只**恒河猴**执行眼动与手动任务时,从**后顶叶皮层(PPC)**流式采集 fUS 数据,驱动**闭环**超声 BMI。作者另外提出用**既往会话数据预训练**解码器的方法,使后续日期可以立即开始控制,而不需大规模重新校准。记录同样在硬膜外层面,论文将这条路线定位为"less-invasive (epidural)"接口。

## 关键数据
- 2 只恒河猴;训练后可用 BMI 控制**至多 8 个运动方向**。
- 预训练方法让**跨天(包括相隔数月的日期)立即可控**,无需大量重新校准。
- 论文自述确立"超声 BMI 的可行性",指向一类跨长时间尺度泛化的低侵入接口。

## 为什么是 milestone
fUS 在此完成从"成像 + 离线解码"到"实时闭环 BCI"的跃迁,并顺带回答了稳定性问题:血流动力学信号来自血管解剖结构,而血管位置比单个神经元的可记录性更稳定,这可能正是跨月免校准的物理来源(与皮层内阵列的单元漂移形成对照,见 [[perge-2013-intraday-signal-instabilities]]、[[downey-2018-intracortical-recording-stability]])。至此 fUS-BMI 的猕猴侧证据链完整;剩下的缺口在人体——人的成人颅骨挡住超声,须先解决声窗([[rabut-2024-human-acoustic-cranial-window]])。
