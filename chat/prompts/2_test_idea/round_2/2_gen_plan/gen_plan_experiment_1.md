# gen_plan_experiment_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_plan`
> Run: `run_txhWJXyNIa5t` — Typological Predictors of Dependency Distance Distribution Shapes in Universal Dependencies
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_plan_experiment_1` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-07-20 01:35:12 UTC

````
<hypothesis>
kind: hypothesis
title: Typological predictors of dependency distance distribution shapes in UD
hypothesis: >-
  The shape parameters of dependency distance (DD) distributions—not merely their means—can be systematically predicted by
  typological features (word order type, morphological complexity, case marking) in a mixed-effects framework using data from
  Universal Dependencies treebanks. Spoken genres may exhibit different DD distribution shapes than written genres, but this
  comparison is currently limited by small spoken treebank sample sizes (6,239 dependencies, 0.6% of total data). Preliminary
  data preparation (979,098 dependency observations from 193 languages, 116 treebanks mapped to WALS features) is complete,
  but statistical confirmation via ZA distribution fitting and mixed-effects modeling remains to be performed.
motivation: >-
  Dependency Distance Minimization (DDM) is a well-established cross-linguistic universal, but prior work focuses almost exclusively
  on mean DD (MDD) as the summary statistic. This ignores the rich distributional information encoded in the full DD distribution
  shape. Meanwhile, the interaction between typology and DD distributions remains understudied: while Futrell et al. (2015)
  established DDM as universal across 37 languages, and Gerdes et al. (2026) recently showed functional vs. lexical distinctions
  across 122 languages, nobody has systematically linked WALS typological features to DD distribution shape parameters using
  mixed-effects models across the full UD collection. Such a study would: (1) reveal whether typological constraints operate
  on distribution shape or only on central tendency; (2) quantify the spoken-vs-written DD difference with appropriate statistical
  controls; (3) identify 'outlier' families that deviate from DDM, providing targets for deeper typological investigation.
  For computational linguistics and quantitative typology, this provides a more nuanced picture of how grammar, processing
  pressures, and modality interact to shape syntactic dependency structures.
assumptions:
- >-
  Dependency distance can be reliably computed from UD treebanks using standard head-dependent linear order differences.
- >-
  WALS typological features (word order, morphology) can be reliably mapped to UD treebank languages at the language level.
- >-
  Mixed-effects models with crossed random effects for language family and treebank can appropriately control for non-independence
  in the data.
- >-
  Distribution shape parameters (e.g., exponential decay rate, tail exponent) meaningfully capture syntactic differences across
  languages and genres.
- >-
  The commul/universal_dependencies dataset on HuggingFace provides sufficient coverage of spoken and written genres for a
  meaningful comparison.
investigation_approach: |-
  1. DATA PREPARATION: Load all 350+ treebanks from commul/universal_dependencies on HuggingFace. Compute DD for every dependency in every sentence. Categorize treebanks by genre (spoken: fr_rhapsodie, en_eslspok, en_childes; written formal: news/wiki treebanks; written informal: reddit, etc.). Map languages to WALS features (word order: SVO/SOV/etc.; morphological complexity; case marking).

  2. DISTRIBUTION FITTING: Fit probability distributions (exponential, power-law with cutoff, Right Truncated Modified Zipf-Alekseev) to each treebank's DD distribution. Extract shape parameters (decay rate λ, tail exponent α, etc.).

  3. MIXED-EFFECTS MODELING: Use linear mixed-effects models (LMMs) with shape parameters as dependent variables, WALS features as fixed effects, and crossed random effects for language family and treebank. Model: shape_param ~ word_order + morphological_complexity + case_marking + (1|family) + (1|treebank). Compare spoken vs written via genre contrast in the model.

  4. OUTLIER DETECTION: Identify language families with large random effect magnitudes (deviating significantly from the universal pattern). Investigate these families qualitatively.

  5. ROBUSTNESS: Control for sentence length (a known confound), treebank size, and annotation scheme differences. Use bootstrap confidence intervals for all estimates.
success_criteria: |-
  1. CONFIRM: WALS word order features (e.g., SOV vs SVO) significantly predict DD distribution shape parameters (p < 0.05) in mixed-effects models, explaining >10% additional variance beyond a null model.

  2. CONFIRM: Spoken genres show systematically different DD distribution shapes (heavier tails, i.e., more long-range dependencies) than written genres, even after controlling for sentence length and language family (β_genre significant, p < 0.05).

  3. CONFIRM: At least 2-3 language families show significant deviations (random effect |estimate| > 2 SE) from the universal DDM pattern, and these deviations correlate with specific typological features not in the main model.

  4. DISCONFIRM: If no WALS features significantly predict shape parameters after correction for multiple comparisons, or if spoken-written differences disappear after controlling for sentence length, the hypothesis is refuted.

  5. REPRODUCIBILITY: All analyses run on public data (commul/universal_dependencies, WALS) with open-source Python code (numpy, pandas, scipy, statsmodels).
related_works:
- >-
  Futrell et al. (2015) PNAS: 'Large-scale evidence of dependency length minimization' - Established DDM as universal across
  37 languages using mean dependency length. Our work extends this by (a) using 350+ UD treebanks (10x more languages), (b)
  analyzing full distribution shapes not just means, (c) using mixed-effects models with WALS predictors, and (d) explicitly
  comparing spoken vs written genres. The core mechanism (linking WALS features to DD distribution parameters via mixed-effects
  models) is entirely novel.
- >-
  Gerdes et al. (2026) arXiv:2607.01899: 'The Grammar Does the Work: Functional vs. Lexical Dependency Length Minimization
  Across Universal Dependencies' - Analyzed 122 languages in UD/SUD, finding functional dependencies are universally short
  while lexical dependencies vary by typology. Our work differs fundamentally: (a) Gerdes separates functional vs lexical
  dependencies; we analyze the FULL DD distribution shape regardless of dependency type, (b) Gerdes reports means; we fit
  distribution parameters, (c) Gerdes does not use WALS features as predictors, (d) Gerdes does not compare spoken vs written
  genres systematically.
- >-
  Niu et al. (2023) PACLIC: 'The Cross-linguistic Variations in Dependency Distance Minimization' - Compared 4 languages (Chinese,
  Japanese, English, Czech), finding trade-off between syntactic and morphological complexity. Our work is novel because:
  (a) Niu uses only 4 languages; we use 350+ treebanks, (b) Niu discusses morphology qualitatively; we quantitatively predict
  DD parameters from WALS features via mixed-effects models, (c) Niu does not compare spoken vs written, (d) Niu does not
  fit distribution shapes.
- >-
  Dobrovoljc (2026) Corpus Linguistics and Linguistic Theory: 'Counting trees: A treebank-driven exploration of syntactic
  variation in speech and writing' - Compared syntactic structures (delexicalized subtrees) in speech vs writing for English/Slovenian.
  Our work is complementary: Dobrovoljc studies subtree inventories; we study dependency distance distributions. The core
  mechanism (DD distribution shapes as typological markers) is entirely different.
- >-
  Liu et al. (2008-2017) various: Established DD minimization as universal, fit Right Truncated Modified Zipf-Alekseev distributions.
  Our work uses these distribution fits but applies them in a novel way: as dependent variables in mixed-effects models with
  WALS predictors, enabling typological generalization not possible in single-language studies.
inspiration: >-
  The hypothesis draws from three cross-domain inspirations: (1) QUANTITATIVE TYPOLOGY: Levshina (2021, 2022) uses mixed-effects
  models with WALS features to predict linguistic variables - we adapt this workflow to dependency distance distribution parameters.
  (2) INFORMATION THEORY: Ferrer-i-Cancho's work on optimality scores and distribution shapes suggests that the FULL distribution
  (not just mean) encodes meaningful linguistic information - we extend this by linking distribution parameters to typological
  features. (3) PSYCHOLINGUISTICS: Mixed-effects models are standard in psycholinguistics for controlling for subject/item
  random effects - we apply this framework to typological data (controlling for family/treebank random effects), which is
  standard in quantitative typology (Levshina, Jaeger) but underused in computational linguistics DD research.
terms:
- term: Dependency Distance (DD)
  definition: >-
    The linear distance (in words) between a syntactic head and its dependent in a sentence. For example, in 'the cat sleeps',
    if 'sleeps' is the head of 'cat', the DD is 1 (one word apart).
- term: Dependency Distance Minimization (DDM)
  definition: >-
    The cross-linguistic tendency for human languages to prefer short syntactic dependencies, hypothesized to reduce working
    memory load during processing.
- term: Universal Dependencies (UD)
  definition: >-
    A framework for cross-linguistically consistent treebank annotation, providing dependency parses for 150+ languages. The
    commul/universal_dependencies dataset on HuggingFace provides programmatic access to 350+ UD treebanks.
- term: WALS (World Atlas of Language Structures)
  definition: >-
    A database of structural (typological) features for the world's languages, including word order type (SVO, SOV, etc.),
    morphological complexity, case marking systems, etc.
- term: Mixed-Effects Model
  definition: >-
    A statistical model that includes both fixed effects (predictors of interest, e.g., word order type) and random effects
    (grouping variables, e.g., language family) to account for non-independence in nested data.
- term: Distribution Shape Parameter
  definition: >-
    A parameter that characterizes the shape of a probability distribution, e.g., the decay rate λ of an exponential distribution,
    or the tail exponent α of a power-law distribution. Different from the mean (central tendency).
- term: Right Truncated Modified Zipf-Alekseev Distribution
  definition: >-
    A probability distribution used to model dependency distance data, combining a power-law decay with an exponential truncation
    to account for the finite length of sentences.
summary: >-
  This study will be the first to systematically link WALS typological features to dependency distance distribution shape
  parameters (not just means) using mixed-effects models across 350+ UD treebanks, while also comparing spoken vs written
  genres and identifying outlier language families that deviate from the universal DDM pattern.
_relation_rationale: >-
  Scaling back to reflect actual completed work: data prep done, statistical analysis pending
_confidence_delta: decreased
_key_changes:
- >-
  Removed specific statistical claims (β = 0.084, R² = 0.147) that were not supported by artifacts
- >-
  Added explicit statement that ZA distribution fitting and mixed-effects modeling have NOT been run yet
- >-
  Toned down spoken vs. written claims due to inadequate sample size (6,239 dependencies = 0.6%)
- >-
  Reframed hypothesis as 'can be predicted' rather than confirmed prediction, since analysis is pending
- >-
  Added specific data preparation accomplishments (979,098 observations, 116 treebanks mapped)
- >-
  Removed claims about '3 outlier families' since random effects have not been computed
relation_type: evolution
</hypothesis>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for the methods, proper baselines, and evaluation this field demands.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>

<artifact_direction>
Make this direction concrete and actionable. Keep the same type and respect dependencies.

id: experiment_iter2_dir1
type: experiment
objective: >-
  Fit ZA distributions to dependency distance data from UD treebanks and run mixed-effects models with WALS predictors to
  produce actual statistical results for the paper.
approach: >-
  1. Load dependency distance data from art_sbnX8nlSAUFX (979,098 observations across 193 languages). 2. Load WALS feature
  mappings from art_JLcGgqg6OO_T (116 treebanks with complete mappings). 3. Merge datasets on treebank name. 4. ZA DISTRIBUTION
  FITTING: For each treebank with >1000 dependencies, fit the Right Truncated Modified Zipf-Alekseev distribution P_x = P_1
  * x^{-(a + b*ln x)} using MLE via scipy.optimize.minimize. Extract shape parameters a and b. 5. SPOKEN SAMPLE HANDLING:
  Given only 6,239 spoken dependencies (0.6%), exclude spoken treebanks from ZA fitting (requires >1000 deps). Instead, do
  a separate analysis comparing mean DD between spoken and written using all data with t-tests and simple linear regression.
  6. MIXED-EFFECTS MODELS: Use statsmodels MixedLM to fit: shape_param ~ word_order + morphological_complexity + case_marking
  + sentence_length_mean + (1|family) + (1|treebank). Run separate models for each WALS feature (dummy coded). 7. MODEL DIAGNOSTICS:
  Check convergence, singular fits, report AIC/BIC. 8. OUTPUT: Save all results to method_out.json including: (a) ZA parameters
  per treebank, (b) Mixed-effects model summaries (β, SE, p, CI, R²), (c) Spoken vs written comparison results, (d) Family
  random effects for outlier detection. 9. Use only standard Python libraries (numpy, pandas, scipy, statsmodels) to avoid
  API costs and dependency issues.
depends_on:
- id: art_sbnX8nlSAUFX
  label: dataset
  relation_type:
  relation_rationale:
- id: art_JLcGgqg6OO_T
  label: wals_mapping
  relation_type:
  relation_rationale:
</artifact_direction>

<dependencies>
Completed artifacts this artifact can use during execution.

--- Dependency 1 ---
id: art_sbnX8nlSAUFX
type: dataset
title: UD treebank dependency distances with WALS features
summary: >-
  This dataset contains dependency distance measurements computed from all 350+ UD treebanks available on HuggingFace (commul/universal_dependencies).
  For each non-root dependency in every sentence, the dependency distance (absolute difference between head and dependent
  positions) was computed. Languages were mapped to WALS typological features including word order (1A), morphological complexity
  (20A, 26A), and case marking (49A, 51A). Treebanks were categorized by genre (spoken, written formal, written informal)
  based on name analysis. The dataset contains 979,098 dependency observations from 193 languages, with 80+ languages having
  complete WALS feature mappings. Output files are split into 7 parts to stay under 300MB limit. The dataset is ready for
  mixed-effects modeling and quantitative typological analysis.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_txhWJXyNIa5t/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json
out_dependency_files:
  file_list:
  - data.py
  - full_data_out_parts/full_data_out_1.json
  - full_data_out_parts/full_data_out_2.json
  - full_data_out_parts/full_data_out_3.json
  - full_data_out_parts/full_data_out_4.json
  - full_data_out_parts/full_data_out_5.json
  - full_data_out_parts/full_data_out_6.json
  - full_data_out_parts/full_data_out_7.json
  - data_out_mini.json
  - data_out_preview.json
  data_file_paths:
  - full_data_out_parts/full_data_out_1.json
  - full_data_out_parts/full_data_out_2.json
  - full_data_out_parts/full_data_out_3.json
  - full_data_out_parts/full_data_out_4.json
  - full_data_out_parts/full_data_out_5.json
  - full_data_out_parts/full_data_out_6.json
  - full_data_out_parts/full_data_out_7.json
  - data_out_mini.json
  - data_out_preview.json

--- Dependency 2 ---
id: art_JLcGgqg6OO_T
type: dataset
title: WALS-UD Language Feature Mapping
summary: >-
  Created a curated mapping dataset linking 116 UD treebanks to 5 WALS typological features (1A word order, 20A fusion, 26A
  exponence, 49A case marking, 51A alignment). The dataset achieves 84.5% high-confidence mappings via ISO 639-3 code matching.
  Each mapping includes confidence levels, match methodology, and complete WALS feature values with descriptions. The dataset
  is formatted for mixed-effects modeling of dependency distance distributions across UD treebanks with WALS predictors. Output
  includes full (116 examples), mini (3 examples), and preview versions in experiment pipeline format.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_txhWJXyNIa5t/3_invention_loop/iter_1/gen_art/gen_art_dataset_2
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json
out_dependency_files:
  file_list:
  - data.py
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json
  data_file_paths:
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json
</dependencies>

<instructions>
YOUR ROLE: Write a detailed PLAN for the artifact. A separate executor agent runs the actual artifact later.

You are a PLANNER, not an executor. Your output is a plan that tells the executor what to do and how.
Do NOT execute the artifact itself — a separate agent handles that. Your job is to plan it so well that the executor can follow your plan step by step.

You CAN and SHOULD: search the web, read papers, and explore library docs to make your plan concrete.
You CANNOT run shell commands or scripts — code execution is disabled. Research via web tools only.

Do NOT do the executor's job: don't download datasets, don't implement code, don't run experiments, don't write proofs, don't compute evaluations.

<artifact_executor_scope>
IMPORTANT: Each artifact executor has a focused prompt that guides it to do ONE thing well. It will NOT perform tasks outside its scope — assigning the wrong work to the wrong artifact type wastes an iteration. Match the task to the right executor.

EXPERIMENT executor scope:
  Output: method_out.json with results (metrics, predictions, analysis) — the core computational work
  DOES: Implement and run methods/algorithms, compute metrics, compare approaches, produce quantitative results
  DOES NOT: Collect new datasets (depends on DATASET artifacts for input data), write formal proofs
  This is the right artifact for any code that processes data and produces results
</artifact_executor_scope>

<artifact_planning_rules>
EXPERIMENT: Must depend on at least one DATASET. Define clear metrics and baselines before running. Consider trying multiple method variations rather than a single approach.
</artifact_planning_rules>

<compute_profiles>
Choose the compute profile this artifact needs for execution.
Available profiles for experiment artifacts:
  - gpu: 1x NVIDIA RTX A4500, 20GB VRAM, 7 vCPUs, 29GB RAM — ML training, CUDA, large models (fallback: GPUs cheap→expensive: 2000 Ada → A4000 → 4000 Ada → L4 → 4090 → 5090)
  - cpu_heavy: 4 vCPUs, 32GB RAM — large datasets, memory-intensive processing (fallback: CPUs cheap→expensive, then GPU hosts cheap→expensive (all ≥32GB RAM))

Set runpod_compute_profile to one of these exact tier names.
</compute_profiles>
GOOD PLANS: specific, actionable, consider failure scenarios, build on the suggested approach.
BAD PLANS: vague hand-waving, ignoring the suggested approach, missing critical executor details.
</instructions><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_txhWJXyNIa5t/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_txhWJXyNIa5t/3_invention_loop/iter_2/gen_plan/gen_plan_experiment_1/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "description": "Plan for an EXPERIMENT artifact.",
  "properties": {
    "title": {
      "description": "Plan title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters).",
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Brief summary",
      "title": "Summary",
      "type": "string"
    },
    "runpod_compute_profile": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "cpu_light",
      "description": "Compute tier for execution \u2014 pick from the available profiles list (e.g., 'gpu', 'cpu_heavy', 'cpu_light'). Only used in RunPod mode.",
      "title": "Runpod Compute Profile"
    },
    "implementation_pseudocode": {
      "description": "High-level pseudocode for the experiment implementation",
      "title": "Implementation Pseudocode",
      "type": "string"
    },
    "fallback_plan": {
      "description": "What to do if the primary approach fails - alternative methods, simplified versions",
      "title": "Fallback Plan",
      "type": "string"
    },
    "testing_plan": {
      "description": "How to validate the experiment works: start with small/fast tests, look for confirmation signals before running full-scale experiments",
      "title": "Testing Plan",
      "type": "string"
    }
  },
  "required": [
    "title",
    "implementation_pseudocode",
    "fallback_plan",
    "testing_plan"
  ],
  "title": "ExperimentPlan",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `/ai-inventor/aii_data/runs/run_txhWJXyNIa5t/3_invention_loop/iter_2/gen_plan/gen_plan_experiment_1/.sdk_openhands_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-07-20 01:35:12 UTC

