# upd_hypo — test_idea

> Phase: `invention_loop` · round 2 · `upd_hypo`
> Run: `run_txhWJXyNIa5t` — Typological Predictors of Dependency Distance Distribution Shapes in Universal Dependencies
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `upd_hypo` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-07-20 02:19:16 UTC

````
<current_hypothesis>
The hypothesis as it stands. Revise it based on the evidence below.

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
</current_hypothesis>

<all_artifacts>
Complete set of research artifacts across all iterations.

--- Item 1 ---
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

--- Item 2 ---
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

--- Item 3 ---
id: art_FomYM_VOxLXl
type: research
title: Methodological review for dependency distance typology study
summary: >-
  This methodological review provides comprehensive guidance for studying dependency distance (DD) minimization across Universal
  Dependencies (UD) treebanks. The research addresses three key methodological questions: (1) how to specify mixed-effects
  models for typological data with crossed random effects, (2) how to fit probability distributions to dependency distance
  data, and (3) what prior evidence exists for spoken vs written genre effects on syntactic structures. Key findings include:
  (1) Mixed-effects models should use lme4 formula syntax with crossed random effects for language family and treebank, implementable
  in Python via pymer4; (2) Dependency distances follow the Right Truncated Modified Zipf-Alekseev distribution with formula
  P_x = P_1 * x^{-(a + b*ln x)}, where parameters a and b indicate syntactic complexity; (3) Dobrovoljc (2026) found spoken
  language has fewer and less diverse syntactic structures than writing, suggesting modality effects on DD; (4) 12 spoken
  UD treebanks are available for comparison; (5) WALS data is accessible via CLDF format on GitHub for mapping typological
  features to UD treebanks. The review includes Python code examples for distribution fitting using scipy.optimize, recommendations
  for mixed-effects model specification, and a complete bibliography with BibTeX entries. This research supports the main
  experiment investigating whether spoken language minimizes dependency distance more than written language, how typology
  interacts with this pattern, and which language families deviate from the universal tendency.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_txhWJXyNIa5t/3_invention_loop/iter_1/gen_art/gen_art_research_1
out_expected_files:
- research_out.json

--- Item 4 ---
id: art_7ioJFjCPvSR4
type: experiment
in_dependencies:
- id: art_sbnX8nlSAUFX
  label: dataset
- id: art_JLcGgqg6OO_T
  label: wals_mapping
title: Dependency distance ZA distribution fitting
summary: >-
  Successfully implemented and executed the full experimental pipeline with corrected output schema: (1) Loaded and merged
  dependency distance data from 979,098 observations across 350+ UD treebanks with WALS typological features (116 treebanks
  with mappings), (2) Fit Right Truncated Modified Zipf-Alekseev distributions to 41 treebanks with complete data (100% convergence
  rate), (3) Performed spoken vs written analysis (no significant difference, p=0.488), (4) Ran mixed-effects models with
  random intercepts for language family, identifying significant predictors: wals_51A (case alignment) predicts both a_param
  (β=-0.024, p=0.034) and b_param (β=0.014, p=0.018), (5) Detected 2 outlier families (Turkic), (6) Completed robustness checks
  including bootstrap analysis and distribution comparison. Output now follows exp_gen_sol_out.json schema with 'datasets'
  top-level key and proper 'input'/'output' structure for each example.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_txhWJXyNIa5t/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json
</all_artifacts>

<new_artifacts_this_iteration>
These 1 artifacts were created THIS iteration.

id: art_7ioJFjCPvSR4
type: experiment
in_dependencies:
- id: art_sbnX8nlSAUFX
  label: dataset
- id: art_JLcGgqg6OO_T
  label: wals_mapping
title: Dependency distance ZA distribution fitting
summary: >-
  Successfully implemented and executed the full experimental pipeline with corrected output schema: (1) Loaded and merged
  dependency distance data from 979,098 observations across 350+ UD treebanks with WALS typological features (116 treebanks
  with mappings), (2) Fit Right Truncated Modified Zipf-Alekseev distributions to 41 treebanks with complete data (100% convergence
  rate), (3) Performed spoken vs written analysis (no significant difference, p=0.488), (4) Ran mixed-effects models with
  random intercepts for language family, identifying significant predictors: wals_51A (case alignment) predicts both a_param
  (β=-0.024, p=0.034) and b_param (β=0.014, p=0.018), (5) Detected 2 outlier families (Turkic), (6) Completed robustness checks
  including bootstrap analysis and distribution comparison. Output now follows exp_gen_sol_out.json schema with 'datasets'
  top-level key and proper 'input'/'output' structure for each example.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_txhWJXyNIa5t/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json
</new_artifacts_this_iteration>

<current_paper>
The paper draft from this iteration — represents the current state of the research story.

# Introduction

Dependency Distance Minimization (DDM) is a fundamental principle of human language, positing that speakers prefer short syntactic dependencies to reduce working memory load during processing [1]. This principle has been demonstrated as a cross-linguistic universal across 37 languages [1] and subsequently confirmed in larger-scale studies [2, 3]. However, the vast majority of prior work characterizes DDM exclusively through mean dependency distance (MDD), ignoring the rich distributional information encoded in the full dependency distance (DD) distribution shape.

The distribution of dependency distances is not merely a reflection of central tendency. Prior work has shown that DD distributions follow a Right Truncated Modified Zipf-Alekseev distribution [4, 5], with shape parameters that encode distinct aspects of syntactic complexity. Parameter $a$ increases with syntactic complexity (indicating more long-distance dependencies), while parameter $b$ decreases with syntactic complexity (indicating sharper decay toward short dependencies) [5]. These parameters capture structural properties that mean DD alone cannot reveal.

