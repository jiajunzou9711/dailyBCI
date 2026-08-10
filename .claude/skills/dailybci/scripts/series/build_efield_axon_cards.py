"""2026-08-08「电场与轴突生长」图卡装配。"""
import os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(SCRIPT_DIR))
from card_generator import CardGenerator  # noqa: E402

SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-08-08-efield-axon")
FIGS = os.path.join(OUT, "figs")
# 本期用到的论文原图 / 外部 CC 图，随成品一起保留，使本期可重新渲染
SRC = os.path.join(FIGS, "src")
os.makedirs(OUT, exist_ok=True)

gen = CardGenerator(date="2026.08.08")
F = lambda n: os.path.join(FIGS, n)
P = lambda n: os.path.join(SRC, n)
O = lambda n: os.path.join(OUT, n)

# ---------------------------------------------------------------- 01 封面
gen.cover_card(
    "电场能让轴突", "朝阴极定向生长",
    "培养皿里如此。成年动物脊髓里，轴突长到损伤断面为止，没有一根穿过。",
    O("01-cover.png"),
    concept_image=P("cover-fig1c.png"), concept_height=545,
    title_size=112, title_top=95,
)

# ---------------------------------------------------------------- 02 目录卡
gen.figure_card(
    F("toc.png"), "本期路线",
    ["2026 年 8 月 5 日 **Science Advances** 刊出《A biodegradable piezoelectric vertebral "
     "implant for programmable electro-neuromodulation in spinal cord injury》。首都医科大学"
     "宣武医院神经外科 × 北京化工大学等，通讯作者 Duan Wanru、Cai Qing、Yu Yingjie。"
     "方法：用可降解压电凝胶替代被切除的椎体，在**大鼠**脊髓损伤模型上评估。"],
    O("02-toc.png"), figure_height=560)

# ---------------------------------------------------------------- 03 引子
gen.figure_card(
    P("fig1B-anat.png"), "Fig. 1B",
    ["先说这篇论文做了什么。研究者把一块可降解的压电凝胶植入**大鼠**体内，替代被切除的椎体；"
     "脊柱承受的压力把它压变形，材料随之产生电，体外超声可以再放大这个输出¹。",
     "如上图，从左到右依次是脊髓损伤、切除椎体、植入凝胶、超声、修复。急性期大鼠瘫痪不动、"
     "没有机械输入，用超声隔空驱动；等能部分负重了，改成负重跑台训练，**由大鼠自己踩踏发电**。"
     "重度损伤组 8 周后后肢运动评分 **13.7** 分，轻度组 4 周后 **16.3** 分¹。",
     "这篇的新意在供电方式。它想达成的目标——用电促进神经再生——是一个有**八十年**历史的问题。"
     "这期剩下的部分讲那个问题现在的答案。"],
    O("03-paper.png"), figure_height=210)

# ---------------------------------------------------------------- 04 解剖背景
gen.figure_card(
    P("ref-Epidural-anesthesia.png"), "腰段矢状面（胸段层次相同）",
    ["要看清这个器件放在哪，先看脊柱的结构。",
     "如上图，右边标着 L3、L4、L5 的三块土黄色骨块是**椎体**，脊柱前方承重的部分；左边伸出来的"
     "骨尖是棘突。中间那条洋红色带标着 Epidural Space，是**硬膜外腔**，紧挨着它的那层膜是"
     "**硬脊膜**。这个腔是真实有宽度的，里面填着脂肪和血管——硬膜外麻醉的导管、脊髓电刺激的"
     "电极，都停在这条带里²。",
     "恢复行走那条线上的经典工作，电极全放在这里，位于脊髓背侧；这篇论文的器件占的是椎体本身，"
     "在脊髓腹侧。**位置换了，要解决的问题没变：电到底凭什么让神经长？**"],
    O("04-anatomy.png"), figure_height=470)

# ---------------------------------------------------------------- 05 神经突
gen.figure_card(
    F("fig-neurite.png"), "培养皿：电场下的生长轨迹",
    ["电作用在神经元的哪个部件上？神经元长出来的突起叫**神经突**，尖端是**生长锥**，"
     "往哪儿长由它决定。",
     "如上图三格，把几十个神经元的胞体叠在同一点、画出每根神经突五小时的轨迹。**无电场时轨迹"
     "向四面八方均匀铺开；加上 150 mV/mm 的电场后，整片轨迹偏向阴极一侧，而且更长**³。"
     "第三格是同样的电场加上阻断细胞骨架的信号通路，偏向消失³。",
     "电场的作用要经过细胞内部的信号通路、再由细胞骨架执行。那么它改变的是方向，还是速度？"],
    O("05-neurite.png"), figure_height=560)

