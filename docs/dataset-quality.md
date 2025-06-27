# Dataset Quality Metrics for GeoGauge

## Overview
GeoGauge evaluates geospatial datasets for quality and compatibility with industry-standard mapping schemas. This document outlines the quality metrics and evaluation criteria for each data theme.

## Standard Geospatial Data Themes

### 1. Places (Points of Interest)
**Key Attributes:**
- Name completeness and accuracy
- Category classification alignment with standard taxonomies
- Operating hours and contact information
- Confidence scores for data reliability

**Quality Metrics:**
- Name presence and formatting consistency
- Category standardization
- Attribute completeness score
- Duplicate detection within dataset
- Spatial accuracy (coordinates match expected location)

### 2. Buildings
**Key Attributes:**
- Building footprint geometry
- Height information
- Building type/use classification
- Unique identifiers

**Quality Metrics:**
- Geometry validity (closed polygons, no self-intersections)
- Height data availability and reasonableness
- Footprint area reasonableness
- Overlap detection with existing buildings
- Classification accuracy

### 3. Addresses
**Key Attributes:**
- Street number and name
- City, state/province, postal code
- Country
- Geocoded coordinates

**Quality Metrics:**
- Address format standardization
- Geocoding accuracy (address components match coordinates)
- Component completeness (all required fields present)
- Country-specific format compliance
- Coordinate precision and validity

### 4. Transportation
**Key Attributes:**
- Road geometry (LineStrings)
- Road class/type
- Directionality
- Access restrictions
- Speed limits

**Quality Metrics:**
- Network connectivity (properly connected segments)
- Geometry simplification appropriateness
- Classification consistency
- Name standardization
- Topology validation (no gaps, overlaps)

### 5. Divisions (Administrative Boundaries)
**Key Attributes:**
- Boundary geometry (Polygons/MultiPolygons)
- Administrative level
- Official names
- Parent-child relationships

**Quality Metrics:**
- Hierarchy validity (proper nesting)
- Boundary precision and simplification
- Name accuracy (matches official sources)
- Complete coverage (no gaps between divisions)
- Relationship consistency

### 6. Base
**Key Attributes:**
- Land use classification
- Natural features (water, parks)
- Infrastructure elements
- Geometry

**Quality Metrics:**
- Classification accuracy
- Geometry complexity appropriateness
- Coverage completeness
- Attribute consistency
- Source reliability

## Universal Quality Indicators

### Data Source Quality
- **Provenance**: Is the source known and reputable?
- **License**: Is the data available under compatible open license?
- **Update frequency**: How often is the source updated?
- **Collection methodology**: How was the data collected?

### Temporal Quality
- **Currency**: How recent is the data?
- **Temporal consistency**: Are timestamps consistent across records?
- **Update tracking**: Is change history available?

### Spatial Quality
- **Coverage**: Geographic completeness for the intended area
- **Spatial accuracy**: Coordinate precision and accuracy
- **Projection**: Proper coordinate reference system usage

### Schema Compatibility
- **Field mapping**: How well do fields map to standard schemas?
- **Data type compatibility**: Are data types consistent?
- **Required fields**: Presence of mandatory fields for mapping platforms
- **Extensibility**: Can additional fields be preserved?

### Data Integrity
- **Uniqueness**: Duplicate detection and handling
- **Consistency**: Internal consistency of related fields
- **Completeness**: Percentage of non-null required fields
- **Validity**: Data meets expected formats and ranges

## Scoring Framework

Each dataset should receive scores in the following categories:
1. **Schema Compatibility Score** (0-100): How well it aligns with target platform
2. **Data Quality Score** (0-100): Overall data quality metrics
3. **Coverage Score** (0-100): Geographic and attribute completeness
4. **Freshness Score** (0-100): How current the data is
5. **Integration Difficulty** (Low/Medium/High): Effort required to integrate

## Implementation Notes
- Use DSPy for intelligent field mapping and classification
- Implement theme-specific validators for each data category
- Create standardized ingestion pipelines for common formats
- Generate detailed quality reports with specific improvement recommendations