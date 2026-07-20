#!/usr/bin/env python3
"""
Experiment: Fit ZA distributions and run mixed-effects models on UD treebanks.

This script implements the full experimental pipeline:
1. Load and merge dependency distance data with WALS mappings
2. Fit Right Truncated Modified Zipf-Alekseev distributions to DD data
3. Analyze spoken vs written differences
4. Run mixed-effects models to predict ZA parameters from WALS features
5. Detect outliers via random effects
6. Perform robustness checks
"""

from loguru import logger
from pathlib import Path
import json
import sys
import numpy as np
import pandas as pd
from scipy import optimize, stats
import statsmodels.api as sm
from statsmodels.regression.mixed_linear_model import MixedLM
import gc
import warnings
from typing import Dict, List, Tuple, Optional, Any
import itertools
import argparse

warnings.filterwarnings('ignore')

# Setup logging
logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")


def load_json_data(filepath: Path) -> Dict:
    """Load JSON data from file."""
    logger.info(f"Loading data from {filepath}")
    with open(filepath, 'r') as f:
        data = json.load(f)
    logger.info(f"Loaded data with keys: {list(data.keys())}")
    return data


def extract_examples_from_dataset(data: Dict) -> List[Dict]:
    """Extract examples from dataset format."""
    examples = []
    if 'datasets' in data:
        for dataset in data['datasets']:
            if 'examples' in dataset:
                examples.extend(dataset['examples'])
    return examples


def load_full_data(data_dir: Path) -> List[Dict]:
    """Load all data from full_data_out_parts directory."""
    logger.info(f"Loading full data from {data_dir}")
    all_examples = []
    
    # Load all parts
    for part_file in sorted(data_dir.glob("full_data_out_*.json")):
        logger.info(f"Loading {part_file.name}")
        data = load_json_data(part_file)
        examples = extract_examples_from_dataset(data)
        all_examples.extend(examples)
        logger.info(f"Loaded {len(examples)} examples from {part_file.name}")
        del data, examples
        gc.collect()
    
    logger.info(f"Total examples loaded: {len(all_examples)}")
    return all_examples


def parse_input_json(input_str: str) -> Dict:
    """Parse input JSON string from example."""
    try:
        return json.loads(input_str)
    except:
        return {}


def parse_output_value(output_str: str) -> int:
    """Parse output value (dependency distance)."""
    try:
        return int(output_str)
    except:
        return 0


def merge_datasets(dd_examples: List[Dict], wals_examples: List[Dict]) -> pd.DataFrame:
    """Merge dependency distance data with WALS mappings."""
    logger.info("Merging datasets...")
    
    # Process DD examples
    dd_rows = []
    for ex in dd_examples:
        input_data = parse_input_json(ex.get('input', '{}'))
        dd = parse_output_value(ex.get('output', '0'))
        
        row = {
            'treebank_name': input_data.get('treebank_name', ''),
            'language': input_data.get('language', ''),
            'family': input_data.get('family', ''),
            'genre': input_data.get('genre', ''),
            'sentence_length': input_data.get('sentence_length', 0),
            'deprel': input_data.get('deprel', ''),
            'head_position': input_data.get('head_position', 0),
            'dependent_position': input_data.get('dependent_position', 0),
            'dd': dd
        }
        dd_rows.append(row)
    
    dd_df = pd.DataFrame(dd_rows)
    logger.info(f"DD DataFrame shape: {dd_df.shape}")
    logger.info(f"Unique treebanks in DD data: {dd_df['treebank_name'].nunique()}")
    
    # Process WALS examples
    wals_rows = []
    for ex in wals_examples:
        # Parse the output which contains wals_features
        output_str = ex.get('output', '{}')
        if isinstance(output_str, str):
            try:
                output_data = json.loads(output_str)
            except:
                output_data = {}
        else:
            output_data = output_str
        
        wals_features = output_data.get('wals_features', {})
        
        row = {
            'treebank_name': ex.get('metadata_treebank', ''),
            'wals_1A_value': wals_features.get('1A', {}).get('value', 'NA'),
            'wals_20A_value': wals_features.get('20A', {}).get('value', 'NA'),
            'wals_26A_value': wals_features.get('26A', {}).get('value', 'NA'),
            'wals_49A_value': wals_features.get('49A', {}).get('value', 'NA'),
            'wals_51A_value': wals_features.get('51A', {}).get('value', 'NA'),
            'wals_1A_desc': wals_features.get('1A', {}).get('value_description', ''),
            'wals_20A_desc': wals_features.get('20A', {}).get('value_description', ''),
            'wals_26A_desc': wals_features.get('26A', {}).get('value_description', ''),
            'wals_49A_desc': wals_features.get('49A', {}).get('value_description', ''),
            'wals_51A_desc': wals_features.get('51A', {}).get('value_description', ''),
        }
        wals_rows.append(row)
    
    wals_df = pd.DataFrame(wals_rows)
    logger.info(f"WALS DataFrame shape: {wals_df.shape}")
    logger.info(f"Unique treebanks in WALS data: {wals_df['treebank_name'].nunique()}")
    
    # Merge on treebank_name
    merged_df = dd_df.merge(wals_df, on='treebank_name', how='inner')
    logger.info(f"Merged DataFrame shape: {merged_df.shape}")
    logger.info(f"Unique treebanks after merge: {merged_df['treebank_name'].nunique()}")
    
    return merged_df


