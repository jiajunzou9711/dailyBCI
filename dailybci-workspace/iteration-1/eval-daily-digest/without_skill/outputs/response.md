# DailyBCI - 2026年6月6日

---

## Today's Pick: 中国批准全球首个商用侵入式脑机接口 NEO

**Source:** MIT Technology Review, June 1, 2026
**Link:** https://www.technologyreview.com/2026/06/01/1138133/china-world-first-brain-chip/

---

### What Happened

2026年3月，中国国家药监局（NMPA）正式批准了由上海博睿康科技（Neuracle Technology）与清华大学联合开发的 NEO 脑机接口设备，用于脊髓损伤导致的四肢瘫痪患者。这是全球第一个获得国家监管机构批准、超越临床试验阶段进入商用的侵入式 BCI 产品。

---

### The Core Insight: 硬膜外 vs 皮层内 -- 两条路线的关键权衡

这条新闻真正值得深挖的不是"中国 vs Neuralink 谁先批准"的竞赛叙事，而是 NEO 的技术路线选择揭示了 BCI 领域一个根本性的工程权衡：**你愿意牺牲多少信号质量来换取安全性和审批速度？**

NEO 采用**硬膜外（epidural）**设计：8个传感器放置在硬脑膜表面，不穿透皮层。对比 Neuralink N1 的**皮层内（intracortical）**设计：1024个电极直接插入运动皮层组织。

这个区别意味着什么？

**信号层面：** 皮层内电极（如 Utah 阵列、Neuralink N1）能记录单个神经元的放电（single-unit activity），信号信噪比高，解码精度强。Neuralink 的首位患者 Noland Arbaugh 实现了 >9 bits/s 的光标控制带宽，每天使用超过10小时。相比之下，硬膜外电极记录的是更大范围的群体电场信号（类似 ECoG），空间分辨率低得多。NEO 只有8个传感器通道，和 Neuralink 的1024通道不在一个数量级。

**安全层面：** 但硬膜外的优势同样巨大。不穿透脑组织意味着：无出血风险、无胶质瘢痕形成、无电极回缩问题（Neuralink 在植入约3个月后就有 ~85% 的电极线程发生回缩）。这直接降低了监管审批的门槛。NEO 自2023年10月以来完成了36项临床试验，其中32项在2025年短短几个月内密集完成，最终顺利拿到批准。

**临床效果：** NEO 的目标不是高精度光标控制或文字输入，而是**运动康复**。患者董辉（39岁，车祸导致颈部以下瘫痪）在植入后第9天就用右手成功抓住了球。经过11个月的康复训练，他能握笔写字。设备将脑信号解码后驱动一个软体机器人手套辅助训练，本质上是一个**神经反馈闭环康复工具**，而不是 BrainGate/Neuralink 式的"意念直接控制电脑"。

**这才是关键洞察：** BCI 领域正在分化出两条不同的产品化路线。一条是 Neuralink/BrainGate 代表的"高带宽-高精度-高风险"路线，追求接近自然运动的解码性能；另一条是 NEO 代表的"低带宽-高安全-快审批"路线，瞄准的是更容易落地的康复辅助场景。NEO 之所以能成为全球首个商用侵入式 BCI，恰恰是因为它选择了后者。

这并不意味着 NEO 的路线"更好"。J Neural Eng 刚发表的综述 (Meyer & Zamani, 2026) 指出，对于当前的临床目标（可靠通信和功能性运动恢复），中等带宽配合模型先验和共享控制架构已经足够。但对于speech BCI这样的高维任务，高通道数仍然是必要的。两条路线服务不同的患者需求。

---

### Context from the Knowledge Base

对比知识库中的里程碑：

| | NEO (2026) | Neuralink N1 (2024) | BrainGate (2006-) |
|---|---|---|---|
| 电极位置 | 硬膜外 | 皮层内 | 皮层内 |
| 通道数 | 8 | 1024 | 96 |
| 无线 | 是 | 是 | 否（经皮连接器） |
| 临床批准 | 商用（中国NMPA） | 临床试验（FDA IDE） | 临床试验（FDA IDE） |
| 核心应用 | 运动康复 | 光标/设备控制 | 光标/设备控制 |
| 植入手术时间 | ~90分钟 | ~2小时（机器人辅助） | ~3小时 |

NEO 的获批还有一个政策背景：中国最新的五年规划将 BCI 列为六大未来科技竞争关键产业之一（与量子技术、人形机器人并列），并将 NEO 纳入医保编码体系。这意味着 BCI 在中国正从实验室走向大规模临床部署。

---

## X Thread (English)

**Thread: China just approved the world's first commercial invasive BCI. But the real story isn't about a US-China race -- it's about a fundamental engineering tradeoff that every BCI developer must face.**

1/ China's NMPA approved NEO, an invasive brain-computer interface by Neuracle Technology + Tsinghua University, for commercial use in paralyzed patients. It's the first invasive BCI in the world to move beyond clinical trials.

