import pandas as pd

# Load datasets
sectors = pd.read_excel(
    "data/raw/sectors.xlsx"
)

health_scores = pd.read_csv(
    "data/processed/health_scores_v2.csv"
)

print("=" * 60)
print("SECTOR ANALYTICS")
print("=" * 60)

# Check columns
print("\nSectors Columns:")
print(sectors.columns)

print("\nHealth Score Columns:")
print(health_scores.columns)

# Merge datasets
merged = pd.merge(
    health_scores,
    sectors,
    on="company_id",
    how="left"
)

print("\nMerged Shape:")
print(merged.shape)

print("\nFirst 5 Rows:")
print(merged.head())
print("\nMerged Shape:")
print(merged.shape)

print("\nColumns After Merge:")
print(merged.columns)

print("\nFirst 5 Rows:")
print(merged.head())
# Average Health Score by Sector

sector_summary = (
    merged.groupby("broad_sector")["health_score_v2"]
    .mean()
    .reset_index()
)

sector_summary.columns = [
    "sector",
    "avg_health_score"
]

# Rank sectors

sector_summary = sector_summary.sort_values(
    by="avg_health_score",
    ascending=False
)

sector_summary["rank"] = range(
    1,
    len(sector_summary) + 1
)

print("\nSECTOR RANKING")
print("=" * 60)

print(sector_summary)

# Save

sector_summary.to_csv(
    "data/processed/sector_analytics.csv",
    index=False
)

print("\nSector Analytics file saved successfully!")