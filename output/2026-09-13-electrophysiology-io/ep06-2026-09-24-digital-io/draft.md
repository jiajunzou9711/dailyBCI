# 第六期：数字输入输出（工作标题）

文件夹日期暂按开工日 2026-09-24，交付日确定后改名。

## 大纲（2026-09-24 用户认可大体结构，细节讨论到对应位置再定）

结构沿用「用途 → 要求 → 怎么连 → 必要原理」。发指令与记事件关注点不同，不强行对称；只有有效极性是两者共用的约定，放在最前讲一次。

- **引言**：从读者已有的问题出发（怎样打 marker；事件为什么漏记、多记、对不上），先说明本期怎样回答：按用途分两类，各讲要求与接法。
- **① 数字口传什么**：只有高低两态，一个事件 = 一次电平变化；共用约定：有效极性。
- **A. 发指令（数字输出）**
  - ② 接收端怎样执行：只认跳变 / 高电平期间持续执行（此时脉宽 = 作用时长）
  - ③ 谁来定时：硬件定时稳定；软件发出受电脑调度影响
  - ④ 怎么连：并入③末尾，作接线前四项核对（2026-09-24 定）
- **B. 记事件（数字输入）**
  - ⑤ 按间隔读取：脉宽须宽于读取间隔
  - ⑥ 机械开关的抖动：一次接通被记成多个事件
  - ⑦ 事件种类多：多根线编码
  - ⑧ 怎么连：通道对应、事件保存形式
- **结语表**：漏记 ⑤ / 反相 ① / 多记 ⑥ / 编码错 ⑦ / 执行时刻不稳 ③

边界：电平阈值一句带过（不回引旧期）；事件时间与神经数据对齐留第七期。B 部分判据为「一次事件恰好一条记录且种类标对」，事件时刻只能精确到一个读取间隔这一点移交第七期（2026-09-24 定）。

待核：② 的执行方式、⑤ 的读取方式，各找一两款主流设备说明书。

## 已定稿

### 引言（2026-09-24 落稿）

做实验时，常要在神经数据里标出某件事发生的时刻：刺激何时出现，动物何时舔水，相机何时拍下一帧。脑电实验里，这一步通常叫打 marker，即事件标记（event marker）。另一些时候方向相反：检测到某个信号，要让光源在那一刻亮起。

这两件事多半经过采集设备上的数字口。用得不对，就会出现事件漏记、多记、极性反了，或者光没有在预想的时刻亮起。

本期先讲两类用途共用的基础：数字口传的是什么。然后按用途分两类，用数字口发指令和用数字口记事件，分别讲各自要满足什么、怎样连接。

### ① 数字口传什么（2026-09-24 落稿）

数字口只区分两种状态：高电平与低电平。接收端把输入电压和阈值比较，高于上阈值判为高，低于下阈值判为低。一个事件，就是一次从一种状态到另一种状态的变化。

实验室里常说的 **TTL 信号**，名字来自晶体管–晶体管逻辑（transistor-transistor logic，TTL）这一类数字芯片。它们用 5 V 供电，输入高于 2 V 判为高，低于 0.8 V 判为低¹。现在说「TTL 信号」，一般指按这套电平收发、高电平约 5 V、低电平约 0 V 的数字信号。3.3 V 供电的设备给出的高电平同样高于 2 V，也会判为高；上述手册也写明这类芯片的输入可接受 3.3 V 逻辑¹。

两端还要约定哪一种状态算「有效」，这叫**有效极性**（active polarity）。说明书里一般写作高电平有效（active high）或低电平有效（active low）。约定反了，有效和空闲就整体对调：本来空闲的时段被当成有效，事件发生时反而成了空闲。

两端约定好电平和极性，一个事件就能被正确送达。先看第一类用途：用数字输出向另一台设备发指令。指令送到之后，接收端怎样执行它？

### ② 接收端怎样执行指令（2026-09-24 落稿）

电平从一种状态跳到另一种状态的那一刻叫**边沿**（edge）：从低到高是上升沿，从高到低是下降沿。同一个脉冲，接收端可以按两种方式执行：

- **边沿触发**（edge-triggered）：只在边沿那一刻动作，例如检测到上升沿，就启动一段预先设好的输出。脉冲之后持续多久，不影响执行。
- **门控**（gated）：有效状态持续多久，就执行多久。这时脉冲宽度就是作用时长。

以 Pulse Pal 为例。它是 2014 年冷泉港实验室 Kepecs 组发布的开源可编程脉冲发生器，用于生理与行为实验中定时输出电压脉冲²。它的触发输入同时提供这两种方式：默认模式下，一个触发脉冲启动预设的脉冲序列，播放期间再来的触发被忽略；门控模式下，上升沿开始播放，下降沿停止²。