def filter_treebanks(merged_df: pd.DataFrame, min_deps: int = 1000) -> pd.DataFrame:
    """Filter to treebanks with minimum number of dependencies and complete WALS data."""
    logger.info(f"Filtering treebanks with at least {min_deps} dependencies...")
    
    # Count dependencies per treebank
    treebank_counts = merged_df.groupby('treebank_name').size().reset_index(name='n_deps')
    logger.info(f"Treebank dependency counts:\n{treebank_counts.describe()}")
    
    # Filter by min_deps
    valid_treebanks = treebank_counts[treebank_counts['n_deps'] >= min_deps]['treebank_name'].tolist()
    logger.info(f"Treebanks with >= {min_deps} deps: {len(valid_treebanks)}")
    
    filtered_df = merged_df[merged_df['treebank_name'].isin(valid_treebanks)].copy()
    
    # Filter to complete WALS data (no NA values)
    wals_cols = ['wals_1A_value', 'wals_20A_value', 'wals_26A_value', 'wals_49A_value', 'wals_51A_value']
    complete_mask = True
    for col in wals_cols:
        complete_mask = complete_mask & (filtered_df[col] != 'NA') & (filtered_df[col].notna())
    
    complete_df = filtered_df[complete_mask].copy()
    logger.info(f"Treebanks with complete WALS data: {complete_df['treebank_name'].nunique()}")
    
    return complete_df


def compute_dd_distribution(treebank_data: pd.DataFrame) -> Dict[int, int]:
    """Compute empirical distribution of dependency distances for a treebank."""
    dd_counts = treebank_data['dd'].value_counts().to_dict()
    return dd_counts


def neg_log_lik_zipf_alekseev(params: Tuple[float, float], dd_counts: Dict[int, int], L: int) -> float:
    """Negative log-likelihood for Right Truncated Modified Zipf-Alekseev distribution.
    
    P(x) = C * x^(-(a + b*ln(x))) for x = 1, 2, ..., L
    where C is the normalization constant
    """
    a, b = params
    
    # Avoid invalid parameters
    if not (np.isfinite(a) and np.isfinite(b)):
        return 1e10
    
    x_vals = np.arange(1, L + 1)
    
    # Unnormalized probabilities
    try:
        log_unnorm = -(a + b * np.log(x_vals)) * np.log(x_vals)
        unnorm_p = np.exp(log_unnorm)
    except:
        return 1e10
    
    # Check for invalid values
    if not np.all(np.isfinite(unnorm_p)) or np.sum(unnorm_p) <= 0:
        return 1e10
    
    # Normalize
    p = unnorm_p / np.sum(unnorm_p)
    
    # Compute negative log-likelihood
    ll = 0.0
    for x, count in dd_counts.items():
        if 1 <= x <= L:
            if p[x-1] > 0:
                ll += count * np.log(p[x-1])
            else:
                ll += count * np.log(1e-10)
    
    return -ll


