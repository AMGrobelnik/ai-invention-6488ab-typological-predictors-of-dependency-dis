# gen_art_experiment_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_art`
> Run: `run_txhWJXyNIa5t` — Typological Predictors of Dependency Distance Distribution Shapes in Universal Dependencies
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_experiment_1` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-07-20 01:40:32 UTC

```
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_txhWJXyNIa5t/3_invention_loop/iter_2/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_txhWJXyNIa5t/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_txhWJXyNIa5t/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_txhWJXyNIa5t/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_txhWJXyNIa5t/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_experiment_1_idx1
type: experiment
title: Fit ZA distributions and run mixed-effects models
summary: >-
  Fit Right Truncated Modified Zipf-Alekseev distributions to dependency distance data from 116 UD treebanks with WALS mappings,
  then run mixed-effects models to predict shape parameters from typological features while controlling for language family
  and treebank random effects.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: "STEP 1: Load and merge datasets\n  - Load dependency distance data from art_sbnX8nlSAUFX (full_data_out_parts/*.json)\n\
  \  - Load WALS mappings from art_JLcGgqg6OO_T (full_data_out.json)\n  - Merge on treebank_name field (from metadata_treebank\
  \ in WALS data, treebank_name in DD data)\n  - Filter to treebanks with >1000 dependencies AND complete WALS mappings (target:\
  \ ~116 treebanks)\n  - Extract WALS feature values: 1A (word order: 1=SVO, 2=SOV, 3=VSO, etc.), 20A (fusion), 26A (exponence),\
  \ 49A (cases), 51A (alignment)\n  - Create dummy variables for WALS features (handle NA values appropriately)\n\nSTEP 2:\
  \ ZA distribution fitting for each treebank\n  - For each treebank with >1000 dependencies:\n    a. Extract all dependency\
  \ distances (dd values from 'output' field)\n    b. Create empirical distribution: count frequency of each dd value (1,\
  \ 2, 3, ...)\n    c. Fit Right Truncated Modified Zipf-Alekseev distribution:\n       Formula: P(x) = P(1) * x^(-(a + b*ln(x)))\
  \ for x = 1, 2, ..., L\n       Where L = maximum observed DD in treebank\n       \n       MLE approach:\n       - Negative\
  \ log-likelihood function:\n         def neg_log_lik(params, dd_counts, L):\n             a, b = params\n             x_vals\
  \ = np.arange(1, L+1)\n             # Unnormalized probabilities\n             unnorm_p = x_vals ** (-(a + b * np.log(x_vals)))\n\
  \             # Normalize\n             p = unnorm_p / unnorm_p.sum()\n             # Compute negative log-likelihood\n\
  \             ll = 0\n             for x, count in dd_counts.items():\n                 ll += count * np.log(p[x-1] + 1e-10)\n\
  \             return -ll\n       \n       - Use scipy.optimize.minimize with bounds: a ∈ [-10, 10], b ∈ [-5, 5]\n      \
  \ - Initial values: a=1.0, b=0.0\n       - Extract fitted parameters: a (shape), b (log-modification)\n       - Compute\
  \ goodness-of-fit: Kolmogorov-Smirnov test, AIC\n    \n    d. Store results: treebank_name, a_param, b_param, n_deps, ks_stat,\
  \ p_value\n\nSTEP 3: Spoken vs written analysis (separate from ZA fitting)\n  - Given only 6,239 spoken dependencies (0.6%),\
  \ exclude spoken from ZA fitting\n  - Instead, compute mean DD per treebank for ALL treebanks (including spoken)\n  - Categorize\
  \ genre: spoken (genre contains 'spoken'), written (else)\n  - T-test: compare mean DD between spoken and written treebanks\n\
  \  - Linear regression: mean_dd ~ genre + sentence_length_mean + (1|family)\n  - Report effect size (Cohen's d) and confidence\
  \ intervals\n\nSTEP 4: Mixed-effects models for ZA parameters\n  - Prepare data: one row per treebank with columns:\n  \
  \  [treebank, family, wals_1A, wals_20A, wals_26A, wals_49A, wals_51A, a_param, b_param, mean_sentence_length, n_deps]\n\
  \  \n  - For each WALS feature (1A, 20A, 26A, 49A, 51A):\n    a. Dummy code the feature (convert to categorical with treatment\
  \ coding)\n    b. Fit separate mixed-effects model for a_param:\n       model_a = MixedLM.from_formula(\n           'a_param\
  \ ~ wals_feature + mean_sentence_length',\n           groups = df['family'],  # random intercept for family\n          \
  \ vc_formula = {'treebank': '0 + treebank'}  # random intercept for treebank\n       )\n       OR simpler:\n       model_a\
  \ = MixedLM(\n           endog = df['a_param'],\n           exog = sm.add_constant(df[['wals_feature', 'mean_sentence_length']]),\n\
  \           groups = df['family']\n       )\n       \n    c. Fit separate model for b_param (same structure)\n    d. Extract:\
  \ beta coefficients, SE, t-values, p-values, 95% CI, R² (marginal and conditional)\n    e. Check convergence: model.fit().converged\
  \ should be True\n    f. Report AIC/BIC for model comparison\n  \n  - For significant predictors (p < 0.05), compute effect\
  \ sizes:\n    Cohen's f² = (R²_full - R²_null) / (1 - R²_full)\n\nSTEP 5: Outlier detection via random effects\n  - Extract\
  \ random effect estimates from mixed-effects models:\n    family_effects = model.random_effects\n  - Identify families with\
  \ |random_effect| > 2*SE\n  - For each outlier family:\n    a. List treebanks in that family\n    b. Report mean a_param,\
  \ b_param vs global mean\n    c. Check if outlier status correlates with unmodeled WALS features\n    d. Qualitative investigation:\
  \ why might this family deviate?\n\nSTEP 6: Robustness checks\n  - Subsample analysis: run models on 80% of treebanks (bootstrap,\
  \ 1000 iterations)\n  - Control for treebank size: add log(n_deps) as covariate\n  - Sensitivity to ZA fitting: compare\
  \ with exponential distribution fit\n  - Multiple comparison correction: apply Benjamini-Hochberg FDR to p-values\n\nSTEP\
  \ 7: Output results to method_out.json\n  - Structure:\n    {\n      \"za_fitting_results\": [\n        {\"treebank\": \"\
  en_ewt\", \"a_param\": 1.23, \"b_param\": -0.05, \"n_deps\": 5000, \"ks_p\": 0.34, ...},\n        ...\n      ],\n      \"\
  mixed_effects_results\": {\n        \"a_param_models\": {\n          \"wals_1A\": {\"beta\": [...], \"se\": [...], \"p\"\
  : [...], \"r_squared\": 0.15, ...},\n          ...\n        },\n        \"b_param_models\": {...}\n      },\n      \"spoken_written_comparison\"\
  : {\n        \"t_test\": {\"statistic\": 2.34, \"p\": 0.02, \"cohens_d\": 0.3},\n        \"regression\": {...}\n      },\n\
  \      \"outlier_families\": [\n        {\"family\": \"Austroasiatic\", \"effect\": 1.5, \"se\": 0.4, ...},\n        ...\n\
  \      ],\n      \"robustness\": {...}\n    }"
fallback_plan: |-
  PRIMARY APPROACH FAILURES AND ALTERNATIVES:

  1. IF ZA distribution fitting fails to converge for many treebanks:
     - Alternative: Fit simpler exponential distribution: P(x) = λ * exp(-λ*x)
     - Extract decay parameter λ as shape parameter
     - Compare AIC between ZA and exponential to justify simpler model
     - Use exponential λ for mixed-effects models instead of ZA parameters

  2. IF insufficient treebanks with >1000 deps AND complete WALS mappings:
     - Lower threshold to >500 dependencies
     - Or use all treebanks but weight by sample size in mixed-effects models
     - Alternative: aggregate by language (merge multiple treebanks per language)

  3. IF mixed-effects model fails to converge (singular fit):
     - Simplify random effects structure: remove treebank random effect, keep only family
     - Use linear regression with clustered standard errors (family clusters)
     - Use LME4-style parameterization: start with simpler model, build complexity

  4. IF WALS features have too many missing values:
     - Use only treebanks with complete cases (listwise deletion)
     - Alternative: multiple imputation using mice approach (sklearn IterativeImputer)
     - Or use only the most complete feature (1A word order has best coverage)

  5. IF spoken sample too small for meaningful comparison:
     - Focus analysis on written treebanks only
     - Report descriptive stats for spoken without statistical tests
     - Suggest spoken analysis as limitation for future work

  6. IF statsmodels MixedLM too slow or problematic:
     - Alternative: use pymer4 (Python interface to R lme4)
     - Or use linear regression with fixed effects for family (absorbing family variation)
     - Or use hierarchical Bayesian model via pymc3 (more flexible but slower)

  7. IF ZA parameter estimates are unstable (large SEs):
     - Use binned DD distributions (group distances into bins: 1, 2-3, 4-7, 8+)
     - Fit ZA to binned data for more stable estimates
     - Or use method of moments estimators instead of MLE
