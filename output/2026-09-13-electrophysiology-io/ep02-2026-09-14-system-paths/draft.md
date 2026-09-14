# 电生理采集的信息通路概览

更新日期：2026-09-14。全文初稿已落完（一、二、三、结语），待通读与拆卡。封面标题「电生理采集的信息通路概览」；封面导语「闭环实验里，判断放在采集设备上还是电脑上，差别在哪里？」（2026-09-14 定）。

## 已定稿

系列定位：承接第一期的需求与验收清单，解释谁完成各项任务、彼此传什么。完成后交给第三期核对电气连接条件。

### 一、系统必须完成哪些职责

第一期写清了要测什么。接下来的问题是：这些事由谁来做？

本期以一类闭环实验为例。Roux 等人 2017 年发表在《Nature Neuroscience》上的研究中，研究者在小鼠背侧海马 CA1 区（dorsal CA1）植入硅探针，实时检测清醒期的尖波涟漪（sharp-wave ripple，SPW-R），每检出一次，就经探针上的光纤给一个 60 ms 的光脉冲¹。下文的「检测到特定神经活动即给光」都指这类闭环。

先把实验系统要完成的任务分开。划分依据是信息在物理量与数值之间的转换方向，由此得到四项职责：

| 职责 | 转换方向 | 闭环实例 |
| --- | --- | --- |
| **生成** | 数值 → 作用于动物的物理量 | 设定值变成实际照到组织上的光 |
| **测量** | 物理量 → 数值 | 电位、画面、实际光强变成采样值 |
| **判断** | 数值 → 决定后续生成的数值 | 检测到特定神经活动，得出「给光」 |
| **保存** | 数值 → 留存供事后分析 | 神经数据、视频、判定记录写入文件 |

生成包含从指令到实际施加输入的全过程，本期把它作为一个整体。

判断与保存都是从数值到数值。区别在于，判断的结果会改变后续的生成，保存的结果不会。

这里的判断，指系统根据测得的数值自动决定后续生成，全程无人参与。因此，只有闭环实验需要判断；开环实验只有生成、测量、保存三项。实验者看屏幕后手动调整刺激，属于系统外部的操作，它对系统的影响只体现为生成的设定值发生变化，这一改动的时刻与数值也要保存。

四项职责按任务划分，与设备无一一对应关系：一台设备可以同时承担多项职责。

### 二、职责怎样分配

同一份需求，职责分配到设备上的方式不止一种。同一台设备完成的职责，信息在设备内部传递；分到两台设备上，信息就要跨设备传递。因此，职责放在哪里，决定了哪些信息需要连接。

那么，哪些职责的位置可以选？

- **生成和测量**需要一条物理通路连到实验对象，例如光纤、导线或光学路径。作用点是固定的：光必须照到目标脑区，电位必须在电极处取得。设备本身可以放在远处，位置受这条通路的条件限制。
- **判断和保存**只处理数值，可以放在任何一台收得到数据、算得了或存得下、并且处理得够快的设备上。

两项可选的职责中，本期只挪判断。闭环的控制通路是测量 → 判断 → 生成，判断位于中间；保存不在这条通路上，本例把它固定在电脑上。

下面固定测量、生成、保存三项，比较两种示意方案：

| 职责 | 方案 A：判断在采集设备上 | 方案 B：判断在电脑上 |
| --- | --- | --- |
| 测量 | 采集设备 | 采集设备 |
| 判断 | 采集设备内部完成检测 | 电脑上的软件完成检测 |
| 生成 | 光源驱动与光源 | 光源驱动与光源 |
| 保存 | 电脑 | 电脑 |

两个方案里，神经数据都要送到电脑保存。区别在于给光这一步：要不要等数据先到电脑、判断完成，再把结果送回光源驱动。

> 注（小字）：开头引用的 Roux 等人的实验，神经信号由 Amplipex 记录系统采集，其中一个通道另外送入 TDT RX6 处理器完成检测¹。判断放在独立于采集设备的另一台处理器上，与 A、B 两种方案都不同。

#### 分配方案改变了哪条连接的用途