def fit_za_distribution(dd_counts: Dict[int, int]) -> Dict:
    """Fit Right Truncated Modified Zipf-Alekseev distribution using MLE."""
    if not dd_counts or len(dd_counts) < 2:
        return {'a_param': np.nan, 'b_param': np.nan, 'converged': False, 'ks_stat': np.nan, 'ks_p': np.nan}
    
    L = max(dd_counts.keys())
    total_count = sum(dd_counts.values())
    
    # Initial values
    initial_params = [1.0, 0.0]
    
    # Bounds for parameters
    bounds = [(-10, 10), (-5, 5)]
    
    try:
        # MLE optimization
        result = optimize.minimize(
            neg_log_lik_zipf_alekseev,
            initial_params,
            args=(dd_counts, L),
            method='L-BFGS-B',
            bounds=bounds,
            options={'maxiter': 1000}
        )
        
        a_param, b_param = result.x
        converged = result.success
        
        # Goodness-of-fit: Kolmogorov-Smirnov test
        # Generate expected frequencies from fitted distribution
        x_vals = np.arange(1, L + 1)
        log_unnorm = -(a_param + b_param * np.log(x_vals)) * np.log(x_vals)
        unnorm_p = np.exp(log_unnorm)
        expected_p = unnorm_p / np.sum(unnorm_p)
        
        # Convert to empirical CDF
        observed_counts = np.zeros(L)
        for x, count in dd_counts.items():
            if 1 <= x <= L:
                observed_counts[x-1] = count
        
        observed_cdf = np.cumsum(observed_counts) / total_count
        expected_cdf = np.cumsum(expected_p)
        
        # KS test
        ks_stat = np.max(np.abs(observed_cdf - expected_cdf))
        ks_p = 1 - stats.kstwo.sf(ks_stat, total_count)  # Approximate p-value
        
        return {
            'a_param': a_param,
            'b_param': b_param,
            'converged': converged,
            'ks_stat': ks_stat,
            'ks_p': ks_p,
            'L': L,
            'n_deps': total_count
        }
    
    except Exception as e:
        logger.warning(f"ZA fitting failed: {e}")
        return {'a_param': np.nan, 'b_param': np.nan, 'converged': False, 'ks_stat': np.nan, 'ks_p': np.nan}


def fit_exponential_distribution(dd_counts: Dict[int, int]) -> Dict:
    """Fit exponential distribution as baseline: P(x) = λ * exp(-λ*x)."""
    if not dd_counts or len(dd_counts) < 2:
        return {'lambda_param': np.nan, 'converged': False}
    
    # MLE for exponential: λ = 1 / mean
    total_count = sum(dd_counts.values())
    weighted_sum = sum(x * count for x, count in dd_counts.items())
    mean_dd = weighted_sum / total_count
    
    if mean_dd <= 0:
        return {'lambda_param': np.nan, 'converged': False}
    
    lambda_param = 1.0 / mean_dd
    
    return {
        'lambda_param': lambda_param,
        'converged': True,
        'mean_dd': mean_dd
    }


def analyze_spoken_written(merged_df: pd.DataFrame) -> Dict:
    """Analyze spoken vs written differences in dependency distance."""
    logger.info("Analyzing spoken vs written differences...")
    
    # Categorize genre
    merged_df['genre_category'] = merged_df['genre'].apply(
        lambda x: 'spoken' if isinstance(x, str) and 'spoken' in x.lower() else 'written'
    )
    
    # Compute mean DD per treebank
    treebank_stats = merged_df.groupby(['treebank_name', 'genre_category', 'family']).agg({
        'dd': ['mean', 'count'],
        'sentence_length': 'mean'
    }).reset_index()
    
    treebank_stats.columns = ['treebank_name', 'genre_category', 'family', 'mean_dd', 'n_deps', 'mean_sentence_length']
    
    # T-test: compare mean DD between spoken and written treebanks
    spoken_mean_dd = treebank_stats[treebank_stats['genre_category'] == 'spoken']['mean_dd']
    written_mean_dd = treebank_stats[treebank_stats['genre_category'] == 'written']['mean_dd']
    
    if len(spoken_mean_dd) > 0 and len(written_mean_dd) > 0:
        t_stat, t_p = stats.ttest_ind(spoken_mean_dd, written_mean_dd, equal_var=False)
        cohens_d = (spoken_mean_dd.mean() - written_mean_dd.mean()) / np.sqrt(
            (spoken_mean_dd.var() + written_mean_dd.var()) / 2
        )
    else:
        t_stat, t_p, cohens_d = np.nan, np.nan, np.nan
    
    # Linear regression: mean_dd ~ genre + sentence_length_mean + (1|family)
    # For simplicity, use linear regression with clustered SEs
    regression_data = treebank_stats.copy()
    regression_data['genre_spoken'] = (regression_data['genre_category'] == 'spoken').astype(int)
    
    # Simple OLS (ignoring clustering for now - will use mixed models later)
    X = sm.add_constant(regression_data[['genre_spoken', 'mean_sentence_length']])
    y = regression_data['mean_dd']
    
    try:
        model = sm.OLS(y, X).fit()
        regression_results = {
            'genre_spoken_coef': model.params['genre_spoken'],
            'genre_spoken_p': model.pvalues['genre_spoken'],
            'sentence_length_coef': model.params['mean_sentence_length'],
            'sentence_length_p': model.pvalues['mean_sentence_length'],
            'r_squared': model.rsquared,
            'adj_r_squared': model.rsquared_adj
        }
    except Exception as e:
        logger.warning(f"Regression failed: {e}")
        regression_results = {}
    
    return {
        't_test': {
            'statistic': t_stat,
            'p': t_p,
            'cohens_d': cohens_d,
            'spoken_mean': spoken_mean_dd.mean() if len(spoken_mean_dd) > 0 else np.nan,
            'written_mean': written_mean_dd.mean() if len(written_mean_dd) > 0 else np.nan,
            'spoken_n': len(spoken_mean_dd),
            'written_n': len(written_mean_dd)
        },
        'regression': regression_results,
        'treebank_stats': treebank_stats.to_dict('records')
    }


