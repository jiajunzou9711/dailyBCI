---
title: "The Self-Paced Graz Brain-Computer Interface: Methods and Applications"
authors: Scherer R, Schloegl A, Lee F, Bischof H, Janša J, Pfurtscheller G
year: 2007
venue: Computational Intelligence and Neuroscience
url: https://doi.org/10.1155/2007/79826
subfield: non-invasive
tags: [self-paced-BCI, motor-imagery, idle-state, EEG, sensorimotor-rhythm]
---

## 解决了什么问题
运动想象(motor imagery)类EEG-BCI此前多为cue-based(系统提示何时输入)，不支持用户自主决定何时发起/停止控制；要走向真实场景应用(如轮椅、虚拟环境导航)，BCI必须能自动判断当前脑活动是"有意图控制(intentional control, IC)"还是"非控制(non-control, NC)"这一自然的第三态。

## 核心方法
Graz组提出3类自定步调BCI:先用cue-based训练获得区分3种运动想象模式的分类器(CFR_MI)，再单独训练一个二分类器(CFR_IC)专门判别"运动想象相关脑活动"vs"背景EEG"，两级分类器组合后即可在完全无外部提示下持续输出IC/NC状态；同时集成EMG伪迹检测与EOG伪迹自动去除，仅用3个双极EEG通道。系统在freeSpace虚拟环境(自主导航拾币)和操作Google Earth(Brainloop界面)两个真实闭环任务中验证。

## 关键数据
3名健康受试者均成功用自定步调BCI在虚拟环境中自主导航拾币(2/3受试者拾到全部3枚)；IC vs NC判别的LDA分类准确率(10×10交叉验证)为77%、84%、78%；EOG伪迹去除约80%；受试者访谈确认"无操作(NC)"状态被主动、有意地用于休息/思考时段，而非仅是分类器噪声。

## 为什么是 milestone
是"显式无动作/非控制态"作为BCI连续控制系统内建组成部分(而非事后阈值)的早期、方法完整的实证之一，直接对应今日候选(Müller-Putz组，同一Graz谱系)"支持主动起停的连续光标控制"这一设计目标的概念前驱。