testing_plan: |-
  TESTING STRATEGY: Gradual scaling from mini to full data

  PHASE 1: Unit tests on mini data (expected time: 15 min)
    - Test data loading: load data_out_mini.json (3 examples), verify structure
    - Test ZA fitting on synthetic data:
      a. Generate synthetic DD data from known ZA distribution (a=1.0, b=0.0)
      b. Fit ZA distribution to synthetic data
      c. Verify recovered parameters within 10% of true values
    - Test WALS mapping merge: merge mini DD data with mini WALS data
    - Test mixed-effects model on 5 treebanks with synthetic ZA parameters
    - Verify method_out.json structure matches schema

  PHASE 2: Scale to preview data (expected time: 30 min)
    - Load data_out_preview.json (100 examples)
    - Fit ZA distributions to treebanks in preview set
    - Run mixed-effects models with subset of WALS features
    - Verify convergence and reasonable parameter estimates
    - Check that spoken/written comparison runs without errors

  PHASE 3: Run on full data (expected time: 2-3 hours)
    - Load all 7 parts of full_data_out_*.json (979,098 observations)
    - Fit ZA distributions to all eligible treebanks (~116 target)
    - Run full mixed-effects models for all WALS features
    - Generate all output tables and figures
    - Validate results:
      a. ZA fitting: check that KS test p-values > 0.05 for good fits
      b. Mixed models: check convergence, no singular fits
      c. Outliers: verify random effects sum to ~0
      d. Spoken-written: check effect direction matches hypothesis (spoken should have longer DD)

  VALIDATION CHECKPOINTS:
    - After data loading: print treebank counts, WALS coverage stats
    - After ZA fitting: print convergence rate, parameter distributions (histogram)
    - After mixed models: print model summaries, check significant predictors
    - Before final output: validate method_out.json against schema using aii-json skill

  ERROR HANDLING:
    - If ZA fitting fails for a treebank: log warning, skip that treebank, continue
    - If mixed model doesn't converge: try simpler model, log warning
    - If merge produces 0 rows: check treebank name formats match between datasets
    - Save intermediate results after each step (checkpointing for long runs)
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

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

Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</dependencies>

<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>

<skills>
Skills are self-contained capabilities with instructions, context, and tools.

- aii-web-tools: Web search (Serper), page/PDF fetch as markdown, regex grep over page/PDF text
- aii-semscholar-bib: Batch-fetch BibTeX from Semantic Scholar
- aii-openrouter-llms: Search and call 300+ LLMs via OpenRouter
- aii-hf-datasets: Search, preview, download HuggingFace datasets
- aii-owid-datasets: Search and load Our World in Data tables
- aii-lean: Compile/verify Lean 4 code, Mathlib search, tactic suggestions
- aii-image-gen: Generate/edit images via Gemini 3 Pro Image (Nano Banana Pro)
- aii-json: Validate JSON against schemas, generate mini/preview variants
- aii-paper-writing: Academic paper structure, bibliography, citations
- aii-paper-to-latex: Assemble LaTeX papers and compile to PDF
- aii-parallel-computing: GPU acceleration, CPU parallelism, async I/O
- aii-python: Python coding standards for experiment scripts
- aii-use-hardware: Detect CPU/RAM/GPU, memory-safe processing
- aii-long-running-tasks: Gradual scaling pattern for long-running tasks
- aii-colab: Google Colab runtime constraints for notebooks
- aii-file-size-limit: Check and split oversized output files
</skills>
</available_resources>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for framework choices, implementation patterns, agent orchestration.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-python, aii-long-running-tasks, aii-json, aii-file-size-limit, aii-use-hardware, aii-parallel-computing.
TODO 2. Read preview files from dependencies to understand data structure. Use ALL datasets provided — do not skip or select a subset. Read domain handbook if applicable (see <available_domain_handbooks>). Test basic functionality with 'uv run'.
TODO 3. Fully implement our method AND baseline (comparison) as described in artifact plan in './method.py'. Use exp_gen_sol_out.json schema in aii-json skill for output format validation. Include everything specified in the artifact plan, but you may also implement additional relevant methods or analysis beyond what's listed. Be very attentive to meticulously and exhaustively fix any errors in your code.
</todos>
```

### [2] HUMAN-USER prompt · 2026-07-20 01:40:32 UTC

```
Direction: Computational Linguistics — Dependency Distance Minimization Across UD Treebanks. Something genuinely novel and groundbreaking that measures dependency-distance distributions across UD treebanks, investigates whether spoken language minimizes more than written, characterizes how typology interacts with the pattern, and identifies families that deviate. MUST use commul/universal_dependencies on HuggingFace.

Ambition: level 3 of 5 — phenomenological science: surface and rigorously characterize a new empirical regularity or anomaly in the data, even before a full theoretical explanation exists.

Reviewer: I am Kaja Dobrovoljc (JSI / University of Ljubljana). Calibrate from my existing papers. Cross-domain methods (information theory, mixed-effects models, sequence models) welcome — but keep them close to what I already know, not too far from my background.

Submission/Goal: a paper for ACL, EMNLP, or the Computational Linguistics journal. Audience: computational linguists and quantitative typologists. Tone: empirically rigorous, careful with linguistic detail, reproducible on public UD.
```

### [3] SKILL-INPUT — aii-python · 2026-07-20 01:40:58 UTC

The agent loaded the **aii-python** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-python
description: Python coding standards for experiment and evaluation scripts. Covers environment setup, logging, error handling, and code structure.
---

## Environment Setup

- Python 3.12+
- **NEVER use `pip` or `.venv/bin/pip`** — they are not installed. Use `uv` for ALL package operations:
  ```bash
  uv venv .venv --python=3.12
  source .venv/bin/activate  # or: .venv/bin/python script.py
  uv pip install pandas loguru  # NOT: pip install
  ```
- Create `.toml` file with dependencies, create uv `.venv` and activate it
- NO inline dependencies (no `# /// script` headers)

## Logging

Use `loguru` for all logging. Add a file sink alongside stdout.

```python
from loguru import logger
import sys

logger.remove()  # Remove default handler
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")
```

Rules:
- Log every major step (data loading, processing start/end, results)
- If applicable, log every LLM API call input and output
- Truncate long outputs in logs (add truncation logic for potentially large strings)
- Use `logger.error()` in except blocks (traceback auto-captured)

## Error Handling

- Wrap major operations in try/except blocks
- Use `@logger.catch(reraise=True)` decorator on main functions — without `reraise=True`, the script exits 0 even on uncaught exceptions, hiding failures from downstream consumers
- Use explicit exception types, not bare `except:`
- Never silently swallow exceptions — always log them

```python
@logger.catch(reraise=True)
def main():
    try:
        data = load_data(path)
    except FileNotFoundError:
        logger.error("Data file not found")
        raise
    except json.JSONDecodeError:
        logger.error("Invalid JSON in data file")
        raise
```

## Code Structure

- Use `pathlib.Path` for file operations: `Path("data/input.json").read_text()` not `open(...).read()`
- Use type hints for function signatures
- Use keyword arguments for functions with more than 4 parameters
- No hardcoded paths — derive from script location or accept as arguments

## Script Pattern

Standard pattern for experiment/evaluation scripts:

```python
#!/usr/bin/env python3
"""Brief description of what this script does."""

from loguru import logger
from pathlib import Path
import json
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def main():
    # Load data
    data_path = Path("full_data_out.json")
    logger.info(f"Loading data from {data_path}")
    data = json.loads(data_path.read_text())
    logger.info(f"Loaded {len(data['examples'])} examples")

    # Process
    results = []
    for i, example in enumerate(data["examples"]):
        try:
            result = process(example)
            results.append(result)
        except Exception:
            logger.error(f"Failed on example {i}")
            continue

    # Save output
    output = {"examples": results}
    Path("method_out.json").write_text(json.dumps(output, indent=2))
    logger.info(f"Saved {len(results)} results")

if __name__ == "__main__":
    main()
```
````

