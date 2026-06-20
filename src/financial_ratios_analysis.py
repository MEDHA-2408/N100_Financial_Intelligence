import pandas as pd

financial_ratios = pd.read_excel(
    "data/raw/financial_ratios.xlsx"
)

print(financial_ratios.head(10))
print("\nColumns:")
print(financial_ratios.columns)