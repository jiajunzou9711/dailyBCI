---
title: "Functional ultrasound imaging of the brain"
authors: Macé, Montaldo, Cohen, Baulac, Fink, Tanter
year: 2011
venue: Nature Methods 8:662–664
url: https://doi.org/10.1038/nmeth.1641
subfield: functional-ultrasound
tags: [fUS, ultrafast-doppler, cerebral-blood-volume, neurovascular-coupling, rat]
---

## 解决了什么问题
在 fMRI(空间分辨率毫米级、时间分辨率秒级)与光学成像(仅限皮层表面)之间,缺少一种既能覆盖整脑深部、又有亚毫米空间分辨率和亚秒时间分辨率的功能成像手段。常规超声多普勒对小血管里的低速血流不敏感,测不到与神经活动耦合的微血管血容量变化。

## 核心方法
把 [[montaldo-2009-plane-wave-compounding]] 的超快平面波成像用于脑血流:以高帧率连续采集,对时间序列做杂波滤除后计算功率多普勒,得到**脑血容量(cerebral blood volume, CBV)**的瞬态变化图像。作者把这一模态命名为 **functional ultrasound(fUS)**。测量对象是神经血管耦合下的血容量信号(与 fMRI 的 BOLD 一样是间接信号,不直接记录动作电位)。

## 关键数据
- 相比既往超声方法,可测更小血管中的血流,从而检出与神经活动相关的 CBV 变化。
- 在**大鼠**上成像了触须刺激诱发的皮层与丘脑响应,以及癫痫样发作在脑内的传播。
- 论文报告 fUS 在时空分辨率上优于当时其他功能脑成像模态(原文表述为 "better spatiotemporal resolution than with other functional brain imaging modalities")。

## 为什么是 milestone
fUS 的**原始方法学论文**,定义了这一整条模态:用超快多普勒读取神经血管耦合。此后 fUS 的所有分支——清醒自由活动记录([[sieu-2015-fus-eeg-mobile-rats]])、超分辨([[errico-2015-ultrasound-localization-microscopy]])、非人灵长类([[blaize-2020-fus-deep-visual-cortex-nhp]])、人体([[demene-2017-fus-human-newborns]]、[[rabut-2024-human-acoustic-cranial-window]])、乃至脑机接口解码([[norman-2021-single-trial-decoding-fus]]、[[griggs-2024-closed-loop-ultrasonic-bmi]])——都以这篇为起点。对 BCI 语境的关键含义:fUS 记录的是血流动力学信号,时间尺度受神经血管耦合限制(秒级),这既是它的天花板,也是它能"不穿刺皮层"的原因。
