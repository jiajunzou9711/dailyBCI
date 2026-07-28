# -*- coding: utf-8 -*-
"""Build 小红书 cards for series ② — 不切开硬膜，把电极送进皮层."""
import sys, os, shutil
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(SCRIPT_DIR))
from card_generator import CardGenerator

PROJECT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "series-dura-02")
FIG = os.path.join(OUT, "figs")
PAPERS = os.path.join(PROJECT, "papers")
os.makedirs(OUT, exist_ok=True)

gen = CardGenerator(date="2026.07.28")
P = lambda n: os.path.join(OUT, n)
F = lambda n: os.path.join(FIG, n)
J = lambda n: os.path.join(PAPERS, n)

# 01 封面
gen.cover_card(
    "不切开硬膜",
    "把电极送进皮层",
    "常规手术要切掉一块硬膜才能看见脑。2026 年 5 月，他们第一次不切了。",
    P("01-cover.png"),
    source="Neuralink 首例经硬膜植入的工程拆解。依据官方视频字幕、2019 年 JMIR 论文，"
           "以及脑运动与脑移位的同行评议测量文献。硬脑膜专题第 ② 期。",
)

# 02 目录（整卡直出）
shutil.copyfile(F("toc.png"), P("02-toc.png"))

# 03 What
gen.figure_card(
    F("ph-model.png"), "官方视频 0:03　脑模型、颅骨与中间那层硬膜",
    [
        "常规的 Neuralink 手术分两步进入：先开颅骨取下骨瓣，再切开硬膜并**移除其中一块**，"
        "露出脑表面，机器人才能把电极丝插进去。",
        "2026 年 5 月，在加拿大多伦多 UHN，与 **Lozano 医生**合作，他们第一次跳过了后半步。"
        "颅骨照常开一个约**一枚硬币大**的窗，硬膜保持完整，电极丝直接穿过它进入皮层。"
        "官方的说法是 \"deleting the durectomy step completely\"。",
        "膜保住了，插入端的条件也随之改变。",
    ],
    P("03-what.png"), figure_height=520,
)

# 04 三个问题
gen.figure_card(
    F("fig-three.png"), "保留硬膜后，插入端要重新解决的事",
    [
        "官方把挑战分成两条：**机械上怎么穿过硬膜**，以及**隔着硬膜怎么获取信息**。"
        "第二条又分成两件——看见血管，和知道皮层有多深。",
        "本篇讲深度与穿透，外加送丝机构。血管规避（ICG 视频血管造影）留到下一期。",
    ],
    P("04-three.png"), figure_height=600,
)

# 05 Why
gen.figure_card(
    F("ph-window.png"), "官方视频 2:16　术中暴露的脑，约一枚硬币大",
    [
        "取消切除硬膜，直接收益是手术更快、创伤更小。官方给出的目标是覆盖更多有未满足医疗需求的人。",
        "更实际的一层与自动化有关。视频里的表述是 \"what steps can you delete such that "
        "you don't even need a robot to do it?\"——**先减少步骤，再谈机器人**在临床监督下完成手术。"
        "切开并移除硬膜需要术者临场判断粘连、血管走行与切口范围，这类操作难以标准化；"
        "取消它，剩下的流程才有可能交给机器。",
        "取消之后，第一个要重新回答的问题是：**针要走多深**。",
    ],
    P("05-why.png"), figure_height=520,
)

# 06 深度从哪里量到哪里
gen.figure_card(
    F("fig-gap.png"), "针要跨过的这段距离",
    [
        "先纠正一个容易出错的理解。开颅时骨瓣被取下，**窗内这块硬膜已经与颅骨内板分离**——"
        "铣刀的护板在切割过程中就把它从骨面上剥开了，之后这块硬膜只在**窗缘**保持附着。",
        "它同样没有贴在脑上。硬膜之下依次是**蛛网膜、蛛网膜下腔、软脑膜**，然后才是皮层；"
        "蛛网膜下腔充满脑脊液，皮层浮于其中。",
        "针要走的这段距离，是从硬膜顶面出发，穿过硬膜本身，再穿过这段脑脊液间隙，到达皮层表面。"
        "**这个距离不是常数。**",
    ],
    P("06-gap.png"), figure_height=560,
)

# 07 三种运动
gen.figure_card(
    F("fig-motion.png"), "植入过程中脑的三种运动",
    [
        "心跳一栏来自 **Enzmann & Pelc 1992**：10 名健康志愿者、相位对比 cine MR，"
        "**颅骨完整**状态下各脑结构的峰值位移为 0.1–0.5 mm。",
        "呼吸一栏来自 **Sloots 2020**：7T MRI 测得心跳引起的体积应变约为呼吸的 3 倍——"
        "测的是**体积应变而非位移**，两者不能直接换算。",
        "对照：电极丝上相邻记录位点的间距是 **50 µm = 0.05 mm**。心跳这一项已经是位点间距的 2–10 倍。",
    ],
    P("07-motion.png"), figure_height=600,
)

