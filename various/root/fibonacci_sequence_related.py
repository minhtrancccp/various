"""
References:
    https://docs.sympy.org/latest/modules/functions/combinatorial.html?highlight=fibonacci#fibonacci
"""
from collections.abc import Iterator
from functools import cache
from itertools import count, islice, takewhile

from beartype import beartype
from codetiming import Timer
from prettytable import PrettyTable
from sympy import fibonacci

_sequence_type = Iterator[int]


@beartype
def infinite_generator(
        start_from_one: bool = True, imported_generator_used: bool = True
) -> _sequence_type:
    """
    Generate Fibonacci numbers infinitely

    Parameters
    ----------
    start_from_one : bool, optional
        Boolean flag whether the first value of the sequence is 1 or 0
        (default is True, meaning the sequence starts from 1)
    imported_generator_used : bool, optional
        Boolean flag whether sympy.fibonacci function or recursive method is used to generate the sequence
        (default is True, meaning sympy.fibonacci function is used)

    Yields
    ------
    int
        The Fibonacci numbers

    """
    if imported_generator_used:
        yield from map(fibonacci, count(2 * start_from_one))

    else:
        current: int = int(start_from_one)
        follow: int = current + 1

        while True:
            yield current
            current, follow = follow, current + follow


@beartype
def length_generator(
        length: int, start_from_one: bool = True, imported_generator_used: bool = True
) -> _sequence_type:
    """
    Generate first n Fibonacci numbers

    Parameters
    ----------
    length : int
        The length n of the generated sequence, must be a positive integer (i.e. >= 1)
    start_from_one : bool, optional
        Boolean flag whether sequence starts from 1 or 0
        (default is True, meaning the sequence starts from 1)
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
) -> _sequence_type:
    """
    Generate Fibonacci numbers upto and including given value

    Parameters
    ----------
    max_value : int
        The maximum Fibonacci number to be generated
    start_from_one : bool, optional
        Boolean flag whether sequence starts from 1 or 0
        (default is True, meaning the sequence starts from 1)
    imported_generator_used : bool, optional
        Boolean flag whether sympy.fibonacci function or recursive technique is used to generate the sequence
        (default is True, meaning sympy.fibonacci function is used)

    Yields
    ------
    int
        Fibonacci numbers satisfying the conditions

    """
    if max_value <= 1:
        raise ValueError(f"{max_value=} is not a non-negative integer")

    yield from takewhile(
        max_value.__ge__, infinite_generator(start_from_one, imported_generator_used)
    )


@cache
@beartype
def recursive_function(index: int) -> int:
    """
    Given an integer index, return the Fibonacci value using recursive method

    Parameters
    ----------
    index : int
        Index of the Fibonacci number to be found, using zero-based numbering
        (0th Fibonacci number is 0, 1st is 1, 2nd is 1, 3rd is 2, etc.)

    Returns
    -------
    int
        Fibonacci value at the given index

    """
    if index <= -1:
        return recursive_function(-index) * (-1) ** (index + 1)

    elif index <= 1:
        return index

    else:
        return recursive_function(index - 1) + recursive_function(index - 2)


def _test_factory(value: int) -> tuple[int, int]:
    return value, recursive_function(value)


if __name__ == "__main__":
    fibonacci_table: PrettyTable = PrettyTable(["Index", "Value"])

    with Timer():
        fibonacci_table.add_rows(reversed([*map(_test_factory, range(100, -1, -1))]))

    print(fibonacci_table)
