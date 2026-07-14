---
title: "Towards passive brain-computer interfaces: applying brain-computer interface technology to human-machine systems in general"
authors: Zander TO, Kothe C
year: 2011
venue: Journal of Neural Engineering 8:025005
url: https://doi.org/10.1088/1741-2560/8/2/025005
subfield: passive-bci
tags: [passive-BCI, neuroadaptive, taxonomy, cognitive-monitoring, EEG, review]
---

## 解决了什么问题
传统 BCI 把脑活动当作使用者主动发出的显式指令(active/reactive),要求用户刻意产生某种脑状态去控制系统。这篇提出:实时脑信号解码(RBSD)得到的隐式认知状态(错误感知、工作负荷、意图、情绪等)本身就能作为一路输入,让技术系统利用——无需用户主动发指令。作者把这类应用命名为 **passive BCI**,并给整个 BCI 应用空间提出统一分类。

## 核心方法
提出以"用户意图是否为控制系统而刻意产生"为轴的三分类框架:
- **active BCI** — 用户主动产生、直接用于控制的脑活动(如运动想象控制光标);
- **reactive BCI** — 由外部刺激诱发、用户借注意调制的脑活动(如 P300、SSVEP);
- **passive BCI** — 自发的认知状态,用户并非为控制而产生,系统被动读取并加以利用。
认知监测(cognitive monitoring)与 BCI 技术在此融合:同一套 RBSD 管线既可做显式控制,也可做隐式状态估计。综述汇总了当时利用隐式状态(错误相关电位、工作负荷等)增强人机交互的研究,并特别面向健康用户的需求界定应用形态。

## 关键数据
- 本文为定义性综述(review),不报告单一实验数据;贡献在于**术语与分类框架**本身。
- "passive BCI"一词自此确立,成为后续 neuroadaptive technology、隐式交互一整条线的命名与概念地基。

## 为什么是 milestone
它把"脑状态作为隐式输入"从零散工作提升为一个有明确定义、有分类坐标的研究范畴,是 passive-BCI / 神经自适应子领域的抽取源与框架原点。此后错误电位监测、工作负荷自适应、neuroadaptive 闭环(Zander 2016)、操作环境部署(Aricò 2016)都在这个坐标系里定位。
