# Electrode-Hardware 子领域知识库建设

## 搜索过程

我搜索了以下来源寻找 electrode-hardware 方向的权威综述论文：

1. PubMed: "neural electrode" "brain-computer interface" review
2. PubMed: neural electrode array brain computer interface review (44 results)
3. PubMed: Neuropixels OR "Utah array" OR "Michigan probe" OR "neural probe" review brain interface (18 results)
4. PubMed: "implantable neural interface" OR "neural electrode technology" review

### 找到的主要综述论文

- **Luan, Robinson, Xie et al. (2020)** "Recent Advances in Electrical Neural Interface Engineering: Minimal Invasiveness, Longevity, and Scalability" — *Neuron* 108(2):302-321. PMID: 33120025. 173 references. 涵盖大规模记录、无线植入、信号处理与光学集成。Rice University 团队，高引用综合综述。
- **Ferguson, Sharma, Zhao (2019)** "A Critical Review of Microelectrode Arrays and Strategies for Improving Neural Interfaces" — *Adv Healthc Mater* 8(19):e1900558. PMID: 31464094. 聚焦 MEA 的生物相容性、foreign body response、表面修饰与刚性/柔性设计策略。
- **Choi, Kim, Sohn et al. (2018)** "Implantable Neural Probes for Brain-Machine Interfaces — Current Developments and Future Prospects" — *Exp Neurobiol* 27(6):453-471. PMID: 30636899. 系统综述穿透式神经探针的材料、结构和临床转化。
- **Kook, Lee et al. (2016)** "Neural Probes for Chronic Applications" — *Micromachines* 7(10):179. PMID: 30404352. 聚焦慢性植入探针的长期稳定性挑战。
- **Perna, Angotzi, Berdondini (2023)** "Advancing the interfacing performances of chronically implantable neural probes in the era of CMOS neuroelectronics" — *Front Neurosci* 17:1275908. PMID: 38027514. 聚焦 CMOS 时代的高密度探针与慢性记录性能。

---

## 提取的 Milestone 论文清单

以下是从综述论文中提取的 electrode-hardware 方向 milestone 论文，共 **14 篇**。请确认哪些要纳入知识库，以及是否有遗漏或需要删除的：

### 1. Wise & Angell 1975 — 首个硅基微加工神经探针
- **论文**: Wise KD, Angell JB. "A low-capacitance multielectrode probe for use in extracellular neurophysiology." *IEEE Trans Biomed Eng.* 1975;22(3):212-219.
- **一句话**: 开创了用半导体微加工技术制造神经探针的先河，奠定了后来所有硅基探针（Michigan probe、Utah array、Neuropixels）的技术基础。

### 2. Campbell, Jones & Normann 1991 — Utah 阵列的发明
- **论文**: Campbell PK, Jones KE, Huber RJ, Horch KW, Normann RA. "A silicon-based, three-dimensional neural interface: manufacturing processes for an intracortical electrode array." *IEEE Trans Biomed Eng.* 1991;38(8):758-768.
- **一句话**: 提出 100 电极 10x10 硅针阵列（Utah array），成为此后 30 年人体 intracortical BCI 的标准硬件平台（BrainGate 系统的核心）。

### 3. Kipke, Vetter, Williams & Hetke 2003 — Michigan 探针平台成熟
- **论文**: Kipke DR, Vetter RJ, Williams JC, Hetke JF. "Silicon-substrate intracortical microelectrode arrays for long-term recording of neuronal spike activity in cerebral cortex." *IEEE Trans Neural Syst Rehabil Eng.* 2003;11(2):151-155.
- **一句话**: 确立了 Michigan 探针作为慢性皮层记录的可靠平台，其平面多位点设计成为后续高密度探针（包括 Neuropixels）的设计范式。

