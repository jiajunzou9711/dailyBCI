# -*- coding: utf-8 -*-
"""Build 小红书 cards for series ③ — 一根电极扎进脑，会在哪四层出血."""
import sys, os, shutil
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(SCRIPT_DIR))
from card_generator import CardGenerator

PROJECT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "series-dura-03")
FIG = os.path.join(OUT, "figs")
PAPERS = os.path.join(PROJECT, "papers")
os.makedirs(OUT, exist_ok=True)

gen = CardGenerator(date="2026.07.29")
P = lambda n: os.path.join(OUT, n)
F = lambda n: os.path.join(FIG, n)
J = lambda n: os.path.join(PAPERS, n)

# 01 封面
gen.cover_card(
    "一根电极扎进脑",
    "会在哪四层出血",
    "每五台手术就有一台在 CT 上看得到出血，其中约九成没有症状。",
    P("01-cover.png"),
    source="从电极的穿刺路径重讲四类颅内出血，并回答两个物理问题——血管什么时候被推开、"
           "针为什么还要加粗。硬脑膜专题第 ③ 期。",
)

# 02 目录
shutil.copyfile(F("toc.png"), P("02-toc.png"))

# 03 路径总览
gen.figure_card(
    F("fig-bleeds.png"), "电极穿过哪一层，就可能在哪一层出血",
    [
        "四类颅内出血通常按外伤机制来记。换一个排法：按一根针**从外往里穿**的顺序排，"
        "四类正好一一对应到路径上的四个位置。",
        "从颅骨内板往里走，依次是：**颅骨与硬膜之间的潜在腔隙、硬膜自身、蛛网膜下腔、皮层实质**。"
        "每一个位置都有自己的血管，也就有自己的出血。",
        "先把这条路径走一遍，四类出血的名称、腔隙和血管来源会自己排好。",
    ],
    P("03-path.png"), figure_height=600,
)

# 04 EDH
gen.text_card(
    "第一站：硬膜外血肿，血来自走在硬膜里的动脉",
    [
        "路径的第一站是颅骨内板与硬膜骨内膜层之间。**这里是一个潜在腔隙**——正常状态下硬膜贴着骨面，"
        "第 ① 期讲过，开颅剥离之后它才被撑开。",
        "典型出血来源是**脑膜中动脉的分支**，它就走在硬膜层内。动脉血把硬膜从骨面继续剥开，"
        "在 CT 上形成边界清楚的**双凸透镜形**。",
        "这一类对经硬膜手术有特殊意义：常规做法切开硬膜时会在直视下处理这些血管，而"
        "**经硬膜插入不切开硬膜，针每穿一次就碰一次**，几十根丝就是几十次。往里一层，情况反而更微妙。",
    ],
    P("04-edh.png"),
)

# 05 SDH
gen.text_card(
    "第二站：硬膜下血肿其实形成在硬膜之内",
    [
        "「硬膜与蛛网膜之间」是常见的省略说法，那里同样没有真正的腔隙。",
        "真实情况是：**桥静脉在硬膜边界细胞层内撕裂**，血肿在硬膜之内形成，"
        "并通过持续出血进入这一层而扩大。硬膜边界细胞层就是第 ① 期讲过的、"
        "硬膜最内侧那层细胞间连接稀疏的结构。CT 上呈**新月形**。",
        "也就是说，这条路径上的前两类出血，都发生在**被撑开的潜在腔隙**里。"
        "再往里一层，才是唯一一个本来就存在的真实腔隙。",
    ],
    P("05-sdh.png"),
)

# 06 SAH + ICH
gen.text_card(
    "第三、四站：蛛网膜下腔出血与脑内血肿",
    [
        "**蛛网膜下腔出血（SAH）**：蛛网膜与软脑膜之间，充满脑脊液的真实腔隙。"
        "来源是软膜血管与皮层表面血管——正是电极丝必须横穿的那一层。血液混入脑脊液，可沿脑沟扩散。",
        "**脑内血肿（ICH）**：皮层实质内，沿电极道。来源是被切断的穿支血管。"
        "它直接破坏神经元与纤维，**致死病例主要出自这一类**。",
        "四类到此列完。接下来的问题是：它们到底有多常见。",
    ],
    P("06-sah-ich.png"),
)