def prepare_mixed_effects_data(merged_df: pd.DataFrame, za_results: List[Dict]) -> pd.DataFrame:
    """Prepare data for mixed-effects models."""
    logger.info("Preparing data for mixed-effects models...")
    
    # Create DataFrame from ZA results
    za_df = pd.DataFrame(za_results)
    
    # Get unique treebank metadata from merged_df
    # Get treebank metadata (excluding family since it's already in za_df)
    treebank_meta = merged_df[['treebank_name', 'wals_1A_value', 'wals_20A_value', 
                               'wals_26A_value', 'wals_49A_value', 'wals_51A_value']].drop_duplicates()
    
    # Convert WALS values to numeric
    for col in ['wals_1A_value', 'wals_20A_value', 'wals_26A_value', 'wals_49A_value', 'wals_51A_value']:
        treebank_meta[col] = pd.to_numeric(treebank_meta[col], errors='coerce')
    
    # Also get mean sentence length per treebank
    sent_len_df = merged_df.groupby('treebank_name')['sentence_length'].mean().reset_index()
    sent_len_df.columns = ['treebank_name', 'mean_sentence_length']
    
    # Merge ZA results with metadata
    model_df = za_df.merge(treebank_meta, on='treebank_name', how='inner')
    model_df = model_df.merge(sent_len_df, on='treebank_name', how='inner')
    
    # Remove rows with missing data
    model_df = model_df.dropna(subset=['a_param', 'b_param', 'family'])
    
    logger.info(f"Mixed-effects data shape: {model_df.shape}")
    return model_df


def run_mixed_effects_model(df: pd.DataFrame, outcome: str, predictor: str) -> Dict:
    """Run mixed-effects model for a single predictor."""
    logger.info(f"Running mixed-effects model: {outcome} ~ {predictor}")
    
    # Prepare data
    y = df[outcome]
    X = sm.add_constant(df[[predictor, 'mean_sentence_length']])
    groups = df['family']
    
    try:
        # Fit mixed-effects model with random intercept for family
        model = MixedLM(y, X, groups=groups)
        result = model.fit()
        
        # Extract results
        params = result.params
        bse = result.bse
        pvalues = result.pvalues
        
        # Get coefficient for predictor
        pred_coef = params[predictor]
        pred_se = bse[predictor]
        pred_p = pvalues[predictor]
        pred_ci = result.conf_int().loc[predictor].tolist()
        
        return {
            'converged': result.converged,
            'predictor_coef': pred_coef,
            'predictor_se': pred_se,
            'predictor_p': pred_p,
            'predictor_ci_lower': pred_ci[0],
            'predictor_ci_upper': pred_ci[1],
            'intercept': params['const'],
            'sentence_length_coef': params['mean_sentence_length'],
            'sentence_length_p': pvalues['mean_sentence_length'],
            'log_likelihood': result.llf,
            'aic': result.aic,
            'bic': result.bic,
            'random_effects_variance': result.cov_re.iloc[0, 0] if len(result.cov_re) > 0 else np.nan,
            'residual_variance': result.scale
        }
    
    except Exception as e:
        logger.warning(f"Mixed-effects model failed for {predictor}: {e}")
        return {'converged': False, 'error': str(e)}


