CSVInspector is a reusable Python component for validating and analyzing CSV files.

## ✅ Features
- Check for missing headers
- Detect duplicate rows
- Ensure column consistency
- Validate column data types (int, float, str, ISO date)
- Generate summary report

## 🚀 Installation
```bash
pip install git+https://github.com/Lukasamba/csvinspector.git
```

## 📦 Usage
```python
from csvinspector import CSVInspector
inspector = CSVInspector("data.csv")
inspector.summary_report()
```

## 🧪 Example
See `examples/basic_usage.py`.

## 🧰 Requirements
- Python 3.7+

## 📄 License
MIT

## 📋 Changelog
- v1.0.0: Initial release

![Python](https://img.shields.io/badge/python-3.7+-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
