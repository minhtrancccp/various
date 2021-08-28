from codetiming import Timer

from various.anagram_checker import are_anagrams


@Timer(text="\n{} seconds")
def test_anagram_check():
    assert are_anagrams("Silent", "Listen")
