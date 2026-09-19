# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, ".claude/skills/dailybci/scripts")
from card_generator import CardGenerator

OUT = "output/2026-09-19-digital-fly"
P = "output/2026-09-19-digital-fly/figs"
os.makedirs(OUT, exist_ok=True)
gen = CardGenerator(date="2026.09.19")

# 01 封面
gen.cover_card(
    "赛博果蝇做到了什么", "还差什么（上）",
    "连接组算得准的那一格，边界在哪里。",
    f"{OUT}/01-cover.png",
    source="2024 年 10 月《Nature》Shiu 等人论文 · 本期为该文与相关演示的解读",
    concept_image=f"{P}/fig2c.png", concept_height=480, title_size=96, title_top=90)

# 02 目录
gen.figure_card(f"{P}/fig-toc.png", "目录与来源", [
    "来源：2024 年 10 月发表于《Nature》的论文《A Drosophila computational brain model reveals sensorimotor processing》，作者 Shiu、Sterne 等，末位作者 Kristin Scott（加州大学伯克利分校分子与细胞生物学系、Helen Wills 神经科学研究所）。方法：用 FlyWire 成年雌果蝇全脑连接组建漏积分发放模型，预测味觉与理毛环路，再用光遗传学在活体果蝇上检验。",
    "另引用 Eon Systems 2026 年 3 月的技术说明与 DOOMFLY 开源仓库。",
], f"{OUT}/02-toc.png", figure_height=560, annot_size=27)

# 03 ① DOOM 钩子
gen.text_card(None, [
    "2026 年 9 月 9 日，软件工程师 Alex Wormuth 把一份果蝇连接组（connectome，神经元之间连接关系的整体图谱）接进了 DOOM。每一帧游戏画面转成 **3,335** 个亮度输入与 **811** 个颜色输入，送进 166,700 个神经元、25,582,938 条连接的网络；活动再映射成转向、前进和开火¹。",
    "学习也实现了。果蝇受伤时，程序给两个 PPL101 多巴胺神经元注入 200 ms 电流，据此改变 **4,184** 条 KC→MBON11 连接的强度¹。这条通路是真实果蝇嗅觉学习的所在。",
    "他自己给出的结论写在项目首页：**未能证明学会生存**；视觉、条件化、生存三项验证全部未通过¹。",
    "同一周的新闻标题是「果蝇大脑学会了打 DOOM」。而这件 9 月的事，和今年 3 月刷屏的那只会走路的虚拟果蝇，并不是同一个项目。",
], f"{OUT}/03-hook.png", heading_lines=["① 他给果蝇大脑接上了 DOOM，", "然后自己判定失败"])

# 04 ① 两条线
gen.figure_card(f"{P}/fig-lineage.png", "自制示意图", [
    "如上图，果蝇连接组有两条独立的线。上面一条从 2018 年的 FAFB 开始：连续切片透射电镜把一只成年雌果蝇的整个脑切成片逐张成像²，切片方向分辨率 40 nm，切片还会破损、错位。它一次覆盖全脑，当年的算法却分割不了这么脏的数据，直到卷积网络解决对齐问题、再加上逐条人工校对，2024 年才有完整的 FlyWire 连接组：**139,255 个神经元**³。",
    "下面一条用聚焦离子束扫描电镜：离子束削掉样品表面极薄一层，扫描电镜对新露出的块面成像，如此循环。三个方向都是 8 nm，机器可直接分割；它一次只能处理很小一块，所以 2020 年先出来的 hemibrain **只覆盖中央脑的一部分，没有视叶**⁴。",
], f"{OUT}/04-lineage.png", figure_height=470, title="① 两条独立的线，两种扫描方式")

# 05 ① 三件事
gen.text_card(None, [
    "2024 年 10 月是第一步。加州大学伯克利分校 Kristin Scott 组的 Shiu 等人在 FlyWire 那份连接组上建了脑模型，算出糖刺激到取食的反应⁶。这一步只有脑，没有身体。",
    "2026 年 3 月是第二步。Eon Systems 的演示**用的还是同一份连接组、同一个脑模型**⁷，新加的是身体：NeuroMechFly v2 的 **87 个关节**，跑在 MuJoCo 物理引擎里，让感觉输入与动作首尾相接。会走路、理毛、进食的那只果蝇是这一件，里面没有新的扫描。",
    "上一张卡的 DOOM 落在另一条线上，用的是 MaleCNS，与 Shiu 的脑模型无关¹。",
    "所以要追的对象只有一个：在 FlyWire 这条线上，结构信息究竟能还原哪些行为。",
], f"{OUT}/05-three.png", heading_lines=["① 三件事，", "分别落在这两条线上"])

