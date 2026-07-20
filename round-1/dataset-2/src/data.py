#!/usr/bin/env python3
"""Data loading script for WALS-UD Language Feature Mapping dataset.

This script loads the WALS-UD mapping dataset and converts it to the
experiment pipeline format (exp_sel_data_out.json schema).
"""

from loguru import logger
from pathlib import Path
import json
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def main():
    """Load WALS-UD mapping dataset and convert to experiment format."""
    logger.info("Loading WALS-UD mapping dataset...")
    
    # Load the mapping dataset
    mapping_path = Path("wals_ud_mapping.json")
    if not mapping_path.exists():
        logger.error(f"Mapping file not found: {mapping_path}")
        return
    
    with open(mapping_path, 'r') as f:
        data = json.load(f)
    
    mappings = data['mappings']
    metadata = data['metadata']
    
    logger.info(f"Loaded {len(mappings)} UD treebank mappings")
    
    # Convert to experiment format
    # Each UD treebank = one example
    examples = []
    
    for tb_name, mapping in mappings.items():
        # Create input text describing the mapping
        input_text = {
            'ud_treebank': mapping['ud_treebank'],
            'ud_language_code': mapping['ud_language_code'],
            'iso_639_3': mapping['iso_639_3'],
            'wals_language_name': mapping.get('wals_language_name', ''),
            'genre': mapping.get('genre', ''),
            'confidence': mapping.get('confidence', 'low')
        }
        
        # Create output with WALS features
        output = {
            'wals_language_id': mapping.get('wals_language_id', ''),
            'wals_features': mapping.get('wals_features', {})
        }
        
        example = {
            'input': json.dumps(input_text, sort_keys=True),
            'output': json.dumps(output, sort_keys=True),
            'metadata_treebank': tb_name,
            'metadata_language_code': mapping['ud_language_code'],
            'metadata_iso_639_3': mapping['iso_639_3'],
            'metadata_confidence': mapping.get('confidence', 'low'),
            'metadata_genre': mapping.get('genre', ''),
            'metadata_num_features': len(mapping.get('wals_features', {}))
        }
        
        examples.append(example)
    
    # Build experiment format
    exp_data = {
        'datasets': [
            {
                'dataset': 'wals_ud_mapping',
                'examples': examples
            }
        ]
    }
    
    # Save full_data_out.json
    output_path = Path("full_data_out.json")
    with open(output_path, 'w') as f:
        json.dump(exp_data, f, indent=2, ensure_ascii=False)
    
    logger.info(f"Saved {len(examples)} examples to {output_path}")
    logger.info(f"Dataset: {metadata['features_included']}")
    logger.info(f"WALS version: {metadata['wals_version']}")
    logger.info(f"UD version: {metadata['ud_version']}")
    
    # Print summary statistics
    high_conf = sum(1 for e in examples if e['metadata_confidence'] == 'high')
    logger.info(f"High confidence: {high_conf}/{len(examples)} ({100*high_conf/len(examples):.1f}%)")

if __name__ == "__main__":
    main()
