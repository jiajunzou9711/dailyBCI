---
title: "A Minimally Invasive Hybrid Brain-Computer Interface: A Distributed, Scalable and Evolvable Architecture for Whole Brain Access"
authors: Li Z, Liu N, Wan L, Liu M, Wu C
year: 2026
venue: bioRxiv
url: https://doi.org/10.64898/2026.07.14.738604
subfield: electrode-hardware
tags: [minimally-invasive, skull-microhole, epidural, distributed-electrodes, temporal-interference, Pt-Ir, ultrasonic-craniotomy, hybrid-BCI, rat, simulation, China]
---

## 解决了什么问题
脑机接口在信号质量与侵入程度间长期两难:非侵入头皮 EEG 被颅骨强烈衰减+空间抹平(颅骨电导率约 20 mS/m vs 头皮约 410 mS/m),经颅电刺激因分流仅约 10% 电流入脑;侵入电极信号质量高但需开颅、难覆盖多脑区、器件难升级,且"技术能植入≠病人接受"(论文援引:DBS 仅 1.6–4.5% 合格、合格者 60–70% 拒绝;人工耳蜗接受率约 10%)。头皮 EEG 与颅内侵入之间的"中间档"长期空缺。

## 核心方法
提出"颅骨微孔电极"混合(hybrid)架构,把颅骨本身用作一排分布式低阻端口。四要素:①超声振动自限微孔打孔(S2MHC:300–800 μm、不取材料塑性成孔、力<500 mN、冷却后孔壁<43°C、2 周愈合;终止检测延迟 34.0±16.4 ms、过冲 16.2±17.2 μm;工具对硬脆骨有效、对软硬膜近乎不切削,持续接触 30 s 硬膜无损伤——被动选择性+主动刹停双重护膜);②单点 Pt/Ir 微电极(500 μm 柱 + 0.7/1.5/4.0 mm 限深凸缘)皮下植入孔内,远端贴硬膜外表面(不穿硬膜、不进脑),近端留皮下;③体外双向头戴经欧姆传导(隔薄头皮、导电膏直接导通,非电磁感应)耦合,做记录/刺激/通道选择;④AI 规划与控制。信号层级=硬膜外场电位;有源电子全在体外,可升级、可分布式按需增点。

## 关键数据
- **记录**(SD 大鼠 n=12,急性麻醉,经体表电极耦合植入件读取):同一体表电极 ± 底下植入件为唯一差别。静息态功率 delta–gamma 各频段一并抬高约 2.6–8.9 倍(各频段同步上抬,与颅骨为频率无关衰减器一致);体感诱发电位(SEP)信噪比从头皮 EEG 的 12–21 提升到 33–47;稳态视觉诱发电位(SSVEP)从头皮上几乎平直到出现清晰频率峰。
- **刺激**(仅仿真,简化人头球模型,无动物实验):微孔低阻通路提高进脑场强与聚焦度;配合时间干涉(TI)聚焦点可由电极位置或两路电流比导向深部靶点。
- **安全**:兔硬膜持续接触 30 s SEM 无可见损伤;鸡蛋不刺破内膜、新西兰兔在体皮层不着色确证。

## 为什么是 milestone
在电极模态谱系里插入"头皮 EEG 与硬膜外之间"的一格:拿到接近硬膜外(epidural)的信号通路,却不开骨瓣、不破硬膜、有源电子留体外、可分布式扩展。与硬膜外 ECoG([[neo-2024-epidural-minimally-invasive-bci]] NEO,整片阵列+小骨瓣)对照,本质差别是"单点 vs 整片、微孔 vs 骨瓣";与血管内 [[oxley-2016-stentrode-endovascular-array]] 并列为"少开颅"的不同路线;刺激侧接 [[grossman-2017-temporal-interference]] 的 TI,用颅骨端口补 TI"电流进不去、可穿戴电极难复位"两处短板。局限:记录为大鼠急性且经体表耦合、刺激纯仿真、无无线/慢性/闭环/人体系统。定位=范式提出 + 早期动物记录 + 刺激仿真,非临床结果(中山大学深圳校区 × 深圳 BrainXess,通讯 Zhe Li,bioRxiv)。
