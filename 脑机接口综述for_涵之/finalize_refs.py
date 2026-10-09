# -*- coding: utf-8 -*-
"""生成最终 GB/T 7714 参考文献列表并写回 MD + DOCX"""
import json, re

data = json.load(open("refs_meta_full.json", encoding="utf-8"))
by_num = {r["num"]: r for r in data}

JNAME = {
    "Science (New York, N.Y.)": "Science",
    "Science translational medicine": "Science Translational Medicine",
    "Amyotrophic lateral sclerosis : official publication of the World Federation of Neurology Research Group on Motor Neuron Diseases": "Amyotrophic Lateral Sclerosis",
    "Frontiers in neuroscience": "Frontiers in Neuroscience",
    "Journal of medical Internet research": "Journal of Medical Internet Research",
    "Journal of neuroengineering and rehabilitation": "Journal of NeuroEngineering and Rehabilitation",
    "JAMA psychiatry": "JAMA Psychiatry",
    "Sleep medicine": "Sleep Medicine",
    "Journal of sleep research": "Journal of Sleep Research",
    "Scientific reports": "Scientific Reports",
    "Neurorehabilitation and neural repair": "Neurorehabilitation and Neural Repair",
    "Archives of physical medicine and rehabilitation": "Archives of Physical Medicine and Rehabilitation",
    "Journal of neural engineering": "Journal of Neural Engineering",
    "Nature communications": "Nature Communications",
    "PloS one": "PLOS ONE",
    "IEEE transactions on bio-medical engineering": "IEEE Transactions on Biomedical Engineering",
    "Journal of rehabilitation research and development": "Journal of Rehabilitation Research and Development",
    "Lancet (London, England)": "The Lancet",
    "The Lancet. Neurology": "The Lancet Neurology",
    "Annals of neurology": "Annals of Neurology",
    "Clinical neurophysiology : official journal of the International Federation of Clinical Neurophysiology": "Clinical Neurophysiology",
    "Brain research bulletin": "Brain Research Bulletin",
    "Frontiers in robotics and AI": "Frontiers in Robotics and AI",
    "Bioelectronic medicine": "Bioelectronic Medicine",
    "Brain : a journal of neurology": "Brain",
    "Artificial organs": "Artificial Organs",
    "Cognitive neurodynamics": "Cognitive Neurodynamics",
    "Proceedings of the National Academy of Sciences of the United States of America": "Proceedings of the National Academy of Sciences",
    "IEEE transactions on neural systems and rehabilitation engineering : a publication of the IEEE Engineering in Medicine and Biology Society": "IEEE Transactions on Neural Systems and Rehabilitation Engineering",
    "AJOB neuroscience": "AJOB Neuroscience",
    "Frontiers in human neuroscience": "Frontiers in Human Neuroscience",
    "Biomedical engineering letters": "Biomedical Engineering Letters",
}

# 页码覆盖(文章号 + 展开缩略页码 + 补全)
PAGE_OVERRIDE = {
    7: "449-455", 11: "100-108", 26: "S33-S37", 38: "270-278",
    43: "145-160", 46: "557-564", 67: "507-522", 71: "E6058-E6067",
    89: "545-553",
    9: "2421", 27: "061005", 30: "eadz9968", 35: "e18554",
    52: "918001", 83: "13", 85: "066022", 94: "051002",
}
YEAR_OVERRIDE = {59: "2023", 64: "2025", 97: "2025"}
VOLUME_OVERRIDE = {67: "119"}  # Brain 1996, vol 字段含 " ( Pt 2)"
ISSUE_OVERRIDE = {67: "Pt 2"}  # Brain 1996 119(Pt 2)

