# -*- coding: utf-8 -*-
# 2026-09-29 日报「ECoG 电极同时解码语音和手势」图卡。文案以 draft.md「已定稿」为准，按版面预算压缩。
# 角标按全期首次出现顺序：¹ Brosler ² Metzger ³ Deo ⁴ Singer-Clark ⁵ Ray ⁶ Crone
import sys
sys.path.insert(0, ".claude/skills/dailybci/scripts")
from card_generator import CardGenerator

OUT = "output/2026-09-29-speech-gesture"
P = f"{OUT}/figs"
gen = CardGenerator(date="2026.09.30")

# 01 封面
gen.cover_card(
    "ECoG电极同时解码", "语音和手势",
    "Edward Chang 组：训练数据包含边说边比，两路输出都能解准。",
    f"{OUT}/01-cover.png",
    source="2026 年 9 月 Nature Neuroscience《Simultaneous speech and gesture decoding for multimodal communication in paralysis》· 通讯作者 Edward F. Chang（UCSF）· 本期为该文解读",
    concept_image=f"{P}/fig1a.png", concept_height=400, title_size=88, title_top=90)

# 02 目录与来源
gen.figure_card(f"{P}/fig-toc.png", "目录与来源", [
    "来源：2026 年 9 月 14 日在线发表于 Nature Neuroscience 的论文《Simultaneous speech and gesture decoding for multimodal communication in paralysis》¹。共同一作 Samantha C. Brosler、Jessie R. Liu、Alexander B. Silva，通讯作者 Edward F. Chang（加州大学旧金山分校神经外科）。同组 2023 年在 Nature 发表过用 ECoG 解码语音并驱动面部化身的工作²。",
    "方法：3 名重度瘫痪者，左半球硬膜下 253 触点 ECoG，比较只说、只比、边说边比三种情境下的训练与解码。",
], f"{OUT}/02-toc.png", figure_height=620, annot_size=27)

# 03 ① 旧认知（文字卡）
gen.text_card(None, [
    "人交流时常常边说边比划。此前的 BCI 研究多数一次只解码一种行为：语音、光标、手势或行走¹。",
    "少数同时解码两种行为的研究用的是皮层内微电极，都发现两种行为会互相干扰：",
    "1. 一名 C4 脊髓损伤被试同时动两只手时，神经元调谐相对单手运动发生非线性变化，解码器要改结构才能解好³。",
    "2. 一名 ALS 被试的电极在腹侧中央前回（ventral precentral gyrus），同时说话会降低他用这片皮层控制光标的表现⁴。",
    "两项研究各只有一名被试。那么，换成贴在皮层表面的电极，情况如何？",
], f"{OUT}/03-prior.png", heading_lines=["① 同时做两件事，", "皮层内解码会互相干扰"])

# 04 ① 问题与答案（图 2a）
gen.figure_card(f"{P}/fig2a.png", "Brosler et al. 2026, Fig. 2a", [
    "ECoG 记录的是成千上万个神经元的场电位，同时做两件事是否也会干扰，此前基本没有检验过¹。Chang 组问：同一块阵列，在上图三种情境（只说、只比、边说边比）下，能否都解码准语音和手势¹？",
    "答案是能，前提是训练数据包含边说边比的试次，并把另一种行为标成静息¹。先看信号从哪里来。",
], f"{OUT}/04-question.png", figure_height=400, title="① ECoG 上会不会干扰，\n此前没有检验过")

# 05 ② 图 1b
gen.figure_card(f"{P}/fig1b.png", "Brosler et al. 2026, Fig. 1b", [
    "3 名重度瘫痪者（2 名脑干卒中，1 名 ALS）左半球感觉运动皮层（sensorimotor cortex）硬膜下各贴一块 253 触点 ECoG，有线引出¹。",
    "如上图，触点按三类动作的高 γ 响应（70–150 Hz）着色：绿为口面与语音，红为手臂，蓝为头眼。高 γ 与电极附近的放电关系紧密⁵，空间分布比 α、β 频段更局限⁶，适合区分触点偏好。三人的偏好都沿中央前回（precentral gyrus）按躯体定位排列¹。",
    "两路信号都在同一块阵列上。它们彼此分得开吗？",
], f"{OUT}/05-array.png", figure_height=360, title="② 一块阵列覆盖了\n说话和手臂的皮层")

