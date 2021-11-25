"""
References:
    https://docs.sympy.org/latest/modules/functions/combinatorial.html?highlight=fibonacci#fibonacci

TODO:
    - Rewrite the script to be a class like sympy.Sieve
"""
from collections.abc import Iterator
from itertools import count, islice, takewhile
from typing import Type

from beartype import beartype
from sympy import fibonacci

iterator_type: Type[Iterator] = Iterator[int]


@beartype
def infinite_generator(
    start_from_one: bool = True, imported_generator_used: bool = True
) -> iterator_type:
    """
    Generate Fibonacci numbers infinitely

    Parameters
    ----------
    start_from_one : bool, optional
        Boolean flag whether the first value of the sequence is 1 or 0
        (default is True, meaning the sequence will be 1, 2, 3, 5, etc.)
    imported_generator_used : bool, optional
        Boolean flag whether sympy.fibonacci function or recursive method is used to generate the sequence
        (default is True, meaning sympy.fibonacci function is used)

    Yields
    ------
    int
        The Fibonacci numbers

    """
    if imported_generator_used:
        index: int
        for index in count(2 * start_from_one):
            yield int(fibonacci(index))

    else:
        current: int = int(start_from_one)
        follow: int = current + 1

        while True:
            yield current
            current, follow = follow, current + follow


@beartype
def length_generator(
    length: int, start_from_one: bool = True, imported_generator_used: bool = True
) -> iterator_type:
    """
    Generate first n Fibonacci numbers

    Parameters
    ----------
    length : int
        The length n of the generated sequence, must be a positive integer (i.e. >= 1)
    start_from_one : bool, optional
        Boolean flag whether sequence starts from 1 or 0
        (default is True, meaning the sequence will be 1, 2, 3, 5, etc.)
    imported_generator_used : bool, optional
        Boolean flag whether sympy.fibonacci function or recursive technique is used to generate the sequence
        (default is True, meaning sympy.fibonacci function is used)

    Yields
    ------
    int
        First n Fibonacci numbers satisfying the conditions
    """
    if length <= 0:
        raise ValueError(f"{length=} is not a positive integer")

    yield from islice(
        infinite_generator(start_from_one, imported_generator_used), 0, length
    )


@beartype
def max_generator(
    max_value: int, start_from_one: bool = True, imported_generator_used: bool = True
) -> iterator_type:
    """
    Generate Fibonacci numbers up to and including given value

    Parameters
    ----------
    max_value : int
        The maximum Fibonacci number to be generated
    start_from_one : bool, optional
        Boolean flag whether sequence starts from 1 or 0
        (default is True, meaning the sequence will be 1, 2, 3, 5, etc.)
    imported_generator_used : bool, optional
        Boolean flag whether sympy.fibonacci function or recursive technique is used to generate the sequence
        (default is True, meaning sympy.fibonacci function is used)

    Yields
    ------
    int
        Fibonacci numbers satisfying the conditions

    """
    if max_value <= -1:
        raise ValueError(f"{max_value = } is not a non-negative integer")

    yield from takewhile(
        max_value.__ge__, infinite_generator(start_from_one, imported_generator_used)
    )
