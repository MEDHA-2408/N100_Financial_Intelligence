import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

print("=" * 60)
print("SECTORS TABLE")
print("=" * 60)

print(pd.read_sql(
    "PRAGMA table_info(sectors);",
    conn
))

print("\nSample Data:\n")

print(pd.read_sql(
    "SELECT * FROM sectors LIMIT 5;",
    conn
))

conn.close()