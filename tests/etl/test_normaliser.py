import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            ".."
        )
    )
)

from src.normaliser import (
    normalize_year,
    normalize_ticker
)

def test_normalize_year():

    assert normalize_year(
        " Mar 2024 "
    ) == "Mar 2024"


def test_normalize_ticker():

    assert normalize_ticker(
        " tcs "
    ) == "TCS"


print("test_normaliser passed!")