Meanwhile, the interaction between typology and DD distributions remains understudied. While Futrell et al. [1] established DDM as universal across 37 languages, and Gerdes et al. [2] recently showed functional vs. lexical distinctions across 122 languages, nobody has systematically linked WALS (World Atlas of Language Structures) typological features [6] to DD distribution shape parameters using mixed-effects models across the full UD collection. Such a study would: (1) reveal whether typological constraints operate on distribution shape or only on central tendency; (2) quantify the spoken-vs-written DD difference with appropriate statistical controls; and (3) identify 'outlier' families that deviate from DDM, providing targets for deeper typological investigation.

This study addresses these gaps by analyzing dependency distances computed from Universal Dependencies (UD) treebanks [7] available via the commul/universal_dependencies dataset on HuggingFace. Our contributions are:

1. **Typological predictors of DD distribution shapes**: We fit Right Truncated Modified Zipf-Alekseev distributions to 41 UD treebanks with complete WALS feature mappings and show that locus of marking (WALS 51A) significantly predicts distribution shape parameters in mixed-effects models (a_param: β = -0.024, p = 0.034; b_param: β = 0.014, p = 0.018).

2. **Spoken vs. written genre effects**: We provide a quantitative comparison of DD distributions across spoken and written genres in UD, finding no significant difference (t = -1.031, p = 0.488), with the analysis limited by small spoken treebank sample sizes (only 2 spoken treebanks meet the minimum dependency threshold of 1000).

3. **Family-level outliers**: We identify the Turkic language family as deviating significantly from the universal DDM pattern, with effect sizes of 0.719 for a_param and -0.291 for b_param.

[FIGURE:fig1]

# Related Work

## Dependency Distance Minimization

The study of dependency distance in natural language was formalized by Hudson [8] and later established as a processing principle by Gibson [9]. Futrell et al. [1] provided the first large-scale evidence of DDM across 37 languages, showing that mean dependency distance is consistently low across diverse language families. This finding has been replicated in numerous subsequent studies [2, 3, 10].

However, most prior work reports only mean DD (MDD) as the summary statistic. Liu et al. [5] and Popescu et al. [4] showed that DD distributions follow the Right Truncated Modified Zipf-Alekseev distribution, with shape parameters $a$ and $b$ that encode syntactic complexity. To date, no study has systematically linked these shape parameters to typological features using mixed-effects models.

## Typological Correlates of Syntax

Quantitative typology has increasingly adopted mixed-effects models to control for phylogenetic non-independence [11, 12]. Baayen et al. [13] established the standard for crossed random effects with subjects and items, which has been adapted for typological data with language family and treebank as grouping factors [14]. Levshina [14] provides a comprehensive guide to using mixed-effects models in quantitative typology with WALS features as predictors.

Niu et al. [3] compared DD minimization across four languages (Chinese, Japanese, English, Czech), finding a trade-off between syntactic and morphological complexity. However, Niu et al. analyzed only four languages without using WALS features or mixed-effects models, limiting the generalizability of their findings. Gerdes et al. [2] analyzed 122 languages in UD/SUD, finding functional dependencies are universally short while lexical dependencies vary by typology. Gerdes et al. did not, however, fit distribution shapes or compare spoken vs. written genres.

The current study extends Niu et al. [3] by: (1) analyzing 41 treebanks across diverse language families with complete WALS feature mappings; (2) using WALS features as quantitative predictors in mixed-effects models; (3) fitting full DD distribution shapes rather than reporting only means; and (4) providing a systematic (though limited by sample size) comparison of spoken vs. written genres. While Niu et al. found a trade-off between syntactic and morphological complexity, our larger-scale analysis identifies locus of marking (WALS 51A) as a significant predictor of distribution shape, suggesting that case alignment patterns—not just broad morphological complexity—play a key role in shaping dependency distance distributions.

## Genre Effects on Syntax

Dobrovoljc [15] provides a treebank-driven exploration of syntactic variation in speech and writing across languages, analyzing syntactic structure inventories in English and Slovenian treebanks. Dobrovoljc found that spoken corpora contain different syntactic structures than written counterparts, with implications for treebank-based research. Dobrovoljc and Nivre [16] also catalog spoken UD treebanks, providing a resource for cross-modal comparison.

Wang and Liu [17] found significant genre effects on dependency distance and direction, though their study did not specifically contrast speech vs. writing using mixed-effects models. The current study builds on this work by explicitly modeling genre as a fixed effect while controlling for sentence length and language family random effects.

# Methods

## Data

### Universal Dependencies Treebanks

We analyzed treebanks from the commul/universal_dependencies dataset on HuggingFace [7], comprising 193 languages. For each non-root dependency in every sentence, we computed the dependency distance as the absolute difference between head and dependent positions. This yielded 979,098 dependency observations after filtering [ARTIFACT:art_sbnX8nlSAUFX].

Treebanks were categorized by genre based on their names and metadata: (1) spoken (e.g., en_childes, fr_rhapsodie); (2) written formal (e.g., news, wiki treebanks); and (3) written informal (e.g., reddit, social media) [ARTIFACT:art_sbnX8nlSAUFX].

### WALS Feature Mapping

We mapped UD treebank languages to WALS typological features [6] using ISO 639-3 code matching. Five WALS features were selected based on their theoretical relevance to dependency distance:

- **1A**: Order of Subject, Object, and Verb (word order type: SVO, SOV, VSO, etc.)
- **20A**: Fusion of Inflectional Morphology (isolating, agglutinative, fusional)
- **26A**: Exponence of Selected Inflectional Categories (minimal, moderate)
- **49A**: Number of Cases (0, 2, 3-5, 6-8, 9+)
- **51A**: Locus of Marking in the Clause (none, prefixing, suffixing)

The mapping achieved 84.5% high-confidence mappings via ISO 639-3 code matching, covering 116 UD treebanks [ARTIFACT:art_JLcGgqg6OO_T]. For each treebank, we extracted the WALS feature values for its language.

### Data Filtering

For the distribution fitting and mixed-effects modeling, we applied two filtering criteria: (1) minimum of 1000 dependencies per treebank to ensure reliable parameter estimation following Liu et al. [5]; and (2) complete WALS feature data (no missing values for the five features). After filtering, 41 treebanks remained for analysis [ARTIFACT:art_7ioJFjCPvSR4].

## Distribution Fitting

Following Liu et al. [5] and Popescu et al. [4], we fit the Right Truncated Modified Zipf-Alekseev (ZA) distribution to each treebank's DD distribution. The ZA distribution has probability mass function:

$$P_x = P_1 \cdot x^{-(a + b\ln x)}, \quad x = 1, 2, 3, \ldots, n$$

where $P_x$ is the probability of dependency distance $x$, $P_1$ is the normalization constant, $a$ and $b$ are shape parameters, and $n$ is the maximum observed dependency distance (truncation point).

Parameters were estimated via Maximum Likelihood Estimation (MLE) using L-BFGS-B optimization with bounds in Python [ARTIFACT:art_7ioJFjCPvSR4]. The Kolmogorov-Smirnov test was used to assess goodness-of-fit for each treebank.

## Mixed-Effects Models

To test whether WALS features predict DD distribution shape parameters, we fit linear mixed-effects models (LMMs) using statsmodels in Python [18]. The model specification follows the recommendations of Baayen et al. [13] and Levshina [14] for typological data:

$$\text{shape\_param}_{ij} = \beta_0 + \beta_1 \text{WALS}_{ij} + \beta_2 \text{sentence\_length}_{ij} + u_j + \epsilon_{ij}$$

where:
- $\text{shape\_param}_{ij}$ is the distribution shape parameter (e.g., parameter $a$) for treebank $i$ in language family $j$
- $\text{WALS}_{ij}$ is the WALS feature value (coded as dummy variables)
- $\text{sentence\_length}_{ij}$ is the mean sentence length for treebank $i$, included as a control variable
- $u_j \sim N(0, \sigma^2_{family})$ is the random intercept for language family
- $\epsilon_{ij} \sim N(0, \sigma^2)$ is the residual error

We fit separate models for each WALS feature and each shape parameter. Fixed effects were coded using dummy variables with the most frequent value as baseline. Random effects were specified as intercepts for language family, allowing for non-independence of observations from the same family.

Model convergence was checked for all models. Singular fits (random effects variance = 0) were noted. Likelihood ratio tests were used to compare models with and without predictors.

## Spoken vs. Written Analysis

To compare spoken vs. written genres, we used two approaches: (1) independent samples t-test comparing mean DD between genres; and (2) linear regression with genre as predictor, controlling for sentence length. Unlike the mixed-effects models for WALS features, the spoken-written comparison used the full dataset (including treebanks without complete WALS mappings) to maximize statistical power, but was limited to treebanks with the genre label.

## Outlier Detection

Language families with large random effect magnitudes were identified as outliers if $|u_j| > 0.25$ on the standardized scale. We then investigated these families qualitatively to identify specific typological features that might explain their deviation from the universal DDM pattern.

# Results

## Dataset Statistics

Our dataset comprises 979,098 dependency observations from 193 languages across 350+ UD treebanks. After filtering for minimum dependencies (1000) and complete WALS mappings, 41 treebanks remained for the distribution fitting and mixed-effects modeling [ARTIFACT:art_7ioJFjCPvSR4].

Genre distribution among the 41 analyzed treebanks: 2 spoken (en_childes, fr_rhapsodie), 39 written formal. The spoken treebanks contained 4,246 total dependencies, while the written treebanks contained 130,158 total dependencies.

[FIGURE:fig2]

## WALS Features Predict DD Distribution Shapes

Mixed-effects models show that WALS feature 51A (locus of marking in the clause) significantly predicts dependency distance distribution shape parameters. Table 1 presents the fixed effects estimates for all WALS features.

**Locus of marking effects (WALS 51A)**: Locus of marking significantly predicts both shape parameters:
- For a_param: β = -0.024, SE = 0.011, p = 0.034, 95% CI [-0.047, -0.002]
- For b_param: β = 0.014, SE = 0.006, p = 0.018, 95% CI [0.002, 0.026]

These effects indicate that languages with suffixing case marking (the baseline category in our models) have higher a_param values (more long-distance dependencies) and lower b_param values (sharper decay) compared to languages with other locus of marking patterns.

**Other WALS features**: Word order (1A), morphological fusion (20A), exponence (26A), and case marking (49A) did not reach statistical significance (all p > 0.05) after controlling for sentence length and family random effects. Full results are presented in Table 1.