因此接线前先确认接收端用的是哪一种：边沿触发时，发送端只需把跳变的时刻发准；门控时，还要把脉冲宽度发准。

### ③ 谁决定脉冲何时发出（2026-09-24 落稿）

数字输出何时跳变，有两种决定方式³：

- **硬件定时**（hardware timing）：由设备上的时钟决定输出时刻。
- **软件定时**（software timing）：由电脑上的程序和操作系统决定，而不由采集设备决定。每条「变高」或「变低」的命令实际到达设备的时刻都有波动，每次晚多少并不相同。

以数据采集设备厂商 NI（美国国家仪器，National Instruments）为例，它为自家采集卡提供的驱动软件叫 DAQmx。DAQmx 的用户手册写明，硬件时钟比软件循环快得多，也准确得多³。

这种波动对两种执行方式的影响不同：

- **边沿触发**：接收端只看跳变的那一刻，波动只让开始时刻不准。脉冲宽度只要够接收端识别即可。
- **门控**：脉冲宽度就是作用时长。「变高」和「变低」两条命令各自波动，作用时长也跟着偏。例如用 Pulse Pal 的门控模式控制光源，脉冲宽了几毫秒，光就多照几毫秒。

因此，开始时刻有要求时，用硬件定时；门控时开始时刻和作用时长都有要求，更需要硬件定时。有些设备不支持硬件定时，要查说明书³。

接线之前，按顺序确认四件事：

1. **接收端切到外部触发**：接收端通常有多种工作方式，要切到由外部数字输入控制。
2. **执行方式**：接收端是边沿触发还是门控；门控时，脉冲宽度按作用时长来设。
3. **极性**：两端对高电平有效还是低电平有效的约定一致。
4. **定时方式**：对时刻或宽度有要求时，确认发送端用的是硬件定时。

发指令到这里讲完。接下来看第二类用途：反过来，用数字输入记下别的设备送来的事件。

### B 部分开头（2026-09-24 落稿）

记事件要达到的目标，可以归成一句话：真实发生一次事件，文件里就恰好留下一条记录，并且标对是哪一种事件。偏离这个目标有三种方式，依次对应下面三节：

- **没记下**：脉冲太窄，落在两次读取之间（⑤）；
- **记了不止一次**：机械开关接通时电平来回跳（⑥）；
- **次数对了，种类认错了**：事件种类多、需要编码时（⑦）。

最后讲在软件里怎样设置，才能让这三点都满足（⑧）。

### ⑤ 采集设备怎样记下一个事件（2026-09-24 落稿）

记事件时，接收端是采集设备的数字输入。以 Intan 的 RHD USB 接口板为例，它的 16 路数字输入与放大器同步采样⁴：放大器每采一个样本，数字输入的电平也读一次。所以读取间隔就是采样率的倒数，由记录神经信号时设定的采样率决定。这块板支持 1–30 kHz⁵，对应每 33 µs 到每 1 ms 读一次（按采样率换算）。下文以手册中的例子为准：采样率 20 kHz，即每秒读 20,000 次，每 50 µs 读一次⁴。

两次读取之间的电平不进入记录。脉冲若整个落在两次读取之间，记录里不留痕迹。因此脉冲宽度要明显大于采集端的读取间隔。

### ⑥ 一次接通，为什么会记成好几次（2026-09-24 落稿）

按键、杠杆这类靠金属触点接通的开关，称为机械开关。触点闭合的瞬间会弹开再碰上若干次，电平在高低之间来回跳几次才稳定，这叫**触点抖动**（contact bounce）。

芯片厂商德州仪器（Texas Instruments，TI）的应用说明写明，许多机械开关按下后会抖动数百微秒⁶。采集设备每 50 µs 读一次时，这段抖动会被读成好几次跳变，一次按压就记成多个事件。

处理方法叫**去抖**（debouncing）：一次跳变之后的一段时间内，再出现的跳变都不算新事件。这段时间要长于开关的抖动时长，又要短于两次真实事件之间的最短间隔。同一份说明提到，这段时间常取 10 ms⁶。去抖可以在硬件电路上做，也可以在分析时对记下的跳变做。

### ⑦ 事件种类多时，怎样区分是哪一件（2026-09-24 落稿；字数多，拆卡时可分两张）

最直接的做法是一根线对应一种事件。以神经记录系统厂商 Plexon 的 OmniPlex 记录系统为例，它的一个数字输入口有 16 根数据线，可以设成 16 路独立事件⁷。手册建议在需要记录的动作种类少时用这种方式，比如杠杆按压、红外光束被遮挡⁷。

