from collections.abc import Collection
from random import Random

from hypothesis import example, given
from hypothesis.strategies import booleans, composite, integers, randoms
from pytest import mark

from data_filter.latin_string import LatinString
from data_filter.real_numbers import PositiveInteger
from miscellaneous_python.anagrams import anagram_checker
from tests.test_miscellaneous_python import config

Strings: type[Collection] = Collection[LatinString]


@composite
def strings_generator(draw: config.Draw) -> Strings:
    least_letters_used: int = 2
    base_phrase: LatinString = draw(config.string_strategy(least_letters_used, False))
    randomizer: Random = draw(randoms())
    result: list[LatinString] = []

    def swap_case(letter: LatinString) -> LatinString:
        return letter.swapcase() if draw(booleans()) else letter

    most_anagrams_possible: PositiveInteger = 11
    for _ in range(draw(integers(2, most_anagrams_possible))):
        group: list[LatinString] = [
            *map(swap_case, base_phrase),
            *draw(config.non_letter_strategy),
        ]
        randomizer.shuffle(group)

        result.append("".join(group))

    return result


@given(strings_generator())
@example(("Silent", "Listen"))
@example(("Anagram", "Nag a ram"))
@example(("liter", "litre", "tiler"))
@example(("ArE", "eAr"))
def test_are_anagrams(are_anagrams_params: Strings):
    assert anagram_checker(are_anagrams_params)


@mark.parametrize(
    "not_anagrams_params",
    (("where", "when"), ("nag", "Gram"), ("liter", "litre", "tiler", "peril")),
)
def test_not_anagrams(not_anagrams_params: Strings):
    assert not anagram_checker(not_anagrams_params)
