import pandas as pd

def test_companies_loaded():

    df = pd.read_excel(
        "data/raw/companies.xlsx",
        header=1
    )

    assert len(df) > 0


def test_profitandloss_loaded():

    df = pd.read_excel(
        "data/raw/profitandloss.xlsx",
        header=1
    )

    assert len(df) > 0


def test_cashflow_loaded():

    df = pd.read_excel(
        "data/raw/cashflow.xlsx",
        header=1
    )

    assert len(df) > 0


print("test_loader passed!")