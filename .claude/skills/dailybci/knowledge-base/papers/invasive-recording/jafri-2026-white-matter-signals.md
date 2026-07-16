---
title: "Electrophysiological features of signals recorded from white matter"
authors: Jafri, Ortega, Manivannan, et al. (通讯 Bartoli; 资深含 Sheth, Hayden, Heilbronner, Provenza)
year: 2026
venue: bioRxiv (预印本)
url: https://doi.org/10.64898/2026.07.11.737939
subfield: invasive-recording
tags: [white-matter, sEEG, aperiodic, 1/f-exponent, complexity, HFD, LZC, volume-conduction, Baylor, stop-signal]
---

## 解决了什么问题

颅内电生理长期把落在**白质(WM)**的 sEEG 触点当伪迹、或当作邻近灰质(GM)信号经容积传导泄漏过来的**衰减副本**，直接 mask 掉。这个默认有理论依据：按 [[buzsaki-2012-extracellular-fields-origin]] 的框架，胞外场主要由树突上的**突触电流**产生、且需神经元几何排列一致才能同相叠加，而白质**无胞体/无树突/无突触、只有有髓轴突**，"不该"有强局部场。但白质占脑容量 40% 以上(论文称)，而 sEEG 探针是**直杆+等距触点**，穿过哪种组织由几何决定——本研究 1717 个触点里 **36% 落在白质**，等于三分之一通道被默认丢弃。本篇检验：白质信号到底是不是灰质的衰减副本。

## 核心方法

19 名药物难治性癫痫患者(Baylor St. Luke's)的 sEEG，清醒静息 5 分钟 + stop-signal 任务(n=9 子集)。触点经 iELVis(CT-MRI 配准)+ Destrieux 图谱按周围 3 mm 体素判为 GM/WM/subcortical/boundary，**混合的 boundary 触点直接排除**。核心是**谱参数化**：把功率谱拆成**非周期成分**(offset=总功率 / exponent=1/f 斜率)与**周期成分**(各频段中心频率)，再加两个时域复杂度指标(HFD、LZC)。

**论证枢纽**：衰减在数学上=乘一个常数=对数坐标下整条线平移 → **只能动 offset，动不了 exponent**；且衰减在**频率轴上无能为力**。这给出可证伪的预言。另做 KNN 子空间集成分类器(仅凭信号特征猜组织类型)、FA(弥散张量)与复杂度的相关、以及任务时频分析(5000 次置换+簇校正)。控制分析换了第二种重参考方案，结果几乎一致。

## 关键数据

- **1717 触点 / 19 人，36% 在白质**
- offset：WM 2.97±0.902 vs GM 3.88±0.861 (β=−0.91, p<0.001) —— 符合衰减
- **exponent：WM 2.46±0.388 vs GM 2.77±0.374 (β=−0.3, p<0.001)，且 19 人全部低于等值线、无一例外** —— **衰减解释不了，假说被证伪**
- **delta 中心频率：WM 2.40±1.13 vs GM 2.00±1.12 Hz (β=0.43, p<0.001)**；alpha 10.9 vs 10.7 (p=0.005)；theta/beta n.s. —— **频率位移完全免疫于幅度缩放，是更干净的一刀**
- 复杂度：HFD WM 1.39±0.187 vs GM 1.30±0.171 (p<0.001)；LZC 0.464 vs 0.354 (p<0.001)
- HFD–exponent rho=−0.59 (p<0.001)，**每名被试单独看都显著**(−0.28～−0.94)；LZC–exponent 仅 15/19 人显著
- 分类器(仅凭信号猜组织)：exponent 单特征 **AUC=0.76**；5 特征 **AUC=0.92**(置换 n=1000, p<0.001) —— 特征非冗余
- 任务：**9 人中 6 人**至少一个白质位点区分 Stop-Success/Stop-Fail；逐人比例 WM 0–39% / GM 0–29%(**均值 8.6% vs 9.0%，按 Table 1 自算，论文未报告**)，调制在 broadband gamma(>40Hz)或 beta
- **FA–HFD 仅 rho=0.12 (p=0.023)，FA–LZC rho=0.09 (p=0.098) 不显著** —— 结构锚点很弱，**摘要/讨论的措辞强于结果部分**(结果写 "weak"，摘要略去)

## 为什么是 milestone

**不是"首次发现白质有信息"**——这条线的前作是：Mercier 2017(NeuroImage 147:219–232，白质信号无法由邻近灰质完全解释)、**Greene 2021**(Front Neurol 11:605696，用谱差异分类触点，**但目的是更干净地丢弃白质**)、**Li G. 2021**(J Neural Eng 18:0460c6，**纳入白质触点提升运动解码——解码增益的实证出处**)、Huang 2023(Nat Commun 14:3414)、Revell 2026(Brain 149:77–89，白质携带癫痫传播信息)、Mercier 2026(Brain 149:6–8 评论"Beyond grey")。

本篇的分量在于**系统刻画 + 把"衰减/泄漏"这个替代解释钉死**：offset 与 exponent 分离，让"衰减"成为可证伪预言并被证伪；delta 频率位移则连滤波性质都不必讨论。价值是把 [[buzsaki-2012-extracellular-fields-origin]] 的理论"对了一半"讲清楚——它正确预言两边生成机制不同(灰质=慢突触电流→谱陡；白质若有本地源只能是约 1 ms 轴突动作电位→谱平，与 [[ray-2011-high-gamma-origin]] 的 broadband gamma=群体放电率自洽)，错在从"无经典发生源"跳到"什么都没有"。

**对 BCI 的意义**：LFP 由突触电流主导→灰质电极偏向"该区收到了什么"；轴突只运输出→白质电极偏向"上游区发出了什么"。**输入≠输出**，这是白质通道原则上**互补而非冗余**的原理基础，也为 Li 2021 已观察到的解码增益提供机制解释。

**证据强度分层(重要，防日后误引)**：谱/复杂度差异(19 人/1717 触点)**最强**；TPJ–SLF 示例(两触点相距很远却高度相似→**距离排除容积传导**→更可能读到沿束传输的内容)**论证漂亮但 n=1、且未排除"共同输入"**；纤维束"对上停止网络"**最弱**——归位是作者自陈的 **"putative"**，**主文未描述任何归位方法**(无白质图谱、无 tractography)，且每束仅 1–3 个触点。本篇**不做行为解码**，功能分析仅单被试层面、无组水平检验。
