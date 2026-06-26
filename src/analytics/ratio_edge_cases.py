import pandas as pd
import os

companies = pd.read_excel(
    "data/raw/companies.xlsx",
    header=1
)

ratios = pd.read_excel(
    "data/raw/financial_ratios.xlsx"
)

os.makedirs("output", exist_ok=True)

log_file = "output/ratio_edge_cases.log"

with open(log_file, "w") as log:

    log.write("N100 Financial Ratio Edge Case Log\n")
    log.write("=" * 60 + "\n\n")

    # Negative ROE
    negative_roe = ratios[
        ratios["return_on_equity_pct"] < 0
    ]

    log.write(
        f"Negative ROE Companies: {len(negative_roe)}\n"
    )

    for _, row in negative_roe.iterrows():

        log.write(
            f"{row['company_id']} "
            f"{row['year']} "
            f"ROE={row['return_on_equity_pct']}\n"
        )

    log.write("\n")

    # Debt Free

    debt_free = ratios[
        ratios["debt_to_equity"] == 0
    ]

    log.write(
        f"Debt Free Records: {len(debt_free)}\n"
    )

    for _, row in debt_free.iterrows():

        log.write(
            f"{row['company_id']} "
            f"{row['year']}\n"
        )

    log.write("\n")

    # Missing Interest Coverage

    missing_icr = ratios[
        ratios["interest_coverage"].isnull()
    ]

    log.write(
        f"Missing Interest Coverage: {len(missing_icr)}\n"
    )

    log.write("\n")

    # ROE Comparison

    company_lookup = companies.set_index(
        "company_name"
    )

    matched = 0

    for _, row in ratios.iterrows():

        company = row["company_id"]

        if company in company_lookup.index:

            source_roe = company_lookup.loc[
                company,
                "roe_percentage"
            ]

            calc_roe = row["return_on_equity_pct"]

            if abs(source_roe - calc_roe) > 5:

                log.write(
                    f"ROE Difference -> "
                    f"{company}: "
                    f"Source={source_roe}, "
                    f"Calculated={calc_roe}\n"
                )

                matched += 1

    log.write("\n")

    log.write(
        f"ROE Anomalies: {matched}\n"
    )

print("ratio_edge_cases.log generated successfully!")