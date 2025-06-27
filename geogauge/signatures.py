import dspy


class ParseRecords(dspy.Signature):
    """Parse raw dataset text into individual records."""
    
    raw_data: str = dspy.InputField(desc="Raw dataset text in CSV, TSV, or other delimited format")
    records: list[str] = dspy.OutputField(desc="List of individual records, each as a complete row including all fields")