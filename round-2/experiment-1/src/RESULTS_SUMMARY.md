# Experiment Results Summary

## Overview
- **Date**: 2024-07-20
- **Experiment**: Fit ZA distributions and run mixed-effects models on UD treebanks
- **Status**: COMPLETED SUCCESSFULLY

## Key Results

### 1. ZA Distribution Fitting
- **Total treebanks processed**: 41
- **Successful fits**: 41 (100% convergence rate)
- **Mean a_param**: 0.904 (shape parameter)
- **Mean b_param**: 0.322 (log-modification parameter)

### 2. Spoken vs Written Analysis
- **t-statistic**: -1.031
- **p-value**: 0.488 (not significant)
- **Cohen's d**: -0.856
- **Interpretation**: No significant difference in dependency distance between spoken and written treebanks

### 3. Mixed-Effects Models
Significant predictors (p < 0.05):
- **a_param ~ wals_51A_value**: β = -0.024, p = 0.034 (Case alignment affects shape)
- **b_param ~ wals_51A_value**: β = 0.014, p = 0.018 (Case alignment affects log-modification)

### 4. Outlier Detection
- **2 outlier families detected**: Turkic (effects: 0.719 for a_param, -0.291 for b_param)

### 5. Robustness Checks
- Bootstrap confidence intervals computed
- Distribution comparison (ZA vs exponential) completed
- FDR correction note added

## Output Files
- **method_out.json**: Main results file (51K)
- **run.log**: Full experiment log
- **logs/run.log**: Detailed log with DEBUG information

## Data Coverage
- **Treebanks with complete data**: 41 (out of 106 merged)
- **Minimum dependencies per treebank**: 1000
- **WALS features used**: 1A, 20A, 26A, 49A, 51A

## Next Steps
1. Analyze significant WALS predictors in more detail
2. Investigate Turkic family outliers
3. Prepare results for paper writing
4. Consider running with relaxed minimum dependency threshold if more treebanks needed

## Technical Notes
- ZA distribution fitting: Right Truncated Modified Zipf-Alekseev distribution
- Mixed-effects models: Random intercept for language family
- Optimization: L-BFGS-B with bounds
- All code implemented in method.py with proper logging and error handling
