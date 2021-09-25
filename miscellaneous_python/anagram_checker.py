"""
References:
    https://twitter.com/fermatslibrary/status/1275066521450975234

TODO:
    - Add documentation
"""
from math import prod
from re import findall
from string import ascii_lowercase

from beartype import beartype
from more_itertools import all_equal
from sympy import sieve


class InvalidString(ValueError):
    def __init__(self, string: str):
        self._string: str = string
        self._message: str = "String doesn't contain any basic Latin letters"

        super().__init__(self._message)

    def __str__(self):
        return f"{self._string!r} -> {self._message}"


class Anagram:
    def __init__(self) -> None:
        latin_letter_count: int = 26
        sieve.extend_to_no(latin_letter_count)

        self._letter_to_prime: dict[str, int] = dict(zip(ascii_lowercase, sieve._list))

    def _string_to_product(self, string: str) -> int:
        latin_letter_pattern: str = r"[a-z]"
        appeared_letters: list[str] = findall(latin_letter_pattern, string.lower())

        if not appeared_letters:
            raise InvalidString(string)

        return prod(map(self._letter_to_prime.get, appeared_letters))

    @beartype
    def are_anagrams(self, *strings: str) -> bool:
        """
        Determine whether given strings are anagrams by calculating the product of primes
        """

        return all_equal(map(self._string_to_product, strings))
