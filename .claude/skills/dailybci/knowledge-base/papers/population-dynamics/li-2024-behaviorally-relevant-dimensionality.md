---
title: "Revealing unexpected complex encoding but simple decoding mechanisms in motor cortex via separating behaviorally relevant neural signals"
authors: Li, Zhu, Qi, Wang, Gallego
year: 2024
venue: eLife 13:e87881
url: https://doi.org/10.7554/eLife.87881
subfield: population-dynamics
tags: [dimensionality, motor-cortex, behaviorally-relevant-signals, decoding, monkey]
---

## 解决了什么问题
"运动皮层是低维的"被广泛引用，但**低维的到底是什么**——是全部神经活动，还是其中与行为相关的那部分？两者未被清晰分离。

## 核心方法
提出一个框架，把神经信号中**与行为相关的成分**与其余成分分离，再分别刻画两者的维度与可解码性；在三只猕猴、不同够物任务的数据上验证。

## 关键数据
- 原始神经信号主子空间的维度分别为 **26、64、45**（三个猕猴数据集）。
- **行为相关信号的维度显著更低：7、13、9**。
- 论文自身的主张：那些以往被认为信息很少的神经响应，实际以复杂非线性方式编码了丰富的行为信息，**行为占据的神经空间比以往认为的更高维**；纳入这些常被忽略的维度后，线性解码即可达到与非线性解码相当的性能。
- 物种：**猕猴**。

## 为什么是 milestone
它给出了"运动皮层行为相关维度约 10 维量级"这个可引用的具体数字，也正是**冗余为何在运动 BCI 上成立**的定量基础（约 100 通道的随机阵列足以覆盖十来个独立方向）。**引用时须注意**：该文的落脚点是"维度比想象的高"，不要把它简单当作"运动皮层就是低维"的证据。
