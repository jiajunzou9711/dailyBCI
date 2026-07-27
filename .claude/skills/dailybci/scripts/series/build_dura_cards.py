# -*- coding: utf-8 -*-
"""Build 小红书 cards for series ① — 硬脑膜：所有入脑手术的第一道关."""
import sys, os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(SCRIPT_DIR))
from card_generator import CardGenerator

PROJECT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "series-dura-01")
FIG = os.path.join(OUT, "figs")
os.makedirs(OUT, exist_ok=True)

gen = CardGenerator(date="2026.07.27")
P = lambda n: os.path.join(OUT, n)
F = lambda n: os.path.join(FIG, n)

# 01 封面
gen.cover_card(
    "硬脑膜",
    "所有入脑手术的第一道关",
    "这层膜只有零点几毫米,却让神经外科几十年不敢绕开。",
    P("01-cover.png"),
    source="硬脑膜的解剖与力学专题。以 2026 年 6 月 Neuralink 公布的经硬膜植入手术为切入,"
           "内容依据硬膜厚度、力学与跨物种比较的同行评议文献。",
)

# 02 目录
gen.figure_card(
    F("toc.png"), "本期路线",
    ["顺着这六步走完,你会自己判断出「不切硬膜」这件事到底难在哪。"],
    P("02-toc.png"), figure_height=620,
)

# 03 What
gen.text_card(
    "先说一件刚发生的事",
    [
        "任何要进到脑子里的操作——植入电极、取活检、放引流管——第一关都是同一层东西:**硬脑膜**。它是包在脑外面最外、最韧的一层膜。",
        "几十年来的标准做法是把它切开、并**移除一小块**,露出脑表面再操作。2026 年 5 月,Neuralink 在多伦多做了一台手术,**第一次没有切它**,让电极丝直接穿了过去¹。",
        "那么问题来了:不切它,到底难在哪?",
    ],
    P("03-what.png"),
)

# 04 Why
gen.text_card(
    "为什么值得把这层膜讲透",
    [
        "要回答「不切它难在哪」,得先知道这层膜是什么。",
        "切不切这一刀,决定的是创伤大小、感染窗口、手术能不能重复、以及能不能规模化。但「不切」到底了不起在什么地方,**取决于这层膜的物理性质**——它多厚、多硬、什么结构。",
        "不知道这些,就只能跟着新闻说一句「重大突破」。所以这一期先把这层膜讲透。",
    ],
    P("04-why.png"),
)

# 05 它在哪一层
gen.figure_card(
    F("gray769-pia.png"), "颅顶冠状切面（Gray's Anatomy, 1918）",
    [
        "先定位。从头皮往里走,依次是:皮肤 → 帽状腱膜 → 骨膜 → 颅骨 → **硬脑膜** → 蛛网膜 → 软脑膜。",
        "如上图,**红线是软脑膜**,它紧贴皮层表面,每一条脑沟都钻进去再折回来;**黄色是硬脑膜**,它在外面平铺,直接从脑沟上方跨过去。",
        "硬脑膜和软脑膜最核心的差别在**贴合方式**:一个贴着脑组织走,一个在外面架着。",
    ],
    P("05-where.png"), figure_height=520,
)

# 06 它其实是两层
gen.figure_card(
    F("gray769-sinus.png"), "上矢状窦区域放大（黄=硬脑膜，蓝=静脉腔）",
    [
        "在外面架着的这层膜,本身还有一个结构。硬脑膜由两层贴合而成:外层叫骨内膜层,本质上就是**颅骨内表面的骨膜**;内层叫脑膜层。活体 OCT 能把两层分别量出来²:**120 µm + 132 µm**。",
        "如上图,黄色的硬膜在中央的静脉腔位置分成上下两片、把腔夹在中间,这就是两层的直接图示。",
        "平时两层融合成一张,但界面确实存在——Chiari 畸形的「硬膜劈开减压」术式就是**只切外层、保留内层完整**³。",
    ],
    P("06-two-layers.png"), figure_height=520,
)

# 07 有多厚
gen.text_card(
    "它到底多厚",
    [
        "既然两层加起来才零点几毫米,那它究竟多厚?",
        "三种测法,三个数:活体 OCT 测得²**216 µm**、组织学切片测得⁴**564 ± 50 µm**、尸体拉伸测得⁵**680 ± 200 µm**。差异来自部位、在体张力、死后时间和测量原理,目前没有文献直接比较并给出定论。",
        "可以负责任地说的是:颅内硬膜在零点几毫米量级,跨研究大致落在 **0.2–1.4 mm** 之间。以后凡是看到「硬膜多厚」这个数,先问它是怎么测的。",
    ],
    P("07-thickness.png"),
)

