#!/usr/bin/env python3
"""Load UD treebank dependency distance dataset and output in standardized format."""

from pathlib import Path
import json
import glob
import sys

def transform_dependency_to_example(dep):
    """Transform a dependency record to the required example format."""
    # Input: JSON string of features (excluding dd_value which is the output)
    input_features = {
        "treebank_name": dep.get("treebank_name", ""),
        "language": dep.get("language", ""),
        "family": dep.get("family", ""),
        "genre": dep.get("genre", ""),
        "sentence_length": dep.get("sentence_length", 0),
        "deprel": dep.get("deprel", ""),
        "head_position": dep.get("head_position", 0),
        "dependent_position": dep.get("dependent_position", 0),
        "wals_1A": dep.get("wals_1A", "NA"),
        "wals_20A": dep.get("wals_20A", "NA"),
        "wals_26A": dep.get("wals_26A", "NA"),
        "wals_49A": dep.get("wals_49A", "NA"),
        "wals_51A": dep.get("wals_51A", "NA")
    }
    
    # Output: dependency distance as string
    output = str(dep.get("dd_value", 0))
    
    # Metadata fields
    metadata = {
        "metadata_sentence_id": dep.get("sentence_id", ""),
        "metadata_split": dep.get("split", ""),
        "metadata_task_type": "regression",
        "metadata_target_name": "dependency_distance"
    }
    
    return {
        "input": json.dumps(input_features),
        "output": output,
        **metadata
    }

def load_and_transform_dataset():
    """Load all dependencies from data_out_parts and transform to required format."""
    examples = []
    for f in sorted(glob.glob('data_out_parts/data_out_*.json')):
        deps = json.loads(Path(f).read_text())
        for dep in deps:
            examples.append(transform_dependency_to_example(dep))
    return examples

def main():
    """Main function to load, transform, and output dataset."""
    examples = load_and_transform_dataset()
    print(f"Transformed {len(examples)} dependencies to examples")
    
    # Output in the format expected by the pipeline
    output = {
        "datasets": [
            {
                "dataset": "ud_dependency_distances",
                "examples": examples
            }
        ]
    }
    
    # Save full dataset (split into parts to stay under 300MB)
    chunk_size = 150000
    chunks = [examples[i:i+chunk_size] for i in range(0, len(examples), chunk_size)]
    
    import os
    os.makedirs("full_data_out_parts", exist_ok=True)
    
    for i, chunk in enumerate(chunks, 1):
        chunk_output = {"datasets": [{"dataset": "ud_dependency_distances", "examples": chunk}]}
        chunk_path = Path(f"full_data_out_parts/full_data_out_{i}.json")
        chunk_path.write_text(json.dumps(chunk_output, indent=2))
        print(f"Saved chunk {i}: {len(chunk)} examples")
    
    # Generate mini and preview (with proper datasets wrapper)
    mini_output = {"datasets": [{"dataset": "ud_dependency_distances", "examples": examples[:3]}]}
    preview_output = {"datasets": [{"dataset": "ud_dependency_distances", "examples": examples[:3]}]}
    
    Path("data_out_mini.json").write_text(json.dumps(mini_output, indent=2))
    Path("data_out_preview.json").write_text(json.dumps(preview_output, indent=2))
    print("Generated mini and preview files")

if __name__ == "__main__":
    main()
