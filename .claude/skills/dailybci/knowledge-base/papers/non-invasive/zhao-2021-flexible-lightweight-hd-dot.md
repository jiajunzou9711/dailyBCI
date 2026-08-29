---
title: "Design and validation of a mechanically flexible and ultra-lightweight high-density diffuse optical tomography system for functional neuroimaging of newborns"
authors: Zhao H, Frijia EM, Vidal Rosas E, Collins-Jones L, Smith G, Nixon-Hill R, Powell S, Everdell NL, Cooper RJ
year: 2021
venue: Neurophotonics 8:015011
url: https://doi.org/10.1117/1.NPh.8.1.015011
subfield: non-invasive
tags: [可穿戴, 模块化, 柔性电路, 新生儿, 硬件]
---

## 解决了什么问题

光纤式 HD-DOT 系统([[eggebrecht-2014-whole-head-hd-dot]] 一类)体积与重量都大，很难在新生儿身上做**反复的**或**长时程**的床旁成像。要把通道数堆上去，机械结构本身就成了瓶颈——尤其在曲率大、承重能力极低的婴儿头上。

## 核心方法

用 **10 层刚柔结合印制电路板**做 DOT 模块的基底：既压缩了模块体积与厚度，又保留了贴合婴儿头皮曲面所需的柔性。实现两种模块排布(双六边形、三六边形)，靠板间连接器可组合出大量阵列构型。验证手段是自制的**解剖精确动态体模**——环氧树脂 + 热致变色染料 + 由 MRI 导出的 3D 打印模具，可电控切换，用来定量测成像性能。

## 关键数据

- 基底工艺：10 层刚柔结合 PCB；模块排布两种(双六边形/三六边形)，可自由组合。
- 验证方式：可电切换的解剖精确动态体模(非活体)。

## 为什么是 milestone

这是**补充性条目(硬件/工程论文)**，不是科学发现。它的复用价值在于指认了可穿戴 HD-DOT 的真实瓶颈是**机械与工效**而非光学：通道密度上不去，往往卡在"这套东西能不能戴在头上、能不能贴合曲面"。评估任何"可穿戴高密度"系统时，先看它的模块基底与贴合方案，再看它报的通道数。
