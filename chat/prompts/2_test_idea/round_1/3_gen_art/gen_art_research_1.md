# gen_art_research_1 — test_idea

> Phase: `invention_loop` · round 1 · `gen_art`
> Run: `run_txhWJXyNIa5t` — Typological Predictors of Dependency Distance Distribution Shapes in Universal Dependencies
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_research_1` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-07-19 23:31:12 UTC

````
Read and STRICTLY follow these skills: aii-web-tools.

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_txhWJXyNIa5t/3_invention_loop/iter_1/gen_art/gen_art_research_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_txhWJXyNIa5t/3_invention_loop/iter_1/gen_art/gen_art_research_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_txhWJXyNIa5t/3_invention_loop/iter_1/gen_art/gen_art_research_1/file.py`, `/ai-inventor/aii_data/runs/run_txhWJXyNIa5t/3_invention_loop/iter_1/gen_art/gen_art_research_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_txhWJXyNIa5t/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for prior work and the field's landscape to ground your research.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>

<artifact_plan>
id: gen_plan_research_1_idx3
type: research
title: Methodological review for DD typology study
summary: >-
  Research best practices for mixed-effects modeling of typological data, distribution fitting for dependency distance, and
  spoken vs written genre effects in syntax to guide the main experiment design.
runpod_compute_profile: cpu_light
question: >-
  What are the best methodological practices for (1) fitting mixed-effects models to typological data with crossed random
  effects, (2) fitting probability distributions to dependency distance data, and (3) what prior evidence exists for spoken
  vs written genre effects on syntactic dependency structures?
research_plan: |
  ## PHASE 1: Mixed-Effects Models for Typological Data (Priority: HIGH)

  ### Step 1.1: Search for Levshina's methodology papers
  - Search query: 'Levshina 2021 mixed-effects models typological data'
  - Search query: 'Levshina 2022 quantitative typology mixed-effects'
  - Look for: 'How to do Linguistics with R' (Levshina 2021) and subsequent papers
  - Fetch and extract: specific model specification recommendations, R packages used (lme4, brms), Python equivalents
  - Key information to extract:
    * How crossed random effects are specified for language family and treebank
    * Whether centered/scaled predictors are recommended
    * How multiple comparisons are handled
    * What effect sizes are reported

  ### Step 1.2: Search for Jaeger's work on mixed-effects in linguistics
  - Search query: 'Jaeger mixed-effects models psycholinguistics crossed random effects'
  - Search query: 'Baayen 2008 mixed-effects models linguistic data'
  - Look for: Recommendations on random effect structure selection
  - Key information: How to determine appropriate random effects structure, when to include random slopes vs only intercepts

  ### Step 1.3: Identify Python tools for mixed-effects models
  - Search query: 'statsmodels MixedLM typological data example'
  - Search query: 'pymer4 Python lme4 equivalent'
  - Search query: 'rpy2 lme4 Python interface tutorial'
  - Evaluate each tool:
    * statsmodels MixedLM: Does it support crossed random effects? What's the syntax?
    * pymer4: Is it maintained? Does it handle complex random effects structures?
    * rpy2: What's the overhead? Is it reliable in research pipelines?
  - Fetch documentation pages and extract code examples

  ### Step 1.4: Search for prior mixed-effects models in quantitative typology
  - Search query: 'mixed-effects model WALS features typological prediction'
  - Search query: 'cross-linguistic mixed-effects model Bickel 2017'
  - Look for: Recent (2020-2026) papers using mixed-effects with WALS data
  - Extract: Model specifications, how they handle non-independence, what random effects they use

  ## PHASE 2: Distribution Fitting for Dependency Distance (Priority: HIGH)

  ### Step 2.1: Find Liu et al. papers on DD distribution fitting
  - Search query: 'Liu dependency distance distribution Right Truncated Modified Zipf-Alekseev'
  - Search query: 'Liu 2008 dependency distance distribution exponential power-law'
  - Fetch papers: Look for arXiv or journal versions
  - Extract:
    * Exact distribution formulas (PDF/CDF)
    * Parameter estimation method (MLE? Method of moments?)
    * Goodness-of-fit criteria used
    * Software used for fitting (R? Python? MATLAB?)
    * Whether they fit per-language or pooled

  ### Step 2.2: Find Ferrer-i-Cancho's work on DD distribution shapes
  - Search query: 'Ferrer-i-Cancho dependency distance distribution shape parameters'
  - Search query: 'Ferrer-i-Cancho 2014 optimality score dependency distance'
  - Extract: Theoretical justification for specific distribution shapes, what shape parameters mean linguistically

  ### Step 2.3: Identify Python tools for distribution fitting
  - Search query: 'scipy.optimize MLE distribution fitting example'
  - Search query: 'scipy.stats.distribution fit method maximum likelihood'
  - Fetch scipy documentation for:
    * scipy.stats.expon (exponential distribution)
    * scipy.stats.powerlaw (power-law distribution)
    * Generic likelihood function maximization with scipy.optimize.minimize
  - Extract: Exact code patterns for fitting arbitrary distributions to data

  ### Step 2.4: Search for distribution comparison methods
  - Search query: 'Kolmogorov-Smirnov test distribution comparison Python'
  - Search query: 'AIC BIC model selection distribution fitting'
  - Extract: How to choose between exponential vs power-law vs other distributions

  ## PHASE 3: Spoken vs Written Genre Effects (Priority: MEDIUM-HIGH)

  ### Step 3.1: Find Dobrovoljc (2026) paper
  - Search query: 'Dobrovoljc 2026 Counting trees speech writing syntax'
  - Search query: 'Dobrovoljc Corpus Linguistics and Linguistic Theory 2026'
  - Fetch paper from journal or arXiv
  - Extract:
    * What syntactic differences were found between speech and writing
    * What treebanks were used (specifically spoken ones)
    * What methodological approach was used
    * Whether dependency distance was discussed

  ### Step 3.2: Search for other spoken vs written syntax studies in UD
  - Search query: 'Universal Dependencies spoken language treebank genre effects syntax'
  - Search query: 'UD treebank speech genre dependency parsing differences'
  - Look for: Papers comparing spoken and written UD treebanks
  - Extract: Which treebanks are identified as spoken (fr_rhapsodie, en_eslspok, en_childes, etc.)

  ### Step 3.3: Search for psycholinguistic evidence of speech vs writing processing differences
  - Search query: 'speech writing working memory dependency processing'
  - Search query: 'spoken language syntactic complexity dependency distance'
  - Extract: Theoretical predictions about whether speech should have shorter or longer dependencies

  ## PHASE 4: WALS-to-UD Mapping (Priority: MEDIUM)

  ### Step 4.1: Search for prior WALS-to-UD mapping efforts
  - Search query: 'WALS features Universal Dependencies treebank mapping'
  - Search query: 'predicting UD treebank WALS typological features'
  - Look for: Papers or repositories that have mapped WALS features to UD languages
  - Extract: Methodology for mapping, any existing datasets/code

  ### Step 4.2: Identify WALS features most relevant to dependency distance
  - Search query: 'WALS word order feature dependency distance'
  - Search query: 'WALS morphological complexity syntactic dependency'
  - Extract: Which WALS features (chapter numbers) are hypothesized to affect DD

  ### Step 4.3: Find WALS API or download options
  - Search query: 'WALS database download CSV API'
  - Search query: 'World Atlas of Language Structures data access'
  - Extract: How to download WALS data programmatically, what format it's in

  ## PHASE 5: Bibliography Compilation (Priority: MEDIUM)

  ### Step 5.1: Collect DOIs and paper titles from all sources found
  - For each paper found, extract: Full title, authors, year, journal/venue, DOI
  - Organize by topic: mixed-effects, distribution fitting, genre effects, WALS

  ### Step 5.2: Generate BibTeX entries
  - Use Semantic Scholar API or similar to get BibTeX for each paper
  - Search query: 'paper title BibTeX Semantic Scholar'
  - Verify each BibTeX entry is complete and correctly formatted

  ### Step 5.3: Summarize methodological recommendations
  - Create a summary table of:
    * Recommended mixed-effects model specification
    * Recommended distribution fitting approach
    * Recommended genre comparison methodology
    * Software recommendations with pros/cons

  ## OUTPUT REQUIREMENTS

  The research executor must produce:
  1. `research_out.json` with fields: answer (synthesized findings), sources (list of sources with URLs and extracted info), follow_up_questions
  2. `research_report.md` with:
     - Introduction stating the methodological questions
     - Section 1: Mixed-Effects Models for Typological Data (findings + recommendations)
     - Section 2: Distribution Fitting for Dependency Distance (findings + code examples)
     - Section 3: Spoken vs Written Genre Effects (prior findings summary)
     - Section 4: WALS-to-UD Mapping (approach recommendations)
     - Section 5: Bibliography (full BibTeX)
     - Conclusion: Methodological recommendations for the main experiment

  ## SEARCH TOOL USAGE PATTERN

  For each search:
  1. Use web_search to discover relevant papers/URLs
  2. Use web_fetch on promising URLs to read content
  3. Use fetch_grep with specific regex patterns to extract exact information (e.g., model formulas, code snippets, parameter names)

  Example fetch_grep patterns:
  - For model specs: '(lmer|lme4|MixedLM)\(.*\)'
  - For distribution formulas: '(PDF|CDF|f\(x\)|p\(x\)).*='
  - For WALS features: 'WALS.*chapter.*[0-9]'

  ## TIME ALLOCATION

  - Phase 1: 60 minutes (mixed-effects models - most critical)
  - Phase 2: 45 minutes (distribution fitting)
  - Phase 3: 45 minutes (genre effects)
  - Phase 4: 30 minutes (WALS mapping)
  - Phase 5: 30 minutes (bibliography compilation)
  - Report writing: 30 minutes

  Total: ~3.5 hours (within 3h budget if efficient parallelization is used)

  ## PARALLELIZATION OPPORTUNITIES

  Can parallelize:
  - Phase 1.1 and 1.2 (both searching for mixed-effects references)
  - Phase 2.1 and 2.2 (both searching for distribution fitting references)
  - Phase 3.1 and 3.2 (both searching for genre effect papers)

  Sequence dependencies:
  - Must fetch before fetch_grep (need URL first)
  - Phase 5 depends on all prior phases (need papers first)
explanation: >-
  This research is critical foundational work that will determine the statistical methodology for the main hypothesis test.
  Without proper mixed-effects model specification, the results may suffer from pseudoreplication (treating non-independent
  data points as independent). Without proper distribution fitting methodology, the shape parameters may be poorly estimated.
  Without understanding prior genre effects, the spoken vs written comparison may be underpowered or misinterpreted. The bibliography
  will also support the related work section of the final paper. Kaja Dobrovoljc, as the reviewer, would expect rigorous methodological
  justification - this research ensures we meet that standard.
</artifact_plan>

<investigation_process>
1. DIVERGE: Brainstorm multiple angles/framings of the question before searching. Think across fields — what adjacent domains might have relevant insights?
2. SEARCH: Multiple queries per angle with different phrasings to discover the landscape
3. FETCH: Read promising URLs at high level. Snippets are NOT enough — fetch full pages
4. DETAIL: aii-web-tools fetch_grep for specifics from key pages/PDFs
5. CONTRAST: Actively try to disprove your emerging conclusions. Search with different phrasings, "[topic] criticism", "[topic] limitations". Check across fields — the same finding may exist under different names
6. SYNTHESIZE: Integrate into balanced conclusion
7. ITERATE: Expect to repeat steps 2-6 if findings are incomplete or one-sided. Don't settle on first results
8. SUMMARIZE: Output JSON must include 'title' and 'summary' fields
</investigation_process>

<output_requirements>
- Write research_out.json to your workspace with all findings
- Provide your finding as clear prose WITH NUMBERED CITATIONS
- EVERY factual claim must have a citation number in brackets: [1], [2], [1, 3], etc.
- Include BOTH supporting AND contradicting evidence
- Be explicit about confidence level and what would change it
- End with follow-up questions for further investigation
</output_requirements>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

Research everything specified in the artifact plan, but you may also investigate additional relevant aspects beyond what's listed. Investigate this question thoroughly.

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_txhWJXyNIa5t/3_invention_loop/iter_1/gen_art/gen_art_research_1/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ResearchExpectedFiles": {
      "description": "All expected output files from research artifact.",
      "properties": {
        "output": {
          "description": "Path to research output JSON. Example: 'research_out.json'",
          "title": "Output",
          "type": "string"
        }
      },
      "required": [
        "output"
      ],
      "title": "ResearchExpectedFiles",
      "type": "object"
    },
    "Source": {
      "description": "A source used in the research.",
      "properties": {
        "index": {
          "description": "Citation number (1, 2, 3, ...)",
          "title": "Index",
          "type": "integer"
        },
        "url": {
          "description": "Full URL of the source",
          "title": "Url",
          "type": "string"
        },
        "title": {
          "description": "Title of the article/page",
          "title": "Title",
          "type": "string"
        },
        "summary": {
          "description": "Brief summary of what this source contributed",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "index",
        "url",
        "title",
        "summary"
      ],
      "title": "Source",
      "type": "object"
    }
  },
  "description": "Research artifact \u2014 structured output + file metadata.\n\nConducts thorough web research using the aii-web-tools skill.\nReturns structured JSON output with citations.",
  "properties": {
    "title": {
      "default": "",
      "description": "Artifact title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters); describe the content, not a status.",
      "maxLength": 90,
      "minLength": 12,
      "title": "Title",
      "type": "string"
    },
    "layman_summary": {
      "default": "",
      "description": "One-sentence plain-language summary of what this artifact does, accessible to non-experts. Used only in the per-artifact README, not in downstream prompts.",
      "maxLength": 250,
      "minLength": 80,
      "title": "Layman Summary",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Summary for downstream artifacts: what this artifact provides",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/ResearchExpectedFiles",
      "description": "All output files you created. Must include research_out.json with your research findings."
    },
    "upload_ignore_regexes": {
      "description": "Regex patterns for workspace paths that must NOT be published to the GitHub repo, matched against each file's path relative to this artifact's workspace root (POSIX form, e.g. 'cache/abc.json'). Applied ON TOP OF the deploy step's built-in exclusions. Use this for executor-specific caches, large transient intermediates, or content-addressed blob stores (e.g. a cache/ dir of thousands of hash-named files) that would bloat the repo. Examples: ['(^|/)cache/', '(^|/)\\\\.weight_cache/', '(^|/)checkpoints/']. Leave empty if every workspace file should be published.",
      "items": {
        "type": "string"
      },
      "title": "Upload Ignore Regexes",
      "type": "array"
    },
    "answer": {
      "description": "Comprehensive answer with NUMBERED CITATIONS. Cite sources by number: 'Claim [1].' or 'According to [2, 3]...'",
      "title": "Answer",
      "type": "string"
    },
    "sources": {
      "description": "All sources used, with index matching citation numbers in answer",
      "items": {
        "$ref": "#/$defs/Source"
      },
      "title": "Sources",
      "type": "array"
    },
    "follow_up_questions": {
      "description": "2-3 follow-up questions that emerged from the investigation",
      "items": {
        "type": "string"
      },
      "title": "Follow Up Questions",
      "type": "array"
    }
  },
  "required": [
    "out_expected_files",
    "answer",
    "sources",
    "follow_up_questions"
  ],
  "title": "ResearchArtifact",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `/ai-inventor/aii_data/runs/run_txhWJXyNIa5t/3_invention_loop/iter_1/gen_art/gen_art_research_1/.sdk_openhands_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-07-19 23:31:12 UTC

