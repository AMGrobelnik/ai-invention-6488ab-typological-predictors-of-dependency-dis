# WALS-UD Language Feature Mapping Dataset

## Summary
This dataset provides a curated mapping between 116 Universal Dependencies (UD) treebanks and WALS (World Atlas of Language Structures) typological features for mixed-effects modeling of dependency distance distributions.

## Files
- `wals_ud_mapping.json` - Full dataset (116 treebanks)
- `wals_ud_mapping_mini.json` - Mini dataset (50 treebanks) for testing
- `wals_ud_mapping_preview.json` - Preview dataset (5 treebanks)

## Dataset Structure
Each mapping entry contains:
- `ud_treebank`: UD treebank name (e.g., 'en_ewt')
- `ud_language_code`: ISO 639-1 language code (e.g., 'en')
- `iso_639_3`: ISO 639-3 language code (e.g., 'eng')
- `wals_language_id`: WALS language identifier
- `wals_language_name`: WALS language name
- `wals_features`: Dictionary of 5 WALS features (1A, 20A, 26A, 49A, 51A)
- `confidence`: Mapping confidence ('high', 'medium', 'low')
- `match_method`: Method used for matching
- `genre`: UD treebank genre

## WALS Features Included
1. **1A** - Order of Subject, Object and Verb (word order)
2. **20A** - Fusion of Inflectional Morphology
3. **26A** - Exponence of Selected Inflectional Categories
4. **49A** - Number of Cases (case marking)
5. **51A** - Locus of Marking in the Clause (alignment)

## Coverage Statistics
- Total mappings: 116 UD treebanks
- High confidence: 98 (84.5%)
- Medium confidence: 0 (0.0%)
- Low confidence: 18 (15.5%)

## Data Sources
- WALS data: CLDF dataset from https://github.com/cldf-datasets/wals (v2020.4)
- UD treebanks: Universal Dependencies 2.15 release
- ISO code mappings: pycountry and langcodes Python packages

## Methodology
Mappings were created by:
1. Converting UD language codes (ISO 639-1) to ISO 639-3
2. Matching ISO 639-3 codes between UD and WALS
3. Extracting WALS feature values for matched languages
4. Assigning confidence levels based on match quality

## Usage
This dataset is designed for mixed-effects modeling of dependency distance distributions across UD treebanks with WALS typological predictors.

## Created
2026-07-19
