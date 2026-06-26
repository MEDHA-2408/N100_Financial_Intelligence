from src.analytics.cagr import calculate_cagr


def test_normal_cagr():

    value, flag = calculate_cagr(100, 200, 5)

    assert flag == "SUCCESS"


def test_zero_base():

    value, flag = calculate_cagr(0, 100, 5)

    assert flag == "ZERO_BASE"


def test_turnaround():

    value, flag = calculate_cagr(-100, 100, 5)

    assert flag == "TURNAROUND"


def test_decline():

    value, flag = calculate_cagr(100, -50, 5)

    assert flag == "DECLINE_TO_LOSS"


def test_negative():

    value, flag = calculate_cagr(-100, -200, 5)

    assert flag == "BOTH_NEGATIVE"


def test_invalid_years():

    value, flag = calculate_cagr(100, 200, 0)

    assert flag == "INVALID_YEARS"