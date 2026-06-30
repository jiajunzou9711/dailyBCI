---
title: "Noninvasive Deep Brain Stimulation via Temporally Interfering Electric Fields"
authors: Grossman N, Bono D, Dedic N, Kodandaramaiah SB, Rudenko A, Suk HJ, Cassara AM, Neufeld E, Kuster N, Tsai LH, Pascual-Leone A, Boyden ES
year: 2017
venue: Cell
url: https://doi.org/10.1016/j.cell.2017.05.024
subfield: neuromodulation
tags: [temporal-interference, deep-stimulation, spatial-selectivity, focal, noninvasive, current-steering]
---

## 解决了什么问题
表面/远场电刺激的铁律是"最近的神经元最先被激活"——想刺激深部就不可避免地先激活覆盖在上面的浅层组织。能不能用表面电极**选择性激活深部、放过浅层**？

## 核心方法
**时间干涉(temporal interference, TI)**：经两对表面电极各施加一个略有差异的高频电场（如 2 kHz 与 2.01 kHz）。神经元对单独的高频场跟不动（低通），但两场在空间某处叠加产生**低频包络(Δf)**——只有包络足够大的深部交汇区才被有效驱动。移动两路电流配比即可在不移动电极的情况下 steering 交汇焦点。

## 关键数据
- 小鼠在体：TI 可在海马等深部结构诱发神经激活，而表面运动皮层相对不被驱动；移动电流比例使激活焦点在皮层下平移（小鼠）。
- 提供"无创、可 steering 的深部聚焦"概念验证。

## 为什么是 milestone
"用电场时空结构、而非移动电极来把激活推向深部并抑制浅层"的概念地标，是本期 ACM（硬膜外表面电极焦点激活深部脊髓、表面被高频抑制）最直接的**概念近亲**——两者都靠多路/高频电场把焦点从电极近旁移到远处深部。与 [[struijk-holsheimer-1996-transverse-tripole]]（横向 steering）、[[rowald-2022-spatiotemporal-epidural]]（多触点电流编排）并列为 current-steering 母题下的不同实现。建立在 [[rattay-1986-activating-function]] 的场—兴奋耦合判据上。物种为小鼠，向人类的转化仍在验证中。
