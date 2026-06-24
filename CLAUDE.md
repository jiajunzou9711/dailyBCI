# DailyBCI — Claude Code 项目指南

这是 **dailybci** 技能的 Claude Code 工程版。每天产出一份双语 BCI 学术日报(英文 X thread + 中文小红书卡片),并维护一个里程碑论文知识库。本文件是你从当前确定版**继续调试 + 日常运行**的操作手册。

---

## 1. 项目结构

```
dailyBCI/                          ← 项目根(用 Claude Code 打开这个文件夹)
├── CLAUDE.md                      ← 本文件,Claude 每次会话自动读取
├── .claude/
│   └── skills/
│       └── dailybci/
│           ├── SKILL.md           ← 技能主文件(调试主要改这里)
│           ├── knowledge-base/    ← INDEX.md + papers/<子领域>/(14 个子领域,篇数见 INDEX.md)
│           ├── scripts/
│           │   ├── card_generator.py   ← 小红书卡片生成器(HTML/CSS+Chromium)
│           │   ├── figcrop.py          ← 论文图自动裁切(亮度投影找真实边界,见 SKILL Step 8)
│           │   └── series/             ← 「专题」长文出图脚本(犹他阵列/电极材料)
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
- **Step 5–8 内容先行**:第一版即给**双语文字稿 + 粗裁图(内联)**→ 自动事实核查 → 生产(渲染卡片)→ 打磨(图多轮裁干净)。最贵的渲染推到事实锁定之后。
- **卡片渲染内核 = HTML/CSS + Chromium**(2026-06-22 从 Pillow 迁移):`card_generator.py` 四个方法签名不变(`cover/figure/text/tail_card`),内核改填 HTML 模板再经 `npx playwright screenshot` 截图。收益:自动流式排版(不再手算坐标/静默溢出)、`**关键词**` 句中高亮、上标原生;代价:多一个 Chromium 依赖。调版式改 CSS,可直接浏览器预览。
- **Content Standards**:标物种、数字回溯原文、慎用"首次/都/all"、术语分层、中文源核实公司名;**双语大纲一致但内容可不同**(thread 纯文字自洽 / 小红书图文更深、用"结论→读图→转场"链);**图永远内联呈现 = 存盘 + Read**(不用浏览器 screenshot)。
- **知识库 14 子领域(篇数见 INDEX.md)**,`population-dynamics` 线延伸到 de Vicente 2026(Sadtler 2014 → Busch 2026 → de Vicente 2026);`non-invasive` 新增 AAD(听觉注意解码)子线;`performance-variability`(认知状态/注意/信号变异,横跨非侵入与皮层内)为 2026-06-23 新建子领域。

---

## 4. 日常怎么用

在项目根运行 `claude`,然后任选:

- 直接说 **「今天BCI有什么新的」** / **「run the daily」** / **「BCI日报」** → 触发 Mode A 全流程。
- **「建知识库 [子领域]」** / **「add to knowledge base」** → 触发 Mode B 补库。
- 技能会按 SKILL.md 在每个关卡停下等你确认——这是设计如此,日报的核心价值就在这几轮对话里。

- **「专题」深度长文(常青,独立于日报)** → 不走 Mode A 的关卡;轻量流程 = 提纲→确认→双语文案→出图,piece-by-piece。成品进 `output/series-<slug>/`,出图复用 `card_generator.py` + 自制 SVG 示意图。已出:犹他阵列 lineage、电极绝缘材料(Parylene-C vs Polyimide)。细节见记忆 `dailybci-series-deep-dive-track`。

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
