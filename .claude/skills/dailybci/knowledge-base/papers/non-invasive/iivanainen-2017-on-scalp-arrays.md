---
title: "Measuring MEG closer to the brain: performance of on-scalp sensor arrays"
authors: Iivanainen J, Stenroos M, Parkkonen L
year: 2017
venue: NeuroImage 147:542-553
url: https://doi.org/10.1016/j.neuroimage.2016.12.048
subfield: non-invasive
tags: [OPM, on-scalp, 空间分辨率, 信息容量, 仿真]
---

## 解决了什么问题

OPM 相对 SQUID 的传感器噪声本底更差(约 7–10 vs 约 2–5 fT/√Hz)。那么把传感器从头皮外约 2 cm 挪到贴着头皮，靠"离源更近"换来的增益，究竟够不够抵消这个劣势？这个取舍此前没有被定量算清。

## 核心方法

仿真研究。构造贴头皮的 OPM 阵列(**nOPM**：只测垂直头皮的法向分量；**tOPM**：测切向分量)与常规 SQUID 磁强计阵列，在同一批皮层源上比较信号功率、源场型之间的相关性、体电流影响、信息容量与点扩散函数。

## 关键数据

- **信号功率**：相对 SQUID 磁强计，nOPM 阵列高 **7.5 倍**，tOPM 阵列高 **5.3 倍**。
- **源场型相关性**(越低越易分辨不同源)：nOPM、tOPM 分别比 SQUID 低 **2.8** 与 **3.6** 倍。
- **体电流对原电流信号的削减**：nOPM 约 **10%**，tOPM 约 **72%**，SQUID 磁强计约 **15%**。
- **信息容量**：两种 OPM 阵列均明显高于 SQUID 阵列。
- **点扩散函数**：SQUID 阵列比 nOPM、tOPM 分别弥散 **2.4** 与 **2.5** 倍。
- 但**单偶极子定位精度**在三类阵列之间相当。

## 为什么是 milestone

给"贴近头皮"这条路线提供了定量依据，并且把收益拆开讲清楚了：主要收益在**信号功率与空间分辨率(分辨多个同时活动源的能力)**，而**单源定位精度**上三者相当。这个区分在评估后续 OPM 系统时很有用——宣称"定位更准"和宣称"能分开更多源"是两回事。另外 nOPM 与 tOPM 在体电流敏感性上的巨大差异(10% vs 72%)，解释了后续系统为何普遍选择测**垂直头皮方向**的分量。
