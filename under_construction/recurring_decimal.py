from itertools import dropwhile
from math import log10

from beartype import beartype
from sympy import divisors, reduced_totient

from type_hints.real_numbers import PositiveInteger


def _totient_rule(value: PositiveInteger) -> int:
    lower_limit: float = log10(value)
    sub_target: int = value - 1

    divisor: int
    for divisor in dropwhile(lower_limit.__gt__, divisors(reduced_totient(value))):
        result: int = pow(10, divisor, value)
        if result == 1:
            return divisor

        if result == sub_target:
            return divisor * 2


@beartype
def reptend_length(denominator: PositiveInteger) -> int:
    excluded: int
    redundant_prime_factors: set[int] = {2, 5}
    for excluded in redundant_prime_factors:
        while not denominator % excluded:
            denominator //= excluded

    return 0 if denominator == 1 else _totient_rule(denominator)
