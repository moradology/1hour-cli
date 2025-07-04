# GeoGauge

A command-line utility for evaluating geospatial datasets using AI-powered quality assessment.

## What It Does

GeoGauge currently reads geospatial datasets and intelligently parses them regardless of format (CSV, TSV, etc.). It's designed to be part of a larger pipeline that evaluates whether datasets are worth ingesting into mapping platforms.

### Current Capabilities

- **Automatic Format Detection**: Uses DSPy/LLMs to parse CSV, TSV, and other delimited formats without explicit configuration
- **Test Data Processing**: Includes sample datasets for hospitals, libraries, rail stations, and bike parking
- **Pipeline Ready**: Accepts line-delimited JSON input and outputs structured evaluation results

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd gis-assessor

# Install dependencies using UV
uv sync
```

## Usage

Currently, GeoGauge runs against test data included in the repository:

```bash
# Run the evaluation on test datasets
uv run python -m geogauge.main
```

This will process 4 test datasets:
- Gary, Indiana hospitals
- Northwest Ohio libraries  
- UK rail stations
- Berlin bike parking facilities

## Project Structure

```
gis-assessor/
   geogauge/           # Main application code
      main.py         # CLI entry point
      signatures.py   # DSPy signatures for data parsing
   docs/               # Documentation
      dataset-quality.md      # Quality metrics guide
      pipeline-interface.md   # Input/output specifications
   tests/              # Test data
      test-crawler-output.jsonl
   claude.md           # Project guidelines
```

## Development

### Running Quality Checks

```bash
# Format code
uv run ruff format

# Lint code  
uv run ruff check

# Type checking
uv run pyright

# Run tests
uv run pytest
```

### Environment Setup

Create a `.env` file with your OpenAI API key:

```
OPENAI_KEY="your-api-key-here"
```

## Architecture

GeoGauge is designed as the middle component in a 3-part pipeline:

1. **Crawler** (external) � discovers datasets
2. **GeoGauge** (this tool) � evaluates quality
3. **Decision Engine** (external) � makes ingestion decisions

## Input/Output Format

**Input**: Line-delimited JSON with dataset metadata and data
```json
{"id": "dataset-001", "title": "Hospital Locations", "data": "csv content here..."}
```

**Output**: Structured evaluation results (coming soon)
```json
{"id": "dataset-001", "scores": {...}, "recommendation": {...}}
```

## Roadmap

- [ ] Implement full quality scoring system
- [ ] Add support for URL-based datasets
- [ ] Create structured JSON output
- [ ] Add more data format parsers
- [ ] Implement the 6 quality themes evaluation

## Contributing

This project uses:
- **UV** for package management (no pip!)
- **Functional programming** style (avoid OOP)
- **DSPy** for AI-powered data processing

See `claude.md` for detailed development guidelines.