**Model fit**: The WALS 51A model explained substantial variance in both a_param (random effects variance = 0.098, residual variance = 0.036) and b_param (random effects variance = 0.013, residual variance = 0.011). All models converged without warnings.

[TABLE:table1]

## Spoken vs. Written Genre Effects

Spoken and written genres do NOT exhibit significantly different dependency distances in our analysis. Results from the independent samples t-test:

- t-statistic = -1.031
- p-value = 0.488 (not significant)
- Cohen's d = -0.856 (large effect size, but low power due to small spoken sample)
- Spoken mean DD = 2.827 (n = 2 treebanks)
- Written mean DD = 3.404 (n = 39 treebanks)

Linear regression controlling for sentence length confirmed this null result:
- Genre (spoken) coefficient = -0.240, p = 0.322
- Sentence length coefficient = 0.041, p < 0.001
- R² = 0.625

The lack of significance is likely due to low statistical power: only 2 spoken treebanks (en_childes with 1,225 dependencies, fr_rhapsodie with 3,021 dependencies) met the minimum 1000-dependency threshold for inclusion. The remaining spoken treebanks in UD (e.g., sl_sst, sv_talbanken spoken portion) had insufficient data for reliable distribution fitting.

Figure 3 shows the distribution of dependency distances by genre. While the figure suggests spoken language may have a different distribution shape, the small sample size (especially the small number of spoken treebanks) limits the reliability of this observation.

[FIGURE:fig3]

## Family-Level Outliers

One language family showed substantial deviation from the mixed-effects model predictions:

**Turkic** (effects: a_param = 0.719, b_param = -0.291): Turkic languages (Turkish tr_imst, tr_pud) show substantially higher a_param values (more long-distance dependencies) and lower b_param values than the model predicts based on their WALS features. This deviation suggests that typological factors not captured by the five WALS features used here—or phylogenetic factors specific to the Turkic family—influence dependency distance distributions in this family.

The Turkic outlier is particularly interesting given that Turkish is a head-final (SOV) language with agglutinative morphology and rich case marking (WALS 49A: 6-8 cases), which may permit longer dependencies than predicted by universal DDM.

# Discussion

## Typological Constraints on DD Distributions

Our findings demonstrate that typological features—specifically locus of marking (WALS 51A)—systematically predict dependency distance distribution shapes across 41 UD treebanks. This extends prior work on DDM in three key ways:

1. **Beyond mean DD**: We show that typological constraints operate on distribution shape parameters (not only on central tendency), confirming that the full DD distribution carries linguistically meaningful information beyond the mean.

2. **WALS features as predictors**: Using mixed-effects models with WALS features as fixed effects, we quantify the magnitude of typological effects. Locus of marking (WALS 51A) significantly predicts both a_param (β = -0.024, p = 0.034) and b_param (β = 0.014, p = 0.018), with effect sizes that are small but statistically significant in our sample.

3. **Distribution shape interpretation**: The ZA distribution parameters $a$ and $b$ show distinct patterns: languages with suffixing case marking (the baseline in our models) have higher $a$ values (more long-distance dependencies) and lower $b$ values (slower decay toward short dependencies), consistent with the theoretical prediction that morphological case marking may permit longer dependencies by reducing dependency processing cost.

The finding that WALS 51A (locus of marking) is a significant predictor, while word order (1A) is not, contrasts with some prior work [1, 3] that emphasized word order effects. This discrepancy may be due to: (1) our focus on distribution shapes rather than mean DD; (2) the specific set of languages in our filtered sample (41 treebanks with complete data); or (3) the mixed-effects modeling approach that controls for family-level random effects.

## Spoken vs. Written Modality

The finding that spoken and written genres do NOT show significantly different DD distributions (p = 0.488) contrasts with our initial hypothesis and with Dobrovoljc's [15] observation that spoken language has different syntactic structures. However, this null result must be interpreted cautiously given the severe power limitation: only 2 spoken treebanks met the inclusion threshold.

The current study's spoken sample (en_childes: child-directed speech; fr_rhapsodie: French spontaneous speech) may not be representative of spoken language broadly. Additionally, the spoken treebanks have different mean sentence lengths (en_childes: 7.3 words; fr_rhapsodie: 25.6 words) than the written treebanks (mean: 24.1 words), which could confound genre effects. The regression controlling for sentence length still shows no significant genre effect, but the small spoken sample limits statistical power.

Future work with larger spoken treebank samples (e.g., combining multiple spoken treebanks per language family) is needed to resolve this question.

## Family-Level Deviations

The identification of the Turkic family as an outlier provides a target for deeper typological investigation. The Turkic deviation is consistent with the observation that Turkish allows flexible word order due to rich case marking, potentially allowing longer dependencies than predicted by universal DDM.

However, the outlier detection in this study is limited by the small number of treebanks per family (Turkic: 2 treebanks). With more treebanks per family, we could more reliably distinguish family-level effects from treebank-specific idiosyncrasies.

## Comparison with Prior Work

Niu et al. [3] found a trade-off between syntactic and morphological complexity across 4 languages. Our larger-scale analysis partially confirms this: locus of marking (WALS 51A, related to morphological complexity) predicts distribution shape, while word order (WALS 1A, related to syntactic complexity) does not reach significance. However, the specific pattern differs: Niu et al. suggested morphological complexity reduces dependency distance, while our findings suggest suffixing case marking is associated with more long-distance dependencies (higher a_param).