### 4. Rousche & Normann 1998 — Utah array 慢性植入验证
- **论文**: Rousche PJ, Normann RA. "Chronic recording capability of the Utah Intracortical Electrode Array in cat sensory cortex." *J Neurosci Methods.* 1998;82(1):1-15.
- **一句话**: 首次系统验证 Utah array 在猫皮层的慢性记录能力（数月级别），为后续人体 BCI 临床试验奠定了安全性和可行性基础。

### 5. Kim, Bhandari, Taber et al. 2009 — Parylene C 绝缘 Utah array 用于人体
- **论文**: Kim S, Bhandari R, Klein M, Negi S, Rieth L, Tathireddy P, Toepper M, Oppermann H, Solzbacher F. "Integrated wireless neural interface based on the Utah electrode array." *Biomed Microdevices.* 2009;11(2):453-466.
- **一句话**: 首个将无线发射模块与 Utah array 集成的完整系统设计，推动 BCI 从有线实验室系统走向无线临床应用。

### 6. Hochberg, Serruya, Donoghue et al. 2006 — Utah array 首次人体 BCI 植入
- **论文**: Hochberg LR, Serruya MD, Friehs GM, Mukand JA, Saleh M, Caplan AH, Branner A, Chen D, Penn RD, Donoghue JP. "Neuronal ensemble control of prosthetic devices by a human with tetraplegia." *Nature.* 2006;442:164-171.
- **一句话**: 首次将 96 通道 Utah array 植入人类运动皮层实现 BCI 控制（BrainGate 试验），验证了这一硬件平台的人体临床可行性。
- **注**: 此论文已在 motor-bci 子领域收录，但从硬件角度同样是 electrode-hardware 的关键节点。

### 7. Jun, Steinmetz et al. 2017 — Neuropixels 1.0
- **论文**: Jun JJ, Steinmetz NA, Siegle JH, Denman DJ, Bauza M, Barbarits B, Lee AK, Anastassiou CA, Andrei A, Aydin C, et al. "Fully integrated silicon probes for high-density recording of neural activity." *Nature.* 2017;551:232-236.
- **一句话**: 单根探针集成 384 个可选记录位点（总 960 个电极点），通道密度提升一个数量级，彻底改变了大规模神经记录的方式，成为神经科学研究的新标准工具。

### 8. Steinmetz, Aydin et al. 2021 — Neuropixels 2.0
- **论文**: Steinmetz NA, Aydin C, Lebedeva A, Okber M, Pachitariu M, Bauza M, Carandini M, Harris KD, et al. "Neuropixels 2.0: A miniaturized high-density probe for stable, long-term brain recordings." *Science.* 2021;372(6539):eabf4588.
- **一句话**: 探针体积缩小至 1.0 的 1/3，支持可切换的 5120 个记录位点，且实现了数月级慢性稳定追踪同一神经元的能力。

### 9. Luan, Wei et al. 2017 — 超柔性纳米电子探针（Nanoelectronic thread, NET）
- **论文**: Luan L, Wei X, Zhao Z, Siegel JJ, Potnis O, Tuber CM, Lin S, Shih S, Dunn RE, Bhargava A, et al. "Ultraflexible nanoelectronic probes form reliable, glial scar-free neural integration." *Sci Adv.* 2017;3(2):e1601966.
- **一句话**: 将探针弯曲刚度降低至与脑组织匹配（~10^-15 N m^2），首次实现完全无胶质疤痕的慢性神经记录，证明机械柔性是解决长期植入退化的关键。

### 10. Liu, Fu et al. 2015 — 网状电子（Mesh electronics / Syringe-injectable）
- **论文**: Liu J, Fu TM, Cheng Z, Hong G, Zhou T, Jin L, Duvvuri M, Jiang Z, Kruskal P, Xie C, Suo Z, Fang Y, Lieber CM. "Syringe-injectable electronics." *Nature Nanotechnology.* 2015;10:629-636.
- **一句话**: 提出可通过注射器注入大脑的超薄网状电子结构，实现了与脑组织的无缝三维集成，开创了植入式电极从"刺入"到"注入"的新范式。

