# Project Guidelines for Claude

## Project Overview
This is a command line utility for evaluating datasets to determine if they're worth ingesting.

### System Architecture
The broader system consists of three main components:

1. **Crawler** (separate component, details TBD)
   - Points at websites with geospatial data
   - Walks links or parses specialized open data portals
   - Discovers potential datasets
   - Passes dataset references/files to GeoGauge

2. **GeoGauge** (this project)
   - Receives arbitrary geospatial datasets from crawler
   - Normalizes data into consistent format
   - Evaluates quality across multiple metrics (see docs/dataset-quality.md)
   - Produces detailed quality scores

3. **Decision Engine** (details TBD)
   - Receives quality metrics from GeoGauge
   - Makes thumbs up/down ingestion decision
   - Could be threshold-based or LLM-based
   - Determines if data should be integrated into target mapping platform

## Technology Stack
- **Language**: Python
- **CLI Framework**: Cyclopts
- **ML Framework**: DSPy (for dataset evaluation)
- **Programming Paradigm**: Functional programming (avoid OOP unless absolutely necessary)
- **Async**: Use asynchronous APIs where possible

## Development Environment
- **Package Manager**: UV (exclusively)
  - Use `uv add` for adding dependencies
  - Use `uv sync` for syncing dependencies
  - Use `uv add --dev` for development dependencies
  - Never use pip commands

## Code Style
- Prefer functional programming patterns
- Avoid classes and object-oriented programming unless there's a compelling reason
- Use async/await patterns where appropriate

## Quality Assurance
After making changes, ALWAYS run:
1. **Formatting**: Ruff
2. **Linting**: Ruff
3. **Type checking**: Pyright
4. **Tests**: PyTest

## Commands to Run
- Formatting: `uv run ruff format`
- Linting: `uv run ruff check`
- Type checking: `uv run pyright`
- Tests: `uv run pytest`