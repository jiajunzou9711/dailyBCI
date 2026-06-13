---
title: "Fully integrated silicon probes for high-density recording of neural activity"
authors: Jun, Steinmetz, Siegle, Denman, Bauza, Barbarits, Lee, Anastassiou, Andrei, Aydin, Barbic, Blanche, Bonin, Cober, et al.
year: 2017
venue: Nature
url: https://doi.org/10.1038/nature24636
subfield: electrode-hardware
tags: [Neuropixels, CMOS, high-density, silicon-probe, large-scale-recording, open-source]
---

## 解决了什么问题
神经科学需要同时记录数百到数千个神经元来理解回路动力学，但传统电极（包括 Utah 阵列）受限于通道密度和覆盖深度。需要一种可沿深度方向高密度覆盖多个脑区的记录工具。

## 核心方法
利用 CMOS 半导体工艺在单根硅探针上集成 960 个记录位点和 384 通道同时读出电路。探针宽 70μm、厚 20μm、长 10mm，沿全长密集排列电极位点（间距 25μm）。片上集成模拟前端、多路复用器和 ADC，通过一根细线缆输出数字信号。

## 关键数据
- 单根探针 960 个电极位点，384 通道同时记录
- 电极间距 25μm（中心距）
- 探针可覆盖 10mm 深度的多个脑区
- CMOS 工艺支持批量制造，成本可控
- 开源设计，学术社区免费分发

## 为什么是 milestone
Neuropixels 彻底改变了大规模神经记录的可及性。通过 CMOS 工艺将数百通道集成在单根探针上，一个实验室就能记录以前需要复杂多探针系统才能获得的数据量。开放分发模式使其迅速成为系统神经科学的标准工具。虽然目前主要用于研究（非慢性植入），但其高密度设计理念直接影响了下一代 BCI 电极的发展方向。