# 07 发生率
gen.figure_card(
    F("fig-rate.png"), "McGovern 等 2019，549 台连续 sEEG 植入",
    [
        "这个数字之所以远高于既往报告，关键在原文的一个词：他们分级的是**每一张**术后 CT，"
        "而不是只读临床起疑的那些。评级由**神经放射科医师**在设盲条件下完成。",
        "关键在于比例的构成：出血里约 **88% 完全没有症状**。它们不会被登记为并发症，"
        "不会被处理，在统计表上近乎不存在。",
        "那么真正要问的问题就变成了：**什么决定了会不会出血。**",
    ],
    P("07-rate.png"), figure_height=460,
)

# 08 三区模型
gen.figure_card(
    J("pnas-fig6a.png"), "Obaid 等 2026, PNAS — 三区血管破裂模型",
    [
        "**Obaid 等 2026**（*PNAS* 123(13):e2529147123，**小鼠**）用高灵敏力传感器配合实时显微成像，"
        "看了 7.5–100 µm 一系列微丝插入时血管到底发生了什么。",
        "结果是三种结局，取决于血管落在针尖下方的哪个区：**捕获区**（被钉在针的表面上、被拉长、最后撕裂）、"
        "**位移区**（从针尖边缘下方滑出去，活下来）、**形变区**（离得远，只跟着组织弯一下）。",
        "决定血管落在哪个区的，是它**离针尖边缘有多远**。而这个距离有一个不随针粗细变化的宽度。",
    ],
    P("08-zones.png"), figure_height=520,
)

# 09 阈值
gen.figure_card(
    J("zone-model.png"), "位移壳厚度固定，捕获区随直径缩小",
    [
        "针尖轴线上，由对称性，组织的横向速度必然为零——血管在那里无处可去。"
        "越靠近边缘，组织越能绕过棱边向外流，血管越有机会滑走。",
        "这圈可逃带的宽度 **w 由局部组织力学决定，与针的直径无关**。端面直径为 d，"
        "两侧各一圈宽 w，中间剩下 **d − 2w** 是逃不掉的核。**当 d ≤ 2w，捕获区消失。**"
        "实测临界直径约 **25 µm**，反推 w ≈ 12.5 µm。",
        "出血率对直径因此呈 S 形：**≥100 µm 必然出血，100–25 µm 偶发，<25 µm 不出血**。"
        "既然细针不出血，Neuralink 为什么反而把针加粗了。",
    ],
    P("09-threshold.png"), figure_height=540,
)

# 10 d^4 vs d
gen.figure_card(
    F("fig-margin.png"), "两条标度并排放，账就清楚了",
    [
        "官方说法很直白：原来的针**无法可靠穿透硬膜**，于是把针径**略微加粗**。",
        "破膜所需的力**线性于直径**，说明失效是沿接触棱边起裂的，而不是端面把膜压破；"
        "而针不屈曲所能推出的力随**直径的四次方**增长。两者之比因此正比于 **d³**。",
        "原来的针并非不够锋利，而是在把力推到破膜所需之前**自己先屈曲了**。"
        "加粗把上限抬上去，账就翻了过来。但账单在另一边。",
    ],
    P("10-margin.png"), figure_height=520,
)

# 11 代价
gen.figure_card(
    F("fig-cost.png"), "加粗之后，三个量同时变化",
    [
        "穿破前的**压陷从 0.33 mm 加深到 0.52 mm**，已经和第 ② 期讲的心跳搏动"
        "（0.1–0.5 mm）同一个数量级；端面平均压强降到约三分之一。",
        "最要紧的是第三条：**61 µm 已经越过了 25 µm 那条临界线**，"
        "重新进入了会扎破血管的区间。锐化针尖可把有效直径降低 20–30 µm，仍高于临界值。",
        "扎破之后，账要付很久。",
    ],
    P("11-cost.png"), figure_height=520,
)

# 12 人体尸检
gen.text_card(
    "人体尸检看到的东西",
    [
        "**Szymanski 等 2021**（*J Neural Eng* 18:0460b9，**人**）：一名 64 岁四肢瘫男性植入三个微电极阵列，"
        "**7 个月后因无关原因去世**，取组织做病理。",
        "三个阵列都仍能记录到神经元活动，但 **S1 阵列包裹最重、信号质量最差，且电刺激无法引出体感**。"
        "组织学上：BA5 位点可见**局灶性脑微出血**与**含铁血黄素巨噬细胞**聚集；"
        "S1 位点可见**血管再通、神经元丢失、广泛的皮层下白质坏死**。",
        "作者的结论是：植入过程中的**血管破坏与微出血，是阵列整体与单个电极性能的重要影响因素**。"
        "分子层面这条链已经被拆开了。",
    ],
    P("12-autopsy.png"),
)

