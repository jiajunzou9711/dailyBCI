---
title: "Functional ultrasound imaging of human brain activity through an acoustically transparent cranial window"
authors: Rabut, Norman, Griggs, Russin, Jann, Christopoulos, Liu, Andersen, Shapiro
year: 2024
venue: Science Translational Medicine 16:eadj3143
url: https://doi.org/10.1126/scitranslmed.adj3143
subfield: functional-ultrasound
tags: [fUSI, human-adult, cranial-window, PMMA, skull-replacement, decoding, awake]
---

## 解决了什么问题
成人颅骨对超声强烈衰减,fUSI 做不进去。人体 fUS 此前只在新生儿囟门([[demene-2017-fus-human-newborns]])或术中开颅([[imbault-2017-intraoperative-human-fus]])完成,前者仅限婴儿,后者只能在手术室里、颅骨敞开的短暂窗口内做,都无法支撑慢性、清醒、可重复的人体功能记录,更谈不上 BCI。

## 核心方法
用**聚合物颅骨置换材料**造出与 fUSI 兼容的**声窗**。先做体外脑血管体模与大鼠颅骨缺损模型,评估不同厚度**聚甲基丙烯酸甲酯(PMMA)**植入物与钛网植入物下的 fUSI 信号强度与信噪比;定制专用 fUSI 脉冲序列后,证明可隔着 PMMA 记录大鼠脑活动。随后为 1 名因创伤性脑损伤接受颅骨重建手术的成人患者设计定制的超声透明颅骨窗植入物,在其清醒状态下、**手术室之外**做经皮 fUSI。注意归类:这是**植入了颅骨置换物**的经皮记录,不穿刺脑组织、不开颅记录,属于介于侵入与非侵入之间的一格。

## 关键数据
- 体外体模 + 大鼠颅骨缺损模型:对比不同厚度 PMMA 与钛网,PMMA 下可高灵敏记录大鼠脑活动。
- **人类成人 1 名**(创伤性脑损伤后颅骨重建),清醒、非手术室环境下完成 fUSI 记录。
- 在"连点(connect the dots)"电子游戏任务中,实现任务调制活动的**映射与解码**。
- 论文给出的功能成像分辨率约 **200 µm**。

## 为什么是 milestone
它把 fUS 的人体应用从"手术室里的一次性机会"变成"可长期存在的声窗",从而让清醒人体的重复会话记录与解码成为可能。与 [[griggs-2024-closed-loop-ultrasonic-bmi]] 合起来,fUS-BCI 的两块拼图各就位:猕猴证明闭环与跨月稳定,人体证明有窗可用、可解码。作为**单一被试的原理验证**,它未回答分辨率能否支撑精细效应器(如单个手指)、也未回答跨会话解码在人体上是否成立——这正是 2026 年 Andersen 组后续工作要接的那一格。
