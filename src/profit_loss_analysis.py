import pandas as pd

# Load Profit & Loss dataset
profit_loss = pd.read_excel(
    "data/raw/profitandloss.xlsx",
    header=1
)

print("=" * 60)
print("PROFIT & LOSS DATASET ANALYSIS")
print("=" * 60)

# Shape
print("\nShape:")
print(profit_loss.shape)

# Columns
print("\nColumns:")
print(profit_loss.columns)

# First 5 rows
print("\nFirst 5 Rows:")
print(profit_loss.head())

# Dataset Info
print("\nDataset Info:")
print(profit_loss.info())

# Missing Values
print("\nMissing Values:")
print(profit_loss.isnull().sum())

# Duplicate Rows
print("\nDuplicate Rows:")
print(profit_loss.duplicated().sum())

# Basic Statistics
print("\nNumeric Summary:")
print(profit_loss.describe())