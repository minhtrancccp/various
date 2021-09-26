"""
TODO:
    - Use hypothesis to conduct property-based tests
"""

from re import escape

from beartype.roar import BeartypeCallHintPepParamException
from pytest import mark, raises

from miscellaneous_python.anagram import anagram_checker

ParamsType: type[tuple] = tuple[str, ...]


@mark.parametrize(
    "are_anagrams_params",
    [
        ("Silent", "Listen"),
        ("Anagram", "Nag a ram"),
        ("liter", "litre", "tiler"),
        ("ArE", "eAr"),
    ],
)
def test_are_anagrams(are_anagrams_params: ParamsType):
    assert anagram_checker(are_anagrams_params)


@mark.parametrize(
    "not_anagrams_params",
    [("where", "when"), ("nag", "Gram"), ("liter", "litre", "tiler", "peril")],
)
def test_not_anagrams(not_anagrams_params: ParamsType):
    assert not anagram_checker(not_anagrams_params)


@mark.parametrize("not_enough_params", [tuple(), ("where",)])
def test_not_enough_params(not_enough_params: ParamsType):
    not_enough_message: str = escape("violates validator Is[_has_sufficient_length()]")
    with raises(
        BeartypeCallHintPepParamException,
        match=not_enough_message,
    ):
        anagram_checker(not_enough_params)


@mark.parametrize(
    "not_latin_params", [("$&%367#%&56", " 5&467865{|:$ 5"), ("情人", "人情")]
)
def test_not_latin_params(not_latin_params: ParamsType):
    not_latin_message: str = escape("violates validator Is[has_latin_letters()]")
    with raises(
        BeartypeCallHintPepParamException,
        match=not_latin_message,
    ):
        anagram_checker(not_latin_params)
