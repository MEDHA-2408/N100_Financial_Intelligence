import pandas as pd
import numpy as np

# Load Profit & Loss data
profit_loss = pd.read_excel(
    "data/raw/profitandloss.xlsx",
    header=1
)

# NPM
profit_loss["net_profit_margin"] = (
    profit_loss["net_profit"] /
    profit_loss["sales"]
) * 100

# OPM
profit_loss["operating_profit_margin"] = (
    profit_loss["operating_profit"] /
    profit_loss["sales"]
) * 100

# Revenue Growth
profit_loss["revenue_growth_pct"] = (
    profit_loss.groupby("company_id")["sales"]
    .pct_change() * 100
)

# Profit Growth
profit_loss["profit_growth_pct"] = (
    profit_loss.groupby("company_id")["net_profit"]
    .pct_change() * 100
)

# Replace bad values
for col in ["revenue_growth_pct", "profit_growth_pct"]:
    profit_loss[col] = (
        profit_loss[col]
        .replace([np.inf, -np.inf], np.nan)
    )

# Simple Health Score
profit_loss["health_score"] = (
      profit_loss["net_profit_margin"].fillna(0) * 0.30
    + profit_loss["operating_profit_margin"].fillna(0) * 0.30
    + profit_loss["revenue_growth_pct"].fillna(0) * 0.20
    + profit_loss["profit_growth_pct"].fillna(0) * 0.20
)

# Cap score at 100
profit_loss["health_score"] = (
    profit_loss["health_score"]
    .clip(0, 100)
)

# Health Band
profit_loss["health_band"] = pd.cut(
    profit_loss["health_score"],
    bins=[0, 35, 50, 65, 80, 100],
    labels=[
        "Poor",
        "Weak",
        "Average",
        "Good",
        "Excellent"
    ],
    include_lowest=True
)

print(
    profit_loss[
        [
            "company_id",
            "year",
            "health_score",
            "health_band"
        ]
    ].head(20)
)

profit_loss.to_csv(
    "data/processed/health_scores.csv",
    index=False
)

print("\nHealth Score file saved successfully!")