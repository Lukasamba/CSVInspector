from csvinspector import CSVInspector

inspector = CSVInspector("example.csv")

print("Missing Headers:", inspector.check_missing_headers())
print("Duplicate Rows:", inspector.check_duplicate_rows())
print("Consistent Columns:", inspector.check_column_consistency())

schema = {
    "age": int,
    "email": str,
    "signup_date": "date",
}
print("Schema Validation:", inspector.validate_column_types(schema))
print("Summary:", inspector.summary_report())