```
Direction: Computational Linguistics — Dependency Distance Minimization Across UD Treebanks. Something genuinely novel and groundbreaking that measures dependency-distance distributions across UD treebanks, investigates whether spoken language minimizes more than written, characterizes how typology interacts with the pattern, and identifies families that deviate. MUST use commul/universal_dependencies on HuggingFace.

Ambition: level 3 of 5 — phenomenological science: surface and rigorously characterize a new empirical regularity or anomaly in the data, even before a full theoretical explanation exists.

Reviewer: I am Kaja Dobrovoljc (JSI / University of Ljubljana). Calibrate from my existing papers. Cross-domain methods (information theory, mixed-effects models, sequence models) welcome — but keep them close to what I already know, not too far from my background.

Submission/Goal: a paper for ACL, EMNLP, or the Computational Linguistics journal. Audience: computational linguists and quantitative typologists. Tone: empirically rigorous, careful with linguistic detail, reproducible on public UD.
```

### [3] SKILL-INPUT — aii-web-tools · 2026-07-19 23:31:20 UTC

The agent loaded the **aii-web-tools** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-web-tools
description: "Web research toolkit: web search (Serper/Google), web page fetch as markdown (HTML and PDF), and regex grep over full page/PDF text. Use whenever a task needs to search the web, read a page, mine a paper/PDF, verify citations, or extract exact quotes, numbers, or methodology from a URL."
---

