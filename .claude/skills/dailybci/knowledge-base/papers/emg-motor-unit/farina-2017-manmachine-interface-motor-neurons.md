---
title: "Man/machine interface based on the discharge timings of spinal motor neurons after targeted muscle reinnervation"
authors: Farina, D., Vujaklija, I., Sartori, M., Kapelner, T., Negro, F., Jiang, N., Bergmeister, K., Andalib, A., Principe, J., Aszmann, O. C.
year: 2017
venue: Nature Biomedical Engineering 1:0025
url: https://doi.org/10.1038/s41551-016-0025
subfield: emg-motor-unit
tags: [man-machine-interface, prosthetics, motor-neuron-discharge, TMR, neural-interface]
---

## 解决了什么问题
传统肌电假肢控制把 EMG 幅度当作控制信号,受非神经因素干扰、维度有限。本文提出一种更接近"神经"的接口:直接用**脊髓运动神经元的放电时序**作为控制命令,而非原始肌电包络。

## 核心方法
在做过**靶向肌肉神经移植(TMR)**的高位截肢者身上(缺失肢体的神经被移植到残端肌肉),用 HD-sEMG 记录被重新支配肌肉的电活动,经卷积盲源分解恢复运动神经元放电时序,再把这些放电序列映射成多自由度控制命令(直接比例控制 / 模式识别 / 肌骨建模)。本质是把"神经驱动"而非肌肉幅度作为人机接口的信号。

## 关键数据
- 6 名肩离断/肱骨水平截肢者(TMR 后)。
- 基于运动神经元放电时序的离线接口性能优于 TMR 后常规直接肌电控制。
- 物种:人类(截肢患者)。注:论文报告为离线(offline)评估。

## 为什么是 milestone
这是把运动单位解码从"研究肌肉生理"推向**真正的神经接口/假肢控制**的关键一跃——证明脊髓运动神经元放电时序可作为人机接口信号。它把 [[deluca-1994-common-drive]]→[[farina-negro-2015-common-synaptic-input]] 的神经驱动框架与 [[holobar-2007-convolution-kernel-compensation]]/[[negro-2016-convolutive-bss-decomposition]] 的分解技术合流到应用端;也是本子领域与脑机接口主线(motor-bci/外周神经接口)最直接的接点。
