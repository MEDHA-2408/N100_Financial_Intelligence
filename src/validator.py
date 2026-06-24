import pandas as pd

df = pd.read_excel(
    "data/raw/financial_ratios.xlsx"
)

print("=" * 60)
print("N100 DATA QUALITY VALIDATION")
print("=" * 60)

# DQ-01 Duplicate Rows

duplicates = df.duplicated().sum()

print(f"\nDQ-01 Duplicate Rows: {duplicates}")

# DQ-02 Missing Values

missing = df.isnull().sum()

print("\nDQ-02 Missing Values")

print(missing)

# DQ-03 Null Company IDs

null_company_ids = df["company_id"].isnull().sum()

print(
    f"\nDQ-03 Null Company IDs: {null_company_ids}"
)

# DQ-04 Duplicate Company-Year

duplicate_company_year = (
    df.duplicated(
        subset=["company_id", "year"]
    ).sum()
)

print(
    f"\nDQ-04 Duplicate Company-Year Records: "
    f"{duplicate_company_year}"
)

# DQ-05 Negative ROE

negative_roe = (
    df["return_on_equity_pct"] < 0
).sum()

print(
    f"\nDQ-05 Negative ROE Records: "
    f"{negative_roe}"
)

# DQ-06 Negative Debt

negative_debt = (
    df["total_debt_cr"] < 0
).sum()

print(
    f"\nDQ-06 Negative Debt Records: "
    f"{negative_debt}"
)

# DQ-07 Missing EPS

missing_eps = (
    df["earnings_per_share"]
    .isnull()
    .sum()
)

print(
    f"\nDQ-07 Missing EPS Records: "
    f"{missing_eps}"
)

# DQ-08 Missing Cash Flow

missing_cashflow = (
    df["cash_from_operations_cr"]
    .isnull()
    .sum()
)

print(
    f"\nDQ-08 Missing Cash Flow Records: "
    f"{missing_cashflow}"
)
# DQ-09 Missing Dividend Payout

missing_dividend = (
    df["dividend_payout_ratio_pct"]
    .isnull()
    .sum()
)

print(
    f"\nDQ-09 Missing Dividend Payout Records: "
    f"{missing_dividend}"
)

# DQ-10 Missing Asset Turnover

missing_asset_turnover = (
    df["asset_turnover"]
    .isnull()
    .sum()
)

print(
    f"\nDQ-10 Missing Asset Turnover Records: "
    f"{missing_asset_turnover}"
)

# DQ-11 Missing Free Cash Flow

missing_fcf = (
    df["free_cash_flow_cr"]
    .isnull()
    .sum()
)

print(
    f"\nDQ-11 Missing Free Cash Flow Records: "
    f"{missing_fcf}"
)

# DQ-12 Missing Capex

missing_capex = (
    df["capex_cr"]
    .isnull()
    .sum()
)

print(
    f"\nDQ-12 Missing Capex Records: "
    f"{missing_capex}"
)

# DQ-13 Negative Book Value

negative_book_value = (
    df["book_value_per_share"] < 0
).sum()

print(
    f"\nDQ-13 Negative Book Value Records: "
    f"{negative_book_value}"
)

# DQ-14 Negative Interest Coverage

negative_interest = (
    df["interest_coverage"] < 0
).sum()

print(
    f"\nDQ-14 Negative Interest Coverage Records: "
    f"{negative_interest}"
)

# DQ-15 Missing Year

missing_year = (
    df["year"]
    .isnull()
    .sum()
)

print(
    f"\nDQ-15 Missing Year Records: "
    f"{missing_year}"
)

# DQ-16 Missing Company ID

missing_company = (
    df["company_id"]
    .isnull()
    .sum()
)

print(
    f"\nDQ-16 Missing Company Records: "
    f"{missing_company}"
)

print("\nValidation Completed Successfully!")
