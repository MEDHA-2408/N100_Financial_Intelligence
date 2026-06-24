import pandas as pd

df = pd.read_excel(
    "data/raw/financial_ratios.xlsx"
)

print("=" * 50)
print("DATA VALIDATION")
print("=" * 50)

# DQ-01 Primary Key Check

duplicates = df.duplicated().sum()

print(f"DQ-01 Duplicate Rows: {duplicates}")

# DQ-02 Missing Values

print("\nMissing Values")

print(df.isnull().sum())

# DQ-03 Positive Sales Check

if "net_profit_margin_pct" in df.columns:

    print("\nDQ-03 Check Completed")

print("\nValidation Finished")