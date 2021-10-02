"""
References:
    https://en.wikipedia.org/wiki/Fizz_buzz
"""
from collections.abc import Iterable
from typing import NamedTuple


class FactorEquivalent(NamedTuple):
    value: int
    string: str


class FizzBuzz:
    def __init__(self, *factors: FactorEquivalent):
        self._factors: Iterable[FactorEquivalent] = sorted(factors) or (
            FactorEquivalent(3, "Fizz"),
            FactorEquivalent(5, "Buzz"),
        )

    def result(self, number: int) -> str:
        return "".join(
            factor.string for factor in self._factors if not number % factor.value
        ) or str(number)
