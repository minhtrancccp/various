from various.application.zeckendorf import decimal_to_zeckendorf, fibonacci_to_decimal


def test_zeckendorf():
    assert decimal_to_zeckendorf(0) == "0"
    assert fibonacci_to_decimal("1001") == 6
    assert fibonacci_to_decimal("0") == 0