# 06 ② 图 2b+c
gen.figure_card(f"{P}/fig2bc.png", "Brosler et al. 2026, Fig. 2b–c", [
    "如上图，蓝线为只说，橙线为只比，绿线为边说边比。e164 只对说话响应，e151 只对手势响应，e58 对两者都响应¹。",
    "全阵列里两种行为都显著激活的触点，在两名被试中约占 38% 和 27%（按原文图 2e 计数自算）¹。",
    "用单独做的数据训练的解码器，遇到边说边比还准吗？",
], f"{OUT}/06-overlap.png", figure_height=300, title="② 说话和手势共用\n中央前回的一部分触点")

# 07 ③ 图 3c
gen.figure_card(f"{P}/fig3c.png", "Brosler et al. 2026, Fig. 3c（Bravo-6 语音解码）", [
    "每个解码器分别用只说、边说边比、两者混合的数据训练，再在两类试次上测试¹。",
    "如上图，只用单独说的数据训练，测边说边比时中位数约 64%，比测只说时低约 25 个百分点（读图估计）；反过来也会下降。手势解码和另一名被试同样如此¹。训练量相同时结论不变¹。混合训练在两类试次上都最高或并列最高¹，其数据总量论文未说明。",
    "为什么会这样？",
], f"{OUT}/07-context.png", figure_height=420, title="③ 解码器在训练时\n见过的情境里最准")

# 08 ③ 图 3e,f
gen.figure_card(f"{P}/fig3ef.png", "Brosler et al. 2026, Fig. 3e–f", [
    "作者用梯度显著性（gradient-based saliency）估计每个触点对解码的贡献¹。如上图，红色表示用边说边比数据训练后贡献升高，蓝色表示降低，点越大表示两种行为共用得越多。",
    "降得最多的集中在共用触点，升高的多是专属触点¹。这是定性描述，正文没有统计检验；很多被降权的共用触点仍有显著贡献¹。",
    "模型是不是只记住了训练过的组合？",
], f"{OUT}/08-saliency.png", figure_height=420, title="③ 用同时做的数据训练后，\n解码器更依赖专属触点")

# 09 ③ 图 3g,h
gen.figure_card(f"{P}/fig3gh.png", "Brosler et al. 2026, Fig. 3g–h", [
    "训练手势解码器时拿掉所有含「hello」的边说边比试次，再测「hello + 挥手」这类试次。短语和手势各自都见过，没见过的只是这个组合¹。",
    "如上图，见过与没见过的组合没有显著差异：手势 65.8% 对 66.7%（P=0.29），语音 79.3% 对 80.0%（P=0.35），仅 Bravo-6 做了这项¹。扩大词表时不必把每种组合都采一遍。",
    "两个解码器同时运行，还会出什么错？",
], f"{OUT}/09-unseen.png", figure_height=400, title="③ 没见过的短语–手势组合\n也能解")

# 10 ④ 图 4b
gen.figure_card(f"{P}/fig4b.png", "Brosler et al. 2026, Fig. 4b", [
    "语音与手势是两个独立的解码器，各自输出 10 类之一或「静息」¹。只说时手势解码器报出手势，就是误触发。如上图灰色箱体，静息类只用真静息训练时，遇到另一种行为的误触发率为 30.6% 和 76.0%¹。",
    "改法只动标签：把另一种行为的试次也标成静息，与真静息各占一半。改后（紫色）两人都降到 0.0%¹。",
    "反过来，该输出时报了静息怎么办？",
], f"{OUT}/10-fp.png", figure_height=380, title="④ 把另一种行为标成静息，\n误触发降到 0")

