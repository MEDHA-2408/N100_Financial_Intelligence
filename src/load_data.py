import pandas as pd

print("=" * 60)
print("N100 FINANCIAL INTELLIGENCE PLATFORM")
print("DATA LOADING & INSPECTION")
print("=" * 60)

# Load datasets
companies = pd.read_excel("data/raw/companies.xlsx", header=1)
profit_loss = pd.read_excel("data/raw/profitandloss.xlsx", header=1)
cashflow = pd.read_excel("data/raw/cashflow.xlsx", header=1)
analysis = pd.read_excel("data/raw/analysis.xlsx", header=1)
documents = pd.read_excel("data/raw/documents.xlsx", header=1)

# Supplementary datasets
sectors = pd.read_excel("data/raw/sectors.xlsx")
market_cap = pd.read_excel("data/raw/market_cap.xlsx")
financial_ratios = pd.read_excel("data/raw/financial_ratios.xlsx")
peer_groups = pd.read_excel("data/raw/peer_groups.xlsx")
stock_prices = pd.read_excel("data/raw/stock_prices.xlsx")

print("\nDATASETS LOADED SUCCESSFULLY!\n")

# Dataset summary
datasets = {
    "Companies": companies,
    "Profit & Loss": profit_loss,
    "Cash Flow": cashflow,
    "Analysis": analysis,
    "Documents": documents,
    "Sectors": sectors,
    "Market Cap": market_cap,
    "Financial Ratios": financial_ratios,
    "Peer Groups": peer_groups,
    "Stock Prices": stock_prices
}

print("=" * 60)
print("DATASET SUMMARY")
print("=" * 60)

for name, df in datasets.items():
    print(f"{name}: {df.shape[0]} rows × {df.shape[1]} columns")

print("\n" + "=" * 60)
print("COMPANIES DATASET DETAILS")
print("=" * 60)

print("\nColumns:")
print(companies.columns)

print("\nMissing Values:")
print(companies.isnull().sum())

print("\nDuplicate Company IDs:")
print(companies["id"].duplicated().sum())

print("\nFirst 5 Rows:")
print(companies.head())