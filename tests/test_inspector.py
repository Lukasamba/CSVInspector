import os
import tempfile
from s import CSVInspector

def test_summary():
    content = """name,age,email\nJohn,30,john@example.com\nJane,25,jane@example.com\nJohn,30,john@example.com\n"""
    with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.csv') as f:
        f.write(content)
        tempname = f.name

    inspector = CSVInspector(tempname)
    assert inspector.check_missing_headers() == []
    assert inspector.check_column_consistency() == True
    assert len(inspector.check_duplicate_rows()) == 2
    os.remove(tempname)