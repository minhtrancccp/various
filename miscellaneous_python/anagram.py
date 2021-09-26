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

from miscellaneous_python.latin_letter_validator import StringType, latin_letter_filter

CollectionType: type[Collection] = Collection[str]


@beartype
def _has_sufficient_length(collection: CollectionType) -> bool:
    return len(collection) >= 2


_LATIN_LETTER_COUNT: int = 26
sieve.extend_to_no(_LATIN_LETTER_COUNT)

_LETTER_TO_PRIME: dict[str, int] = dict(zip(ascii_lowercase, sieve._list))


@beartype
def _string_to_product(string: StringType) -> int:
    return prod(map(_LETTER_TO_PRIME.get, latin_letter_filter(string)))


@beartype
def anagram_checker(
    strings: Annotated[CollectionType, Is[_has_sufficient_length]]
) -> bool:
    """
    Determine whether given strings are anagrams by calculating the product of primes
    """

    return all_equal(map(_string_to_product, strings))
