# -*- coding: utf-8 -*-
"""脑机接口外设综述：引文拉通 + 标题重构 + 术语标注"""
import re

SRC = "脑机接口外设0820初稿.md"
DST = "脑机接口外设0820初稿_整理版.md"

text = open(SRC, encoding="utf-8").read()

# ============ 1. 删除元信息 blockquote ============
text = text.replace(
    "> 正文协作稿。稳定规则与生产阶段分别维护在[写作与生产规范](./写作与生产规范.md)和[项目进度](./项目进度.md)中；每次成文或改稿前必须先读取两份文件。\n\n",
    ""
)

# ============ 2. 标题层级重构 ============
# 2.1 总引去标题（变成无标题段落）
text = text.replace("## 一、总引（外设的定义、作用与发展概况）\n", "")

# 2.2 一级标题：括号 + 汉字序号
text = text.replace("## 一、侵入式脑机接口外设", "## （一）侵入式脑机接口外设")
text = text.replace("## 二、非侵入式脑机接口外设", "## （二）非侵入式脑机接口外设")

# 2.3 侵入式引语去标题
text = text.replace("### 1. 引语：功能定位与重要性\n", "")

# 2.4 侵入式二级标题重排
text = text.replace("### 2. 文字与语音终端：把神经活动转换为语言", "### 1. 文字与语音终端：把神经活动转换为语言")
text = text.replace("### 3. 机械臂、肢体驱动装置与运动刺激器：把运动意图转换为动作", "### 2. 机械臂、肢体驱动装置与运动刺激器：把运动意图转换为动作")
text = text.replace("### 4. 接触传感器、摄像机与感觉刺激器：把环境信息转换为感觉", "### 3. 接触传感器、摄像机与感觉刺激器：把环境信息转换为感觉")

# 2.5 侵入式三级标题重排（加 1.1/1.2/1.3 编号）
text = text.replace("**呈现终端：展示文字和语音**", "**1.1 呈现终端：展示文字和语音**")
text = text.replace("**映射层：把低维输出接入标准输入**", "**1.2 映射层：把低维输出接入标准输入**")
text = text.replace("**部署环境：从实验室终端到家庭工作站**", "**1.3 部署环境：从实验室终端到家庭工作站**")
text = text.replace("**机械臂：执行动作意图**", "**2.1 机械臂：执行动作意图**")
text = text.replace("**共享控制：补充神经输入**", "**2.2 共享控制：补充神经输入**")
text = text.replace("**肌电刺激器：协助上肢运动**", "**2.3 肌电刺激器：协助上肢运动**")
text = text.replace("**外骨骼与脊髓刺激：支撑站立与步行**", "**2.4 外骨骼与脊髓刺激：支撑站立与步行**")
text = text.replace("**接触与力传感器：把抓握变成可感反馈**", "**3.1 接触与力传感器：把抓握变成可感反馈**")
text = text.replace("**视觉输入前端：场景压缩与刺激图样生成**", "**3.2 视觉输入前端：场景压缩与刺激图样生成**")

# 2.6 侵入式小结与转场去标题
text = text.replace("### 5. 小结与转场\n", "")

# 2.7 非侵入式三级标题重排
text = text.replace("**刺激屏：在呈现选项的同时诱发脑反应**", "**1.1 刺激屏：在呈现选项的同时诱发脑反应**")
text = text.replace("**计算机与家居终端：把选择接入实际服务**", "**1.2 计算机与家居终端：把选择接入实际服务**")
text = text.replace("**电刺激与手部外骨骼：把运动意图转换为患肢动作**", "**2.1 电刺激与手部外骨骼：把运动意图转换为患肢动作**")
text = text.replace("**轮椅与下肢外骨骼：把运动意图转换为站立和移动**", "**2.2 轮椅与下肢外骨骼：把运动意图转换为站立和移动**")
text = text.replace("**脑电头戴与脑电耳机：把脑状态采集嵌入可穿戴终端**", "**3.1 脑电头戴与脑电耳机：把脑状态采集嵌入可穿戴终端**")
text = text.replace("**视觉、声音与刺激终端：把脑状态转为直接反馈**", "**3.2 视觉、声音与刺激终端：把脑状态转为直接反馈**")
text = text.replace("**自适应工作站：根据脑状态调整界面与任务**", "**3.3 自适应工作站：根据脑状态调整界面与任务**")