种类再多，线就不够了。这时把几根线合起来表示一个编号：每根线的高或低代表二进制的一位，N 根线可以表示 2 的 N 次方个编号。OmniPlex 的另一种模式用 15 根线组成编号，范围是 0 到 32767。手册写明，这种方式适合要记录成百上千种条件的场合⁷。

多根线一起编码，会出现单根线没有的问题。以 3 根线为例：编号 3 是「低、高、高」，编号 4 是「高、低、低」，从 3 换到 4，三根线都要跳变。三根线跳变的时刻总会差一点，比如线 3 先变高，另外两根稍后才变低，中间就短暂出现「高、高、高」，也就是编号 7。接收端恰好在这一刻读取，就会记下一个从未发生的事件。

解决办法是另加一根**选通线**（strobe），它不代表编号里的任何一位。两端约定：接收端只在选通线出现脉冲时读数据线。发送端先把数据线换成新编号，等几根线都跳完、电平稳定后，再在选通线上发脉冲。这样，跳变中间出现的状态不会被读到。OmniPlex 要求数据线在选通脉冲之前至少稳定 100 ns，否则编号可能记错⁷。

还有一处容易出错：OmniPlex 没接线的输入会被拉到 +5 V，在编号模式下被当作高电平算进编号，所以手册建议把不用的线接地⁷。

### ⑧ 在软件里要设什么（2026-09-24 落稿）

前面几节的要求，最后都要落到采集软件的设置上。开始记录前，确认四件事：

1. **这一路有没有被记录。** 两家设备的做法相反：Intan 接口板的数字输入默认关闭，要在软件里启用⁴；Plexon OmniPlex 的数字输入始终记录，没有开关⁷。
2. **线怎样对应事件。** 每根线对应哪种事件；或者几根线组成编号，并用选通线指示何时读取。
3. **有效极性。** 按发送端的约定设为高电平有效或低电平有效。
4. **事件以什么形式存下。** Intan 把数字输入当作波形，按采样率逐点存下每一刻的电平⁴；OmniPlex 只存检测到边沿的时刻，编号模式下另存编号⁷。前一种要在分析时自己找出跳变、做去抖，后一种存下来就已经是事件列表。

### 结语（2026-09-24 落稿）

数字口只传高、低两种状态。一次指令要被正确执行，一个事件要被正确记下，靠的是两端在几件事上约定一致：极性，执行方式，由谁定时，多久读一次，怎样编号。出了问题，可以按现象倒查：

| 现象 | 原因 | 查哪里 |
|---|---|---|
| 有效和空闲整体对调 | 两端极性约定不一致 | 两端的极性设置 |
| 执行时刻忽早忽晚 | 软件定时 | 改用硬件定时 |
| 刺激时长不对 | 门控方式下脉冲宽度不准 | 执行方式、定时方式 |
| 事件漏记 | 脉冲窄于读取间隔 | 脉冲宽度与采样率 |
| 一次动作记成多次 | 触点抖动 | 去抖 |
| 记下不存在的编号 | 没有选通线或等待不够；未接线的输入没有接地 | 选通、接地 |
| 整路没有记录 | 数字输入未启用 | 采集软件设置 |

事件记下以后，它的时刻怎样和神经数据、视频对齐，留到后续一期讲。

## 成品（2026-09-24）

- 16 卡：01 封面《数字接口（DIO），怎样发指令和记事件》/ 02 目录 / 03 引言 / 04–05 电平·TTL·极性 / 06 边沿触发与门控 / 07–08 定时与接线核对 / 09 B 开头 / 10 按间隔读取 / 11 抖动 / 12–13 编码与选通 / 14 软件设置 / 15 排障表 / 16 尾卡。
- 配图原则：图更能说明处才画（8 张示意图 + 表），03/08/09/12/14 为纯文字卡。
- 卡面在落稿文字基础上按版面精简：④ 卡删去图上已显示的阈值数字；③ 的影响段与接线核对合在 08 卡。
- 脚本：.claude/skills/dailybci/scripts/series/ioreq6_figs.py、build_ioreq6_cards.py。

## 讨论中

## 核查记录

