---
title: "Electroencephalogram and visual evoked potential generation in a mathematical model of coupled cortical columns"
authors: Jansen, Rit
year: 1995
venue: Biological Cybernetics 73:357–366
url: https://doi.org/10.1007/BF00199471
subfield: brain-encoding-models
tags: [neural-mass, EEG, evoked-potential, cortical-column, forward-model]
---

## 解决了什么问题
[[wilson-cowan-1972-excitatory-inhibitory]] 给出了群体动力学的形式，但要把它与实际可测的信号对上，需要说明模型的状态变量如何生成 **EEG 波形**与**诱发电位**这类具体观测量。

## 核心方法
把皮层柱建模为锥体细胞群 + 兴奋性中间神经元群 + 抑制性中间神经元群三个相互连接的群体，各自带有描述突触响应的二阶线性算子与群体发放的 sigmoid 非线性；再把若干这样的柱耦合起来，用锥体细胞群的膜电位作为 EEG 的代理输出。

## 关键数据
- 理论/仿真工作。
- 同一套模型在不同参数下既能产生自发的类 alpha 节律活动，也能在脉冲输入下产生形态类似**视觉诱发电位**的波形。

## 为什么是 milestone
把神经质量模型从抽象的群体动力学推进到**可与真实 EEG 观测量直接对照**的前向模型，这一步使模型可被数据证伪。它也是动态因果建模（[[friston-2003-dynamic-causal-modelling]]）中 EEG/MEG 版本所用生成模型的直系祖先。对非侵入 BCI 而言，这条线解释的是"头皮上量到的波形从哪来"，与 EEG 信号处理线互补。
