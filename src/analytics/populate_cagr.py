import sqlite3
import pandas as pd

from cagr import calculate_cagr

print("=" * 60)
print("POPULATING CAGR VALUES")
print("=" * 60)

# ----------------------------------
# Load Data
# ----------------------------------

pl = pd.read_excel(
    "data/raw/profitandloss.xlsx",
    header=1
)

pl = pl[
    pl["year"] != "TTM"
].copy()

# Extract numeric year

pl["year_num"] = (
    pl["year"]
    .astype(str)
    .str.extract(r"(\d{4})")
    .astype(int)
)

pl = pl.sort_values(
    ["company_id", "year_num"]
)

# ----------------------------------
# Load SQLite
# ----------------------------------

conn = sqlite3.connect(
    "db/nifty100.db"
)

ratios = pd.read_sql(
    "SELECT * FROM financial_ratios",
    conn
)

# ----------------------------------
# Calculate CAGR
# ----------------------------------

for company in pl["company_id"].unique():

    company_df = pl[
        pl["company_id"] == company
    ].sort_values("year_num")

    if len(company_df) < 6:
        continue

    start = company_df.iloc[-6]
    end = company_df.iloc[-1]

    rev_cagr, _ = calculate_cagr(
        start["sales"],
        end["sales"],
        5
    )

    pat_cagr, _ = calculate_cagr(
        start["net_profit"],
        end["net_profit"],
        5
    )

    eps_cagr, _ = calculate_cagr(
        start["eps"],
        end["eps"],
        5
    )

    ratios.loc[
        ratios["company_id"] == company,
        "revenue_cagr_5yr"
    ] = rev_cagr

    ratios.loc[
        ratios["company_id"] == company,
        "pat_cagr_5yr"
    ] = pat_cagr

    ratios.loc[
        ratios["company_id"] == company,
        "eps_cagr_5yr"
    ] = eps_cagr

# ----------------------------------
# Save back
# ----------------------------------

ratios.to_sql(
    "financial_ratios",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("\nCAGR columns populated successfully!")

print(
    ratios[
        [
            "company_id",
            "revenue_cagr_5yr",
            "pat_cagr_5yr",
            "eps_cagr_5yr"
        ]
    ].head(20)
)