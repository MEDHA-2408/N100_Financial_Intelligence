import pandas as pd

# Load datasets
companies = pd.read_excel("data/raw/companies.xlsx", header=1)
profit_loss = pd.read_excel("data/raw/profitandloss.xlsx", header=1)
cashflow = pd.read_excel("data/raw/cashflow.xlsx", header=1)
analysis = pd.read_excel("data/raw/analysis.xlsx", header=1)
documents = pd.read_excel("data/raw/documents.xlsx", header=1)

sectors = pd.read_excel("data/raw/sectors.xlsx")
market_cap = pd.read_excel("data/raw/market_cap.xlsx")
financial_ratios = pd.read_excel("data/raw/financial_ratios.xlsx")
peer_groups = pd.read_excel("data/raw/peer_groups.xlsx")
stock_prices = pd.read_excel("data/raw/stock_prices.xlsx")

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

for name, df in datasets.items():
    print("\n" + "=" * 50)
    print(name)
    print("=" * 50)

    print("Shape:", df.shape)
    print("Missing Values:", df.isnull().sum().sum())
    print("Duplicate Rows:", df.duplicated().sum())