---
title: "Excitatory and inhibitory interactions in localized populations of model neurons"
authors: Wilson, Cowan
year: 1972
venue: Biophysical Journal 12:1–24
url: https://doi.org/10.1016/S0006-3495(72)86068-5
subfield: brain-encoding-models
tags: [neural-mass, mean-field, dynamical-systems, foundational]
---

## 解决了什么问题
单神经元层面的动作电位生成机制在 1950 年代已由 Hodgkin–Huxley 模型解决，但感知与运动来自大量神经元的集体行为。缺的是一套描述**神经元群体**而非单个细胞的数学。

## 核心方法
把局部皮层组织抽象成相互耦合的兴奋性与抑制性两个群体，用各自的**平均发放率**作为状态变量写出一对耦合的非线性微分方程，群体输入-输出关系由 sigmoid 型激活函数给出。这样就把描述层级从单个细胞的膜电位换成了群体活动水平。

## 关键数据
- 理论工作，非实验记录。
- 模型给出的定性行为：稳定不动点、迟滞、以及在参数区间内的极限环振荡——后者为皮层节律提供了群体层面的动力学解释。

## 为什么是 milestone
神经质量模型（neural mass model）的奠基工作，此后全部全脑动力学建模的基本构件。今天的全脑模型（[[honey-2007-network-structure-shapes-fc]]、[[deco-2009-coupling-delay-noise]]）本质上是把这类局部群体模型按连接组耦合起来。术语上要注意：这里的"群体"是解剖上邻近的局部群体，与群体动力学（population dynamics）子领域讨论的"记录到的神经元群体状态空间"是不同的概念。
