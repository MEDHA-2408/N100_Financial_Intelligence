import pandas as pd

files = [
    "companies.xlsx",
    "profitandloss.xlsx",
    "cashflow.xlsx",
    "analysis.xlsx",
    "documents.xlsx",
    "sectors.xlsx",
    "market_cap.xlsx",
    "financial_ratios.xlsx",
    "peer_groups.xlsx",
    "stock_prices.xlsx"
]

for f in files:

    try:
        df = pd.read_excel(
            f"data/raw/{f}",
            header=1
        )

    except:
        df = pd.read_excel(
            f"data/raw/{f}"
        )

    print("\n" + "=" * 50)
    print(f)
    print(df.columns.tolist())