# 06 ② 补的三样
gen.text_card(None, [
    "连接组只说谁连谁、连了几个突触，不含任何随时间变化的量。要让它跑起来，Shiu 等人另外补了三样⁶。",
    "连接的符号——兴奋还是抑制，来自对每个神经元递质身份的机器学习预测，从电镜图像本身推出来⁸。",
    "连接的强度——突触数量乘一个全局参数，取 **0.275 mV**。这是模型里唯一的自由参数，由**拟合**一个已知的行为结果定出来，**不是测量值**⁶。",
    "神经元的动力学——静息电位 −52 mV、发放阈值 −45 mV、不应期 2.2 ms、突触衰减时间常数 5 ms、从发放到下游电位改变的延迟 1.8 ms⁶。",
    "这组参数对模型纳入的 **127,400 个**已校对神经元统一取值，不区分细胞类型；而果蝇脑内已标注出 8,453 个细胞类型⁹，它们的膜特性并不相同。",
], f"{OUT}/06-rules.png", heading_lines=["② 连接组是静态的，", "让它跑起来的规则是选定的"])

# 07 ② 相互作用（Fig 1a）
gen.figure_card(f"{P}/fig1a.png", "Shiu et al. 2024, Fig. 1a", [
    "网络层面没有另外一个模型。漏积分发放（leaky integrate-and-fire）既是单神经元模型，也是相互作用模型⁶。",
    "如上图左，灰色神经元分别经 **80** 个和 **40** 个突触连到绿色与紫色神经元；右图里绿线被推高的幅度约是紫线的两倍，与突触数量成比例。每次推高之后按 5 ms 的时间常数衰减，所以第二串输入要在几毫秒内先后到达才叠加得起来，绿线由此越过顶部虚线标出的阈值并复位。",
    "所有上游输入在胞体处线性相加。论文写明由此忽略了神经元形态与树突计算；模型也不含缝隙连接、内部状态与长程神经肽，并**假设每个神经元的基础放电为零**⁶。",
], f"{OUT}/07-lif.png", figure_height=400, title="② 相互作用全部由这一条规则决定")

# 08 ③ 细胞类型
gen.text_card(None, [
    "上一节里模型对全部神经元用同一组参数，而果蝇脑内已标注出 8,453 个细胞类型（cell type）⁹。这些类型按什么划分，决定了后面所有实验的单位。",
    "传统做法按形态：树突和轴突分别伸进哪几个脑区、分支形状如何，再结合发育谱系（hemilineage，同一个神经母细胞分裂出来的一组神经元）与递质身份。",
    "有了两份连接组之后，Schlegel 等人给出了一个可操作的定义⁹：**一个细胞类型，是这样一组细胞——其中每一个，与另一只果蝇脑里某个细胞的相似度，都高于它与同一只脑里任何其他细胞的相似度。**",
    "这个判据要求一个类型必须跨个体可重认，执行它需要两只脑。执行的结果是，hemibrain 提出的类型里**约三分之一**在 FlyWire 里无法可靠重认⁹。",
], f"{OUT}/08-celltype.png", heading_lines=["③ 细胞类型的判据是", "「在另一只脑里还能被认出来」"])

# 09 ③ 模型侧
gen.text_card(None, [
    "检验从一个可判定的单点开始：果蝇尝到糖会伸喙（proboscis extension），喙的第一节由运动神经元 **MN9** 控制。整条通路因此被压成一个二值问题——MN9 发不发放。",
    "模型侧的操作：选定一个细胞类型，给它包含的全部神经元泊松分布的输入，使平均发放率达到 **50 Hz**；其余神经元不加任何驱动。每个实验跑 **30 次、每次 1,000 ms**⁶。",
    "读出只有一个量：MN9 的发放率。判据是**大于 0 Hz** 就算「预测会伸喙」⁶。",
    "这条判据依赖上一节那个假设——模型里每个神经元的基础放电被设为零。既然没有自发活动，MN9 只要发放过，就只能是这次驱动传过去的结果。",
], f"{OUT}/09-model-side.png", heading_lines=["③ 在模型里一次只驱动一个细胞类型，", "只读一个神经元"])