# 08 脑移位
gen.figure_card(
    F("fig-shift.png"), "Hill 等 1998，同一台手术里三个时刻的实测",
    [
        "这项测量在问：术前 MRI 说脑表面在某个位置，等真正开始做手术，它还在那儿吗？"
        "做法是把患者的头与术前 MRI 对齐，再用带跟踪的探针去碰表面，看实测位置比预测低了多少。",
        "同一台手术里碰了三次。硬膜还没切时，硬膜表面只低 **1.2 mm**——这个数落在该研究 **1–2 mm 的测量误差**里，"
        "等于测不出移动。硬膜一切开，脑表面就低了 **4.4 mm**；再过约一小时，低到 **5.6 mm**。",
        "所以这几毫米是**「切开硬膜」这个动作的后果**，主要由脑脊液流失驱动。"
        "这正是本篇关心的：不切开硬膜，这一项应当基本不发生。因果关系目前只有这一项间接证据，标为推论。",
    ],
    P("08-shift.png"), figure_height=480,
)

# 09 OCT
gen.figure_card(
    F("ph-oct.png"), "官方视频 3:16　OCT 断面上直接标着 DURA 与 CORTICAL SURFACE",
    [
        "心跳和呼吸在保留硬膜后依然存在，所以深度必须实时测。Neuralink 用的是**光学相干断层成像**"
        "（optical coherence tomography, OCT）——用低相干近红外光的干涉测距，"
        "给出组织的深度方向断面，分辨率在微米量级。",
        "官方原话：\"the distance from the dural surface to the cortex is **actively changing "
        "in the live human**\"，以及 \"OCT allows us to measure the distance from the top of "
        "the dura to the cortex with high accuracy, so we can insert our threads into the "
        "cortex with high precision\"。",
        "**边界要划清**：OCT 在官方材料里的定位是**高精度测距**，落点是「插得准」。"
        "所有一手材料中都没有「针实时跟随组织运动」这类闭环伺服的说法——那个说法只出现在科技媒体的转述里。",
    ],
    P("09-oct.png"), figure_height=420,
)

# 10 针加粗
gen.figure_card(
    F("ph-needle.png"), "官方视频 1:47　新旧插入针并排，标尺 100 µm",
    [
        "深度解决了，还剩穿透。官方讲得很直白：\"Our original needle design was **not able to "
        "reliably penetrate it**. One of the things we did was **increase the diameter of our "
        "needle just slightly**.\"",
        "时间线比那台手术更早。2025 年夏季更新讲的是**针盒在工厂里怎么装配**"
        "（术前就做好的一次性耗材，不是术中步骤）：技师把 40 µm 钨铼线**电抛光**成锥尖，"
        "再**手工**穿进套管上 60 µm 的孔——官方原话是 \"This is done manually\"，最后激光焊接。"
        "单个针盒周期约 **24 小时**、机加工件约 **350 美元**。",
        "讲到下一代针盒时，官方说 \"deleted the electropolishing setup with a **revised needle "
        "tip geometry**, which is also compatible with **inserting the threads through the "
        "dura**\"，并用漏斗结构取消了手工穿线，周期降到 30 分钟。"
        "**2025 年夏，官方就已把新针尖几何与「经硬膜插丝」绑在一起说明。**",
    ],
    P("10-needle.png"), figure_height=380,
)

# 11 钨铼
gen.figure_card(
    F("fig-material.png"), "针为什么是钨铼合金",
    [
        "屈曲临界载荷 P_cr = π²EI/(KL)² 里，除了几何量 I，还有材料的**弹性模量 E**。"
        "钨的弹性模量约 **400 GPa**，在可加工的常用金属里属最高一档。"
        "钨微电极在神经电生理里也有长期使用史，可追到 **Hubel 1957**。",
        "代价是纯钨在室温下脆：韧脆转变温度高于室温，做成几十微米的细丝后，弯折、装配、插拔都可能脆性断裂。"
        "加铼针对的正是这一条，材料学里称为「**铼效应**」。",
        "需要说明：铼效应随成分与温度变化，高铼含量下固溶强化反而可能抬高韧脆转变温度，收益并非线性。",
    ],
    P("11-material.png"), figure_height=560,
)

# 12 d^4
gen.figure_card(
    F("fig-d4.png"), "屈曲载荷对直径的四次方标度",
    [
        "「just slightly」听起来像微调，落到力学上不是。圆截面的截面惯性矩 I = πd⁴/64，"
        "代回临界载荷公式得 **P_cr ∝ d⁴**。直径涨 1.4 倍，抗屈曲能力涨到约 **4 倍**。",
        "我按官方那张图里的 100 µm 标尺量了两根针的杆径：旧针约 **43 µm**，新针约 **61 µm**。"
        "43 µm 与 2019 年论文所说的 40 µm 线材原始直径吻合。",
        "**这是本人在视频帧上的像素测量，不是公开数值**，且默认那根标尺对两幅图同时适用，仅供量级参考。",
    ],
    P("12-d4.png"), figure_height=560,
)

