"""第一期:谁真正需要脑机接口 —— 图卡装配。
卡片标题与目录卡逐条对应(① ~ ⑦),便于读者导航。
"""
import os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(SCRIPT_DIR))
from card_generator import CardGenerator

PROJECT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-08-10-vision-layers")
FIGS = os.path.join(OUT, "figs")
PAPERS = os.path.join(PROJECT, "papers")
os.makedirs(OUT, exist_ok=True)

g = CardGenerator(date="2026.08.10")
P = lambda *a: os.path.join(*a)


# 01 封面
g.cover_card(
    "有一类失明", "只剩脑机接口",
    "一半以上的失明靠手术或眼镜就能解决。脑机接口对准的是剩下的一小格：视神经已经损坏，眼球内部再无介入点。",
    P(OUT, "01-cover.png"),
    concept_image=P(PAPERS, "cover-cand-3brains.png"),
    concept_height=430, title_size=132, title_top=110,
)

# 02 目录 + 来源
g.figure_card(
    P(FIGS, "toc.png"), "本期路线",
    ["本期不解读单篇论文。数据来自全球疾病负担研究视力损害组（**Lancet Global Health, 2021**）"
     "等 16 项来源，逐条列于尾卡。",
     "封面图为人类视皮层的三种解剖视图，白色虚线框标出 96 通道微电极阵列的植入位置，"
     "取自 Fernández 等 2021 年 **J Clin Invest**。"],
    P(OUT, "02-toc.png"), figure_height=640,
)

# 03 ①
g.figure_card(
    P(PAPERS, "prima-cover-fig.png"), "Fig. 1 · Holz et al., N Engl J Med 2026",
    ["在 2026 年发表的一项试验中，一块植入视网膜下的芯片让 **32 名参与者中的 26 人**（81%）"
     "视力显著改善，该系统正在申请欧洲上市¹。",
     "如上图，这套系统叫 PRIMA：左侧是配套眼镜，摄像头把图像交给投影模块，以近红外光投射到"
     "植入体上；中间是植入位置，芯片本体 **2 毫米见方、厚 30 微米**，放在视网膜下方已经萎缩的区域；"
     "上方的剖面图标出信号去向——光转成电流后刺激视网膜，再经**视神经**传出。",
     "这是当下最好的成绩。它能成立有一个前提：芯片刺激的是视网膜内层的双极细胞，"
     "因此要求这些细胞与它们下游的通路仍然完好。不满足这个前提的人有多少，要先看全球盲人的病因构成。"],
    P(OUT, "03-prima.png"), figure_height=430,
    title="一块视网膜下芯片做到了什么", title_num="①",
)

# 04 ②
g.figure_card(
    P(FIGS, "fig-causes.png"), "全球致盲病因分布",
    ["2020 年全球 50 岁及以上盲人共 **3360 万**，占比最大的两类病因已有成熟解决办法。",
     "如上图，**白内障 1520 万人、45.2%**，手术即可复明；**未矫正屈光不正 230 万人、6.8%**，"
     "一副眼镜即可。两项合计**超过一半**，限制因素是医疗资源可及性²。",
     "占 **29.3%、984 万人**的「其他 / 未指明」里，包含调查未指明病因的个案，"
     "以及沙眼、角膜疾病等数据有限的病因²，眼外伤也在其中。而位置才决定能用什么办法。"],
    P(OUT, "04-causes.png"), figure_height=545,
    title="3360 万盲人的病因分布", title_num="②",
)

# 05 ③
g.figure_card(
    P(FIGS, "fig-pathway.png"), "损伤部位与病因的对应",
    ["这些病因损坏的部位分布在整条通路上，位置不同，方案完全不同。",
     "如上图，**青光眼损坏的是神经节细胞及其轴突，也就是视神经**。这条通路上的约束贯穿全部方案："
     "**干预只能作用在损伤的下游。**",
     "由此得到一条推论：**青光眼致盲者用不了任何一种视网膜假体**——信号都要经神经节细胞传出。"
     "Argus II 的试验正是把青光眼列为排除标准³。"],
    P(OUT, "05-pathway.png"), figure_height=610,
    title="坏的部位不在同一处", title_num="③",
)

# 06 ④
g.figure_card(
    P(FIGS, "fig-layers.png"), "各层的现有方案与成熟度",
    ["按损伤部位从外向内排列，方案的成熟度依次下降。如上图，基因治疗只适用于携带双等位 RPE65 "
     "突变的患者：这类突变约占 Leber 先天性黑矇的 **2–16%**、视网膜色素变性的 **2% 以下**，"
     "而两病本身的患病率仅为每 10 万人 **1.2–2.4 例**与 **11–26 例**⁴。",
     "于是判断一个人能用什么，归成依次三问：**有没有成熟的常规办法**；**靶细胞还活着吗**；"
     "**损伤下游还剩什么**。还有一类病因不遵守这种分层。"],
    P(OUT, "06-layers.png"), figure_height=615,
    title="越往通路内侧，办法越少", title_num="④",
)

# 07 ⑤
g.figure_card(
    P(FIGS, "fig-trauma.png"), "眼外伤的跨层损伤",
    ["眼外伤不限于某一层，一次事故可以同时损坏多个部位。如上图，最外两层的办法与非外伤病因相同；"
     "**外伤性视神经病变没有有效治疗，眼球摘除后没有任何眼内方案。**",
     "下方那三个数是证据：**单纯观察组反而最高**⁶。而因外伤致盲的人数，至今仍只有 1998 年的"
     "估计：约 **160 万人**⁸——这些人与青光眼晚期患者处境相同，眼球内部已无介入点。"],
    P(OUT, "07-trauma.png"), figure_height=590,
    title="眼外伤", title_num="⑤",
)