# 10 ③ 去抑制
gen.figure_card(f"{P}/fig-disinhibition.png", "自制示意图", [
    "论文举了一个自己没预测对的例子⁶：Phantom 这个细胞类型，模型判它不激活 MN9，实验里它引起了伸喙。论文的解释是，Phantom 与它强烈投射的 Scapula 都被判为抑制性，压住 Scapula 反而放开了下游。这是去抑制。",
    "如上图，去抑制要起作用，前提是先有抑制在那里。上排里只有 Phantom 被驱动，Scapula 发放率为零，把零再压低仍是零；下排的真实果蝇里 Scapula 平时就在抑制下游，压住它喙才伸出来。把这次漏报归因到这条假设是本篇的推断，论文未如此表述。",
], f"{OUT}/10-disinhibition.png", figure_height=465, title="③ 把基础放电设为零，去抑制就算不出来")

# 11 ③ 真果蝇侧
gen.text_card(None, [
    "模型的预测要拿到活体上验。用 split-GAL4 品系把同一个细胞类型标记出来，让这些神经元表达 CsChrimson——一种光门控阳离子通道，受光照时通道打开、细胞去极化⁶。",
    "随后用 635 nm 激光照射，记录果蝇在 **5 秒内**有没有伸喙。筛查时每个基因型测 **10 只**果蝇，实验对基因型设盲⁶。",
    "这里有一处不对称：模型给出的是 MN9 的发放率，果蝇给出的是伸喙这个动作。两者对接的依据是 MN9 控制喙的第一节，因此把「第一节伸出」当作 MN9 被激活的读出⁶。这批筛查没有同时记录 MN9 的电活动来直接验证这个对应关系。",
], f"{OUT}/11-fly-side.png", heading_lines=["③ 在真果蝇里用光让同一类细胞放电，", "看 5 秒内伸不伸喙"])

# 12 ③ 比对结果
gen.figure_card(f"{P}/fig2ab.png", "Shiu et al. 2024, Fig. 2a–b", [
    "候选来自 SEZ（食道下区）split-GAL4 品系库的 138 个细胞类型，作者在 FlyWire 里认出其中 **106 个**⁶；挑选与模型的预测无关。",
    "如上图，图 a 是模型算出的 MN9 发放率并按高低排序，图 b 是同一顺序下真果蝇伸喙的比例。左端几根高柱两图对应得上，右端出现了图 a 为零、图 b 不为零的几根。",
    "论文给出的数：预测会激活 MN9 的 **11 个**里 **10 个**真的伸了喙；预测不会的 **95 个**里 **4 个**其实会⁶。",
], f"{OUT}/12-compare.png", figure_height=540, title="③ 106 个细胞类型的比对结果")

# 13 ③ 统计
gen.figure_card(f"{P}/fig-baseline.png", "自制示意图", [
    "由上面四个数可以把 106 个类型全部归位：真的会伸喙的只有 **14** 个，不会的有 **92** 个。也就是说，这道题的正确答案里「不会」占了 86.8%。",
    "如上图，构造一个不做任何计算的规则——一律回答「不会」——它的准确率就有 **86.8%**。模型的准确率是 **95.3%**，两者相差 9 题：模型在 14 个真阳性里抓到 10 个，同时误报 1 个。",
    "所以描述它的能力要用两个分开的量：说「会」的 11 个里 10 个是对的（**90.9%**），真的会的 14 个里找到 10 个（**71.4%**）。以上比例与基线均由论文给出的 11／10／95／4 计算，论文未直接列出。",
], f"{OUT}/13-baseline.png", figure_height=470, title="③ 一行计算都不做，准确率也有 86.8%")

# 14 ④ 人接上去的那一段
gen.text_card(None, [
    "真果蝇里，脑不直接连到腿部肌肉。脑通过下行神经元（descending neurons）把指令送到腹神经索（ventral nerve cord）——相当于脊髓的结构——腿的运动神经元与产生节律性步态的环路都在那里。",
    "Shiu 模型用的 FlyWire 连接组只有脑，没有腹神经索³。从「脑模型算出某些神经元在发放」到「虚拟果蝇迈出一步」，这一段在模型里是空的。",
    "Eon 把它手工搭了起来：选定 **7 条下行通路**，分别对应转向、前进速度、理毛、取食与逃逸⁷。身体是按真实果蝇 X 射线显微断层扫描建成的 87 关节力学模型，关节运动、脚与地面的接触摩擦以及交互之后的力学结果，全部由 MuJoCo 计算，而不是预先做好的动画。脑与身体每 **15 ms** 同步一次⁷。",
    "Eon 写明这些映射由人选定，不从连接组推出；真实果蝇的下行神经元有一千多条，这里用了 7 个接口⁷。",
], f"{OUT}/14-body.png", heading_lines=["④ 脑模型不直接控制关节，", "中间那一段是人接上去的"])

