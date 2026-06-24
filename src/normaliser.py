def normalize_year(year):
    """
    Convert year values to string format.
    """

    return str(year).strip()


def normalize_ticker(ticker):
    """
    Convert ticker to uppercase.
    """

    return str(ticker).strip().upper()


if __name__ == "__main__":

    print(normalize_year(" Mar 2024 "))
    print(normalize_ticker(" tcs "))