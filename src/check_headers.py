import pandas as pd

files = [
    "sectors.xlsx",
    "market_cap.xlsx",
    "financial_ratios.xlsx",
    "peer_groups.xlsx",
    "stock_prices.xlsx"
]

for file in files:

    print("\n" + "="*60)
    print(file)

    df = pd.read_excel(
        f"data/raw/{file}",
        header=None
    )

    print(df.head())