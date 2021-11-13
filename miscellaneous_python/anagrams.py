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
    Return product of primes corresponding to each letter in the given string

    Raises
    ------
    BeartypeCallHintPepParamException
        If the given string is not a Basic Latin one

    Examples
    --------
    >>> string_to_product('abc')
    30

    >>> string_to_product('xyz')
    871933
    """

    return prod(map(LETTER_TO_PRIME.get, letter_filter(string)))


@beartype
def anagram_checker(
    strings: Annotated[Collection[LatinString], Is[_long_enough]]
) -> bool:
    """
    Return a boolean indicating whether given strings are anagrams by calculating the product of corresponding primes

    Raises
    ------
    BeartypeCallHintPepParamException
        If any of the given strings is not a Basic Latin one or fewer than two strings are given

    Examples
    --------
    >>> anagram_checker(['abc', 'cba'])
    True

    >>> anagram_checker(['abc', 'cba', 'xyz'])
    False
    """

    return all_equal(map(string_to_product, strings))
