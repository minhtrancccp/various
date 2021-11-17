"""
References:
    https://rosettacode.org/wiki/Fibonacci_sequence#Recursive_64
"""

from functools import cache

from beartype import beartype


@cache
@beartype
def recursive_function(index: int) -> int:
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


@beartype
def _row_factory(value: int) -> tuple[int, int]:
    """
    Return a tuple of given index and the Fibonacci number at that index
    """

    return value, recursive_function(value)


def main():
    from codetiming import Timer
    from prettytable import PrettyTable

    column_names: tuple[str, str] = ("Index", "Value")
    fibonacci_table: PrettyTable = PrettyTable(column_names)

    value_count: int = 500
    with Timer():
        fibonacci_table.add_rows(map(_row_factory, range(value_count)))

    print(fibonacci_table)


if __name__ == "__main__":
    main()