This apparent contradiction may be resolved by noting that locus of marking (WALS 51A) is not identical to morphological complexity (WALS 20A): 51A captures where case/agreement markers appear (prefixing vs. suffixing), while 20A captures how fused the morphology is (isolating vs. agglutinative vs. fusional). The different findings highlight the importance of distinguishing different dimensions of morphological typology.

## Limitations

Several limitations constrain the interpretation of our findings:

1. **Small spoken sample**: Only 2 spoken treebanks met the inclusion threshold, severely limiting power for spoken-written comparisons. This is a major limitation that future work must address.

2. **WALS mapping coverage**: 41 of 350+ treebanks (11.7%) have complete WALS feature mappings and sufficient data for analysis. While this represents treebanks with available WALS data, the remaining 88.3% could introduce bias if unmapped treebanks differ systematically. Indo-European languages are overrepresented (24 of 41 treebanks, 58.5%).

3. **Selection bias**: Treebanks with WALS mappings and sufficient data may differ systematically from those without. Well-studied languages (English, French, German) have both WALS data and large treebanks, while low-resource languages may not. This could bias results toward Indo-European languages.

4. **Distribution fitting requirements**: The ZA distribution requires substantial data (>1000 dependencies) for reliable parameter estimation. Smaller treebanks were excluded, reducing sample size and potentially introducing bias.

5. **Causal inference**: Mixed-effects models identify correlations, not causal relationships. The observed WALS effects could be mediated by unmeasured confounds (e.g., sociolinguistic factors, historical relationships).

6. **Model specification**: We used only random intercepts for language family, not random slopes. Barr et al. (2013) recommend starting with the maximal random effects structure, which would include random slopes for WALS effects by family. Our simpler specification may underestimate standard errors.

7. **FDR correction**: We did not apply False Discovery Rate correction to the multiple WALS features tested. Applying FDR correction (e.g., Benjamini-Hochberg) would increase the threshold for significance, potentially rendering even the WALS 51A effects non-significant.

# Conclusion

This study provides an investigation of typological predictors of dependency distance distribution shapes across 41 UD treebanks with complete WALS feature mappings. Our key findings are:

1. WALS locus of marking feature (51A) significantly predicts DD distribution shape parameters, with suffixing languages showing higher a_param (more long-distance dependencies) and lower b_param (sharper decay) than other languages (a_param: β = -0.024, p = 0.034; b_param: β = 0.014, p = 0.018).

2. Spoken vs. written genre analysis reveals no significant difference in dependency distance (p = 0.488), but this null result is limited by the small spoken sample (2 treebanks).

3. The Turkic language family deviates from the universal DDM pattern predicted by WALS features, with effect sizes of 0.719 for a_param and -0.291 for b_param.

These findings demonstrate that typological constraints—specifically locus of marking—operate on distribution shape, not only on central tendency. The work provides a more nuanced picture of how grammar, processing pressures, and modality interact to shape syntactic dependency structures. However, the limitations (small spoken sample, selection bias, limited WALS features) highlight the need for larger-scale studies with more comprehensive typological coverage.

Future work should: (1) increase spoken treebank coverage for reliable genre comparisons; (2) include additional WALS features (e.g., head-marking vs. dependent-marking); (3) apply FDR correction for multiple comparisons; (4) investigate the Turkic outlier with additional treebanks; and (5) extend the analysis to dependency direction (left- vs. right-branching) in addition to dependency distance.

# Acknowledgments

We thank the Universal Dependencies consortium for maintaining the UD treebanks, and the Max Planck Institute for Evolutionary Anthropology for making WALS data publicly available. This research was conducted using the commul/universal_dependencies dataset on HuggingFace.

# References

[1] Futrell, R., Mahowald, K., & Gibson, E. (2015). Large-scale evidence of dependency length minimization in 37 languages. *Proceedings of the National Academy of Sciences*, 112(33), 10336-10341.

[2] Gerdes, K. (2026). The Grammar Does the Work: Functional vs. Lexical Dependency Length Minimization Across Universal Dependencies. *arXiv preprint arXiv:2607.01899*.

[3] Niu, R., Wang, Y., & Liu, H. (2023). The Cross-linguistic Variations in Dependency Distance Minimization and its Potential Explanations. *Proceedings of the 37th Pacific Asia Conference on Language, Information and Computation*, 559-569.

[4] Popescu, I. I., & Altmann, G. (2014). *Unified Modeling of Length in Language*. RAM-Verlag.

[5] Liu, H., Xu, C., & Liang, J. (2017). Dependency distance: a new perspective on syntactic patterns in natural languages. *Physics of Life Reviews*, 21, 171-193.

[6] Dryer, M. S., & Haspelmath, M. (Eds.). (2013). *The World Atlas of Language Structures Online*. Max Planck Institute for Evolutionary Anthropology.

[7] Nivre, J., et al. (2020). Universal Dependencies v2: An evergrowing multilingual treebank collection. *Proceedings of the 12th Language Resources and Evaluation Conference*, 4034-4043.

[8] Hudson, R. (1995). Measuring syntactic difficulty. *University College London, Department of Phonetics and Linguistics, Working Papers*, 7, 1-26.

[9] Gibson, E. (1998). Linguistic complexity: Locality of syntactic dependencies. *Cognition*, 68(1), 1-76.

[10] Futrell, R., & Levy, R. (2017). Noisy-context surprisal as a human sentence processing cost model. *Proceedings of the 15th Conference of the European Chapter of the Association for Computational Linguistics*, 688-693.

[11] Jaeger, T. F. (2008). Categorical data analysis: Away from ANOVAs (transformation or not) and towards logit mixed models. *Journal of Memory and Language*, 59(4), 434-446.

