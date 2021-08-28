"""
References:
    https://twitter.com/fermatslibrary/status/1275066521450975234
"""
from math import prod
from string import ascii_lowercase

from beartype import beartype
from more_itertools import all_equal
from sympy import prime


class _ProductEquivalent:
    def __init__(self):
        self._char_prime_dict: dict[str, int] = {
            char: prime(index) for index, char in enumerate(ascii_lowercase, start=1)
        }

    def word_to_product(self, word: str) -> int:
        return prod(
            self._char_prime_dict[char] for char in word.lower() if char.isalpha()
        )


@beartype
def are_anagrams(*words: str) -> bool:
    """
    Determine whether given strings are anagrams by calculating the product of primes
    """
    machine: _ProductEquivalent = _ProductEquivalent()
    return all_equal(map(machine.word_to_product, words))
