"""
References:
    https://twitter.com/fermatslibrary/status/1275066521450975234
"""
from math import prod
from string import ascii_lowercase

from beartype import beartype
from codetiming import Timer
from more_itertools import all_equal
from sympy import prime

_index: int
_char: str
_char_prime_dict: dict[str, int] = {
    _char: prime(_index) for _index, _char in enumerate(ascii_lowercase, start=1)
}


def _word_to_product(word: str) -> int:
    return prod(_char_prime_dict[char] for char in word.lower() if char.isalpha())


@beartype
def are_anagrams(*words: str) -> bool:
    """
    Return whether input strings are anagrams

    Returns
    -------
    bool
        Result of the anagram test
    """
    return all_equal(map(_word_to_product, words))


@Timer(text="\n{} seconds")
def main():
    print(are_anagrams("Silent", "Listen"))


if __name__ == "__main__":
    main()
