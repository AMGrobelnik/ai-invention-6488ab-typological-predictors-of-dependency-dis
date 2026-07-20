# gen_full_paper — report_results

> Phase: `gen_paper_repo` · `gen_full_paper`
> Run: `run_txhWJXyNIa5t` — Typological Predictors of Dependency Distance Distribution Shapes in Universal Dependencies
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_full_paper` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-07-20 02:48:05 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_txhWJXyNIa5t/4_gen_paper_repo/_4_assemble_paper/paper/workspace`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_txhWJXyNIa5t/4_gen_paper_repo/_4_assemble_paper/paper/workspace/`:
GOOD: `/ai-inventor/aii_data/runs/run_txhWJXyNIa5t/4_gen_paper_repo/_4_assemble_paper/paper/workspace/file.py`, `/ai-inventor/aii_data/runs/run_txhWJXyNIa5t/4_gen_paper_repo/_4_assemble_paper/paper/workspace/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>

<task>
Create a publication-ready top-conference LaTeX paper with BibTeX from <paper_text> and <available_figures>, compile to PDF.
</task>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<paper_text>
title: >-
  Typological Predictors of Dependency Distance Distribution Shapes in Universal Dependencies
abstract: >-
  Dependency Distance Minimization (DDM) is a well-established cross-linguistic universal, but prior work focuses almost exclusively
  on mean dependency distance (MDD) as the summary statistic. This study investigates whether the shape parameters of dependency
  distance (DD) distributions—not merely their means—can be systematically predicted by typological features (word order type,
  morphological complexity, case marking) in a mixed-effects framework using data from Universal Dependencies treebanks. We
  fit Right Truncated Modified Zipf-Alekseev distributions to 41 treebanks with complete data (100% convergence rate) and
  show that WALS feature 51A (locus of marking in the clause) significantly predicts both distribution shape parameters: a_param
  (β = -0.024, p = 0.034) and b_param (β = 0.014, p = 0.018). Spoken vs. written genre analysis reveals no significant difference
  in dependency distance (t = -1.031, p = 0.488), limited by the small number of spoken treebanks with sufficient data (n
  = 2). Outlier detection identifies the Turkic language family as deviating from the universal DDM pattern. These findings
  demonstrate that specific typological constraints operate on distribution shape—not only on central tendency—and provide
  a more nuanced picture of how grammar and processing pressures interact to shape syntactic dependency structures.
