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
│           ├── knowledge-base/    ← INDEX.md + papers/<子领域>/(当前 118 篇)
│           ├── scripts/
│           │   └── card_generator.py   ← 小红书卡片生成器(Pillow)
│           └── fonts/             ← CJK 字体(STHeiti / Hiragino)
├── papers/                        ← 每日运行的工作区:下载的 PDF + 抽出的 figure PNG
├── output/                        ← 生成的卡片 PNG,按 <日期>-<slug>/ 分目录
├── drafts/                        ← 历史草稿(可选保留)
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
4. **联网**:Step 3 需要 `curl` 下载论文 PDF(macOS 自带),以及 Claude 的联网搜索能力查候选/核实事实。
5. (建议)**初始化 git**,给技能和知识库做版本管理,改坏能回滚:
   ```bash
   cd dailyBCI && git init && git add -A && git commit -m "migrate dailybci skill to Claude Code"
   ```

---

## 3. 当前进度(从这里接着调)

技能已是**合并后的权威版**,包含:

- **9 步主流程(Mode A)**,带三个强制确认关卡:
  - **Step 2 选题关卡** — 候选用表格呈现(标题/子领域/时效/知识库对照/significance/角度),机器给推荐倾向,用户拍板;若候选在知识库无对照基准,弹出**醒目的缺位提示块**,问是否切 Mode B 补库后回 Step 2 重审。
  - **Step 4 insight 关卡** — 机器先给带理由的 insight 主张 + 打算用哪几张图,用户确认才往下。
  - **Step 6 事实核查关卡** — 草稿后自动跑三层核查(回溯原文 / 跨源 / 断言审计)出核查表,**事实先于措辞**,全部 ✓ 才进表达打磨。
- **Content Standards**:标物种、数字回溯原文、慎用"首次/都/all"、术语分层、双语各自独立写+信息对等、中文源核实公司名。
- **知识库 118 篇**,含本会话新增的 NEO 三篇(`invasive-recording/neo-2024-…`、`neo-2025-…`、`clinical-regulatory/neuracle-2026-…`)。

**上次中断点**:正在跑 2026-06-10 的日报(选题=NEO 商业获批,insight=硬膜外信号 9 个月反增 + BCI 当康复用患者手功能部分恢复),已完成双语草稿和事实核查表,**卡在事实核查表的 3 个 ⚠ 待你定**(批准时间措辞、"36 人全部改善"是否降级、"全球首个商业"如何收紧边界)。迁移后可直接从这步继续,或重新跑一遍验证全流程。

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

## 6. 已知待验证项(首次在本机跑时留意)

- **PyMuPDF 抽图**:首跑确认 `pip install pymupdf` 成功,且 `papers/*.pdf` 是真 PDF(`file papers/*.pdf`)。
- **CJK 字形**:若用系统 PingFang/Noto 而非自带 STHeiti,简体字形不对就把 `card_generator.py` 里 `CJK_IDX` 从 1 试成 0。
- **小红书卡片里的论文图**:Claude Code 有真实 shell,Step 3 会用 `curl` 自动下 PDF、PyMuPDF 抽图——不再需要你手动放图(这正是迁移要解决的核心问题)。
- `output/_smoketest/`:迁移自带的一个测试残留,可删。
