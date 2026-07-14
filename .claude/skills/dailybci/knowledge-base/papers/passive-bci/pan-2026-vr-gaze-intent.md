---
title: "Seamless interaction in VR: decoding user intent with eye gaze and passive brain–computer interfaces"
authors: Pan Y, Rabe L, Zander TO, Klug M
year: 2026
venue: bioRxiv 2026.07.06.736575
url: https://doi.org/10.64898/2026.07.06.736575
subfield: passive-bci
tags: [passive-BCI, neuroadaptive, VR, eye-gaze, intent-decoding, ERP, valence, affordance, approach-avoidance, online-closed-loop, EEG]
---

## 解决了什么问题
VR 交互几乎全靠显式动作(手柄、手势),这是"无缝沉浸"的瓶颈;想用注视做免手交互又撞上 Midas touch 问题(看即命令,分不清打量与选择)。被动 BCI/neuroadaptive 被提出来当解法,但此前这类闭环意图解码多停在受控或离线任务。核心问题:在动态 VR 游戏里,能不能实时(在线闭环)从脑电解出"交互意图"。

## 核心方法
非侵入 64 通道头皮 EEG + VR 头显内置眼动,23 名健康被试玩护盾防御游戏。眼动负责"哪个物品、何时"(注视触发物品出现、定 epoch 时间锚点、保持注视控伪迹),脑电负责在物品出现后 1 秒决策期(item-onset 锁定的 ERP,不许动手)解码意图。把"交互意图"拆成两个二分类:affordance(actionable vs 非 actionable)与 approach–avoidance(take vs discard)。校准环节用手柄按键给真值训练分类器;在线环节由预训练分类器实时驱动游戏动作,系统做错时被试才按键纠正。

## 关键数据
- affordance(值不值得交互):四类物品对比碎石,中位 77.76%–83.50%,稳健。
- approach–avoidance(拿/丢):价值两极分明的 coins vs bombs 达 80.84%±1.73%;价值随情境模糊的"非金币的拿 vs 非炸弹的丢"跌到 59.03%,接近随机。
- 在线闭环迁移:approach–avoidance 离线 66.28% → 在线 69.64%,均高于随机。
- UX(探索性问卷):比手柄显著更好玩,但掌控感/易用性/满意度更低;想象一个准确率≈99% 的"近乎完美"BCI 则在多维反超手柄。
- 人类 23 名健康被试,非侵入头皮 EEG。

## 为什么是 milestone
据作者所知,首个在动态 VR 游戏中实时(闭环)解码交互意图的工作,把 Zander 2016 的 neuroadaptive 闭环从受控 2D 光标推进到生态复杂的 VR 游戏 + 眼动。更关键的是它诚实地划出能力边界:可解码的信号本质是价值评价(带符号的效价),意图只在绑定强而两极的价值时才连带可解,价值模糊即塌回随机——affordance(相关性/显著性)稳、approach–avoidance(效价)脆。为 passive-BCI 意图解码的现实边界提供了定量参照。参见 [[zander-2016-neuroadaptive-cursor]]、[[zander-2011-passive-bci]]。
