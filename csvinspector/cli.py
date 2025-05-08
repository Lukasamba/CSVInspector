import argparse
from .inspector import CSVInspector

def main():
    parser = argparse.ArgumentParser(description="CSVInspector - Validate CSV files.")
    subparsers = parser.add_subparsers(dest="command")

    validate_parser = subparsers.add_parser("validate", help="Validate a CSV file.")
    validate_parser.add_argument("filepath", type=str, help="Path to the CSV file.")

    args = parser.parse_args()

    if args.command == "validate":
        inspector = CSVInspector(args.filepath)

        print("=== CSVInspector Validation Report ===")
        print("Missing Headers:", inspector.check_missing_headers())
        print("Duplicate Rows:", inspector.check_duplicate_rows())
        print("Consistent Columns:", inspector.check_column_consistency())
        print("Schema Validation: Not available in CLI (use Python API)")
        print("Summary:", inspector.summary_report())

if __name__ == "__main__":
    main()