paper_text: |-
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

  We analyzed treebanks from the commul/universal_dependencies dataset on HuggingFace [7], comprising 193 languages. For each non-root dependency in every sentence, we computed the dependency distance as the absolute difference between head and dependent positions. This yielded 979,098 dependency observations after filtering \footnote{Code: \url{https://github.com/AMGrobelnik/ai-invention-6488ab-typological-predictors-of-dependency-dis/tree/main/round-1/dataset-1}}.

  Treebanks were categorized by genre based on their names and metadata: (1) spoken (e.g., en_childes, fr_rhapsodie); (2) written formal (e.g., news, wiki treebanks); and (3) written informal (e.g., reddit, social media) .

  ### WALS Feature Mapping

  We mapped UD treebank languages to WALS typological features [6] using ISO 639-3 code matching. Five WALS features were selected based on their theoretical relevance to dependency distance:

  - **1A**: Order of Subject, Object, and Verb (word order type: SVO, SOV, VSO, etc.)
  - **20A**: Fusion of Inflectional Morphology (isolating, agglutinative, fusional)
  - **26A**: Exponence of Selected Inflectional Categories (minimal, moderate)
  - **49A**: Number of Cases (0, 2, 3-5, 6-8, 9+)
  - **51A**: Locus of Marking in the Clause (none, prefixing, suffixing)

  The mapping achieved 84.5% high-confidence mappings via ISO 639-3 code matching, covering 116 UD treebanks \footnote{Code: \url{https://github.com/AMGrobelnik/ai-invention-6488ab-typological-predictors-of-dependency-dis/tree/main/round-1/dataset-2}}. For each treebank, we extracted the WALS feature values for its language.

  ### Data Filtering

  For the distribution fitting and mixed-effects modeling, we applied two filtering criteria: (1) minimum of 1000 dependencies per treebank to ensure reliable parameter estimation following Liu et al. [5]; and (2) complete WALS feature data (no missing values for the five features). After filtering, 41 treebanks remained for analysis \footnote{Code: \url{https://github.com/AMGrobelnik/ai-invention-6488ab-typological-predictors-of-dependency-dis/tree/main/round-2/experiment-1}}.

  ## Distribution Fitting

  Following Liu et al. [5] and Popescu et al. [4], we fit the Right Truncated Modified Zipf-Alekseev (ZA) distribution to each treebank's DD distribution. The ZA distribution has probability mass function:

  $$P_x = P_1 \cdot x^{-(a + b\ln x)}, \quad x = 1, 2, 3, \ldots, n$$

  where $P_x$ is the probability of dependency distance $x$, $P_1$ is the normalization constant, $a$ and $b$ are shape parameters, and $n$ is the maximum observed dependency distance (truncation point).

  Parameters were estimated via Maximum Likelihood Estimation (MLE) using L-BFGS-B optimization with bounds in Python . The Kolmogorov-Smirnov test was used to assess goodness-of-fit for each treebank.

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

  Our dataset comprises 979,098 dependency observations from 193 languages across 350+ UD treebanks. After filtering for minimum dependencies (1000) and complete WALS mappings, 41 treebanks remained for the distribution fitting and mixed-effects modeling .

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
summary: >-
  This study fits Right Truncated Modified Zipf-Alekseev distributions to 41 UD treebanks and uses mixed-effects models to
  show that WALS locus of marking (51A) significantly predicts distribution shape parameters (a_param: β=-0.024, p=0.034;
  b_param: β=0.014, p=0.018). Spoken vs. written analysis shows no significant difference (p=0.488), limited by small spoken
  sample (n=2). Turkic family identified as outlier.
</paper_text>

<available_figures>
--- Item 1 ---
id: fig1
title: Research Overview
caption: >-
  Overview of the research pipeline: (1) Dependency distances are computed from UD treebanks, (2) WALS typological features
  are mapped to treebank languages, (3) Right Truncated Modified Zipf-Alekseev distributions are fit to each treebank's DD
  data, and (4) Mixed-effects models predict shape parameters from WALS features.
image_gen_detailed_description: >-
  Horizontal flow diagram with 4 boxes connected by arrows. Box 1: 'UD Treebanks' (light blue) with icon of tree structure.
  Box 2: 'WALS Features' (light green) with icon of globe. Box 3: 'ZA Distribution Fitting' (light yellow) with formula P_x
  = P_1 * x^{-(a + b*ln x)}. Box 4: 'Mixed-Effects Models' (light pink) with formula y = β0 + β1*WALS + u_family + ε. Arrow
  from 1 to 2, 2 to 3, 3 to 4. Sans-serif font, white background, clean professional style.
aspect_ratio: '21:9'
summary: >-
  Hero diagram showing the full research pipeline from UD treebanks to mixed-effects models
figure_path: figures/fig1_v0.jpg

--- Item 2 ---
id: fig2
title: Dataset Composition
caption: >-
  Distribution of treebanks by WALS features in the analyzed sample (n=41). (A) Word order type (WALS 1A), (B) Morphological
  fusion (WALS 20A), (C) Number of cases (WALS 49A), (D) Locus of marking (WALS 51A).
image_gen_detailed_description: >-
  Four-panel bar chart (2x2 layout). Panel A: Word order - SVO: 18 treebanks, SOV: 12, VSO: 3, Other: 8. Panel B: Fusion -
  Fusional: 20, Agglutinative: 12, Isolating: 6, Other: 3. Panel C: Cases - 0-2: 8, 3-5: 15, 6-8: 12, 9+: 6. Panel D: Locus
  - Suffixing: 22, Prefixing: 8, None: 11. All bars in blue color, white background, sans-serif font, axis labels: 'WALS Feature
  Value' (x), 'Number of Treebanks' (y).
aspect_ratio: '21:9'
summary: Shows the distribution of WALS feature values across the 41 analyzed treebanks
figure_path: figures/fig2_v0.jpg

--- Item 3 ---
id: fig3
title: Spoken vs Written Dependency Distance
caption: >-
  Distribution of dependency distances by genre. (A) Empirical distribution of DD values for spoken (blue) and written (red)
  treebanks. (B) Fitted ZA distributions for the two genres. Note: Only 2 spoken treebanks met inclusion criteria, limiting
  statistical power.
image_gen_detailed_description: >-
  Two-panel figure. Panel A: Bar chart showing frequency of dependency distances 1-15. Spoken (blue bars): DD=1: 35%, DD=2:
  28%, DD=3: 18%, DD=4: 10%, DD=5+: 9%. Written (red bars): DD=1: 32%, DD=2: 26%, DD=3: 20%, DD=4: 12%, DD=5+: 10%. Panel
  B: Line plot of fitted ZA distributions. Spoken line (blue): a=-0.225, b=1.056. Written line (red): a=0.742, b=0.335. X-axis:
  Dependency Distance (1-15), Y-axis: Probability density (0-0.4). Sans-serif font, white background.
aspect_ratio: '21:9'
summary: Compares dependency distance distributions between spoken and written genres
figure_path: figures/fig3_v0.jpg
</available_figures>

<figure_requirements>
CRITICAL: Include ALL figures from <available_figures>. No exceptions.

- Every figure MUST use \includegraphics{figures/filename.jpg}
- Do NOT skip, convert to tables, or describe without inserting
- Each needs: \begin{figure*|figure}[placement], \includegraphics, \caption, \label, \end{...} — pick env + placement by the figure's `aspect_ratio` field (see PLACEMENT below). Constrain every \includegraphics with `width=\linewidth,height=0.4\textheight,keepaspectratio` (single-column) or `width=\textwidth,height=0.45\textheight,keepaspectratio` (figure*). Use exactly these option keys — `max height=` is NOT valid LaTeX
- Use the `caption` field from each figure for \caption{...} — do NOT invent new captions
- Place figures where their [FIGURE:fig_id] markers appear in paper_text
- VERIFICATION: paper.tex MUST have exact same number of \includegraphics as <available_figures>
- Do NOT generate new figure images (no matplotlib, no PIL, no image generation). Use ONLY the pre-generated figures from <available_figures>. They were already created by a previous pipeline step.

PLACEMENT BY ASPECT RATIO (use the `aspect_ratio` field on each figure):
- `21:9` (architecture diagrams / hero figures): \begin{figure*}[!t] (full two-column width, top of page). The hero architecture diagram should appear EARLY in the paper — typically at the top of page 2. Marker placement in paper_text already determines this; preserve it.
- `16:9` (comparisons, multi-panel results): \begin{figure*}[!t] for full-width or \begin{figure}[!htbp] for single-column.
- `4:3` / `1:1` / `3:2` / `3:4` / `9:16`: \begin{figure}[!htbp] (single-column).
</figure_requirements>

<artifact_links>
The paper_text contains \footnote{Code: \url{...}} references linking to artifact source code
on GitHub. Include \usepackage{hyperref} and \usepackage{url}.
Preserve these exactly as-is — do not remove, rewrite, or convert them to plain text.
The URLs will not resolve yet (the repo is deployed after compilation) — do NOT try to verify or fix them.
</artifact_links>

<headings>
NEVER use inline math (``$...$``) inside ``\section{...}`` / ``\subsection{...}`` / ``\subsubsection{...}`` arguments — hyperref's bookmark builder errors out (``Token not allowed in a PDF string``) and the PDF outline breaks. If a section heading needs a math-looking term, use the text equivalent (``d star`` not ``$d^*$``, ``alpha-equivalent`` not ``$\alpha$-equivalent``) or wrap it in ``\texorpdfstring{$math$}{plain}``. Inline math inside body paragraphs is fine.
</headings>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-to-latex, aii-semscholar-bib.
TODO 2. Review <paper_text> and <available_figures>. Copy all figure images into ./figures/ in your workspace. Count figures — MUST include every one. Plan placements per section. Build `./references.bib` via aii_semscholar_bib__fetch — collect DOIs/ArXiv IDs from <paper_text> and batch-fetch all BibTeX in one call. Do NOT fabricate entries.
TODO 3. Create `./paper.tex` per aii-paper-to-latex skill's setup, write ALL sections, insert ALL figures from <available_figures>, include `./references.bib` via \bibliography. Compile to PDF per skill's process. Fix errors.
TODO 4. CRITICAL VERIFICATION: Run `grep -c 'includegraphics' paper.tex`, confirm count equals figures in <available_figures>. If not, add missing figures. Verify `./paper.pdf` was created.
TODO 5. VISUAL REVIEW: Write Python script to convert EVERY page of paper.pdf to PNG at 150 DPI (use pdf2image or pymupdf). Then read ALL page screenshots — each page image costs ~1,600 tokens so a 15-page paper is only ~24K tokens. You MUST read every page. The ONLY exception is if all page images would not fit in your remaining context — in that case, read as many as fit and state which pages you are skipping and why. Check every page for layout issues, overlapping figures, cut-off text, bad spacing, formatting problems. Fix issues and recompile.
TODO 6. FINAL READ: Check page count (`pdfinfo paper.pdf` or pymupdf). Read entire paper.pdf — check for missing sections, unclear explanations, inconsistencies, typos. Fix and recompile. The ONLY exception is if all pages would not fit in your remaining context — in that case, read as many pages as fit and state which pages you are skipping and why.
</todos>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_txhWJXyNIa5t/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FullPaperExpectedFiles": {
      "description": "All expected output files from full paper generation.",
      "properties": {
        "paper_tex_path": {
          "description": "Path to LaTeX source file. Example: 'paper.tex'",
          "title": "Paper Tex Path",
          "type": "string"
        },
        "paper_pdf_path": {
          "description": "Path to compiled PDF. Example: 'paper.pdf'",
          "title": "Paper Pdf Path",
          "type": "string"
        },
        "references_bib_path": {
          "description": "Path to BibTeX bibliography file. Example: 'references.bib'",
          "title": "References Bib Path",
          "type": "string"
        },
        "figure_paths": {
          "description": "Paths to all figure image files. Example: ['figures/fig1_v0.jpg', 'figures/fig2_v0.jpg']",
          "items": {
            "type": "string"
          },
          "title": "Figure Paths",
          "type": "array"
        }
      },
      "required": [
        "paper_tex_path",
        "paper_pdf_path",
        "references_bib_path",
        "figure_paths"
      ],
      "title": "FullPaperExpectedFiles",
      "type": "object"
    }
  },
  "description": "Full paper \u2014 structured output from paper generation.",
  "properties": {
    "title": {
      "description": "Paper title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance. Aim for about 4-8 words (~40 characters).",
      "maxLength": 90,
      "minLength": 12,
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "description": "Brief summary of the generated paper: sections written, figures included, compilation status",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/FullPaperExpectedFiles",
      "description": "All output files you created. Must include paper.tex, paper.pdf, references.bib, and paths to all figure files."
    }
  },
  "required": [
    "title",
    "summary",
    "out_expected_files"
  ],
  "title": "FullPaper",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `/ai-inventor/aii_data/runs/run_txhWJXyNIa5t/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.sdk_openhands_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-07-20 02:48:05 UTC

```
Direction: Computational Linguistics — Dependency Distance Minimization Across UD Treebanks. Something genuinely novel and groundbreaking that measures dependency-distance distributions across UD treebanks, investigates whether spoken language minimizes more than written, characterizes how typology interacts with the pattern, and identifies families that deviate. MUST use commul/universal_dependencies on HuggingFace.

Ambition: level 3 of 5 — phenomenological science: surface and rigorously characterize a new empirical regularity or anomaly in the data, even before a full theoretical explanation exists.

Reviewer: I am Kaja Dobrovoljc (JSI / University of Ljubljana). Calibrate from my existing papers. Cross-domain methods (information theory, mixed-effects models, sequence models) welcome — but keep them close to what I already know, not too far from my background.

Submission/Goal: a paper for ACL, EMNLP, or the Computational Linguistics journal. Audience: computational linguists and quantitative typologists. Tone: empirically rigorous, careful with linguistic detail, reproducible on public UD.
```

### [3] SKILL-INPUT — aii-paper-to-latex · 2026-07-20 02:48:26 UTC

The agent loaded the **aii-paper-to-latex** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-to-latex
description: LaTeX paper assembly and compilation. Covers document setup, figure inclusion from pre-generated JPEGs, compilation process, and output files. Use when assembling a paper from pre-written text and pre-generated figures into a compiled PDF.
---

## LaTeX Paper Assembly

Assembles a research paper from paper text, pre-generated figure JPEGs, and bibliography into a compiled PDF.

### Document Setup

```latex
\documentclass[11pt,letterpaper]{article}
\usepackage{graphicx, geometry, amsmath, hyperref, natbib, booktabs, xcolor, listings}
\geometry{margin=1in}
\hypersetup{colorlinks=true, linkcolor=black, citecolor=black, urlcolor=black}
```

### Figure Inclusion

CRITICAL: Include ALL figures. Every figure MUST appear in the paper.

```latex
\begin{figure}[!htbp]
  \centering
  \includegraphics[width=0.92\textwidth,keepaspectratio]{figures/filename.jpg}
  \caption{Descriptive caption.}
  \label{fig:label}
\end{figure}
```

Rules:
- ALWAYS use `[!htbp]` float placement (NOT `[t]` or `[h]` alone)
- ALWAYS constrain with `width` and `keepaspectratio` to prevent page takeover
- Every figure needs `\caption`, `\label`, and a `\ref` in the text
- Do NOT convert figures to tables or describe them without inserting the image
- Do NOT skip any figures

### Compilation Process

Run each command separately (do NOT chain with `&&` — pdflatex often exits non-zero on warnings, which would skip bibtex and leave citations as `??`):

```bash
pdflatex -interaction=nonstopmode paper.tex
bibtex paper
pdflatex -interaction=nonstopmode paper.tex
pdflatex -interaction=nonstopmode paper.tex
```

All four commands are required. Skipping bibtex causes `??` in all citations.
Fix any errors between runs. Verify `./paper.pdf` was created.

### Output Files

- `./paper.tex` — LaTeX source
- `./references.bib` — bibliography file
- `./paper.pdf` — compiled PDF
- `./figures/*.jpg` — all figure images (pre-generated, copied into workspace)
````

### [4] SKILL-INPUT — aii-semscholar-bib · 2026-07-20 02:48:26 UTC

The agent loaded the **aii-semscholar-bib** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-semscholar-bib
description: Build bibliographies using Semantic Scholar. Batch-fetch BibTeX for papers by DOI, ArXiv ID, or title. Use when writing papers, generating reference lists, or building .bib files.
---

## Tool: `aii_semscholar_bib__fetch`

Batch-fetch BibTeX entries from Semantic Scholar. Pass all references in a single call — the tool handles batching internally.

### How it works

1. **DOI/ArXiv refs** → batched into POST /paper/batch calls (up to 500 per API call, auto-chunked)
2. **Title-only refs** → individual GET /paper/search/match (1s delay between)
3. **Post-process** → fix entry type, fix citation key (AuthorYYYY), inject DOI

The ability server runs a single worker (`max_threads: 1`). Multiple concurrent tool calls are queued — each runs independently (no cross-request aggregation). Batching happens within each request.

### Input format

```json
{
  "references": [
    {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
    {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
    {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
  ]
}
```

Each reference object can have:
- `doi` — DOI string (ArXiv DOIs like `10.48550/arXiv.XXXX.XXXXX` auto-convert to ArXiv IDs)
- `arxiv` — ArXiv ID (e.g. `"2305.14325"`)
- `title` — Paper title (used for search/match when no DOI/ArXiv)
- `author` — First author last name (for cleaner citation key)
- `year` — Publication year (int, for citation key)

At least one of `doi`, `arxiv`, or `title` is required per reference.

### Output format

```json
{
  "success": true,
  "bib_text": "@inproceedings{Vaswani2017, ...}\n\n@article{Wei2022, ...}",
  "total": 3,
  "found": 3,
  "failed_count": 0,
  "entries": [{"citation_key": "Vaswani2017", "bibtex": "...", "title": "...", "doi": "...", "arxiv": ""}],
  "failed": []
}
```

### Workflow

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in **one call**
3. Save `bib_text` from the response to your `references.bib` file
4. Check `failed` — for any missed papers, follow the **fallback procedure** below

### Fallback for failed references (MANDATORY)

NEVER fabricate BibTeX. For each failed reference:
1. **WebSearch** for `"Title" author year` (try `site:arxiv.org` too)
2. **WebFetch** the paper page → extract title, authors, year, venue, DOI/ArXiv ID
3. If DOI/ArXiv found → retry `aii_semscholar_bib__fetch` with it
4. Last resort: write BibTeX by hand using **only verified info from the actual paper page**

---

### CLI (for manual use / debugging)

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-semscholar-bib" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_semscholar_bib__fetch.py --refs '[
  {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
  {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
  {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
]'
```

`--json, -j` — output raw JSON instead of .bib text

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [5] SYSTEM-USER prompt · 2026-07-20 02:59:46 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `title`: 'Typological Predictors of Dependency Distance Distribution Shapes in Universal Dependencies' is too long (at most 90 characters, got 91)
Every required field must be present and every field type must match the schema.

Please use the Write tool to overwrite `.sdk_openhands_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```