（图片：方案 A、B 的信息通路示意图。两边设备位置相同，只有控制箭头的路径不同；草图见 `figs-draft/ep02-sketch.png`，红色实线表示控制，蓝色虚线表示保存，灰线表示电极、光纤等物理通路；箭头表示信息方向，不代表线缆。）

对照两个方案，跨设备的连接有三条：采集设备到电脑的神经数据，摄像头到电脑的行为视频，以及送到光源驱动的给光指令。前两条的起点与终点在两个方案中相同，第三条只是发送端不同。单看连线，A 与 B 几乎一样。

区别在于每条连接承担的用途：

| 连接 | 方案 A | 方案 B |
| --- | --- | --- |
| 采集设备 → 电脑（神经数据） | 保存 | **控制 + 保存** |
| 摄像头 → 电脑（行为视频） | 保存 | 保存 |
| → 光源驱动（给光指令） | 控制，由采集设备发出 | 控制，由电脑发出 |

判断移到电脑上之后，采集设备到电脑这条原本只用于保存的连接，进入了控制通路：测量 → 采集设备 → 电脑（判断）→ 光源驱动 → 光。

也就是说，连线的起点和终点没有变，变的是这条连接的用途。

### 三、连接要求与判断的两种实现

#### 1. 用途变了，要求随之改变

**用于保存时，要求事后能对齐。** 延迟固定，属于第一期所说的系统误差，测出后可以扣除；延迟每次不同，属于随机误差，只能减小。数据晚到多少，不影响实验本身，只影响事后分析的对齐精度。

**用于控制时，要求及时送达。** 这时延迟无法事后扣除：光照到组织的时刻已经发生，校正记录改变不了光落在事件的哪个时间点。要看两件事：

- **延迟多大。** 参照被检测事件本身的持续时间。延迟超过事件持续时间，光就落在事件结束之后。
- **延迟是否稳定。** 延迟固定，每次光落在事件内的相对位置相同，结果可以统一解释；延迟波动，有的光落在事件中，有的落在事件后，同一组试次混入了不同的刺激时机。

因此，同一条连接从保存进入控制之后，延迟的大小与稳定性就决定了实验能否成立。

#### 2. 两种方案怎样完成「收数据 → 判断 → 输出」

仍以检测到涟漪即给光为例，看两种方案各自经过哪些步骤。

**判断在电脑上**，要经过六步，每一步都可能增加延迟：

1. 采集设备把信号数字化；
2. 数据按块打包，经 USB 或以太网传到电脑，其间有缓冲等待与传输时间²；
3. 操作系统把数据交给软件，受系统调度影响；
4. 软件逐块运行检测算法；
5. 经外接的微控制器发出数字脉冲；
6. 光源驱动收到脉冲。

**判断在采集设备上**，只有三步：

1. 数字化；
2. 在同一台设备的现场可编程门阵列（field-programmable gate array，FPGA）或数字信号处理器（digital signal processor，DSP）上直接运行检测，没有跨设备传输，也没有操作系统介入；
3. 由设备自身的数字输出口送出脉冲。

FPGA 是一类出厂后可以重新配置内部逻辑电路的芯片。运算以电路的形式并行执行，每个样本的处理时间固定。DSP 是专门用于数字信号运算的处理器。

两种方案都有一段相同的**检测延迟**：算法需要一段足够长的信号才能作出判定。这段延迟由算法与信号本身决定，与判断放在哪台设备上无关。

所以，从事件开始到刺激实际施加（本例中即光亮起），总延迟由三部分组成：检测延迟、系统延迟，以及光源驱动的响应时间。判断放在哪里，只改变其中的系统延迟。

#### 3. 常见系统实例

**判断在采集设备上**

