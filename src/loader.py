import pandas as pd
import sqlite3

print("=" * 60)
print("N100 FINANCIAL INTELLIGENCE PLATFORM")
print("SQLITE DATA LOADER")
print("=" * 60)

# Database connection
conn = sqlite3.connect("db/nifty100.db")

# Load datasets

companies = pd.read_excel(
    "data/raw/companies.xlsx",
    header=1
)

profitandloss = pd.read_excel(
    "data/raw/profitandloss.xlsx",
    header=1
)

cashflow = pd.read_excel(
    "data/raw/cashflow.xlsx",
    header=1
)

analysis = pd.read_excel(
    "data/raw/analysis.xlsx",
    header=1
)

documents = pd.read_excel(
    "data/raw/documents.xlsx",
    header=1
)

sectors = pd.read_excel(
    "data/raw/sectors.xlsx"
)

market_cap = pd.read_excel(
    "data/raw/market_cap.xlsx"
)

financial_ratios = pd.read_excel(
    "data/raw/financial_ratios.xlsx"
)

peer_groups = pd.read_excel(
    "data/raw/peer_groups.xlsx"
)

stock_prices = pd.read_excel(
    "data/raw/stock_prices.xlsx"
)

# Save tables

companies.to_sql(
    "companies",
    conn,
    if_exists="replace",
    index=False
)

profitandloss.to_sql(
    "profitandloss",
    conn,
    if_exists="replace",
    index=False
)

cashflow.to_sql(
    "cashflow",
    conn,
    if_exists="replace",
    index=False
)

analysis.to_sql(
    "analysis",
    conn,
    if_exists="replace",
    index=False
)

documents.to_sql(
    "documents",
    conn,
    if_exists="replace",
    index=False
)

sectors.to_sql(
    "sectors",
    conn,
    if_exists="replace",
    index=False
)

market_cap.to_sql(
    "market_cap",
    conn,
    if_exists="replace",
    index=False
)

financial_ratios.to_sql(
    "financial_ratios",
    conn,
    if_exists="replace",
    index=False
)

peer_groups.to_sql(
    "peer_groups",
    conn,
    if_exists="replace",
    index=False
)

stock_prices.to_sql(
    "stock_prices",
    conn,
    if_exists="replace",
    index=False
)

# Load Audit

audit = pd.DataFrame({
    "table_name": [
        "companies",
        "profitandloss",
        "cashflow",
        "analysis",
        "documents",
        "sectors",
        "market_cap",
        "financial_ratios",
        "peer_groups",
        "stock_prices"
    ],
    "row_count": [
        len(companies),
        len(profitandloss),
        len(cashflow),
        len(analysis),
        len(documents),
        len(sectors),
        len(market_cap),
        len(financial_ratios),
        len(peer_groups),
        len(stock_prices)
    ]
})

audit.to_csv(
    "output/load_audit.csv",
    index=False
)

conn.close()

print("\nAll 10 tables loaded successfully!")
print("load_audit.csv generated.")