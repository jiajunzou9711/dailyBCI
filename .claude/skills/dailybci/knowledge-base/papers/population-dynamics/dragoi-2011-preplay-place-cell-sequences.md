---
title: "Preplay of future place cell sequences by hippocampal cellular assemblies"
authors: Dragoi, Tonegawa
year: 2011
venue: Nature 469:397–401
url: https://doi.org/10.1038/nature09633
subfield: population-dynamics
tags: [hippocampus, CA1, place-cells, preplay, replay, sharp-wave-ripples, preconfigured-sequences, mouse, tetrode]
---

## 解决了什么问题
主流模型认为位置细胞的放电顺序在首次探索时才建立，之后在休息/慢波睡眠中 replay 用于巩固。本文检验：在动物从未到过某段轨道之前，CA1 的静息放电里是否已经出现日后该轨道上位置细胞的放电顺序。

## 核心方法
小鼠（4 只）CA1，6 根可独立推进的四电极（tetrode）。两种条件：(1) 熟悉直轨两端静息（Fam-Rest）之后，把一段新臂接上组成 L 形轨道（Contig-Run）；(2) de novo：从未上过任何直轨的小鼠先在高墙睡眠箱中休息/睡眠，再放到同一房间里看不见的新直轨上。静息期检测"至少 4 个细胞参与、间隔 <50 ms、前后各 ≥50 ms 静默"的放电事件，用秩相关与新臂位置野顺序模板比较，模板打乱 200 次作零分布（单事件 P<0.025）；另用贝叶斯位置重建解码静息期的虚拟轨迹。

## 关键数据
- Contig-Run 条件：至少 4 个新臂位置细胞参与的放电事件中，14.2% 显著匹配新臂顺序（preplay，P<10⁻³²，二项检验）；同期 16.2% 为熟悉轨道 replay。
- 纯 preplay 事件 54 个、纯 replay 171 个，比值约 3.1；79.9% 的事件两种模板都不显著。75 个 preplay 事件中 72% 与熟悉轨道模板无显著相关，排除"其实是熟悉轨道 replay"。
- 新臂上的位置细胞中，此前在熟悉轨道沉默的占 19%（两方向）/31%（至少一方向）；由沉默细胞组成的三元组完美匹配新臂模板的比例 0.67（16/24），随机期望 0.33。
- 贝叶斯解码：16.36% 的静息期轨迹落在尚未去过的新臂内。
- de novo 条件：睡眠箱中 16.1% 的放电事件与首次上新轨的位置细胞顺序显著相关，4 只小鼠各自均成立；preplay 与涟漪（ripple）同时出现。

## 为什么是 milestone
preplay 的命名与首个系统证据：海马在经验之前已有可被日后经验调用的时间序列，挑战了"顺序由经验首次写入"的模型，开启"预先配置的网络 vs 经验依赖可塑性"之争。此后 preplay 的计算意义受到质疑（Grosmark 2016 引 Silva 2015 Nat Neurosci），Maboudi 2024 也报告 PRE 期离线调谐整体不对齐日后位置野；作者本人将更早研究未检出 preplay 归因于成对相关法不够敏感或样本量小。引用时注意：物种是**小鼠**，样本 4 只；preplay 只占全部放电事件的少数（约 14–16%）。Dragoi 2020 Curr Opin Neurobiol 64:111 综述将本文列为 preplay 一线的源头文献。
