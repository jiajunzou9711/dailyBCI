# DailyBCI — Claude Code 项目指南

本仓库包含 DailyBCI 学术内容生产流程、知识库、图卡生成工具，以及一个独立的脑机接口外设综述项目。

## 会话入口

1. 先读取根目录 `AGENTS.md`，其中保存跨工具通用的写作规则与事实核查红线。
2. DailyBCI 日报、专题或知识库任务，读取 `.claude/skills/dailybci/SKILL.md` 并按对应模式执行。
3. 修改 `脑机接口综述for_涵之/` 前，完整读取该目录下的《写作与生产规范.md》和《项目进度.md》。

稳定规则只维护在上述三个入口。当前稿件进度、已完成事项和未决问题统一写入综述项目的《项目进度.md》，不在本文件追加会话历史。

## 项目结构

```text
dailyBCI/
├── AGENTS.md                         # 跨工具写作规则与项目红线
├── CLAUDE.md                         # Claude Code 操作入口
├── README.md                         # 面向使用者的项目概览
├── .claude/skills/dailybci/
│   ├── SKILL.md                      # DailyBCI 权威工作流
│   ├── series-backlog.md             # C 类原理期的未闭环问题清单
│   ├── knowledge-base/               # 里程碑论文知识库；INDEX.md 是索引权威
│   ├── scripts/                      # 卡片生成、裁图与专题脚本
│   └── fonts/                        # 图卡使用的 CJK 字体
├── papers/                           # 每期论文与图的临时工作区
├── output/                           # 日报、专题与看板成品
├── dashboard/                        # 常驻内容数据看板
├── research/                         # 独立调研材料
├── 脑机接口综述for_涵之/             # 外设综述、证据库与项目进度
└── PRODUCT_BLUEPRINT.md              # 早期产品设想，仅作历史背景
```

## DailyBCI 工作流

- “今天 BCI 有什么新的”“run the daily”“BCI 日报”：进入 `SKILL.md` Mode A。
- “建知识库”“add to knowledge base”：进入 Mode B。
- “专题”：进入 Mode C，按提纲确认、文案确认和成品确认逐步推进。
- 当天候选都不合适时，走 SKILL.md 的 Step 2.5：从 `series-backlog.md` 挑一条未闭环的原理问题，转 C 类原理期。日报（A 类）与原理期（C 类）不写死频次，按当天扫到什么决定。
- X thread 默认不产出；当期明确要求时再制作。
- 最终交付包括图卡、小红书发布标题与话题标签、微信公众号摘要。
- 每次讨论的实时状态写入 `output/<日期>-<slug>/draft.md`，不得只留在对话中。

知识库以 `.claude/skills/dailybci/knowledge-base/INDEX.md` 为唯一索引权威。新增或删除论文后，核对索引总数与实际 Markdown 文件数一致。

## 外设综述工作流

- 当前权威稿件、生产阶段和下一步只看 `脑机接口综述for_涵之/项目进度.md`。
- 正文写作遵循 `脑机接口综述for_涵之/写作与生产规范.md`。
- 原始证据、关键数字和监管口径均从 `脑机接口综述for_涵之/资料/` 调用。
- Word 原稿与旧 Markdown 草稿保留作历史底稿；编辑对象以《项目进度.md》为准。

## 环境准备

- Python 图像依赖：`pillow`、`pymupdf`。
- 图卡由 HTML/CSS 与 Playwright Chromium 渲染；首次使用运行 `npx playwright install chromium`。
- CJK 字体位于 `.claude/skills/dailybci/fonts/`，无需系统安装。
- 联网用于论文检索、来源核验和搜索词研究；论文一旦选定，优先将全文与图片存入 `papers/` 后在本地处理。

## 调试与维护

1. 修改 `.claude/skills/dailybci/SKILL.md`、脚本或知识库。
2. 在同一项目中用对应触发词运行目标步骤。
3. 图卡生成后检查溢出、裁切、字号和引用，再交用户确认。
4. 单人项目按现有 Git 流程提交；保留工作区中与当前任务无关的改动。

## 常见故障

- Playwright 报 Chromium 可执行文件不存在：重新运行 `npx playwright install chromium`。
- 生僻字显示为方块：更新 `.claude/skills/dailybci/fonts/HeitiSC-Subset.ttf` 的字形子集。
- 论文网站阻止静态抓取：改用浏览器获取公开全文；选题完成后保存到本地，减少重复访问。
- 综述引用与正文不一致：先查六项证据库索引和核心数值核查日志，再修改正文和《项目进度.md》。