# 2.8 非侵入式本部分小结去标题
text = text.replace("### 4. 本部分小结\n", "")

# 2.9 结语去标题
text = text.replace("## 三、两类脑机接口系统的外设能力与发展格局\n", "")

# 2.10 参考文献标题
text = text.replace("## 五、参考文献", "## 参考文献")

# ============ 3. 术语首次出现标注（核心缩写） ============
text = text.replace(
    "脑机接口的核心读写设备用于采集神经信号",
    "脑机接口（brain-computer interface，BCI）的核心读写设备用于采集神经信号",
    1
)
text = text.replace(
    "卒中、肌萎缩侧索硬化、脑干损伤等患者难以稳定地说和写",
    "卒中、肌萎缩侧索硬化（amyotrophic lateral sclerosis，ALS）、脑干损伤等患者难以稳定地说和写",
    1
)
text = text.replace(
    "前臂神经肌肉电刺激（NMES）电极贴片",
    "前臂神经肌肉电刺激（neuromuscular electrical stimulation，NMES）电极贴片",
    1
)
text = text.replace(
    "脑电头带、反馈终端与自适应界面共同构成",
    "脑电（electroencephalography，EEG）头带、反馈终端与自适应界面共同构成",
    1
)
text = text.replace(
    "闪烁刺激会诱发具有相应频率和相位特征的稳态视觉诱发电位，系统再将脑电",
    "闪烁刺激会诱发具有相应频率和相位特征的稳态视觉诱发电位（steady-state visual evoked potential，SSVEP），系统再将脑电",
    1
)
text = text.replace(
    "Dreem 3 睡眠头带与多导睡眠图同步记录",
    "Dreem 3 睡眠头带与多导睡眠图（polysomnography，PSG）同步记录",
    1
)
text = text.replace(
    "该设备对快速眼动睡眠的识别灵敏度为 89.88%",
    "该设备对快速眼动（rapid eye movement，REM）睡眠的识别灵敏度为 89.88%",
    1
)
text = text.replace(
    "但未观察到事件相关电位、听觉稳态反应或 α 阻断",
    "但未观察到事件相关电位（event-related potential，ERP）、听觉稳态反应或 α 阻断",
    1
)

# ============ 4. 引文修正 ============
# 4.1 悬空引文 101（BrainCo，已从参考文献移除）——删除
text = text.replace("[66,67,72–77,90,95,97,98,100,101]", "[66,67,72–77,90,95,97,98,100]")
text = text.replace("[60,67,92,93,95,98,100,101]", "[60,67,92,93,95,98,100]")

# 4.2 未用引文 109（IDUN 产品页）——补到"单通道"规格处
text = text.replace(
    "Tremmel 等使用 IDUN Guardian 2.1 单通道耳内脑电设备开展同步对照研究",
    "Tremmel 等使用 IDUN Guardian 2.1 单通道耳内脑电设备[109]开展同步对照研究",
    1
)