### [4] SKILL-INPUT — aii-long-running-tasks · 2026-07-20 01:40:58 UTC

The agent loaded the **aii-long-running-tasks** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-long-running-tasks
description: Gradual scaling pattern for long-running autonomous tasks. Use when running experiments, evaluations, or any code that processes data at increasing scale with runtime checks.
---

## Core Principles

1. **Time budget first**: Read your time/runtime constraints before running anything. Set every Bash timeout to fit within the budget.
2. **Start small, scale up**: Run on minimal input first, fix errors, then increase scale.
3. **Extrapolate before scaling**: Use recorded runtimes to predict whether the next step fits in the budget. Don't guess — calculate.
4. **Background execution**: For anything that takes >1 min, run in background (`run_in_background=true`) and do useful work while waiting.
5. **Stop early if needed**: Quality results on less data beats a timeout or crash. It's always acceptable to stop at a smaller scale.

---

## Gradual Scaling Sequence

Run code at increasing data sizes, checking runtime at each step.

Substitute your actual file names:
- `{mini_file}` — mini JSON (3 examples) from dependency workspace
- `{full_file}` — full dataset from dependency workspace
- `{script}` — your processing script (e.g., `./method.py`, `./eval.py`)
- `{schema}` — JSON schema to validate output against

**STEP 1 — MINI DATA:** Run `{script}` on `{mini_file}`. Do NOT truncate logs. Fix all errors. Validate output against `{schema}`. Verify you are NOT using mock scripts, mock data, or mock APIs.

**STEP 2 — 10 EXAMPLES:** Modify `{script}` to load only the first 10 examples from `{full_file}`. Run and fix errors. Validate schema. Record the runtime.

**STEP 3 — 50 EXAMPLES:** Load first 50 examples from `{full_file}`. Run and fix errors. Record runtime. **EXTRAPOLATE**: Using runtimes from steps 2-3, estimate time per example. Calculate how many examples fit in your remaining time budget. If 50 already used most of the budget, stop here.

**STEP 4 — 100 EXAMPLES (if budget allows):** Load first 100 examples. Run and fix errors. Record runtime. Re-extrapolate with the new data point.

**STEP 5 — 200 EXAMPLES (if budget allows):** Load first 200 examples from `{full_file}`. Run and fix errors. Record runtime.

**STEP 6 — MAXIMIZE:** Using all recorded runtimes, extrapolate time-per-example (it may not be perfectly linear — account for overhead). Calculate the maximum number of examples that fits within your remaining time budget with a 10% safety margin. Load that many (or all if they fit). Run and validate.

## Final Testing Phase

After completing the scaling sequence, redo the entire sequence **one more time** up to your final example count:

mini → 10 → 50 → 100 → 200 → max

At each scale: look for issues, fix problems, validate output, ensure it completes within time limits.

---

## Background Execution

For any step that takes >1 min, run as a **background task**:

1. Launch with Bash `run_in_background=true`
2. While it runs, use the time productively:
   - Sanity-check previous outputs
   - Verify file integrity (correct field names, non-empty values)
   - Review code for edge cases at larger scale
   - Prepare the next step
3. Check back on the background task to get results
4. If it failed, fix errors and re-run

---

## Resource Limits

Set hard RAM and CPU time limits so code fails fast instead of crashing the system. Read limits from `<hardware>` and leave headroom for the OS (e.g., if 16GB total, cap at 14GB).

Python example using stdlib `resource` module:
```python
import resource
resource.setrlimit(resource.RLIMIT_AS, (14 * 1024**3, 14 * 1024**3))  # 14GB RAM
resource.setrlimit(resource.RLIMIT_CPU, (3600, 3600))  # 1 hour CPU time
```
Exceeding RAM raises `MemoryError`. Exceeding CPU time sends `SIGKILL`.

## Monitoring

At each step, record runtime AND check resource usage (`free -h` for RAM, `top -bn1 | head -5` for CPU). If memory usage is climbing toward the limit or CPU is pegged, stop and investigate before scaling further.
````

### [5] SKILL-INPUT — aii-json · 2026-07-20 01:40:58 UTC

The agent loaded the **aii-json** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-json
description: JSON validation and formatting toolkit. Validate JSON files against schemas for experiment pipelines, and generate full/mini/preview versions of JSON datasets. Use for validating pipeline outputs, checking schema compliance, or creating size-optimized JSON variants.
---

## Contents

- Validating JSON (schema validation against experiment schemas)
- Formatting JSON (generate full/mini/preview versions)

**IMPORTANT - Parallel execution:** GNU `parallel` subshells do NOT inherit `source activate`. Use `export` for variables and **single-quoted** command templates so parallel's subshells can resolve them:
```
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

---

## Validating JSON

Validate JSON files against predefined schemas for experiment-based hypothesis selection, data collection, solution generation, and evaluation.

### Quick Start

1. Read the schema spec you need to adhere to (e.g., `schemas/exp_eval_sol_out.json`)
2. Create your output file following that schema structure
3. Validate:

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /path/to/eval_out.json
```

### Script: aii_json_validate_schema.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /tmp/eval_out.json
```

**Parallel execution (multiple validations):**

IMPORTANT: When validating multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_validate_schema.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --format {1} --file {2}' ::: 'exp_sel_data_out' 'exp_gen_sol_out' 'exp_eval_sol_out' :::+ '/tmp/full_data_out.json' '/tmp/method_out.json' '/tmp/eval_out.json'
```

**Example output (success):**
```
Validating: aii_json_validate_schema.py
Format: exp_eval_sol_out

✓ Validation PASSED
```

**Example output (failure):**
```
Validating: aii_json_validate_schema.py
Format: exp_sel_data_out

✗ Validation FAILED

Errors:
  Path: datasets → 0 → examples → 0
  Error: 'output' is a required property
  Validator: required
```

**Parameters:**

`--format` (required)
- Format type to validate against
- Determines which schema to use

`--file` (required)
- Path to JSON file to validate
- Must be valid JSON
- **Always pass an absolute path.** Relative paths resolve from the
  ability server's CWD (typically ``/ai-inventor/aii_server``), not from
  your agent workspace, so ``data_out/x.json`` will silently look in the
  wrong directory and fail with "Could not load JSON file". The validate
  endpoint also accepts a ``workspace_dir`` arg if you need to keep a
  relative path — pass your workspace path there.

**Tips:**
- Fix errors in your JSON and rerun validation until it passes

### Schema Files

Schemas are stored in `.claude/skills/aii-json/schemas/`:

**Hypothesis Selection & Evaluation:**
- `sel_hypo_out.json` - Hypothesis Selection output (all hypotheses with selected flags)
- `feasibility_eval_all.json` - All hypotheses with feasibility scores
- `feasibility_eval_top.json` - Top 5 most feasible hypotheses
- `novelty_research_one.json` - Single hypothesis novelty research arguments with citations
- `novelty_eval_all.json` - All hypotheses with novelty scores
- `novelty_eval_top.json` - Single best selected hypothesis

**Experiment Pipeline:**
- `exp_sel_data_out.json` - Experiment Data Selection format
- `exp_gen_sol_out.json` - Experiment Solution Generation format
- `exp_eval_sol_out.json` - Experiment Solution Evaluation format

---

## Formatting JSON

Generate three size-optimized versions of a JSON file for efficient development and preview:
- **full**: Identical to original (all data)
- **mini**: First 3 items only (for quick testing)
- **preview**: Mini + all strings truncated to 200 chars (for quick inspection)

### Quick Start

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

### Script: aii_json_format_mini_preview.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

**Parallel execution (multiple files):**

IMPORTANT: When formatting multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_format_mini_preview.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --input {}' ::: 'full_data_out.json' 'method_out.json' 'eval_out.json'
```

**Example output:**
```
Generated 3 versions:
  Full (50 items): /path/to/full_method_out.json
  Mini (3 items): /path/to/mini_method_out.json
  Preview (3 items, truncated): /path/to/preview_method_out.json
