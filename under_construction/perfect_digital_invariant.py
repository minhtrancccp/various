"""
References:
    https://en.wikipedia.org/wiki/Digit_sum
    https://en.wikipedia.org/wiki/Happy_number
    https://en.wikipedia.org/wiki/Perfect_digital_invariant
"""

from functools import cache
from math import log10

from beartype import beartype

from data_filter.real_numbers import NaturalNumber


@beartype
def happy_function(number: NaturalNumber, power: NaturalNumber = 2) -> int:
    return (
        1
        if log10(number).is_integer()
        else sum(int(digit) ** power for digit in str(number))
    )


@cache
@beartype
def is_happy(number: NaturalNumber) -> bool:
    formatted: int = int("".join(sorted(str(number))))
    if formatted != number:
        return is_happy(formatted)

    if formatted == 1:
        return True

    looping_numbers: set[int] = {2, 4, 16, 24, 37, 58, 89, 145}
    if formatted in looping_numbers:
        return False

    return is_happy(happy_function(formatted))