- **Intan**：Intan 公开的采集接口方案 Rhythm USB-7310，用 Verilog 代码配置一块 Xilinx FPGA，由它控制前端放大芯片采样，再经 USB 3.0 把数据送到电脑³。选定的通道可以在 FPGA 内部直接送到数模转换器输出，不经过 USB 与电脑。FPGA 上还实现了阈值比较器：波形超过设定阈值，数字输出口即给出高电平；比较前可以先用 FPGA 上的高通滤波去掉局部场电位（local field potential，LFP），再检测动作电位³。Intan 的 RHD 记录控制器同样提供低延迟的阈值比较数字输出⁴。这类判断限于阈值比较。
- **Müller 等人的系统**：高密度互补金属氧化物半导体微电极阵列（CMOS-MEA）接到 FPGA 上，由 FPGA 完成动作电位检测与反馈刺激的生成。实验对象为大鼠胚胎（E18）皮层神经元的离体培养⁵。
- **TDT**：Synapse 软件中的功能模块在编译实验时分配到处理器内的 DSP 上运算⁶，可以设置检测动作电位并控制脉冲输出⁷。开头 Roux 等人的实验，就由 TDT RX6 处理器完成涟漪检测¹。

**判断在电脑上**

- **Open Ephys GUI**：数据处理全部在软件中完成；官方闭环示例中，由外接的 Arduino 配合 GUI 内的 Arduino Output 插件输出反馈信号²。
- **Trodes**：Dutta 等人在这一开源采集软件中加入涟漪检测模块，检测到涟漪后，由经以太网连接的 BeagleBone Black 微控制器发出数字脉冲。前端为 Intan RHD2000 系列 headstage，分别接入经 USB 2.0 传输的 Open Ephys 采集板与经千兆以太网传输的 SpikeGadgets 主控单元。实验对象为 1 只雄性 Long Evans 大鼠⁸。
- **BRAND**：人体皮层内脑机接口平台，运行在带实时补丁（PREEMPT_RT）的 Linux 上。BrainGate2 临床试验受试者 T11 用它完成光标控制任务，30 kHz 信号处理、循环神经网络（recurrent neural network，RNN）解码、任务控制与图形显示都在其中执行⁹。

#### 4. 两种方案的差异

| | 判断在采集设备上（FPGA / DSP） | 判断在电脑上（软件） |
| --- | --- | --- |
| **系统延迟** | 可到亚毫秒。Müller 等人的系统最小可编程闭环延迟为 400 μs⁵ | 取决于传输方式。Dutta 等人用同一套软件测得：USB 采集硬件 7.5–13.8 ms，以太网 1.35–2.6 ms⁸ |
| **稳定性** | 运算按固定时序执行，抖动小。Müller 等人报告抖动小于 50 μs⁵ | 受缓冲与操作系统调度影响。Open Ephys 示例的延迟分布在 0–27 ms² |
| **实现难度** | 需要编写硬件描述语言，修改算法慢 | 用常规编程语言，便于修改和迭代 |
| **可运行的算法** | 受芯片资源限制，常见的是阈值比较、滤波 | 可运行复杂模型。BRAND 在人体脑机接口中运行 RNN 解码，从输入神经数据到输出预测不到 8 ms⁹ |

> 注（小字）：表中数值来自不同的系统、样本与配置，只用于说明数量级差异，不宜逐项直接比较。

由此，选择判断放在哪里，看两件事：实验允许多大的延迟，算法有多复杂。电脑端的系统延迟已经远小于事件持续时间时，放在电脑上可以保留算法的灵活性；需要亚毫秒级延迟、抖动极小时，就要放在采集设备上。

系统延迟也常常不是延迟的主要来源。Dutta 等人报告，涟漪持续约 100 ms；使用以太网采集硬件、每分钟误检少于 10 次时，检测算法本身的延迟约为 20–66 ms，并随阈值参数变化⁸。这部分延迟与判断放在哪里无关。

### 结语

从实验系统必须完成的四项职责出发，本期先说明判断的位置可以选择，再比较判断放在采集设备上与电脑上两种方案：同一条连接进入控制通路后，延迟的大小与稳定性决定实验能否成立；两种方案在系统延迟、稳定性、实现难度与可运行的算法上各有差异。

回到图中的三条连接，先看每条连接传的是什么信息，再看可以用什么形式传：

| 连接 | 信息类型 | 常见传输形式 | 本期实例 |
| --- | --- | --- | --- |
| 采集设备 → 电脑（神经数据） | 连续量，多通道 | 通信接口，以数据包传输 | Open Ephys 采集板经 USB 2.0，SpikeGadgets 主控单元经千兆以太网⁸ |
| 摄像头 → 电脑（行为视频） | 连续量 | 通信接口 | — |
| → 光源驱动（给光指令） | 离散事件 | 数字输出 → 数字输入 | Intan 阈值比较器的数字输出³，BeagleBone Black 发出的数字脉冲⁸ |