```

**Parameters:**

`--input` (required)
- Path to input JSON file
- Must have a top-level array
- Example: `method_out.json`, `full_data_out.json`

`--output-dir` (optional)
- Output directory for generated files
- Default: same directory as input file
- Files are prefixed with `full_`, `mini_`, `preview_`

**Output Files:**

All three files use the same base name with different prefixes:
- `full_{basename}.json` - Complete dataset (identical to original)
- `mini_{basename}.json` - First 3 array items only
- `preview_{basename}.json` - First 3 items with strings truncated to 200 chars

**Tips:**
- Input JSON must have a top-level array structure
- String truncation is recursive (applies to nested objects and arrays)
- Use preview files for quick inspection without reading large datasets
- Use mini files for developing/testing code before running on full dataset

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [6] SKILL-INPUT — aii-file-size-limit · 2026-07-20 01:41:02 UTC

The agent loaded the **aii-file-size-limit** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

```
---
name: aii-file-size-limit
description: File size check procedure for splitting oversized output files. Use after generating JSON output files to check and split files exceeding the provided size limit.
---

## File Size Check

After generating output files, run `ls -lh` to check sizes. If ANY file exceeds the provided file size limit:

1. Create directory with same base name (e.g., `data_out/` for `full_data_out.json`)
2. Split into parts under the limit named: `full_data_out_1.json`, `full_data_out_2.json`, etc.
3. Place parts in directory (e.g., `data_out/full_data_out_1.json`, `data_out/full_data_out_2.json`)
4. Delete the original oversized file
5. Update the script to read from split files: `for f in sorted(glob.glob('data_out/full_data_out_*.json')): data.extend(json.load(open(f)))`
6. For each split part, generate its own mini/preview versions with the json skill's format script
```

### [7] SKILL-INPUT — aii-use-hardware · 2026-07-20 01:41:02 UTC

The agent loaded the **aii-use-hardware** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-use-hardware
description: Detect hardware and use it responsibly. Covers CPU/RAM/GPU detection, memory-safe data processing, and resource-aware computation.
---

**Step 1** — Run `bash scripts/get_hardware.sh` (relative to this skill's directory).

Read the `=== CGROUP ===` section carefully. If `Type: cgroup v1` or `cgroup v2`:
- You are in a **container with hard resource limits**. Exceeding them = OOM kill, no recovery.
- **Never** use `psutil.virtual_memory().total`, `free -h`, `/proc/meminfo`, `os.cpu_count()`, or `nproc` for resource limits — these report **host** values, not your container's allocation.
- **Always** read limits from the cgroup paths shown in the output, or use the Python helpers below.
- For **runtime memory monitoring**, read current usage from cgroup too:
  - v2: `/sys/fs/cgroup/memory.current`
  - v1: `/sys/fs/cgroup/memory/memory.usage_in_bytes`

**Step 2** — Use Step 1 results to pick package variants **before** installing.

Defaults often target the most powerful environment — PyPI's `torch` ships with CUDA libs even on CPU-only hosts. Wrong variant = wasted disk, slow setup, possible import-time failures.

If `=== GPU ===` shows `No GPU`, install torch's CPU build (skips ~4.5GB of CUDA libs):
```bash
uv pip install torch --extra-index-url https://download.pytorch.org/whl/cpu
```
Same idea for any library whose wheel selection depends on detected hardware (GPU/CPU-only builds, architecture-specific wheels).

After install, sanity-check imports right away (`python -c "import torch"`). Disk-pressure or interrupted installs leave half-built wheels (e.g. `libtorch_global_deps.so` missing) — catch these before the experiment runs.

**Step 3** — Set Python constants from the Step 1 results:
```python
import os, math, torch, psutil
from pathlib import Path

def _detect_cpus() -> int:
    """Detect actual CPU allocation (containers/pods/bare metal)."""
    try:  # cgroups v2 quota
        parts = Path("/sys/fs/cgroup/cpu.max").read_text().split()
        if parts[0] != "max":
            return math.ceil(int(parts[0]) / int(parts[1]))
    except (FileNotFoundError, ValueError): pass
    try:  # cgroups v1 quota
        q = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_quota_us").read_text())
        p = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_period_us").read_text())
        if q > 0:
            return math.ceil(q / p)
    except (FileNotFoundError, ValueError): pass
    try:  # CPU affinity (cpuset — used by RunPod, Docker --cpuset-cpus)
        return len(os.sched_getaffinity(0))
    except (AttributeError, OSError): pass
    return os.cpu_count() or 1

def _container_ram_gb() -> float | None:
    """Read RAM limit from cgroup (containers/pods)."""
    for p in ["/sys/fs/cgroup/memory.max", "/sys/fs/cgroup/memory/memory.limit_in_bytes"]:
        try:
            v = Path(p).read_text().strip()
            if v != "max" and int(v) < 1_000_000_000_000:
                return int(v) / 1e9
        except (FileNotFoundError, ValueError): pass
    return None

NUM_CPUS = _detect_cpus()
HAS_GPU = torch.cuda.is_available()
VRAM_GB = torch.cuda.get_device_properties(0).total_mem / 1e9 if HAS_GPU else 0
DEVICE = torch.device("cuda" if HAS_GPU else "cpu")
TOTAL_RAM_GB = _container_ram_gb() or psutil.virtual_memory().total / 1e9
AVAILABLE_RAM_GB = min(psutil.virtual_memory().available / 1e9, TOTAL_RAM_GB)
```

## Step 4 — Set Memory Limits

OOM kills the entire container. **Every script MUST set RAM and VRAM limits at startup.**

Decide the budget based on what the script actually needs. Estimate data size × 2-5x for in-memory overhead, then add ~50% breathing room for temporaries. You may use up to 90% of available RAM/VRAM, but **scale gradually** — start small (e.g. 30-50%), verify it works, then increase toward the limit. Never exceed 90% to keep a buffer for the OS, system processes, and the agent runtime itself. Going over crashes the container/machine with no recovery.

```python
import resource, psutil

_avail = psutil.virtual_memory().available
RAM_BUDGET = ???  # YOU decide: estimate what this script needs (in bytes)
assert RAM_BUDGET < _avail, f"Budget {RAM_BUDGET/1e9:.1f}GB > available {_avail/1e9:.1f}GB"
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET * 3, RAM_BUDGET * 3))  # 3x: virtual > RSS; raises MemoryError on exceed

if HAS_GPU:
    _free, _total = torch.cuda.mem_get_info(0)
    VRAM_BUDGET = ???  # YOU decide: estimate GPU memory needs
    torch.cuda.set_per_process_memory_fraction(min(VRAM_BUDGET / _total, 0.95))  # raises OutOfMemoryError on exceed
