---
title: "Natural speech reveals the semantic maps that tile human cerebral cortex"
authors: Huth AG, de Heer WA, Griffiths TL, Theunissen FE, Gallant JL
year: 2016
venue: Nature
url: https://doi.org/10.1038/nature17637
subfield: semantic-decoding
tags: [fMRI, encoding-model, naturalistic-stimuli, semantic-map, voxel-wise, human]
---

## 解决了什么问题

此前的语义研究几乎全用受控的孤立刺激（单个词、单张图），得到的是"某某范畴激活某某脑区"这种分块结论。真实语言理解发生在连续自然语流里，涉及成千上万个词。本文用自然叙事语音 + 体素级编码模型，画出语义在整个皮层上的连续分布图。

## 核心方法

人类 fMRI。被试听数小时的自然叙事故事（naturalistic narrative speech）。给每个词赋一个基于语料库共现统计的语义特征向量，再为**每个体素**单独拟合一个编码模型（voxel-wise encoding model），预测该体素对语义特征的调谐。把全皮层体素的调谐参数做降维，得到连续的语义空间，并投到皮层表面。

## 关键数据

- *Nature* 532:453–458（2016 年 4 月 28 日），DOI 10.1038/nature17637，PMID 27121839
- 结果形态：语义选择性**平铺（tile）整个皮层**的大片区域，跨双侧半球广泛分布，而非局限于经典语言区
- 语义图在被试间高度一致

## 为什么是 milestone

它把语义表征从"哪个区管哪类概念"改写成**连续的皮层语义地图**，并确立了自然刺激 + 体素级编码模型这套方法论——[[tang-2023-semantic-language-reconstruction]]（同为 Huth 组，首次非侵入连续语言语义重建）直接建在它上面。

对侵入式语义解码，它带来一个不太受欢迎的推论：**语义信息在皮层上分布极广**。sEEG/ECoG 只能采样到少数几个位置，天然只看得见这张大地图的稀疏片段——这是颅内语义解码准确率长期远低于全脑 fMRI 的结构性原因之一（[[rupp-2017-ecog-semantic-attributes]] 能做到"与全脑 fMRI 相当"因而值得注意）。它也提示 [[patterson-2007-semantic-knowledge-representation]] 的 ATL 枢纽与这张广布地图并不矛盾：枢纽负责跨模态绑定，辐条铺满皮层。
