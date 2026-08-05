---
name: dailybci
description: >
  Daily BCI (brain-computer interface) academic digest with two modes:
  (1) Daily digest mode — find the most important recent BCI paper, identify its core technical insight using the
  knowledge base for context, and produce a deep explanation as Chinese 小红书 cards (English X thread only when the user asks for one that issue).
  (2) Knowledge base mode — build and maintain a structured library of milestone BCI papers organized by sub-field.
  Use this skill whenever the user says "今天BCI有什么新的", "dailybci", "BCI日报", "run the daily",
  "generate today's post", "建知识库", "add to knowledge base", or any request related to finding, explaining,
  or cataloguing BCI academic progress. Also trigger for searches about neural decoding, neuroprosthesis,
  neurotechnology breakthroughs, brain-machine interfaces, or ECoG/intracortical research.
---

# DailyBCI

A daily bilingual BCI academic digest. Two modes: **daily digest** and **knowledge base construction**.

The author's identity is an **explainer** (解读者) — someone who reads more broadly across BCI sub-fields than any single researcher has time for. The value is making complex work accessible: finding the most interesting thing that happened today and helping people understand it. Not an expert handing down judgments, but a knowledgeable guide still building their own understanding.

---

## Content Standards

These standards apply to all output — X threads, 小红书 cards, knowledge base entries, and dialogue with the user. They were established through iterative review and reflect the author's quality expectations.

### Factual Accuracy

1. **Label species for every cited study.** BCI results in macaques, rodents, and humans carry very different weight. Always specify: "Chestek et al. (2011) measured in rhesus macaques…", "In a human patient with C4 SCI…". Never leave the reader guessing whether a result comes from an animal model or a clinical trial.

2. **Always specify the electrode/recording modality — at the very start, every time it comes up.** 脑机接口领域里"用什么电极"几乎决定了一项工作的性质、风险和可比对象,所以**一旦涉及电极,开篇第一时间就要讲清它的类型**,绝不含糊带过。按这棵分类树明确归位:
   - **侵入式 (invasive)** — 进一步说清是哪一种:
     - **皮层内 / intracortical(穿刺式微电极阵列,如 Utah array)** — 电极扎进皮层、记录单神经元动作电位 + LFP;
     - **皮层表面 / ECoG**(含**硬膜下 subdural** 与 **硬膜外 epidural/eECoG**)— 电极贴在皮层表面,不穿刺;
     - **深部电极 / depth(sEEG)**;
     - **DBS** — 深部脑刺激电极(多为治疗性刺激,非记录主导)。
   - **非侵入式 (non-invasive)** — 说清是 **EEG / MEG / fNIRS / 耳周或皮下 EEG** 等具体技术。
   - **血管内 / endovascular(如 Stentrode)** — 经血管放置、不开颅,单列一类。
   要点:植入位置(哪块脑区)、记录的信号层级(单神经元 / LFP / 表面场电位)、有线还是无线,这些都属于"电极说明"的一部分,能讲清就讲清。读者看完应当立刻知道"这是扎进脑子里的、还是贴在表面的、还是戴在头皮上的"。

3. **Every quantitative claim must trace back to the original paper.** Do not paraphrase from memory or round loosely. If you write "100% success rate within 10 seconds," be ready to point to the exact figure, table, or sentence in the source. If you cannot verify a number, say "the paper reports X" rather than asserting X as fact.

4. **Avoid universal claims unless individually verified.** Words like "all", "every", "no other", "the first ever", and "都" are strong assertions that require exhaustive checking. Prefer bounded language: "the main prior approaches included…" instead of "all previous work relied on…"; "among the earliest" instead of "the first." Use "首次" or "first" only when verified against the knowledge base.

5. **Fact verification step.** After completing a draft, run the three-layer verification defined in Step 6 (trace back to source → cross-source check → assertion audit with knowledge base + web search). Present the verification table to the user before any discussion of wording. Facts must be confirmed before polish begins. See Step 6 for the full procedure.

### 背景先行 + 一次一小块（2026-07-17 用户定，写死；管全流程与全部对话）

两条硬规则，适用范围是**我对用户的全部叙述**，不限于成品文案，也不限于 Step 4：

1. **背景先行。** 任何判断、insight、对比、评价抛出之前，先讲清它所处的背景——这个领域在干什么、现在卡在哪、这篇站在哪一格。**默认用户没听说过这个子方向**（他是泛神经科学背景，不是每个子领域的专家）。承重的名词第一次出现就地讲透，且要讲"它为什么存在、解决什么问题"，不能只给定义。**原理：用户无法判断一个他不理解其背景的结论的质量。** 背景缺席时，确认关卡就退化成盲签。
2. **一次只出一小块，出完停下来问。** 不要一口气倒出大段内容。用户原话（2026-07-17）："我最开始就有问题，后面的我也不可能看得懂的。"——前一块没懂，后面全部作废。宁可多几轮往返，不要一次性堆料。这与"口语化可以口水化不行"不冲突：**每一块都要紧凑，但块要小、要分次给。**

配套的完整操作细则见 Step 4a（背景对齐关卡）。用户随时可喊停内容生产转纯讲解，此时放弃出稿节奏、转入教学（见记忆 `user-stepwise-tech-tutorials`）。

### Technical Term Usage

Terms fall into two tiers:

- **Core technical terms** — terms that define this work's identity and cannot be simplified without losing meaning (e.g., "硬脑膜外/epidural," "Utah阵列," "体感诱发电位/somatosensory evoked potentials"). These MUST appear, with sufficient context for a non-specialist to understand them. A good test: could the reader explain this term to a friend after reading your sentence?

- **Paper-internal validation metrics** — metrics the authors use to prove their claims but that carry no intuitive meaning for the reader (e.g., F1 score, ARAT score, ERSP). Replace these with functional outcomes wherever possible: "the patient wrote his own name" instead of "ARAT score improved by 16 points." If a validation metric is genuinely the most important piece of evidence and cannot be replaced, keep it — but explain what it measures and why that number matters.

### Expression Style

- **No hype, no clickbait.** Never use "出人意料", "颠覆", "震惊", "重大突破", "groundbreaking", "gives hope to millions." Let the technical facts carry their own weight. If the result is genuinely surprising, the reader will feel it without being told.
- **No motivational commentary.** Don't editorialize about how this will "change lives" or "open new doors." The 10% comment at the end should be a concrete observation — what open question this raises, what would need to happen next — not a grand narrative.
- **Understated confidence.** "The paper reports X; if this holds across more patients, it would suggest Y" is better than "X proves Y."
- **Prefer concrete scenarios over abstract scores.** "患者写出了自己的名字" > "ARAT评分提高16分". Functional outcomes that a reader can visualize are more powerful and more honest than context-free numbers.
- **能不用比喻就不用比喻（硬规则，非"少用"）。** 这是相对数学/数据分析的学科，比喻很多时候会失真、反而让读者更摸不到头脑。**默认用朴素、准确、直接的人话**把术语/逻辑讲明白；比喻只在**确实非常贴切、且绝不引入误导**时，万不得已才用。能直说就直说。（2026-06-18 提出，2026-06-20 用户强烈重申并要求写死，理由：数学/数据学科里比喻易失真。）反面教材（2026-06-20 被点名为"让人困惑"）：把"两个超参数维度"说成"旋钮"、把"训练目标 vs 评测指标"说成"训练的尺/考试的尺"——这类比喻要么弃用、要么务必先把字面意思讲清。（"旋钮"因后文已大量使用，本期经用户同意暂留为例外，新内容默认不再引入新比喻。）
- **保留术语，别替换成会失真的俗话；拟人同样禁止（2026-06-30 用户重申，写死）。** 有专业术语就**直接用术语**（"激活函数""边缘化隐变量""对数线性""逆问题不适定"），不要为了"通俗"换成会失真的大白话或比喻。读者是泛神经科学背景，看得懂术语；看不懂会主动追问，那时再从第一性原理讲透。**拟人也算修辞、一并禁止**——本期被点名的反例："v1 拄着拐杖/v2 把它戒了"、把求和过程拟人化，这类一律弃用，改为字面陈述（"v1 运行时依赖按键时刻；v2 取消了这一依赖"）。
- **口语化可以，口水化不行（2026-06-30 用户定，写死）。** 文案与对话可以读起来自然、像在好好说话（口语化），但**不要为了"像人说话"而注水**：不堆语气词、不重复、不绕圈、不加无信息量的铺垫和感叹；一句话能讲清就不要两句。把握"自然但紧凑"的度。**这条同时管成品文案与给用户的全部叙述**（与全局 `~/.claude/CLAUDE.md` 的"科学、平实、保留术语"一节一致）。
- **本期（2026-06-30 Brain2Qwerty/MEG）被用户确认为表达与图卡的标杆样例。** 以后照此办：① **文案科学平实**——开篇身份直说、术语保留、少修辞零拟人、不口水化、承重数字带角标；② **图卡截干净**——用亮度投影定真实包围盒、逐版 `Read` 自检四边构件齐（标签/坐标/图例全进、邻图/散文图注全出），做到"这张卡的图恰好说明这张卡、不多不少"。

### Bilingual Content Workflow

> **⛔ X thread 默认不出（2026-07-30 用户定，写死）。** 从 2026-07-30 起，**除用户在当期明确要求外，不再生产 English X/Twitter thread**——每期的成品只有**中文小红书图卡**。所以 Step 5 只出小红书 copy、Step 7 只渲染小红书图卡、Step 8 的"最终版"也只含图卡。不要主动询问是否要 thread，也不要"顺手附上"。
> 用户明确说要 thread 的那一期，才回到下面这套双语流程（届时 thread 与图卡共用同一提纲、各自独立撰写、每条 ≤280 字符等规则全部照旧）。

1. **Start with a unified content outline** — a numbered list of information points and their order. Both the English X thread and the Chinese 小红书 cards are written from this outline. The outline determines what to include, what to omit, and in what sequence.

2. **Write each language independently from the outline.** Do not translate one from the other. The English version should read like native English written for an X/Twitter audience. The Chinese version should read like native Chinese written for 小红书 readers — not like translated English.

3. **Shared outline — but the two media may differ in depth.** Both versions follow the *same* outline: same logical spine, same order, same load-bearing facts. They need **not** be word-for-word information-equivalent. The two media have different affordances:
   - **X thread = text only.** It must say everything in words — no figures to lean on — so it stays tight and self-contained. Include only what text alone can make clear.
   - **小红书 = text + figures.** Because each card pairs words with a figure, it can go **deeper**: weave figure-reading into the narrative, elaborate where a figure earns it.
   What must stay consistent is the outline and the load-bearing claims; the 小红书 version may carry more detail. Neither version may contain a load-bearing claim the other contradicts.

### Information Sources

- **For events in China or involving Chinese institutions:** Always search Chinese-language authoritative sources (新华网, 澎湃, 国家药监局, etc.) to verify and supplement English-language reporting. Chinese sources often contain details (official product classifications, regulatory terminology, clinical trial numbers, patient counts) that English coverage lacks or simplifies. Chinese-source findings can also enrich the English thread with additional information dimensions.

- **For events in the English-speaking world:** Use English-language sources directly. The Chinese 小红书 version should verify Chinese translations of technical terms against established Chinese BCI literature, but does not need to search for Chinese-language commentary on English-world events.

- **Company, institution, and product names in Chinese:** Always confirm against Chinese sources. Do not transliterate from English — the official Chinese name may differ entirely (e.g., Neuracle Technology → 博睿康, not 神络医疗).

### Figures Are Always Shown Inline (贯穿全流程)

**只要某一步涉及图——论文原图、裁出的子图、或生成的卡片——默认就要把图本身真正贴进对话框内联呈现,绝不停在"这张图画了什么"的文字转述。** 这是贯穿全流程的硬性要求,不依赖各 step 各自重申。用户是看着图本身才能真正参与判断(对照 insight、检查图文对版、确认成品),文字描述替代不了。

#### 唯一正确的贴图方法(强制、默认)

**两步,就这两步:**
1. **把图存成本地文件**放进 `papers/`(浏览器 fetch 原图 blob → 触发下载 → `mv` 进 `papers/`;或 PyMuPDF 抽图;或 PIL 裁子图后另存)。
2. **用 `SendUserFile` 把这个文件推给用户**(`display:"render"`,可一次传多张、带 caption)—— 这是唯一确认能让图出现在用户界面里的方式。

**`Read` 只进模型上下文,不等于用户看见(2026-08-01 实测踩坑,写死)。** 桌面端会把 `Read` 折叠成一行工具调用(显示为 "Ran a command, read xxx.png"),用户界面里**看不到图**;当期用户明确反馈"我没看到任何图"。所以:**`Read` 用来给自己做裁图自检,`SendUserFile` 用来给用户看**。两者用途不同,不能互相替代;需要用户参与判断的每一张图都必须走 `SendUserFile`。

**裁子图(只想给某个 panel):** PIL `Image.crop()` 存成新文件 → 先 `Read` 自检四边构件齐不齐 → 再 `SendUserFile` 推给用户。原尺寸直接推即可,不要为体积纠结。

**不要做的事:** 不要把图转成 base64 塞进 `show_widget`/HTML widget —— 又慢又吃 token。也不要靠浏览器 `screenshot` 当作"贴给用户看"的手段(那种截图进的是模型上下文,用户界面里不一定可见)。

适用全流程,典型两处:
- **源图(Step 4):** 呈现 insight 时,贴出打算用的那 1-3 张论文原图(或其中关键 panel 的裁图)。
- **成品卡(Step 7/8):** "最终版"是真正渲染出来、推给用户的图卡(`card_generator.py` 产出 PNG 后用 `SendUserFile` 一次性推全套),不是纯文字 copy。

