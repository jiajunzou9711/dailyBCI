# Skill Execution: KB Gap Handling for Non-Invasive Sub-field

## User Prompt
"我看到一篇关于 EEG-based non-invasive BCI 的新论文，帮我评估一下值不值得写"

---

## Skill Workflow Execution

### Step Triggered: Mode A, Step 2 — Evaluate candidate against the knowledge base

The user is asking me to evaluate a candidate paper. Before I can search or assess anything, I need to check the knowledge base for context on this sub-field.

**Action taken:** Read `knowledge-base/INDEX.md`

**Finding:** The `non-invasive` sub-field is listed as "待建设" — zero papers, no milestone entries.

This triggers the skill's graduated warning system. The applicable warning level is:

> **Knowledge base exists but no entries match this specific topic**: "知识库中没有找到与 [topic] 直接相关的 milestone 论文，这个判断缺少历史对比基准。"

---

## Response Presented to User

---

先说一个问题：**知识库中 non-invasive（EEG-based BCI）方向目前完全是空的（0 篇 milestone 论文），这个判断缺少历史对比基准。**

目前知识库覆盖了 speech-decoding（12 篇）和 motor-bci（15 篇），但 non-invasive 方向还没有建设。这意味着：

- 我没办法告诉你这篇论文相对于 EEG-BCI 领域的历史里程碑有多大进步
- 我没办法判断它的方法是真正新颖的，还是已经被做过的变体
- 我没办法准确评估这篇论文的 "值不值得写"

没有基准的评估容易高估也容易低估——等于凭印象判断，不是 DailyBCI 应该做的事。

**要不要我先搜索这个方向的综述论文，补充几篇 milestone 到知识库，然后再回来评估今天的候选？还是先按现有信息继续？**

具体来说，如果先建知识库，我会：
1. 搜索 EEG-based BCI 和 non-invasive BCI 方向近 3-5 年的权威综述
2. 从综述中提取 5-15 篇里程碑论文（比如 P300 speller 的经典工作、SSVEP-BCI、motor imagery 解码的关键进展等）
3. 为每篇生成结构化摘要，你确认后入库
4. 然后回来用这些基准重新评估你看到的这篇论文

这大概需要额外 10-15 分钟。但之后 non-invasive 方向的每一次选题判断都会有基准可依。

你怎么选？

---

## Skill Logic Trace

1. **User intent identified**: Evaluate a candidate paper (Mode A, Step 2 territory)
2. **Sub-field identified**: non-invasive (EEG-based BCI)
3. **Knowledge base check**: Loaded INDEX.md → `non-invasive` is "待建设", 0 papers
4. **Graduated warning triggered**: Level 3 — "知识库中没有找到与 [topic] 直接相关的 milestone 论文，这个判断缺少历史对比基准。"
5. **User choice offered** (per skill instruction): Supplement KB first via Mode B, or continue with current info
6. **Awaiting user decision** before proceeding further

### What happens next depending on user choice:

**If user says "先建知识库" / "supplement first":**
→ Switch to Mode B for `non-invasive` sub-field
→ Search for authoritative reviews (e.g., Wolpaw, Birbaumer, Millán's work on EEG-BCI)
→ Extract milestone papers, generate structured summaries
→ Present batch for user approval, write to `knowledge-base/papers/non-invasive/`
→ Update INDEX.md
→ Return to Mode A Step 2 with newly loaded context
→ Ask user to share the paper link, then evaluate properly

**If user says "先按现有信息继续":**
→ Ask user to share the paper link/title
→ Proceed with evaluation but caveat all judgments clearly
→ After evaluation, suggest building the non-invasive KB as a follow-up
