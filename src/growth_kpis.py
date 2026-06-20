import pandas as pd

# Load data
profit_loss = pd.read_excel(
    "data/raw/profitandloss.xlsx",
    header=1
)

# Sort data
profit_loss = profit_loss.sort_values(
    by=["company_id", "year"]
)

# Revenue Growth %
profit_loss["revenue_growth_pct"] = (
    profit_loss.groupby("company_id")["sales"]
    .pct_change() * 100
)

# Replace infinity values
profit_loss["revenue_growth_pct"] = (
    profit_loss["revenue_growth_pct"]
    .replace([float("inf"), float("-inf")], pd.NA)
)

print(
    profit_loss[
        [
            "company_id",
            "year",
            "sales",
            "revenue_growth_pct"
        ]
    ].head(20)
)