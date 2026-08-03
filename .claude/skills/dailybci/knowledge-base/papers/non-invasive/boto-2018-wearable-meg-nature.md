---
title: "Moving magnetoencephalography towards real-world applications with a wearable system"
authors: Boto E, Holmes N, Leggett J, Roberts G, Shah V, Meyer SS, Muñoz LD, Mullinger KJ, Tierney TM, Bestmann S, Barnes GR, Bowtell R, Brookes MJ
year: 2018
venue: Nature 555:657-661
url: https://doi.org/10.1038/nature26147
subfield: non-invasive
tags: [OPM, wearable-MEG, 自由运动, 里程碑]
---

## 解决了什么问题

常规 MEG 要求被试头部在刚性扫描仪内保持静止(容许头动通常小于 2 mm)。这条限制既把很多人排除在外(婴幼儿、运动障碍患者)，也把很多实验问题排除在外(空间导航、自然交互、运动学习)。此前的 OPM 工作解决了"贴近头皮"([[boto-2017-room-temperature-opm-meg]])和"场置零"([[holmes-2018-biplanar-nulling-coils]])，但没有把两者合成一个真正可戴着动的系统。

## 核心方法

把不需要超导冷却的 OPM 装进可像头盔一样佩戴的支架，与双平面主动场置零线圈系统整合，使传感器随头一起移动、而头所在体积内的背景场被压到 OPM 动态范围之内。被试在扫描过程中做自然动作：点头、伸展、喝水、以及打乒乓球(用球拍颠球)。结果与同被试的常规 SQUID MEG 对照。

## 关键数据

- 允许头动幅度超过 **±10 cm**，对照常规系统的 **< 2 mm**。
- 静态残余场降低约 **50 倍**，主要场梯度降低约 **35 倍**。
- OPM 传感器噪声约 **15 fT/√Hz**，与 SQUID 可比。
- 原型使用 **13 个**头皮传感器；连接性演示使用 **26 个**传感器。
- 在被试做大幅头动的条件下，结果仍与当时最好的常规系统相当。

## 为什么是 milestone

**可穿戴 MEG 的奠基工作**，此后所有 OPM-MEG 应用研究(虚拟现实范式、学习乐器、互动游戏、终身适配头盔)都建立在它证明的这件事上：毫秒级非侵入电生理成像可以在被试自然活动时进行。

**同时要看清它没解决什么**——这套系统仍然在**被动磁屏蔽室内部**运行，场置零只覆盖头部上方一个**固定体积**，允许自由转头但不允许在房间里走动。综述([[brookes-2022-opm-meg-review]])在 2022 年仍把"大幅运动(如行走)尚未被演示"和"脱离屏蔽室"列为公开问题。评估任何后续"开放环境 OPM-MEG"工作时，这两条是必须先对照的边界。走另一条技术路线、直接在无屏蔽地磁场下记录的尝试见 [[zhang-2020-unshielded-earth-field-meg]]。