**抓图/裁图费劲不构成跳过的理由**——已知坑(懒加载占位符、URL 路径、内容过滤)见 Step 3,换方法继续直到图真的出现在对话里。**唯一例外**是确无浏览器、无法把图贴进对话的无头运行(cron/`claude -p`):那种情况要明确告诉用户"本次无法贴图、只能文字描述",而不是默默跳过。

---

## Project layout & paths (Claude Code)

This skill runs as a Claude Code project. Anchor all paths to these locations (working directory = project root):

- **Skill + resources:** `.claude/skills/dailybci/` — contains `SKILL.md`, `scripts/card_generator.py`, `fonts/`, and `knowledge-base/`.
- **Knowledge base:** `.claude/skills/dailybci/knowledge-base/` (`INDEX.md` + `papers/<subfield>/`). Wherever the text below writes `knowledge-base/...`, read it as `.claude/skills/dailybci/knowledge-base/...`.
- **Working data (per-run):** `papers/` at project root — downloaded full-text PDF/`<slug>-fulltext.txt`, figure images, and PIL crops. **Gitignored scratch:** not version-controlled (figures are baked into the committed `output/` cards), so it's regenerable and deleted at Step 9.
- **Output:** `output/<date>-<slug>/` at project root — generated card PNGs.

To import the card generator from project root:
```python
import sys; sys.path.insert(0, ".claude/skills/dailybci/scripts")
from card_generator import CardGenerator
```

---

## Mode A: Daily Digest

Trigger: "今天BCI有什么新的", "run the daily", "BCI日报", or any request for recent BCI news/papers.

### Step 1: Search for candidates

Find BCI-related papers and news from the past 48 hours. **Browser-first, search-as-supplement.** This is the same browser-first principle as Step 3, and it matters even more here: timeliness is the whole point of a *daily* digest, and the two failure modes that kill freshness both bite at this step.

**Why browser-first (do not skip this reasoning):**
- **Search-engine indexing lags days behind.** `WebSearch` rides a search index, and brand-new preprints (exactly the past-48h items we want) often aren't indexed yet — so search systematically returns work that's weeks old and *looks* recent. If you lead with `WebSearch`, you will quietly miss today's papers.
- **bioRxiv/medRxiv are Cloudflare-gated.** `WebFetch`/`curl` on their listing and abstract pages return 403, so you can't even read the fresh items search *does* point you to. A connected browser reads the rendered page and gets past this.

**Default path — connected browser (interactive runs).** First check for a connected browser (`list_connected_browsers`; `select_browser` if present). If one is connected, open the time-sorted listing pages directly and read them with `get_page_text`:
- **bioRxiv neuroscience, newest first** (clinical/preprint BCI lands here): the search-results page sorted by publication date descending, e.g. `biorxiv.org/search/brain-computer+interface numresults:30 sort:publication-date direction:descending` (URL-encode the spaces). Also worth a pass: `neural+decoding`, `speech+BCI`, `intracortical`.
- **arXiv recent** (computational/ML-for-neuro): `arxiv.org/list/q-bio.NC/recent` and `arxiv.org/list/eess.SP/recent`. Note arXiv doesn't post on weekends — on Sat/Sun the freshest batch is Friday's.
- **Company/regulatory & researcher social** — open the source pages directly (Neuralink/Synchron/Paradromics/Precision blogs, FDA, X/Twitter of domain researchers).
- Then use `WebSearch` to **supplement** — news framing, and cross-checking anything the listings surfaced. Search is the second pass, not the first.

**⛔ 期刊正刊必须每天单独扫一遍（2026-08-04 用户定，写死）。** 预印本服务器只覆盖 BCI 的一部分——**很多最重要的工作直接发正刊、从不上 bioRxiv/arXiv**（尤其是临床试验、系统神经科学、器件工程）。只扫 bioRxiv + arXiv 会系统性漏掉这一整类。所以每天 Step 1 里，除预印本外，**必须再扫一遍下面这批期刊的「最新上线」页**，与预印本并列作为候选来源，不要降级成"WebSearch 顺带补一下"：

| 期刊 | 最新上线页 |
|---|---|
| Nature | `nature.com/nature/research-articles` |
| Science | `science.org/toc/science/0/0`（Current / First Release） |
| Cell | `cell.com/cell/newarticles` |
| Neuron | `cell.com/neuron/newarticles` |
| Nature Neuroscience | `nature.com/neuro/research-articles` |
| Nature Medicine | `nature.com/nm/research-articles` |
| Nature Biomedical Engineering | `nature.com/natbiomedeng/research-articles` |
| Current Biology | `cell.com/current-biology/newarticles` |
| Nature Communications | `nature.com/ncomms/research-articles`（按 neuroscience 主题筛） |
| Science Advances | `science.org/toc/sciadv/0/0` |
| NEJM | `nejm.org/browse/specialty/neurology-neurosurgery` |

做法：浏览器打开各刊的 new-articles / 最新目录页 → `get_page_text` → 按 BCI 关键词过一遍标题。刊多时可分两轮（Nature 系一轮、Cell 系 + Science 系一轮）。命中的正刊工作与预印本候选**平等参与 Step 2 的候选表**；正刊是 version of record，同等质量下优先于预印本。

**⛔ 上表 11 个刊必须逐个扫完、逐个报，不许漏刊、不许合并报、不许用出版节奏推断（2026-08-05 用户因实际漏扫而写死）。** 起因：当期我实际只开了 9 个刊——**Cell 主刊整个漏了**（只扫了 Neuron 和 Current Biology，汇报时却写成"Cell 系"），Science First Release 只读到返回被截断的前十几条就停了，Science Advances 页面跳到 `no-first-release` 返回空之后，我**按"周刊、上一期 7/31、48h 内不会有新的"推断了没有**。用户当场问"为什么没扫 science 和 cell"。三条硬规则：

1. **逐刊清点，扫完为止。** 每个刊都要单独 navigate + 取到标题列表，取回的列表被截断时**必须分片取完**（`slice(0,25)` → `slice(24,46)` … 直到覆盖全部条目），不能读到一半就当扫过了。Cell 主刊、Neuron、Current Biology 是**三个独立的刊**，不能用"Cell 系"一笔带过。
2. **推断不算核查。** "这是周刊，本周还没到出版日""上一期是上周五，窗口内不会有新的"——这类基于出版节奏的推理**一律不作数**，必须真去当期目录页看到最新一条的日期。页面结构变了（如 Sci Adv 无 First Release 通道、跳转到别的 URL）就换入口（当期目录 `science.org/journal/sciadv` 的 Current Issue）再看，不要用空返回值当"没有新内容"的结论。
3. **汇报用逐刊清单，写明"最新一条的日期"。** 给用户的 Step 1/2 汇报里必须逐刊列出：**刊名 → 扫到的最新一条上线日 → 有无 BCI 命中**。写"最新一条 7 月 30 日"这种可核实的事实，胜过写"无命中"这种无法回查的结论。整刊没打开就如实说没打开，绝不写成扫过了。

**顺带产物：窗口外但相关的命中要单独记一笔。** 扫刊时常会碰到与知识库某条线直接对话、但上线日落在 48h 窗口外的论文（本期例：Cell 6/24 的 *Shared neural geometries for bilingual semantic representations in human hippocampal neurons*，人类海马单神经元 × 双语语义，对 `silva-2024` 与 semantic-decoding 线）。这类**不进候选表**（时效不符），但要在汇报末尾单独提一行，供用户挑去补库或做"错过的好文"。

**Fallback path — no browser (headless / cron / `claude -p`).** Run at least 3 different `WebSearch` queries to cast a wide net, and pull preprint text via open APIs (e.g. NCBI BioC) rather than `curl` on the gated sites. Be explicit with the user that without a browser the freshest 48h may be under-covered due to index lag.

**Honesty about the window:** the field does not produce a landmark every day. If the strict past-48h window is genuinely thin (common on weekends), say so in one line and present the most significant *recent* (this-week) work instead — degrade gracefully, never skip a day, never pad the freshness column.

Source priority:
1. **Academic preprints & journals（两条腿，缺一不可）** — 预印本：arXiv (q-bio.NC, eess.SP, cs.AI+neuro)、bioRxiv、medRxiv；**正刊：Nature / Science / Cell / Neuron / Nature Neuroscience / Nature Medicine / Nature Biomedical Engineering / Current Biology / Nature Communications / Science Advances / NEJM，每天单独扫最新上线页**（表见上）
2. **Conferences** — if SfN, NeurIPS, BCI Society, IEEE EMBS, or similar is happening, prioritize its outputs
3. **Researcher social media** — X/Twitter posts from domain researchers
4. **Company & regulatory** — Neuralink, Synchron, Paradromics, Precision Neuroscience, FDA, NIH BRAIN Initiative

Search terms: "brain-computer interface", "BCI", "neural decoding", "neuroprosthesis", "ECoG", "intracortical", "neural interface", "brain-machine interface", "speech BCI", "motor decoding", "closed-loop neural", combined with date-relevant terms.

**⛔ 不许只靠标题关键词过滤候选（2026-08-04 因实际漏检而写死）。** 起因：当期用 bioRxiv API 拉全窗口后跑关键词正则，把 *Linguistic contextualization in the human hippocampus* 滤掉了——该标题不含任何 BCI 关键词，内容却是**人类海马单神经元 + 自然语音**，与知识库 `ismail-2026-naturalistic-word-meaning` 同组同线，本该进候选表。**关键词过滤的假阴性比假阳性危险得多**：假阳性你一眼就丢掉，假阴性你根本不知道自己漏了。所以：
1. **按类目全量看标题，别按关键词过滤。** bioRxiv/medRxiv 用 API 拉日期区间（`api.biorxiv.org/details/biorxiv/<from>/<to>/<cursor>`，每页 30 条，翻到 `total` 为止），筛出 `neuroscience` + `bioengineering` 类目后，**把标题整张列出来自己逐条看**。48h 窗口通常只有 40–60 篇，人眼扫得完。
2. **标题看不出的就读摘要**，别猜。凡是涉及"人类颅内记录/单神经元/自然刺激/闭环/解码/植入/皮层刺激"的，哪怕标题很像纯认知神经科学，都读一遍摘要再决定。
3. **关键词正则只用来排序、不用来删除**——命中的排前面看，未命中的仍然要过一遍标题。

**⛔ 报告"新鲜度"前必须核版本号 / 原始公开日期（同日写死）。** 同期还踩到第二个坑：bioRxiv API 的 `date` 是**该版本**的上线日，正刊的上线日同理。当期看起来落在 48h 内的两条，实为旧工作的新版本——海马那篇是 **v3**（原始预印本 2025-06），Nature Neuroscience 那台全息中尺度显微镜是 **2026-08-03 正刊**但预印本 **2023** 年就公开了。**把改版日/见刊日当成"新工作"报给用户，是让日报的"新"失真。** 所以候选表的「时效」列必须分开写两件事：**这个版本的日期** 与 **这项工作首次公开的日期**，例如"8/3 正刊 ✓，预印本 2023 年已公开"。核法：bioRxiv API 的 `version` 字段、或 DOI 里的年份（`10.1101/2023.xx.xx` 即 2023 年首发）。

### Step 2: Present 2-3 candidate topics for user selection

This step requires the knowledge base. Load it before making judgments.

1. Read the index file at `knowledge-base/INDEX.md` to understand what milestone papers exist and which sub-fields are covered.
2. For each candidate from Step 1, identify its sub-field (e.g., speech-decoding, motor-BCI, electrode-hardware, signal-processing).
3. Load the 3-5 most relevant milestone paper summaries from `knowledge-base/papers/` matching that sub-field.
4. Evaluate each candidate against this context:
   - Does this advance the state of the art meaningfully compared to the milestones?
   - Does it introduce a genuinely new approach, or is it incremental tuning?
   - Does it break an assumption the field currently holds?
   - Is the margin of improvement large enough to matter?

**这是一个强制的确认关卡（hard gate）。** 机器只负责搜集候选、给出推荐理由和知识库对照；最终选哪篇由用户拍板。在用户明确确认选题之前，绝不进入 Step 3、绝不深读论文、绝不生成任何内容。不允许机器自己选定后直接往下走。

**Present 2-3 candidates to the user (strict limit: never exceed 3).**

呈现目的是让用户 3 秒内扫完、快速选定，不是让用户读长文。因此候选清单**必须用一张表格**呈现，每个单元格压缩到一句话/一个短语，绝不展开成段落或多层 bullet。表格列固定如下：

| # | 选题（原文标题+来源+物种） | 团队·单位·影响力 | 子领域 | 时效 | 知识库对照 | Significance（一句话，标物种） | 可讲角度 |
|---|---|---|---|---|---|---|---|

把握平衡：**前五列要极简**（一眼扫过），**后两列要给足判断依据**——不能瘦到用户无法据此做选择。

各列填写要求：
- **#**：1 / 2 / 3。
- **选题**：填**论文/新闻的原标题（verbatim，可适度缩短但不要改写成你的转述）** + 来源 + 物种，一行。你的 hook/切入口归「可讲角度」列，不要写在这里。
- **团队·单位·影响力**：一句话点出**通讯/一作 + 实验室/机构 + 行业影响力**——这是谁的工作、为什么权威或这是哪条路线（如"Francis Willett · Stanford 神经假体实验室 · 2023 年 62 词/分语音 BCI 一作"；或"Flavio Donato 组 · Basel · 海马环路动力学"）。看文章本质看人/看实验室；这一列也是用户长期积累"领域 taste（谁在认真做、哪条线归谁推）"的核心载体。叫不准影响力时如实写"团队影响力待核（首次见到）"，不要编造资历。
- **子领域**：单个标签。
- **时效**：标"48h内 ✓"或"较早（X月）"，一眼看出新鲜度。
- **知识库对照**：填对照 milestone 的文件名（如 `willett-2023`，不必写全路径）；找不到对照就填 **"⚠ 无对照基准"**，并触发下方「知识库缺位处理」。
- **Significance（1-2 句，标物种）**：相对那篇 milestone 具体做到了什么新东西。**必须带上关键数字或明确对比**（如"62→78 词/分钟""从单被试到跨 5 名被试"），不能只写"有提升"这种空话。这是用户判断"值不值得讲"的核心依据。
- **可讲角度（1-2 句）**：选它的话具体聚焦哪 1-2 个点，要写出真正的 hook（那个会让人停下来的点），而不是泛泛的"讲讲它的方法"。

