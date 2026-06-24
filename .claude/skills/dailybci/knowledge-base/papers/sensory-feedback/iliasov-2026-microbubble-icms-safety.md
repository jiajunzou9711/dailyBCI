---
title: "Electrolytic-microbubble dynamics delineate safety thresholds during intracortical microstimulation with flexible neural interfaces"
authors: Iliasov A, Ma H, Li F, Chen Z, Xu M, Yu C, Li R, Wu J, He F
year: 2026
venue: bioRxiv 2026.06.17.733032 (preprint, posted 2026-06-23)
url: https://doi.org/10.64898/2026.06.17.733032
subfield: sensory-feedback
tags: [stimulation-safety, ICMS, ultraflexible-electrode, two-photon, blood-brain-barrier, microbubble, in-vivo-imaging, awake-mouse]
---

## 解决了什么问题
ICMS 用超柔性微电极做感觉恢复/双向 BCI 时,"多大电流才安全"一直靠 [[shannon-1992-safe-levels-model]] 这类**宏电极 + 事后切片**导出的电荷判据。既往血脑屏障/损伤研究又多停在体外/微流控或电穿孔类(千伏级)协议。没有谁在清醒皮层、ICMS 微安级电流下,**实时看清微血管层面先发生什么、又是什么机制**——正是 [[cogan-2016-tissue-damage-thresholds]] 呼吁为微电极重画安全线所缺的证据。

## 核心方法
清醒小鼠(C57BL/6J),超柔性铂微电极,活体双光子成像皮层血管 + 电生理 + 2 MDa FITC-葡聚糖示踪,扫电荷平衡电流 20/40/60/80 µA,同步看电极旁气泡与血管渗漏;配 COMSOL 有限元模型(气泡致电场再分布 + 电压依赖的血管壁通透性)。

## 关键数据
- ICMS 在电极上**电解析出气泡**,气泡面积随电流**约二次方**增长(仿真∥实验吻合)。
- **两区阈值**:20–40 µA 渗漏小、局部、可逆(Regime I);**≥60 µA** 急转——血脑屏障破裂、大范围外渗、红细胞外渗(60–80 µA)、电极同步退化(Regime II)。
- 渗漏在气泡**塌缩瞬间**起,非气泡最大时;模型"去掉气泡"则高电流处无急升,指认气泡为元凶("electrical lens"局部聚场)。
- 安全窗**组织 × 电极双重限定**:铂耐受高电荷,金/PEDOT:PSS 在"对组织安全"的 20–40 µA 即退化。

## 为什么是 milestone
这条「刺激安全」线此前全是判据/材料/事后组织学([[mccreery-1990-charge-density-charge-per-phase]] → [[shannon-1992-safe-levels-model]] → [[mccreery-2010-chronic-icms-neuronal-loss]] → [[cogan-2016-tissue-damage-thresholds]])。本篇是子簇里**第一篇"在体实时血管成像看 ICMS 损伤发生"**的工作:把电解微气泡从"过度刺激的被动标志"重新定位为**主动致损机制**,并给出柔性电极 ICMS 有机制依据的安全电流窗。提示"场参数(电荷/电场幅值)单独无法刻画在体安全边界"。局限:小鼠皮层、急性,60 µA 阈值未必外推到灵长类/人、更大电极或慢性使用。
