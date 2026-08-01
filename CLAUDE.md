# DailyBCI — Claude Code 项目指南

这是 **dailybci** 技能的 Claude Code 工程版。每天产出一份 BCI 学术日报(中文小红书图卡;**X thread 自 2026-07-30 起默认不出**,仅当期明确要求才做),并维护一个里程碑论文知识库。本文件是你从当前确定版**继续调试 + 日常运行**的操作手册。

## 写作偏好

- 中文内容默认使用肯定陈述,减少否定起句。
- 严格禁用"不是……而是……"式对照句,包括"不是 X,而是 Y""并不是 X,而是 Y""不只是 X,而是 Y"等变体;需要表达对比时,改用"关键在于""核心差别是""更准确地说""主要来自""相比 X,Y 更..."等肯定句式。
- 任何技术术语、缩写、指标第一次出现时必须给出一句简短解释。例如第一次写 CPM 时标明 "characters per minute, 每分钟字符数"。
- 标题必须是简短、肯定、信息增量明确的断言句,优先直接传递本篇文章的核心结论;避免疑问句、悬念句和只抛问题的标题。
- 日报通常围绕一篇主文章展开:封面/来源区已交代主文章后,后续图卡引用主文章事实默认不重复加脚标;只有引用其他论文、综述、公司/监管来源或横纵对照材料时再加脚标。
- 图卡文案要保持链式逻辑:每张开头承接上一张结尾并高度总结本卡要点,每张结尾自然引出下一张。生产前先给分卡文字供审阅。
- **小红书单帖图卡硬上限 18 张**(封面+图卡+文字卡+尾卡全部计入)。出提纲阶段就先数卡数并留余量,超了拆成上/下多篇,不要硬塞。
- **目录卡 + 发布标题/话题标签 = 所有小红书图文通用**(日报与专题都出,2026-07-24 定):封面后强制出一张 SVG 目录卡(计入 18 卡);渲染完卡后自动产出发布标题候选 + 话题标签候选(先采真实搜索词再打分)。完整规则见 SKILL.md Step 7 的两个「通用」节。
- **图卡注文按「3 段 ≈12 行」写**(图高 500px 时的实测容量)。写长了渲染必溢出、承重数字会被截掉;注文只指认图里的东西,不复述图上已经画出来的内容。
- 少用比喻和拟人等修辞(硬规则)。比喻会让信息失真,对严谨科学论文尤其危险,默认用字面、准确的说法把术语和逻辑讲清。被点名的反例:把"结果分成两类"说成"劈成两种命运"、给数据/过程套上命运/意志等拟人。需要对比时用肯定句式("关键差别是""相比 X,Y 更…")。
- 术语第一次出现时,即使读者可能没读过原文也要能看懂:承重的抽象说法(如"价值两极清晰 / 价值模糊")首次出现必须就地用一句具体话解释(如"物品的奖惩含义是否分明"),不要把只有读过论文的人才懂的压缩表达直接抛给冷读者。
- 脚手架标签(承上/读图/转场/分点/结论/Qn 等)只是写作时给自己的结构提示,绝不能作为字面文字进入小红书图卡或 thread 的成品正文。

---

## 1. 项目结构

```
dailyBCI/                          ← 项目根(用 Claude Code 打开这个文件夹)
├── CLAUDE.md                      ← 本文件,Claude 每次会话自动读取
├── .claude/
│   └── skills/
│       └── dailybci/
│           ├── SKILL.md           ← 技能主文件(调试主要改这里)
│           ├── knowledge-base/    ← INDEX.md + papers/<子领域>/(22 个子领域,篇数见 INDEX.md)
│           ├── scripts/
│           │   ├── card_generator.py   ← 小红书卡片生成器(HTML/CSS+Chromium)
│           │   ├── figcrop.py          ← 论文图自动裁切(亮度投影找真实边界,见 SKILL Step 8)
│           │   └── series/             ← 「专题」长文出图脚本(每个专题一对:*_figs.py 出 SVG、build_*_cards.py 出卡)
│           └── fonts/             ← CJK 字体(HeitiSC-Subset.ttf,@font-face 引用)
├── papers/                        ← 每日运行的 scratch 工作区(已 gitignore):下载的论文图 + 全文 PDF/txt;每期发完可整目录删,成品在 output/
├── output/                        ← 生成的卡片 PNG。日报按 <日期>-<slug>/ 分目录;「专题」长文按 series-<slug>/(见 §4)
└── PRODUCT_BLUEPRINT.md           ← 产品蓝图(背景资料)
```

