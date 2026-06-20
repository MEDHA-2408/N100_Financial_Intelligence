import pandas as pd

# Load data
profit_growth = pd.read_csv(
    "data/processed/profit_growth_kpi.csv"
)

health_scores = pd.read_csv(
    "data/processed/health_scores_v2.csv"
)

# Latest year only
latest_profit = profit_growth[
    profit_growth["year"] == "Mar 2024"
].copy()

latest_health = health_scores[
    health_scores["year"] == "Mar 2024"
].copy()

# Remove duplicates
latest_profit = latest_profit.drop_duplicates(
    subset=["company_id"]
)

latest_health = latest_health.drop_duplicates(
    subset=["company_id"]
)

# Merge
merged = pd.merge(
    latest_profit,
    latest_health[
        ["company_id", "health_score_v2"]
    ],
    on="company_id",
    how="inner"
)

# Turnaround criteria
turnaround = merged[
    (merged["profit_growth_pct"] > 20)
    & (merged["health_score_v2"] > 60)
]

print("=" * 60)
print("TURNAROUND SCREENER")
print("=" * 60)

print(
    turnaround[
        [
            "company_id",
            "profit_growth_pct",
            "health_score_v2"
        ]
    ]
    .sort_values(
        by="profit_growth_pct",
        ascending=False
    )
)

turnaround.to_csv(
    "data/processed/turnaround_screener.csv",
    index=False
)

print("\nTurnaround Screener saved successfully!")