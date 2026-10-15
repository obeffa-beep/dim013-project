from pathlib import Path
import pandas as pd

def test_csv_structure():
    project_root = Path(__file__).resolve().parents[1]
    csv_path = project_root / "data" / "sample.csv"

    df = pd.read_csv(csv_path, encoding="utf-8-sig")

    expected_columns = ["product", "price", "quantity"]

    assert list(df.columns) == expected_columns
    assert not df.empty

    cd ~/exam-git-project/partner-project


# --- Part 1: save the change already made to your test file ---
git diff tests/test_csv_structure.py                # show what changed in the test (press q to exit)
python -m pytest tests/test_csv_structure.py        # run the test to check it still passes
git add tests/test_csv_structure.py                 # stage the updated test
git commit -m "test: improve CSV structure test"    # save it in its own commit

# --- Part 2: open the file to add the function ---
code src/load_data.py                               # opens VS Code: add the function, save with Ctrl+S

