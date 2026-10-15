from pathlib import Path
import pandas as pd

def test_csv_structure():
    project_root = Path(__file__).resolve().parents[1]
    csv_path = project_root / "data" / "sample.csv"

    df = pd.read_csv(csv_path, encoding="utf-8-sig")

    expected_columns = ["product", "price", "quantity"]

    assert list(df.columns) == expected_columns
    assert not df.empty

    