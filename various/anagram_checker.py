"""
References:
    https://twitter.com/fermatslibrary/status/1275066521450975234

TODO:
    - Explain why 27th prime is needed when defining Anagram object
    - Consider to implement acceptance of self defined alphabet
    - Add documentation for the are_anagrams method
"""
from math import prod
from string import ascii_lowercase

from beartype import beartype
from more_itertools import all_equal
from sympy import primerange


class Anagram:
    def __init__(self):
        twenty_seventh_prime: int = 103
        self._char_prime_dict: dict[str, int] = dict(
            zip(ascii_lowercase, primerange(2, twenty_seventh_prime))
        )

    def _word_to_product(self, word: str) -> int:
        return prod(
            self._char_prime_dict[char] for char in word.lower() if char.isalpha()
        )

    @beartype
    def are_anagrams(self, *words: str) -> bool:
        """
        Determine whether given strings are anagrams by calculating the product of primes
        """

        return all_equal(map(self._word_to_product, words))