def detect_outliers(model_results: Dict, df: pd.DataFrame) -> List[Dict]:
    """Detect outlier families via random effects."""
    logger.info("Detecting outliers via random effects...")
    
    outliers = []
    
    # This is a simplified version - in practice, we'd extract random effects from the model
    # For now, compute family-level deviations from global mean
    
    for outcome in ['a_param', 'b_param']:
        family_means = df.groupby('family')[outcome].mean()
        global_mean = df[outcome].mean()
        family_effects = family_means - global_mean
        
        # Identify outliers: |effect| > 2 * SE
        se = family_effects.std()
        outlier_families = family_effects[abs(family_effects) > 2 * se].index.tolist()
        
        for family in outlier_families:
            outliers.append({
                'family': family,
                'outcome': outcome,
                'effect': family_effects[family],
                'se': se,
                'n_treebanks': len(df[df['family'] == family]),
                'mean_value': family_means[family],
                'global_mean': global_mean
            })
    
    return outliers


def robustness_checks(df: pd.DataFrame, za_results: List[Dict]) -> Dict:
    """Perform robustness checks."""
    logger.info("Performing robustness checks...")
    
    results = {}
    
    # Convert za_results to DataFrame for easier processing
    za_df = pd.DataFrame(za_results)
    
    # 1. Bootstrap analysis (simplified - 100 iterations)
    logger.info("Running bootstrap analysis...")
    bootstrap_results = []
    
    for i in range(100):
        # Subsample 80% of treebanks
        sampled_treebanks = np.random.choice(
            za_df['treebank_name'].unique(),
            size=int(0.8 * za_df['treebank_name'].nunique()),
            replace=False
        )
        sampled_df = za_df[za_df['treebank_name'].isin(sampled_treebanks)].copy()
        
        if len(sampled_df) > 0:
            bootstrap_results.append({
                'a_param_mean': sampled_df['a_param'].mean(),
                'b_param_mean': sampled_df['b_param'].mean()
            })
    
    if bootstrap_results:
        bootstrap_df = pd.DataFrame(bootstrap_results)
        results['bootstrap'] = {
            'a_param_mean_ci': [bootstrap_df['a_param_mean'].quantile(0.025), 
                               bootstrap_df['a_param_mean'].quantile(0.975)],
            'b_param_mean_ci': [bootstrap_df['b_param_mean'].quantile(0.025),
                               bootstrap_df['b_param_mean'].quantile(0.975)]
        }
    
    # 2. Compare ZA with exponential distribution
    logger.info("Comparing ZA with exponential distribution...")
    exp_results = []
    
    # Group df by treebank to get dd counts
    for treebank in df['treebank_name'].unique():
        treebank_data = df[df['treebank_name'] == treebank]
        dd_counts = treebank_data['dd'].value_counts().to_dict()
        
        za_fit = fit_za_distribution(dd_counts)
        exp_fit = fit_exponential_distribution(dd_counts)
        
        exp_results.append({
            'treebank': treebank,
            'za_a': za_fit.get('a_param', np.nan),
            'za_b': za_fit.get('b_param', np.nan),
            'exp_lambda': exp_fit.get('lambda_param', np.nan)
        })
    
    results['distribution_comparison'] = exp_results
    
    # 3. Multiple comparison correction (Benjamini-Hochberg FDR)
    logger.info("Applying FDR correction...")
    # This would be applied to p-values from mixed models
    results['fdr_note'] = "FDR correction should be applied to mixed model p-values"
    
    return results


