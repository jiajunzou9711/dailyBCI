---
title: "Dendritic calcium signals in rhesus macaque motor cortex drive an optical brain-computer interface"
authors: Trautmann EM, O'Shea DJ, Sun X, et al., Deisseroth K, Shenoy KV
year: 2021
venue: Nat Commun 12:3689
url: https://doi.org/10.1038/s41467-021-23884-5
subfield: optical-bci
tags: [two-photon, macaque, optical-BCI, dendritic-imaging, motor-cortex, Shenoy]
---

## 解决了什么问题
光学 BMI 此前只在小鼠上做成过。要把它用于研究与人更接近的运动皮层，卡点在光子散射：表面双光子成像**够不到**猕猴运动皮层各层的胞体钙信号。

## 核心方法
猕猴，开发可长期使用、带运动稳定的双光子成像植入与成像系统，在动物执行运动任务时成像。绕开胞体不可及的办法是改成像**顶树突（apical dendrites）**，从而在光学上接入背侧前运动皮层（PMd）与回部初级运动皮层（M1）的大量深层与浅层神经元；再用这些树突信号在线解码运动方向，驱动光学 BCI（oBCI）。最后用 CLARITY 容积成像回溯这些树突的来源细胞。

## 关键数据
- 单个神经元的树突信号对不同手臂运动方向表现出方向调谐。
- oBCI 成功在线解码运动方向。
- 容积成像验证：许多参与解码的树突来自**第 5 层输出神经元**，包括一个疑似 Betz 细胞。

## 为什么是 milestone
把光学 BCI 从小鼠推进到非人灵长类，并给出了一个绕开物理限制的具体解法——记录树突而非胞体。对 BCI 路线的含义：光学接入深层输出神经元在灵长类上是可行的，尽管代价是信号来自树突而非胞体。相关：[[clancy-2014-optical-neuroprosthetic-learning]]、[[zhang-2018-closed-loop-all-optical]]