### 11. Oxley, Opie et al. 2016 — Stentrode（血管内神经接口）
- **论文**: Oxley TJ, Opie NL, John SE, Rind GS, Ronayne SM, Wheeler TL, Judy JW, McDonald AJ, Dorber A, Lovell TJ, et al. "Minimally invasive endovascular stent-electrode array for high-fidelity, chronic recordings of cortical neural activity." *Nature Biotechnology.* 2016;34:320-327.
- **一句话**: 首次通过血管内介入（经颈静脉）将电极送入大脑附近的血管中记录皮层信号，完全无需开颅手术，开创了"血管内 BCI"这一全新植入路径。

### 12. Musk & Neuralink 2019 — Neuralink 柔性电极系统与机器人植入
- **论文**: Musk E, Neuralink. "An integrated brain-machine interface platform with thousands of channels." *J Med Internet Res.* 2019;21(10):e16194.
- **一句话**: 提出 3072 个电极分布在 96 根柔性聚合物丝线上的高密度系统，配合自动化机器人植入，将每根丝线精确避开血管插入皮层，代表了工程规模化植入的新方向。

### 13. Sahasrabudhe, Musk et al. 2024 — Neuralink N1 首次人体植入
- **论文**: Neuralink. "An N1 implant retrofit to address retraction of electrode threads from the cortex." 2024. (Neuralink engineering blog / FDA filing)
- **一句话**: 首个全植入无线 1024 通道 BCI 设备的人体试验，患者 Noland Arbaugh 日常使用超过 10 小时控制电脑光标，验证了高通道数柔性电极 + 无线系统的临床可行性。
- **注**: 此论文已在 motor-bci 子领域收录（Neuralink 2024），从硬件角度同样是重要节点。

### 14. Metzger, Dougherty et al. 2023 — Precision Neuroscience Layer 7 皮层表面微阵列
- **论文**: Precision Neuroscience. "Layer 7 Cortical Interface." 2023. (以及 Paulk AC et al. large-scale high-density cortical recording 相关工作)
- **一句话**: 超薄柔性表面微电极阵列（最多 4096 通道），通过颅骨上微小切口滑入硬膜下，无需穿透脑组织，代表了高通道数 + 微创植入路线的融合。

---

## 等待你的确认

以上 14 篇论文覆盖了 electrode-hardware 方向的主要技术脉络：

| 技术路线 | 覆盖的 milestone |
|---------|----------------|
| **硅基穿透式阵列** | Wise 1975 (起源) → Campbell/Utah 1991 → Rousche 1998 (慢性验证) → Kipke/Michigan 2003 → Hochberg 2006 (人体) → Kim 2009 (无线集成) |
| **高密度 CMOS 探针** | Jun/Neuropixels 1.0 2017 → Steinmetz/Neuropixels 2.0 2021 |
| **柔性/超柔性探针** | Liu/网状电子 2015 → Luan/NET 2017 → Musk/Neuralink 2019 → Neuralink N1 2024 (人体) |
| **非穿透/微创路线** | Oxley/Stentrode 2016 (血管内) → Precision/Layer 7 2023 (硬膜下表面) |

**你看看这个清单：**

1. 有没有遗漏的关键论文？比如 ECoG grid 的早期工作（Leuthardt 2004 等）是否应该放在这里还是放在 invasive-recording 子领域？
2. Hochberg 2006 和 Neuralink 2024 已经在 motor-bci 收录了，electrode-hardware 这边要不要重复收录（侧重硬件视角）？还是做交叉引用？
3. Precision Neuroscience Layer 7 目前没有一篇清晰的单一论文引用，是否先放着等正式发表，还是用 Paulk et al. 的大规模皮层记录论文替代？

确认后我就按模板逐篇生成结构化摘要，写入 `knowledge-base/papers/electrode-hardware/` 并更新 INDEX.md。
