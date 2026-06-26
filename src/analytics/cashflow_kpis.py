def free_cash_flow(operating_activity, investing_activity):
    """
    Free Cash Flow = CFO + Investing Activity
    """
    return operating_activity + investing_activity


def cfo_quality_score(cfo, pat):
    """
    CFO Quality Score
    """

    if pat == 0:
        return None, "PAT_ZERO"

    ratio = cfo / pat

    if ratio > 1:
        return ratio, "High Quality"

    elif ratio >= 0.5:
        return ratio, "Moderate"

    else:
        return ratio, "Accrual Risk"


def capex_intensity(capex, sales):
    """
    CapEx Intensity
    """

    if sales == 0:
        return None, "ZERO_SALES"

    intensity = abs(capex) / sales * 100

    if intensity < 3:
        label = "Asset Light"

    elif intensity <= 8:
        label = "Moderate"

    else:
        label = "Capital Intensive"

    return intensity, label


def fcf_conversion(fcf, operating_profit):
    """
    FCF Conversion
    """

    if operating_profit == 0:
        return None

    return (fcf / operating_profit) * 100


def capital_allocation_pattern(cfo, cfi, cff):

    signs = (
        "+" if cfo >= 0 else "-",
        "+" if cfi >= 0 else "-",
        "+" if cff >= 0 else "-"
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


if __name__ == "__main__":

    fcf = free_cash_flow(150, -40)

    print("FCF:", fcf)

    print(cfo_quality_score(180, 150))

    print(capex_intensity(-60, 900))

    print(fcf_conversion(fcf, 200))

    print(capital_allocation_pattern(150, -40, -25))