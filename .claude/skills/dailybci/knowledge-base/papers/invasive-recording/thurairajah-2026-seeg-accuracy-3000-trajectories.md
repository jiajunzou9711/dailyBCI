---
title: "Stereoelectroencephalography accuracy in a series of over 3000 trajectories"
authors: Thurairajah A, Gilmore G, Persad ARL, Youshani AS, Taha A, Abbass M, Santyr B, Al Orabi K, Pellegrino G, Burneo JG, Suller-Marti A, Western Epilepsy Research Group, Parrent AG, MacDougall K, Steven DA, Lau JC
year: 2026
venue: medRxiv
url: https://doi.org/10.64898/2026.07.14.26358071
subfield: invasive-recording
tags: [sEEG, implantation-accuracy, robot-vs-frame, implantation-angle, radial-error, retrospective-cohort, human, largest-series]
---

## 解决了什么问题

sEEG 植入精度此前的文献分两类,都不够:要么只报一个中心的总体误差数字(如 [[cardinale-2013-seeg-500-procedures-accuracy]]、[[gonzalez-martinez-2016-robot-assisted-seeg]]),要么只争"机器人 vs 框架"(如 [[vakharia-2021-robot-vs-manual-rct]]、[[abbas-2026-robot-vs-frame-meta-analysis]])。而且报告方式混乱——不同研究的"误差"不是同一个量(欧氏/径向/深度/角度混用),导致跨研究比较失效([[cardinale-2016-seeg-implantation-review]] 早已指出)。本文在迄今最大的单一系列上,同时报告所有常用误差指标,并逐条轨迹拆解"什么在影响精度"。

## 核心方法

**电极模态:侵入式深部电极(sEEG)**,单中心(London Health Sciences Centre / Western University,Jonathan Lau 组)回顾性队列。2013–2025 共 12 年:2013–2017 用框架式(Leksell G + Framelink),2017 年 4 月起常规机器人辅助(Neuromate + Neuroinspire);两组均用 Leksell 框架做头固定与影像配准,差别只在"瞄准"这一步。逐条轨迹计算欧氏/径向/深度/角度误差(入点与靶点均算)。进针角度定义为**骨锚与颅骨法向量的夹角**(0°=垂直,越大越斜),用 3D Slicer 半自动测。做相关分析(Spearman)、多变量线性回归、logistic 回归找角度阈值、并按脑叶/轨迹分组。

## 关键数据

- 规模:340 人接受手术,可算精度者 **260 人 / 3176 条轨迹**(机器人 2858 电极/229 人,框架 318 电极/31 人)。作者自陈迄今最大系列
- **机器人 vs 框架(论文第一结论):机器人更快也更准**——靶点欧氏误差中位数 **2.19mm**(IQR 1.54–2.98)vs **2.76mm**(1.79–3.76),入点 1.38 vs 2.21mm,p<.001;麻醉与手术时间也更短(p<.001)
- **进针角度**与靶点径向误差相关最强(可规划因素中):**ρ=0.28**,p<.001;角度每变 30° 径向误差增约 1mm;**22.25°** 是超 2mm 的 logistic cutpoint(但该模型 AUC 仅 0.67±0.02)
- **同颞叶内 2.8 倍差**:海马后部 1.18mm @ 角度 10.40°(最正)↔ 颞极 3.28mm @ 33.92°(最斜)
- **组织状态**:硬化海马(MTS,n=88)径向误差 1.58mm vs 正常(n=54)1.12mm,径向偏移多 0.4mm(p<.05,欧氏误差无差异);作者措辞 "presumably due to tissue properties"
- **多变量模型 adjusted R²=0.150**——角度/颅骨/头皮/轨迹长度/BMI 等已测因素**只解释约 15% 的误差变异**
- 全队列中位角度 20.30°,斜行(>30°)仅 446 条(18.6%)
- 安全:23 例颅内出血,仅 2 例(0.6%)有症状,无人返手术室;机器人前有 1 例致命出血(手术中止)

## 为什么是 milestone

它是 sEEG 精度子簇里**当代最大规模的实证盘点**,把这条线从"设备之争"推进到"逐轨迹因素分解",并给出两个有分量的落点:

1. **精度更多是"轨迹几何"的属性**:同一批病人、同一台机器人、同一个颞叶内,误差随进针角度差 2.8 倍——设备不是唯一变量。这与 [[vakharia-2021-robot-vs-manual-rct]](RCT:手动反而略准)和 [[abbas-2026-robot-vs-frame-meta-analysis]](meta:精度无差)汇成一致图景:**设备之争被年代混杂放大,几何才是被长期忽略的主因**。
2. **15% 天花板(最诚实的数字)**:即便把所有已测因素加起来,也只解释 15% 的误差方差。**毫米级不确定性在很大程度上是这项技术的固有属性,不是换台更好的机器就能消掉的。**

**重要边界(引用时必带)**:① 本文自身的"机器人更准"是**单中心回顾性、框架组为历史对照(2013–17)**,存在年代流程混杂——作者在 Limitations 明写 "introducing potential confounds";② 论文只声称各因素"相关(correlated)",**未验证力学机制**("斜进针打滑"是领域常识,非本文结论);③ 角度→误差虽显著但相关不强(ρ=0.28,AUC 0.67),"显著"来自 3176 的大样本,不等于"强"。**本篇不做神经解码**,是癫痫外科的精度方法学研究,经"植入式电极定位"这条母题与 BCI 主线相接(见待做专题 ⑥:精度路线 vs 容差路线 vs 回避路线)。