```

## Memory-Safe Data Processing

- **One at a time**: load one large object → process → `del obj; gc.collect()` → next
- **Load only what you need**: select specific tables/columns/rows, not entire databases
- **Test small first**: run on a sample before scaling to full data to estimate memory/time
- **Free intermediates in loops**: don't accumulate large results — aggregate incrementally
- **Size before loading**: check file/dataset size before loading; if it's >30% of `RAM_BUDGET`, chunk it

## Common Mistakes (from real crashes)

- **Skipping this skill entirely** — loading data with no RAM detection, no limits, no budget. Container OOM-killed, all agents lost.
- **Using `psutil.virtual_memory().total` instead of `_container_ram_gb()`** — reports host RAM (e.g. 66 GB) when container limit is 28 GB. You MUST use the cgroup-aware functions above.
- **Loading all tables from a multi-table database at once** — one agent loaded 14 RelBench tables simultaneously, spiked past container limit.
- **Setting no memory limits** — without `resource.setrlimit` (RAM) and `set_per_process_memory_fraction` (VRAM), a runaway script OOM-kills the container instead of raising a catchable error.
- **Using `os.cpu_count()` directly** — returns host CPUs (e.g. 192) instead of container limit (e.g. 4) on RunPod/Docker. Always use `_detect_cpus()` above which checks cgroup quota → CPU affinity → `os.cpu_count()` in order.

## Hardware Use

- Keep these results in mind for ALL subsequent tasks — don't assume more than detected
- GPU if available and parallelizable, multiprocessing if multiple CPUs
- Push available resources to their full potential — don't leave hardware idle
````

### [8] SKILL-INPUT — aii-parallel-computing · 2026-07-20 01:41:02 UTC

The agent loaded the **aii-parallel-computing** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-parallel-computing
description: "CRITICAL PERFORMANCE SKILL. Maximize hardware utilization for compute-intensive tasks. Covers GPU acceleration, CPU parallelism, and async I/O. The difference between hours of failure and minutes of success. Use whenever writing ANY script that processes data, makes API calls, or does computation."
---

**ALWAYS parallelize. Sequential processing is unacceptable for any non-trivial workload.** A sequential script doing 1000 API calls takes hours and fails halfway. An async version finishes in minutes with proper error handling. ALWAYS ask: "Can this run in parallel?" — the answer is almost always yes.

Read aii-use-hardware skill first → get `NUM_CPUS`, `HAS_GPU`, `VRAM_GB`, `device`. Set `NUM_WORKERS` proportional to available CPU capacity — check `psutil.cpu_percent(interval=1)` and scale accordingly (e.g. 30% used → use ~70% of cores).

## Decision Tree (follow strictly)

- **I/O-bound** (API calls, downloads, web, file reads) → `asyncio` + `aiohttp` with `Semaphore(NUM_WORKERS * 4)`. NEVER do sequential HTTP requests in a loop.
- **CPU-bound, vectorizable** → GPU available: PyTorch on device / No GPU: NumPy vectorized ops. NEVER loop over array elements in Python.
- **CPU-bound, independent items** → `ProcessPoolExecutor(max_workers=NUM_WORKERS)`. NEVER process items one-by-one when they're independent.
- **Sequential** → only acceptable when items have data dependencies (each depends on the previous result).

## GPU Rules

- Use up to 90% of available VRAM — scale gradually (start small, increase after each successful run, keep 10% buffer)
- Move to device → compute → move back: `torch.tensor(data, device=device)` → `.cpu().numpy()`
- OOM fallback: catch `torch.cuda.OutOfMemoryError` → `empty_cache()` → halve batch size → retry on GPU. Keep reducing until it fits. Stay on GPU.
- Batch large data: chunk it, `del batch` between iterations to free VRAM

## Parallelism Rules

- **CPU-bound**: `ProcessPoolExecutor` + `as_completed`, pre-allocate result list indexed by submission order
- **I/O-bound**: `asyncio` + `aiohttp`, `Semaphore(NUM_WORKERS * 4)`, single shared `ClientSession`, `asyncio.gather(*tasks, return_exceptions=True)`
- Always add `tenacity` retries for transient failures, always set timeouts on HTTP requests
- **CRITICAL — `ProcessPoolExecutor` start method**: Default `fork` deadlocks with loguru (and any threading library). ALWAYS pass `mp_context=multiprocessing.get_context("spawn")` when constructing `ProcessPoolExecutor` in any script that uses loguru, threading, or async I/O. Example:
  ```python
  import multiprocessing as mp
  from concurrent.futures import ProcessPoolExecutor
  with ProcessPoolExecutor(max_workers=N, mp_context=mp.get_context("spawn")) as pool:
      ...
  ```
````

### [9] SYSTEM-USER prompt · 2026-07-20 01:52:44 UTC

```
YOUR PREVIOUS SESSION WAS INTERRUPTED: A single operation exceeded the 720s message timeout. Each individual operation must complete within 720s. Do NOT mock, skip, or compromise your execution — still do the real work. Try to make operations run faster if possible. If a command genuinely takes longer than 720s, split it into sequential parts that each complete within the time limit.

CONTINUE FOLLOWING THESE INSTRUCTIONS:

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_txhWJXyNIa5t/3_invention_loop/iter_2/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_txhWJXyNIa5t/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_txhWJXyNIa5t/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_txhWJXyNIa5t/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_txhWJXyNIa5t/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_experiment_1_idx1
type: experiment
title: Fit ZA distributions and run mixed-effects models
summary: >-
  Fit Right Truncated Modified Zipf-Alekseev distributions to dependency distance data from 116 UD treebanks with WALS mappings,
  then run mixed-effects models to predict shape parameters from typological features while controlling for language family
  and treebank random effects.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: "STEP 1: Load and merge datasets\n  - Load dependency distance data from art_sbnX8nlSAUFX (full_data_out_parts/*.json)\n\
  \  - Load WALS mappings from art_JLcGgqg6OO_T (full_data_out.json)\n  - Merge on treebank_name field (from metadata_treebank\
  \ in WALS data, treebank_name in DD data)\n  - Filter to treebanks with >1000 dependencies AND complete WALS mappings (target:\
  \ ~116 treebanks)\n  - Extract WALS feature values: 1A (word order: 1=SVO, 2=SOV, 3=VSO, etc.), 20A (fusion), 26A (exponence),\
  \ 49A (cases), 51A (alignment)\n  - Create dummy variables for WALS features (handle NA values appropriately)\n\nSTEP 2:\
  \ ZA distribution fitting for each treebank\n  - For each treebank with >1000 dependencies:\n    a. Extract all dependency\
  \ distances (dd values from 'output' field)\n    b. Create empirical distribution: count frequency of each dd value (1,\
  \ 2, 3, ...)\n    c. Fit Right Truncated Modified Zipf-Alekseev distribution:\n       Formula: P(x) = P(1) * x^(-(a + b*ln(x)))\
  \ for x = 1, 2, ..., L\n       Where L = maximum observed DD in treebank\n       \n       MLE approach:\n       - Negative\
  \ log-likelihood function:\n         def neg_log_lik(params, dd_counts, L):\n             a, b = params\n             x_vals\
  \ = np.arange(1, L+1)\n             # Unnormalized probabilities\n             unnorm_p = x_vals ** (-(a + b * np.log(x_vals)))\n\
  \             # Normalize\n             p = unnorm_p / unnorm_p.sum()\n             # Compute negative log-likelihood\n\
  \             ll = 0\n             for x, count in dd_counts.items():\n                 ll += count * np.log(p[x-1] + 1e-10)\n\
  \             return -ll\n       \n       - Use scipy.optimize.minimize with bounds: a ∈ [-10, 10], b ∈ [-5, 5]\n      \
  \ - Initial values: a=1.0, b=0.0\n       - Extract fitted parameters: a (shape), b (log-modification)\n       - Compute\
  \ goodness-of-fit: Kolmogorov-Smirnov test, AIC\n    \n    d. Store results: treebank_name, a_param, b_param, n_deps, ks_stat,\
  \ p_value\n\nSTEP 3: Spoken vs written analysis (separate from ZA fitting)\n  - Given only 6,239 spoken dependencies (0.6%),\
  \ exclude spoken from ZA fitting\n  - Instead, compute mean DD per treebank for ALL treebanks (including spoken)\n  - Categorize\
  \ genre: spoken (genre contains 'spoken'), written (else)\n  - T-test: compare mean DD between spoken and written treebanks\n\
  \  - Linear regression: mean_dd ~ genre + sentence_length_mean + (1|family)\n  - Report effect size (Cohen's d) and confidence\
  \ intervals\n\nSTEP 4: Mixed-effects models for ZA parameters\n  - Prepare data: one row per treebank with columns:\n  \
  \  [treebank, family, wals_1A, wals_20A, wals_26A, wals_49A, wals_51A, a_param, b_param, mean_sentence_length, n_deps]\n\
  \  \n  - For each WALS feature (1A, 20A, 26A, 49A, 51A):\n    a. Dummy code the feature (convert to categorical with treatment\
  \ coding)\n    b. Fit separate mixed-effects model for a_param:\n       model_a = MixedLM.from_formula(\n           'a_param\
  \ ~ wals_feature + mean_sentence_length',\n           groups = df['family'],  # random intercept for family\n          \
  \ vc_formula = {'treebank': '0 + treebank'}  # random intercept for treebank\n       )\n       OR simpler:\n       model_a\
  \ = MixedLM(\n           endog = df['a_param'],\n           exog = sm.add_constant(df[['wals_feature', 'mean_sentence_length']]),\n\
  \           groups = df['family']\n       )\n       \n    c. Fit separate model for b_param (same structure)\n    d. Extract:\
  \ beta coefficients, SE, t-values, p-values, 95% CI, R² (marginal and conditional)\n    e. Check convergence: model.fit().converged\
  \ should be True\n    f. Report AIC/BIC for model comparison\n  \n  - For significant predictors (p < 0.05), compute effect\
  \ sizes:\n    Cohen's f² = (R²_full - R²_null) / (1 - R²_full)\n\nSTEP 5: Outlier detection via random effects\n  - Extract\
  \ random effect estimates from mixed-effects models:\n    family_effects = model.random_effects\n  - Identify families with\
  \ |random_effect| > 2*SE\n  - For each outlier family:\n    a. List treebanks in that family\n    b. Report mean a_param,\
  \ b_param vs global mean\n    c. Check if outlier status correlates with unmodeled WALS features\n    d. Qualitative investigation:\
  \ why might this family deviate?\n\nSTEP 6: Robustness checks\n  - Subsample analysis: run models on 80% of treebanks (bootstrap,\
  \ 1000 iterations)\n  - Control for treebank size: add log(n_deps) as covariate\n  - Sensitivity to ZA fitting: compare\
  \ with exponential distribution fit\n  - Multiple comparison correction: apply Benjamini-Hochberg FDR to p-values\n\nSTEP\
  \ 7: Output results to method_out.json\n  - Structure:\n    {\n      \"za_fitting_results\": [\n        {\"treebank\": \"\
  en_ewt\", \"a_param\": 1.23, \"b_param\": -0.05, \"n_deps\": 5000, \"ks_p\": 0.34, ...},\n        ...\n      ],\n      \"\
  mixed_effects_results\": {\n        \"a_param_models\": {\n          \"wals_1A\": {\"beta\": [...], \"se\": [...], \"p\"\
  : [...], \"r_squared\": 0.15, ...},\n          ...\n        },\n        \"b_param_models\": {...}\n      },\n      \"spoken_written_comparison\"\
  : {\n        \"t_test\": {\"statistic\": 2.34, \"p\": 0.02, \"cohens_d\": 0.3},\n        \"regression\": {...}\n      },\n\
  \      \"outlier_families\": [\n        {\"family\": \"Austroasiatic\", \"effect\": 1.5, \"se\": 0.4, ...},\n        ...\n\
  \      ],\n      \"robustness\": {...}\n    }"