```
Direction: Computational Linguistics — Dependency Distance Minimization Across UD Treebanks. Something genuinely novel and groundbreaking that measures dependency-distance distributions across UD treebanks, investigates whether spoken language minimizes more than written, characterizes how typology interacts with the pattern, and identifies families that deviate. MUST use commul/universal_dependencies on HuggingFace.

Ambition: level 3 of 5 — phenomenological science: surface and rigorously characterize a new empirical regularity or anomaly in the data, even before a full theoretical explanation exists.

Reviewer: I am Kaja Dobrovoljc (JSI / University of Ljubljana). Calibrate from my existing papers. Cross-domain methods (information theory, mixed-effects models, sequence models) welcome — but keep them close to what I already know, not too far from my background.

Submission/Goal: a paper for ACL, EMNLP, or the Computational Linguistics journal. Audience: computational linguists and quantitative typologists. Tone: empirically rigorous, careful with linguistic detail, reproducible on public UD.
```

### [3] SYSTEM-USER prompt · 2026-07-20 01:35:40 UTC

```
<validation-feedback>
Attempt 1 failed validation.

You have not created the output file `.sdk_openhands_agent_struct_out.json` yet. Use the Write tool to create it.

Please use the Write tool to overwrite `.sdk_openhands_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```

### [4] SYSTEM-USER prompt · 2026-07-20 01:35:58 UTC

```
<validation-feedback>
Attempt 2 failed validation.

You have not created the output file `.sdk_openhands_agent_struct_out.json` yet. Use the Write tool to create it.

Please use the Write tool to overwrite `.sdk_openhands_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```

### [5] SKILL-INPUT — aii-web-tools · 2026-07-20 01:36:07 UTC

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
