---
title: "Dual-mode dynamics in hippocampal populations enable rapid and precise spatial coding"
authors: Ren, Feng, Chen, Lin, Xu
year: 2026
venue: Current Biology 36:1–10
url: https://doi.org/10.1016/j.cub.2026.09.052
subfield: population-dynamics
tags: [hippocampus, CA1, place-cells, place-field-formation, backbone-cells, offline-dynamics, sharp-wave-ripples, BLT, preplay, rat, tetrode]
---

## 解决了什么问题
大鼠进入陌生环境，海马 CA1 的空间地图几分钟内就成形，经典 Hebb 可塑性难以解释这一速度。已有观察表明位置野有的首圈即现、有的逐圈出现，但这两类是否构成功能上可分离的群体、如何协同，以及离线（休息）活动能否在单细胞层面提前对上日后的位置野，此前没有直接证据。

## 核心方法
4 只大鼠，背侧 CA1 植入 16 根四电极（tetrode，64 通道），记录单神经元动作电位。陌生 U 形轨道（266 cm）往返取水，9 段 × 30 min 笼中休息与跑动交替（H0→RUN1→…→RUN4→H4），H0 在首次上轨道之前。位置野分 IE（首圈出现并保持）与 GE（之后出现并保持）；细胞分 B（含 IE 且跨圈稳定性高于中位数）、H（含 IE、稳定性低于中位数）、E（只有 GE）。用 Maboudi 2024 的贝叶斯学习调谐（BLT）从涟漪相关群体放电事件推断每个细胞的离线调谐曲线，与其日后位置野求相关（LT-PF fidelity）。

## 关键数据
- 393 个稳定位置野：IE 38%（151）、GE 62%（242）；GE 起始放电强度约为 IE 一半（149 vs 309 Hz·cm），约 30 圈后持平。
- 169 个位置细胞：B 45、H 44、E 80；往返两方向的类型一致性显著高于随机。
- B 只占 27%，但打乱 B 的放电使位置解码误差增加最多（B vs E 仅 RUN4 显著）；发放率匹配后 B 与 E 差异消失。
- 休息期 E 细胞参与群体放电事件的概率与占比逐段上升；H1 replay 以 B 为主，H4 时 E 的贡献上升。
- H0（首次上轨道前）：B 细胞 LT-PF fidelity 中位数 0.23（p<0.01），H −0.04、E −0.01；H1 时 B 0.73、H 0.33、E 0.39。
- E 细胞：对齐到 GE 位置野出现时刻，离线 fidelity 从约 −1 min 起显著上升并保持；场内放电率出现前无提前上升；上轨道 180 s 后才出现的位置野仍有提前上升。
- 作者自列局限：骨干来源未定；离线因果未经 SWR 干扰检验；每鼠只一个新环境；无 NMDAR 阻断；奖励与空间学习未分离。

## 为什么是 milestone
把"网络预先组织"（preplay 一线）落到单细胞层面：用 BLT 显示部分细胞在首次经历之前的静息放电已与日后的位置野一致，并把快速成图拆成"预先组织的骨干 + 经验依赖细胞逐步并入"两部分。与 Grosmark & Buzsáki 2016 的 rigid/plastic 区分相比，本文是首次暴露、无预训练、逐圈追踪。证据为相关性，n=4。
