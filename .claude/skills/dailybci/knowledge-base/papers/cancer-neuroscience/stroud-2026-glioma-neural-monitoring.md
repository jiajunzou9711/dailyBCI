---
title: "Neural correlates of glioma progression using implanted neural interfaces"
authors: Stroud, Bratsch-Prince, Coles, Middya, ..., Monje, Woodington, Jenkins et al.
year: 2026
venue: bioRxiv
url: https://doi.org/10.64898/2026.07.01.735772
subfield: cancer-neuroscience
tags: [glioma, GBM, DIPG, LFP, gamma-band, tumor-monitoring, cancer-neurotechnology, implantable, closed-loop, mouse-xenograft]
---

## 解决了什么问题
脑肿瘤（尤其高级别胶质瘤）临床监测靠间断 MRI 快照，信号间接（钆增强反映血脑屏障渗漏而非肿瘤细胞）、且被假性进展/假性反应混淆，缺少连续、在体、实时的肿瘤状态读出。cancer neuroscience 已证明神经活动驱动胶质瘤、肿瘤电整合进神经环路（[[venkatesh-2019-electrical-synaptic-integration-glioma]]），但一直缺少可纵向追踪肿瘤进展的电生理生物标志物与配套器件。

## 核心方法
自建一套 <2g 模块化头帽 + 双 5 通道微丝电极的植入平台，植入小鼠初级运动皮层（M1），肿瘤在同一位点异种移植（人成人 GBM U-87 与儿童 DIPG 两种模型，NSG/nude 小鼠）。在自由活动小鼠中做数周慢性局部场电位（LFP）记录。分析：逐日线性 SVM 分类荷瘤/健康；elastic net 回归从功率谱预测生物发光成像（BLI）肿瘤负荷；对各频段功率的纵向轨迹拟合"峰型（二次）vs 饱和（平方根）"两个竞争模型，取高 γ 轨迹的上升速率预测生长率。平台架构预留无线电刺激能力（未在本文验证）。

## 关键数据
- gamma 频段功率随肿瘤生长升高，**GBM 与 DIPG 两模型都成立**（跨肿瘤泛化）；低频呈品系特异：GBM 降、DIPG 升。
- LFP 功率预测肿瘤负荷（BLI）**R²=0.61**；高/低负荷逐日分类 **73%（41/56）**。
- 高 γ 轨迹上升速率预测个体肿瘤生长率，**留一交叉验证 R²=0.88（p=0.0006）**——faster-growing 肿瘤高 γ 上升更快。
- 化疗（替莫唑胺 TMZ）组轨迹更接近健康组的单调饱和型（荷瘤组为先升后降峰型），提示轨迹形状携带治疗反应信号。
- 物种：小鼠、人肿瘤异种移植；概念验证（proof-of-concept）。gamma 与肿瘤为相关，非证明因果。

## 为什么是 milestone
首批把 cancer neuroscience 的机制积累，做成一个**专门的慢性植入监测器件**、并首次实现"从神经电轨迹纵向预测胶质瘤个体生长率"的概念验证。它给这条线补上此前空缺的"器件化连续监测（作者称 cancer neurotechnology）"分支——区别于机制类工作（[[venkatesh-2019-electrical-synaptic-integration-glioma]]、[[venkataramani-2019-glutamatergic-input-glioma]]）与人体一次性快照（[[derks-2018-oscillatory-activity-glioma-survival]] MEG、[[krishna-2023-glioblastoma-remodelling-human-circuits]] 术中）。Monje 作为该领域奠基人共同署名。局限：小鼠异种移植、监测≠治疗、闭环刺激仅为设想、人体可行性未证。
