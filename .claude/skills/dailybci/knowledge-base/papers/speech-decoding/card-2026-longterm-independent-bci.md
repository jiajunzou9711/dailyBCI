---
title: "Long-term independent use of an intracortical brain–computer interface for speech and cursor control"
authors: Card, ..., Brandman, Stavisky et al.
year: 2026
venue: Nature Medicine (preprint bioRxiv 2025)
url: https://doi.org/10.1038/s41591-026-04414-6  # preprint: https://doi.org/10.1101/2025.06.26.661591
subfield: speech-decoding
tags: [speech-BCI, intracortical, Utah-array, ALS, home-use, long-term-stability, transformer-decoder, silent-speech, multimodal, cursor-control, BrainGate2]
---

## 解决了什么问题
高性能皮层内语音 BCI(Willett 2023、Card 2024)此前都只在**有研究员监督的实验室**场景里 demo;离临床真正可用还差两道坎:**患者能否在家、研究员不在场、独立长期使用**,以及**性能能否跨越数月乃至数年保持稳定**。本研究直接回答这两点。

## 核心方法
与 Card 2024 同一参与者(代号 T15,45 岁,ALS 重度构音障碍)。**电极:侵入式—皮层内穿刺式**,4 块 64 通道硅基 Utah 阵列(共 256 电极,1.5mm 针长、氧化铱镀层,Blackrock Neurotech),2023 年夏植入左侧腹侧中央前回(**语音运动皮层**),经皮有线连接(BrainGate2,NCT00912041)。一套**多模态**系统由他自己在家操作:语音解码(解"尝试发音"的运动指令→每 80ms 出 39 音素[+静音+CTC blank=41 类]→语言模型从 12.5 万词拼词),光标解码(同一语音皮层阵列、用手部运动想象),均在后台**持续微调(continuous finetuning)**以追踪神经漂移。语音解码器从 RNN 升级为 transformer(约第 600 天起)。护理者只负责戴上/取下设备。

## 关键数据
- **使用规模**:19 个月 / 678 天;第 281 天起进入独立模式;累计 **3,801 小时**、**183,060 句**;近每日自用;**维持全职工作**。
- **日常自评**:完全正确 53.3% / 自行修正 12.9% / 大致正确 26.1% / 错误 7.7%;越用越准(第 412 天起完全正确升至 58.9%);最长正确解码连续话语 215 词。
- **Copy Task 客观基准**:出声 >99% 准确率 @ 30.6 WPM;默念 96.5% @ 49.7 WPM;transformer 解码器达 **99.2% 词准确率**(125k 词汇)。
- **自创"默念"策略**:从出声改为只做发音动作不发声,更省力,速度 ~30→50+ WPM(系统靠持续微调主动适应)。
- **光标**:第 358 天加入,约 121 分钟/天;第 654 天换 RNN 后"取得控制"时间从 2.0 降到 **0.8 分钟**,日校准从 16.9 降到 9.2 分钟;Grid Task 最高 ~3 bits/s。
- **信号稳定**:>90% 电极在 19 个月后仍记录到 ≥2Hz 放电;语音相关调制的余弦相似度即便间隔 >18 个月仍 >0.6(d6v 阵列语音调制弱,为例外)。

## 为什么是 milestone
首次证明皮层内语音(+光标)BCI 可以作为**研究员不在场、患者自主操作的日常生活工具,稳定运行近两年**,并**量化了长期信号稳定性**。它把高性能语音 BCI 从"实验室 demo"推进到"临床可用性"这一关:相较 [[card-2024]](同一患者,实验室 8 个月 97.5%)、[[willett-2023]](62 WPM、125k 词汇,实验室)、[[simeral-2021]](家用无线但为运动光标)、[[vansteensel-2016]](家用但慢速点选),本工作是已知首个在"语音 + 电脑控制同时、家庭自主、长期"四者俱全的演示。仍属单患者、有线经皮、单一植入位点,推广性待验证。
