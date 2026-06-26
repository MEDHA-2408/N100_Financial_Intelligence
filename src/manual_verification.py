import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

companies = [
    "ABB",
    "TCS",
    "HDFCBANK"
]

for company in companies:

    print("\n" + "=" * 70)
    print(company)
    print("=" * 70)

    query = f"""
    SELECT
        company_id,
        year,
        return_on_equity_pct,
        revenue_cagr_3yr,
        revenue_cagr_5yr,
        revenue_cagr_10yr,
        pat_cagr_5yr,
        eps_cagr_5yr,
        debt_to_equity,
        interest_coverage,
        high_leverage_flag,
        icr_label,
        icr_warning
    FROM financial_ratios
    WHERE company_id='{company}'
    LIMIT 10
    """

    df = pd.read_sql(query, conn)

    print(df)

conn.close()