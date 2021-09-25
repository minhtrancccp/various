"""
TODO:
    - Use hypothesis to conduct property-based tests
"""

from miscellaneous_python.zeckendorf import (
    decimal_to_zeckendorf,
    fibonacci_to_decimal,
    fibonacci_to_zeckendorf,
)


def test_dz():
    assert decimal_to_zeckendorf(0) == "0"
    assert decimal_to_zeckendorf(1) == "1"
    assert decimal_to_zeckendorf(10) == "10010"


def test_fz():
    assert fibonacci_to_zeckendorf("1111") == "10100"


def test_fd():
    assert fibonacci_to_decimal("1001") == 6
    assert fibonacci_to_decimal("0") == 0
