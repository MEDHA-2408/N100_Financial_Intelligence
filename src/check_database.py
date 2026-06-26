import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

tables = pd.read_sql(
    "SELECT name FROM sqlite_master WHERE type='table';",
    conn
)

print("Tables:")
print(tables)

print("\nfinancial_ratios columns:\n")

cols = pd.read_sql(
    "PRAGMA table_info(financial_ratios);",
    conn
)

print(cols)

print("\nRow Count:")

count = pd.read_sql(
    "SELECT COUNT(*) AS total FROM financial_ratios;",
    conn
)

print(count)

conn.close()