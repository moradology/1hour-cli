import json
import os
import sys
from pathlib import Path

import cyclopts
import dspy
from dotenv import load_dotenv

from geogauge.signatures import ParseRecords

# Load environment variables
load_dotenv()

app = cyclopts.App()


def read_jsonl(file_path: Path):
    """Read line-delimited JSON file and yield each record."""
    with open(file_path, 'r') as f:
        for line in f:
            if line.strip():
                yield json.loads(line)


@app.default
def evaluate():
    """Evaluate geospatial datasets for quality and compatibility with major mapping platforms."""
    # For now, use the test file
    test_file = Path(__file__).parent.parent / "tests" / "test-crawler-output.jsonl"
    
    # Initialize DSPy with OpenAI
    api_key = os.getenv("OPENAI_KEY")
    if not api_key:
        print("Error: OPENAI_KEY not found in environment variables")
        sys.exit(1)
    
    lm = dspy.LM(
        model="openai/gpt-4o-mini",
        api_key=api_key,
        temperature=0.1
    )
    dspy.configure(lm=lm)
    
    print("Starting GeoGauge evaluation...")
    print(f"Reading from: {test_file}")
    print("-" * 80)
    
    # Create a DSPy module for parsing records
    parse_records = dspy.Predict(ParseRecords)
    
    for dataset in read_jsonl(test_file):
        print(f"\nProcessing dataset: {dataset['id']} - {dataset['title']}")
        print(f"  Source: {dataset.get('source_url', 'N/A')}")
        print(f"  Format: {dataset.get('metadata', {}).get('format', 'unknown')}")
        
        # Process inline data with DSPy
        if isinstance(dataset.get('data'), str) and not dataset['data'].startswith('http'):
            # Use DSPy to parse the records
            result = parse_records(raw_data=dataset['data'])
            
            print(f"  Parsed {len(result.records)} records:")
            # Show first 3 records
            for i, record in enumerate(result.records[:3]):
                print(f"    [{i+1}] {record[:100]}..." if len(record) > 100 else f"    [{i+1}] {record}")
            if len(result.records) > 3:
                print(f"    ... and {len(result.records) - 3} more records")
        else:
            print(f"  Data URL: {dataset.get('data', 'N/A')}")


if __name__ == "__main__":
    app()