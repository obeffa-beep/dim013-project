import sys

import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """Load a CSV file into a DataFrame.

    Args:
        path: Relative path to the CSV file.

    Returns:
        The loaded data.
    """
    return pd.read_csv(path, sep=",", encoding="utf-8-sig")


def is_valid_csv(path: str) -> bool:
    """Check that a CSV file loads and contains at least one row.

    Args:
        path: Relative path to the CSV file.

    Returns:
        True if the file loads and has data, False otherwise.
    """
    try:
        return not load_data(path).empty
    except (FileNotFoundError, pd.errors.ParserError, pd.errors.EmptyDataError):
        return False


if __name__ == "__main__":
    print(load_data(sys.argv[1]).head())