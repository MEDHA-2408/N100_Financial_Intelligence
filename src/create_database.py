import pandas as pd
import sqlite3

# Load source data
df = pd.read_excel(
    "data/raw/financial_ratios.xlsx"
)

# Create database
conn = sqlite3.connect(
    "db/nifty100.db"
)

# Store table
df.to_sql(
    "financial_ratios",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("nifty100.db created successfully!")