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
│           ├── knowledge-base/    ← INDEX.md + papers/<子领域>/(当前 125 篇,13 个子领域)
│           ├── scripts/
│           │   └── card_generator.py   ← 小红书卡片生成器(Pillow)
│           └── fonts/             ← CJK 字体(STHeiti / Hiragino)
├── papers/                        ← 每日运行的工作区:抓到的论文图(浏览器优先;拿不到才下 PDF)
├── output/                        ← 生成的卡片 PNG,按 <日期>-<slug>/ 分目录
└── PRODUCT_BLUEPRINT.md           ← 产品蓝图(背景资料)
```

**关键点:Claude Code 会自动发现 `.claude/skills/` 下的技能。** 改完 `SKILL.md` 存盘,**下一次调用即时生效,不需要重新安装、不需要同步缓存**——这正是从 Cowork 迁过来的最大好处(Cowork 里改技能要走"改文件夹→重装→刷新快照",还容易分叉)。

---

## 2. 一次性环境准备

1. **安装 Claude Code**(若未装):见 https://docs.claude.com → Claude Code。通常 `npm install -g @anthropic-ai/claude-code`,然后在本文件夹运行 `claude`。
2. **Python 依赖**(卡片生成 + 抽图):
   ```bash
   pip install pillow pymupdf --break-system-packages
   ```
3. **字体**:
   - CJK 已随包携带(`.claude/skills/dailybci/fonts/`),无需额外安装。
   - Latin 字体 `card_generator.py` 会自动回退到系统 Arial/Helvetica(macOS 自带),无需装 Lato。若想要原版 Lato 观感,可自行安装。
4. **联网 / 浏览器**:Step 3 优先连浏览器读论文全文 + 抓图;拿不到时才用 `curl`/API 下载(curl macOS 自带)。另需 Claude 联网搜索查候选 / 核实事实。
5. **git 已初始化**——技能、知识库、输出都在版本管理下,改坏用 `git checkout -- <文件>` 回滚。

---

## 3. 当前进度(流程第一版已定稿)

主流程第一版于 **2026-06-13 定稿**(commit `f022b4b`),已用 Yale 流形 BCI 那期端到端跑通验证。要点:

- **Mode A 9 步**,三个强制确认关卡:**Step 2 选题**(表格候选 + 知识库对照 + 推荐;无对照基准弹缺位提示问是否补库)、**Step 4 insight**(先给带理由的主张 + **直接贴论文原图**,用户确认才走)、**Step 6 事实核查**(草稿后自动三层核查出表,⚠/✗ 按"承重×严重度"分流,全 ✓ 才进生产)。
- **Step 3 浏览器优先、下载兜底**:连浏览器读全文 + 抓原图;curl/PDF 仅用于无头 / 付费墙 / 超清图(bioRxiv/PMC 的 curl 会被 Cloudflare/JS 门挡)。
- **Step 5–8 内容先行**:内容草稿(prose,对话框)→ 事实核查 → 生产(thread + 配图卡)→ 对话打磨。最贵的做卡 / 配图推到事实锁定之后。
- **Content Standards**:标物种、数字回溯原文、慎用"首次/都/all"、术语分层、双语各自独立写 + 信息对等、中文源核实公司名。
- **知识库 126 篇 / 13 子领域**,`population-dynamics` 为最新子领域(神经流形约束学习线:Sadtler 2014 → Busch 2026)。

---

## 4. 日常怎么用

在项目根运行 `claude`,然后任选:

- 直接说 **「今天BCI有什么新的」** / **「run the daily」** / **「BCI日报」** → 触发 Mode A 全流程。
- **「建知识库 [子领域]」** / **「add to knowledge base」** → 触发 Mode B 补库。
- 技能会按 SKILL.md 在每个关卡停下等你确认——这是设计如此,日报的核心价值就在这几轮对话里。

**定时运行**:想每天自动出初稿,可用 cron 调用 Claude Code 的无头模式(`claude -p "run the daily"` 之类),让它跑到第一个确认关卡或产出草稿,你早上来审。具体命令见 docs.claude.com 的 Claude Code headless / print 模式。

---

## 5. 调试这个技能的工作流

1. 改 `.claude/skills/dailybci/SKILL.md`(或 `card_generator.py` / 知识库)。
2. 存盘 → 下一次调用即时生效,**无需重装**。
3. 在同一个项目里直接发触发词测试效果。
4. 满意就 `git commit`;改坏就 `git checkout`。

**调试建议**:
- 一次只动一个关卡/一段,跑一遍看效果(我们这一路就是这么迭代的)。
- 想验证某一步,可以直接对 Claude 说"从 Step X 开始,用 [某篇论文] 跑"。
- 知识库是判断"重要性/首次"的基准,扩得越全,选题和事实核查越准。

---

## 6. 已知待留意项(首次在本机跑时)

- **抓论文图(Step 3)**:默认连浏览器读全文 + 下原图(实测 curl 抓 bioRxiv/PMC 会被 Cloudflare/JS 拦)。无浏览器时(如 cron / `claude -p`)才退回 curl 下 PDF + PyMuPDF 抽图,需先确认 `pip install pymupdf` 成功。
- **CJK 字形**:若用系统 PingFang/Noto 而非自带 STHeiti,简体字形不对就把 `card_generator.py` 里 `CJK_IDX` 从 1 试成 0。