四个术语：

- **模拟**：用连续变化的电压表示数值。
- **数字 IO**：用高低电平表示状态或事件。
- **通信接口**：按约定的协议传输数据包。
- **输入与输出**：相对某一台设备而言。同一条连接，在发送端是输出，在接收端是输入。

接口候选不是唯一的。同一份神经数据，Intan 的设备既可以经 USB 以数据包形式送到电脑，也可以把选定通道重新转换为电压，从模拟输出口实时送出，用于示波器观察或声音监听⁴。两端怎样连接才能正确传递、每类接口怎样工作，留到后续各期。

## 成品（2026-09-14）

15 张：本目录 cards/01-cover … 14-c12 / 15-tail。生成脚本 `.claude/skills/dailybci/scripts/series/build_ioreq2_cards.py`，示意图脚本 `ioreq2_figs.py`（复用 grounding2_figs 与 ioreq1_figs 的 render）。自制图 9 张：cover-concept、toc、fig1 闭环实例、fig2 四项职责表、fig3 A/B 表、fig4 信息通路、fig5 步骤与延迟构成、fig6 差异对比表、fig7 接口候选表。

卡序：封面 → 目录（导读）→ ① 以闭环实验为例 / 四项职责 → ② 位置可选 / A/B 两方案 / 连接用途变化 → ③ 要求变化 / 步骤与延迟构成 / 采集端实例 / 电脑端实例 / 差异对比 / 怎样选择 / 接口候选 → 尾卡（9 条参考文献）。

与草稿的差异：结语复述段压成尾卡一句；接口候选并入第 14 张；「用于示波器观察或声音监听」按 Intan 手册原文收为「用于声音监听」；FPGA 定义并入第 9 张。封面用自制概念图（原理期例外）。已逐张 Read 验收，页脚无溢出。

## 讨论中

### 核心问题

主线（2026-09-14 确认）：职责放在哪里，决定哪些信息需要跨设备传递。

### 大纲（2026-09-14 第二次修订）

1. **系统必须完成哪些职责？**（已定稿）生成、测量、判断、保存。
2. **职责怎样分配？**（已定稿）固定测量、生成、保存，只改变判断位置，比较 A/B 两种示意方案。实例统一挪到第三部分，本部分只留 A/B 表与 Roux 小字注。
3. **判断放在哪里：两种实现的差异**
   - 3.1 同一条连接，用途变了（已定稿）
   - 3.2 用途变了，要求随之改变（已定稿）
   - 3.3 基本原理：电脑端与采集端分别怎样完成「接收数据 → 判断 → 输出」。电脑端的延迟来自传输与缓冲（Open Ephys 原文），与传输方式、操作系统有关（Dutta 2019：以太网 vs USB 2.0）；采集端靠 FPGA 或 DSP，按固定时序执行。补充检测延迟：算法需看到足够长的信号才能判定，与判断位置无关（Dutta 2019：检测延迟约 80% 在 20–66 ms，比系统延迟大一个数量级）。
   - 3.4 常见系统实例：采集端 Intan（FPGA 阈值比较器，重点）、Müller 2012（FPGA，400 μs、抖动 <50 μs，大鼠离体培养）、TDT（DSP，回扣 Roux）；电脑端 Open Ephys、Trodes（Dutta 2019）、BRAND（人体 iBCI，<8 ms）。
   - 3.5 对比表与优缺点小结：系统延迟、稳定性、实现难度、算法复杂度；选择取决于允许的延迟与算法需求。
4. **结语与交接**：每条连接上传的是连续量还是离散事件，据此给出接口候选（模拟／数字 IO／通信接口／设备内部），模拟、数字、输入、输出简短定义，细节交给后续各期。

### 本期边界

