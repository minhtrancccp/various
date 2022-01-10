"""
References:
    https://twitter.com/fermatslibrary/status/1275066521450975234
"""

from collections.abc import Collection
from typing import Annotated

from beartype import beartype
from beartype.vale import Is

from data_filter.latin_string import CaseConversionModes, LatinString, letter_filter
from data_filter.real_numbers import PositiveInteger


@beartype
def _long_enough(collection: Collection) -> bool:
    """
    Return a boolean indicating if enough strings, i.e. at least 2, are given to be checked for occurrences of anagrams
    """

    return len(collection) >= 2


@beartype
def string_to_product(string: LatinString) -> PositiveInteger:
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

    from math import prod
    from string import ascii_lowercase

    from sympy import sieve

    letter_to_prime: dict[str, PositiveInteger] = dict(zip(ascii_lowercase, sieve))
    return prod(
        map(letter_to_prime.get, letter_filter(string, CaseConversionModes.LOWERCASE))
    )


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

    from more_itertools import all_equal

    return all_equal(map(string_to_product, strings))