# 08 有多硬
gen.text_card(
    "它有多硬",
    [
        "厚度只是一半,另一半是这层膜的力学性能。",
        "汇总 11 项研究、448 份新鲜样本的合并估计:弹性模量 **68.1 MPa**、极限抗拉强度 **7.2 MPa**、最大力时应变 **14.4%**⁶。作为对照,它保护的脑组织本身在 kPa 量级⁷——硬膜比脑组织硬约**四个数量级**。",
        "三个数里最关键的是最后一个。断裂应变只有 **11–14%**⁵ ⁶:要让这层膜破,必须在局部把它拉伸到这个程度。达不到,膜只会变形,不会破。",
    ],
    P("08-stiffness.png"),
)

# 09 各向异性
gen.figure_card(
    F("fig-aniso.png"), "示意图（自制）",
    [
        "而且这层膜的「硬」还分方向。硬脑膜是胶原纤维增强结构。",
        "如上图,沿纤维方向拉,力由胶原直接承担,模量高;垂直纤维方向拉,承力的是纤维之间的基质,模量低。同一块颅内硬膜实测 **193 MPa 与 73 MPa**,差 **2.6 倍**⁸。",
        "这直接决定针该怎么进:针的斜面**垂直于纤维走向**时,穿透所需的力和功都显著更大⁹。",
    ],
    P("09-anisotropy.png"), figure_height=640,
)

# 10 它是活组织
gen.text_card(
    "它是活组织,不是包装",
    [
        "讲完力学,还有一件容易被忽略的事。",
        "硬脑膜有自己的**动脉血供**(脑膜中动脉及其分支),也有**痛觉神经支配**。这里要纠正一个常见误解:脑组织本身没有痛觉感受器,但硬脑膜有——牵拉或破坏它会产生明确的痛觉。",
        "另一个误解是「硬膜负责密封脑脊液」。真正的屏障是**蛛网膜屏障细胞层**(细胞间有大量紧密连接),硬膜自身的血管反而是有孔的¹⁰。硬膜承担的是力学上的容器壁。",
    ],
    P("10-living-tissue.png"),
)

# 11 手术里怎么处理
gen.figure_card(
    F("fig-craniotomy.png"), "示意图（自制）",
    [
        "那在真实手术里,这层膜是怎么被处理的?",
        "如上图②,开颅铣刀下端有一块**脚板**,伸在颅骨与硬膜之间托着膜、隔开刀刃,而且脚板前端略向后仰,一边锯一边就在把硬膜从骨内板上剥离¹¹。到了③,骨瓣被整块取走,**硬膜两层原封不动地留在脑这一侧**。",
        "这一步做得到,是因为骨内膜层与颅骨内板之间本就是骨膜与骨的正常附着,相对疏松。",
    ],
    P("11-craniotomy.png"), figure_height=620,
)

# 12 一个反常识 + 悬吊线
gen.figure_card(
    F("fig-tackup.png"), "示意图（自制）",
    [
        "骨瓣拿走之后,出现了一个原本不存在的东西:颅内的「硬膜外腔」**是手术制造出来的**。正常状态下硬膜直贴颅骨,剥离之后才撑开一个腔,一旦渗血就是硬膜外血肿。",
        "所以传统做法是关颅前在骨上钻孔、用 **3-0～4-0 不可吸收线**把硬膜缝回骨缘¹¹。如上图,骨头本身不需要被缝,它只提供一个穿线的孔。",
        "有意思的是,这个做了几十年的标准步骤刚被挑战:2025 年一项 **n=490** 的多中心随机对照试验显示,择期幕上开颅**省略这一步是非劣的**(因血肿再手术 0.8% vs 0.4%)¹²。",
    ],
    P("12-tackup.png"), figure_height=480,
)

