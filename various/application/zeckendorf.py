"""
References:
    https://en.wikipedia.org/wiki/Zeckendorf%27s_theorem
"""
from collections.abc import Callable
from itertools import compress
from typing import Union

from various.root.fibonacci_sequence_related import length_generator, max_generator

_replace_args: tuple[str, str, int] = ("011", "100", 1)


def _wrapper(
    func: Callable[[str], Union[int, str]]
) -> Callable[[str], Union[int, str]]:
    def _valid_sequence(sequence: str) -> Union[int, str]:
        if all(map("01".__contains__, sequence)):
            return func(sequence)

        raise ValueError(f"{sequence=} has digits different than 0 or 1")

    return _valid_sequence


def decimal_to_zeckendorf(integer: int) -> str:
    if integer <= -1:
        raise ValueError(f"{integer=} is not a non-negative integer")

    if not integer:
        return "0"

    zeckendorf_representation: str = ""
    for base in reversed([*max_generator(integer)]):
        if integer >= base:
            zeckendorf_representation += "1"
            integer -= base

        else:
            zeckendorf_representation += "0"

    return zeckendorf_representation


@_wrapper
def fibonacci_to_zeckendorf(fibonacci_sequence: str) -> str:
    return (
        fibonacci_to_zeckendorf(f"0{fibonacci_sequence}".replace(*_replace_args))
        if "11" in fibonacci_sequence
        else fibonacci_sequence.lstrip("0")
    )


@_wrapper
def fibonacci_to_decimal(fibonacci_sequence: str) -> int:
    return sum(
        compress(
            length_generator(len(fibonacci_sequence)),
            map(int, reversed(fibonacci_sequence)),
        )
    )
