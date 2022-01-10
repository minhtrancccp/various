"""
References:
    https://mathworld.wolfram.com/AdditivePersistence.html
    https://mathworld.wolfram.com/MultiplicativePersistence.html

TODO:
    - Add docstrings & doctests
    - Add unit tests
"""

from functools import cache

from beartype import beartype

from data_filter.real_numbers import NaturalNumber


@beartype
def _digits_seperator(number: NaturalNumber) -> set[NaturalNumber]:
    return {*map(int, str(number))}


@cache
@beartype
def additive_persistence(number: NaturalNumber) -> NaturalNumber:
    return (
        0 if number <= 9 else 1 + additive_persistence(sum(_digits_seperator(number)))
    )


@cache
@beartype
def multiplicative_persistence(number: NaturalNumber) -> NaturalNumber:
    from math import prod

    even_digits: set[NaturalNumber] = {2, 4, 6, 8}

    if number <= 9:
        return 0

    digits: set[NaturalNumber] = _digits_seperator(number)
    if 0 in digits:
        return 1

    elif 5 in digits and any(map(even_digits.__contains__, digits)):
        return 2

    else:
        return 1 + multiplicative_persistence(prod(digits))
