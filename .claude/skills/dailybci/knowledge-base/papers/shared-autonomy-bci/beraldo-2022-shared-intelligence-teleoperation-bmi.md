---
title: "Shared Intelligence for Robot Teleoperation via BMI"
authors: Beraldo, Tonin, Millán, Menegatti
year: 2022
venue: IEEE Transactions on Human-Machine Systems, 52(3):400-409
url: https://doi.org/10.1109/THMS.2022.3155716
subfield: shared-autonomy-bci
tags: [non-invasive-BCI, EEG, shared-control, telepresence, robot-teleoperation]
---

## 解决了什么问题
EEG-BMI遥操作移动机器人/远程呈现机器人时,用户发出的指令带宽低、噪声大,若机器人完全被动执行解码指令,导航效率和安全性都受限;需要机器人自身具备一定"智能"来弥补低带宽指令的不足。

## 核心方法
提出"共享智能(shared intelligence)"框架:机器人自主导航/避障能力与用户经BMI发出的高层指令相结合,机器人在用户指令框架内自主处理低层执行细节(如避障、路径微调)。

## 关键数据
在机器人远程呈现/遥操作任务上验证,证明该框架下用户仅需发出稀疏、低带宽的高层指令,机器人即可完成原本需要连续精细控制的导航任务。

## 为什么是 milestone
是EEG-BMI遥操作方向"共享智能"路线的代表作,与 [[ghasemi-2022-shared-autonomy-eeg-bci]] 一起构成非侵入式BCI共享自主的两条并行工作,补齐了皮层内BCI(Muelling/Downey路线)之外的非侵入式对照案例。
