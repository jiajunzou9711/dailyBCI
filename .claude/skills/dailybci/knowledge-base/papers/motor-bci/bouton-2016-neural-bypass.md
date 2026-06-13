---
title: "Restoring cortical control of functional movement in a human with quadriplegia"
authors: Bouton, Shaikhouni, Annetta, Bockbrader, Friedenberg, Nielson, Sharma, Sederberg, Glenn, Mysiw, Morgan, Deogaonkar, Rezai
year: 2016
venue: Nature
url: https://doi.org/10.1038/nature17435
subfield: motor-bci
tags: [neural-bypass, FES, functional-electrical-stimulation, own-hand, quadriplegia, Battelle]
---

## 解决了什么问题
之前的 motor BCI 控制的都是外部设备（光标、机器人手臂）。能否让瘫痪患者恢复对自己手部的控制——用大脑信号绕过受损的脊髓，直接驱动自己的肌肉？

## 核心方法
"Neural bypass"方案：在一名 C5/C6 脊髓损伤患者的运动皮层植入 Utah 阵列，解码运动意图信号，通过功能性电刺激（FES）电极套装直接激活前臂肌肉。BCI 解码出的不是光标位移，而是手部动作类型和力度，FES 按比例驱动对应的肌肉群。关键创新：实现了分级控制（graded control），而非简单的开/关。

## 关键数据
- 患者恢复了手腕和手指的自主运动
- 可执行 6 种不同的手部/腕部动作
- 实现了分级肌肉收缩控制（非二元开/关）
- 患者瘫痪超过 6 年后仍可恢复控制

## 为什么是 milestone
首次实现"neural bypass"——将 BCI 从控制外部设备转向恢复患者自身肢体的运动。这在概念上是一个根本性转变：BCI 不再是"义肢替代"，而是"功能修复"。分级控制的实现说明解码精度已经足以支撑自然的运动控制，而不仅仅是触发预设动作。
