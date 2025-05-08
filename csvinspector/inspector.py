import csv
from collections import Counter
from datetime import datetime

class CSVInspector:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.rows = []
        self.headers = []
        self._load()

    def _load(self):
        with open(self.filepath, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            self.rows = list(reader)
            if self.rows:
                self.headers = self.rows[0]

    def check_missing_headers(self) -> list[str]:
        return [h for h in self.headers if h.strip() == '']

    def check_duplicate_rows(self) -> list[int]:
        seen = Counter(tuple(row) for row in self.rows[1:])
        return [i+1 for i, row in enumerate(self.rows[1:]) if seen[tuple(row)] > 1]

    def check_column_consistency(self) -> bool:
        expected_len = len(self.headers)
        return all(len(row) == expected_len for row in self.rows[1:])

    def validate_column_types(self, schema: dict) -> dict:
        """
        Schema format: {"age": int, "email": str, "signup_date": "date"}
        """
        results = {}
        header_index = {h: i for i, h in enumerate(self.headers)}

        for col, expected_type in schema.items():
            idx = header_index.get(col)
            if idx is None:
                results[col] = "Missing column"
                continue

            col_valid = True
            for i, row in enumerate(self.rows[1:], start=2):
                value = row[idx]
                try:
                    if expected_type == int:
                        int(value)
                    elif expected_type == float:
                        float(value)
                    elif expected_type == "date":
                        datetime.fromisoformat(value)
                    elif expected_type == str:
                        str(value)
                except Exception:
                    col_valid = False
                    results[col] = f"Invalid type at line {i}: {value}"
                    break
            if col_valid:
                results[col] = "OK"

        return results

    def summary_report(self) -> dict:
        return {
            "missing_headers": self.check_missing_headers(),
            "duplicate_rows": len(self.check_duplicate_rows()),
            "consistent_columns": self.check_column_consistency(),
        }

    def to_markdown_report(self) -> str:
        summary = self.summary_report()
        md = [
            "# CSVInspector Report",
            "",
            f"- **Missing headers**: {summary['missing_headers'] or 'None'}",
            f"- **Duplicate rows**: {summary['duplicate_rows']}",
            f"- **Consistent columns**: {summary['consistent_columns']}",
            "",
            "### Notes",
            "- Use the Python API to validate column types with a schema."
        ]
        return "\n".join(md)