# ============ 5. 引文重排（按首次出现顺序） ============
# 旧编号 -> 新编号（2 与 37 为同一篇 Lorach 2023，合并为 4；80/101 已删除）
old_to_new = {
    26:1, 1:2, 3:3, 2:4, 37:4, 40:5, 59:6, 66:7, 67:8, 72:9, 73:10, 74:11,
    75:12, 76:13, 77:14, 90:15, 95:16, 97:17, 98:18, 100:19, 53:20, 58:21,
    4:22, 6:23, 13:24, 21:25, 22:26, 23:27, 5:28, 12:29, 8:30, 7:31, 14:32,
    16:33, 41:34, 9:35, 17:36, 18:37, 11:38, 45:39, 10:40, 19:41, 42:42,
    24:43, 25:44, 28:45, 29:46, 35:47, 36:48, 31:49, 27:50, 30:51, 32:52,
    33:53, 34:54, 38:55, 39:56, 46:57, 44:58, 43:59, 47:60, 48:61, 49:62,
    50:63, 51:64, 56:65, 57:66, 54:67, 60:68, 78:69, 63:70, 64:71, 65:72,
    61:73, 68:74, 69:75, 81:76, 82:77, 83:78, 84:79, 102:80, 88:81, 107:82,
    108:83, 110:84, 105:85, 106:86, 109:87, 104:88, 96:89, 94:90, 89:91,
    92:92, 93:93, 103:94, 85:95, 87:96, 20:97,
}

def renumber(match):
    inner = match.group(1)
    parts = [p.strip() for p in inner.split(',')]
    nums = set()
    for p in parts:
        if '–' in p or '-' in p:
            a, b = re.split('[–\-]', p)
            for n in range(int(a), int(b) + 1):
                if n in old_to_new:
                    nums.add(old_to_new[n])
        else:
            n = int(p)
            if n in old_to_new:
                nums.add(old_to_new[n])
    nums = sorted(nums)
    # 合并连续编号为区间
    runs = []
    i = 0
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
            j += 1
        if j - i >= 2:
            runs.append(f"{nums[i]}–{nums[j]}")
        else:
            for k in range(i, j + 1):
                runs.append(str(nums[k]))
        i = j + 1
    return "[" + ",".join(runs) + "]"

# 只对正文中的引文（[数字]）做重排；参考文献条目行以"数字. ["开头，不受影响
text = re.sub(r"\[([0-9]+(?:[–\-][0-9]+)?(?:,[0-9]+(?:[–\-][0-9]+)?)*)\]", renumber, text)

# ============ 6. 删除各节暂用参考文献，替换为统一参考文献表 ============
# 删除所有 "#### 本节暂用参考文献" 等标题及其后的条目（到下一个 ## 或 ### 或文件尾）
lines = text.split("\n")
out = []
skip = False
for ln in lines:
    s = ln.strip()
    if s.startswith("####") and "暂用参考文献" in s:
        skip = True
        continue
    if s == "【随正文逐条加入，最终统一格式；定稿时按首次出现顺序统一重排编号并合并各节的暂用参考文献】":
        skip = True
        continue
    if skip:
        # 跳过参考文献条目（数字. 开头或空行），遇到新标题则停止
        if re.match(r"^\d+\.\s", s) or s == "":
            continue
        else:
            skip = False
    out.append(ln)
text = "\n".join(out)

