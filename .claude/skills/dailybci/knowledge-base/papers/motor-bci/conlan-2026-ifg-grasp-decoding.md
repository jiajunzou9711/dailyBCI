---
title: "Assessing the Relative Impact of Grasp and Object on Inferior Frontal Gyrus Activity during a Grasping Task"
authors: Conlan, Foli, Memberg, Herring, Sweet, Ajiboye
year: 2026
venue: bioRxiv (preprint)
url: https://doi.org/10.64898/2026.06.30.735663
subfield: motor-bci
tags: [IFG, F5, lateral-grasp-network, electrode-target, Utah-array, intracortical, factorial-design, tetraplegia]
---

## 解决了什么问题
皮层内抓握解码过去几乎都以初级运动皮层(M1)为靶点(同组 Ajiboye 2017)。人类唯一一篇记录额下回(IFG,猕猴F5人类同源区)的皮层内先例(Wandelt et al. 2022, Neuron)证明了能从该区解码出特定"抓法-物体"组合,但未拆分驱动信号的到底是抓法、物体,还是两者的交互——这篇论文填的就是这个缺口。

## 核心方法
同一位C3-C4 AIS-B四肢瘫参与者(RP1,Case Western/Cleveland VA的ReHAB临床试验)左半球植入六个8×8犹他阵列(M1×2、S1×2、AIP×1、IFG×1),本文仅用IFG阵列64通道。采用3种抓法(power/pinch/lateral)×3种物体(球/方块/棒)的析因设计(9条件),在意念抓握(motor imagery/attempted movement)任务中,用5折交叉验证线性判别分析分别在premovement和movement两个时期解码抓法、物体、二者交互。

## 关键数据
- 抓法解码准确率:premovement 41.1%±1.3%,movement 41.8%±1.3%(3分类随机水平33.3%)
- 抓法高于随机水平约7.7-8.5个百分点,显著高于物体(约+1.4至-1.5个百分点)和交互项(约+0.6个百分点),p<0.001(Tukey-Kramer)
- movement期物体解码已不再显著高于随机水平
- 物体信息峰值比抓法早约200ms出现,随后迅速减弱
- 单例人类参与者(n=1),离线分析,未做实时闭环验证

## 为什么是 milestone
不是范式转变型的里程碑,而是**确证性/澄清性**贡献——首次在人类IFG皮层内记录里,用析因设计把"抓法"与"物体"两个此前在猕猴F5生理学和唯一人类先例(Wandelt 2022)中始终纠缠不清的因素干净拆开。价值在于:①为知识库补上"非M1皮层内电极靶点"这条此前空白的线(与 Ajiboye 2017 形成纵向对照);②提出IFG因premovement期即可解码抓法、可能提供比M1更早意图读出的候选靶点角度,但尚未经闭环验证。