[12] Levshina, N. (2022). *How to Do Linguistics with R: Data Exploration and Statistical Analysis*. John Benjamins.

[13] Baayen, R. H., Davidson, D. J., & Bates, D. M. (2008). Mixed-effects modeling with crossed random effects for subjects and items. *Journal of Memory and Language*, 59(4), 390-412.

[14] Levshina, N. (2021). Mixed-effects models in quantitative typology. *Journal of Language Evolution*, 6(2), 115-128.

[15] Dobrovoljc, K. (2025). Counting trees: a treebank-driven exploration of syntactic variation in speech and writing across languages. *Corpus Linguistics and Linguistic Theory*. https://doi.org/10.1515/cllt-2025-0046

[16] Dobrovoljc, K., & Nivre, J. (2022). Spoken Language Treebanks in Universal Dependencies: an Overview. *Proceedings of the 13th Language Resources and Evaluation Conference*, 1254-1262.

[17] Wang, Y., & Liu, H. (2017). The effects of genre on dependency distance and dependency direction. *Journal of Chinese Linguistics*, 45(2), 211-241.

[18] Jolly, E., & Chang, L. J. (2021). Pymer4: Connecting R and Python for Linear Mixed-Effects Models. *Journal of Open Source Software*, 6(67), 3730.
</current_paper>

<reviewer_feedback>
Feedback from the paper reviewer this iteration.

- [MAJOR] (rigor) The paper fails to apply False Discovery Rate (FDR) correction despite testing 5 WALS features across 2 dependent variables (a_param and b_param), resulting in 10 statistical tests. The experiment metadata explicitly notes: 'FDR correction should be applied to mixed model p-values'. The only significant findings (WALS 51A: p=0.034 for a_param, p=0.018 for b_param) might not survive FDR correction. Using Benjamini-Hochberg at q=0.05, these p-values (ranked 1st and 2nd smallest among 10 tests) would need to be compared against thresholds of 0.005 and 0.010 respectively, which they would not pass. This is a critical statistical rigor issue that undermines the paper's main conclusion.
  Action: Apply FDR correction (Benjamini-Hochberg procedure) to the p-values from all 10 mixed-effects models (5 WALS features × 2 DVs). Report both uncorrected and FDR-corrected p-values in Table 1. If the results do not survive FDR correction, reframe the paper to focus on: (1) the descriptive finding that WALS 51A has the smallest p-values, (2) the Turkic outlier, and (3) the methodological contribution of linking WALS to ZA parameters. Alternatively, apply a more stringent significance threshold (e.g., p<0.01) from the outset.
- [MAJOR] (evidence) The spoken vs. written genre comparison is severely underpowered: only 2 spoken treebanks (en_childes, fr_rhapsodie) meet the inclusion threshold of 1000 dependencies. With n=2, the statistical power to detect a medium effect size is approximately 0.15 (far below the conventional 0.80). The paper reports 'no significant difference (t = -1.031, p = 0.488)' but this null result is uninterpretable—it could be due to low power rather than a true null effect. The paper acknowledges this limitation in the Discussion ('severe power limitation') but still presents the null result in the Abstract and Results as if it were informative.
  Action: Either: (1) Remove the spoken vs. written analysis from the main results and move it to a Limitations section, explicitly stating that 'no conclusions can be drawn about genre effects due to insufficient spoken treebank sample size (n=2)'. (2) Pool spoken treebanks by language family to increase sample size (e.g., combine all Indo-European spoken treebanks). (3) Use a permutation test or bootstrap method that doesn't rely on parametric assumptions given the small sample. (4) Acknowledge that the spoken sample size limitation is a major constraint and tone down all claims about 'no significant difference'.
- [MAJOR] (rigor) Reference [2] Gerdes et al. (2026) with arXiv:2607.01899 is dated July 2026, which is extremely recent (current date: 2026-07-20, meaning this preprint would be only days old). This raises concerns about whether this reference actually exists or if it was fabricated. Similarly, reference [15] Dobrovoljc (2025) 'Counting trees: a treebank-driven exploration of syntactic variation in speech and writing across languages' lists the journal volume as '0' which is unusual for a published paper. Reference [15] also has a DOI (10.1515/cllt-2025-0046) which should be verifiable. These reference issues undermine confidence in the paper's scholarship.
  Action: Verify all references, especially: (1) Gerdes et al. (2026) arXiv:2607.01899 - check if this preprint actually exists on arXiv.org. If not, remove or correct the citation. (2) Dobrovoljc (2025) - verify the publication details (journal, volume, issue, pages). The DOI 10.1515/cllt-2025-0046 should resolve to the correct paper. (3) Use a bibliography management tool (e.g., BibTeX with Semantic Scholar) to ensure all references are accurate and complete. (4) Ensure in-text citations match the reference list (check that [15] and [16] are correctly assigned).
- [MINOR] (methodology) The mixed-effects models use only random intercepts for language family, not random slopes. Barr et al. (2013) recommend starting with the maximal random effects structure, which would include random slopes for WALS effects by family. The paper notes in the Limitations section that 'We used only random intercepts for language family, not random slopes... Our simpler specification may underestimate standard errors.' However, this should be addressed in the main analysis, not just noted as a limitation.
  Action: Test models with random slopes for the main predictor (WALS 51A) by language family. If the model converges, compare the results with the random-intercept-only model using a likelihood ratio test. If the random slope model does not converge (singular fit), report this and use the simpler model, but justify the decision based on Bates et al. (2015) who recommend simplifying to a positive-definite variance-covariance matrix. Alternatively, use the maximal model but with regularization (e.g., rstanarm or brms for Bayesian mixed-effects models).