# 15 ④ 两种证据
gen.text_card(None, [
    "上一节里，模型输出与实验观察之间只隔一个解剖事实：MN9 控制喙的第一节。这条链短，每一步都有依据，预测因此可证伪——模型说会、果蝇不伸，就是错了。",
    "这一节的链长得多：脑模型 → 人工选定的 7 条映射 → 身体控制器 → 物理引擎 → 动作。中间两层都不来自连接组。步态是否自然，很大程度上由身体模型与控制器决定；映射换一种选法，同一个脑模型能产出完全不同的动作。",
    "所以两节给出的证据强度不同。前者是一个可证伪的预测，在别的果蝇身上被检验，结果能用数字说清；后者是一套能持续运行、不崩溃、看上去合理的闭环系统，属于工程结果。",
    "Eon 自己也没有主张后者等于前者：技术说明里写了映射由人选定、下行接口只有 7 个、尚未针对头朝向环吸引子与中枢模式发生器做验证⁷。",
], f"{OUT}/15-evidence.png", heading_lines=["④ 动作逼真，", "与脑模型算得准是两件事"])

# 16 收束
gen.text_card(None, [
    "**能主张的**：在不涉及学习的快速感觉—运动这一格里，只用结构加递质符号给出的预测有真实分辨力。说「会」的时候基本可信，说「不会」的时候会漏掉约三成；而且这套预测是在**别的果蝇**身上被检验的——连接组取自一只被固定、切片、扫描的雌果蝇，验证却做在另外几十只活果蝇身上⁶。",
    "**不能主张的**：视频里那些行走、理毛、进食，目前还不能算「由连接组还原出来的行为」——中间两层不来自连接组。这套验证方式按设计也看不见个体经历带来的差异：能被它记为「对」的，只有在个体之间可重复的那部分反应。",
    "下一期回答两个问题：漏掉的那三成里，还有哪些机制是被假设排除掉的；以及要解释同一只果蝇在饿与不饿时的不同反应，需要补测什么。",
], f"{OUT}/16-closing.png", heading_lines=["⑤ 能主张什么，", "不能主张什么"])

# 17-18 尾卡
refs1 = [
 "¹ Wormuth A. (2026). DOOMFLY 开源仓库与训练协议. github.com/nftechie/doomfly.",
 "² Zheng Z, et al. (2018). A complete electron microscopy volume of the brain of adult Drosophila melanogaster. Cell 174:730–743.",
 "³ Dorkenwald S, et al. (2024). Neuronal wiring diagram of an adult brain. Nature 634:124–138.",
 "⁴ Scheffer LK, et al. (2020). A connectome and analysis of the adult Drosophila central brain. eLife 9:e57443.",
 "⁵ Berg S, et al. (2026). Sexual dimorphism in the complete Drosophila male central nervous system connectome. Cell.",
]
refs2 = [
 "⁶ Shiu PK, et al. (2024). A Drosophila computational brain model reveals sensorimotor processing. Nature 634:210–219.",
 "⁷ Eon Systems. (2026). How the Eon Team Produced a Virtual Embodied Fly. 技术说明.",
 "⁸ Eckstein N, et al. (2024). Neurotransmitter classification from electron microscopy images at synaptic sites in Drosophila melanogaster. Cell 187:2574–2594.",
 "⁹ Schlegel P, et al. (2024). Whole-brain annotation and multi-connectome cell typing of Drosophila. Nature 634:139–152.",
]
gen.tail_card(refs1, f"{OUT}/17-tail1.png", lead_paragraphs=[
 "把这套方法被证明有效的条件写清楚，本身就说明了它现在能主张什么。下一期从漏掉的那三成开始。"])
gen.tail_card(refs2, f"{OUT}/18-tail2.png")
print("done")
