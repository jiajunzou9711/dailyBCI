---
name: dailybci
description: >
  Daily BCI (brain-computer interface) academic digest with two modes:
  (1) Daily digest mode — find the most important recent BCI paper, identify its core technical insight using the
  knowledge base for context, and produce a deep explanation in English (X thread) and Chinese (小红书 post).
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

2. **Every quantitative claim must trace back to the original paper.** Do not paraphrase from memory or round loosely. If you write "100% success rate within 10 seconds," be ready to point to the exact figure, table, or sentence in the source. If you cannot verify a number, say "the paper reports X" rather than asserting X as fact.

3. **Avoid universal claims unless individually verified.** Words like "all", "every", "no other", "the first ever", and "都" are strong assertions that require exhaustive checking. Prefer bounded language: "the main prior approaches included…" instead of "all previous work relied on…"; "among the earliest" instead of "the first." Use "首次" or "first" only when verified against the knowledge base.

4. **Fact verification step.** After completing a draft, run the three-layer verification defined in Step 6 (trace back to source → cross-source check → assertion audit with knowledge base + web search). Present the verification table to the user before any discussion of wording. Facts must be confirmed before polish begins. See Step 6 for the full procedure.

### Technical Term Usage

Terms fall into two tiers:

- **Core technical terms** — terms that define this work's identity and cannot be simplified without losing meaning (e.g., "硬脑膜外/epidural," "Utah阵列," "体感诱发电位/somatosensory evoked potentials"). These MUST appear, with sufficient context for a non-specialist to understand them. A good test: could the reader explain this term to a friend after reading your sentence?

- **Paper-internal validation metrics** — metrics the authors use to prove their claims but that carry no intuitive meaning for the reader (e.g., F1 score, ARAT score, ERSP). Replace these with functional outcomes wherever possible: "the patient wrote his own name" instead of "ARAT score improved by 16 points." If a validation metric is genuinely the most important piece of evidence and cannot be replaced, keep it — but explain what it measures and why that number matters.

### Expression Style

- **No hype, no clickbait.** Never use "出人意料", "颠覆", "震惊", "重大突破", "groundbreaking", "gives hope to millions." Let the technical facts carry their own weight. If the result is genuinely surprising, the reader will feel it without being told.
- **No motivational commentary.** Don't editorialize about how this will "change lives" or "open new doors." The 10% comment at the end should be a concrete observation — what open question this raises, what would need to happen next — not a grand narrative.
- **Understated confidence.** "The paper reports X; if this holds across more patients, it would suggest Y" is better than "X proves Y."
- **Prefer concrete scenarios over abstract scores.** "患者写出了自己的名字" > "ARAT评分提高16分". Functional outcomes that a reader can visualize are more powerful and more honest than context-free numbers.

### Bilingual Content Workflow

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
2. **用 `Read` 工具读这个文件** —— Read 会把图渲染进用户对话框,这就是内联呈现。**确认这一步真的执行了,而不是只在文字里描述图。**

**裁子图(只想给某个 panel):** PIL `Image.crop()` 存成新文件 → 同样 `Read` 渲染。原尺寸直接读即可,不要为体积纠结。

**不要做的事:** 不要把图转成 base64 塞进 `show_widget`/HTML widget —— 又慢又吃 token,且不是必要的;`Read` 渲染本身就能让用户在对话框看到图。也不要靠浏览器 `screenshot` 当作"贴给用户看"的手段(那种截图进的是模型上下文,用户界面里不一定可见)。**结论:存盘 + Read,别绕路。**

适用全流程,典型两处:
- **源图(Step 4):** 呈现 insight 时,贴出打算用的那 1-3 张论文原图(或其中关键 panel 的裁图)。
- **成品卡(Step 7/8):** "最终版"是真正渲染出来、内联展示的图卡(`card_generator.py` 产出 PNG 后用 Read 贴进对话),不是纯文字 copy。

**抓图/裁图费劲不构成跳过的理由**——已知坑(懒加载占位符、URL 路径、内容过滤)见 Step 3,换方法继续直到图真的出现在对话里。**唯一例外**是确无浏览器、无法把图贴进对话的无头运行(cron/`claude -p`):那种情况要明确告诉用户"本次无法贴图、只能文字描述",而不是默默跳过。