- [MINOR] (novelty) The paper claims to be the first to 'systematically link WALS typological features to DD distribution shape parameters using mixed-effects models across the full UD collection.' While this is largely true, the related work section does not adequately compare with Niu et al. (2023) who analyzed 4 languages and found a trade-off between syntactic and morphological complexity. The paper should more clearly articulate what NEW insights the larger-scale WALS-based analysis provides beyond Niu et al.
  Action: Strengthen the related work comparison with Niu et al. (2023): (1) State that Niu et al. analyzed only 4 languages without WALS features or mixed-effects models. (2) Explain how the current study's WALS-based approach across 41 treebanks provides more generalizable insights. (3) Compare the findings: Niu et al. found a trade-off between syntactic and morphological complexity—does the current study confirm or contradict this? The paper mentions that WALS 51A (locus of marking) is significant while WALS 20A (fusion) is not, which partially contradicts Niu et al.'s emphasis on morphological complexity. Elaborate on this discrepancy.
- [MINOR] (scope) The WALS feature mapping coverage is 11.7% (41 out of 350+ treebanks), which the paper acknowledges. However, the paper does not adequately discuss potential selection bias: treebanks with WALS mappings may differ systematically from those without. For example, well-studied languages (English, French, German) have WALS data, while low-resource languages may not. This could bias the results toward Indo-European languages (which dominate the dataset: 24 of 41 treebanks, 58.5%). The Limitations section mentions this briefly but does not quantify the potential bias.
  Action: Add a section on 'Potential Selection Bias' in the Discussion or Limitations. Analyze whether treebanks with vs. without WALS mappings differ in: (1) language family distribution (chi-square test), (2) mean dependency distance (t-test), (3) treebank size (correlation with WALS availability). If differences exist, acknowledge that the WALS-based results may not generalize to all UD languages. Consider using multiple imputation or other methods to handle missing WALS data, or at least provide sensitivity analyses.
- [MINOR] (clarity) Table 1 is referenced in the Results section ('Table 1 presents the fixed effects estimates for all WALS features') but is not provided in the text—only a [TABLE:table1] placeholder appears. Similarly, Figures 1, 2, and 3 are referenced but only appear as placeholders. For a complete paper, all tables and figures must be included with proper captions and axis labels. The reviewer cannot fully evaluate the results without seeing the actual Table 1 with coefficient estimates.
  Action: Include all tables and figures in the paper: (1) Add Table 1 with fixed effects estimates (β, SE, p-value, 95% CI) for all 5 WALS features × 2 DVs (a_param and b_param). (2) Ensure Figure 1, 2, 3 are properly specified with: exact data to plot, axis labels, caption. (3) The figure specifications should be detailed enough for a reader to understand what each figure shows without referring to the text. (4) Consider adding a table summarizing the ZA distribution fitting results (a_param, b_param) for all 41 treebanks.
</reviewer_feedback>



<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for the field's landscape, prior work, crowded lanes, and the novelty bar — consult it while revising so the updated hypothesis stays genuinely novel and well-positioned.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>

<task>
IMPORTANT: Your ONLY output is the revised hypothesis text. Do NOT run code, produce artifacts,
fix bugs, or attempt to address the evidence yourself — the next iteration of the invention loop
will generate fresh artifacts based on your revised hypothesis. Reflect and rewrite; nothing else.

Do NOT generate a completely new hypothesis. Take the current hypothesis and REVISE it
to incorporate new evidence. Keep the core idea — refine, narrow, or strengthen it.

1. Does the evidence support the hypothesis? Narrow or broaden scope as needed.
2. Which claims now have strong evidence? Which are still unsupported?
3. Should the hypothesis become more specific based on what we've learned?
4. If reviewer feedback is provided, address the critiques directly.

STABILITY IS OK: If progress is good and evidence supports the current direction, keep the
hypothesis similar or identical. Only make substantive changes when evidence clearly calls for
them — e.g., contradictory results, fundamental reviewer critiques, or findings that refine scope.

You must also classify two kinds of edges in the research trace:

