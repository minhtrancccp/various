from pytest import fixture, mark

from miscellaneous_python.anagram_checker import Anagram


@fixture
def anagram_machine() -> Anagram:
    return Anagram()


@mark.parametrize(
    "are_anagrams_params",
    [
        ("where",),
        ("Silent", "Listen"),
        ("Anagram", "Nag a ram"),
        ("liter", "litre", "tiler"),
        ("ArE", "eAr"),
        # ("$&%367#%&56", " 5&467865{|:$ 5"),
    ],
)
def test_are_anagrams(anagram_machine: Anagram, are_anagrams_params: tuple[str, ...]):
    assert anagram_machine.are_anagrams(*are_anagrams_params)


@mark.parametrize(
    "not_anagrams_params",
    [("where", "when"), ("nag", "Gram"), ("liter", "litre", "tiler", "peril")],
)
def test_not_anagrams(anagram_machine: Anagram, not_anagrams_params: tuple[str, ...]):
    assert not anagram_machine.are_anagrams(*not_anagrams_params)
