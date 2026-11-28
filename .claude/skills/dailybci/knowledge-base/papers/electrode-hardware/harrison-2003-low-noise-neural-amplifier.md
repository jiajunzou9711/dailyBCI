---
title: "A low-power low-noise CMOS amplifier for neural recording applications"
authors: Harrison, Charles
year: 2003
venue: IEEE Journal of Solid-State Circuits 38(6):958–965
url: https://doi.org/10.1109/JSSC.2003.811979
subfield: electrode-hardware
tags: [neural-amplifier, input-referred-noise, 1/f-noise, CMOS, front-end]
---

## 解决了什么问题
多通道植入式记录需要每通道一个前置放大器（neural amplifier），它同时要满足三条约束：输入参考噪声低于胞外动作电位幅度、功耗低到可以多通道集成、能抑制电极与组织界面的直流偏置（DC offset）。这篇给出一个同时满足三条的 CMOS 实现。

## 核心方法
- 1.5 µm CMOS 工艺，电容反馈的全差分放大器。
- 用 MOS-双极型伪电阻（MOS-bipolar pseudoresistor）提供极大的反馈电阻，把高通截止压到 0.025 Hz，从而隔掉电极的直流偏置。
- 输入管用大栅面积 pMOS，压低 1/f 噪声。

## 关键数据
- 通带 0.025 Hz–7.2 kHz；输入参考噪声 2.2 µVrms（输出噪声除以增益得到，Fig. 8）。
- 功耗 80 µW，面积 0.16 mm²。
- 噪声谱（Fig. 7）：热噪声平台约 21 nV/√Hz，1/f 角频率（corner frequency）约 100 Hz。
- 同文给出 EEG 用变体：带宽 30 Hz，功耗 0.9 µW。
- 实测对象是芯片本身，未做动物或人体记录。

## 定位
神经记录前端放大器设计中被大量引用的电路论文；2026-11-28 原理期《读懂放大器规格表上的「输入参考噪声」》用它的 Fig. 7/8 讲噪声谱与「输出噪声 ÷ 增益」的测法。尚未按 selecting-milestone-papers 流程判定是否为里程碑。