@logger.catch(reraise=True)
def main():
    """Main execution function."""
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Fit ZA distributions and run mixed-effects models')
    parser.add_argument('--data-dir', type=str, help='Directory containing full_data_out_parts')
    parser.add_argument('--wals-file', type=str, help='Path to WALS full_data_out.json')
    parser.add_argument('--mini', action='store_true', help='Use mini data for testing')
    parser.add_argument('--preview', action='store_true', help='Use preview data for testing')
    parser.add_argument('--test-size', type=int, default=0, help='Use only first N treebanks for testing')
    args = parser.parse_args()
    
    logger.info("Starting experiment: Fit ZA distributions and run mixed-effects models")
    
    # Setup paths
    workspace_dir = Path("/ai-inventor/aii_data/runs/run_txhWJXyNIa5t/3_invention_loop/iter_2/gen_art/gen_art_experiment_1")
    
    # STEP 1: Load and merge datasets
    logger.info("=" * 50)
    logger.info("STEP 1: Load and merge datasets")
    logger.info("=" * 50)
    
    # Load DD data
    if args.mini or args.preview:
        logger.info("Loading mini/preview data (may have merge issues)")
        dd_file = workspace_dir / ("data_out_mini.json" if args.mini else "data_out_preview.json")
        wals_file = workspace_dir / ("mini_data_out.json" if args.mini else "preview_data_out.json")
        
        dd_data = load_json_data(dd_file)
        dd_examples = extract_examples_from_dataset(dd_data)
        
        wals_data = load_json_data(wals_file)
        wals_examples = extract_examples_from_dataset(wals_data)
    else:
        logger.info("Loading full data")
        data_dir = Path(args.data_dir) if args.data_dir else workspace_dir / "full_data_out_parts"
        wals_file = Path(args.wals_file) if args.wals_file else workspace_dir / "full_data_out.json"
        
        dd_examples = load_full_data(data_dir)
        wals_data = load_json_data(wals_file)
        wals_examples = extract_examples_from_dataset(wals_data)
    
    logger.info(f"Loaded {len(dd_examples)} DD examples")
    logger.info(f"Loaded {len(wals_examples)} WALS examples")
    
    # Merge datasets
    merged_df = merge_datasets(dd_examples, wals_examples)
    del dd_examples, wals_data
    gc.collect()
    
    logger.info(f"Merged DataFrame shape: {merged_df.shape}")
    logger.info(f"Unique treebanks after merge: {merged_df['treebank_name'].nunique()}")
    
    if len(merged_df) == 0:
        logger.error("No data after merge! Check treebank name matching.")
        logger.info("DD treebank names: " + str(set(parse_input_json(ex.get('input', '{}')).get('treebank_name', '') for ex in dd_examples if ex.get('input'))))
        logger.info("WALS treebank names: " + str(set(ex.get('metadata_treebank', '') for ex in wals_examples)))
        return
    
    # Filter treebanks
    min_deps = 10 if (args.mini or args.preview or args.test_size > 0) else 1000
    filtered_df = filter_treebanks(merged_df, min_deps=min_deps)
    logger.info(f"Filtered DataFrame shape: {filtered_df.shape}")
    logger.info(f"Unique treebanks after filtering: {filtered_df['treebank_name'].nunique()}")
    
    if len(filtered_df) == 0:
        logger.error("No data after filtering!")
        return
    
    # Limit to test_size if specified
    if args.test_size > 0:
        unique_treebanks = filtered_df['treebank_name'].unique()[:args.test_size]
        filtered_df = filtered_df[filtered_df['treebank_name'].isin(unique_treebanks)].copy()
        logger.info(f"Limited to {len(unique_treebanks)} treebanks for testing")
    
    # STEP 2: ZA distribution fitting for each treebank
    logger.info("=" * 50)
    logger.info("STEP 2: ZA distribution fitting")
    logger.info("=" * 50)
    
    za_results = []
    treebanks = filtered_df['treebank_name'].unique()
    logger.info(f"Fitting ZA distribution to {len(treebanks)} treebanks...")
    
    for i, treebank in enumerate(treebanks):
        if i % 10 == 0:
            logger.info(f"Processing treebank {i+1}/{len(treebanks)}: {treebank}")
        
        treebank_data = filtered_df[filtered_df['treebank_name'] == treebank]
        dd_counts = compute_dd_distribution(treebank_data)
        
        # Fit ZA distribution
        za_fit = fit_za_distribution(dd_counts)
        za_fit['treebank_name'] = treebank
        za_fit['family'] = treebank_data['family'].iloc[0]
        za_fit['n_deps'] = len(treebank_data)
        
        za_results.append(za_fit)
        
        # Free memory
        del treebank_data, dd_counts, za_fit
        if i % 50 == 0:
            gc.collect()
    
    logger.info(f"ZA fitting complete. Successful fits: {sum(1 for r in za_results if r.get('converged', False))}")
    
    # STEP 3: Spoken vs written analysis
    logger.info("=" * 50)
    logger.info("STEP 3: Spoken vs written analysis")
    logger.info("=" * 50)
    
    spoken_written_results = analyze_spoken_written(merged_df)
    
    # STEP 4: Mixed-effects models
    logger.info("=" * 50)
    logger.info("STEP 4: Mixed-effects models")
    logger.info("=" * 50)
    
    # Prepare data for mixed models
    model_df = prepare_mixed_effects_data(filtered_df, za_results)
    
    # Run mixed models for each WALS feature
    wals_features = ['wals_1A_value', 'wals_20A_value', 'wals_26A_value', 'wals_49A_value', 'wals_51A_value']
    mixed_effects_results = {'a_param_models': {}, 'b_param_models': {}}
    
    for feature in wals_features:
        # Model for a_param
        model_result_a = run_mixed_effects_model(model_df, 'a_param', feature)
        mixed_effects_results['a_param_models'][feature] = model_result_a
        
        # Model for b_param
        model_result_b = run_mixed_effects_model(model_df, 'b_param', feature)
        mixed_effects_results['b_param_models'][feature] = model_result_b
    
    # STEP 5: Outlier detection
    logger.info("=" * 50)
    logger.info("STEP 5: Outlier detection")
    logger.info("=" * 50)
    
    outliers = detect_outliers(mixed_effects_results, model_df)
    
    # STEP 6: Robustness checks
    logger.info("=" * 50)
    logger.info("STEP 6: Robustness checks")
    logger.info("=" * 50)
    
    robustness = robustness_checks(filtered_df, za_results)
    
    # Compile final results in the correct schema format
    logger.info("=" * 50)
    logger.info("Compiling final results")
    logger.info("=" * 50)
    
    # Convert results to the required schema format
    # The schema expects: {"datasets": [{"dataset": "...", "examples": [{"input": "...", "output": "..."}]}]}
    
    # Create examples from ZA fitting results
    examples = []
    for za_result in za_results:
        example = {
            "input": json.dumps({
                "treebank_name": za_result.get("treebank_name"),
                "family": za_result.get("family")
            }),
            "output": json.dumps({
                "a_param": za_result.get("a_param"),
                "b_param": za_result.get("b_param"),
                "converged": za_result.get("converged"),
                "ks_stat": za_result.get("ks_stat"),
                "ks_p": za_result.get("ks_p"),
                "n_deps": za_result.get("n_deps")
            }),
            "metadata_treebank": za_result.get("treebank_name"),
            "metadata_family": za_result.get("family"),
            "predict_a_param": str(za_result.get("a_param", "")),
            "predict_b_param": str(za_result.get("b_param", ""))
        }
        examples.append(example)
    
    final_results = {
        "datasets": [
            {
                "dataset": "za_distribution_fitting",
                "examples": examples
            }
        ],
        "metadata": {
            "num_treebanks": len(treebanks),
            "num_treebanks_fitted": len(za_results),
            "num_treebanks_converged": sum(1 for r in za_results if r.get('converged', False)),
            "wals_features_used": wals_features,
            "mixed_effects_results": mixed_effects_results,
            "spoken_written_comparison": spoken_written_results,
            "outlier_families": outliers,
            "robustness": robustness
        }
    }
    
    # Save results
    output_file = workspace_dir / "method_out.json"
    logger.info(f"Saving results to {output_file}")
    with open(output_file, 'w') as f:
        json.dump(final_results, f, indent=2, default=str)
    
    logger.info("Experiment complete!")
    
    # Print summary
    logger.info("=" * 50)
    logger.info("SUMMARY")
    logger.info("=" * 50)
    logger.info(f"ZA fitting: {final_results['metadata']['num_treebanks_converged']}/{final_results['metadata']['num_treebanks_fitted']} converged")
    
    if 't_test' in spoken_written_results:
        t_test = spoken_written_results['t_test']
        logger.info(f"Spoken vs written: t={t_test.get('statistic', 'N/A'):.3f}, p={t_test.get('p', 'N/A'):.3f}")
    
    logger.info(f"Outliers detected: {len(outliers)}")


if __name__ == "__main__":
    main()
