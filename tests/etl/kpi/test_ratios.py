from src.analytics.ratios import (
    net_profit_margin,
    operating_profit_margin,
    return_on_equity,
    roce,
    roa,
    debt_to_equity,
    interest_coverage,
    asset_turnover,
)


def test_net_profit_margin():
    assert round(net_profit_margin(100, 1000), 2) == 10.00


def test_zero_sales():
    assert net_profit_margin(100, 0) is None


def test_operating_profit_margin():
    assert round(operating_profit_margin(200, 1000), 2) == 20.00


def test_return_on_equity():
    assert round(return_on_equity(100, 200, 300), 2) == 20.00


def test_negative_equity():
    assert return_on_equity(100, -100, 50) is None


def test_roce():
    assert round(roce(200, 300, 300, 400), 2) == 20.00


def test_roa():
    assert round(roa(100, 1000), 2) == 10.00


def test_debt_to_equity():
    assert round(debt_to_equity(200, 300, 200), 2) == 0.40


def test_debt_free():
    assert debt_to_equity(0, 200, 100) == 0


def test_interest_coverage():
    assert round(interest_coverage(100, 20, 10), 2) == 12.00


def test_zero_interest():
    assert interest_coverage(100, 20, 0) is None


def test_asset_turnover():
    assert round(asset_turnover(1000, 500), 2) == 2.00