# 句首大写(把 Crossref 的 Title Case 转成句首大写)
TITLE_OVERRIDE = {
    10: "Post-stroke rehabilitation training with a motor-imagery-based brain-computer interface (BCI)-controlled hand exoskeleton: a randomized controlled multicenter trial",
    13: "Efficacy of brain-computer interface therapy for upper limb rehabilitation in chronic stroke: systematic review and meta-analysis of randomized controlled trials",
    15: "Neurofeedback for attention-deficit/hyperactivity disorder: a systematic review and meta-analysis",
    16: "Dreem headband performance in insomnia disorder: an in-lab comparison to polysomnography",
    17: "The effect of closed-loop auditory stimulation on memory consolidation and sleep physiology in an ecological setting",
    20: "Dynamic stimulation of visual cortex produces form vision in sighted and blind humans",
    21: "Subretinal photovoltaic implant to restore vision in geographic atrophy due to AMD",
    12: "Brain-machine interface-based training for improving upper extremity function after stroke: a meta-analysis of randomized controlled trials",
    25: "Brain-computer interfaces for communication: preferences of individuals with locked-in syndrome",
    26: "Brain-computer interface users speak up: the virtual users' forum at the 2013 international brain-computer interface meeting",
    36: "Fully implanted brain-computer interface in a locked-in patient with ALS",
    37: "Longevity of a brain-computer interface for amyotrophic lateral sclerosis",
    38: "Assessment of safety of a fully implanted endovascular brain-computer interface for severe paralysis in 4 patients",
    41: "Home use of a percutaneous wireless intracortical brain-computer interface by individuals with tetraplegia",
    52: "Shared control of bimanual robotic limbs with a brain-machine interface for self-feeding",
    59: "Brain-computer interface control of stepping from invasive electrocorticography upper-limb motor imagery in a patient with quadriplegia",
    65: "Disentangling function from benefit: participant perspectives from an early feasibility trial for a novel visual cortical prosthesis",
    66: "The role of scalp EEG recordings during cortical visual prosthesis testing",
    72: "Enhanced system robustness of asynchronous BCI in augmented reality using steady-state motion visual evoked potential",
    76: "Brain-computer interface-controlled exoskeleton training for lower-limb rehabilitation in spinal cord injury: a pilot randomized clinical trial",
    77: "Control of an ambulatory exoskeleton with a brain-machine interface for spinal cord injury gait rehabilitation",
    80: "Passive brain-computer interfaces for enhanced human-robot interaction",
    86: "Electrophysiological characterisation of commercial ear-EEG devices",
    92: "Adaptive automation triggered by EEG-based mental workload index: a passive brain-computer interface application in realistic air traffic control environment",
    93: "Brain-computer interface-based adaptive automation to prevent out-of-the-loop phenomenon in air traffic controllers dealing with highly automated systems",
    51: "Ten-dimensional anthropomorphic arm control in a human brain-machine interface: difficulties, solutions, and limitations",
}

CONF = {
    62: "2024 46th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC)",
    86: "2025 47th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC)",
}

