import pandas as pd

# ============================================================
# LOAD DATA
# ============================================================

data = pd.read_csv(
    "data/processed/health_scores_v2.csv"
)

# Latest year only
latest_data = data[
    data["year"] == "Mar 2024"
].copy()

# Remove duplicate companies
latest_data = latest_data.drop_duplicates(
    subset=["company_id"]
)

# Cap unrealistic ROE values
latest_data["return_on_equity_pct"] = (
    latest_data["return_on_equity_pct"]
    .clip(upper=100)
)

print("=" * 60)
print("INVESTMENT SCREENER")
print("=" * 60)

print("\nUnique Companies:", len(latest_data))


# ============================================================
# QUALITY GROWTH SCREENER
# ============================================================

quality_growth = latest_data[
    (latest_data["health_score_v2"] > 80)
    & (latest_data["return_on_equity_pct"] > 15)
]

print("\n")
print("=" * 60)
print("QUALITY GROWTH SCREENER")
print("=" * 60)

print(
    quality_growth[
        [
            "company_id",
            "health_score_v2",
            "return_on_equity_pct"
        ]
    ]
    .sort_values(
        by="health_score_v2",
        ascending=False
    )
)

quality_growth.to_csv(
    "data/processed/quality_growth_screener.csv",
    index=False
)

print("\nQuality Growth Screener saved successfully!")


# ============================================================
# DEBT FREE SCREENER
# ============================================================

debt_free = latest_data[
    latest_data["debt_to_equity"] < 0.5
]

print("\n")
print("=" * 60)
print("DEBT-FREE SCREENER")
print("=" * 60)

print(
    debt_free[
        [
            "company_id",
            "debt_to_equity",
            "health_score_v2"
        ]
    ]
    .sort_values(
        by="health_score_v2",
        ascending=False
    )
    .head(20)
)

debt_free.to_csv(
    "data/processed/debt_free_screener.csv",
    index=False
)

print("\nDebt-Free Screener saved successfully!")


# ============================================================
# HIGH ROE SCREENER
# ============================================================

high_roe = latest_data[
    latest_data["return_on_equity_pct"] > 20
]

print("\n")
print("=" * 60)
print("HIGH ROE SCREENER")
print("=" * 60)

print(
    high_roe[
        [
            "company_id",
            "return_on_equity_pct",
            "health_score_v2"
        ]
    ]
    .sort_values(
        by="return_on_equity_pct",
        ascending=False
    )
    .head(20)
)

high_roe.to_csv(
    "data/processed/high_roe_screener.csv",
    index=False
)

print("\nHigh ROE Screener saved successfully!")

print("\n")
print("=" * 60)
print("ALL SCREENERS COMPLETED SUCCESSFULLY!")
print("=" * 60)