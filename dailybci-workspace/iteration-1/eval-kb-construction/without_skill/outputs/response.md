# Electrode-Hardware 子领域知识库构建报告

## 完成情况

已在 `/Users/zoujiajun/Desktop/dailylife/dailyBCI/knowledge-base/papers/electrode-hardware/` 目录下创建了 12 篇里程碑论文条目，覆盖电极阵列、材料、植入设计和无线系统四个方向。

## 论文列表（按时间线）

### 基础与早期硅电极
1. **Wise 1970** — 首次用IC工艺制造多位点神经探针，开启微加工电极时代
2. **Campbell 1991** — Utah阵列发明，100通道3D硅电极阵列，BCI临床试验的硬件基石
3. **Rousche 1998** — 首次系统验证Utah阵列慢性植入可行性，揭示胶质瘢痕核心挑战

### 柔性电极与新材料
4. **Kim 2010** — 可溶解丝蛋白基底+超薄共形电极（Rogers团队），开创暂态基底策略
5. **Viventi 2011** — 360通道柔性ECoG，有源多路复用解决高密度引线瓶颈
6. **Liu 2015** — 注射式网状电子器件（Lieber团队），力学匹配脑组织，颠覆刚性探针范式
7. **Luan 2017** — 超柔性纳米探针实现无胶质瘢痕神经集成，证明力学匹配是根本方案

### 高密度与CMOS集成
8. **Jun 2017 (Neuropixels)** — CMOS工艺单根探针960位点384通道，改变大规模记录可及性
9. **Musk/Neuralink 2019** — 1024通道全无线BCI平台，柔性线程+手术机器人+定制ASIC
10. **Obaid 2020** — 微线阵列直接键合CMOS芯片，万通道穿透式电极技术路线

### 无线传输系统
11. **Borton 2013** — 首个全频段宽带无线神经接口，100通道24Mbps植入式传输
12. **Simeral 2021** — 首次intracortical BCI家庭无线化使用，24小时连续运行

## 技术叙事线

这12篇论文构成了一条清晰的技术演进叙事：

**刚性到柔性**：Wise 1970 → Campbell 1991 (Utah阵列) → Kim 2010 / Liu 2015 / Luan 2017 展示了电极从手工金属丝→硅微加工→柔性薄膜→注射式网状→超柔纳米探针的演进。核心驱动力是解决慢性植入的胶质瘢痕问题（Rousche 1998首次揭示）。

**低密度到高密度**：Utah阵列100通道 → Viventi 2011多路复用360通道 → Neuropixels 960位点 → Neuralink 1024通道 → Obaid 2020万通道路线。核心挑战是引线瓶颈，解决方案从被动引线走向有源多路复用和CMOS片上集成。

**有线到无线**：BrainGate有线 → Borton 2013首个宽带无线 → Simeral 2021家庭无线使用 → Neuralink 2019全植入无线。这条线直接决定了BCI能否走出实验室。

## 格式说明

每篇论文条目完全遵循已有子领域（speech-decoding、motor-bci）的格式：
- YAML front matter：title, authors, year, venue, url, subfield, tags
- 四个标准段落：解决了什么问题、核心方法、关键数据、为什么是milestone
- 中文撰写，专业术语保留英文

INDEX.md 已更新：
- 总论文数从27更新为39
- electrode-hardware 部分从"待建设"更新为12篇论文的索引列表
