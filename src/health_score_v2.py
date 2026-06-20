import pandas as pd
import numpy as np

# Load financial ratios
ratios = pd.read_excel(
    "data/raw/financial_ratios.xlsx"
)

# Create score components

ratios["roe_score"] = ratios["return_on_equity_pct"].clip(0, 30) * (25 / 30)

ratios["npm_score"] = ratios["net_profit_margin_pct"].clip(0, 25) * (20 / 25)

ratios["opm_score"] = ratios["operating_profit_margin_pct"].clip(0, 25) * (20 / 25)

ratios["de_score"] = (
    (2 - ratios["debt_to_equity"].clip(0, 2))
    * (15 / 2)
)

ratios["interest_score"] = (
    ratios["interest_coverage"]
    .clip(0, 10)
    * (20 / 10)
)

# Final Health Score
ratios["health_score_v2"] = (
    ratios["roe_score"].fillna(0)
    + ratios["npm_score"].fillna(0)
    + ratios["opm_score"].fillna(0)
    + ratios["de_score"].fillna(0)
    + ratios["interest_score"].fillna(0)
)

ratios["health_score_v2"] = (
    ratios["health_score_v2"]
    .clip(0, 100)
)

# Health Band
ratios["health_band"] = pd.cut(
    ratios["health_score_v2"],
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
    ratios[
        [
            "company_id",
            "year",
            "health_score_v2",
            "health_band"
        ]
    ].head(20)
)

ratios.to_csv(
    "data/processed/health_scores_v2.csv",
    index=False
)

print("\nHealth Score V2 saved successfully!")