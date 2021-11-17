from beartype import beartype

from data_filter.real_numbers import NaturalNumber, PositiveInteger


@beartype
def _row_factory(value: NaturalNumber) -> tuple[NaturalNumber, NaturalNumber]:
    """
    Return a tuple of given index and the Fibonacci number at that index
    """

    from miscellaneous_python.recursive_fibonacci import recursive_function

    return value, recursive_function(value)


def main():
    from codetiming import Timer
    from prettytable import PrettyTable

    column_names: tuple[str, str] = ("Index", "Value")
    fibonacci_table: PrettyTable = PrettyTable(column_names)

    value_count: PositiveInteger = 500
    with Timer():
        fibonacci_table.add_rows(map(_row_factory, range(value_count)))

    print(fibonacci_table)


if __name__ == "__main__":
    main()
