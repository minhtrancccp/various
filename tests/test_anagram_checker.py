"""
TODO:
    - Rewrite into at least 3 functions: one for passing, one for not passing, and one for wrong data types
    - Add time measurement for the passing tests
"""
from codetiming import Timer

from various.anagram_checker import Anagram

english_anagram_checker: Anagram = Anagram()


@Timer(text="\n{} seconds")
def test_anagram_check():
    assert english_anagram_checker.are_anagrams("Silent", "Listen")
    assert not english_anagram_checker.are_anagrams("when", "what")
