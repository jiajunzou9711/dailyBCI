---
title: "A new generation of magnetoencephalography: room temperature measurements using optically-pumped magnetometers"
authors: Boto E, Meyer SS, Shah V, Alem O, Knappe S, Kruger P, Fromhold TM, Lim M, Glover PM, Morris PG, Bowtell R, Barnes GR, Brookes MJ
year: 2017
venue: NeuroImage 149:404-414
url: https://doi.org/10.1016/j.neuroimage.2017.01.034
subfield: non-invasive
tags: [OPM, room-temperature, scanner-cast, MEG]
---

## 解决了什么问题

[[iivanainen-2017-on-scalp-arrays]] 在仿真里算出贴头皮 OPM 阵列的收益，但仿真不等于实测。缺的是在真人身上把"室温 OPM 贴头皮"与"同一被试的常规 SQUID MEG"直接对照，看理论增益能不能兑现。

## 核心方法

用室温工作的 OPM，配合按被试头部解剖定制的 3D 打印**头模(scanner-cast)** 把传感器精确定位并贴近头皮，在磁屏蔽室内记录人类诱发反应与自发节律，并与同一被试的常规 SQUID MEG 结果对照。定制头模同时解决两件事：把传感器压到尽可能贴头皮，以及让传感器位置相对脑解剖已知(源定位的前提)。

## 关键数据

该工作在真人上验证了贴近头皮带来的信号幅值增益，并证明室温 OPM 记录的诱发反应与常规 MEG 结果一致。（本条目未核实原文报告的具体增益倍数与通道数，引用时勿编造数值；仿真侧的定量预期见 [[iivanainen-2017-on-scalp-arrays]]。）

## 为什么是 milestone

OPM-MEG 从仿真走向**人体实测**的转折点，也确立了"定制 scanner-cast"这个此后被反复使用的工程做法。但要注意它的传感器仍是固定在刚性头模里、被试仍需相对静止——**"可穿戴、可自由活动"要到下一步**([[boto-2018-wearable-meg-nature]])才成立。评价 OPM 系统时区分这两个阶段很重要：贴近头皮(信号增益)和允许运动(生态效度)是两件被分开解决的事。
