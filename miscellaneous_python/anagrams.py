"""
References:
    https://twitter.com/fermatslibrary/status/1275066521450975234
"""
from collections.abc import Collection
from math import prod
from string import ascii_lowercase
from typing import Annotated

from beartype import beartype
from beartype.vale import Is
from more_itertools import all_equal
from sympy import sieve

from type_hints.latin_string import LatinString, letter_filter

LETTER_TO_PRIME: dict[str, int] = dict(zip(ascii_lowercase, sieve))


@beartype
def _long_enough(collection: Collection) -> bool:
    """
    Return a boolean indicating whether enough strings are given to be checked for occurrences of anagrams
    """

    return len(collection) >= 2


@beartype
def string_to_product(string: LatinString) -> int:
    """
    Return the product of the primes corresponding to each letter in the given string
    """

    return prod(map(LETTER_TO_PRIME.get, letter_filter(string)))


@beartype
def anagram_checker(
    strings: Annotated[Collection[LatinString], Is[_long_enough]]
) -> bool:
    """
    Return a boolean indicating whether given strings are anagrams by calculating the product of corresponding primes
    """

    return all_equal(map(string_to_product, strings))
