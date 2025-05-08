# CSVInspector

**CSVInspector** is a reusable Python component designed to validate and analyze CSV files before processing. It helps identify common data issues such as missing headers, inconsistent rows, duplicate records, and invalid column types.

---

## ✅ Features

- Check for **missing headers**
- Detect **duplicate rows**
- Validate **column consistency**
- Support for **schema-based type checking** (via Python API)
- Generate **Markdown reports**
- Command-line interface (CLI): `csvinspector validate yourfile.csv`

---

## 🚀 Installation

Install directly from GitHub:

```bash
pip install git+https://github.com/Lukasamba/csvinspector.git
```

---

## 🧩 Usage Examples

### 🐍 Python API

```python
from csvinspector import CSVInspector

inspector = CSVInspector("example.csv")
print(inspector.summary_report())
print(inspector.to_markdown_report())
```

### 🖥️ CLI Usage

```bash
csvinspector validate example.csv
```

This will print and save:

```markdown
# CSVInspector Report

- **Missing headers**: None
- **Duplicate rows**: 2
- **Consistent columns**: True

### Notes
- Use the Python API to validate column types with a schema.
```

---

## 📁 Project Structure

```
csvinspector/
├── csvinspector/
│   ├── __init__.py
│   ├── inspector.py
│   └── cli.py
├── examples/
│   ├── example.csv
│   └── basic_usage.py
├── tests/
│   └── test_inspector.py
├── pyproject.toml
├── README.md
```

---

## 🔧 Requirements

- Python 3.7 or later  
- No external dependencies

---

## 📄 License

MIT License

---

## 📝 Change Log

- **v1.0.2** – Added Markdown report generation
- **v1.0.1** – Introduced CLI tool (`csvinspector validate`)
- **v1.0.0** – Initial release with validation API

---

## 🔬 Author

**Lukas Velička**  
T120M156 – Component-Based Software Engineering
