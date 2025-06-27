# GeoGauge Pipeline Interface

## Input Format
GeoGauge accepts line-delimited JSON (JSONL) from the crawler component.

### Input Schema
```json
{
  "id": "unique-dataset-id",
  "title": "Dataset Title",
  "description": "Optional description",
  "source_url": "https://example.com/dataset",
  "discovered_at": "2024-01-15T10:30:00Z",
  "metadata": {
    "format": "csv|geojson|shapefile|unknown",
    "size_bytes": 1234567,
    "record_count": 1000
  },
  "data": "inline text data or URL to fetch"
}
```

### Example Input Stream
```jsonl
{"id": "ds-001", "title": "NYC Buildings", "source_url": "https://data.ny.gov/buildings.csv", "data": "https://data.ny.gov/buildings.csv"}
{"id": "ds-002", "title": "Parks POIs", "data": "name,lat,lon\nCentral Park,40.785091,-73.968285\n..."}
```

## Output Format
GeoGauge outputs line-delimited JSON with evaluation results.

### Output Schema
```json
{
  "id": "unique-dataset-id",
  "timestamp": "2024-01-15T10:35:00Z",
  "scores": {
    "schema_compatibility": 85.5,
    "data_quality": 72.0,
    "coverage": 90.0,
    "freshness": 65.0,
    "completeness": 88.5
  },
  "theme": "buildings|places|addresses|transportation|divisions|base",
  "record_count": 1000,
  "quality_issues": [
    {
      "severity": "warning|error",
      "type": "missing_field|invalid_geometry|duplicate_records",
      "description": "Missing height data for 30% of buildings",
      "affected_count": 300
    }
  ],
  "qualitative_assessment": {
    "field_mapping_confidence": "high|medium|low",
    "data_consistency": "Addresses follow consistent formatting",
    "notable_features": "Includes rare building height metadata"
  },
  "integration_difficulty": "low|medium|high",
  "recommendation": {
    "ingest": true,
    "confidence": 0.85,
    "notes": "High quality building data with good coverage"
  }
}
```

### Example Output Stream
```jsonl
{"id": "ds-001", "timestamp": "2024-01-15T10:35:00Z", "scores": {"schema_compatibility": 85.5, "data_quality": 72.0}, "theme": "buildings", "recommendation": {"ingest": true, "confidence": 0.85}}
{"id": "ds-002", "timestamp": "2024-01-15T10:35:05Z", "scores": {"schema_compatibility": 45.0, "data_quality": 30.0}, "theme": "places", "recommendation": {"ingest": false, "confidence": 0.90}}
```

## CLI Usage
```bash
# Pipe from crawler to GeoGauge to decision engine
crawler --source "https://data.gov" | geogauge evaluate | decision-engine

# Or with files
crawler --source "portal.json" > datasets.jsonl
geogauge evaluate < datasets.jsonl > evaluations.jsonl

# Single dataset evaluation
echo '{"id": "test", "data": "https://example.com/data.csv"}' | geogauge evaluate
```

## Processing Options
- `--parallel N`: Process N datasets concurrently
- `--timeout SECONDS`: Maximum time per dataset evaluation
- `--sample-size N`: Limit records analyzed per dataset
- `--verbose`: Include detailed field-level analysis in output