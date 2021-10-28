from collections.abc import Collection

from hypothesis import example, given
from hypothesis.strategies import booleans, composite, integers, randoms, text

from miscellaneous_python.anagrams import anagram_checker
from tests.shared_strategies import Draw, latin_letter_strategy

Strings: type[Collection] = Collection[str]
CharGroup: type[list] = list[str]


@composite
def strings_generator(draw: Draw, inverse_test: bool = False) -> Strings:
    letter_only_groups: list[CharGroup] = []

    def new_group() -> CharGroup:
        generated_group: CharGroup = sorted(
            draw(text(latin_letter_strategy, min_size=1)).lower()
        )
        return (
            generated_group
            if generated_group not in letter_only_groups
            else new_group()
        )

    most_anagrams_possible: int = 11
    word_count: int
    for word_count in range(draw(integers(2, most_anagrams_possible))):
        letter_only_groups.append(
            new_group() if inverse_test or not word_count else letter_only_groups[0]
        )

    result: list[str] = []

    group: CharGroup
    for group in letter_only_groups:
        index: int
        letter: str
        for index, letter in enumerate(group):
            if draw(booleans()):
                group[index] = letter.swapcase()

        # TODO: why non_letter_strategy includes chars like "Ι" (U+03B9)
        # group.extend(draw(text(non_letter_strategy)))
        draw(randoms()).shuffle(group)

        result.append("".join(group))

    return result


@given(strings_generator())
@example(("Silent", "Listen"))
@example(("Anagram", "Nag a ram"))
@example(("liter", "litre", "tiler"))
@example(("ArE", "eAr"))
def test_are_anagrams(are_anagrams_params: Strings):
    assert anagram_checker(are_anagrams_params)


# TODO: RecursionError raises
@given(strings_generator(True))
@example(("where", "when"))
@example(("nag", "Gram"))
@example(("liter", "litre", "tiler", "peril"))
def test_not_anagrams(not_anagrams_params: Strings):
    assert not anagram_checker(not_anagrams_params)