# 非期刊来源(GB/T 7714 EB/OL / DB/OL)
ACCESS = "2026-08-22"
NONJOURNAL = {
    1: "FDA. Implanted brain-computer interface devices for patients with paralysis or amputation: non-clinical testing and clinical considerations[EB/OL]. (2021-05-20)[2026-08-22]. https://www.fda.gov/regulatory-information/search-fda-guidance-documents/implanted-brain-computer-interface-bci-devices-patients-paralysis-or-amputation-non-clinical-testing",
    19: "Neurable. MW75 Neuro[EB/OL]. (2026)[2026-08-22]. https://www.neurable.com/products/mw75neuro",
    22: "国家药品监督管理局. 首款侵入式脑机接口医疗器械获批上市[EB/OL]. (2026-03-13)[2026-08-22]. https://yjj.sh.gov.cn/zjyw/20260313/04985a5fbe284e9c806ff5f370cb00b2.html",
    34: "Apple. Use Switch Control to navigate your iPhone, iPad, or iPod touch[EB/OL]. (2026)[2026-08-22]. https://support.apple.com/en-us/119835",
    39: "Synchron. Synchron debuts first thought-controlled iPad experience using Apple's new BCI Human Interface Device Protocol[EB/OL]. (2025-08-04)[2026-08-22]. https://www.businesswire.com/news/home/20250804537175/en/Synchron-Debuts-First-Thought-Controlled-iPad-Experience-Using-Apples-New-BCI-Human-Interface-Device-Protocol",
    53: "ClinicalTrials.gov. CONVOY (NCT06710626)[DB/OL]. (2024)[2026-08-22]. https://clinicaltrials.gov/study/NCT06710626",
    54: "Neuralink. CONVOY Study Launch[EB/OL]. (2024-11-08)[2026-08-22]. https://neuralink.com/updates/convoy-study-launch/",
    57: "国家药品监督管理局医疗器械技术审评中心. 植入式脑机接口手部运动功能代偿系统技术审评报告（受理号 CQZ2600324、CQZ2600325）[EB/OL]. (2026)[2026-08-22]. https://www.cmde.org.cn/directory/web/cmde/images/1775031381651060289.pdf",
    69: "U.S. Food and Drug Administration. Evaluation of automatic class III designation for Neurolutions IpsiHand (De Novo DEN200046)[EB/OL]. (2021-04-23)[2026-08-22]. https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN200046.pdf",
    75: "g.tec medical engineering GmbH. BCI product catalog[EB/OL]. (2018)[2026-08-22]. https://gtec.at/wp-content/uploads/2019/10/gtec-Product-Catalog-2018-web.pdf",
    82: "NextSense. Smartbuds[EB/OL]. (2026)[2026-08-22]. https://nextsense.io/products/smartbuds",
    87: "IDUN Technologies. IDUN Guardian[EB/OL]. (2026)[2026-08-22]. https://iduntechnologies.com/idun-guardian",
    88: "EMOTIV. MN8 Quick Start Guide[EB/OL]. (2026)[2026-08-22]. https://www.emotiv.com/quick-start-guide-mn8",
}
# 无作者/新闻 + PeerJ(需手补)
NONJOURNAL[56] = "China approves brain chip to overcome paralysis[J]. Nature Biotechnology, 2026, 44(4):497."
NONJOURNAL[96] = "Williams N S, McArthur G M, de Wit B, et al. A validation of Emotiv EPOC Flex saline for EEG and ERP research[J]. PeerJ, 2020, 8:e9713."

def fmt_authors(authors):
    if len(authors) > 3:
        return ", ".join(authors[:3]) + ", et al"
    return ", ".join(authors)

final = {}
for n in range(1, 98):
    if n in NONJOURNAL:
        final[n] = NONJOURNAL[n]
        continue
    r = by_num[n]
    meta = r["meta"]
    journal = JNAME.get(meta["journal"], meta["journal"])
    authors = fmt_authors(meta["authors"])
    title = TITLE_OVERRIDE.get(n, meta["title"].rstrip('.'))
    year = YEAR_OVERRIDE.get(n, meta["year"])
    vol = VOLUME_OVERRIDE.get(n, meta["volume"])
    issue = ISSUE_OVERRIDE.get(n, meta["issue"])
    page = PAGE_OVERRIDE.get(n, meta["page"])
    if n in CONF:
        final[n] = f"{authors}. {title}[C]//{CONF[n]}. {year}: {page}."
    elif issue:
        final[n] = f"{authors}. {title}[J]. {journal}, {year}, {vol}({issue}):{page}."
    else:
        final[n] = f"{authors}. {title}[J]. {journal}, {year}, {vol}:{page}."

# 保存最终列表
with open("refs_final2.txt", "w", encoding="utf-8") as f:
    for n in range(1, 98):
        f.write(f"[{n}] {final[n]}\n")
print("已生成 refs_final2.txt，共", len(final), "条")
# 校验是否有缺项
missing = [n for n in range(1,98) if n not in final]
print("缺项:", missing)