表格之外不要再为每个候选写额外的展开段落。若某条有纯技术性的小硬伤（如公司名待核查），用表格下方一行**脚注**带过。

**例外——知识库缺位不能塞进脚注。** 只要任一候选的「知识库对照」列是"⚠ 无对照基准"，必须在表格和推荐之后用一个**独立、醒目的提示块**单独处理（见下方「知识库缺位处理」），不要把它降级成脚注或夹在备注里一笔带过。这是整个选题流程的一个关卡，必须让用户一眼看到并明确回应。

如果搜索结果不足 2 篇值得候选的，降级处理——有几篇呈现几篇，并用一句话说明今天的情况。Never skip a day.

**表格后，给出推荐（2-3 句，给足理由）：**
- **我的推荐**：我倾向选 X。理由要具体到能让用户据此判断——说清它相对另外两个候选的取舍（为什么是它而不是另两个：时效？分量？知识库空白？insight 的稀缺度？），不用炒作词。这不是一句套话，而是帮用户做决定的实质论证。
- 末尾把决定权交回用户："选题权在你——你选哪个？想了解某篇更多再决定，随时问。"

用户可能会追问（例如："这个团队是谁？""用的什么电极？""和 XX 那篇有什么区别？"）。这些追问是选题决策的一部分，不是闲聊。耐心回答，直到用户明确说"选这篇"或给出等价确认。不要催促用户做决定。

#### 知识库缺位处理（当任一候选标注"⚠ 无对照基准"时）

这是一个**独立、醒目的提示块**，紧跟在推荐之后输出。用 `> ⚠️` 引用块的形式让它视觉上跳出来，不要混进正文。它要把逻辑讲清楚——分三部分：

**① 点明哪条候选缺基准。** "候选 X（[topic]）在知识库里没有可对照的 milestone。"

**② 解释为什么这是问题（关键，不能省）。** 缺基准意味着**机器对这条工作"有多重要、是不是真新"的判断缺少历史参照，可能高估或低估**。一句话说清这层因果，让用户理解为什么要停下来，而不是觉得这只是个无关紧要的备注。按缺位程度选用对应措辞：
- **完全没有知识库**："知识库还没建好，今天整批候选都没有历史基准，所有重要性判断都只是基于当下搜索、可信度有限。"
- **子领域有但条目太少**："知识库中 [subfield] 方向仅 N 篇相关，不足以支撑对这条工作的重要性判断——我现在的评估可能不准。"
- **子领域有但没有匹配此具体主题**："知识库中 [subfield] 有条目，但没有与 [topic] 这条具体路线直接对应的 milestone，所以我对它'是不是首个/有多大突破'的判断缺少对照，存在说过头或说轻了的风险。"

**③ 明确询问是否触发补库流程（醒目的二选一）。** 不要含糊，给出清晰的两个选项让用户直接回应：
> **是否先补足知识库？**
> - **补**：我切到 Mode B，搜这个方向的综述、补几篇 milestone 进知识库，然后回到 Step 2 从头重审今天这批候选（带着新基准重新判断）。
> - **不补**：先按现有信息继续，但你我都清楚这条的重要性判断缺历史对照。

如果用户选择"补"：切换到 Mode B 完成该子领域的知识库补全，然后 **回到 Step 2 的开头，带着新加载的上下文从头重新评估全部候选**（重新做对照、重新给 significance、重新给推荐），而不是只补评那一篇。补完后的重审同样是强制确认关卡，仍需用户拍板。

### Step 3: Obtain the paper's full text + key figures

After the user confirms their topic choice, get the full paper. **Browser-first, download-fallback.** A connected browser reads the rendered page directly and gets past the Cloudflare / JS / soft-paywall gates that block `curl` — so it usually retrieves both the full text and the figures in one go. Reserve PDF download for the cases the browser can't cover.

#### 正刊优先,付费墙挡住时回退到 OA 预印本(2026-06-16 定)

期刊正刊是 version of record,**优先用正刊**。但顶刊(Nature Medicine、Nature、NEJM 等)常**不开放获取**——全文和高清原图都在付费墙后,浏览器/curl 都拿不到完整 PDF 与图。这种情况下:
1. **回退到该论文的 OA 预印本**(bioRxiv/medRxiv,同一篇)拿全文 + 全部图——这是允许的现实回退,不是偷懒。
2. **预印本"未经同行评审",定稿可能与正刊有个别数字/图的微调**,所以走预印本时,承重数字要在 Step 6 **额外与正刊摘要 / 官方新闻稿交叉核对一次**。
3. **溯源(封面 source / 尾卡 / thread refs)以正刊为准**,并注明图取自预印本,例如"Nature Medicine 正刊《…》(图取自 bioRxiv 预印本 <doi>)"。

#### 一次性扒全 — 强制,选题确认后立即做(在进 Step 4 之前)

**选题一确定,就把这篇的全文 + 全部图一次性落到本地,后面所有步骤只读本地文件,不再回访浏览器。** 这是为了避免反复访问网页 / 重复下载(实测会触发浏览器卡死、Cloudflare 拦截、多次下载被拦),也让 Step 4 理解、裁子图、Step 6 事实核查、Step 7 配图全程快而稳。

落选题后**马上**做两件事:
1. **下全文 PDF(首选):** 通过浏览器(Chrome 连接)把这篇的全文 PDF 下到 `papers/<slug>.pdf`,再用 PyMuPDF 在本地抽出全文存 `papers/<slug>-fulltext.txt`。**优先走 PDF,不要把渲染网页的全文整篇拉进上下文**——那样既烧 token、又得过浏览器内容过滤器(URL/符号被拦)反复切片净化,既慢又易丢内容。bioRxiv 的 PDF 用 `curl` 会被 Cloudflare 拦,所以走浏览器下载(和下图同套路:页面内 `fetch` blob → `<a download>` → `mv` 进 `papers/`)。之后深读、事实核查、图的裁取全部读本地文件 / 本地图,**一律不再回访网页**。
2. **全图先下:** 不要只下"打算用的那几张"——**把 F1 起逐张 `fetch(...).then(r=>r.status)` 探到 404 为止,把所有返回 200 的图全部下载存进 `papers/`**(`donato-fig1.jpg`…`fig6.jpg`)。哪几张进卡片是 Step 4/7 才定,但全下成本极低、且省掉来回跑。遇到 Chrome 多下载拦截就按下面 Gotcha 处理(提示用户点 Allow,或每次 re-navigate 后下一张)。**已下好的本地图别再 `curl` 覆盖**(会被 403 HTML 冲掉)。

下面的浏览器/下载细节是**实现这两件事**的手册。

#### Default path — connected browser (interactive runs)

If a browser is connected (Claude in Chrome), use it as the default:

