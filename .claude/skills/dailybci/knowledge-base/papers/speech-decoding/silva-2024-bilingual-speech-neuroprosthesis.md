---
title: "A bilingual speech neuroprosthesis driven by cortical articulatory representations shared between languages"
authors: Silva, Liu, Metzger, Bhaya-Grossman, Dougherty et al.
year: 2024
venue: Nature Biomedical Engineering
url: https://doi.org/10.1038/s41551-024-01207-5
subfield: speech-decoding
tags: [bilingual, Spanish-English, shared-representation, articulatory, ECoG, Chang-lab]
---

## 解决了什么问题
之前所有 speech BCI 都只支持单一语言。全球数亿人是双语者，尤其在美国有大量西班牙语-英语双语人群。双语 speech BCI 面临一个根本问题：需要为每种语言分别训练解码器吗？还是大脑对不同语言使用共享的表征？

## 核心方法
在一名西班牙语-英语双语患者（PANCHO 研究的同一名患者）上测试。发现两种语言在 vSMC 上共享 articulatory representations——相同的发音动作（如 /p/、/t/ 等）在两种语言中激活相同的皮层区域。基于这个发现，用单一解码器同时处理两种语言的 attempted speech，解码器自动检测当前说的是哪种语言。

## 关键数据
- 单一解码器同时解码西班牙语和英语
- 英语词错误率：~30%，西班牙语类似
- 关键发现：跨语言的 articulatory representations 高度共享
- 证明不需要为每种语言单独训练

## 为什么是 milestone
首个双语 speech BCI。但更重要的是它揭示的神经科学原理：语音运动皮层编码的是"怎么动嘴"而非"说哪种语言"，不同语言在发音动作层面共享表征。这意味着 speech BCI 理论上可以扩展到任何语言而不需要语言特异的训练，对全球化临床部署有深远意义。
