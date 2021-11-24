"""
References:
    https://rosettacode.org/wiki/Fibonacci_sequence#Recursive_64
"""

from functools import cache

from beartype import beartype
from numerary.types import IntegralLikeSCU


@cache
@beartype
def recursive_function(index: IntegralLikeSCU) -> IntegralLikeSCU:
    """
    Recursive function that returns the Fibonacci number at the given integer index

    Examples
    --------
    >>> recursive_function(0)
    0

    >>> recursive_function(1)
    1

    >>> recursive_function(3)
    2

    >>> recursive_function(-5)
    5
    """

    if index <= -1:
        return recursive_function(-index) * (-1) ** ((index + 1) % 2)

    elif index <= 1:
        return index

    else:
        return recursive_function(index - 1) + recursive_function(index - 2)