# 13 四件套实物
gen.figure_card(
    J("musk2019-fig2.jpg"), "Musk & Neuralink 2019, JMIR — A 针 / B pincher / C 针盒",
    [
        "针只解决「能不能破膜」。真正要送进去的，是一根长约 20 mm、总厚仅 **4–6 µm** 的聚酰亚胺电极丝，"
        "柔到几乎没有抗弯能力。",
        "2019 年论文里这一端有四个部件：**针**（钩住丝末端 16×50 µm² 的环）、**套管**（针在其中滑动）、"
        "**pincher**（一根末端折弯的 50 µm 钨丝）、**线性电机**（回缩加速度可达 30,000 mm/s²）。",
        "图中 A 是针，注意它从上方一根明显更粗的亮管下端伸出——那根管就是套管。B 是 pincher。"
        "底下那枚 1 美分硬币直径 **19.05 mm**。",
    ],
    P("13-parts-photo.png"), figure_height=560,
)

# 14 套管
gen.figure_card(
    F("fig-len.png"), "自由长度决定针会不会弯",
    [
        "回到屈曲公式：**L 是自由长度**，即杆上没有横向支撑的那一段。"
        "一根 24 µm 的针若 20 mm 全裸露，临界载荷仅 0.16 mN——**16 毫克就能把它压弯**。"
        "套管把 L 压缩到只剩伸出管口的一小截，L 减到 1/10，P_cr 涨 100 倍。",
        "**资料边界**：2019 年论文没有描述套管的功能，上面是力学推论；K 与各段 L 均为假设值，属量级推演。",
        "官方只给过几何——2025 年更新里说套管**外径 150 µm、内孔 60 µm**。"
        "看 2019 年 Fig 3，管口停在组织表面，**套管不进脑**。",
    ],
    P("14-cannula.png"), figure_height=560,
)

# 15 pincher
gen.figure_card(
    F("fig-parts.png"), "四个部件的相对位置与分工",
    [
        "针尖只在丝末端的环上钩住**一个点**。厚度 4–6 µm 的丝靠这一个点无法定形。"
        "论文给 pincher 的职责是**运送中托住电极丝**，以及**保证丝沿针开出的通道进入组织**。"
        "它可轴向进退、也可旋转——旋转让折弯的横臂压紧或松开。",
        "**需要说明**：pincher 只在 2019 年那篇论文里有明确记载。当时整个组件称 "
        "**needle-pincher cartridge（NPC）**，2025–2026 年官方材料已改称 **needle cartridge（NC）**。",
        "「pincher」一词在 2025 年夏季更新全文、机器人自动化视频、经硬膜手术视频中**均未出现**。"
        "这只说明官方不再提及，没有任何材料说该零件被取消。",
    ],
    P("15-pincher.png"), figure_height=500,
)

# 16 四步
gen.figure_card(
    J("musk2019-fig3.jpg"), "Musk & Neuralink 2019, JMIR — 插入四步，标尺 1 mm",
    [
        "论文对这四格的描述是：插入器带着丝接近 → 在组织表面触底 → 针穿透组织、把丝送到目标深度 → "
        "插入器抽离，丝留在组织里。",
        "最后一步靠**回缩加速度**。线性电机以最高 **30,000 mm/s²** 急退，让丝在惯性下从针尖的钩上脱开。"
        "官方措辞是 \"to encourage separation of the probe from the needle\"。",
        "三件事合起来看：**OCT 决定插多深，针的材料与几何决定破不破得了膜，"
        "套管与 pincher 决定丝能不能沿着针开出的那条通道进去。**"
        "硬膜保住了，这三件事都要重做一遍——这就是「少切一刀」背后的全部工作量。",
    ],
    P("16-sequence.png"), figure_height=560,
)

# 17 尾卡
gen.tail_card(
    [
        "① Musk E, Neuralink. An Integrated Brain-Machine Interface Platform With Thousands "
        "of Channels. J Med Internet Res. 2019;21(10):e16194",
        "② Neuralink. Our First Transdural Procedure. 2026-06-30（官方视频字幕）",
        "③ Neuralink Update, Summer 2025（官方视频字幕）",
        "④ Neuralink. Automating Neurosurgery with Robotics（官方视频字幕）",
        "⑤ Enzmann DR, Pelc NJ. Brain motion: measurement with phase-contrast MR imaging. "
        "Radiology. 1992;185(3):653–660",
        "⑥ Sloots JJ, Biessels GJ, Zwanenburg JJM. Cardiac and respiration-induced brain "
        "deformations in humans quantified with high-field MRI. NeuroImage. 2020;210:116581",
        "⑦ Hill DL, Maurer CR Jr, Maciunas RJ, et al. Measurement of intraoperative brain "
        "surface deformation under a craniotomy. Neurosurgery. 1998;43(3):514–526",
        "⑧ Hubel DH. Tungsten microelectrode for recording from single units. "
        "Science. 1957;125(3247):549–550",
        "",
        "图 13、16 引自 ①（JMIR，开放获取）；图 3、5、9、10 为 ②③ 官方视频截帧。"
        "第 12 张的针径为本人在视频帧上按标尺自测，非公开数值。",
    ],
    P("17-refs.png"),
    lead_paragraphs=[
        "下一期讲第三个问题：隔着不透明的硬膜，怎么看见血管并绕开它。",
    ],
)

print("done ->", OUT)