## Web tools

You have three web capabilities: **search**, **fetch**, and **grep** (exact
regex extraction over a full page or PDF).

**Pick where they come from, in this order:**

1. **If you have built-in `WebSearch` / `WebFetch` tools, PREFER those over the
   scripts below.** They may be **deferred tools** (listed by name but with
   schemas not yet loaded) — if so, call `ToolSearch("select:WebSearch,WebFetch")`
   ONCE to load them, then use them normally. Do not skip them just because they
   need that one extra load step; they are the preferred path. Pair them with the
   `aii_web_tools__fetch_grep` script below when you need exact text / numbers /
   methodology that a summary would miss, or when reading a PDF.
2. **Only if you have NO built-in `WebSearch` / `WebFetch`** (e.g. the OpenHands
   backend), use the scripts in this skill (below). They are our own
   implementations — Serper.dev for search, html2text + PyMuPDF for fetch, and
   regex grep over the full document text. They work without any built-in web
   tools.

Workflow either way: **search** (discover) → **fetch** (read for the gist) →
**grep** (pull exact details / read PDFs).

---

## Running the scripts

Run every script with the skill's pre-provisioned interpreter (it already has
`requests`, `html2text`, `pymupdf`, `python-dotenv`). Set `PY` once:

```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

### 1. Search the web (Serper.dev / Google)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "neuro-symbolic FOL translation LLM" --max-results 10
```