# 08 ⑥
g.text_card(
    "",
    ["视神经上做过人体尝试。1998 年起，一名因视网膜色素变性致盲的志愿者被慢性植入了"
     "环绕视神经的螺旋袖套电极。经过训练，他能识别简单图形，正确率达 **85%**，"
     "但平均每个图形需要 **54 秒**⁹；另一组任务中识别率为 63%、耗时 60 秒¹⁰。"
     "这条路线此后没有推进到更大规模。",
     "更关键的一点是适应症：这名志愿者的病因是视网膜色素变性，"
     "**他的神经节细胞与视神经本身是完好的**。刺激视神经同样要求视神经完好，"
     "因此这条路线并不能覆盖青光眼或视神经损伤的患者——它没有扩大适用范围。",
     "外侧膝状体曾被提出作为靶点，猕猴的微刺激实验能产生可预期的视觉感知，但至今没有人体试验。",
     "眼球内部、视神经、外侧膝状体依次排除之后，通路上还剩最后一站。"],
    P(OUT, "08-optic-nerve.png"),
    heading_lines=["⑥ 视神经与外侧膝状体", "至今空白的两站"],
)

# 09 ⑦
g.figure_card(
    P(FIGS, "fig-scale.png"), "被跳过的那一层有多大",
    ["对这部分患者，直接刺激初级视皮层是通路上唯一剩下的介入位置。它跳过眼球与视神经，"
     "用电流激活视皮层神经元产生光幻视，**对病因不作要求**。",
     "如上图，人眼约 **9200 万视杆 + 460 万视锥**¹¹输出到 **70 万–150 万神经节细胞**¹²，"
     "中央凹几乎不汇聚、周边大幅汇聚，传出的是局部对比度而非亮度。绕过视网膜，这些处理"
     "全要由软件重做，而人体皮层阵列只有 **96 个电极**¹³。",
     "所以它不是更好的方案，而是唯一可能的方案。"],
    P(OUT, "09-scale.png"), figure_height=520,
    title="只剩初级视皮层", title_num="⑦",
)

# 10 收尾 + 下期预告
g.text_card(
    "",
    ["按上面的顺序看下来会出现一个不对称：占比最大的病因早已解决，而剩下最难的那一格，"
     "患者数量并不大。皮层视觉假体面对的正是这一格。它值得做的理由不是市场规模，"
     "而是对这些人来说没有第二条路。",
     "同时要说清的是，这一格至今仍是空的。**存在唯一的路径，与这条路径已经走通，是两件事。**",
     "**本期局限**：病因分布的拆分只覆盖 50 岁及以上人群；眼外伤的全球致盲人数仍依赖 1998 年的估计；"
     "各病因占比为按原文人数自行计算。",
     "**下一期 · 电刺激视皮层，究竟能做到什么**",
     "· 电流为什么能让人「看见」，光幻视到底是什么",
     "· 为什么 58 年过去，人体端仍停在简单形状——三条硬约束",
     "· 现有系统走到哪一步：CORTIVIS、Orion 的六年随访、ICVP、Neuralink Blindsight"],
    P(OUT, "10-closing.png"),
    heading_lines=["这一格至今仍是空的"],
)

# 11 参考文献 A
g.tail_card(
    ["¹ Holz FG, et al. (2026). Subretinal photovoltaic implant to restore vision in geographic atrophy due to AMD. N Engl J Med 394:232–242.",
     "² GBD 2019 Blindness and Vision Impairment Collaborators. (2021). Causes of blindness and vision impairment in 2020 and trends over 30 years. Lancet Glob Health 9:e144–e160.",
     "³ ClinicalTrials.gov NCT00407602. Argus II Retinal Stimulation System Feasibility Protocol.(来源层级:临床试验注册记录)",
     "⁴ Sallum JMF, et al. (2022). Epidemiology of mutations in the RPE65 gene-mediated inherited retinal dystrophies. Adv Ther 39:1179–1198.",
     "⁵ Sahel JA, et al. (2021). Partial recovery of visual function in a blind patient after optogenetic therapy. Nat Med 27:1223–1229.",
     "⁶ Levin LA, et al. (1999). The treatment of traumatic optic neuropathy: the International Optic Nerve Trauma Study. Ophthalmology 106:1268–1277.",
     "⁷ Li C, et al. (2023). The global incidence and disability of eye injury: an analysis from the Global Burden of Disease Study 2019. eClinicalMedicine 62:102134."],
    P(OUT, "11-refs-a.png"),
)

# 12 参考文献 B
g.tail_card(
    ["⁸ Négrel AD, Thylefors B. (1998). The global impact of eye injuries. Ophthalmic Epidemiol 5:143–169.",
     "⁹ Brelén ME, et al. (2005). Creating a meaningful visual perception in blind volunteers by optic nerve stimulation. J Neural Eng 2:S22–S28.",
     "¹⁰ Veraart C, et al. (2003). Pattern recognition with the optic nerve visual prosthesis. Artif Organs 27:996–1004.",
     "¹¹ Curcio CA, et al. (1990). Human photoreceptor topography. J Comp Neurol 292:497–523.",
     "¹² Curcio CA, Allen KA. (1990). Topography of ganglion cells in human retina. J Comp Neurol 300:5–25.",
     "¹³ Fernández E, et al. (2021). Visual percepts evoked with an intracortical 96-channel microelectrode array inserted in human occipital cortex. J Clin Invest 131:e151331.",
     "¹⁴ Chen X, et al. (2020). Shape perception via a high-channel-count neuroprosthesis in monkey visual cortex. Science 370:1191–1196."],
    P(OUT, "12-refs-b.png"),
)

print("cards written to", OUT)