# 参考文献表（新编号 1..97，按首次出现顺序）
refs = {
 1: ("FDA. Implanted Brain-Computer Interface Devices for Patients with Paralysis or Amputation: Non-clinical Testing and Clinical Considerations, 2021", "https://www.fda.gov/regulatory-information/search-fda-guidance-documents/implanted-brain-computer-interface-bci-devices-patients-paralysis-or-amputation-non-clinical-testing"),
 2: ("Card et al. Long-term independent use of an intracortical brain–computer interface for speech and cursor control. Nature Medicine, 2026", "https://www.nature.com/articles/s41591-026-04414-6"),
 3: ("Flesher et al. A brain-computer interface that evokes tactile sensations improves robotic arm control. Science, 2021", "https://pubmed.ncbi.nlm.nih.gov/34016775/"),
 4: ("Lorach et al. Walking naturally after spinal cord injury using a brain-spine interface. Nature, 2023", "https://www.nature.com/articles/s41586-023-06094-5"),
 5: ("Chandrasekaran et al. A neuroprosthesis for restoring hand movement and sensation in a person with complete tetraplegia. Nature Medicine, 2026", "https://www.nature.com/articles/s41591-026-04498-0"),
 6: ("Greenspon et al. Long-term safety and efficacy of intracortical microstimulation in humans. Science Translational Medicine, 2026", "https://pubmed.ncbi.nlm.nih.gov/42455900/"),
 7: ("Sellers, Vaughan & Wolpaw. A brain-computer interface for long-term independent home use. Amyotrophic Lateral Sclerosis, 2010", "https://pubmed.ncbi.nlm.nih.gov/20583947/"),
 8: ("Wolpaw et al. Independent home use of a brain-computer interface by people with amyotrophic lateral sclerosis. Neurology, 2018", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6059033/"),
 9: ("Biasiucci et al. Brain-actuated functional electrical stimulation elicits lasting arm motor recovery after stroke. Nature Communications, 2018", "https://www.nature.com/articles/s41467-018-04673-z"),
 10: ("Frolov et al. Post-stroke Rehabilitation Training with a Motor-Imagery-Based BCI-Controlled Hand Exoskeleton. Frontiers in Neuroscience, 2017", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5517482/"),
 11: ("Ramos-Murguialday et al. Brain-machine interface in chronic stroke rehabilitation. Annals of Neurology, 2013；长期随访 Neurorehabilitation and Neural Repair, 2019", "https://pubmed.ncbi.nlm.nih.gov/23494615/"),
 12: ("Xie et al. Brain-machine interface-based training for improving upper extremity function after stroke: a meta-analysis. Frontiers in Neuroscience, 2022", "https://pubmed.ncbi.nlm.nih.gov/35992923/"),
 13: ("Chen & Yun. Efficacy of Brain-Computer Interface Therapy for Upper Limb Rehabilitation in Chronic Stroke. Journal of Medical Internet Research, 2026", "https://pubmed.ncbi.nlm.nih.gov/41605490/"),
 14: ("Bai et al. Immediate and long-term effects of BCI-based rehabilitation of the upper extremity after stroke. Journal of NeuroEngineering and Rehabilitation, 2020", "https://pubmed.ncbi.nlm.nih.gov/32334608/"),
 15: ("Westwood et al. Neurofeedback for Attention-Deficit/Hyperactivity Disorder: A Systematic Review and Meta-Analysis. JAMA Psychiatry, 2025", "https://pmc.ncbi.nlm.nih.gov/articles/PMC11800020/"),
 16: ("Beau et al. Dreem headband performance in Insomnia Disorder: an in-lab comparison to polysomnography. Sleep Medicine, 2025", "https://pubmed.ncbi.nlm.nih.gov/40712528/"),
 17: ("Baldassarri et al. The Effect of Closed-Loop Auditory Stimulation on Memory Consolidation and Sleep Physiology in an Ecological Setting. Journal of Sleep Research, 2026", "https://pmc.ncbi.nlm.nih.gov/articles/PMC13193352/"),
 18: ("Bressler et al. A randomized controlled trial of alpha phase-locked auditory stimulation to treat symptoms of sleep onset insomnia. Scientific Reports, 2024", "https://pmc.ncbi.nlm.nih.gov/articles/PMC11156862/"),
 19: ("Neurable MW75 Neuro 官方产品页", "https://www.neurable.com/products/mw75neuro"),
 20: ("Beauchamp et al. Dynamic Stimulation of Visual Cortex Produces Form Vision in Sighted and Blind Humans. Cell, 2020", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7331799/"),
 21: ("Holz et al. Subretinal Photovoltaic Implant to Restore Vision in Geographic Atrophy Due to AMD. New England Journal of Medicine, 2026;394:232–242（2025-10-20 在线发表）", "https://www.nejm.org/doi/full/10.1056/NEJMoa2501396"),
 22: ("国家药监局：首款侵入式脑机接口医疗器械获批上市，2026", "https://yjj.sh.gov.cn/zjyw/20260313/04985a5fbe284e9c806ff5f370cb00b2.html"),
 23: ("Metzger et al. A high-performance neuroprosthesis for speech decoding and avatar control. Nature, 2023", "https://www.nature.com/articles/s41586-023-06443-4"),
 24: ("Willett et al. A high-performance speech neuroprosthesis. Nature, 2023", "https://www.nature.com/articles/s41586-023-06377-x"),
 25: ("Branco et al. Brain-Computer Interfaces for Communication: Preferences of Individuals With Locked-in Syndrome. Neurorehabilitation and Neural Repair, 2021", "https://pubmed.ncbi.nlm.nih.gov/33530868/"),
 26: ("Peters et al. Brain-computer interface users speak up: the virtual users' forum at the 2013 international brain-computer interface meeting. Archives of Physical Medicine and Rehabilitation, 2015", "https://pubmed.ncbi.nlm.nih.gov/25721545/"),
 27: ("BCI patient preferences: a systematic review, 2024", "https://pubmed.ncbi.nlm.nih.gov/39569894/"),
 28: ("Willett et al. High-performance brain-to-text communication via handwriting. Nature, 2021", "https://www.nature.com/articles/s41586-021-03506-2"),
 29: ("Metzger et al. Generalizable spelling using a speech neuroprosthesis in an individual with severe limb and vocal paralysis. Nature Communications, 2022", "https://pmc.ncbi.nlm.nih.gov/articles/PMC9643551/"),
 30: ("Qian et al. Real-time decoding of full-spectrum Chinese using brain-computer interface. Science Advances, 2025", "https://doi.org/10.1126/sciadv.adz9968"),
 31: ("Wairagkar et al. An instantaneous voice-synthesis neuroprosthesis. Nature, 2025", "https://www.nature.com/articles/s41586-025-09127-3"),
 32: ("Littlejohn et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. Nature Neuroscience, 2025", "https://www.nature.com/articles/s41593-025-01905-6"),
 33: ("Silva et al. A bilingual speech neuroprosthesis driven by cortical articulatory representations shared between languages. Nature Biomedical Engineering, 2024", "https://www.nature.com/articles/s41551-024-01207-5"),
 34: ("Apple 官方支持文档：Use Switch Control to navigate your iPhone, iPad, or iPod touch", "https://support.apple.com/en-us/119835"),
 35: ("Pandarinath et al. High performance communication by people with paralysis using an intracortical brain-computer interface. eLife, 2017", "https://elifesciences.org/articles/18554"),
 36: ("Vansteensel et al. Fully Implanted Brain–Computer Interface in a Locked-In Patient with ALS. New England Journal of Medicine, 2016", "https://www.nejm.org/doi/10.1056/NEJMoa1608085"),
 37: ("Vansteensel et al. Longevity of a Brain–Computer Interface for Amyotrophic Lateral Sclerosis. New England Journal of Medicine, 2024", "https://www.nejm.org/doi/10.1056/NEJMoa2314598"),
 38: ("Mitchell et al. Assessment of Safety of a Fully Implanted Endovascular Brain-Computer Interface for Severe Paralysis in 4 Patients. JAMA Neurology, 2023", "https://jamanetwork.com/journals/jamaneurology/fullarticle/2799839"),
 39: ("Synchron Debuts First Thought-Controlled iPad Experience Using Apple's New BCI Human Interface Device Protocol, 2025", "https://www.businesswire.com/news/home/20250804537175/en/Synchron-Debuts-First-Thought-Controlled-iPad-Experience-Using-Apples-New-BCI-Human-Interface-Device-Protocol"),
 40: ("Nuyujukian et al. Cortical control of a tablet computer by people with paralysis. PLOS ONE, 2018", "https://pubmed.ncbi.nlm.nih.gov/30462658/"),
 41: ("Simeral et al. Home use of a percutaneous wireless intracortical BCI. IEEE Transactions on Biomedical Engineering, 2021", "https://pubmed.ncbi.nlm.nih.gov/33784612/"),
 42: ("Kunz et al. Inner speech in motor cortex and implications for speech neuroprostheses. Cell, 2025", "https://pubmed.ncbi.nlm.nih.gov/40816265/"),
 43: ("Collinger et al. Functional Priorities, Assistive Technology, and Brain-Computer Interfaces after Spinal Cord Injury. JRRD, 2013", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3684986/"),
 44: ("Blabe et al. Assessment of brain-machine interfaces from the perspective of people with paralysis. Journal of Neural Engineering, 2015", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4761228/"),
 45: ("Hochberg et al. Reach and grasp by people with tetraplegia using a neurally controlled robotic arm. Nature, 2012", "https://www.nature.com/articles/nature11076"),
 46: ("Collinger et al. High-performance neuroprosthetic control by an individual with tetraplegia. Lancet, 2013", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3641862/"),
 47: ("Bouton et al. Restoring cortical control of functional movement in a human with quadriplegia. Nature, 2016", "https://www.nature.com/articles/nature17435"),
 48: ("Benabid et al. An exoskeleton controlled by an epidural wireless brain-machine interface in a tetraplegic patient. Lancet Neurology, 2019", "https://pubmed.ncbi.nlm.nih.gov/31587955/"),
 49: ("Downey et al. Blending of brain-machine interface and vision-guided autonomous robotics improves neuroprosthetic arm performance during grasping. Journal of NeuroEngineering and Rehabilitation, 2016", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4797113/"),
 50: ("Hochberg et al. Neuronal ensemble control of prosthetic devices by a human with tetraplegia. Nature, 2006", "https://www.nature.com/articles/nature04970"),
 51: ("Wodlinger et al. Ten-dimensional anthropomorphic arm control in a human brain-machine interface. Journal of Neural Engineering, 2015", "https://motorlab.pitt.edu/pub/Ten-dimensional%20anthropomorphic%20arm%20control%20in%20a%20human%20brain-machine%20interface_Wodlinger_2015.pdf"),
 52: ("Handelman et al. Shared Control of Bimanual Robotic Limbs With a Brain-Machine Interface for Self-Feeding. Frontiers in Neurorobotics, 2022", "https://www.frontiersin.org/journals/neurorobotics/articles/10.3389/fnbot.2022.918001/full"),
 53: ("ClinicalTrials.gov. CONVOY, NCT06710626", "https://clinicaltrials.gov/study/NCT06710626"),
 54: ("Neuralink. CONVOY Study Launch, 2024", "https://neuralink.com/updates/convoy-study-launch/"),
 55: ("Ajiboye et al. Restoration of reaching and grasping movements through brain-controlled muscle stimulation in a person with tetraplegia. Lancet, 2017", "https://pubmed.ncbi.nlm.nih.gov/28363483/"),
 56: ("China approves brain chip to overcome paralysis. Nature Biotechnology, 2026", "https://www.nature.com/articles/s41587-026-03101-8"),
 57: ("国家药监局器审中心：植入式脑机接口手部运动功能代偿系统技术审评报告（受理号 CQZ2600324、CQZ2600325）", "https://www.cmde.org.cn/directory/web/cmde/images/1775031381651060289.pdf"),
 58: ("Capogrosso et al. A brain-spine interface alleviating gait deficits after spinal cord injury in primates. Nature, 2016", "https://pubmed.ncbi.nlm.nih.gov/27830790/"),
 59: ("Cajigas, Davis et al. Brain-Computer interface control of stepping from invasive electrocorticography upper-limb motor imagery in a patient with quadriplegia. Frontiers in Human Neuroscience, 2023", "https://pmc.ncbi.nlm.nih.gov/articles/PMC9912159/"),
 60: ("Bensmaia & Miller. Restoring sensorimotor function through intracortical interfaces. Nature Reviews Neuroscience, 2014", "https://www.nature.com/articles/nrn3724"),
 61: ("Valle et al. Restoring vision and touch with cortical microstimulation. Nature Reviews Bioengineering, 2026", "https://www.nature.com/articles/s44222-026-00449-z"),
 62: ("Osborn et al. Artificial touch feedback using microstimulation of human somatosensory cortex to convey grip force from a robotic hand. IEEE EMBC, 2024", "https://pubmed.ncbi.nlm.nih.gov/40039504/"),
 63: ("Verbaarschot et al. Conveying tactile object characteristics through customized intracortical microstimulation. Nature Communications, 2025", "https://pubmed.ncbi.nlm.nih.gov/40312384/"),
 64: ("Greenspon et al. Evoking stable and precise tactile sensations via multi-electrode intracortical microstimulation. Nature Biomedical Engineering, 2025", "https://www.nature.com/articles/s41551-024-01299-z"),
 65: ("ClinicalTrials.gov NCT03344848（Orion）；Participant perspectives from the Orion trial, 2024", "https://pmc.ncbi.nlm.nih.gov/articles/PMC11001790/"),
 66: ("Stephan et al. The Role of Scalp EEG Recordings During Cortical Visual Prosthesis Testing. Artificial Organs, 2025", "https://pubmed.ncbi.nlm.nih.gov/40421717/"),
 67: ("Schmidt et al. Feasibility of a visual prosthesis for the blind based on intracortical microstimulation. Brain, 1996", "https://pubmed.ncbi.nlm.nih.gov/8800945/"),
 68: ("Peters et al. A systematic review of AAC-BCI systems for individuals with disabilities. Frontiers in Human Neuroscience, 2022", "https://pmc.ncbi.nlm.nih.gov/articles/PMC9374067/"),
 69: ("FDA De Novo DEN200046（IpsiHand，2021-04-23）", "https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN200046.pdf"),
 70: ("Miao et al. An ERP-based BCI with peripheral stimuli: validation with ALS patients. Cognitive Neurodynamics, 2020", "https://pubmed.ncbi.nlm.nih.gov/32015765/"),
 71: ("Chen et al. High-speed spelling with a noninvasive brain-computer interface. PNAS, 2015", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4640776/"),
 72: ("Ravi et al. Enhanced System Robustness of Asynchronous BCI in Augmented Reality Using SSMVEP. IEEE TNSRE, 2022", "https://pubmed.ncbi.nlm.nih.gov/34990366/"),
 73: ("Nijboer et al. A P300-based brain-computer interface for people with amyotrophic lateral sclerosis. Clinical Neurophysiology, 2008", "https://pubmed.ncbi.nlm.nih.gov/18571984/"),
 74: ("Cincotti et al. Non-invasive brain-computer interface system: towards its application as assistive technology. Brain Research Bulletin, 2008", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2896271/"),
 75: ("g.tec BCI product catalog, 2018；FDA 510(k) 数据库按 applicant 检索 g.tec", "https://gtec.at/wp-content/uploads/2019/10/gtec-Product-Catalog-2018-web.pdf"),
 76: ("Hu et al. Brain-Computer Interface-Controlled Exoskeleton Training for Lower-Limb Rehabilitation in Spinal Cord Injury. Annals of Neurology, 2026", "https://pubmed.ncbi.nlm.nih.gov/41480666/"),
 77: ("López-Larraz et al. Control of an Ambulatory Exoskeleton with a Brain-Machine Interface for Spinal Cord Injury Gait Rehabilitation. Frontiers in Neuroscience, 2016", "https://pubmed.ncbi.nlm.nih.gov/27536214/"),
 78: ("Tonin et al. Learning to control a BMI-driven wheelchair for people with severe tetraplegia. iScience, 2022", "https://pmc.ncbi.nlm.nih.gov/articles/PMC9801246/"),
 79: ("King et al. The feasibility of a brain-computer interface functional electrical stimulation system for the restoration of overground walking after paraplegia. Journal of NeuroEngineering and Rehabilitation, 2015", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4581411/"),
 80: ("Alimardani & Hiraki. Passive Brain-Computer Interfaces for Enhanced Human-Robot Interaction. Frontiers in Robotics and AI, 2020", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7805996/"),
 81: ("Sitaram et al. Closed-loop brain training: the science of neurofeedback. Nature Reviews Neuroscience, 2017", "https://www.nature.com/articles/nrn.2016.164"),
 82: ("NextSense Smartbuds 官方产品页", "https://nextsense.io/products/smartbuds"),
 83: ("Berent et al. A novel, wearable, in-ear EEG technology to assess sleep and daytime sleepiness. Bioelectronic Medicine, 2026", "https://pubmed.ncbi.nlm.nih.gov/42169202/"),
 84: ("Crétot-Richert et al. Assessing focus through ear-EEG: a comparative study between conventional cap EEG and mobile in- and around-the-ear EEG systems. Frontiers in Neuroscience, 2023", "https://pubmed.ncbi.nlm.nih.gov/37829725/"),
 85: ("Tremmel et al. Estimating cognitive workload using a commercial in-ear EEG headset. Journal of Neural Engineering, 2024", "https://pubmed.ncbi.nlm.nih.gov/39500044/"),
 86: ("Bradshaw Bernacchi & Lopez Valdes. Electrophysiological Characterisation of Commercial Ear-EEG Devices. EMBC, 2025", "https://pubmed.ncbi.nlm.nih.gov/41336899/"),
 87: ("IDUN Guardian 官方产品页", "https://iduntechnologies.com/idun-guardian"),
 88: ("EMOTIV MN8 Quick Start Guide", "https://www.emotiv.com/quick-start-guide-mn8"),
 89: ("Ngo et al. Auditory closed-loop stimulation of the sleep slow oscillation enhances memory. Neuron, 2013", "https://pubmed.ncbi.nlm.nih.gov/23583623/"),
 90: ("Ehrlich et al. A closed-loop, music-based brain-computer interface for emotion mediation. PLOS ONE, 2019", "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0213516"),
 91: ("Ros et al. Consensus on the reporting and experimental design of clinical and cognitive-behavioural neurofeedback studies（CRED-nf checklist）. Brain, 2020", "https://pubmed.ncbi.nlm.nih.gov/32176800/"),
 92: ("Aricò et al. Adaptive Automation Triggered by EEG-Based Mental Workload Index. Frontiers in Human Neuroscience, 2016", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5080530/"),
 93: ("Di Flumeri et al. BCI-based adaptive automation to prevent out-of-the-loop phenomena. Frontiers in Human Neuroscience, 2019", "https://pubmed.ncbi.nlm.nih.gov/31555113/"),
 94: ("Kaongoen et al. The future of wearable EEG: a review of ear-EEG technology and its applications. Journal of Neural Engineering, 2023", "https://pubmed.ncbi.nlm.nih.gov/37748474/"),
 95: ("Lee, Kim & Ahn. Evaluation of consumer-grade wireless EEG systems for brain-computer interface applications. Biomedical Engineering Letters, 2024", "https://pmc.ncbi.nlm.nih.gov/articles/PMC11502727/"),
 96: ("Williams et al. A validation of Emotiv EPOC Flex saline for EEG and ERP research. PeerJ, 2020", "https://peerj.com/articles/9713/"),
 97: ("Patrick-Krueger et al. The state of clinical trials of implantable brain–computer interfaces. Nature Reviews Bioengineering, 2025", "https://www.nature.com/articles/s44222-024-00239-5"),
}

ref_block = "## 参考文献\n\n" + "\n".join(
    f"{n}. [{title}]({url})" for n, (title, url) in sorted(refs.items())
) + "\n"

# 追加参考文献表（去掉旧文件中残留的"参考文献"标题行，避免重复）
if "## 参考文献" in text:
    # 找到 ## 参考文献 之后的内容，替换
    idx = text.index("## 参考文献")
    text = text[:idx] + ref_block
else:
    text = text.rstrip() + "\n\n" + ref_block

# ============ 7. 清理多余空行 ============
text = re.sub(r"\n{3,}", "\n\n", text)

open(DST, "w", encoding="utf-8").write(text)
print("写入完成:", DST)
print("参考文献条数:", len(refs))