**关键点:Claude Code 会自动发现 `.claude/skills/` 下的技能。** 改完 `SKILL.md` 存盘,**下一次调用即时生效,不需要重新安装、不需要同步缓存**——这正是从 Cowork 迁过来的最大好处(Cowork 里改技能要走"改文件夹→重装→刷新快照",还容易分叉)。

---

## 2. 一次性环境准备

1. **安装 Claude Code**(若未装):见 https://docs.claude.com → Claude Code。通常 `npm install -g @anthropic-ai/claude-code`,然后在本文件夹运行 `claude`。
2. **依赖**:
   - **Python**(抽图 + 可选 PIL 图输入):`pip install pillow pymupdf --break-system-packages`
   - **卡片渲染**:卡片走 HTML/CSS 模板 + Chromium 截图(`card_generator.py` 调 `npx playwright screenshot`)。需 Node + 一次性 `npx playwright install chromium`。**无 Chromium 出不了卡**(cron/无头同理,机器上必须装)。
3. **字体**:
   - CJK 自带 `fonts/HeitiSC-Subset.ttf`(从 STHeiti 抽出简体黑体面、再按 GB2312+知识库用字子集化到 ~6MB),`@font-face` 引用,无需额外安装。若日后某生僻字渲成方块,重跑子集化(保留集见提交历史)把该字补进即可。
   - Latin 由 CSS 回退到系统 Helvetica/Arial(macOS 自带);上标 ¹²³⁴ 由 Latin 字体原生渲染。
4. **联网 / 浏览器**:Step 3 经浏览器下全文 PDF + 抓全图到本地;无浏览器时才退回 `curl`/API(curl macOS 自带)。另需 Claude 联网搜索查候选 / 核实事实。
5. **git 已初始化**——技能、知识库、输出都在版本管理下,改坏用 `git checkout -- <文件>` 回滚。

---

## 3. 当前进度(流程第一版已定稿)

主流程第一版于 **2026-06-13 定稿**(commit `f022b4b`),已用 Yale 流形 BCI 那期端到端跑通验证。要点:

