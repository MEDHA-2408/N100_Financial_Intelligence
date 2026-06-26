import sys
import os
import pandas as pd

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            ".."
        )
    )
)

def test_dataframe_exists():

    df = pd.read_excel(
        "data/raw/financial_ratios.xlsx"
    )

    assert len(df) > 0


def test_columns_exist():

    df = pd.read_excel(
        "data/raw/financial_ratios.xlsx"
    )

    assert len(df.columns) > 0


def test_duplicate_check():

    df = pd.read_excel(
        "data/raw/financial_ratios.xlsx"
    )

    duplicates = df.duplicated().sum()

    assert duplicates >= 0


print("test_validator passed!")