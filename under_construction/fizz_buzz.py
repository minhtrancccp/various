"""
References:
    https://en.wikipedia.org/wiki/Fizz_buzz
"""
from collections.abc import Iterable
from dataclasses import dataclass

from beartype import beartype


@dataclass(frozen=True, order=True)
class FactorEquivalent:
    value: int
    string: str


class FizzBuzz:
    def __init__(self, *factors: FactorEquivalent) -> None:
        self._factors: Iterable[FactorEquivalent] = sorted(factors) or (
            FactorEquivalent(3, "Fizz"),
            FactorEquivalent(5, "Buzz"),
        )

    @property
    @beartype
    def factors(self):
        for factor in self._factors:
            yield factor

    @beartype
    def result(self, number: int) -> str:
        return "".join(
            factor.string for factor in self._factors if not number % factor.value
        ) or str(number)


def main():
    FizzBuzz()


if __name__ == "__main__":
    main()
