"""
References:
    https://twitter.com/fermatslibrary/status/1275066521450975234

TODO:
    - Add documentation
"""
from collections.abc import Collection
from math import prod
from string import ascii_lowercase
from typing import Annotated

from beartype import beartype
from beartype.vale import Is
from more_itertools import all_equal
from sympy import sieve

from auxiliary.latin_string import LatinString, letter_filter

LETTER_TO_PRIME: dict[str, int] = dict(zip(ascii_lowercase, sieve))


@beartype
def _long_enough(collection: Collection) -> bool:
    return len(collection) >= 2


@beartype
def string_to_product(string: LatinString) -> int:
    return prod(map(LETTER_TO_PRIME.get, letter_filter(string)))


@beartype
def anagram_checker(
    strings: Annotated[Collection[LatinString], Is[_long_enough]]
) -> bool:
    """
    Determine whether given strings are anagrams by calculating the product of primes
    """

    return all_equal(map(string_to_product, strings))