fallback_plan: |-
  PRIMARY APPROACH FAILURES AND ALTERNATIVES:

  1. IF ZA distribution fitting fails to converge for many treebanks:
     - Alternative: Fit simpler exponential distribution: P(x) = λ * exp(-λ*x)
     - Extract decay parameter λ as shape parameter
     - Compare AIC between ZA and exponential to justify simpler model
     - Use exponential λ for mixed-effects models instead of ZA parameters

  2. IF insufficient treebanks with >1000 deps AND complete WALS mappings:
     - Lower threshold to >500 dependencies
     - Or use all treebanks but weight by sample size in mixed-effects models
     - Alternative: aggregate by language (merge multiple treebanks per language)

  3. IF mixed-effects model fails to converge (singular fit):
     - Simplify random effects structure: remove treebank random effect, keep only family
     - Use linear regression with clustered standard errors (family clusters)
     - Use LME4-style parameterization: start with simpler model, build complexity

  4. IF WALS features have too many missing values:
     - Use only treebanks with complete cases (listwise deletion)
     - Alternative: multiple imputation using mice approach (sklearn IterativeImputer)
     - Or use only the most complete feature (1A word order has best coverage)

  5. IF spoken sample too small for meaningful comparison:
     - Focus analysis on written treebanks only
     - Report descriptive stats for spoken without statistical tests
     - Suggest spoken analysis as limitation for future work

  6. IF statsmodels MixedLM too slow or problematic:
     - Alternative: use pymer4 (Python interface to R lme4)
     - Or use linear regression with fixed effects for family (absorbing family variation)
     - Or use hierarchical Bayesian model via pymc3 (more flexible but slower)

  7. IF ZA parameter estimates are unstable (large SEs):
     - Use binned DD distributions (group distances into bins: 1, 2-3, 4-7, 8+)
     - Fit ZA to binned data for more stable estimates
     - Or use method of moments estimators instead of MLE
testing_plan: |-
  TESTING STRATEGY: Gradual scaling from mini to full data

  PHASE 1: Unit tests on mini data (expected time: 15 min)
    - Test data loading: load data_out_mini.json (3 examples), verify structure
    - Test ZA fitting on synthetic data:
      a. Generate synthetic DD data from known ZA distribution (a=1.0, b=0.0)
      b. Fit ZA distribution to synthetic data
      c. Verify recovered parameters within 10% of true values
    - Test WALS mapping merge: merge mini DD data with mini WALS data
    - Test mixed-effects model on 5 treebanks with synthetic ZA parameters
    - Verify method_out.json structure matches schema

  PHASE 2: Scale to preview data (expected time: 30 min)
    - Load data_out_preview.json (100 examples)
    - Fit ZA distributions to treebanks in preview set
    - Run mixed-effects models with subset of WALS features
    - Verify convergence and reasonable parameter estimates
    - Check that spoken/written comparison runs without errors

  PHASE 3: Run on full data (expected time: 2-3 hours)
    - Load all 7 parts of full_data_out_*.json (979,098 observations)
    - Fit ZA distributions to all eligible treebanks (~116 target)
    - Run full mixed-effects models for all WALS features
    - Generate all output tables and figures
    - Validate results:
      a. ZA fitting: check that KS test p-values > 0.05 for good fits
      b. Mixed models: check convergence, no singular fits
      c. Outliers: verify random effects sum to ~0
      d. Spoken-written: check effect direction matches hypothesis (spoken should have longer DD)

  VALIDATION CHECKPOINTS:
    - After data loading: print treebank counts, WALS coverage stats
    - After ZA fitting: print convergence rate, parameter distributions (histogram)
    - After mixed models: print model summaries, check significant predictors
    - Before final output: validate method_out.json against schema using aii-json skill

  ERROR HANDLING:
    - If ZA fitting fails for a treebank: log warning, skip that treebank, continue
    - If mixed model doesn't converge: try simpler model, log warning
    - If merge produces 0 rows: check treebank name formats match between datasets
    - Save intermediate results after each step (checkpointing for long runs)
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

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

Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</dependencies>

<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>

<skills>
Skills are self-contained capabilities with instructions, context, and tools.

- aii-web-tools: Web search (Serper), page/PDF fetch as markdown, regex grep over page/PDF text
- aii-semscholar-bib: Batch-fetch BibTeX from Semantic Scholar
- aii-openrouter-llms: Search and call 300+ LLMs via OpenRouter
- aii-hf-datasets: Search, preview, download HuggingFace datasets
- aii-owid-datasets: Search and load Our World in Data tables
- aii-lean: Compile/verify Lean 4 code, Mathlib search, tactic suggestions
- aii-image-gen: Generate/edit images via Gemini 3 Pro Image (Nano Banana Pro)
- aii-json: Validate JSON against schemas, generate mini/preview variants
- aii-paper-writing: Academic paper structure, bibliography, citations
- aii-paper-to-latex: Assemble LaTeX papers and compile to PDF
- aii-parallel-computing: GPU acceleration, CPU parallelism, async I/O
- aii-python: Python coding standards for experiment scripts
- aii-use-hardware: Detect CPU/RAM/GPU, memory-safe processing
- aii-long-running-tasks: Gradual scaling pattern for long-running tasks
- aii-colab: Google Colab runtime constraints for notebooks
- aii-file-size-limit: Check and split oversized output files
</skills>
</available_resources>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for framework choices, implementation patterns, agent orchestration.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-python, aii-long-running-tasks, aii-json, aii-file-size-limit, aii-use-hardware, aii-parallel-computing.
TODO 2. Read preview files from dependencies to understand data structure. Use ALL datasets provided — do not skip or select a subset. Read domain handbook if applicable (see <available_domain_handbooks>). Test basic functionality with 'uv run'.
TODO 3. Fully implement our method AND baseline (comparison) as described in artifact plan in './method.py'. Use exp_gen_sol_out.json schema in aii-json skill for output format validation. Include everything specified in the artifact plan, but you may also implement additional relevant methods or analysis beyond what's listed. Be very attentive to meticulously and exhaustively fix any errors in your code.
</todos>

Direction: Computational Linguistics — Dependency Distance Minimization Across UD Treebanks. Something genuinely novel and groundbreaking that measures dependency-distance distributions across UD treebanks, investigates whether spoken language minimizes more than written, characterizes how typology interacts with the pattern, and identifies families that deviate. MUST use commul/universal_dependencies on HuggingFace.

Ambition: level 3 of 5 — phenomenological science: surface and rigorously characterize a new empirical regularity or anomaly in the data, even before a full theoretical explanation exists.

Reviewer: I am Kaja Dobrovoljc (JSI / University of Ljubljana). Calibrate from my existing papers. Cross-domain methods (information theory, mixed-effects models, sequence models) welcome — but keep them close to what I already know, not too far from my background.

