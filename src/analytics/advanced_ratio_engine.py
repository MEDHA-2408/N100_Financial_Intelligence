import sqlite3
import pandas as pd

from cagr import calculate_cagr

print("=" * 60)
print("ADVANCED FINANCIAL RATIO ENGINE")
print("=" * 60)

# ----------------------------------------------------
# Load Profit & Loss
# ----------------------------------------------------

pl = pd.read_excel(
    "data/raw/profitandloss.xlsx",
    header=1
)

# Remove TTM
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

# ----------------------------------------------------
# Open SQLite
# ----------------------------------------------------

conn = sqlite3.connect(
    "db/nifty100.db"
)

ratios = pd.read_sql(
    "SELECT * FROM financial_ratios",
    conn
)

# ----------------------------------------------------
# Create New Columns
# ----------------------------------------------------

new_columns = [

    "revenue_cagr_3yr",
    "pat_cagr_3yr",
    "eps_cagr_3yr",

    "revenue_cagr_10yr",
    "pat_cagr_10yr",
    "eps_cagr_10yr",

    "revenue_cagr_3yr_flag",
    "pat_cagr_3yr_flag",
    "eps_cagr_3yr_flag",

    "revenue_cagr_5yr_flag",
    "pat_cagr_5yr_flag",
    "eps_cagr_5yr_flag",

    "revenue_cagr_10yr_flag",
    "pat_cagr_10yr_flag",
    "eps_cagr_10yr_flag"
]

for col in new_columns:

    if col not in ratios.columns:

        ratios[col] = None

# ----------------------------------------------------
# Calculate CAGR
# ----------------------------------------------------

for company in pl["company_id"].unique():

    company_df = pl[
        pl["company_id"] == company
    ].sort_values("year_num")

    def compute(window):

        if len(company_df) < window + 1:

            return (
                None,
                None,
                None,
                "INSUFFICIENT",
                "INSUFFICIENT",
                "INSUFFICIENT"
            )

        start = company_df.iloc[-(window + 1)]
        end = company_df.iloc[-1]

        rev, rev_flag = calculate_cagr(
            start["sales"],
            end["sales"],
            window
        )

        pat, pat_flag = calculate_cagr(
            start["net_profit"],
            end["net_profit"],
            window
        )

        eps, eps_flag = calculate_cagr(
            start["eps"],
            end["eps"],
            window
        )

        return (
            rev,
            pat,
            eps,
            rev_flag,
            pat_flag,
            eps_flag
        )

    rev3, pat3, eps3, rf3, pf3, ef3 = compute(3)

    rev5, pat5, eps5, rf5, pf5, ef5 = compute(5)

    rev10, pat10, eps10, rf10, pf10, ef10 = compute(10)

    mask = ratios["company_id"] == company

    ratios.loc[mask, "revenue_cagr_3yr"] = rev3
    ratios.loc[mask, "pat_cagr_3yr"] = pat3
    ratios.loc[mask, "eps_cagr_3yr"] = eps3

    ratios.loc[mask, "revenue_cagr_5yr"] = rev5
    ratios.loc[mask, "pat_cagr_5yr"] = pat5
    ratios.loc[mask, "eps_cagr_5yr"] = eps5

    ratios.loc[mask, "revenue_cagr_10yr"] = rev10
    ratios.loc[mask, "pat_cagr_10yr"] = pat10
    ratios.loc[mask, "eps_cagr_10yr"] = eps10

    ratios.loc[mask, "revenue_cagr_3yr_flag"] = rf3
    ratios.loc[mask, "pat_cagr_3yr_flag"] = pf3
    ratios.loc[mask, "eps_cagr_3yr_flag"] = ef3

    ratios.loc[mask, "revenue_cagr_5yr_flag"] = rf5
    ratios.loc[mask, "pat_cagr_5yr_flag"] = pf5
    ratios.loc[mask, "eps_cagr_5yr_flag"] = ef5

    ratios.loc[mask, "revenue_cagr_10yr_flag"] = rf10
    ratios.loc[mask, "pat_cagr_10yr_flag"] = pf10
    ratios.loc[mask, "eps_cagr_10yr_flag"] = ef10

print("\nModule A Complete")
print(ratios.head())
# ----------------------------------------------------
# MODULE B
# High Leverage
# ICR Labels
# Financial Sector Rule
# ----------------------------------------------------

print("\nStarting Module B...")

# Load sectors table
sectors = pd.read_sql(
    "SELECT * FROM sectors",
    conn
)

# Create new columns if they don't exist
extra_cols = [
    "high_leverage_flag",
    "icr_label",
    "icr_warning"
]

for col in extra_cols:
    if col not in ratios.columns:
        ratios[col] = None

# Financial sector companies
financial_companies = sectors[
    sectors["broad_sector"] == "Financials"
]["company_id"].tolist()

for idx, row in ratios.iterrows():

    company = row["company_id"]

    de = row["debt_to_equity"]

    icr = row["interest_coverage"]

    # ----------------------------
    # High Leverage Flag
    # ----------------------------

    if company not in financial_companies:

        if pd.notna(de) and de > 5:

            ratios.at[idx, "high_leverage_flag"] = True

        else:

            ratios.at[idx, "high_leverage_flag"] = False

    else:

        # Financial companies exempt
        ratios.at[idx, "high_leverage_flag"] = False

    # ----------------------------
    # Interest Coverage Label
    # ----------------------------

    if pd.isna(icr):

        ratios.at[idx, "icr_label"] = "Debt Free"

    else:

        ratios.at[idx, "icr_label"] = "Has Debt"

    # ----------------------------
    # ICR Warning
    # ----------------------------

    if pd.notna(icr) and icr < 1.5:

        ratios.at[idx, "icr_warning"] = "WARNING"

    else:

        ratios.at[idx, "icr_warning"] = "OK"

print("Module B Complete")
# ----------------------------------------------------
# Save Database
# ----------------------------------------------------

ratios.to_sql(
    "financial_ratios",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("\nDatabase Updated Successfully!")

print("\nCurrent Columns:")
print(ratios.columns.tolist())