# 13 纤维蛋白原链
gen.figure_card(
    F("fig-fibrin.png"), "Schachtrup 等 2010, J Neurosci",
    [
        "血脑屏障一破，**纤维蛋白原**立刻漏进中枢。它是**潜伏型 TGF-β 的载体**，"
        "把生长因子一并带进脑实质，进而诱导星形胶质细胞 **Smad2 磷酸化**，"
        "结果是沉积**硫酸软骨素蛋白聚糖**，抑制神经突生长。",
        "关键在于这不是相关性：**用遗传或药理手段去掉纤维蛋白原，整条链都减轻**。这是干预实验。",
        "配合 **Saxena 2013**（*Biomaterials*，**大鼠**，16 周）观察到的"
        "「血脑屏障破坏程度与电极记录性能负相关」，这条链在动物上是成立的。"
        "那么止住出血，是不是就解决了慢性问题。",
    ],
    P("13-fibrin.png"), figure_height=520,
)

# 14 两条链
gen.figure_card(
    F("fig-chronic.png"), "慢性危害是两条链，不是一条",
    [
        "**链 A** 由血管损伤起始，可以靠避开血管减少。**链 B** 由植入体持续存在维持，"
        "与是否扎中血管无关：**Biran 2005**（大鼠）发现只做刺伤的对照组炎症会消退，有电极留置的不消退；"
        "**Solarana 2020**（**小鼠**，双光子 + OCT 血管造影）发现电极 100 µm 内**毛细血管密度显著下降**，"
        "而只开窗不植电极的对照动物血管密度反而持续增加，随后 **137 ± 56 天出现 100 µm 内 50% 的神经元丢失**。",
        "**Barrese 2013**（**恒河猴**，78 个阵列）的失效模式分布也指向同一侧：主导是"
        "**急性机械失效 48.4%**（其中 83% 是连接器与线束），脑膜包裹占慢性失效的一半以上，"
        "而作者判断最重要的单一因素是**绝缘材料失效**。",
        "两条链各自贡献多少，目前没有定论。**止住出血解决不了全部。**",
    ],
    P("14-two-chains.png"), figure_height=480,
)

# 15 DSA
gen.figure_card(
    F("fig-dsa.png"), "Stefanelli 等 2022, World Neurosurg",
    [
        "即便如此，链 A 那部分仍然值得单独去解决，因为它是**可预测、可干预**的。",
        "把术后 CT 与术前**数字减影血管造影（DSA）**配准后回溯：所有硬膜下与蛛网膜下腔出血，"
        "其电极都与血管碰撞或在 1 mm 内擦过；术前 DSA 预测术后影像学出血的**敏感度 94.7%**。",
        "常规手术靠**切开硬膜、直视皮层**来控制这个变量。保留硬膜，这条路就没了——"
        "所以必须换一种隔着膜看见血管的办法。那是下一期。",
    ],
    P("15-dsa.png"), figure_height=520,
)

# 16 尾卡
gen.tail_card(
    [
        "① McGovern RA, et al. Risk analysis of hemorrhage in stereo-electroencephalography "
        "procedures. Epilepsia. 2019;60(3):571–580",
        "② Obaid A, Hanna M-E, Huang S-W, et al. Ultrasensitive measurement of brain penetration "
        "mechanics and blood vessel rupture with microscale probes. PNAS. 2026;123(13):e2529147123",
        "③ Szymanski LJ, et al. Neuropathological effects of chronically implanted, intracortical "
        "microelectrodes in a tetraplegic patient. J Neural Eng. 2021;18:0460b9",
        "④ Schachtrup C, et al. Fibrinogen triggers astrocyte scar formation by promoting the "
        "availability of active TGF-β after vascular damage. J Neurosci. 2010;30(17):5843–5854",
        "⑤ Saxena T, et al. Biomaterials. 2013;34(20):4703–4713",
        "⑥ Biran R, Martin DC, Tresco PA. Exp Neurol. 2005;195(1):115–126",
        "⑦ Solarana K, et al. Neurophotonics. 2020;7(1):015004",
        "⑧ Barrese JC, et al. J Neural Eng. 2013;10(6):066014",
        "⑨ Stefanelli A, et al. World Neurosurg. 2022;164:e964–e969",
        "⑩ StatPearls《Epidural Hematoma》《Subdural Hematoma》",
        "",
        "图 8 引自 ②；第 10、11 张的针径为本人在 Neuralink 官方视频帧上按标尺自测，非公开数值。"
        "各项研究的物种已在正文逐条标明。",
    ],
    P("16-refs.png"),
    lead_paragraphs=[
        "下一期：隔着一层不透明的硬膜，怎么看见血管并绕开它。",
    ],
)

print("done ->", OUT)