Submission/Goal: a paper for ACL, EMNLP, or the Computational Linguistics journal. Audience: computational linguists and quantitative typologists. Tone: empirically rigorous, careful with linguistic detail, reproducible on public UD.
```

### [10] SYSTEM-USER prompt · 2026-07-20 01:58:29 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_txhWJXyNIa5t/3_invention_loop/iter_2/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_txhWJXyNIa5t/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_txhWJXyNIa5t/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_txhWJXyNIa5t/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_txhWJXyNIa5t/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_experiment_1_idx1
type: experiment
title: Fit ZA distributions and run mixed-effects models
summary: >-
  Fit Right Truncated Modified Zipf-Alekseev distributions to dependency distance data from 116 UD treebanks with WALS mappings,
  then run mixed-effects models to predict shape parameters from typological features while controlling for language family
  and treebank random effects.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: "STEP 1: Load and merge datasets\n  - Load dependency distance data from art_sbnX8nlSAUFX (full_data_out_parts/*.json)\n\
  \  - Load WALS mappings from art_JLcGgqg6OO_T (full_data_out.json)\n  - Merge on treebank_name field (from metadata_treebank\
  \ in WALS data, treebank_name in DD data)\n  - Filter to treebanks with >1000 dependencies AND complete WALS mappings (target:\
  \ ~116 treebanks)\n  - Extract WALS feature values: 1A (word order: 1=SVO, 2=SOV, 3=VSO, etc.), 20A (fusion), 26A (exponence),\
  \ 49A (cases), 51A (alignment)\n  - Create dummy variables for WALS features (handle NA values appropriately)\n\nSTEP 2:\
  \ ZA distribution fitting for each treebank\n  - For each treebank with >1000 dependencies:\n    a. Extract all dependency\
  \ distances (dd values from 'output' field)\n    b. Create empirical distribution: count frequency of each dd value (1,\
  \ 2, 3, ...)\n    c. Fit Right Truncated Modified Zipf-Alekseev distribution:\n       Formula: P(x) = P(1) * x^(-(a + b*ln(x)))\
  \ for x = 1, 2, ..., L\n       Where L = maximum observed DD in treebank\n       \n       MLE approach:\n       - Negative\
  \ log-likelihood function:\n         def neg_log_lik(params, dd_counts, L):\n             a, b = params\n             x_vals\
  \ = np.arange(1, L+1)\n             # Unnormalized probabilities\n             unnorm_p = x_vals ** (-(a + b * np.log(x_vals)))\n\
  \             # Normalize\n             p = unnorm_p / unnorm_p.sum()\n             # Compute negative log-likelihood\n\
  \             ll = 0\n             for x, count in dd_counts.items():\n                 ll += count * np.log(p[x-1] + 1e-10)\n\
  \             return -ll\n       \n       - Use scipy.optimize.minimize with bounds: a ∈ [-10, 10], b ∈ [-5, 5]\n      \
  \ - Initial values: a=1.0, b=0.0\n       - Extract fitted parameters: a (shape), b (log-modification)\n       - Compute\
  \ goodness-of-fit: Kolmogorov-Smirnov test, AIC\n    \n    d. Store results: treebank_name, a_param, b_param, n_deps, ks_stat,\
  \ p_value\n\nSTEP 3: Spoken vs written analysis (separate from ZA fitting)\n  - Given only 6,239 spoken dependencies (0.6%),\
  \ exclude spoken from ZA fitting\n  - Instead, compute mean DD per treebank for ALL treebanks (including spoken)\n  - Categorize\
  \ genre: spoken (genre contains 'spoken'), written (else)\n  - T-test: compare mean DD between spoken and written treebanks\n\
  \  - Linear regression: mean_dd ~ genre + sentence_length_mean + (1|family)\n  - Report effect size (Cohen's d) and confidence\
  \ intervals\n\nSTEP 4: Mixed-effects models for ZA parameters\n  - Prepare data: one row per treebank with columns:\n  \
  \  [treebank, family, wals_1A, wals_20A, wals_26A, wals_49A, wals_51A, a_param, b_param, mean_sentence_length, n_deps]\n\
  \  \n  - For each WALS feature (1A, 20A, 26A, 49A, 51A):\n    a. Dummy code the feature (convert to categorical with treatment\
  \ coding)\n    b. Fit separate mixed-effects model for a_param:\n       model_a = MixedLM.from_formula(\n           'a_param\
  \ ~ wals_feature + mean_sentence_length',\n           groups = df['family'],  # random intercept for family\n          \
  \ vc_formula = {'treebank': '0 + treebank'}  # random intercept for treebank\n       )\n       OR simpler:\n       model_a\
  \ = MixedLM(\n           endog = df['a_param'],\n           exog = sm.add_constant(df[['wals_feature', 'mean_sentence_length']]),\n\
  \           groups = df['family']\n       )\n       \n    c. Fit separate model for b_param (same structure)\n    d. Extract:\
  \ beta coefficients, SE, t-values, p-values, 95% CI, R² (marginal and conditional)\n    e. Check convergence: model.fit().converged\
  \ should be True\n    f. Report AIC/BIC for model comparison\n  \n  - For significant predictors (p < 0.05), compute effect\
  \ sizes:\n    Cohen's f² = (R²_full - R²_null) / (1 - R²_full)\n\nSTEP 5: Outlier detection via random effects\n  - Extract\
  \ random effect estimates from mixed-effects models:\n    family_effects = model.random_effects\n  - Identify families with\
  \ |random_effect| > 2*SE\n  - For each outlier family:\n    a. List treebanks in that family\n    b. Report mean a_param,\
  \ b_param vs global mean\n    c. Check if outlier status correlates with unmodeled WALS features\n    d. Qualitative investigation:\
  \ why might this family deviate?\n\nSTEP 6: Robustness checks\n  - Subsample analysis: run models on 80% of treebanks (bootstrap,\
  \ 1000 iterations)\n  - Control for treebank size: add log(n_deps) as covariate\n  - Sensitivity to ZA fitting: compare\
  \ with exponential distribution fit\n  - Multiple comparison correction: apply Benjamini-Hochberg FDR to p-values\n\nSTEP\
  \ 7: Output results to method_out.json\n  - Structure:\n    {\n      \"za_fitting_results\": [\n        {\"treebank\": \"\
  en_ewt\", \"a_param\": 1.23, \"b_param\": -0.05, \"n_deps\": 5000, \"ks_p\": 0.34, ...},\n        ...\n      ],\n      \"\
  mixed_effects_results\": {\n        \"a_param_models\": {\n          \"wals_1A\": {\"beta\": [...], \"se\": [...], \"p\"\
  : [...], \"r_squared\": 0.15, ...},\n          ...\n        },\n        \"b_param_models\": {...}\n      },\n      \"spoken_written_comparison\"\
  : {\n        \"t_test\": {\"statistic\": 2.34, \"p\": 0.02, \"cohens_d\": 0.3},\n        \"regression\": {...}\n      },\n\
  \      \"outlier_families\": [\n        {\"family\": \"Austroasiatic\", \"effect\": 1.5, \"se\": 0.4, ...},\n        ...\n\
  \      ],\n      \"robustness\": {...}\n    }"
fallback_plan: |-
  PRIMARY APPROACH FAILURES AND ALTERNATIVES:

  1. IF ZA distribution fitting fails to converge for many treebanks:
     - Alternative: Fit simpler exponential distribution: P(x) = λ * exp(-λ*x)
     - Extract decay parameter λ as shape parameter
     - Compare AIC between ZA and exponential to justify simpler model
     - Use exponential λ for mixed-effects models instead of ZA parameters

  2. IF insufficient treebanks with >1000 deps AND complete WALS mappings:
     - Lower threshold to >500 dependencies
     - Or use all treebanks but weight by sample size in mixed-effects models
     - Alternative: aggregate by language (merge multiple treebanks per language)

  3. IF mixed-effects model fails to converge (singular fit):
     - Simplify random effects structure: remove treebank random effect, keep only family
     - Use linear regression with clustered standard errors (family clusters)
     - Use LME4-style parameterization: start with simpler model, build complexity

  4. IF WALS features have too many missing values:
     - Use only treebanks with complete cases (listwise deletion)
     - Alternative: multiple imputation using mice approach (sklearn IterativeImputer)
     - Or use only the most complete feature (1A word order has best coverage)

  5. IF spoken sample too small for meaningful comparison:
     - Focus analysis on written treebanks only
     - Report descriptive stats for spoken without statistical tests
     - Suggest spoken analysis as limitation for future work

  6. IF statsmodels MixedLM too slow or problematic:
     - Alternative: use pymer4 (Python interface to R lme4)
     - Or use linear regression with fixed effects for family (absorbing family variation)
     - Or use hierarchical Bayesian model via pymc3 (more flexible but slower)

  7. IF ZA parameter estimates are unstable (large SEs):
     - Use binned DD distributions (group distances into bins: 1, 2-3, 4-7, 8+)
     - Fit ZA to binned data for more stable estimates
     - Or use method of moments estimators instead of MLE
testing_plan: |-
  TESTING STRATEGY: Gradual scaling from mini to full data

  PHASE 1: Unit tests on mini data (expected time: 15 min)
    - Test data loading: load data_out_mini.json (3 examples), verify structure
    - Test ZA fitting on synthetic data:
      a. Generate synthetic DD data from known ZA distribution (a=1.0, b=0.0)
      b. Fit ZA distribution to synthetic data
      c. Verify recovered parameters within 10% of true values
    - Test WALS mapping merge: merge mini DD data with mini WALS data
    - Test mixed-effects model on 5 treebanks with synthetic ZA parameters
    - Verify method_out.json structure matches schema

  PHASE 2: Scale to preview data (expected time: 30 min)
    - Load data_out_preview.json (100 examples)
    - Fit ZA distributions to treebanks in preview set
    - Run mixed-effects models with subset of WALS features
    - Verify convergence and reasonable parameter estimates
    - Check that spoken/written comparison runs without errors

  PHASE 3: Run on full data (expected time: 2-3 hours)
    - Load all 7 parts of full_data_out_*.json (979,098 observations)
    - Fit ZA distributions to all eligible treebanks (~116 target)
    - Run full mixed-effects models for all WALS features
    - Generate all output tables and figures
    - Validate results:
      a. ZA fitting: check that KS test p-values > 0.05 for good fits
      b. Mixed models: check convergence, no singular fits
      c. Outliers: verify random effects sum to ~0
      d. Spoken-written: check effect direction matches hypothesis (spoken should have longer DD)

  VALIDATION CHECKPOINTS:
    - After data loading: print treebank counts, WALS coverage stats
    - After ZA fitting: print convergence rate, parameter distributions (histogram)
    - After mixed models: print model summaries, check significant predictors
    - Before final output: validate method_out.json against schema using aii-json skill

  ERROR HANDLING:
    - If ZA fitting fails for a treebank: log warning, skip that treebank, continue
    - If mixed model doesn't converge: try simpler model, log warning
    - If merge produces 0 rows: check treebank name formats match between datasets
    - Save intermediate results after each step (checkpointing for long runs)
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

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

Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</dependencies>

<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>

<skills>
Skills are self-contained capabilities with instructions, context, and tools.

- aii-web-tools: Web search (Serper), page/PDF fetch as markdown, regex grep over page/PDF text
- aii-semscholar-bib: Batch-fetch BibTeX from Semantic Scholar
- aii-openrouter-llms: Search and call 300+ LLMs via OpenRouter
- aii-hf-datasets: Search, preview, download HuggingFace datasets
- aii-owid-datasets: Search and load Our World in Data tables
- aii-lean: Compile/verify Lean 4 code, Mathlib search, tactic suggestions
- aii-image-gen: Generate/edit images via Gemini 3 Pro Image (Nano Banana Pro)
- aii-json: Validate JSON against schemas, generate mini/preview variants
- aii-paper-writing: Academic paper structure, bibliography, citations
- aii-paper-to-latex: Assemble LaTeX papers and compile to PDF
- aii-parallel-computing: GPU acceleration, CPU parallelism, async I/O
- aii-python: Python coding standards for experiment scripts
- aii-use-hardware: Detect CPU/RAM/GPU, memory-safe processing
- aii-long-running-tasks: Gradual scaling pattern for long-running tasks
- aii-colab: Google Colab runtime constraints for notebooks
- aii-file-size-limit: Check and split oversized output files
</skills>
</available_resources>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for framework choices, implementation patterns, agent orchestration.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Use aii-json skill's format script with `--input method_out.json` to generate full, mini, and preview versions. If not in your workspace (see <workspace> above), copy them there. Run 'ls -lh' to verify these three files exist (DO NOT read them).
TODO 2. Apply aii-file-size-limit skill's file size check procedure (100MB limit) to method_out.json and full_method_out.json.
TODO 3. Ensure a `pyproject.toml` exists in your workspace with ALL dependencies pinned to the exact versions installed in your .venv (run `.venv/bin/pip freeze` to get them). This is required for reproducibility. The [project] section must include name, version, requires-python, and a dependencies list with pinned versions (e.g. `numpy==2.0.2`, not `numpy>=2.0`).
</todos>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_txhWJXyNIa5t/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ExperimentExpectedFiles": {
      "description": "All expected output files from experiment artifact.",
      "properties": {
        "script": {
          "description": "Path to method.py script. Example: 'method.py'",
          "title": "Script",
          "type": "string"
        },
        "full_output": {
          "description": "Full method output JSON file. Example: 'full_method_out.json'",
          "title": "Full Output",
          "type": "string"
        },
        "mini_output": {
          "description": "Mini method output JSON file. Example: 'mini_method_out.json'",
          "title": "Mini Output",
          "type": "string"
        },
        "preview_output": {
          "description": "Preview method output JSON file. Example: 'preview_method_out.json'",
          "title": "Preview Output",
          "type": "string"
        }
      },
      "required": [
        "script",
        "full_output",
        "mini_output",
        "preview_output"
      ],
      "title": "ExperimentExpectedFiles",
      "type": "object"
    }
  },
  "description": "Experiment artifact \u2014 structured output + file metadata.\n\nImplements research methodology with baseline comparison.\nProduces method.py and method_out.json files.",
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
      "$ref": "#/$defs/ExperimentExpectedFiles",
      "description": "All output files you created. Must include method.py script plus full/mini/preview method output JSON files."
    },
    "upload_ignore_regexes": {
      "description": "Regex patterns for workspace paths that must NOT be published to the GitHub repo, matched against each file's path relative to this artifact's workspace root (POSIX form, e.g. 'cache/abc.json'). Applied ON TOP OF the deploy step's built-in exclusions. Use this for executor-specific caches, large transient intermediates, or content-addressed blob stores (e.g. a cache/ dir of thousands of hash-named files) that would bloat the repo. Examples: ['(^|/)cache/', '(^|/)\\\\.weight_cache/', '(^|/)checkpoints/']. Leave empty if every workspace file should be published.",
      "items": {
        "type": "string"
      },
      "title": "Upload Ignore Regexes",
      "type": "array"
    }
  },
  "required": [
    "out_expected_files"
  ],
  "title": "ExperimentArtifact",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `/ai-inventor/aii_data/runs/run_txhWJXyNIa5t/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/.sdk_openhands_agent_struct_out.json`.
````

### [11] SYSTEM-USER prompt · 2026-07-20 02:02:15 UTC

```
<verification_failed>
Your experiment output failed verification (attempt 1/10).
</verification_failed>

