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


### setup.py
from setuptools import setup, find_packages

setup(
    name='csvinspector',
    version='1.0.0',
    description='CSV Validation and Analysis Tool',
    author='Your Name',
    packages=find_packages(),
    install_requires=[],
    python_requires='>=3.7',
)
