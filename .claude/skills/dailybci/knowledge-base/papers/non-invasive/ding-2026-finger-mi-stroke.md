---
title: "Adaptive Neural Reorganization Enables Real-Time Finger-Level Robotic Control in BCI-Naïve Stroke Survivors"
authors: Ding, Karrenbach, Johnson, Wang, Zhang, Wittenberg, He
year: 2026
venue: bioRxiv (preprint)
url: https://doi.org/10.64898/2026.06.15.732267
subfield: non-invasive
tags: [non-invasive, EEG, motor-imagery, finger-decoding, stroke, rehabilitation, EEGNet, robotic-hand, BCI-naive]
---

## 解决了什么问题
非侵入(头皮 EEG)脑机接口在中风人群长期停在粗粒度控制(整手开合/抓握)——头皮 EEG 空间分辨率仅厘米级、容积导体糊化、手指在运动皮层表征高度重叠,使"逐指"长期被视作皮层内电极的专属;中风又被认为会让信号重组、变乱、更难解。此前非侵入逐指机械手控制只在健康、有 BCI 经验者身上做过(同组 Ding et al., Nat Commun 2025,2 指 80.6%/3 指 60.6%)。本研究问:**零 BCI 经验的中风患者能否仅凭头皮 EEG + 运动想象,实时控制单根机械手指?**

## 核心方法
9 名 BCI-naïve 慢性中风患者(6 男 3 女,平均 68.9±8.1 岁,8 名右利;6 人有单侧运动障碍),128 通道 BioSemi ActiveTwo 头皮 EEG(非侵入,湿电极)。先做两次肢体级 MI 训练熟悉范式,再做逐指 MI 在线任务:想象拇指/食指/小指运动,用 **EEGNet-8,2 紧凑卷积网络**实时解码、每 125 ms 出一次决策驱动机械手(majority-vote 精度)。在线滤波从 4–40 Hz 改为 0.5–40 Hz(纳入 delta);并对比 Base 与逐人 Fine-tuned 模型。配合传感器级/源级电生理分析(ERD、MRCP、频带地形、wPLI 连接、PAC)刻画中风后神经重组。

## 关键数据
- **逐指控制可行**:训练末群体平均 2 指(拇 vs 小)**83.5%**(随机 50%)、3 指(拇/食/小)**61.4%**(随机 33%);7 个阶段内显著学习提升(ANOVA 前 5 阶段:binary F=10.3, p<0.001;ternary F=4.29, p=0.003)。Base 与 Fine-tuned 差异不显著。
- **食指是软肋**:3 分类中食指 recall 仅 0.38,42% 被误判为拇指(夹在中间最难分);拇 0.71、小 0.75。
- **患侧 ≈ 健侧**:患侧手 MI(n=6)精度与健侧组(n=3)基本持平(Cohen's d=0.18/0.42);优势手 > 非优势手(d=0.78/0.53);臂级(光标)MI 与指级 MI 精度正相关(Pearson r=0.636)。
- **低频是信号**:纳入 delta(0.5–4 Hz)后解码精度明显上升(线性混合模型控制学习效应后仍显著)。
- **重组特征**:相比健康对照,中风组去同步更双侧、更弥散(对侧/同侧手区、额、顶均贡献解码),低频(delta/theta)活动更强(DAR 升高),MRCP 波幅衰减、潜伏期延后,theta/beta 源级 wPLI 连接改变。
- **对照前作**:零经验的中风患者(83.5/61.4)与同组 2025 年健康熟练者(80.6/60.6)基本持平甚至略高。

## 为什么是 milestone
首次在**零经验的中风患者**身上、用**非侵入头皮 EEG** 实现实时**逐指**机械手控制,把 He 组的非侵入逐指路线从健康熟练者推进到最需要它的临床人群。它给出一个反直觉证据链:中风损伤的是"皮层→脊髓→肌肉"输出通路,而产生手指意图的皮层编码大体幸存,只是被**重组**成更双侧、分散、低频的形态;被当作病理标志(预后用)的低频慢波其实**携带可解码的手指信息**;柔性数据驱动解码器(EEGNet,见 lawhern-2018-eegnet)不套用"对侧 mu-ERD"模板,才能跟住这种重组后的个体化模式。与 BCI 卒中康复线(ramos-murguialday-2013、ang-2015、biasiucci-2018)互补:那条线证 BCI 可驱动可塑性,这篇证精细运动意图在中风后仍可被非侵入读出。仍属可行性结果(3 指 61%、食指弱、病灶—表征因果未做),非日常可用产品。