1. **Open the paper's page** — prefer the OA full-text HTML: bioRxiv/medRxiv `.../vN.full`, PMC full-text, or the publisher's OA page.
2. **Get the full text from the downloaded PDF** (一次性扒全 above) for deep reading (Step 4) and fact verification (Step 6) — `fitz` → `papers/<slug>-fulltext.txt`, then grep locally. **Don't scrape the rendered page text into context.** (If you ever must pull a snippet in-page, note the content filter blocks returns containing URL/symbol tokens `http`/`?`/`=`/`&`/`.jpg` — strip/replace them and slice under the 50k char limit — but PDF-first avoids all of this.)
3. **Download ALL figures + the full-text PDF** (per 一次性扒全 above — F1 probed to 404, plus `<slug>.pdf`) so every later step reads local files. This is fiddly on bioRxiv — here is the recipe that actually works, learned the hard way (use it instead of rediscovering the gotchas):
   - **Gotcha A — the content filter eats URLs.** `javascript_tool` return values containing URL/query-string-like tokens (`http`, `?`, `=`, `&`, `.jpg`, long base64, even mangled URLs) get blocked as "Cookie/query string data". So **never try to read the image URL back out** — keep URLs *inside* the page and act on them there. Long `get_page_text` (>50k chars) also errors; slice via `javascript_tool` and strip URL tokens (replace `=`/`/`).
   - **Gotcha B — inline `<img>` are lazy-loaded placeholders** (0×0, broken icon). Don't screenshot them and don't trust their `src`. Fetch the real bytes instead.
   - **Gotcha C — the highres path.** On bioRxiv the working full-size URL is the **`/early/` path**, not the article-DOI path: `‹origin›/content/biorxiv/early/<YYYY>/<MM>/<DD>/<numeric-doi>/F‹N›.large.jpg` returns 200 (~100-130 KB). The `/content/<doi>vN/F‹N›.large.jpg` form 403s, and `.large.gif` 404s. Confirm the date/numeric-doi from the abstract page first, then probe a few patterns with `fetch(...).then(r=>r.status)` and keep the one that returns 200.
   - **Gotcha D — the newer bioRxiv platform (DOIs under `10.64898/…`) breaks the figure-URL route.** On this namespace the `/early/.../F‹N›.large.jpg` path 404s (those derivatives aren't generated), and rapid programmatic `fetch()` bursts get **429-throttled** for minutes. Don't fight it by probing figure URLs — **download the full PDF and extract every figure with PyMuPDF** (`page.get_images` → `Pixmap.save`), which is the 首选 for text anyway, so one PDF yields text *and* all figures in one shot. If even the PDF `fetch` 429s: **navigate the tab directly to the `…v1.full.pdf` URL** (Chrome's PDF viewer loads it as a normal top-level request the throttle doesn't hit), then `fetch(location.href)` in-page → blob → `<a download>`. If the download is browser-blocked, ask the user to open/allow it (per `shortest-path-on-user-resolvable-blockers`).
   - **Download a figure to `papers/`:** fetch the blob in-page (`fetch(earlyUrl,{credentials:'include'})`) and trigger a download via a temporary `<a download>` click, then `mv ~/Downloads/<name> papers/`. (`curl` on the image CDN usually returns the Cloudflare HTML challenge, not the JPEG — don't rely on it. **Don't `curl` over a good local file** — it'll clobber it with the 403 HTML page.)
   - **To display any figure to the user:** do NOT use browser `screenshot` (that image only enters the model context, not reliably the user's chat). Per Content Standards → *Figures Are Always Shown Inline*: the figure is already a local file in `papers/`, so just **`Read` that file** — Read renders it inline in the user's chat. To show one panel, `PIL Image.crop()` it to a new file, then `Read`. Reliable recipe: put explanation text first and the `Read` as the last line of the message.
   - **If the download is blocked by a browser permission, STOP and ask the user to click "Allow" — do not build a workaround.** Chrome blocks *multiple automatic downloads* per page after the first: the 1st figure lands, the rest are silently blocked behind an "Allow / Block" chip the user may not even notice. The correct move is a one-line prompt: *"Chrome is blocking multiple downloads — please click 'Allow' on the download prompt (top-right of the address bar), then I'll continue."* A workaround that worked this-session-only: trigger **one** download per fresh page-load (re-`navigate` the tab between each), since the per-load block resets. **Do NOT** stand up a local HTTP server to receive POSTed bytes — it dead-ends on Private Network Access preflight + extension network sandboxing, and the repeated DOM-wiping freezes the tab. This is a specific instance of a general rule (user, 2026-06-19): **whenever something just isn't working and the user — who's right there at the machine — could clear it faster by doing it themselves (a permission/download/auth popup, but also a rate-limit, a flaky fetch, a frozen tab), stop and prompt them in chat immediately and explicitly (say what to do); don't grind on technical workarounds or long back-off retry loops to route around a human in the loop.** Only work around it when the user genuinely cannot intervene (headless/cron). See memory `shortest-path-on-user-resolvable-blockers`.
   - **Do not read or base64 the browser's session cookies** to feed an external download — blocked as credential exfiltration. Fetch inside the page's own credentialed context instead.
   - **The PDF is the full-text source (首选):** download it via the same in-page `fetch` blob → `<a download>` route (curl gets Cloudflare-blocked), then `fitz` to `papers/<slug>-fulltext.txt`. Don't scrape the rendered page text into context — it burns tokens and trips the content filter. See 一次性扒全 above.

#### Fallback path — download (any one trigger is enough)

- **Headless / cron / `claude -p` runs with no browser to connect** — the only path. Pull full text via an open API (e.g. NCBI BioC: `https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/<PMCID>/unicode`), or download the PDF via `curl`.
- **Page exposes only an abstract** (full text paywalled) but an OA preprint PDF exists elsewhere.
- **Step 8 needs higher-resolution figures** than the web serves.

When downloading:
```bash
curl -L -A "Mozilla/5.0" -o papers/[author-year-slug].pdf "<pdf-url>"
file papers/*.pdf   # confirm "PDF document", not an HTML challenge page
```
Then extract text + figures with PyMuPDF (fitz):
```python
import fitz
doc = fitz.open("papers/[slug].pdf")
text = "\n".join(p.get_text() for p in doc)
for pno, page in enumerate(doc):
    for i, img in enumerate(page.get_images(full=True)):
        pix = fitz.Pixmap(doc, img[0])
        if pix.n > 4: pix = fitz.Pixmap(fitz.csRGB, pix)
        pix.save(f"papers/[slug]-p{pno}-{i}.png")
```
- Reality check (learned the hard way): bioRxiv/medRxiv sit behind Cloudflare and PMC behind a JS download gate, so `curl` often returns an HTML challenge page, and the NCBI OA FTP may be blocked by the sandbox. If downloads fail and no browser is available, fall back to the BioC full-text API for text and ask the user to drop a PDF into `papers/` for figures. This soft-gate problem is exactly why the browser is the default.

### Step 4: Identify THE core insight

The hardest and most important step. The goal is NOT to summarize everything in the paper. It is to answer one question:

**"What is the ONE thing in this work that matters most to a reader who follows BCI?"**

This is NOT about technical comprehensiveness. It's about finding the single most compelling angle — the one thing that would make someone stop scrolling.

**The insight must be concrete and human-graspable.** Good examples:
- "瘫痪患者用意念控制机械臂，自己喝到了咖啡" — 聚焦：患者具体做到了什么？康复到什么程度？什么样的日常任务可以完成了？
- "解码速度从 15 词/分钟跳到 62 词/分钟，第一次接近正常说话的速度" — 聚焦：一个关键数字的跃迁和它的意义
- "电极植入 9 个月后信号不但没衰减，反而变强了" — 聚焦：一个违反预期的发现

**Bad examples (too scattered):**
- "这篇论文使用了新型解码算法，改进了信号处理流程，在多名患者中验证了有效性，并讨论了临床转化路径" — 四个点都蜻蜓点水，没有一个讲透

Use the milestone paper summaries loaded in Step 2 to sharpen this judgment:
- What was the previous best result? By whom, when?
- What specific limitation did this work overcome?
- Is the improvement in the method, the scale, the robustness, or the clinical setting?

Distinguish clearly between:
- **Standard practice** in the field — mention only as brief context (one sentence max)
- **This paper's unique contribution** — explain this thoroughly: the mechanism, the principle, why it works where previous approaches didn't

A good test: if you removed your explanation of this one point, would a reader miss the most important thing about this paper? If yes, you found it.

#### Step 4a: 背景对齐关卡 —— 先讲清"这篇在解决什么问题"，再谈 insight（2026-07-17 用户定，写死）

**这是 Step 4 的第一个动作，也是一道独立的确认关卡：在抛出任何 insight 之前，必须先把这篇论文所处的大背景讲清楚，并停下来等用户确认。** 用户不确认背景，不许进入 insight 呈现。

**为什么写死这条（起因）：** 本条源于 2026-07-17 的 sEEG 植入精度那期——我直接抛出"进针角度是最强相关因子（ρ=0.28）""框架式 vs 机器人"这类判断，默认了用户已经知道 sEEG 手术怎么做、什么叫框架式、什么叫径向误差。用户的原话是"我是一脸懵的"。**根因是我把"选题时的候选表"当成了背景交代——它不是。** 候选表回答的是"值不值得讲"，背景回答的是"这到底是个什么事"。两者不能互相替代。

**根本原理：用户无法判断一个他不理解其背景的 insight 的质量。** insight 的价值恒等于"它相对背景推进了什么"——背景缺席时，再准确的 insight 也只是一串悬空的名词和数字，用户既没法判断它好不好，也没法判断自己想不想深入。**这一步不是礼貌性的铺垫，它是让确认关卡真正有效的前提。** 没有它，用户的"确认"只是在盲签。

**必须讲清的四件事**（顺序即讲述顺序，全部用字面、平实的说法，术语首次出现就地解释）：
1. **这个领域在干什么、为什么要干** —— 这项技术/手术/范式本身是做什么用的，它服务的真实需求是什么。假设用户没听说过。
2. **现状与卡点** —— 目前是怎么做的，做到什么程度，卡在哪。这里要把后文会用到的**每一个核心名词就地讲透**（如"框架式""机器人辅助""径向误差 vs 欧氏误差"），并且**讲清它们各自要解决的问题**——名词不能只给定义，要给"它为什么存在"。
3. **这篇论文站在哪一格** —— 它接的是谁的问题，动的是哪一格。此处可引知识库条目。
4. **为什么这个问题值得关心** —— 特别是当选题不在 BCI 主线上时（如本例是癫痫外科），必须说清它与 BCI 的关系，别让用户觉得跑题。

**呈现方式（硬性）：**
- **一次只出一小块，出完就停下来问。** 不要把背景 + insight + 对比分析一股脑倒出来。背景本身若较长，也要拆成小块逐块确认。**理由（用户 2026-07-17 原话）："我最开始就有问题，后面的我也不可能看得懂的。"** 前一块没懂，后面全部作废，且用户的阅读负担被白白浪费。
- 讲完背景明确交回："**这个背景清楚了吗？有没有哪个概念要我再展开？**"——用户确认后才呈现 insight。
- 用户在背景阶段追问，**耐心逐个答透，一次答一个**，不要急着回到内容生产。这些追问是产品的核心价值（见记忆 `user-stepwise-tech-tutorials`），不是打断。

**用户随时可以喊停内容生产、转成纯讲解模式。** 出现这种情况时，**放弃 Step 5–8 的节奏，转入教学**：一次一小部分、给路线图、从第一性原理拆、拒绝堆名词。日报可以晚一点，甚至这期不出——用户把论文搞懂的价值高于按时出稿。搞懂之后再问要不要回到生产。

**呈现 insight 并等待用户确认，然后才进入 Step 5。** 与 Step 2 一致——机器不是中立地把选项摆出来，而是**先给出自己带理由的主张**，让用户在一个明确判断上做确认或反驳。简洁地告诉用户：

- **我认为这篇最该讲的核心 insight 是 X**（一两句话讲清那"一件事"）。
- **为什么是它（理由，不能省）**：这是把它从"标准操作"里拣出来的依据——相对知识库里的前作/里程碑，这一点为什么是真正新的、最值得讲的。一两句话，可引知识库具体条目。
- **打算从哪个角度展开**：机制？关键数据？患者故事？监管逻辑？说清你倾向哪个切入口。
- **必须在对话框里贴出打算用的那 1-3 张论文原图，让用户边看图边对照你的 insight 判断——这是硬性要求，不是可选项。** 用户是看着图本身（不是看你"这张图画了什么"的文字转述）才更有感觉、才能真正参与到 insight 的判断里。具体做法见 Content Standards → *Figures Are Always Shown Inline*：图已在 Step 3 下载到 `papers/`，**直接 `Read` 该文件即内联渲染**（要看某个 panel 就 PIL crop 成新文件再 Read）；文字写在前、`Read` 放消息最后一行。**不要用浏览器 `screenshot`**——那种截图只进模型上下文、用户界面里看不到。每张图配一句话说明它为什么支撑这个 insight。这是源图、不是生成的卡片，不违反下面"确认前不做卡"的规则。
  - **抓图费劲不构成跳过的理由。** 如果第一种方法没抓到（懒加载占位符、URL 路径不对、内容过滤拦截等，全是已知坑，见 Step 3），换方法继续抓，直到图真的出现在对话里；不允许因为"抓不到"就只用文字描述带过。唯一例外是确无浏览器的无头运行（cron/`claude -p`），那种情况要明确告诉用户"本次无法贴图、只能文字描述"，而不是默默跳过。

然后把判断权交回用户："我倾向这个角度——你觉得对吗？还是该换一个？"

用户可能会：
- 直接确认 → 进入 Step 5
- 提出不同角度 → 重新调整 insight，再次确认
- 追问细节 → 耐心回答，直到用户满意

**在用户确认 insight 之前，不要生成任何 thread 文字或卡片图片。** 这些都是算力密集的操作，方向不对就全部白费。

#### 横纵对比小分析（每期固定动作，2026-06-23 用户定）

**这是日报的核心价值锚点：我们有一个持续扩充的知识库,能"博通古今"地把今天这篇放进坐标系里看。所以每期在 insight 确认后(相关里程碑已加载好时),都要顺手做一份简短的横纵对比小分析——首先是给用户的学习增量,其次是日报潜在的信息增量。** 不是可选项,每期都做(KB 覆盖不足时按下方降级)。

- **纵轴(历时 / longitudinal)**:这条问题/技术线从早到今天怎么演进的——从 KB 拉关键几篇里程碑串成一条链,说清这篇站在谁的肩膀上、把哪一格往前推了(如 `perge-2013 → downey-2018 →（本篇）` 从"被动观察状态相关漂移"到"主动操纵注意负荷")。
- **横轴(共时 / cross-sectional)**:同期(同年前后)其他组在做同一问题 / 相似问题的工作——相似技术或不同技术路线都要看;从 KB 拉 1-3 篇,对比各自的路线选择、取舍与结果差异(如非侵入 EEG-BCI 侧的注意效应 vs 本篇皮层内侧)。
- **产出形态**:一份简短的对比小报告(几句话 + 必要时一个小表),在 Step 4 insight 确认之后、进 Step 5 初稿之前呈现给用户。**目的首先是用户的学习过程**,不必每条都进日报。
- **升格规则**:若某条横/纵对比特别精彩、构成"超出单篇解读的信息增量",就把它编进当天日报——thread 加 1 条对比 tweet,或小红书加 1 张对比卡(对比卡同样守三段式 + 图文对版)。普通的对比留在小分析里即可。
- **硬约束(承接 §Factual Accuracy 与 Step 2 缺位处理)**:对比**必须基于 KB 真实条目或当场核实的来源**,绝不凭记忆编造"同期某组也做了 X"。KB 在该方向覆盖不足时,如实标"此方向 KB 尚薄、横向对比有限",并可顺势提议补库(Mode B),**不硬凑一个看似博学的对比**。

### Step 5: First draft — 小红书 copy with rough figures, in chat

**默认只出小红书 copy（X thread 默认不出，见 Content Standards → Bilingual Content Workflow 顶部的写死条款）。** 下文凡提到 thread 的部分，仅在用户当期明确要求 thread 时才适用。

Right after the insight is confirmed, produce the **first full version** and present it in chat: the 小红书 card-by-card copy (plus the English X-thread copy **only if the user asked for one this issue**), with **each figure card's figure shown inline (a rough crop is fine)** so the user sees text+figure paired from the very first version. This is the content layer — logic, numbers, comparisons, and the text–figure pairing — produced cheaply so it can be revised and fact-checked **before** the expensive final card rendering. (Rationale: rendering polished cards is the heavy step; if a core number is wrong, that work is wasted. Facts first, polished production later. But rough crops of already-downloaded figures are cheap, so pair them in from the start — don't make the user imagine the layout.)

Both versions are written from the **shared outline** (see Content Standards → Bilingual Content Workflow) and cover, in order:
- Enough context to understand the problem (2-3 sentences, no more)
- What exactly they did differently — the mechanism, the principle, the technical specifics
- Why this approach works where previous ones didn't — cite specific comparisons to milestone papers from the knowledge base
- The evidence: key numbers, before/after comparisons, statistical claims, **species and sample size**
- A 1-2 sentence understated closing comment (the "10%")

Practical notes:
- **X thread** = self-contained in text (no figures to lean on, keep it tight, respect the per-tweet char limit — see Step 7). **小红书** = conclusion→read-figure→transition per card (see Step 7 card rule 4).
- **Figures here may be rough** — quick PIL crops of the figures already downloaded in Step 3, shown via `Read` (save + Read; never browser `screenshot`). **Do NOT run `card_generator.py` or polish yet** — cleanup and rendering happen at Step 7/8.
- Label species and sample sizes; keep every number traceable for the fact-check that follows.

**Then proceed directly to Step 6 — do not wait for the user to approve the wording.** Facts get checked first; the expensive rendering waits until after.

### Step 6: Fact verification

This step runs automatically after the **content draft** (Step 5) is generated — do not wait for the user to ask. The user reviews the verification table before any discussion of wording or style. Facts first, polish later. Figures and cards are **not** needed to fact-check — verify numbers against the source text and the figure captions/data already read in Step 3.

**Three-layer verification:**

**Layer 1 — Trace back to source.** List every quantitative claim and key fact in the draft (numbers, dates, injury classifications, success rates, timelines, species, sample sizes). For each one, locate the exact source in the original paper (figure, table, or sentence). Mark as ✓ if confirmed, ✗ if wrong, ⚠ if cannot verify.

**Layer 2 — Cross-source check.** For Chinese institutions, products, regulatory approvals, and official classifications: search Chinese authoritative sources (国家药监局, 新华网, 澎湃, official company sites) to verify names, classifications, and details. For non-Chinese entities, verify against their official communications. Mark any discrepancy.

**Layer 3 — Assertion audit (knowledge base + web search).** Identify every comparative or generalizing statement in the draft — anything that uses "first", "most", "all", "首次", "大多数", "都", or implies a broad pattern. Verify in two steps:
1. Check the knowledge base for counterexamples or supporting evidence
2. If the knowledge base coverage is insufficient for a confident judgment, use web search to find a recent review or authoritative source that addresses the claim. Prefer peer-reviewed reviews (Nature Reviews, Lancet Neurology, Annual Reviews) over blog posts or press releases.

**Output format — present to the user as a verification table:**

| 声明 | 验证层 | 验证方式 | 验证源 | 结果 | 备注 |
|------|--------|----------|--------|------|------|
| 9个月成功率从35%→100% | Layer 1 | 回溯原文 | 预印本 Table 2 | ✓ | |
| 博睿康（公司名） | Layer 2 | 中文源核查 | 新华网报道 | ✓ | 英文论文中为Neuracle |
| "首个商业化获批的侵入式BCI" | Layer 3 | 知识库 + 联网 | 国家药监局 + Lancet Neurology 2024 | ⚠ | 应为"半侵入式"；Stentrode已获FDA突破性设备认定但未正式获批 |
| "大多数人体试验使用Utah阵列" | Layer 3 | 联网 | Annual Rev Biomed Eng 2025 综述 | ⚠ | 不够准确，ECoG和Stentrode试验数量在增长 |

Present this table immediately after the content draft, before inviting any discussion of wording.

**Handling ✗ and ⚠ — route by severity × whether the claim is load-bearing (does the insight depend on it?).** The governing rule: **a ⚠ is never silently promoted to an assertion.** It must be resolved, softened, dropped, or escalated.

| 核查结果 | 是否承重 | 处理 |
|---|---|---|
| **✗ 错**（数字/事实与源矛盾） | 非承重 | **就地改对**，标回 ✓，把改动指给用户看。Step 6 内小循环，不回退。 |
| **✗ 错** | **承重**（insight 依赖它，如 "<1 小时学会" 被证伪） | insight 不成立 → **退回 Step 4 重选角度**，不硬撑。 |
| **⚠ 查不到 / 源冲突** | 非承重（边角信息） | **软化成归因句式**（"论文报告 X" / "据报道"）或直接删除，继续。 |
| **⚠ 查不到 / 源冲突** | **承重**（就是 hook 本身） | 先**再挖一层**（回读页面/PDF 那一段、再找一个权威源）。仍定不了 → **明确上交用户**：压着不发 / 软化成保守说法 / 换一个能证实的角度，三选一由用户拍板。 |

Only after every ✗ and ⚠ is resolved (fixed in the draft, softened/dropped, or explicitly accepted by the user) does the flow move on to production (Step 7).

### Step 7: Production — 小红书 cards with figures（X thread 仅在用户当期要求时才出）

Run this **only after the fact-check gate (Step 6) is clear.** The copy was already drafted in Step 5 and verified in Step 6; Step 7 turns it into the **published form** — render the 小红书 cards. **默认成品只有小红书图卡**（见 Content Standards → Bilingual Content Workflow 顶部的写死条款）。(When a thread *is* requested, keep each language written independently from the shared outline — never translate one from the other. They share the outline and load-bearing facts, but the two media may differ in depth: thread = self-contained in text; 小红书 = deeper via figure+text.)

**English — X/Twitter thread（仅用户当期明确要求时才做）：**
- Hook tweet naming the core finding, then numbered 1/, 2/, 3/ … (typically 6-10 tweets)
- ~90% deep explanation of the core insight, ~10% understated closing comment
- **Respect X's 280-character per-tweet limit — every tweet (hook, each numbered tweet, and the reference tweet) must independently fit within 280 characters.** Count the characters of each tweet and split or trim anything over; never assume a long tweet will post. (A URL counts as ~23 chars on X regardless of length.)
- **End with a references tweet** (native English, subscript ¹ ² ³ style) and **include a link to the core/primary paper** (DOI or preprint URL). The reference tweet is **also** bound by 280 chars: keep each ref terse (Author Year · venue). If the primary-paper link + refs don't all fit, put the link + top refs in the last tweet and spill the remainder into one additional tweet rather than overflowing any single one.

**Chinese — 小红书 cards (with the figures grabbed in Step 3):**

Generate cards with the reusable script at `.claude/skills/dailybci/scripts/card_generator.py` (run from project root):
```python
import sys; sys.path.insert(0, ".claude/skills/dailybci/scripts")
from card_generator import CardGenerator
gen = CardGenerator(date="2026.06.07")
gen.cover_card("标题第一行", "标题第二行", "一句话核心发现。", "output/2026-06-07-slug/01-cover.png",
               source="2026年6月·bioRxiv 预印本《标题》。团队/机构,通讯作者 XXX(机构,一句为什么权威)。方法:一句话。")
gen.figure_card("papers/[slug]-fig1c.jpg", "Fig. 1c", ["如上图,红柱…(评注必须指认图里的元素)"], "output/2026-06-07-slug/02-figure.png")
gen.text_card("小标题", ["段落1...", "段落2..."], "output/2026-06-07-slug/03-text.png")
gen.tail_card(["¹ Ref 1...", "² Ref 2..."], "output/2026-06-07-slug/05-tail.png",
              lead_paragraphs=["这期的 10% 收尾评论…"])
# 尾卡里「参考文献」标题/列表绝不能排在收尾评论之上——那样很奇怪(用户 2026-06-19)。
# 收尾评论在上、参考文献在下。lead_paragraphs= 是实现方式之一,排版可灵活,守住这个先后即可。
```
Card sequence: 封面卡 → **目录卡（本期路线,强制,见下）** → 图卡（按内容需要,通常 2-5 张,用 Step 3 下到本地的论文原图/裁图 + 三段式中文评注）→ 文字卡（每张一个要点,字大留白）→ 尾卡（简评 + 参考来源,含核心论文链接）. 图卡数量服从逻辑链,别硬凑或硬砍。

**§封面 + 目录卡（所有小红书图文通用,日报与专题一律照办;2026-07-24 用户定「只要是小红书图卡就都要出目录卡」,2026-08-05 大改板式）:**

**⛔ 默认板式(2026-08-05 用户定,写死,以后每期照此出,不必再问):**

**封面 = 标题(两行) + 一句话核心句 + 一张概念图。三样,没有别的。**
- **来源/溯源信息一律不放封面**,移到目录卡(见下)。理由:封面与目录承担两种不同的注意力——封面要在读者滑动的半秒里换来一次点击,此时"通讯作者是谁、用了什么方法"帮不上忙;读者点进来后第一件想确认的才是"这是谁做的、靠不靠谱、要讲几步",那是目录卡的位置。
- **标题结构 = 方法 + 可感知结果,且必须让人一眼知道讲什么(2026-08-05 用户两次打回后定)。** 反面教材两个,都被点名"摸不到头脑":①「一个阴性结果的可信度/由它的对照设计决定」——三个抽象名词,读完不知道要看什么;②「三层对照/逐层剥掉干扰」——结构对了,但"干扰"没有主语,不知道是什么实验。**定稿「脑刺激有没有效/三层对照来判」**:前半给判断对象与领域,后半给方法。**判据:把标题遮住正文念给外人听,他应当能说出"这篇在讲什么领域的什么事"。**
- **标题字号必须放大到标题块约占封面 1/4(约 360px),由 `cover_card(..., title_size=...)` 传入**(2026-08-05 为此加了 `title_size` 参数)。默认 `SIZE_TITLE_LG=64` 太小,封面撑不住。**字数与字号的硬约束:内容宽 880px,每字宽约等于字号+1px 字距,所以 120px 时每行最多 7 字、124px 时最多 7 字(已顶到边)、112px 时 8 字。** 超了会折行,渲染完必须 `Read` 自检有没有折。字数放不下时优先改短标题,其次才降字号(降到 112px 标题块约占 22.6%,仍可接受;再低就失去大字效果)。
- **概念图是必须项,由 `cover_card(..., concept_image=..., concept_height=...)` 传入**(2026-08-05 为此在 `card_generator.py` 加了这两个参数与 `.conceptwrap` 样式)。
- **概念图的硬约束:它是"概念",不是示意图。** 绝不能是流程图、结构图、带框线和箭头的机制图——那些属于正文图卡。它要满足三条:① **半秒内被看懂**;② **与标题互相加强**,而不是把标题的字面意思再画一遍;③ **尽可能简洁**,少文字甚至零文字标签(标签会把它从概念图拖向示意图,解释留给正文卡)。
- **⚠️ 概念图最容易犯的错是"太抽象、看不出这篇讲什么"(2026-08-05 被打回一次)。** 第一版画的是"四条颜色不同的线汇成一条分不出成分的曲线",形式很干净,但用户的判断是**只表达了"混在一起"这个状态,没有本篇的内容**。**改法:让概念图直接画出这篇的主干动作。** 定稿版画的是「四条灰色干扰线 + 三道竖直关卡 + 一条蓝线穿过全部三道」——三道关卡对应三层对照,灰线在各自关卡处终止,蓝线通到底且出关后更粗。零文字,靠颜色与位置说话。**自检问法:遮住标题只看图,能不能说出这篇大致在讲什么?说不出就是太抽象。**
- 概念图同样用自制 SVG(`scripts/series/<slug>_figs.py`)产出,渲染成 PNG 后传给 `cover_card`。概念图的 SVG 背景色应设成与卡面一致的 `#FAFAFA`(而非默认白),否则卡上会出现一个突兀的白色方块。

**目录卡 = 强制的第 2 张卡,承担「路线 + 溯源」两件事:**
1. **本期路线**:自制 SVG 做成分行分点——每一步 = 序号(圆号) + 一句标题 + 一句灰色副标题,让读者一眼扫完本期要讲的 5-6 步。做法复用 `series/eeg_drift_figs.py` 的 `toc()`。
2. **来源区(2026-08-05 从封面移来)**:何时 · 什么平台/期刊 · 题为《…》的论文 · 团队/机构与通讯作者(值得说时加一句为什么权威) · 方法一句话。排在路线之下或之上均可,守住"同一张卡上读者能同时完成信任判断与导航"。
3. **这一张计入 18 卡上限**,出提纲数卡时就把它数进去。

**三者分工:封面给读者看(吸引点开)、发布标题给平台搜(见下 §发布标题+话题标签)、目录给导航与溯源。** 不要混在一张卡上硬塞。

**⛔ 最终交付固定是三件套,缺一不可(2026-08-04 用户定,写死)。** 渲染完图卡后,一次性交付下面三样,**每一样都做成可直接复制粘贴的形式**(标题/标签/摘要一律放进代码块,不要混在叙述里让用户自己摘):
1. **图卡定稿** —— 全部 PNG 经 `SendUserFile` 推给用户;
2. **小红书发布标题 + 话题标签建议** —— 见下方 §发布标题 + 话题标签(先采真实搜索词、再造句、再打分);
3. **微信公众平台摘要** —— 小红书与公众号是两个平台,文案形态不同,**不能拿小红书的标题或封面句顶替**。公众号的形态是「标题 + 下方一段摘要」,所以固定给两版:**(a) ≤120 字的摘要**(公众号摘要字段的官方上限,必须能整段塞进字段)、**(b) 约 200–300 字的正文开头导语**(可选,用户想放正文开头时用)。两版都守本技能的表达规则:科学平实、少修辞零拟人、承重数字带出处、不吹。

**⛔ 交付到「最终稿」为止,不要顺势去跑 Step 9(2026-08-04 用户定,写死)。** 三件套交付完就**停下来等用户确认稿子**。用户明确说「这稿没问题」之后,才进入 Step 9 收尾(知识库入库 / 清理 scratch / neat-freak / commit)。**理由:Step 9 会写知识库、删文件、提交 git,都是基于「这一版就是定稿」这个前提;稿子还可能改的时候跑它,产出的入库摘要与提交都要返工。** 记忆 `dailybci-step9-autonomous`(Step 9 内部 a→d 全自动、不逐项征询)仍然有效——它管的是**进入 Step 9 之后**怎么跑,不是**什么时候进入**。

**§发布标题 + 话题标签(所有小红书图文通用,日报与专题一律照办;2026-07-24 用户定「不仅专题,文献解读也都需要」)。渲染完全部图卡后自动做,产出「标题打分表 + 标签建议 + 推荐」,决定权交用户。**

**先分清两种标题:封面标题**(印卡上,给读者看、吸引点开)守既有规则=**简短肯定断言句**(见 Content Standards / 写作偏好);**发布标题**(小红书图文的文字标题,给平台搜索/推流)**以匹配真实搜索词为准,哪怕是疑问形式**(如"为什么脑电会漂"本身就是真实联想词)——它唯一目的是被搜到,此处不受"避免疑问句"约束。

**标题:先采词 → 再造句 → 再打分。**
1. **采词**:渲染完卡后围绕本期主题在小红书扫一轮,收集三类词汇成「本期可用搜索词池」,并标硬/软:① **平台联想词**("大家都在搜",最硬) ② **相关搜索词**(结果页底部) ③ **头部帖标题高频词**(前 10 条帖标题里反复出现的,软信号)。
2. **造句(硬规则)**:① **长度**——小红书标题约 20 字上限且信息流会截断,**核心搜索词必须放前 10 个字**;② **至少嵌一个联想词的原词,不改写**(改写就搜不到,如"基线漂移"别写成"信号乱跑");③ 给 **3-5 个候选**,覆盖不同策略(精准问题词=转化高 / 大流量词=曝光高 / 承接系列)。
3. **打分(每维 0-2,均可核实)**:命中联想词 / 搜索词覆盖广度 / 精准vs泛 / 与封面呼应 / 差异化。列成表,标各自侧重,给推荐,决定权交用户。

**话题标签:先采 → 再配 → 再说明。**
1. **采**:看本期主题下**头部帖实际在用哪些 #标签**、发布界面**推荐哪些标签**、每个标签的**体量**(标签页显示的浏览/参与数,粗读)。
2. **配比(混搭,别堆一堆)**:**大流量标签 2-3 个**(走曝光,如 #脑电 #脑机接口 #EEG) + **精准标签 2-3 个**(走转化,如 #基线漂移 #脑电帽 #科研日常) + **可选 1 个系列/品牌标签**(如 #DailyBCI,积累辨识)。
3. **说明**:每个标签标注属大流量还是精准、体量大概量级。

**诚实边界**:小红书不公开真实搜索量/标签浏览量的精确值,所以标题和标签的分数都是**可见代理信号(联想词命中、头部帖赞藏、标签页粗读体量)的估计**,最终建议标"基于当前可见信号的估计",不假装精确。这套机制随平台推流规则持续 fine-tune,当前是可迭代的第一版,非唯一正确答案。

**`tail_card` 参考文献超过约 4-5 条(取决于每条长度)会撑破 1440px 画布、跟签名叠字(2026-07-01 发现)。** 超过时拆成两张 `tail_card`——`lead_paragraphs`(收尾评论)只放第一张,第二张纯排剩余参考文献;渲染完照常逐张 `Read` 自检有没有溢出/叠字。方法论综述类选题(引用篇数多、常超 5 条)尤其容易踩到,出卡前默认检查一遍。

**【出卡前强制检查 · 正文就地标角标】(2026-06-24 写死,本次因漏标被点名):** 生成各卡正文时,**每一处承重数据/最高级/对比结论都要在该卡当场挂上标 ¹²³**(unicode 上标直接写进 `card_generator` 文字串,与 `**高亮**` 共存),并与尾卡参考列表一一对应——封面核心句、图卡评注里的数字、文字卡里的判断都不例外。**渲染完逐卡 `Read` 时,顺带核一遍"这张卡的承重点有没有角标"**;只在尾卡列编号、正文裸奔=不合格,要重渲染。完整规则见 Tone and Voice → 标注参考来源 第 1 条。

**渲染内核 = HTML/CSS 模板 + Chromium 截图**(经 `npx playwright screenshot`,需一次性 `npx playwright install chromium`;无 Chromium 则出不了图)。脚本自动处理中英混排(系统 Latin + 自带 Heiti SC)、自动换行、统一页眉页脚、上标(¹²³⁴ 由 Latin 字体原生渲染)。**句中高亮**:在任意文字串里用 `**关键词**` 包住关键术语/数字,即渲染成克制的学术蓝加粗(如 `样本为 **2 名** 参与者`);不加 `**` 的纯文字照常显示。克制使用——一张卡只点几个真正承重的数/词,别整句变蓝。

**Four hard rules for the cards (established by user review — apply them yourself, do not make the user re-request them each round):**

1. **封面必须交代"在解读哪一篇"——这是开篇身份。** Don't open with a colloquial method gloss ("用'让十个解码器投票'的办法"). The cover's `source` block must state, plainly: **何时 · 什么平台/期刊 · 题为《…》的论文 · 用什么方法**. If the authors/lab are notable, **add who & where + a one-line why-credible** (e.g. "通讯作者 Francis Willett,Stanford 神经假体实验室——2023 年 62 词/分语音 BCI 的一作"). The reader should know exactly what work they're reading an explanation *of* before anything else. The punchy "与我有关" hook still goes in the title lines; provenance goes in `source`.

2. **图卡裁到关键面板——清楚 > 全面,而且你自己先决策,别来回问。** A dense multi-panel paper figure shrunk whole makes every sub-panel unreadable. If **one** panel carries this card's insight, **crop the figure to that panel** before passing it in (PIL crop → `papers/[slug]-figNx.jpg`) so it renders large and legible. Decide crop-vs-keep-whole **up front, yourself**, at figure-prep time — making the user iterate "here's the figure → want me to crop? → ok now decide again" wastes their time. Only keep the full figure when the card genuinely needs multiple panels together. Helping the reader *see it clearly* always beats showing more.

3. **图文必须对版——评注要指认图里的东西.** The point of putting a figure on a card is that the text alone couldn't show it. So the annotation must **explicitly reference what's in the figure** — "如上图,红柱(完整集成)、紫柱(伪集成)都明显低于灰柱(基线)…" — not text that talks past the image. Figure and words describe the same thing; the figure is evidence the words point at, never decoration with self-contained text beside it.

4. **每张卡(图卡与纯文字卡同理)都是"结论开头 → 主体 → 转场"的三段式,卡与卡咬成一条逻辑链.** 整套卡不是孤立要点的堆叠。每张卡分三拍:**(1) 第一句直接给该卡的结论/承上**(接住上一张的转场);**(2) 中间主体**——图卡是"读图"(指认图里的线/形状/坐标/颜色,见规则 3,但不要纯描述像素),纯文字卡是把该结论讲透的展开;**(3) 最后一句收束并转场到下一张**("好,我们已经知道了 X,但接下来还需要 Y")。**这个三段式对纯文字卡一样强制**——文字卡也必须有承上的开头结论和引出下一张的转场,不能只甩一段孤立内容(2026-06-16 用户明确:文字卡曾漏掉首尾两拍,需补回)。把握"读图"的度:既部分解读了图,又把大逻辑串顺——不脱离图、也不就图论图。前一张的转场要接得住后一张的开头,让封面→各卡→尾卡顺成一条承前启后的链。这是 2026-06-15 用户定稿、2026-06-16 推广到全部卡的规矩。**（2026-06-20 用户再次强调并要求写死：承上开头 + 转出转场必须出现在每一张卡，且必须真正落到最终渲染的卡片文字里——草稿里写了三段式、渲染时却把首尾两拍删掉，是会被立刻发现的错误，禁止为省版面而砍掉转场。此"断言开头→细节主体→引出下一张"的逻辑与具体选题/论文无关，恒定不变，任何一期都照此办理。）** **（2026-07-13 写死：三段式是我给自己的结构提示，"（开头）/（主体）/（转场）/承上/结论/Q几"这类脚手架标签、以及给自己的卡片编号提示，绝不能出现在给用户的成品文案或渲染出的卡片里——按三段式组织内容，但呈现时只留自然流畅的正文。见记忆 `scaffolding-words-never-in-output`。同理，草稿里给自己标的"（Qn）"疑问映射、"图卡/文字卡"这类元信息，最终输出一律去掉。）**

**Present the thread text and the card images together** for review.

### Step 8: Dialogue, refinement, and final polish

Present both versions, then ask: "这是今天的内容。核心点找准了吗？图文搭配对吗？有没有哪里要调整？"

The user typically refines through 1-3 rounds. During dialogue:
- For related work / historical context → **look up the knowledge base** and cite specific milestone papers
- When the user questions whether something is truly novel → compare against knowledge base entries
- For more technical detail on a point → re-read the relevant section (browser page, or downloaded PDF)
- To change a figure or re-angle the insight → regenerate the affected cards

This dialogue is the core of the product. The user learns through conversation; the published content is a byproduct.

Once content is locked, produce the **final publishing-ready version**:
- **English thread** — each tweet clearly separated and numbered, copy-paste ready
- **Chinese cards** — re-generate at production quality: **mobile-optimized 1080×1440px**, text readable without zooming, higher-resolution figures if the draft figures were too rough (re-grab from the browser at larger size, or extract from PDF). Save to `output/[date]-[slug]/` as numbered PNGs (`01-cover.png`, `02-figure1.png`, … `06-tail.png`).
- **裁子图先用"留白投影"定位 panel 边界,不要肉眼猜像素坐标。** 反复目测 `crop()` 坐标既慢又总切不准(切掉时间序列右端、漏掉图例、把高出量程的误差棒截顶)。正确做法是让图自己告诉你边界:把整图转灰度→`ink = (pixels < 235)`→对**列**求和找出"基本无墨的列区间"(=左右 panel 之间的竖直留白沟),对**行**求和找出横向留白沟;panel 的真实包围盒就在相邻留白沟之间。多 panel 共用一行/一列时(如左列多子图紧贴、右列上方还压着别的 panel),要**只在目标列区间内**再投影一次行、或只在目标行区间内再投影一次列,才能把目标 panel 从邻居里分离干净。关键教训:**panel 的数据/坐标轴常比你以为的延伸得更远**(本期 Fig 2A 的时间序列一直画到 x≈1028,肉眼以为到 805 就完了,结果右端 1/4 被切),所以一定要用投影量出真实右/下边界,再加一点点统一边距。
- **裁图边界判据:"相关的全进、无关的全出"(2026-06-20 用户要求精进)。** 一张图的"相关内容"不只是数据区,而是**让这张图自洽所需的全部构件**:图例(legend)、子图标题(NSD/HUTH/…)、坐标轴+刻度标签、颜色条(colorbar)、显著性星号/方括号、单位。这些常**散落在数据墨迹主带之外**(图例浮在顶部、colorbar 在右侧、标题在上方),纯靠"投影找主带"会把它们漏在框外——本期 Figure 3 的图例上沿就是这么被切掉一线的。"无关内容"= 论文的**散文图注**(`Figure N: …` 那段)、邻图、页眉页脚,必须全部排除。
- **改进的裁图流程(按此顺序,别再只靠肉眼或单次投影):**
  1. 用投影(`ink=pixels<235`,行/列求和找留白沟)定出**数据区**包围盒;
  2. **向四周扩张**把所有 chrome 收进来——上(图例/标题)、下(x 轴刻度)、左(y 轴标签)、右(colorbar);判断"散文图注从哪行开始"用**全宽散文检测**(图注是整页宽的文本,数据/图例不是:找最左和最右同时有墨、且呈密集文本的行),把裁切下界设在它**之前**;
  3. 加一圈**统一小边距**(各边等宽),不要某边贴死、某边留一大片白;
  4. `Read` 裁出图**逐边自检**:图例完整?标题在?四角坐标轴和刻度齐?colorbar 全?星号没被截?散文图注没混进来?任一不满足就回到第 2 步调边界。
- **多轮重审、裁到干干净净为止——图的清晰好看很重要。** 即便用了投影定位,仍要**每裁一版就 `Read` 裁出的子图、再 `Read` 渲染后的卡**——只有看渲染后的卡才看得出残留和截断;一旦发现图不干净(邻 panel 杂块、缺轴、断线、图例被切、图注混入),就调整边界重裁、重渲染,**该几轮就几轮**,直到这张图只剩它自己、构件齐全、四边留白均匀。别把脏裁图发出去当最终版。
- **图卡黄金标准(2026-06-23 用户确认的成功案例,以后所有图卡一律照此办)= ①截干净 + ②图要大。** 这两条是图卡质量的硬指标:
  - **① 截干净(投影 + 逐版自检)**:用墨迹投影(灰度 `<235`、行/列求和找留白沟)量出真实包围盒再裁;**每裁一版必 `Read` 自检四边构件齐不齐**(图例 / 子图标题 / 坐标轴刻度 / 显著性 * / 单位全进,散文图注 / 邻图全出),不齐就调边界重裁,**确认无漏截、无错截之后才把图呈现给用户**——绝不把没自检过的裁图发出去。
  - **② 图在整张卡里要占大比例、放大看清**:图卡的价值就在图本身,别让它缩成一小条。三个反复踩的坑:(a) **论文图的实际内容常只占画面中央,四周是大片白边**——必须裁到"内容真实包围盒",把无意义白边全去掉(本期 Fig 1C 的环形任务流程只在中间约 1/3,裁掉空白后宽高比从 7.9:1 收到 2.25:1,在卡里放大约 3.5×、四步全清晰;Fig 5 把被切掉的顶部图例补回后含全部面板);(b) `figure_card(..., figure_height=…)` 默认 560,**宽-扁图可调大到 700–720** 给足竖向空间。判据:裁紧 → 宽高比更接近方形 → 在卡宽内铺满 → 读者一眼看清每个面板/标注。脏的、或缩成细条的图,都不算合格成品。
    - (c) **宽-扁的"多 panel 一字排开"图,必须重新拼版,不能整条塞进去(2026-06-24 用户强烈要求写死)。** 关键认知:`figure_card` 的图按"宽度铺满卡宽 + 高度上限=figure_height"渲染,所以**对一条 6:1 的横排图,把 figure_height 调大根本没用**——图是宽度受限的,高度恒等于"卡宽÷宽高比"(6:1 → 只有约 147px 高),再大的 figure_height 只是给它上下补白,图本身不会变大。**唯一解法是把每个子 panel 用投影干净切出来、重新拼成接近方形(目标宽高比≈卡的图区比例,约 1.2:1)的复合图**,这样宽度铺满时高度也铺满、每个 panel 才放得大。本期 Fig 3 E–G 原是 6 个子图一字排开(6:1、塞进去每格仅约 147px、还截到邻图),改成 **3 列(20/40/60 µA)×2 行(气泡最大时刻 / 刺激后渗漏)** 的网格(≈1.5:1)后,每格放大到约 285px、四角干净;K/L/M 也从一字排开收紧成紧贴的一行(去掉 panel 间大白沟),panel 尺寸翻倍。**做法**:对原图做列/行亮度投影(2P 黑底图用"找白色留白沟 `亮度>240`"分割,比找墨迹更准)定位每个子 panel 的真实边界 → 各自 `crop` → `PIL` 贴到白底画布上重排 → `Read` 复合图逐格自检(无邻图杂块、标签/坐标/图例齐)。重排只是把论文自己的子图重新平铺,不改像素、不算篡改;但要保留可追溯的标签(µA / panel 字母 / 图例)。
    - **首选用 `scripts/figcrop.py`,别再手填裁切坐标(2026-06-24 新增,起因:手填 x 把 K 截掉一截)。** 关键教训:**手敲坐标=凭眼估=必然截到或截掉**;让图自己报边界更快更准。该 helper 的 `figure_box(gray, y_band=(Y0,Y1))` 自动做三件事——① **裁掉页边距**(干掉 bioRxiv 侧栏水印),② **切在散文图注之上**(用行留白沟找 panel 块/图注分界),③ 用"内容包围盒(任何 `gray<235` 的非白像素,含 panel 字母/图例/colorbar/黑底 2P 图)"框出真实边界。`split_panels(gray, box)` 再按白沟切分,**每个 panel 扩到相邻留白沟的中线(绝不在沟内缘切)**,所以不会截掉字母/图例。用法:`fitz` 把页面 `get_pixmap(dpi=300)` 存 PNG → `figure_box` 拿框 → `crop` → `Read` 逐边自检 → 要拼版就 `split_panels`(注意它会把 panel 字母切成单独一格,拼版时与其图归并)。Y0/Y1 从全文里 `Figure N.` 那行的位置估个**宽松**区间即可,精确边界交给 `figure_box`。

**The "最终版 / final version" is always the actually-rendered cards, shown inline — never text-only copy.** When the user asks for the final/最终版, that means: run `card_generator.py`, produce the PNGs (figure cards composited with the real paper images), and **display the rendered card images in chat so the user can browse the actual 图卡** — image and text together as they will publish. Do not stop at a text description of the cards and make the user imagine the layout. Rough text copy belongs to the *draft* stage (Steps 5/7); the final stage owes the user browsable cards. The only exception is a headless run with no way to surface images — then say so explicitly.

**"最终版"= 图卡 + 另外两样,不是只有图卡(2026-08-04 补,防漏)。** 上一段只讲了"图卡必须真渲染出来",但**渲染好的图卡只是三件套的第一件**。最终稿必须同时交付:**① 图卡定稿 ② 小红书发布标题 + 话题标签建议(须先在小红书实采联想词/相关搜索词/头部帖标签,再造句打分,不许凭空拟) ③ 微信公众平台摘要(≤120 字字段版 + 200–300 字导语版)**,三样都放进代码块供直接复制。完整操作手册见 **Step 7 的「⛔ 最终交付固定是三件套」与「§发布标题 + 话题标签」两节**——只读本 Step 会漏掉后两样。

Present all final cards for last confirmation before posting. **交付完三件套即停,等用户明确确认稿子后才进 Step 9**(见 Step 7 顶部写死条款与 Step 9 进入条件)。

**发布后花絮 / 彩蛋留言选项(最终版锁定后,随成品一起给出)** — 每期最终版(图卡 + thread)定稿后,除了成品,再附 **2–3 条可直接复制粘贴的「彩蛋留言」**,供用户以「小邹」第一人称贴到小红书评论区,给硬核内容加一点「活人感」。要求:
- **口吻**:低姿态、自黑、俏皮但真诚;给读者一点优越感(「能读到这儿已经很厉害」),绝不居高临下。口语化可以、口水化不行,少用比喻(仍守 avoid-metaphor 全局规则)。
- **内容必须是这一期真实的制作花絮**,不是空泛的「做得好辛苦」。取材于本期实际发生的具体波折:数字重算了几遍、哪一版翻车(如自注意力权重糊成一团、学习率过冲)、被砍掉的某个比喻、反复卡壳的理解点、标题改了几版、某张卡溢出重排……**越具体越可信,也正好让读者感到「这么费劲才做出来」**。
- **长度**:评论区体量,每条几句话;给 2–3 个不同侧重(如「边学边做」/「代码翻车自黑」/「给读者台阶」)供挑选。
- 这是**可选的附加交付**:用户想用就复制,不用也不影响成品。(2026-07-22 用户定:每期定稿后固定给几条彩蛋留言选项,取材真实花絮、给读者优越感。)

### Step 9: Close out(**用户对最终稿明确确认之后**才启动,启动后一次性走完)

> **进入条件(2026-08-04 写死):** Step 8 交付「三件套」(图卡定稿 + 标题标签 + 公众号摘要)后**停下**,等用户给出「这稿没问题」之类的明确确认。**没拿到确认就不许进 Step 9。** 详见 Step 7 顶部的两条写死条款。

**这是一个单一的收尾步骤,不是四个独立环节**——用户在 Step 8 给出最终确认后,以下 a→d 顺序执行、中途不再逐项停下来问,除非某一步本身要求用户表态(知识库入库的判断、删除前的确认):

**a. 知识库更新** — 评估今天这篇是否够格进知识库(是否milestone、还是只是确证性/补充性条目)。给出你的判断和理由,问用户"今天这篇关于 [topic] 的工作值得加入知识库吗?"。用户确认要加 → 按 Mode B 格式生成结构化摘要,写入 `knowledge-base/papers/[subfield]/`,更新 `INDEX.md`(含子领域计数、总篇数)。

**b. 清理本地 scratch** — `papers/` 里这一期的工作文件(下载原图、裁图、全文PDF/txt)已经用不上了,图已烤进 `output/<date>-<slug>/` 的成品卡。给用户一个带清单+大小的提示:
> 今天这期发完了。`papers/` 下这期的工作文件(下载原图 N 张、裁图 M 张、PDF/全文 ≈ X MB)已经用不上了——成品卡在 `output/<slug>/`、图已烤进卡。要我清掉吗?

用户同意 → `rm` 掉这一期的 `papers/<slug>*`。**绝不碰 `output/`(成品)、`.claude/`(技能/知识库)、或别期的工作文件**,删前再扫一眼清单确认范围。删除不可逆,必须用户明确同意才删。

**c. 跑 `/neat-freak`** — 审查这期会话有没有让 `CLAUDE.md`、本 `SKILL.md`、知识库 `INDEX.md`、记忆系统之间出现漂移(常见的:知识库加了条目但 `INDEX.md` 的子领域/总篇数计数没跟着改;某篇论文改名/改年份后,`CLAUDE.md` 里旧的引用没同步)。发现漂移就地修正。

**d. `git commit`**(单人项目,默认直接 commit + push master,不开 PR,见 §5)——把 a-c 的全部产出(知识库新条目、`INDEX.md` 更新、`output/<date>-<slug>/` 卡片、neat-freak 修正的文档)一并提交、推送。

无头运行(cron/`claude -p`)不自动做 b 的删除,但涉及 push 的动作仍遵循"先在聊天里说明、拿到确认"的默认规则,不要在无人值守时静默推送。

---

## Mode C: 专题深度长文 (Series Deep-Dive)

Trigger: "做一个专题", "深度长文", "把 X 讲透", 或任何脱离单篇日报、要从第一性原理把某个原理/技术/硬件讲穿的常青长文需求。

专题与日报(Mode A)是**两条不同的 pipeline**:日报绑当天单篇论文、走 10 步关卡;专题不绑单篇、可跨多期、原理驱动。成品进 `output/series-<slug>/`,出图复用 `card_generator.py` + 自制 SVG 示意图(见记忆 `dailybci-series-deep-dive-track`)。已出:犹他阵列、电极材料、神经解码方法论、侵入式定位精度、**EEG 工频/阻抗均衡(series-eeg-impedance-01)**、**EEG 电极界面/基线漂移(series-eeg-impedance-02)**。

专题的写作/讲解节奏沿用全局规则:**背景先行 + 一次一小块**(见 Content Standards 同名节)、用户随时可喊停内容生产转纯讲解(记忆 `user-stepwise-tech-tutorials`)、科学平实少修辞。以下是专题**特有**的三道关卡。

### C-1. 选题关卡:三方交汇,小红书需求权重最高 (2026-07-24 用户定)

**每一期专题(乃至日报)的选题,都必须是三个来源的交汇,不能只靠其中一个:**
1. **① 用户的兴趣** —— 圈定大方向(如"想搞懂 EEG 硬件")。
2. **② 主题/文献本身的核心 insight** —— 有没有扎实的第一性原理能讲透、差异化空位在哪(你对"这东西好在哪/值得讲在哪"的判断)。
3. **③ 小红书上的真实需求** —— **权重最高、top priority**。到底大家有什么痛点、对什么还不清楚。

**两个方向的先后不同,别搞反:**
- **日报**:文献先行(②)→ 给出几个候选 insight → 与小红书兴趣做 **overlap 交汇** → 选交汇最强的一条。③ 在此是**校验+排序**。
- **专题**:用户兴趣先行(①)→ **先用 ③ 反向锁定切入点**(如"EEG 硬件"这个方向里,小红书上"为什么脑电会漂"是真实高频且没被讲清的)→ 再回到 ② 找支撑原理。**③ 是专题选题的起点,不是终点。** (起因:series-01 从"阻抗全绿还满屏工频"这个真实困惑反推、series-02 从"为什么脑电会漂"反推,都是 ③ 起点。)

#### 小红书需求怎么判定:两轴分开,不加总

一个好选题 = **需求强(A 轴) 且 供给空位大(B 轴)**。这是**两个独立的轴,分别打分、都过线才入选,绝不揉成一个总分**——否则"需求强但已被讲烂"(如降阻抗妙招)会和"需求中等但没人讲透"(如漂移原理)被算成一样,选错。

**A 轴 · 需求强度**(每个信号先归到这轴):

| 信号 | 能否量化 | 可靠性 | 坑 |
|---|---|---|---|
| 平台联想词("大家都在搜"里出现) | 二元可读 | **高** | 最硬的需求信号,几乎无坑 |
| 相关搜索词 | 可读 | 高 | 同上 |
| **收藏数** | 列表可见 | **高**(科普/教程尤其) | 收藏=想反复看=真实用性,比点赞硬 |
| **留言数** | 需点进帖 | **中高** | 留言=同问题的人在聚集,真需求;争议话题会虚高 |
| 点赞数 | 列表可见 | **中** | **求助帖天生低赞**,不能单看(series-01 差点被误导) |
| 高情绪 why 帖存在("为什么…啊啊啊") | 定性 | 中 | 证明真困惑非伪需求;仅作佐证 |

**B 轴 · 供给空位**:

| 信号 | 能否量化 | 可靠性 | 坑 |
|---|---|---|---|
| 现有头部帖的内容层次(妙招/软文 vs 讲透原理) | 定性 | 中高 | 需人工读,判断有没有到原理层 |
| 厂商软文占比 | 定性 | 中 | 软文多=真空位(只卖货不讲原理) |
| 同名精准内容数量 | 粗估 | 中 | 少=空位大 |

**权重初稿(可迭代,不追求当前唯一正确):**
- A 轴:联想词 30% · 收藏 25% · 留言 25% · 点赞 10% · 高情绪帖 10%
- B 轴:现有内容层次 50% · 软文占比 25% · 同名数量 25%
- **过线规则:A、B 两轴各自算分,都达标才入选(不加总)。**

**诚实边界(硬约束):小红书不公开真实搜索量/浏览量。** 所以 A 轴永远是**代理指标的组合估计,不是真值**。收藏/留言/联想词是能拿到的最好代理,但没有一个等于搜索量。**加权时让硬信号(联想词、收藏、留言)权重高,但最终分必须标成"估计",绝不包装成精确真值**——这与全局准确性要求一致。这套打分是**多信号半定量**,不是伪精确评分。

**这三方交汇的调研本身也遵守"从真实需求出发、不凭空构想痛点"**:痛点必须来自小红书/知乎/reddit 上大家的真实吐槽和留言,绝不能是从原理倒推的"应该会痛"(series-01 起因:我曾编了五个痛点,被用户要求逐条去平台核实,结果发现最痛的那个我漏了、编的几个是伪需求)。

### C-2. 封面关卡:极简封面 + 目录卡 (2026-07-24 用户定)

小红书封面**至关重要**——它同时承担"吸引点进来读"和"导航本期讲什么"两个任务。规范:

1. **封面极简、排版清晰**:只放标题(两行) + 一句话核心句 + 极淡的来源/日期。**绝不把大段文字/目录堆叠在封面上不分行不分段**——那对阅读极不友好。哪怕字少也要清晰。
2. **目录卡是所有小红书图文的通用规范,不限专题**——见 Step 7 的「§封面 + 目录卡(所有小红书图文通用)」;专题与日报都必须出。
3. 封面 + 目录的分工:**封面给读者看(吸引读)**,标题给平台搜(见 C-3),目录给导航(知道要讲什么)。三者各司其职,不要混在一张卡上硬塞。

### C-3. 发布元数据关卡:标题候选 + 话题标签候选 + 半定量打分

**这一关卡是所有小红书图文的通用规范,不限专题——完整操作手册(采词→造句→打分、标签采配、封面标题 vs 发布标题、诚实边界)见 Step 7 的「§发布标题 + 话题标签(所有小红书图文通用)」。** 专题与日报一律照办:渲染完全部图卡后自动做,产出标题打分表 + 标签建议 + 推荐,决定权交用户。

---

## Mode B: Knowledge Base Construction

Trigger: "建知识库", "add to knowledge base", "搜索 [subfield] 的综述", or any request to build/maintain the milestone paper library.

### Knowledge base structure

```
knowledge-base/
├── INDEX.md                    # Master index: all papers listed by sub-field
└── papers/
    ├── speech-decoding/
    │   ├── willett-2023-speech-neuroprosthesis.md
    │   ├── chang-2021-neuroprosthesis-speech.md
    │   └── ...
    ├── motor-bci/
    │   └── ...
    ├── electrode-hardware/
    │   └── ...
    ├── signal-processing/
    │   └── ...
    └── [other sub-fields]/
```

### Sub-field taxonomy

Use these categories (expandable as needed):

- `speech-decoding` — speech neuroprostheses, language decoding, phoneme/word decoding
- `motor-bci` — hand/arm motor control, cursor control, robotic arm
- `locomotion` — walking, leg movement, spinal cord stimulation for mobility
- `electrode-hardware` — electrode arrays, materials, implant design, wireless systems
- `signal-processing` — decoding algorithms, neural signal analysis, feature extraction
- `non-invasive` — EEG-based BCI, fNIRS, sub-scalp EEG
- `invasive-recording` — intracortical, ECoG, epidural, depth electrodes
- `sensory-feedback` — somatosensory stimulation, closed-loop haptic feedback
- `neuromodulation` — DBS, cortical stimulation, therapeutic neural modulation
- `clinical-regulatory` — clinical trials, FDA approvals, long-term patient outcomes
- `rehabilitation` — neuroplasticity, spinal cord repair, BCI-assisted recovery
- `ai-neural-modeling` — foundation models for neural data, transfer learning, self-supervised methods

### Paper summary format

Each milestone paper is one markdown file:

```yaml
---
title: "Full paper title"
authors: Last, Last, Last et al.
year: 2023
venue: Nature / Nature Electronics / NEJM / arXiv / etc.
url: https://doi.org/...  # or preprint link
subfield: speech-decoding
tags: [speech-BCI, RNN, phoneme, high-density-array]
---

## 解决了什么问题
[2-3 sentences: what gap or limitation in the field did this work address?]

## 核心方法
[3-5 sentences: what was the key technical approach? What made it different from prior work?]

## 关键数据
[Bullet points: the most important quantitative results, before/after comparisons]

## 为什么是 milestone
[2-3 sentences: why does this paper matter for the field's trajectory? What did it change or enable?]
```

### Building the knowledge base: workflow

When the user asks to build or expand the knowledge base:

> **硬约束：禁止直接从训练知识列论文清单。** 必须先找到至少一篇该子领域的综述文章，从其引用中提取 milestone 候选。训练知识和 web search 可以用来*补充*综述遗漏的近期工作，但不能替代综述作为主要选择依据。

1. **Ask which sub-field to start with**, or suggest one based on what's missing from INDEX.md.

2. **Search for authoritative review papers** in that sub-field:
   - Search: "[subfield] review brain-computer interface" on Google Scholar, PubMed, Nature Reviews
   - Look for reviews from the past 3-5 years with high citation counts
   - Prioritize reviews from recognized groups (e.g., Shenoy lab, Chang lab, Schwartz lab, Wolpaw, Birbaumer)

3. **Extract milestone papers from the review's references:**
   - Read the review paper (via web_fetch)
   - Identify papers that the review highlights as turning points, breakthroughs, or foundational work
   - Typically 5-15 milestone papers per sub-field

4. **For each milestone paper, generate a structured summary:**
   - Fetch the paper's abstract and key details via its URL
   - Fill in the summary template above
   - If the full paper is accessible, read the methods section for more precise technical details

5. **Present the batch to the user for approval:**
   - Show the list of papers with one-line descriptions
   - User confirms which ones to include, suggests additions or removals
   - Write approved entries to `knowledge-base/papers/[subfield]/`
   - Update `INDEX.md`

6. **Repeat for the next sub-field.**

### INDEX.md format

```markdown
# DailyBCI Knowledge Base

Last updated: [date]
Total papers: [count]

## speech-decoding (N papers)
- [Willett 2023](papers/speech-decoding/willett-2023-speech-neuroprosthesis.md) — Phoneme-level decoding, 125k vocabulary, 9.8% WER
- [Chang 2021](papers/speech-decoding/chang-2021-neuroprosthesis-speech.md) — First real-time speech BCI from ECoG, 50-word vocabulary
- ...

## motor-bci (N papers)
- ...

## electrode-hardware (N papers)
- ...
```

---

## Tone and Voice

- **学者科普风** — 像 Andrej Karpathy 写博客：技术人自己写的，有深度但不端着，偶尔有自己的判断但不说教。关键是"这个人自己也在思考"的感觉，而非"我在给你发布一条新闻"。
- **Technically precise** — actual method names, metrics, numbers, comparisons to prior work
- **Never press-release** — no "groundbreaking", no "scientists are excited", no "gives hope to millions"
- **Never exhaustive** — find THE insight, not list every contribution
- **Honest about uncertainty** — "the paper reports X; if this replicates, it would mean Y" is good
- **标注参考来源（硬规则，从文章生成内容、引用他篇时一律遵守）**

  > **⚖️ 参考文献三条铁律（2026-06-29 用户定为"铁的纪律，任何产出都要服从"）—— 出任何稿（小红书卡片 / X thread / 知识库）前，必须逐条过这三关：**
  > 1. **一致**：正文里出现的每个角标，必须和尾部 Reference 列表**一一对应、完全一致**——¹ 对 ¹、² 对 ²、³ 对 ³。不留孤儿引用（列表里有、正文没标），不留未标记的承重数据（正文有承重点、却没角标）。
  > 2. **顺序**：正文角标与尾部列表都**按正文首次出现顺序编号**——正文里最先出现的引用是 ¹，下一处新引用是 ²，依次递增；尾部列表同序。**绝不跳号**（不能读到第 2 张卡却是 ³）。出稿前从头扫一遍角标序列，确认 ¹→²→³… 单调不跳。
  > 3. **统一格式**：所有条目套**同一个标准模板** `作者. (年份). 题名. 期刊/平台 卷:页码.`，不夹带任何解释性文字、不中英混排、不各写各的（详见下方第 2 条模板与硬禁止）。
  >
  > 这三条是铁律，宁可多花一遍自检也不许违反。下面四条是它们的展开与操作细则。

  四条展开（缺一不可）：
  1. **正文就地标角标（最易漏，务必落到渲染出的卡片文字里；2026-06-24 用户因这次漏标而要求写死）**：每一处关键数据/最高级/对比结论,在它**出现的那张卡/那条 tweet 当场**挂上上标角标 ¹ ² ³（不能只在尾部列、正文不标）。具体到小红书:**封面的核心发现句、每张图卡评注里的承重数字（如 60 µA、约二次方）、文字卡里的承重论断（如 Shannon/McCreery 判据、铂 vs 金退化）都要在该卡正文当场带 ¹²³**,与尾卡参考列表一一对应;`card_generator` 的正文串里直接写 unicode 上标 ¹²³⁴(由 Latin 字体原生渲染,和句中 `**高亮**` 可共存)。**只在尾卡列编号、正文裸奔=不合格**,出卡前逐卡核一遍每个承重点是否都挂了角标。
  2. **尾部统一汇总且格式一致（标准参考文献格式，2026-06-29 用户要求固化、严格执行）**：小红书在尾卡、X thread 在末尾 tweet(refs 超长就拆成多条,每条仍 ≤280 字符)汇总全部参考。**所有条目严格套同一个标准模板,不得夹带任何解释性文字**：
     - **唯一模板**：`作者. (年份). 题名. 期刊/平台 卷:页码.`
       - **作者**：姓 + 首字母（如 `Mesgarani N, Chang EF`）；≥3 位作者用 `一作姓 名首字母, et al.`（如 `Ismail T, et al.`）。
       - **预印本**：`作者. (年份). 题名. bioRxiv/medRxiv <DOI 或编号>.`（如 `Ismail T, et al. (2026). Estimation of neuronal tuning for word meaning from passively recorded naturalistic speech. bioRxiv 2026.06.23.733980.`）。
       - **期刊**：`作者. (年份). 题名. 期刊 卷:页码.`（如 `Mesgarani N, Chang EF. (2012). Selective cortical representation of attended speaker in multi-talker speech perception. Nature 485:233–236.`）。
     - **硬禁止**（这次被点名的"乱七八糟"）：① 条目里**不准**塞 `(527万词/871h…均出自此文)` 这类承重点说明——承重点靠正文角标对应,参考列表只放干净引用；② 不准英文 author-year 与中文描述式标签混排；③ 不准 DOI/PMCID/期刊缩写各写各的；④ 题名要么全给、要么统一省略,不要有的给有的不给。
     - **X thread 的 refs tweet** 受 280 字符限,可把题名压掉、只留 `作者 (年份). 期刊 卷:页码.`,但**三条之间仍须同一压缩规则**,不要一条带题名一条不带。
  3. **每个角标都要有对应正文出处、每条正文引用都要进尾部列表**（不留"孤儿引用",不留"未标记的承重数据"）。**角标按正文首次出现顺序编号（2026-06-29 用户指出乱序）**：把全部卡片/推文按阅读顺序走一遍,正文里**最先**出现的引用是 ¹,下一处**新**引用是 ²,依此递增;同一条引用后续再出现时沿用同一编号。尾部参考列表也**按这个顺序**排列。绝不能出现"读到第 2 张卡却标 ³、第 5 张才出现 ²"这种跳号。出卡前从头到尾扫一遍角标序列,确认是 ¹→²→³… 单调不跳。**非同行评议的史实/监管/商业事实**（公司沿革、FDA 记录、新闻）与学术论文**分层标注**,单列一行说明来源层级,不要混进学术引用里冒充论文。
  4. **参考文献本身要准确**：作者、年份、期刊要查实(必要时查 PubMed/期刊页),不要凭记忆写错刊名或年份。（2026-06-21 用户定稿:参考文献的"就地标注 + 尾部统一格式 + 本身准确"是本 schema 的通用要求。）
- **收尾的局限性段落用"局限性/本研究的局限性"措辞，不要写"诚实边界"等生造说法**（2026-06-29 用户指出："诚实边界"表述本身有问题，改"局限性"更自然）。
- **不要把"预印本 / 未经同行评审"当作一条局限性来写（2026-06-30 用户定，写死）。** 本日报绝大多数选题本就基于预印本，"这是预印本、尚未同行评议"是废话、几乎不携带信息量——**正文、文字卡、尾卡一律不再把它列为 limitation**。溯源需要时，参考文献里如实写明发表平台（venue）即可（如 `Nature Neuroscience` vs `Meta AI` / `bioRxiv`），这是中性的出处标注，不是局限性陈述。预印本与正刊可能有数字微调的核对要求仍照旧（见 §正刊优先 第 2 条，那是 Step 6 内部动作，不写进成品文案）。
- **避免"不是...而是..."句式** — 中文写作中不要使用"不是 X，而是 Y"这种对立表达。改用直接陈述：直接说 Y 是什么，如果需要对比，用"相比 X，Y 更..."或直接并列呈现让读者自己判断。
- **中文里指代论文子图用"图 A / 图 D"，不要说"面板 A / 面板 D"** —— "面板(panel)"是英文 figure panel 的直译，在中文语境里很生硬。卡片评注、对话讲解里一律说"图 A""图 2D""上图左"等自然说法。（2026-06-16 用户指出）
- **中文里 spike 一律写"动作电位"，不要用"脉冲"或直接写"spike"** —— 中文神经科学语境下"动作电位"更标准、更对味；"脉冲"偏工程信号味。spike train → 动作电位序列。（2026-06-18 用户指出）

## Visual Design (小红书卡片)

**排版风格：学术简洁。** 类似 Nature Briefing 的克制感——大量留白、无装饰、纯靠字号和灰度层级建立信息结构。

- 背景：纯白或极浅灰（#FAFAFA）
- 无色块、无渐变、无图标装饰
- 信息层级靠字号（正文层级 64/56/34/24px）和灰度（#1A1A1A → #666666 → #BBBBBB）区分。**例外:封面标题另算**——它要放大到标题块约占封面 1/4(约 120px,见 Step 7 §封面 + 目录卡的 `title_size` 一条),不受这里 64px 的层级约束。
- 边距慷慨（100px+），内容不要贴边
- 封面卡只放：标题（放大）+ 一句话核心发现 + **一张概念图** + 品牌/日期（极淡）。**来源/溯源放目录卡,不放封面**（2026-08-05 定,见 Step 7）
- 详细数据、引用、分析留给后续卡片

**署名：**
- X thread 署名：`xiaozou × Claude`
- 小红书署名：`小邹 × Claude`
- 署名位置：尾卡底部，小字

## Content Depth Principle (核心原则)

**1-2 个点讲透，胜过 5 个点蜻蜓点水。** This is the single most important content quality rule.

**首先判断这篇论文最独特的点在哪个维度。** 核心 insight 不局限于技术细节——它可以是任何维度：

- 临床结果（患者具体做到了什么、康复到什么程度）
- 实验设计的巧妙之处（为什么这个实验能回答别人回答不了的问题）
- 技术路线的创新（和主流方法有什么根本性不同）
- 关键数字的跃迁（一个指标的大幅突破及其意义）
- 违反预期的发现（领域以为 A，结果发现 B）
- 监管或政策突破（为什么这个审批/许可本身就是里程碑）
- 团队或合作模式的独特性（为什么这个组合能做到别人做不到的事）

**判断在先，展开在后。** 确定了核心维度之后，在那个维度上讲深讲透：

- **讲具体**：不要说"帮助患者康复"，要说"患者在训练 13 周后能用机械臂自己拿起杯子喝咖啡，成功率从第一周的 30% 提升到 92%"
- **讲机制**：不要只说"用了新算法"，要说这个算法具体改变了什么——是更新了什么模型？利用了什么之前被忽略的信号特征？
- **讲对比**：引用知识库中的前代工作，用具体数字说明差距——"之前最好的结果是 X（某某, 2021），这篇做到了 Y，提升了 Z%"
- **讲意义**：这个具体的改进为什么对患者/对领域有实际影响？

核心维度之外的其他信息只作为背景一笔带过（1-2 句），绝不展开。如果一段文字删掉后不影响读者理解核心 insight，就应该删掉。

## What NOT to Do

- Don't list every finding — find the one that matters most and explain it thoroughly
- Don't scatter across multiple technical dimensions (algorithm + signal processing + clinical translation + regulatory) — pick ONE angle and go deep
- Don't write generic summaries that could describe any paper in the field
- Don't use "首次" or "first ever" unless it genuinely is, verified against the knowledge base
- Don't start Chinese titles with emoji-heavy clickbait ("震惊！重大突破！")
- Don't add motivational commentary — let the science speak
- Don't fabricate details — say "the paper reports X" rather than asserting X as fact
- Don't generate content without reading the actual source material
- Don't make importance judgments without consulting the knowledge base (when available)
- Don't proceed past Step 2 without user confirmation of the topic choice
- Don't omit species information when citing animal or human studies
- Don't translate company/institution names from English — look up their official Chinese names (e.g., Neuracle → 博睿康)
- Don't translate one language version from the other — write each independently from the shared outline
- Don't use paper-internal validation metrics (F1, ARAT, ERSP) when a concrete functional outcome can convey the same point
- Don't use universal quantifiers ("all", "every", "都", "no other", "首次") without exhaustive verification against the knowledge base
