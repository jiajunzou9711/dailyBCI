---
title: "Magnetoencephalography with optically pumped magnetometers (OPM-MEG): the next generation of functional neuroimaging"
authors: Brookes MJ, Leggett J, Rea M, Hill RM, Holmes N, Boto E, Bowtell R
year: 2022
venue: Trends in Neurosciences 45:621-634 (Open Access)
url: https://doi.org/10.1016/j.tins.2022.05.008
subfield: non-invasive
tags: [OPM-MEG, wearable-MEG, magnetic-shielding, review, milestone-source]
---

## 解决了什么问题

常规 MEG(脑磁图)用超导量子干涉器件(SQUID)测神经电流产生的磁场，SQUID 必须浸在约 4 K 的液氦里，因而传感器与头皮之间要留真空隔热层、阵列必须刚性固定。由此派生出常规 MEG 的一整套限制：被试全程不能动、传感器最近只能到头皮约 2 cm、头盔按约 95% 成人尺寸"一码通吃"导致覆盖不均(儿童尤甚)、系统昂贵且依赖液氦供应。这篇综述系统梳理用**光泵磁力计(optically pumped magnetometer, OPM)** 替换 SQUID 之后，这些限制分别被解到什么程度、还剩哪些没解。

## 核心方法

综述性质，分三层组织：① **传感器物理**——OPM 用碱金属原子蒸气(通常 ⁸⁷Rb)、激光把原子泵浦到特定量子态，外磁场改变透过蒸气的光强，由光电二极管读出；靠加热进入**自旋交换弛豫自由(SERF)** 区来避免原子碰撞破坏相干性，靠加调制场解决 Lorentz 响应关于零场对称、无法分辨方向的问题。单个 OPM 约乐高积木大小，噪声本底约 7–10 fT/√Hz(SQUID 约 2–5 fT/√Hz)。② **磁屏蔽**——OPM 是矢量磁力计且动态范围小(场变化超过约 3 nT 即停止工作)，所以可穿戴 MEG 的成败高度依赖屏蔽；现行方案是"被动屏蔽(mu-metal + 高导材料)+ 主动屏蔽(参考传感器测残余场、线圈发等大反向场抵消)"。③ **应用与未决问题**。

## 关键数据

- 屏蔽效果链条：无屏蔽约 **60 µT**(地磁场)→ 仅被动屏蔽约 **5 nT** → 被动+主动屏蔽约 **200 pT**，屏蔽因子约 **300 000**。
- 未屏蔽条件下 OPM 的动态范围问题：在约 30 nT 的"典型 MEG 屏蔽环境"里，头部旋转约 **4°** 就足以让 OPM 失效。
- OPM 噪声本底约 **7–10 fT/√Hz**；SQUID 约 **2–5 fT/√Hz**。综述明确指出当前 OPM 尚未达到 SQUID 的噪声本底，对**浅层皮层源**靠贴近头皮补偿有余，对**深部源** SQUID 仍可能占优。

## 为什么是 milestone

本子线的 **milestone 抽取源**。更重要的是它在正文和 Outstanding Questions 里把当时(2022)的未决问题写得很明确，构成后续工作的评判基准：

1. **"已发表工作使用的线圈只在头部上方一个固定体积内补偿磁场(允许自由转头)，模块化线圈设计有望扩展这一能力，最终使人在房间里走动时也能扫描。"**
2. **"虽然置零线圈已能产生低场环境，但大幅运动(例如被试行走)尚未被演示……开发可重构线圈、把零场体积放到房间任意位置，以及把残余场进一步降低，仍是关键发展方向。"**
3. 屏蔽本身"仍笨重且昂贵"，能否做得更小更轻以便在临床落地，被列为公开问题。

评估任何"OPM-MEG 走出屏蔽室 / 房间尺度自由活动"的新工作时，先对照这三条看它动的是哪一格。相关条目：[[boto-2018-wearable-meg-nature]]、[[holmes-2018-biplanar-nulling-coils]]、[[zhang-2020-unshielded-earth-field-meg]]。