- 跨设备会产生接口与时间关系的要求；物理线缆数量和实际延迟不能直接预判：已有通信连接可能承载新增信息，延迟取决于传输、处理与设备实现，需实例核实。
- 第三部分讲「为什么有差异、各适合什么场景」；延迟的测量方法与各环节数值分配留到第七期，避免重叠。
- 时间关系只分「及时送达 / 事后能对齐」两类。
- 四类接口的解释控制在一张卡以内，只给定义与方向约定，不讲模数、数模转换机制（与 2026-09-07 已发《模拟口与数字口辨析（上）》避免重复）。
- 产品对照留到第八期。
- 本期能力目标：能根据系统任务提出合理的接口候选，并知道还要核对哪些条件；完成选型需要后续各期的知识。
- 向第三期交接：已明确要传什么、候选接口是什么，两端怎样连接才能正确传递。

## 备用素材

- Roux 2017 的实际分配（原文已核，见 ep01 draft 备用素材表）：神经记录由 Amplipex 256 通道系统完成，单个通道另送入 TDT RX6 的 DSP 做 ripple 检测。也就是说，判断放在独立于记录设备的第三台处理器上，与本期 A、B 两种示意方案都不完全相同；正文第二部分末以小字注说明。
- Open Ephys 闭环示例实测往返延迟 0–27 ms、均值 14 ms（文档示例配置）；方案 A 无可比数值，留第七期。
- Intan RHS headstage 在前端完成放大、滤波与数字化（官方系统说明），可作「测量的非作用点环节可分布到不同设备」的例子。

### 第三部分已核实素材（2026-09-14）

- **Open Ephys Closed-Loop Latency 文档**（官网逐句核）：「all of the data processing happens in software」；「moves data around using buffers」；USB 缓冲「set to 10 ms at 30 kHz」，Ethernet 或 PCIe 可用更小缓冲；一般预期 20–30 ms；示例 0–27 ms，均值 14 ms。
- **Dutta S., Ackermann E., Kemere C.**（bioRxiv 298661 原文逐句核；正式版 J Neural Eng 2019 16(1):016009 仅见检索结果，待核期刊页）：Trodes 电脑端 SWR 检测模块，经以太网连接的 BeagleBone Black 输出脉冲；前端均为 Intan RHD2000，30 kHz；SpikeGadgets（千兆以太网）80% 闭环延迟 1.35–2.6 ms，Open Ephys（USB 2.0）7.5–13.8 ms；体内检测延迟约 80% 在 ≈20–66 ms；1 只雄性 Long Evans 大鼠。SWR「≈100 ms」为检索摘要，待逐字核。
- **TDT**（官网逐句核）：光遗传页「configure Synapse to detect spiking events (PCA spike sorting) to control the output of the Pulse Generator Gizmo」；Synapse Troubleshooting「Each gizmo gets assigned to a DSP when Synapse compiles an experiment」「DSP cards inside of it that do all the computational heavy lifting」。
- **Intan RHD 记录控制器用户手册**（PDF 逐句核）：「Low-latency digital threshold comparators for real-time spike detection」；比较器作用于送往模拟输出的信号；模拟输出「< 0.2 ms latency」（比较器本身无数值）。**Rhythm USB-7310 文档**：Verilog 配置 Opal Kelly XEM7310 上的 Xilinx Artix-7 FPGA；通道经 FPGA 直送 DAC「eliminating any USB or host computer latency」。
- **Müller J., Bakkum D.J., Hierlemann A.**（Frontiers in Neural Circuits 6:121，网页逐句核）：CMOS-MEA 接 Xilinx Virtex II Pro FPGA，检测与反馈在 FPGA 上；最小可编程闭环延迟 400 μs，抖动 <50 μs；大鼠 E18 皮层神经元离体培养。年份检索显示 2012/2013 不一致，待核。
- **BRAND**（PMC11021878，网页摘录）：进程间 <600 μs（1024 通道 30 kHz、1 ms 块）；RNN 解码从输入到预测 <8 ms；Ubuntu 20.04 + PREEMPT_RT；BrainGate2 受试者 T11 光标控制全部在 BRAND 中运行。待逐字核。
- **Hogan et al. 2026, arXiv 2602.11632**（Cortical Labs，PDF 逐句核，利益相关）：FPGA 系统「slow development times with limited transparency」；纯 Python 方案「relatively slow and variable response latencies of >60 ms」。
- **Aleman-Zapata A., van der Meij J., Genzel L. (2022) J Sleep Res 31(6):e13532**：综述未统计各研究所用检测系统，仅称方法差异大（网页摘录）。结论：无「主流」统计依据。
- **NeuroPace RNS**（Bergey 2015 Neurology 84(8):810–817，摘录未逐字核）：植入设备自身检测并刺激；留第八期。