- **Mode A 10 步**(末步 Step 10 收尾清理 papers/ scratch),三个强制确认关卡:**Step 2 选题**(表格候选 + 知识库对照 + 推荐;无对照基准弹缺位提示问是否补库)、**Step 4 insight**(先给带理由的主张 + **直接贴论文原图**,用户确认才走)、**Step 6 事实核查**(草稿后自动三层核查出表,⚠/✗ 按"承重×严重度"分流,全 ✓ 才进生产)。
- **Step 3 选题即"一次性扒全"**:经浏览器把**全文 PDF**(PyMuPDF 抽文)+ **全部图**(F1 探到 404)一次性下到本地,之后深读/核查/裁图全读本地、不再回访网页。curl 抓 bioRxiv/PMC 会被 Cloudflare/JS 拦,故走浏览器。
- **Step 5–8 内容先行**:第一版即给**文字稿 + 粗裁图(内联)**→ 自动事实核查 → 生产(渲染卡片)→ 打磨(图多轮裁干净)。最贵的渲染推到事实锁定之后。
- **卡片渲染内核 = HTML/CSS + Chromium**(2026-06-22 从 Pillow 迁移):`card_generator.py` 四个方法签名不变(`cover/figure/text/tail_card`),内核改填 HTML 模板再经 `npx playwright screenshot` 截图。收益:自动流式排版(不再手算坐标/静默溢出)、`**关键词**` 句中高亮、上标原生;代价:多一个 Chromium 依赖。调版式改 CSS,可直接浏览器预览。
- **Content Standards**:标物种、数字回溯原文、慎用"首次/都/all"、术语分层、中文源核实公司名;**图卡用"结论→读图→转场"链**(若当期同时出 thread,两者共用提纲、各自独立撰写);**图永远呈现给用户 = 存盘 + `SendUserFile`**(`Read` 只进模型上下文、桌面端会折叠成一行,用户看不到;浏览器 screenshot 同理)。
- **知识库 23 子领域(篇数见 INDEX.md)**,`population-dynamics` 线延伸到 de Vicente 2026(Sadtler 2014 → Busch 2025 → de Vicente 2026);`non-invasive` 新增 AAD(听觉注意解码)子线;`performance-variability`(认知状态/注意/信号变异,横跨非侵入与皮层内)为 2026-06-23 新建子领域;`affective-bci`(情感/EEG 情绪解码) 与 `emg-motor-unit`(外周肌电/运动单位解码→神经驱动) 为 2026-06-29 新建;`neuromodulation` 下 2026-06-30 新增 current-steering(电流聚焦/刺激空间选择性)子簇;`cancer-neuroscience`(神经元活动↔胶质瘤电/突触整合、用神经记录监测肿瘤)为 2026-07-09 新建;`functional-ultrasound`(功能超声成像 fUSI/血流动力学神经接口:Macé 2011→Norman 2021→Griggs 2024→Rabut 2024→Lin 2026)为 2026-07-11 新建;`presurgical-mapping`(术前无创功能定位,先建语言区线:Ojemann DCS 金标准→Pascual-Leone 1991→Papanicolaou 2004 MEG→Picht 2013 nrTMS vs DCS→Tarapore 2013→Krieg 2017→Autti 2026 MEG 引导 nrTMS 时机)与 `visual-prosthesis`(视觉假体/视网膜电刺激:Humayun 1996→Argus II/Alpha-IMS/PRIMA + Chichilnisky 精准刺激线)为 2026-07-12 新建;`neuromodulation` 2026-07-12 增 Liu 2026(加速度计 vs beta 生物标志物);`presurgical-mapping` 2026-07-13 增 Autti 2026(用个人 MEG 峰值个体化 nrTMS 发放时机 PTI,best PTI≈MEG 峰值−132ms,R=0.713);`passive-bci`(被动脑机接口/神经自适应:把自发认知状态当隐式输入让机器适应,抽取源 Zander & Kothe 2011;Parra 2003 ERN 纠错→Kohlmorgen 2007 真实驾驶工作负荷→Ferrez 2008 交互 ErrP→Zander 2016 PNAS neuroadaptive 闭环→Aricò 2016 空管部署)为 2026-07-14 新建(6 篇);同日日报选题 Pan 2026(首个动态 VR 游戏中实时闭环解码交互意图:gaze+被动EEG,人类23人;affordance 稳在77.8–83.5%,approach-avoidance 仅价值两极可解 coins/bombs 80.8%、价值模糊塌回随机59%;划出"可解码信号=效价"边界)入库,并补横向对照 Reddy 2024(SPN 隐式选择,CHI '24)、Dehais 2022(dual passive-reactive,Front Neuroergonomics),`passive-bci` 增至 9 篇;`invasive-recording` 2026-07-16 增 Jafri 2026(把"白质 sEEG 触点=灰质衰减副本"证伪:谱参数化拆 offset/exponent,衰减只能动前者而实测双降且 19 人无一例外,delta 中心频率位移更免疫于幅度缩放;仅凭信号分类组织 AUC 0.92。给 buzsaki-2012 补实证:"生成机制不同"对、"那里什么都没有"错。**本篇不做解码**,增益出处是 Li 2021),`invasive-recording` 增至 10 篇;2026-07-17 补库两条线并新建 `semantic-decoding`(语义解码/读概念非发音,抽取源 Rybář&Daly 2022 综述,Patterson 2007→Mitchell 2008→Rupp 2017 属性零样本标杆→Nagata 2022,11 篇)、`invasive-recording` 加 sEEG 植入精度子簇(Bancaud 1970→Cardinale 2013 基准→Vakharia 2021 唯一 RCT→Abbas 2026 meta,共识"机器人买到时间不是精度",8 篇);同日日报选题 Thurairajah 2026(3176 条轨迹拆解 sEEG 精度=轨迹几何属性、已知因素只解释 15%)入库,`invasive-recording` 增至 19 篇。**补库流程 2026-07-14 起自动写入,不再逐篇征询用户(见记忆 `dailybci-modeb-autoadd`)。背景先行+一次一小块见记忆 `background-first-one-chunk-at-a-time`。**
- **2026-07-30**:`electrode-hardware` 增至 27 篇——补入 Steinmetz 2021(Neuropixels 2.0,四针脚/5120 点/384 通道的事实标准)与当日选题 Chang 2026(Quad Base,同时通道 384→1536;用同一份记录自我抽子集作对照,证明一次 8 针脚同时记录检出的跨区 Granger 连接数超过四次连续 2 针脚记录的总和)。成品 17 卡在 `output/2026-07-30-quadbase/`,自制 SVG 脚本 `scripts/series/quadbase_figs.py`、卡片脚本 `scripts/series/build_quadbase_cards.py`。本期同时定下两条规则:**X thread 默认不出**、**对话与成品一律不用 LaTeX 记号**;由本期派生的两个方法论期已出:`output/2026-07-31-identifiability/`(跨 session 可辨识性与缝合,17 卡)、`output/2026-08-01-dlag/`(DLAG/mDLAG 方法论,18 卡;脚本 `series/dlag_figs.py` + `series/build_dlag_cards.py`)。

---

## 4. 日常怎么用

在项目根运行 `claude`,然后任选:

- 直接说 **「今天BCI有什么新的」** / **「run the daily」** / **「BCI日报」** → 触发 Mode A 全流程。
- **「建知识库 [子领域]」** / **「add to knowledge base」** → 触发 Mode B 补库。
- 技能会按 SKILL.md 在每个关卡停下等你确认——这是设计如此,日报的核心价值就在这几轮对话里。

- **「专题」深度长文(常青,独立于日报)= SKILL.md 的 Mode C** → 不走 Mode A 的关卡;轻量流程 = 提纲→确认→文案→出图,piece-by-piece。成品进 `output/series-<slug>/`,出图复用 `card_generator.py` + 自制 SVG 示意图。**Mode C 有三道特有关卡(2026-07-24 建):C-1 选题三方交汇(用户兴趣 × 主题insight × 小红书真实需求·权重最高;需求判定两轴分开——A需求强度[联想词/收藏/留言]、B供给空位,都过线才入选)、C-2 极简封面 + 目录卡、C-3 出稿同时给标题候选 + 话题标签候选 + 半定量打分。** 已出:犹他阵列、电极绝缘材料、神经解码方法论(四轴/生成式脊柱/三层嵌套)、侵入式定位精度(上下各17卡)、EEG 工频/阻抗均衡(series-eeg-impedance-01,17卡)、EEG 电极界面/基线漂移(series-eeg-impedance-02,18卡含目录卡)、硬脑膜四期系列(起因是 Neuralink 2026-05 首例经硬膜植入):①「所有入脑手术的第一道关」series-dura-01,17卡;②「不切开硬膜,把电极送进皮层」series-dura-02,17卡;③「一根电极扎进脑,会在哪四层出血」series-dura-03,16卡;**④系留代价待做**。体量大的拆上/下多篇,各守 18 卡上限。细节见记忆 `dailybci-series-deep-dive-track` 与 SKILL.md Mode C。

**定时运行**:想每天自动出初稿,可用 cron 调用 Claude Code 的无头模式(`claude -p "run the daily"` 之类),让它跑到第一个确认关卡或产出草稿,你早上来审。具体命令见 docs.claude.com 的 Claude Code headless / print 模式。

---

## 5. 调试这个技能的工作流

1. 改 `.claude/skills/dailybci/SKILL.md`(或 `card_generator.py` / 知识库)。
2. 存盘 → 下一次调用即时生效,**无需重装**。
3. 在同一个项目里直接发触发词测试效果。
4. 满意就 `git commit`;改坏就 `git checkout`。**单人项目:默认直接 commit + push master,不开 PR。**

**调试建议**:
- 一次只动一个关卡/一段,跑一遍看效果(我们这一路就是这么迭代的)。
- 想验证某一步,可以直接对 Claude 说"从 Step X 开始,用 [某篇论文] 跑"。
- 知识库是判断"重要性/首次"的基准,扩得越全,选题和事实核查越准。

---

## 6. 已知待留意项(首次在本机跑时)

- **抓论文全文+图(Step 3)**:选题即经浏览器一次性下全文 PDF + 全部图到本地(PyMuPDF 抽全文/抽图),之后全程读本地(实测 curl 抓 bioRxiv/PMC 会被 Cloudflare/JS 拦,故走浏览器)。无浏览器时(如 cron / `claude -p`)才退回 curl + BioC API,需先确认 `pip install pymupdf` 成功。
- **卡片渲染(Step 7/8)**:渲染靠 `npx playwright screenshot` 起 Chromium。首次跑前先 `npx playwright install chromium`;报"找不到浏览器"就是没装。CJK 字形由自带 `fonts/HeitiSC-Subset.ttf`(简体黑体子集 ~6MB)经 `@font-face` 锁定,不再依赖系统字体 / 字体集合 index,字形稳定。