Returns ranked title / URL / snippet lines. Use it first to scan the
landscape; snippets are for discovery only — fetch a page before judging it.

### 2. Fetch a page as markdown (HTML or PDF)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" fetch --url "https://arxiv.org/abs/2303.11366" --max-chars 10000
```

`--max-chars` caps output (default 10000); `--char-offset N` pages further in.
Handles PDFs transparently via PyMuPDF.

### 3. Grep a page or PDF (exact regex extraction)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" grep --url "https://arxiv.org/pdf/2303.11366" --pattern "verbal reinforcement" --max-matches 20 --context-chars 200
```

Returns only the matching sections with surrounding context — the right tool
for exact numbers, table values, methodology, or long PDFs where a summary
would lose the detail. `-i` for case-insensitive.

**Parallelize** independent searches/fetches in one turn; only sequence a
fetch after the search that produced its URL.

---

## Notes

- The scripts call our ability server. If a script prints
  `Ability service not available`, the server is down — say so rather than
  silently improvising a different search method.
- Do **not** hand-roll your own `requests`/scraping for search when these
  tools are available: Serper returns clean Google results and the fetch/grep
  scripts already handle HTML, PDFs, and encoding.
````

### [4] SYSTEM-USER prompt · 2026-07-19 23:31:34 UTC