# ---------------------------------------------------------------- 06 转向 vs 变快
gen.figure_card(
    F("fig-turn-speed.png"), "两件不同的事",
    ["电场对神经突的作用要拆成两件事。",
     "如上图，**转向**指已经在长的神经突改变前进方向，把头调向阴极；**长得快**指方向不变、"
     "伸长速率提高。两者阈值不同：鸡胚延髓外植体在 **50–60 mV/mm** 时转向阴极；鸡背根神经节的"
     "神经突在场强超过 **70 mV/mm** 时，朝阴极的生长速度约为朝阳极的 **3 倍，却完全不转向**³。",
     "方向本身也不统一——感觉神经突不转向，运动神经突朝阴极转³。这些数字都成立，"
     "但成立的条件很窄。"],
    O("06-turn-speed.png"), figure_height=440)

# ---------------------------------------------------------------- 07 三道边界
gen.figure_card(
    F("fig-boundary.png"), "三道边界",
    ["上面那些数字成立的条件有三道边界，必须一起记住。",
     "**量级**：培养皿里的转向阈值是 50–60 mV/mm，而活体研究里到达脊髓的场强是 "
     "**40–600 µV/mm**⁴，相差约两个数量级。**细胞**：经典证据几乎全部来自鸡胚、蛙胚、胚胎大鼠"
     "这类本来就在生长的神经元，成年中枢神经元不处在这个状态³。**统计**：改变的是群体轨迹的"
     "分布，加了场之后仍有神经突朝别的方向长³。",
     "记住这三条，再看活体里发生了什么。"],
    O("07-boundary.png"), figure_height=520)

# ---------------------------------------------------------------- 08 在体给电
gen.figure_card(
    F("fig-invivo.png"), "活体：电极放在哪",
    ["活体里第一个要问的是：电极放在哪、脊髓实际拿到多强的场。",
     "具体做法各家不同，电极位置、电流大小、刺激时程随物种和损伤程度而变。共通的有两条：**电极"
     "都在脊髓之外**，靠电流穿过中间的组织，在损伤区两侧之间建立跨越损伤处的电场；因此到达脊髓"
     "的场强只有 **40–600 µV/mm**⁴。",
     "还有一条通用设计：**电场极性每隔一段时间翻转一次**。脊髓里上行的感觉通路与下行的运动通路"
     "走向相反，固定方向的电场只能帮到一边⁴。那么在这样的场强下，轴突长到了哪里？"],
    O("08-invivo.png"), figure_height=470)

# ---------------------------------------------------------------- 09 长到哪里
gen.figure_card(
    F("fig-howfar.png"), "顺行示踪的结果",
    ["回答这个问题要用**顺行示踪**。多数在体研究用神经丝染色数纤维，那只能判定此刻这里有多少根"
     "轴突，判定不了它们从哪儿来；顺行示踪把示踪剂注进特定神经元的胞体，只有从这些细胞长出的"
     "轴突被标记。",
     "这条线上最硬的一项是**成年豚鼠**实验：脊髓部分切断、植入电极施加电场，50–60 天后用辣根"
     "过氧化物酶标记背柱轴突，并精确标出原始切断平面。如上图，**多数动物中轴突长进胶质瘢痕、"
     "到达切断平面；少数动物中轴突绕到损伤区边缘；没有一根穿过损伤区**⁵。",
     "那么这样的生长量，换来了多少功能？"],
    O("09-howfar.png"), figure_height=470)

# ---------------------------------------------------------------- 10 功能
gen.figure_card(
    F("fig-function.png"), "功能改善的量级",
    ["功能这一侧有两组结果，量级都不大。",
     "**成年豚鼠**：胸段脊髓半切，施加 200 µV/mm 的电场，**25% 的动物一个跨节段反射恢复**，"
     "对照组功能缺损持续⁶。恢复的是反射，不是行走。**大鼠**：8 项研究合并后，后肢运动评分"
     "第 8 周高出 **3.00 分**⁴。",
     "如上图，这把尺子 0 分为后肢关节完全无活动、21 分为正常步态，其中 8–13 分是间歇性的不协调"
     "迈步、14 分以上才出现稳定的前后肢协调⁷。**提高 3 分是在同一档内移动。**"],
    O("10-function.png"), figure_height=430)

