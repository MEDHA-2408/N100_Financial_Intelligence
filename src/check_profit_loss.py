import pandas as pd

df = pd.read_excel(
    "data/raw/profitandloss.xlsx",
    header=1
)

print(df.head(15))

print("\nColumns:")
print(df.columns.tolist())

print("\nSample Companies:")
print(df["company_id"].unique()[:5])