---

## Project layout & paths (Claude Code)

This skill runs as a Claude Code project. Anchor all paths to these locations (working directory = project root):

- **Skill + resources:** `.claude/skills/dailybci/` — contains `SKILL.md`, `scripts/card_generator.py`, `fonts/`, and `knowledge-base/`.
- **Knowledge base:** `.claude/skills/dailybci/knowledge-base/` (`INDEX.md` + `papers/<subfield>/`). Wherever the text below writes `knowledge-base/...`, read it as `.claude/skills/dailybci/knowledge-base/...`.
- **Working data (per-run):** `papers/` at project root — downloaded full-text PDF/`<slug>-fulltext.txt`, figure images, and PIL crops. **Gitignored scratch:** not version-controlled (figures are baked into the committed `output/` cards), so it's regenerable and deleted at Step 10.
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
- Then use `WebSearch` to **supplement** — fill in journal (Nature/Science/NEJM) coverage, news framing, and to cross-check anything the listings surfaced. Search is the second pass, not the first.

**Fallback path — no browser (headless / cron / `claude -p`).** Run at least 3 different `WebSearch` queries to cast a wide net, and pull preprint text via open APIs (e.g. NCBI BioC) rather than `curl` on the gated sites. Be explicit with the user that without a browser the freshest 48h may be under-covered due to index lag.

**Honesty about the window:** the field does not produce a landmark every day. If the strict past-48h window is genuinely thin (common on weekends), say so in one line and present the most significant *recent* (this-week) work instead — degrade gracefully, never skip a day, never pad the freshness column.

Source priority:
1. **Academic preprints & journals** — arXiv (q-bio.NC, cs.AI+neuro), bioRxiv, medRxiv, Nature, Science, NEJM
2. **Conferences** — if SfN, NeurIPS, BCI Society, IEEE EMBS, or similar is happening, prioritize its outputs
3. **Researcher social media** — X/Twitter posts from domain researchers
4. **Company & regulatory** — Neuralink, Synchron, Paradromics, Precision Neuroscience, FDA, NIH BRAIN Initiative

