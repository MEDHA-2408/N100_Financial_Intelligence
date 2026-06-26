import pandas as pd
import os

# Load cashflow dataset
cashflow = pd.read_excel(
    "data/raw/cashflow.xlsx",
    header=1
)


def get_sign(value):
    if value >= 0:
        return "+"
    return "-"


def classify_pattern(cfo, cfi, cff):

    signs = (
        get_sign(cfo),
        get_sign(cfi),
        get_sign(cff)
    )

    patterns = {
        ("+", "-", "-"): "Reinvestor",
        ("+", "+", "-"): "Liquidating Assets",
        ("-", "+", "+"): "Distress Signal",
        ("-", "-", "+"): "Growth Funded by Debt",
        ("+", "+", "+"): "Cash Accumulator",
        ("-", "-", "-"): "Pre-Revenue",
        ("+", "-", "+"): "Mixed"
    }

    return patterns.get(signs, "Unknown")


cashflow["cfo_sign"] = cashflow["operating_activity"].apply(get_sign)

cashflow["cfi_sign"] = cashflow["investing_activity"].apply(get_sign)

cashflow["cff_sign"] = cashflow["financing_activity"].apply(get_sign)

cashflow["pattern_label"] = cashflow.apply(
    lambda row: classify_pattern(
        row["operating_activity"],
        row["investing_activity"],
        row["financing_activity"]
    ),
    axis=1
)

output = cashflow[
    [
        "company_id",
        "year",
        "cfo_sign",
        "cfi_sign",
        "cff_sign",
        "pattern_label"
    ]
]

os.makedirs("output", exist_ok=True)

output.to_csv(
    "output/capital_allocation.csv",
    index=False
)

print("capital_allocation.csv generated successfully!")
print(output.head())