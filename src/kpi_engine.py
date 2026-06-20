import pandas as pd

profit_loss = pd.read_excel(
    "data/raw/profitandloss.xlsx",
    header=1
)

# KPI 1: Net Profit Margin
profit_loss["net_profit_margin"] = (
    profit_loss["net_profit"] /
    profit_loss["sales"]
) * 100

# KPI 2: Operating Profit Margin
profit_loss["operating_profit_margin"] = (
    profit_loss["operating_profit"] /
    profit_loss["sales"]
) * 100

print(
    profit_loss[
        [
            "company_id",
            "year",
            "sales",
            "operating_profit",
            "net_profit",
            "operating_profit_margin",
            "net_profit_margin"
        ]
    ].head(10)
)
# Save KPI dataset
profit_loss.to_csv(
    "data/processed/financial_kpis.csv",
    index=False
)

print("\nKPI file saved successfully!")