Search terms: "brain-computer interface", "BCI", "neural decoding", "neuroprosthesis", "ECoG", "intracortical", "neural interface", "brain-machine interface", "speech BCI", "motor decoding", "closed-loop neural", combined with date-relevant terms.

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
   - **Download a figure to `papers/`:** fetch the blob in-page (`fetch(earlyUrl,{credentials:'include'})`) and trigger a download via a temporary `<a download>` click, then `mv ~/Downloads/<name> papers/`. (`curl` on the image CDN usually returns the Cloudflare HTML challenge, not the JPEG — don't rely on it. **Don't `curl` over a good local file** — it'll clobber it with the 403 HTML page.)
   - **To display any figure to the user:** do NOT use browser `screenshot` (that image only enters the model context, not reliably the user's chat). Per Content Standards → *Figures Are Always Shown Inline*: the figure is already a local file in `papers/`, so just **`Read` that file** — Read renders it inline in the user's chat. To show one panel, `PIL Image.crop()` it to a new file, then `Read`. Reliable recipe: put explanation text first and the `Read` as the last line of the message.
   - **If the download is blocked by a browser permission, STOP and ask the user to click "Allow" — do not build a workaround.** Chrome blocks *multiple automatic downloads* per page after the first: the 1st figure lands, the rest are silently blocked behind an "Allow / Block" chip the user may not even notice. The correct move is a one-line prompt: *"Chrome is blocking multiple downloads — please click 'Allow' on the download prompt (top-right of the address bar), then I'll continue."* A workaround that worked this-session-only: trigger **one** download per fresh page-load (re-`navigate` the tab between each), since the per-load block resets. **Do NOT** stand up a local HTTP server to receive POSTed bytes — it dead-ends on Private Network Access preflight + extension network sandboxing, and the repeated DOM-wiping freezes the tab. This is a specific instance of a general rule: **when a blocker is one user click away (download/permission/auth popups), take the shortest path — prompt the user immediately and explicitly (say where to click and what to click); only reach for technical workarounds when the user genuinely cannot intervene (headless/cron).** See memory `shortest-path-on-user-resolvable-blockers`.
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

### Step 5: First draft — thread copy + 小红书 copy with rough figures, in chat

Right after the insight is confirmed, produce the **first full version** and present it in chat: **both** the English X-thread copy **and** the 小红书 card-by-card copy, with **each figure card's figure shown inline (a rough crop is fine)** so the user sees text+figure paired from the very first version. This is the content layer — logic, numbers, comparisons, and the text–figure pairing — produced cheaply so it can be revised and fact-checked **before** the expensive final card rendering. (Rationale: rendering polished cards is the heavy step; if a core number is wrong, that work is wasted. Facts first, polished production later. But rough crops of already-downloaded figures are cheap, so pair them in from the start — don't make the user imagine the layout.)

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

### Step 7: Production — X thread + 小红书 cards with figures

Run this **only after the fact-check gate (Step 6) is clear.** The copy for both languages was already drafted in Step 5 and verified in Step 6; Step 7 turns it into the two **published forms** — finalize the thread and render the 小红书 cards. (When revising, keep each language written independently from the shared outline — never translate one from the other. They share the outline and load-bearing facts, but the two media may differ in depth: thread = self-contained in text; 小红书 = deeper via figure+text. See Content Standards → Bilingual Content Workflow.)

**English — X/Twitter thread:**
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
gen.tail_card(["¹ Ref 1...", "² Ref 2..."], "output/2026-06-07-slug/05-tail.png")
```
Card sequence: 封面卡 → 图卡（按内容需要,通常 2-5 张,用 Step 3 下到本地的论文原图/裁图 + 三段式中文评注）→ 文字卡（每张一个要点,字大留白）→ 尾卡（简评 + 参考来源,含核心论文链接）. 图卡数量服从逻辑链,别硬凑或硬砍。The script handles dual-font mixing (Latin + STHeiti SC), line wrapping, consistent header/footer, and superscript fallback.

**Four hard rules for the cards (established by user review — apply them yourself, do not make the user re-request them each round):**

1. **封面必须交代"在解读哪一篇"——这是开篇身份。** Don't open with a colloquial method gloss ("用'让十个解码器投票'的办法"). The cover's `source` block must state, plainly: **何时 · 什么平台/期刊 · 题为《…》的论文 · 用什么方法**. If the authors/lab are notable, **add who & where + a one-line why-credible** (e.g. "通讯作者 Francis Willett,Stanford 神经假体实验室——2023 年 62 词/分语音 BCI 的一作"). The reader should know exactly what work they're reading an explanation *of* before anything else. The punchy "与我有关" hook still goes in the title lines; provenance goes in `source`.

2. **图卡裁到关键面板——清楚 > 全面,而且你自己先决策,别来回问。** A dense multi-panel paper figure shrunk whole makes every sub-panel unreadable. If **one** panel carries this card's insight, **crop the figure to that panel** before passing it in (PIL crop → `papers/[slug]-figNx.jpg`) so it renders large and legible. Decide crop-vs-keep-whole **up front, yourself**, at figure-prep time — making the user iterate "here's the figure → want me to crop? → ok now decide again" wastes their time. Only keep the full figure when the card genuinely needs multiple panels together. Helping the reader *see it clearly* always beats showing more.

3. **图文必须对版——评注要指认图里的东西.** The point of putting a figure on a card is that the text alone couldn't show it. So the annotation must **explicitly reference what's in the figure** — "如上图,红柱(完整集成)、紫柱(伪集成)都明显低于灰柱(基线)…" — not text that talks past the image. Figure and words describe the same thing; the figure is evidence the words point at, never decoration with self-contained text beside it.

4. **每张图卡是"结论开头 → 读图 → 转场"的三段式,卡与卡咬成一条逻辑链.** 整套卡不是孤立要点的堆叠。每张图卡的评注分三拍:**(1) 第一句直接给该卡的结论/承上**(接住上一张的转场);**(2) 中间一两句读图**——指认图里的线/形状/坐标/颜色(规则 3),但**不要纯描述像素**;**(3) 最后一句收束并转场到下一张**("好,我们已经知道了 X,但接下来还需要 Y")。把握"读图"的度:既部分解读了图,又把大逻辑串顺——不脱离图、也不就图论图。前一张的转场要接得住后一张的开头,让封面→各图卡→尾卡顺成一条承前启后的链。这是 2026-06-15 用户定稿的规矩。

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
- **图的裁切要多轮重审、裁到干干净净为止——图的清晰好看很重要。** 粗裁常常带进隔壁 panel 的残块(箱线、图例)、切掉坐标轴/标签、或把曲线截断。**每渲染一版就把卡片本身 `Read` 出来看**——只有看渲染后的卡才看得出残留和截断;一旦发现图不干净(邻 panel 杂块、缺轴、断线),就重裁、重渲染,**该几轮就几轮**,直到这张图只剩它自己、坐标曲线完整。别把脏裁图发出去当最终版。

**The "最终版 / final version" is always the actually-rendered cards, shown inline — never text-only copy.** When the user asks for the final/最终版, that means: run `card_generator.py`, produce the PNGs (figure cards composited with the real paper images), and **display the rendered card images in chat so the user can browse the actual 图卡** — image and text together as they will publish. Do not stop at a text description of the cards and make the user imagine the layout. Rough text copy belongs to the *draft* stage (Steps 5/7); the final stage owes the user browsable cards. The only exception is a headless run with no way to surface images — then say so explicitly.

Present all final cards for last confirmation before posting.

### Step 9: Knowledge base update (automatic)

After publishing, assess whether today's paper is significant enough to become a milestone entry. If yes:
- Generate a structured summary in the knowledge base format (see Mode B)
- Suggest adding it: "今天这篇关于 [topic] 的工作值得加入知识库吗？"
- If the user confirms, write it to `knowledge-base/papers/` and update `INDEX.md`

### Step 10: Clean up local scratch (disk)

发布完、知识库也更新后,`papers/` 里这一期的工作文件就用不上了——**主动提醒用户清理**(用户本机磁盘有限)。`papers/` 是 scratch 且已 gitignore(下载的论文图、PIL 裁的子图、全文 `<slug>.pdf` / `<slug>-fulltext.txt` 都不进版本库);真正的成品是 `output/<date>-<slug>/` 的卡片 PNG——**图已烤进卡片,源图删了不影响成品**。

给用户一个带清单 + 大小的提示,**等用户确认再删**:
> 今天这期发完了。`papers/` 下这期的工作文件(下载原图 N 张、裁图 M 张、PDF/全文 ≈ X MB)已经用不上了——成品卡在 `output/<slug>/`、图已烤进卡。要我清掉吗?

- 用户同意 → `rm` 掉这一期的 `papers/<slug>*`(图 + PDF + 全文)。
- **绝不碰 `output/`(成品)、`.claude/`(技能/知识库)、或别期的工作文件。** 删前再扫一眼清单确认范围。
- 删除是不可逆操作:**必须用户明确同意才删**,不要默认替用户清。无头运行(cron/`claude -p`)不要自动删,留着等人工确认。

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
- **标注参考来源** — 所有关键数据（数字、百分比、对比结论）必须加角标引用。X thread 在末尾 tweet 列出参考链接；小红书在尾卡列出参考文献。角标格式：上标数字 ¹ ² ³，对应尾部编号列表。
- **避免"不是...而是..."句式** — 中文写作中不要使用"不是 X，而是 Y"这种对立表达。改用直接陈述：直接说 Y 是什么，如果需要对比，用"相比 X，Y 更..."或直接并列呈现让读者自己判断。

## Visual Design (小红书卡片)

**排版风格：学术简洁。** 类似 Nature Briefing 的克制感——大量留白、无装饰、纯靠字号和灰度层级建立信息结构。

- 背景：纯白或极浅灰（#FAFAFA）
- 无色块、无渐变、无图标装饰
- 信息层级靠字号（64/56/34/24px）和灰度（#1A1A1A → #666666 → #BBBBBB）区分
- 边距慷慨（100px+），内容不要贴边
- 封面卡只放：标题 + 一句话核心发现 + 品牌/日期（极淡）
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
