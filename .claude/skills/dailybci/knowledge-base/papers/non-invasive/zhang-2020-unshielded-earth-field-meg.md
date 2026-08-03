---
title: "Recording brain activities in unshielded Earth's field with optically pumped atomic magnetometers"
authors: Zhang R, Xiao W, Ding Y, Feng Y, Peng X, Shen L, Sun C, Wu T, Wu Y, Yang Y, Zheng Z, Zhang X, Chen J, Guo H
year: 2020
venue: Science Advances 6:eaba8792
url: https://doi.org/10.1126/sciadv.aba8792
subfield: non-invasive
tags: [OPM, 无屏蔽, 地磁场, 标量磁力计, AM-NMOR, 梯度计]
---

## 解决了什么问题

主流 OPM-MEG 走的是 SERF 路线，而 SERF 只在近零场工作，因此必须待在被动磁屏蔽室里(见 [[allred-2002-serf-magnetometer]]、[[boto-2018-wearable-meg-nature]])。这篇换一条技术路线，直接问：能不能不要屏蔽室，在**未屏蔽的地磁场**(约 50 µT)里测到脑磁？

## 核心方法

放弃 SERF，改用**幅度调制非线性磁光旋转(AM-NMOR)** 标量磁力计——这类传感器的工作场范围宽得多，可覆盖地磁场量级。用两个铯原子 AM-NMOR 磁力计构成**梯度计**做差分探测，抑制远场共模干扰，并加反馈进一步压低磁场噪声。

## 关键数据

- 传感器：**2 通道**(双传感器原子梯度计)，铯原子 AM-NMOR 标量磁力计。
- 未屏蔽条件下磁场梯度噪声本底约 **4 fT/cm·√Hz**。
- 记录到与闭眼相关的自发 **alpha 节律(7–13 Hz)** 和清晰的**听觉诱发场 M100** 成分(刺激后约 100 ms)。
- **未做源定位**——工作聚焦在信号检出与表征。

## 为什么是 milestone

证明"脱离磁屏蔽室测脑磁"在物理上可行，并给出与 SERF 完全不同的技术路径(宽场标量磁力计 + 梯度计差分)。

**但它的边界必须讲清，否则会高估**：2 通道、无源定位。而源定位要求一整个阵列、且每个传感器沿已知方向测量(见 [[tierney-2019-opm-quantum-origins]])。所以"在无屏蔽环境测到信号"与"在无屏蔽环境做源成像"之间还隔着一大步。这一步是此后该方向的核心待办，也是评估任何"开放环境 OPM-MEG"新工作时首先要问的问题：它是只测到了信号，还是真的定位了源？

（通讯作者 Hong Guo，北京大学。2026 年那篇"开放环境可穿戴 OPM-MEG"(Zheng et al., bioRxiv 2026.07.28.740707)通讯作者为北京大学高家红，作者列表与本篇无重合——同校、不同作者群，横向对照时注意区分。）
