import pandas as pd

# Load Profit & Loss dataset
profit_loss = pd.read_excel(
    "data/raw/profitandloss.xlsx",
    header=1
)

# Sort by company and year
profit_loss = profit_loss.sort_values(
    by=["company_id", "year"]
)

# Calculate Profit Growth %
profit_loss["profit_growth_pct"] = (
    profit_loss.groupby("company_id")["net_profit"]
    .pct_change() * 100
)

# Replace infinity values with NA
profit_loss["profit_growth_pct"] = (
    profit_loss["profit_growth_pct"]
    .replace([float("inf"), float("-inf")], pd.NA)
)

# Get previous year's profit
previous_profit = (
    profit_loss.groupby("company_id")["net_profit"]
    .shift(1)
)

# Remove growth values where previous profit was 0 or negative
profit_loss.loc[
    previous_profit <= 0,
    "profit_growth_pct"
] = pd.NA

print("=" * 60)
print("PROFIT GROWTH KPI")
print("=" * 60)

print(
    profit_loss[
        [
            "company_id",
            "year",
            "net_profit",
            "profit_growth_pct"
        ]
    ].head(20)
)

# Save output
profit_loss.to_csv(
    "data/processed/profit_growth_kpi.csv",
    index=False
)

print("\nProfit Growth KPI file saved successfully!")