2/ The patient story is remarkable: Dong Hui, paralyzed from the neck down after a car accident, had NEO implanted in Nov 2024. By day 9 of training, he grabbed a ball without assistance. After 11 months, he could write his own name with a pen.

3/ But here's what most coverage misses: NEO's sensors sit ON TOP of the brain's protective membrane (epidural). They don't penetrate cortical tissue. Compare this to Neuralink's N1, which inserts 1024 electrodes directly into the motor cortex.

4/ This is a massive design tradeoff. Epidural = far fewer channels (8 vs 1024), lower signal resolution, less decoding precision. But also: no bleeding risk, no glial scarring, no electrode retraction (Neuralink saw ~85% thread retraction at ~3 months).

5/ The safety profile is what enabled fast approval. Neuracle ran 36 clinical trials since Oct 2023, with 32 packed into just a few months in 2025. Lower surgical risk = lower regulatory bar.

6/ But the applications are fundamentally different. NEO isn't trying to be a high-bandwidth neural interface for computer control. It's a rehabilitation tool: brain signals drive a robotic glove for motor retraining. The goal is neural remodeling, not cursor control.

7/ A new review in J Neural Eng (Meyer & Zamani 2026) asks exactly the right question: "Do we need high bandwidth?" For rehab and basic motor restoration, moderate bandwidth + smart algorithms is enough. For speech BCIs decoding 60+ words/min, you still need dense arrays.

8/ So BCI is splitting into two product tracks: High-bandwidth/high-risk (Neuralink, BrainGate) for digital autonomy. Low-bandwidth/high-safety (NEO) for physical rehabilitation. NEO won the regulatory race precisely because it chose the second path.

9/ China is also putting serious institutional weight behind this: BCI is now in the national 5-year plan alongside quantum tech and humanoid robots. NEO already has a health insurance code. This is infrastructure for scale, not just a research win.

10/ The next few years will be fascinating. Neuralink is scaling to high-volume production. China has more BCI devices in the approval pipeline (Beinao-1, targeting ~2028). The question isn't who wins -- it's whether both approaches can deliver for the patients who need them.

---

## 小红书文案 (Chinese)

**中国批准了全球第一个商用脑机接口，但真正的故事不是"赢了Neuralink"**

今天聊一个刚发生的大事：中国药监局批准了 NEO 脑机接口的商业使用，这是全球第一个走出临床试验、正式商用的侵入式脑机接口。

先说患者的故事。董辉，39岁，车祸后颈部以下瘫痪。2024年11月植入 NEO，训练第9天右手成功抓住了球。11个月后，他能握笔写下自己的名字。他说："我激动得连自己名字都写漏了一笔。"

但我想聊的不是"中国赢了"这个叙事，而是 NEO 的技术路线选择为什么值得深思。

**关键区别：NEO 的传感器放在硬脑膜上面，不刺入大脑。**

这和 Neuralink 完全不同。Neuralink N1 有1024个电极直接插入皮层，能记录单个神经元放电，信号精度极高。NEO 只有8个传感器，贴在脑膜外，记录的是更粗糙的群体信号。

信号差这么多，为什么 NEO 反而先拿到批准？

**因为不刺入大脑 = 不出血、不留疤、不回缩。** Neuralink 植入3个月后约85%的电极线程发生回缩，NEO 完全不存在这个问题。安全风险低，审批门槛自然低。

**而且 NEO 的目标本身就不同。** 它不是让你用意念刷手机，而是一个康复工具：脑信号解码后驱动一个机器人手套，帮你训练手部抓握能力。目标是神经可塑性重建，让大脑重新学会控制手。

所以现在 BCI 领域其实在分化成两条路线：

- **高带宽路线**（Neuralink、BrainGate）：1024通道，高精度解码，目标是打字、上网、控制机器人
- **低带宽路线**（NEO）：8通道，够用就好，目标是运动康复和神经重塑

NEO 之所以成为全球第一个商用侵入式 BCI，恰恰是因为选择了第二条路——更安全、更容易落地。

最后一个信息：中国最新五年规划把 BCI 列为六大关键产业之一，NEO 已经开始纳入医保编码。这不是实验室里的论文，这是要大规模铺开的临床基础设施。

对于脑机接口来说，2026年可能真的是"everything changed"的一年。

---

*Sources:*
- [MIT Technology Review: China has approved the world's first invasive brain-computer chip](https://www.technologyreview.com/2026/06/01/1138133/china-world-first-brain-chip/)
- [Meyer & Zamani 2026 - But do we need high bandwidth? J Neural Eng](https://iopscience.iop.org/article/10.1088/1741-2552/ae6dfd)
- [Swanson et al. 2026 - Recalibration of iBCIs systematic review, J Neural Eng](https://doi.org/10.1088/1741-2552/ae7694)
- [Neuralink PRIME Study updates](https://neuralink.com/blog/prime-study-progress-update/)
- Knowledge Base: Neuralink 2024, BrainGate 2023 long-term safety data