# 11 ④ 图 4c
gen.figure_card(f"{P}/fig4c.png", "Brosler et al. 2026, Fig. 4c", [
    "漏检是在说或在比，解码器却判为静息。如上图棕色箱体，只用单独做的数据训练，边说边比时漏检率为 14.5% 和 34.9%；只用边说边比训练，测单独做时也有 12.0% 和 5.2%¹。",
    "混合训练（深蓝）后，两类试次上的漏检率都在 0.8%–4.5%¹。图 3c 中的准确率下降，有一部分来自这类漏检。",
    "这套做法放到实时系统里还成立吗？",
], f"{OUT}/11-fn.png", figure_height=400, title="④ 混合训练压低了漏检")

# 12 ⑤ 图 5a
gen.figure_card(f"{P}/fig5a.png", "Brosler et al. 2026, Fig. 5a", [
    "如上图，实时系统里两个解码器并行输出，化身做出手势，说出的话显示为文字¹。",
    "Bravo-6 的实时准确率：只比 81.8%；边说边比时手势 66.0%、语音 70.0%，与离线的 68.8%、77.5% 接近；对话范式手势 85.0%、语音 75.0%，但只有 20 次试次¹。机会水平均为 9.1%。实时部分没有单独测只说的准确率¹。",
], f"{OUT}/12-realtime.png", figure_height=300, title="⑤ 实时系统里，准确率\n与离线分析接近")

# 13 ⑥ 闭环（文字卡）
gen.text_card(None, [
    "回到开头的问题：同时做两件事时，ECoG 解码同样受干扰。只用单独做的数据训练，边说边比时语音准确率下降约 25 个百分点，漏检率达到 14.5% 和 34.9%¹。",
    "这篇的处理办法是调整训练数据，没有改动电极或解码器结构：混合训练，加上把另一种行为标成静息。改后漏检率降到 0.8%–4.5%，对另一种行为的误触发降到 0.0%¹。",
    "作者认为，开头提到的皮层内研究没有专门针对同时做的情境训练，同样的策略可能也适用于皮层内记录¹。这一点还没有经过检验。",
], f"{OUT}/13-closing.png", heading_lines=["⑥ ECoG 同样存在干扰，", "调整训练数据可以处理"])

# 14 ⑥ 局限性（文字卡）
gen.text_card(None, [
    "1. **样本小**：边说边比的分析只有 2 名被试，实时结果只有 1 名¹。",
    "2. **词表小**：最多 10 个短语和 10 个手势¹。",
    "3. **需要开始信号**：每次试次取一段固定时间窗给出一个标签，使用者还不能随时自主表达；作者把连续解码列为下一步¹。",
    "4. **尝试方式不一致**：Bravo-6 的手势只是想象，Bravo-1r 尽量做出动作¹。",
    "5. **混合训练的数据量未交代**：它的优势中有多少来自数据更多，无法判断。",
], f"{OUT}/14-limits.png", heading_lines=["⑥ 这项工作的五点局限"])

# 15 尾卡
refs = [
    "¹ Brosler SC, et al. (2026). Simultaneous speech and gesture decoding for multimodal communication in paralysis. Nature Neuroscience.",
    "² Metzger SL, et al. (2023). A high-performance neuroprosthesis for speech decoding and avatar control. Nature 620:1037–1046.",
    "³ Deo DR, et al. (2024). Brain control of bimanual movement enabled by recurrent neural networks. Sci Rep 14:1598.",
    "⁴ Singer-Clark T, et al. (2025). Speech motor cortex enables BCI cursor control and click. J Neural Eng 22:036015.",
    "⁵ Ray S, Maunsell JHR. (2011). Different origins of gamma rhythm and high-gamma activity in macaque visual cortex. PLoS Biol 9:e1000610.",
    "⁶ Crone NE, et al. (1998). Functional mapping of human sensorimotor cortex with electrocorticographic spectral analysis. II. Event-related synchronization in the gamma band. Brain 121:2301–2315.",
]
gen.tail_card(refs, f"{OUT}/15-tail.png", lead_paragraphs=[
    "这篇把「同时做会干扰」处理成了训练数据如何设计的问题。下一步要看的是：词表扩大、去掉开始信号之后，需要多少边说边比的数据才够。",
])
print("done")