(A) The H↔H edge — how does this revised hypothesis relate to the previous one?
    Set `relation_type` (Moulines's structuralist typology) to one of:
    - "evolution": refining specialised claims, same conceptual frame
    - "embedding": previous hypothesis is now a special case of a broader frame
    - "replacement": rejecting the previous frame entirely (Kuhnian shift)
    Set `relation_rationale` to a brief justification (≤120 chars).

(B) The A↔A edges — for each artifact created THIS iteration, classify each of its
    `in_dependencies` (predecessor → dependent) using MultiCite's citation-function
    typology (Lauscher et al., NAACL 2022) — emit one entry in `artifact_relations`
    per (predecessor, dependent) pair. Predecessors are ALWAYS artifacts from EARLIER
    iterations — artifacts within one iteration run in parallel and cannot depend on
    each other, so never emit a relation between two same-iteration artifacts (it
    will be dropped):
    - "background": predecessor is treated as background context
    - "motivation": predecessor motivated this artifact's research
    - "uses": this artifact uses the predecessor's data, method, or output
    - "extends": this artifact extends the predecessor
    - "similarities": this artifact's results agree with the predecessor's
    - "differences": this artifact's results disagree with the predecessor's
    Each `relation_rationale` must be ≤120 characters.

Output the COMPLETE revised hypothesis (with the H↔H relation fields) AND the full
list of A↔A `artifact_relations` for this iteration's new artifacts.
</task><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_txhWJXyNIa5t/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_txhWJXyNIa5t/3_invention_loop/iter_2/upd_hypo/upd_hypo/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ArtifactRelation": {
      "description": "One typed A\u2194A edge between a dependent artifact and one of its in_dependencies.\n\nMultiCite citation-function typology (Lauscher et al., NAACL 2022),\nreduced to 6 plain-English types.",
      "properties": {
        "from_id": {
          "description": "ID of the predecessor artifact (the one being depended on)",
          "title": "From Id",
          "type": "string"
        },
        "to_id": {
          "description": "ID of the dependent artifact (the new artifact this iteration)",
          "title": "To Id",
          "type": "string"
        },
        "relation_type": {
          "description": "MultiCite citation-function type for the predecessor\u2192dependent edge: 'background' \u2014 predecessor is treated as background context; 'motivation' \u2014 predecessor motivated this artifact's research; 'uses' \u2014 this artifact uses the predecessor's data, method, or output; 'extends' \u2014 this artifact extends the predecessor; 'similarities' \u2014 this artifact's results agree with the predecessor's; 'differences' \u2014 this artifact's results disagree with the predecessor's.",
          "enum": [
            "background",
            "motivation",
            "uses",
            "extends",
            "similarities",
            "differences"
          ],
          "title": "Relation Type",
          "type": "string"
        },
        "relation_rationale": {
          "description": "Brief rationale for this relation type (one short line, max 120 characters).",
          "maxLength": 120,
          "title": "Relation Rationale",
          "type": "string"
        }
      },
      "required": [
        "from_id",
        "to_id",
        "relation_type",
        "relation_rationale"
      ],
      "title": "ArtifactRelation",
      "type": "object"
    }
  },
  "description": "Revised hypothesis after reviewing iteration results.\n\nOutput matches the hypothesis dict structure so it can replace the\noriginal hypothesis in subsequent iterations.",
  "properties": {
    "title": {
      "description": "Revised hypothesis title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters); may be unchanged if still accurate.",
      "title": "Title",
      "type": "string"
    },
    "hypothesis": {
      "description": "Revised hypothesis statement \u2014 what we now believe based on evidence",
      "title": "Hypothesis",
      "type": "string"
    },
    "relation_rationale": {
      "description": "Brief rationale for the H\u2194H revision type (one short line, max 120 characters).",
      "maxLength": 120,
      "title": "Relation Rationale",
      "type": "string"
    },
    "confidence_delta": {
      "description": "How confidence changed: 'increased', 'decreased', or 'unchanged'",
      "title": "Confidence Delta",
      "type": "string"
    },
    "key_changes": {
      "description": "Bullet list of specific changes made to the hypothesis",
      "items": {
        "type": "string"
      },
      "title": "Key Changes",
      "type": "array"
    },
    "relation_type": {
      "description": "Moulines's structuralist typology of this hypothesis revision: 'evolution' \u2014 refining specialised claims while keeping the same conceptual frame; 'embedding' \u2014 the previous hypothesis is now a special case of a broader frame; 'replacement' \u2014 rejecting the previous frame entirely (incommensurable, Kuhnian revolution).",
      "enum": [
        "evolution",
        "embedding",
        "replacement"
      ],
      "title": "Relation Type",
      "type": "string"
    },
    "artifact_relations": {
      "description": "Typed A\u2194A edges for this iteration's new artifacts. Emit one entry per (predecessor \u2192 dependent) edge for every in_dependency on each artifact produced this iteration.",
      "items": {
        "$ref": "#/$defs/ArtifactRelation"
      },
      "title": "Artifact Relations",
      "type": "array"
    }
  },
  "required": [
    "title",
    "hypothesis",
    "relation_rationale",
    "confidence_delta",
    "key_changes",
    "relation_type"
  ],
  "title": "RevisedHypothesis",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `/ai-inventor/aii_data/runs/run_txhWJXyNIa5t/3_invention_loop/iter_2/upd_hypo/upd_hypo/.sdk_openhands_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-07-20 02:19:16 UTC

```
Direction: Computational Linguistics — Dependency Distance Minimization Across UD Treebanks. Something genuinely novel and groundbreaking that measures dependency-distance distributions across UD treebanks, investigates whether spoken language minimizes more than written, characterizes how typology interacts with the pattern, and identifies families that deviate. MUST use commul/universal_dependencies on HuggingFace.

Ambition: level 3 of 5 — phenomenological science: surface and rigorously characterize a new empirical regularity or anomaly in the data, even before a full theoretical explanation exists.

Reviewer: I am Kaja Dobrovoljc (JSI / University of Ljubljana). Calibrate from my existing papers. Cross-domain methods (information theory, mixed-effects models, sequence models) welcome — but keep them close to what I already know, not too far from my background.

Submission/Goal: a paper for ACL, EMNLP, or the Computational Linguistics journal. Audience: computational linguists and quantitative typologists. Tone: empirically rigorous, careful with linguistic detail, reproducible on public UD.
```

### [3] SYSTEM-USER prompt · 2026-07-20 02:20:31 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `<root>`: 'relation_rationale' is a required property
Every required field must be present and every field type must match the schema.

Please use the Write tool to overwrite `.sdk_openhands_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```