- ¹ TI SN7400 数据手册 SDLS025D：p.1 Features「Inputs Are TTL Compliant; VIH = 2 V and VIL = 0.8 V」「Inputs Can Accept 3.3-V or 2.5-V Logic Inputs」；p.4 Recommended Operating Conditions：SN74xx00 VCC 4.75/5/5.25 V，VIH min 2 V，VIL max 0.8 V。本地 papers/ephys-io-ep06/sn7400.pdf。
- ² Sanders & Kepecs 2014（PMC4263096）原文：「In normal mode, an incoming logic pulse triggers all linked output channels, but subsequent triggers are ignored during playback.」「In pulse gated mode, pulse trains are triggered by a low to high logic transition on the trigger channel, and terminated by the subsequent high to low transition if it occurs during playback.」另有 toggle 模式未写入。Pulse Pal Wiki Parameter guide 同述，并写 normal 模式为 low to high transition 触发。
- ³ NI-DAQmx User Manual「Timing, Hardware Versus Software」（ni.com/docs，Updated 2026-07-30，浏览器读取）原文：「With hardware timing, a digital signal, such as a clock on your device, controls the rate of generation. With software timing, the rate at which the samples are generated is determined by the software and operating system instead of by the measurement device. A hardware clock can run much faster than a software loop. A hardware clock is also more accurate than a software loop.」「Some devices do not support hardware timing.」「每条命令到达时刻有波动」为原理推论，未挂角标。
- ⁴ Intan RHD2000 Evaluation System 手册（intan_eval.pdf，修改日期 2021-02-23）：p.1「16 digital inputs that are sampled in synchrony with the amplifiers」；p.2「The 16 digital inputs and 8 analog inputs are sampled in synchrony with the amplifiers」；p.16「if the sampling frequency is 20 kS/s」。50 µs 为按 20 kS/s 自算。本地 papers/ephys-io-ep06/intan_eval.pdf。
- ⁵ Intan RHD USB Interface Board 产品页（intantech.com/RHD_USB_interface_board.html，2026-09-24 读取，本地 papers/ephys-io-ep06/intan_usb_board.html）：「Supports all Intan RHD headstages with sampling rates from 1 kS/s to 30 kS/s.」33 µs、1 ms 为自算。
- ⁶ TI SCEA094「Debounce a Switch」（2020-10，本地 papers/ephys-io-ep06/ti_scea094.pdf）p.1：「Many physical switches can bounce for hundreds of microseconds after being pressed」；表注「This is commonly selected as 10 ms to give maximum debounce time while preventing humans from noticing the delay.」10 ms 的依据是人察觉不到延迟，针对人按按键；是否在正文加「动物连续舔水等场景不可照搬」一句，待用户定。
- ⁷ Plexon OmniPlex Digital Input Guide v1.2（2013-04，本地 papers/ephys-io-ep06/plexon_di.pdf）：p.3「Mode 1: 16 individual events / Mode 3: 15-bit strobed word」「With 15 bits you can send 0 to 32767」；p.4「inputs … will float high (… pulled up to +5V)… Strobed mode (Mode 3) will see those floating inputs as high… It is standard practice to ground unused lines.」「the voltage setting on the bit pins must be stable for at least 100ns before the strobe pulse is sent… will result in the setting to be misrecorded」；p.6「Individual event mode (Mode 1) is typically used when there are few actions… Lever presses or IR beam breaks」「Strobed words (Mode 3) are ideal when there are hundreds or thousands of conditions」。「拼出第三个数」（3→4 途经 7）为原理举例，手册只给 100 ns 要求。
- ⑧ 补充：Intan 手册 p.13「The eight ADCs and 16 digital inputs on the USB interface board may also be observed, although these channels are disabled by default and must be enabled for viewing.」p.20「no ADC channels or digital input channels were enabled when the data file was saved. If those waveforms had been present, additional MATLAB variables would have been created」及「board_dig_in_sample_rate: 20000」——「逐点存电平」为据此推出。Plexon 指南 p.5「Digital inputs are always recorded and there are no enable/disable settings.」p.3「An Event is a timestamp that marks the time when an edge is detected. A Strobed word is a binary number with a timestamp.」

## 参考文献

1. Texas Instruments. (2017). SNx400, SNx4LS00, and SNx4S00 Quadruple 2-Input Positive-NAND Gates Datasheet. SDLS025D.
2. Sanders J. I., Kepecs A. (2014). A low-cost programmable pulse generator for physiology and behavior. Frontiers in Neuroengineering 7:43.
3. National Instruments. (2026). Timing, Hardware Versus Software. NI-DAQmx User Manual.
4. Intan Technologies. (2021). RHD2000 Evaluation System.
5. Intan Technologies. RHD USB Interface Board. intantech.com（2026-09-24 访问）.
6. Texas Instruments. (2020). Debounce a Switch. Application Brief SCEA094.
7. Plexon Inc. (2013). OmniPlex Digital Input Guide. OPXTN0001a, v1.2.
