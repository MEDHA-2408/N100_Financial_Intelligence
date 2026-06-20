import pandas as pd

# Load datasets
health_scores = pd.read_csv(
    "data/processed/health_scores_v2.csv"
)

sectors = pd.read_excel(
    "data/raw/sectors.xlsx"
)

# Merge datasets
merged = pd.merge(
    health_scores,
    sectors,
    on="company_id",
    how="left"
)

# Latest year only
latest_data = merged[
    merged["year"] == "Mar 2024"
].copy()

# Sector Average
sector_avg = (
    latest_data.groupby("broad_sector")["health_score_v2"]
    .mean()
    .reset_index()
)

sector_avg.columns = [
    "broad_sector",
    "sector_avg_score"
]

# Merge sector average back
latest_data = pd.merge(
    latest_data,
    sector_avg,
    on="broad_sector",
    how="left"
)

# Difference from sector average
latest_data["difference_from_sector"] = (
    latest_data["health_score_v2"]
    - latest_data["sector_avg_score"]
)

print("=" * 60)
print("PEER COMPARISON")
print("=" * 60)

print(
    latest_data[
        [
            "company_id",
            "broad_sector",
            "health_score_v2",
            "sector_avg_score",
            "difference_from_sector"
        ]
    ].head(20)
)

# Save
latest_data.to_csv(
    "data/processed/peer_comparison.csv",
    index=False
)

print("\nPeer Comparison file saved successfully!")
print("\n")
print("=" * 60)
print("TOP 10 COMPANIES")
print("=" * 60)

top_companies = (
    latest_data[
        [
            "company_id",
            "broad_sector",
            "health_score_v2"
        ]
    ]
    .sort_values(
        by="health_score_v2",
        ascending=False
    )
)

print(top_companies.head(10))