## 参考文献

1. Roux L., et al. (2017). Sharp wave ripples during learning stabilize the hippocampal spatial map. Nature Neuroscience 20(6):845–853.
2. Open Ephys. (n.d.). Closed-Loop Latency. Open Ephys GUI Documentation. https://open-ephys.github.io/gui-docs/Tutorials/Closed-Loop-Latency.html
3. Intan Technologies. (2025). RHD XEM7310 Interface: Rhythm USB-7310. https://intantech.com/files/Intan_RHD_XEM7310_interface.pdf
4. Intan Technologies. (2024). Intan Recording Controller User Guide. https://intantech.com/files/Intan_Recording_Controller_user_guide.pdf
5. Müller J., et al. (2012). Sub-millisecond closed-loop feedback stimulation between arbitrary sets of individual neurons. Frontiers in Neural Circuits 6:121.
6. Tucker-Davis Technologies. (n.d.). Synapse Manual – Troubleshooting. https://www.tdt.com/docs/synapse/troubleshooting/
7. Tucker-Davis Technologies. (n.d.). Optogenetic Stimulation. https://www.tdt.com/system/optogenetic-stimulation/
8. Dutta S., et al. (2019). Analysis of an open source, closed-loop, realtime system for hippocampal sharp-wave ripple disruption. Journal of Neural Engineering 16(1):016009.
9. Ali Y.H., et al. (2024). BRAND: a platform for closed-loop experiments with deep network models. Journal of Neural Engineering 21(2). doi:10.1088/1741-2552/ad3b3a

核对记录（2026-09-14，逐条对照原文）：³ Rhythm USB-7310 PDF：Verilog 配置 Xilinx FPGA、SuperSpeed USB 3.0、通道经 FPGA 直送 DAC「eliminating any USB or host computer latency」、「on-FPGA threshold comparators」、on-FPGA 高通滤波「remove low-frequency local field potentials (LFPs) … before detecting spikes」（文档 2023-03-03 首发、2025-07-30 更新）。⁴ Recording Controller 手册（2024-12-11 更新）与 RHD Controllers 页：「low-latency threshold comparators」；两份控制器文档与 RHX 软件手册均未写明控制器内部为 FPGA，故正文只把 FPGA 归于 Rhythm USB-7310。⁵ Frontiers 网页原句「an FPGA that performs signal-processing, such as spike-detection and feedback generation」「cultured networks of cortical neurons and glia」、E18 大鼠胚胎；PubMed：卷 6（2012），网络首发 2013-01-10。⁶⁷ TDT 官网原句（见备用素材）。⁸ PubMed 摘要 + bioRxiv 全文：Trodes 模块、BeagleBone Black、Intan RHD2000、Open Ephys USB 2.0 / SpikeGadgets 千兆以太网、1 只雄性 Long Evans 大鼠。3.5 所用数值一律取 PubMed 正式版摘要原文：「≈100 ms periods of large 150-250 Hz oscillations」；「a data acquisition component of 7.5-13.8 ms and 1.35-2.6 ms for USB and ethernet hardware respectively, and an algorithmic component which varies depending on the threshold parameter」；「Using ethernet acquisition hardware … an algorithmic latency in the range of ≈20-66 ms can be achieved while maintaining <10 false detections per minute」。预印本中的「80%」限定正式版摘要未写，正文不用。⁵ 400 μs、<50 μs 为 Frontiers 原句。² 0–27 ms 为 Open Ephys 文档示例原句。「修改算法慢 / 便于修改」为按实现方式的推导，无单独出处。⁹ PMC11021878 原句：PREEMPT_RT、T11、「30 kHz signal processing, RNN decoding, task control, and graphics were all executed in BRAND」。