# ---------------------------------------------------------------- 11 人体
gen.figure_card(
    F("fig-human.png"), "人身上做到什么程度",
    ["就外加电场促进轴突再生这条路线而言，同行评议发表的人体结果只有 **2005 年那一项 I 期试验**，"
     "10 例患者。",
     "入组的是伤后不久的完全性脊髓损伤。伤后 18 天内植入振荡电场刺激器，第 15 周取出，随访到"
     "1 年。如上图，**感觉与运动明显不对称：轻触觉平均改善 25.5 分、针刺觉 20.4 分（两项各满分"
     "112），运动只改善 6.3 分（满分 100）**⁸。原文摘要没有说明这 6.3 分转化成了什么具体动作。",
     "三条限制要和这些数字一起看：**没有同期对照组**；所有患者同时接受了大剂量甲泼尼龙；后续"
     "只再入组过 4 例，器械至今未获批⁹。距今二十年。"],
    O("11-human.png"), figure_height=450)

# ---------------------------------------------------------------- 12 回到论文
gen.figure_card(
    P("fig4D-timedomain.png"), "Fig. 4D",
    ["回到开头那篇论文，它落在这张尺子的哪一格？",
     "如上图，五行分别是呼吸、弯身、被捏、点头、被推；橙色是含压电成分的凝胶，紫色是不含的对照。"
     "**动作幅度越大，输出越大**，被推时单次峰值接近 **100 mV**¹。这支持了它的设计前提：训练"
     "强度决定刺激强度。",
     "也要看清它没有解决什么。**论文自述器件输出是交流电**¹，而上面那条促生长的机制来自持续同向"
     "的直流场；它的输出量级同样落在活体这一档。**它推进的是供电方式；"
     "「能不能长回来」这个问题，它没有回答。**"],
    O("12-back-to-paper.png"), figure_height=500)

# ---------------------------------------------------------------- 13/14 尾卡
gen.tail_card(
    ["¹ Liu P, et al. (2026). A biodegradable piezoelectric vertebral implant for "
     "programmable electro-neuromodulation in spinal cord injury. Sci Adv 12:eaeg0515.",
     "² Kafshdooz L, et al. (2019). Labour analgesia; molecular pathway and the role of "
     "nanocarriers: a systematic review. Artif Cells Nanomed Biotechnol 47:927–935.",
     "³ McCaig CD, Rajnicek AM, Song B, Zhao M. (2005). Controlling cell behavior "
     "electrically: current views and future potential. Physiol Rev 85:943–979.",
     "⁴ Wang G, et al. (2025). Application of oscillating field stimulation in the treatment "
     "of spinal cord injury: a systematic review and meta-analysis of preclinical studies. "
     "J NeuroEng Rehabil 22:85."],
    O("13-tail.png"),
    lead_paragraphs=[
        "这条线八十年了。1946 年就证明电流能控制培养中的神经纤维往哪儿长，量级不小；"
        "八十年后，活体里最好的示踪证据仍然是轴突长到断面为止。",
        "中间的落差来自三件事：活体里场强低两个数量级、成年神经元不在生长状态、损伤区还有瘢痕。"
        "今天这篇论文把供电方式换成了患者自己的运动，这一步有意思；它面对的仍然是同一道落差。"])

gen.tail_card(
    ["⁵ Borgens RB, Blight AR, Murphy DJ, Stewart L. (1986). Transected dorsal column axons "
     "within the guinea pig spinal cord regenerate in the presence of an applied electric "
     "field. J Comp Neurol 250:168–180.",
     "⁶ Borgens RB, Blight AR, McGinnis ME. (1987). Behavioral recovery induced by applied "
     "electric fields after spinal cord hemisection in guinea pig. Science 238:366–369.",
     "⁷ Basso DM, Beattie MS, Bresnahan JC. (1995). A sensitive and reliable locomotor rating "
     "scale for open field testing in rats. J Neurotrauma 12:1–21.",
     "⁸ Shapiro S, et al. (2005). Oscillating field stimulation for complete spinal cord "
     "injury in humans: a phase 1 trial. J Neurosurg Spine 2:3–10.",
     "⁹ 后续入组与监管进展：公司公告与行业媒体报道，非同行评议来源。",
     "",
     "图片来源：封面与 Fig. 1B、Fig. 4D 取自文献 1（CC BY-NC）；腰段矢状面取自文献 2"
     "（CC BY 4.0）；其余示意图为自制，数据出处见对应角标。「相差约两个数量级」为本文自算。"],
    O("14-tail2.png"))

print("done ->", OUT)