```
<validation-feedback>
Attempt 1 failed validation.

You have not created the output file `.sdk_openhands_agent_struct_out.json` yet. Use the Write tool to create it.

Please use the Write tool to overwrite `.sdk_openhands_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```

### [5] SYSTEM-USER prompt · 2026-07-19 23:32:00 UTC

```
<validation-feedback>
Attempt 2 failed validation.

You have not created the output file `.sdk_openhands_agent_struct_out.json` yet. Use the Write tool to create it.

Please use the Write tool to overwrite `.sdk_openhands_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```

### [6] SYSTEM-USER prompt · 2026-07-19 23:40:21 UTC

```
<verification_failed>
Your research output failed verification (attempt 1/10).
</verification_failed>

<schema_errors>
JSON SCHEMA ERRORS:
  - research_out.json: Missing required 'title' field
  - research_out.json: Missing required 'summary' field

Fix: research_out.json must have:
     {
       "answer": "comprehensive answer with [1], [2] citations",
       "sources": [{"index": 1, "url": "...", "title": "...", "summary": "..."}],
       "follow_up_questions": ["Question 1?", "Question 2?"],
       "summary": "what was found"
     }

     Each citation [N] in answer MUST match a source with that index.
</schema_errors>

<content_warnings>
CONTENT ISSUES:
  - research_out.json: 'title' is too short

Fix: Ensure answer is comprehensive, has proper citations, and all sources are cited.
</content_warnings>

<task>
FIX ISSUES:
1. Output valid research_out.json with all required fields
2. Ensure every factual claim has a numbered citation [1], [2], etc.
3. Ensure every source has a matching citation in the answer
</task>
```
