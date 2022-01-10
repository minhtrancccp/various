"""
References:
    https://mathworld.wolfram.com/ZeckendorfRepresentation.html
    https://pi.edu.vn/detail-news/bieu-dien-zeckendorf-va-tro-choi-fibonacci-nim-120.html (Vietnamese)

TODO:
    - Add docstrings & doctests
    - Add unit tests
"""

from typing import Annotated, Optional

from beartype import beartype
from beartype.vale import Is

from data_filter.real_numbers import NaturalNumber
from miscellaneous_python.fibonacci_sequence import optimized_fibonacci


@beartype
def _binary_string(string: str) -> bool:
    try:
        int(string, 2)
        return True

    except ValueError:
        return False


FibonacciRepresentation: type[str] = Annotated[str, Is[_binary_string]]


@beartype
def decimal_to_zeckendorf(integer: NaturalNumber) -> FibonacciRepresentation:
    from itertools import count, takewhile

    if integer <= 1:
        return str(integer)

    fibonacci_bases: list[int] = [
        *takewhile(integer.__ge__, map(optimized_fibonacci, count(2)))
    ]

    zeckendorf_representation: str = ""
    while integer:
        next_digit: int
        next_digit, integer = divmod(integer, fibonacci_bases.pop())
        zeckendorf_representation += str(next_digit)

    if fibonacci_bases:
        zeckendorf_representation += "0" * (len(fibonacci_bases))

    return zeckendorf_representation


@beartype
def fibonacci_to_zeckendorf(
    fibonacci_representation: FibonacciRepresentation,
) -> FibonacciRepresentation:
    from re import Match, Pattern, compile

    double_ones_group: Pattern = compile(r"0?((?:10)*11)")
    result: Optional[Match] = double_ones_group.search(fibonacci_representation)
    if result:
        start: int
        end: int
        start, end = result.span(1)
        replacement: str = "1" + "0" * (end - start)

        return fibonacci_to_zeckendorf(
            double_ones_group.sub(replacement, fibonacci_representation, 1)
        )

    return fibonacci_representation.lstrip("0")


@beartype
def fibonacci_to_decimal(
    fibonacci_representation: FibonacciRepresentation,
) -> NaturalNumber:
    return sum(
        optimized_fibonacci(index)
        for index, value in enumerate(reversed(fibonacci_representation), start=2)
        if int(value)
    )