<schema_errors>
JSON SCHEMA / CODE VALIDATION ERRORS:
  - full_method_out.json: Missing required 'datasets' key
  - mini_method_out.json: Missing required 'datasets' key
  - preview_method_out.json: Missing required 'datasets' key

Fix: Your JSON files must follow the datasets-grouped exp_gen_sol_out.json schema:
     {
       "datasets": [
         {
           "dataset": "dataset_name",
           "examples": [
             {
               "input": "string (required)",
               "output": "string (required)",
               "metadata_fold": 2,
               "predict_<method_name>": "string - prediction per method"
             }
           ]
         }
       ]
     }

     NO 'split', 'dataset', or 'context' per-example. Dataset name at group level.
     Metadata via flat metadata_<name> fields.
     Read exp_gen_sol_out.json schema in aii-json skill.
     Then update method.py and regenerate the output files.

     If Python syntax errors: fix the syntax in method.py
</schema_errors>

<task>
FIX THESE ISSUES:
2. Fix schema/syntax errors in method.py
3. Re-run method.py to regenerate output files
4. Validate with aii-json skill: validate method_out.json against exp_gen_sol_out schema

After making changes, verify:
- 'ls -la' shows all required files
- 'uv run method.py' completes successfully
- JSON files are valid (use aii-json skill validation)
- full_method_out.json has at least 50 examples
</task>
```