# 13 物种差异
gen.figure_card(
    F("fig-species.png"), "示意图（自制，数据来自跨物种组织学研究）",
    [
        "讲到这里会有一个自然的疑问:这些为什么不先在动物身上做?",
        "因为动物的硬膜跟人不是一个量级。如上图,人 **564 µm**,大鼠只有 **49 µm**,差 **11.5 倍**⁴;猪 304 µm 是最接近的动物模型,也只有人的一半左右。结构上差得更远——人、猪、兔可分辨出多个纤维血管层,大鼠、绵羊、山羊、马只有**单一一层**⁴。",
        "非人灵长类也不够近:人与恒河猴的直接对照显示,**人的硬膜显著更硬、更厚**,纤维束更粗更密¹³。",
    ],
    P("13-species.png"), figure_height=600,
)

# 14 所以要做仿体
gen.text_card(
    "所以必须做一个人的仿体",
    [
        "动物给不了人的参数,人体又不可能拿来反复试。",
        "这就是 Neuralink 那句话的份量:他们说必须开发一整套新的测试流程,其中最关键的是做出能模拟**人硬膜厚度与穿刺力**的合成膜片,然后在台架上跑**数百次**穿刺测试¹。这是在人体手术之前,唯一能按人的参数迭代到统计意义的办法。",
        "边界也要说清楚:这个仿体的配方、标定值、与真实人硬膜的对照验证,**官方一条都没公布**。它按自述只对齐了厚度和穿刺力两项,而各向异性、分层结构、在体张力这些,公开资料无法回答。",
    ],
    P("14-phantom.png"),
)

# 15 收尾
gen.text_card(
    "那一刀原本买到三样东西",
    [
        "回到开头那个问题:不切硬膜,到底难在哪?",
        "因为「切开并移除一块硬膜」这个动作,原本一次性买到了三样东西:**进入皮层的通路**、**看得见皮层血管**、**看得见该插多深**。保住硬膜,等于这三样同时失去,必须逐一用别的手段赎回来。",
        "下一期讲第一样:一根直径 **24 µm** 的针¹⁴,怎么在一层断裂应变只有 11% 的膜上,制造出足以破膜的局部应变。",
    ],
    P("15-closing.png"),
)

# 16 尾卡 A
gen.tail_card(
    [
        "¹ Neuralink. (2026). Our First Transdural Procedure. 官方视频与 X 帖, 2026-06-30.",
        "² Hartmann K, Stein KP, Neyazi B, Sandalcioglu IE. (2021). Optical coherence tomography of cranial dura mater: Microstructural visualization in vivo. Clin Neurol Neurosurg 200:106370.",
        "³ Chiari I 硬膜劈开减压技术. Neurosurgical Review (2009); Fluids Barriers CNS 6:7 (2009).",
        "⁴ Kinaci A, et al. (2020). Histologic Comparison of the Dura Mater among Species. Comp Med 70(2):170–175.",
        "⁵ Zwirner J, et al. (2019). Mechanical Properties of Human Dura Mater in Tension. Sci Rep 9:16655.",
    ],
    P("16-tail-a.png"),
    lead_paragraphs=[
        "这一期没有讲 Neuralink 做得多好,只讲了它面对的那层膜是什么。判断一项工作的份量,前提是知道它站在什么样的约束条件里——这层膜的厚度、模量、断裂应变和纤维取向,就是那些约束条件。",
    ],
)

# 17 尾卡 B
gen.tail_card(
    [
        "⁶ Pearcy Q, et al. (2022). Systematic review and meta-analysis of the biomechanical properties of the human dura mater. Biomech Model Mechanobiol 21(3):755–770.",
        "⁷ 人脑组织力学:压痕法灰质 1.389 ± 0.289 kPa、白质 1.895 ± 0.592 kPa.",
        "⁸ Sacks MS, et al. (1998). 颅内硬膜纵向与横向拉伸性能对比.",
        "⁹ Lewis MC, et al. (2000). How much work is required to puncture dura with Tuohy needles? Br J Anaesth 85(2):238–241.",
        "¹⁰ 蛛网膜屏障细胞层与硬膜有孔血管. Acta Neuropathol (2018) 综述.",
        "¹¹ 开颅技术与硬膜悬吊线. 神经外科手术学章节.",
        "¹² Przepiorka L, et al. (2025). Dural Tenting in Elective Craniotomies: A Randomized Clinical Trial. Neurosurgery 97(5):1108–1117.",
        "¹³ Galford JE, McElhaney JH. (1970). 人与恒河猴颅内硬膜力学对比.",
        "¹⁴ Musk E, Neuralink. (2019). An integrated brain-machine interface platform with thousands of channels. J Med Internet Res 21(10):e16194.",
    ],
    P("17-tail-b.png"),
)

print("built ->", OUT)
