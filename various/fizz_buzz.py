"""
References:
    https://en.wikipedia.org/wiki/Fizz_buzz
"""
from math import factorial

from codetiming import Timer

_reference: dict[int, str] = {3: "Fizz", 5: "Buzz"}


def formatter(number: int) -> str:
    return "".join(
        value for key, value in _reference.items() if not number % key
    ) or str(number)


@Timer(text="\n{} seconds")
def test_formatter():
    assert formatter(factorial(15)) == "FizzBuzz"
