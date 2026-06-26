import pandas as pd


def net_profit_margin(net_profit, sales):
    """
    Net Profit Margin = Net Profit / Sales × 100
    """

    if sales == 0:
        return None

    return (net_profit / sales) * 100


def operating_profit_margin(operating_profit, sales):
    """
    Operating Profit Margin = Operating Profit / Sales × 100
    """

    if sales == 0:
        return None

    return (operating_profit / sales) * 100


def return_on_equity(net_profit, equity, reserves):
    """
    ROE = Net Profit / (Equity + Reserves) × 100
    """

    capital = equity + reserves

    if capital <= 0:
        return None

    return (net_profit / capital) * 100


def roce(ebit, equity, reserves, borrowings):
    """
    ROCE = EBIT / (Equity + Reserves + Borrowings) × 100
    """

    employed = equity + reserves + borrowings

    if employed <= 0:
        return None

    return (ebit / employed) * 100


def roa(net_profit, total_assets):
    """
    Return on Assets
    """

    if total_assets == 0:
        return None

    return (net_profit / total_assets) * 100


def debt_to_equity(borrowings, equity, reserves):
    """
    Debt to Equity Ratio
    """

    if borrowings == 0:
        return 0

    capital = equity + reserves

    if capital <= 0:
        return None

    return borrowings / capital


def interest_coverage(operating_profit, other_income, interest):
    """
    Interest Coverage Ratio
    """

    if interest == 0:
        return None

    return (operating_profit + other_income) / interest


def asset_turnover(sales, total_assets):
    """
    Asset Turnover
    """

    if total_assets == 0:
        return None

    return sales / total_assets