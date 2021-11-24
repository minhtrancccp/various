"""
References:
    https://en.wikipedia.org/wiki/Persistence_of_a_number
"""
from collections.abc import Callable
from functools import cache
from math import prod
from typing import Optional

from beartype import beartype
from codetiming import Timer


def _prod_test(digits: list[int]) -> Optional[int]:
    if 0 in digits:
        return 1

    if 5 in digits and not all(map((1).__and__, digits)):
        return 2

    return None


@cache
@beartype
def persistence(number: int, key: Callable[[list[int]], int] = prod) -> int:
    # noinspection GrazieInspection
    """
    Count how many times the "key" operation has to be repeated for the number to reach its digital root

    Parameters
    ----------
    number : int
        Non-negative (i.e. greater than or equal to 0) integer to be calculated

    key : Callable[[list[int]], int], default=math.prod
        Operation applied on the number's digit, by default is math.prod (i.e. multiplication)

    Returns
    -------
    int
        Count of repeated operations until the number is equal to its digital root

    """
    if number <= -1:
        # Rewrite
        raise ValueError(
            f"Input number must be greater than or equal to 0, but {number = }"
        )

    if number <= 9:
        return 0

    digital_list: list[int] = [*map(int, str(number))]

    if key == prod:
        special_test: Optional[int] = _prod_test(digital_list)
        if special_test is not None:
            return special_test

    # noinspection PyTypeChecker
    return 1 + persistence(key(digital_list), key)


@Timer()
def main():
    value: int
    for value in range(10, 1000):
        print(value, persistence(value))


if __name__ == "__main__":
    main()
