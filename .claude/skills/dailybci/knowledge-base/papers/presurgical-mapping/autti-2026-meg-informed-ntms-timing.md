---
title: "MEG-informed navigated TMS for individualized speech cortical mapping"
authors: Autti S, Korkealaakso S, Gogulski J, Engelhardt M, Vaalto S, Renvall H, Liljeström M, Lioumis P
year: 2026
venue: bioRxiv 2026.07.10.737657
url: https://doi.org/10.64898/2026.07.10.737657
subfield: presurgical-mapping
tags: [navigated-TMS, MEG, speech-mapping, picture-to-TMS-interval, temporal-individualization, language]
---

## 解决了什么问题
nrTMS 语言作图一直只个体化刺激的**空间**(靠导航对准每个人的解剖),而脉冲发放的**时机**(PTI, picture-to-TMS interval)对所有人用固定值。这留下 nrTMS 的老痛点:高灵敏(~90%)/低特异(~24%,Picht 2013)。本研究检验能否用每个人的 MEG 语音激活时序,为每人**个体化 TMS 的发放时机**,补上一直缺席的时间维。

## 核心方法
13 名健康成人,先做 MEG 看图命名(被动记录,毫秒级)得到各皮层区激活的时间进程与峰值时刻;再做 nrTMS 语言作图,在多个 PTI(0–500 ms,含按 MEG 定制的值)上发放 5 脉冲串(5/7 Hz)扰动命名,逐区找出"最能致错的 PTI"(best PTI=错误率最高的延时)。把每人的 best PTI 与其 MEG 峰值时刻做相关。两次测量相互独立(MEG 无 TMS、TMS 无同步 MEG),命名错误经录像人工判读。

## 关键数据
- Combined ROI:best PTI 与 MEG 峰值时刻显著正相关 **R=0.713, p=0.006**(95%CI [0.26,0.88]);Frontal ROI R=0.673, p=0.012。
- 方向:**best PTI 系统性地早于 MEG 峰值**,整组平均差 132±77 ms(CROI:MEG 峰值 339±83 ms、best PTI 207±110 ms,t(24)=3.33,p=0.003)。注:预印本摘要/引言把该方向误写为"MEG 峰值早于 best PTI",与其自身 Table 2/图/讨论矛盾,以数据为准=best PTI 在前。
- 区域解离:感觉运动(R=0.158)、顶叶(R=0.425)、颞叶(R=0.049)均不显著;仅额叶/语言产出区成立。
- 17 个 PTI×区域组合(跨 9 名被试)错误率较各自均值显著升高。

## 为什么是 milestone
presurgical-mapping 语言线的扩展节点:把 nrTMS 的个体化从"只调空间"推进到"空间+时间",并让一个被动记录模态(MEG)去**配置**一个主动扰动模态(TMS)的采集参数,而不只是像 [[tarapore-2013-ntms-megi-language]] 那样并联提供第二张图。定位:概念验证(健康人、N=13、**未对照 DCS 金标准**),"改善特异度"目前是合理推断而非实证,尚待在术前患者+术后 DCS 对照中验证。承接 [[picht-2013-ntms-vs-dcs-language]] 的能力边界与 [[papanicolaou-2004-meg-wada-language]] 的 MEG 术前语言线。
