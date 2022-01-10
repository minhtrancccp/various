"""
References:
    https://mathworld.wolfram.com/FibonacciNumber.html

TODO:
    - Add docstrings & doctests
    - Add unit tests
"""

from functools import cache
from typing import Annotated

from beartype import beartype
from beartype.vale import Is
from numerary.types import IntegralLikeSCU


@beartype
def _within_recursion_limit(index: IntegralLikeSCU) -> bool:
    from sys import getrecursionlimit

    return abs(index) <= getrecursionlimit()


@cache
@beartype
def recursive_fibonacci(
    index: Annotated[IntegralLikeSCU, Is[_within_recursion_limit]]
) -> IntegralLikeSCU:
    """
    Recursive function that returns the Fibonacci number at the given integer index.

    Index must be smaller than the system's recursion limit, which can be raised manually with sys.setrecursionlimit().

    Examples
    --------
    >>> recursive_fibonacci(0)
    0

    >>> recursive_fibonacci(1)
    1

    >>> recursive_fibonacci(3)
    2

    >>> recursive_fibonacci(-5)
    5
    """

    if index <= -1:
        return recursive_fibonacci(-index) * (-1) ** ((index + 1) % 2)

    elif index <= 1:
        return index

    else:
        return recursive_fibonacci(index - 1) + recursive_fibonacci(index - 2)


@beartype
def optimized_fibonacci(index: IntegralLikeSCU) -> IntegralLikeSCU:
    from sympy import fibonacci

    return (
        recursive_fibonacci(index)
        if _within_recursion_limit(index)
        else fibonacci(index)
    )
