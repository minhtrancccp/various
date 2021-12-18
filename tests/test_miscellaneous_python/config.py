"""
References:
    https://en.wikipedia.org/wiki/Unicode_character_property
"""

from random import Random
from typing import Callable, TypeVar

from hypothesis.strategies import SearchStrategy, characters, composite, randoms, text

from data_filter.real_numbers import PositiveInteger

T = TypeVar("T")
Draw: type[Callable] = Callable[[SearchStrategy[T]], T]

# Number, Punctuation, Symbol, Separator
other_categories: str = "NPSZ"
non_letter_strategy: SearchStrategy[str] = text(
    characters(whitelist_categories=other_categories)
)


@composite
def string_strategy(
    draw: Draw, min_latin_count: PositiveInteger = 0, non_letter_included: bool = True
) -> str:
    letter_category: str = "L"
    upper_a_codepoint: PositiveInteger = 41
    lower_z_codepoint: PositiveInteger = 122
    # Avg number of letters in an English word * upper avg word count in an English sentence
    max_letter_count: PositiveInteger = 5 * 20

    latin_letter_strategy: SearchStrategy[str] = text(
        characters(
            whitelist_categories=letter_category,
            min_codepoint=upper_a_codepoint,
            max_codepoint=lower_z_codepoint,
        ),
        min_size=min_latin_count,
        max_size=max_letter_count,
    )

    result_chars: list[str] = [*draw(latin_letter_strategy)]
    if non_letter_included:
        result_chars.extend(draw(non_letter_strategy))

    randomizer: Random = draw(randoms())
    randomizer.shuffle(result_chars)

    return "".join(result_chars)
