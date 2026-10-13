# -*- coding: utf-8 -*-
"""日报 2026-10-13 · 头皮 N140 的颅内来源（Mikulan 2026 bioRxiv）—— 卡片生成
用法：python3 build_n140_cards.py [卡片文件名 ...]"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from card_generator import CardGenerator

PROJ = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", ".."))
EP = os.path.join(PROJ, "output", "2026-10-13-n140-scalp-intracranial")
FIG = os.path.join(EP, "figs")
OUT = os.path.join(EP, "cards"); os.makedirs(OUT, exist_ok=True)
def f(n): return os.path.join(FIG, n + ".png")

only = set(sys.argv[1:])
def want(name): return not only or name in only

gen = CardGenerator(date="2026.10.13")

if want("01-cover.png"):
    gen.cover_card("头皮上的触觉波", "源自颅内岛盖",
                   "8 名患者同时记录头皮 EEG 与颅内电极：头皮上的 N140 与岛盖–后岛叶的局部场电位同时到达波谷，比同一位置的高频活动晚约 **28 ms**¹。",
                   os.path.join(OUT, "01-cover.png"),
                   concept_image=f("fig2d"), concept_height=370, title_size=120, title_top=70,
                   source="2026 年 10 月 bioRxiv《Simultaneous recordings link intracranial and scalp correlates of somatosensory awareness in humans》· Mikulan & Pigorini")

if want("02-toc.png"):
    gen.figure_card(f("toc"), "本期路线", [
        "2026 年 10 月 11 日，bioRxiv 预印本《Simultaneous recordings link intracranial and scalp correlates of somatosensory awareness in humans》。通讯作者 Ezequiel Mikulan 与 Andrea Pigorini（米兰大学）。合作者 Avanzini、Sartori 等 2016 年在 PNAS 发表过 99 名 sEEG 患者的体感响应图谱，本文第 ⑤ 章对照的颅内分布图即出自该文。",
        "方法：8 名癫痫术前患者，256 通道头皮 EEG 与立体定向深部电极（sEEG）同步记录，刺激手腕正中神经。"],
        os.path.join(OUT, "02-toc.png"), figure_height=600, annot_size=27)

C = [
 dict(n="①", t="头皮上的体感觉察信号，对应岛盖的局部场电位", out="03.png", a=[
   "用头皮 EEG 研究触觉感知时，常用的指标之一是 N140：刺激手腕后约 140 ms 出现的负波，近年被当作「刺激被感到」的头皮标记。它由颅内哪里产生，长期靠模型估计。",
   "2026 年 10 月，米兰大学的团队在 8 名癫痫术前患者身上，同时记录了 256 通道头皮 EEG 与颅内深部电极（sEEG）¹。作者的结论是：N140 对应顶叶岛盖与后岛叶的局部场电位（local field potential，**LFP**）经容积导体传到头皮的部分，两者峰值平均相差约 **1 ms**；同一位置的宽带高频活动（broadband high-frequency activity，**BHA**）比 LFP 早约 **28 ms**¹。",
   "对用 N140 做实验的人，它有了一个实测的颅内对应物。另一个推论是：颅内与觉察相关的高频活动，在头皮上难以可靠测到。",
   "下面先交代这两个标记各自是什么。"]),
 dict(n="②", t="头皮上的波，来源多靠模型估计", fig="inverse", lab="示意图：两组不同的颅内源，产生同一张头皮电压分布（自制）", fh=420, out="04.png", a=[
   "头皮 EEG 每一时刻的电压，是脑内大量电流源经脑脊液、颅骨、头皮传导后的叠加。从头皮的电压分布反推源分布，是一个不适定的逆问题（ill-posed inverse problem）：如上图，不同的源组合可以产生同一张头皮分布图。",
   "因此，「某个成分来自某个脑区」的结论，多数来自源定位模型的估计；另一类做法是拿不同时间采集的颅内记录作比对¹。两种做法都没有在同一时刻、同一个人身上，把头皮波形与颅内信号逐毫秒对齐。",
   "体感研究里的 N140，就是一个来源靠这种方式推定的成分。"]),
 dict(n="②", t="N140 被重新解读为体感觉察负波 SAN", fig="fig2a", lab="Fig. 2a：刺激右手正中神经时的头皮平均波形", fh=330, out="05.png", a=[
   "刺激手腕的正中神经（median nerve）后约 140 ms，头皮上会出现一个负向偏转，称 N140，1977 年由 Desmedt 与 Robertson 首报²。如上图，本文刺激右手时，这一负波在 116 ms 前后最明显¹。",
   "传统上 N140 用**阈上**刺激测量：强度明显高于感觉阈值（sensory threshold，被试约一半次数能感到的强度），每次都能感到，直接平均波形即可。",
   "2021 年，Dembski、Koch 与 Pitts 把它重新解读为体感觉察负波（somatosensory awareness negativity，SAN）³。SAN 用**近阈值**刺激测量：强度在阈值附近，同样的刺激有时感到、有时没有，两类试次相减，得到的负波即 SAN。",
   "两种测法得到的是否同一段负波，此前没有直接验证。"]),
 dict(n="②", t="颅内也有一个觉察标记：岛盖–后岛叶的 tonic BHA", fig="fig2c", lab="Fig. 2c：颅内触点的平均 BHA 与时频图", fh=340, out="06.png", a=[
   "颅内这一头来自 sEEG（立体定向植入的深部电极）。刺激正中神经后，初级体感皮层（primary somatosensory cortex，S1）先有一段短暂响应；随后，顶叶岛盖（parietal operculum）与后岛叶（posterior insula）出现一段 50–150 Hz 的宽带高频活动，持续约到 250 ms，称 tonic 响应⁴。",
   "如上图，黑线是本文这一类触点上的平均 BHA，约 0.1 s 达峰；蓝线为同一触点的 LFP¹。",
   "这些区域受损的患者出现触觉觉察障碍⁵；近阈值任务里，tonic BHA 能区分被感到与没被感到的刺激⁶。",
   "N140 与 tonic BHA 时程相近、位置看来重叠，却从未在同一个人身上同时测过。"]),
 dict(n="③", t="同一根触点，能读出 LFP 与 BHA 两种信号", fig="fig1d", lab="Fig. 1d：三次刺激的单试次信号", fh=330, out="07.png", a=[
   "sEEG 的一个触点记录的是一段电压随时间的变化，本文从中读出两样东西¹。如上图，三次刺激各占一列：",
   "- **LFP**（蓝）：电压波形本身的低频部分，有正有负，刺激后下沉。主要来自大量神经元突触电流的叠加⁷。",
   "- **BHA**（黑）：同一段信号在 50–150 Hz 的功率，只有大小，刺激后出现尖峰。常作为触点附近神经元群体放电的代理⁸。",
   "橙线是同一时刻头皮 Pz 电极的 EEG，单次刺激下看不出响应。头皮 EEG 只能对应 LFP 这类低频信号：高于约 30 Hz 的头皮信号难以与伪迹区分，本文的头皮 EEG 只保留了 0.5–40 Hz¹。",
   "下一张讲作者怎样同时测到这三种信号。"]),
 dict(n="④", t="8 名 sEEG 患者，头皮与颅内同时记录", fig="fig1a", lab="Fig. 1a：头皮电极（橙）与 sEEG 电极（蓝）", fh=400, out="08.png", a=[
   "被试是 8 名做癫痫术前评估的患者，颅内已为定位致痫灶植入 sEEG 电极。评估结束时，神经外科医生按无菌流程为他们加戴 256 通道头皮 EEG 网帽¹。如上图，照片中箭头所指，是 sEEG 电极露在头皮外的部分。",
   "两台放大器各自采集（均 1000 Hz），刺激手腕时，刺激器向两台同时发送触发信号，离线据此对齐¹。",
   "以前少见有两个原因：sEEG 位置由临床决定，本文 1306 个触点里只有 27 个出现 tonic BHA¹；据作者检索，此前唯一的同被试对照多在术中麻醉下完成⁹，而麻醉会改变诱发电位的潜伏期与形态。",
   "下一张看三种信号的时间顺序。"]),
 dict(n="⑤", t="头皮 N140 与岛盖 LFP 同时到达波谷，BHA 早约 28 ms", fig="fig2d", lab="Fig. 2d：岛盖 LFP（蓝）与对侧头皮 EEG（橙）的平均波形", fh=400, out="09.png", a=[
   "如上图，蓝线是岛盖–后岛叶触点 LFP 的平均（左轴），橙线是刺激对侧额颞区头皮通道的平均（右轴，所用通道见插图中的橙点）。两者在约 0.1 s 同时到达波谷，下降与回升的走势基本重合¹。按图上刻度读，LFP 波谷约 −45 µV，头皮约 −1.2 µV，幅度相差约 40 倍。",
   "群体峰潜伏期均值：BHA **96 ms**，LFP **124 ms**，头皮 EEG **125 ms**¹。BHA 早于 LFP 约 28 ms，差异显著；LFP 与 EEG 相差约 1 ms，差异不显著¹。",
   "逐个被试看，LFP 与 EEG 的峰时差有正有负，大小与触点深度有关，下一张展开。"]),
 dict(n="⑤", t="触点离头皮越远，LFP 与头皮 EEG 越不相像", fig="fig2gh", lab="Fig. 2g–h：峰时差、波形相关与触点深度", fh=340, out="10.png", a=[
   "逐个被试看，LFP 与头皮 EEG 的峰时差有正有负。作者用触点到头皮的最短距离来解释这一差异¹。",
   "如上图，每个点是一名患者。左图横轴是两者的峰时差，纵轴是触点到头皮的距离：距离约 28 mm 的触点，峰时差接近 0；越远，峰时差越大，正负都有（二次回归，n = 8）¹。右图纵轴是两条波形的相关系数（互相关最大值），平均 0.76；距离每增加 1 cm，相关系数降低约 **0.27**¹。",
   "作者的解释是：头皮 EEG 对浅层源更敏感，深处的源传到头皮时衰减更多，并与其他源的信号混在一起¹⁰。",
   "下一张看空间位置是否也对得上。"]),
 dict(n="⑤", t="头皮源定位与 99 人的颅内 BHA 分布图有显著重叠", fig="fig3c", lab="Fig. 3c：头皮源定位（橙）、颅内 BHA 分布（黑）与重叠（绿）", fh=340, out="11.png", a=[
   "作者用头皮数据做源定位，取 70–150 ms 内最强的前 15% 源（橙），与此前 99 名 sEEG 患者中出现持续性 BHA 的触点分布图（黑）比较⁴˒¹。",
   "重叠程度用 Dice 系数衡量（0 为不重叠，1 为完全重合），结果为 **0.34**，在保留空间自相关的置换检验下 p = 0.03¹。如上图，橙色范围比黑色大得多：重叠在外侧裂一带有一条，内侧面还有一大片。",
   "可以得出的初步结论有两点：岛盖–后岛叶确实在 N140 的来源范围之内；但 N140 很可能不只来自这里，内侧面那片重叠就是候选。橙色偏宽也可能部分来自源定位本身的空间分辨率有限，作者没有展开讨论这一点。",
   "下一张回到觉察本身。"]),
 dict(n="⑤", t="近阈值实验里，只有被感到的刺激诱发这个负波", fig="fig3d", lab="Fig. 3d：重新分析 Schröder 2021 的头皮数据", fh=290, out="12.png", a=[
   "本文用的是阈上刺激、被试不报告，每次刺激都能感到，无法直接比较「感到」与「没感到」。为此，作者重新分析了一项独立研究（24 名被试）的头皮 EEG 数据：近阈值强度下，同样的刺激有时被报告感到（橙），有时没有（紫）¹¹。",
   "如上图，橙线在约 0.1–0.18 s 出现负波，紫线没有；两者差异显著（灰条，95–175 ms）¹。",
   "由此可以判断 N140 与 SAN 是否同一段负波：被感到的刺激诱发的负波，潜伏期与波形和阈上实验的 N140 相近；没被感到时不出现。阈上刺激每次都能感到，所以总能记到它。作者因此认为 N140 与 SAN 是同一段负波¹；这是跨数据集的定性比较，更细的差异仍待同一批被试直接对比。",
   "下一张把前面的结果连起来。"]),
 dict(n="⑥", t="两条觉察证据，对应同一事件的先后两个阶段", fig="fig2f", lab="Fig. 2f：三种信号的峰潜伏期（均值与 95% 置信区间）", fh=300, out="13.png", a=[
   "头皮的 N140/SAN 与颅内的 tonic BHA，在同一个人、同一时刻测量后，排成了一条时间序列¹：",
   "1. 约 96 ms：岛盖–后岛叶的 BHA 达峰；\n2. 约 124 ms：同一触点的 LFP 到达波谷；\n3. 约 125 ms：头皮 N140 到达波谷。",
   "如上图，BHA 与 LFP 之间的差异显著（星号），LFP 与 EEG 之间不显著（n.s.）¹。作者对 BHA 领先的解释是：BHA 反映较快的局部神经元活动，LFP 是更大范围、更长时间内电流叠加的结果¹。",
   "按作者的结论，两条证据描述的是同一事件的两个阶段：BHA 所代表的局部活动在先，约 30 ms 后形成场电位，头皮记到的是后者。",
   "下一张讲这个结论能支持到哪一步。"]),
 dict(n="⑦", t="本研究的局限性", fig="fig3f", lab="Fig. 3f：各 session 单试次可检出的比例", fh=290, out="14.png", a=[
   "本文结果直接支持的结论是：N140 与岛盖–后岛叶的 LFP 在时间与波形上对齐，在 BHA 之后约 28 ms 出现¹。",
   "1. **样本小**：8 人，每人只分析一个触点，位置由临床植入决定；与深度相关的两个回归也只有 8 个点¹。",
   "2. **证据属相关性**：不排除其他来源，图 3c 内侧面的重叠、Allison 等提出的额叶与内侧中央皮层⁹都是候选。",
   "3. **本文数据不含「感到/没感到」对比**：N140 与 SAN 等同，依赖跨数据集的比较¹¹。",
   "4. **单试次层面没有回答**：如上图，阈上刺激下 BHA 在约 95% 的试次可检出，LFP 约 74%¹；哪一种与单次「感到」对应，需要近阈值条件下的同步记录。"]),
 dict(n="⑦", t="对脑机接口研究的两点推断", out="15.png", a=[
   "以下两点是我们的推断，论文本身没有讨论脑机接口。",
   "1. **头皮 EEG 上的「高 γ」特征，来源需要单独核实。** 本文头皮 EEG 只保留到 40 Hz，对上的是岛盖的 LFP；作者引用的研究指出，高于约 30 Hz 的头皮信号难以与肌电、微眼跳等伪迹区分¹。以头皮高频成分为特征的非侵入 BCI，需要说明这些成分来自脑内而不来自伪迹。",
   "2. **感觉反馈 BCI 可能多一个客观读数。** 皮层内脑机接口里，人工触觉的一条路线是向初级体感皮层（S1）做皮层内微刺激（intracortical microstimulation，ICMS）¹²，患者是否感到靠口头报告。若觉察相关活动出现在岛盖–后岛叶，刺激后头皮上的 SAN 或岛盖的 LFP，有可能用作「人工触觉是否被感到」的读数。这是一个可以检验的推论，本文没有涉及。"]),
]

for c in C:
    if not want(c["out"]):
        continue
    o = os.path.join(OUT, c["out"])
    if c.get("fig"):
        gen.figure_card(f(c["fig"]), c["lab"], c["a"], o, figure_height=c["fh"],
                        title=c["t"], title_num=c["n"])
    else:
        gen.text_card(None, c["a"], o, heading_lines=[f'{c["n"]} {c["t"]}'])

REFS1 = [
    "1. Mikulan E, et al. (2026). Simultaneous recordings link intracranial and scalp correlates of somatosensory awareness in humans. bioRxiv 10.64898/2026.10.03.756393.",
    "2. Desmedt JE, Robertson D. (1977). Differential enhancement of early and late components of the cerebral somatosensory evoked potentials during forced-paced cognitive tasks in man. J Physiol 271:761–782.",
    "3. Dembski C, et al. (2021). Perceptual awareness negativity: a physiological correlate of sensory consciousness. Trends Cogn Sci 25:660–670.",
    "4. Avanzini P, et al. (2016). Four-dimensional maps of the human somatosensory system. PNAS 113:E1936–E1943.",
    "5. Del Vecchio M, et al. (2021). Tonic somatosensory responses and deficits of tactile awareness converge in the parietal operculum. Brain 144:3779–3787.",
]
REFS2 = [
    "6. Albertini D, et al. (2025). Conscious tactile perception entails distinct neural dynamics within somatosensory areas. Curr Biol 35:2583–2596.",
    "7. Buzsáki G, et al. (2012). The origin of extracellular fields and currents — EEG, ECoG, LFP and spikes. Nat Rev Neurosci 13:407–420.",
    "8. Ray S, Maunsell JHR. (2011). Different origins of gamma rhythm and high-gamma activity in macaque visual cortex. PLoS Biol 9:e1000610.",
    "9. Allison T, et al. (1992). The relationship between human long-latency somatosensory evoked potentials recorded from the cortical surface and from the scalp. Electroencephalogr Clin Neurophysiol 84:301–314.",
    "10. Nunez PL, Srinivasan R. (2006). Electric fields of the brain: the neurophysics of EEG. Oxford University Press.",
    "11. Schröder P, et al. (2021). Dissociating perceptual awareness and postperceptual processing: the P300 is not a reliable marker of somatosensory target detection. J Neurosci 41:4686–4696.",
    "12. Flesher SN, et al. (2016). Intracortical microstimulation of human somatosensory cortex. Sci Transl Med 8:361ra141.",
]
if want("16-tail.png"):
    gen.tail_card(REFS1, os.path.join(OUT, "16-tail.png"), lead_paragraphs=[
        "N140 从 1977 年首报到今天，它的颅内来源大多靠源定位估计；这篇在 8 名患者身上，把它与岛盖–后岛叶的 LFP 在同一时刻对上了¹。",
        "下一步最直接的实验，是在近阈值任务里做同样的同步记录，看单次刺激中 BHA 和 LFP 哪一个与「感到」对应。作者也提出，同一套方法可以用于视觉、听觉的觉察负波¹。"])
if want("17-tail.png"):
    gen.tail_card(REFS2, os.path.join(OUT, "17-tail.png"))
