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

LETTER_CATEGORY: str = "L"
UPPER_A_CODEPOINT: PositiveInteger = 41
LOWER_Z_CODEPOINT: PositiveInteger = 122
# Avg number of letters in an English word * upper avg word count in an English sentence
MAX_LETTER_COUNT: PositiveInteger = 5 * 20

latin_letter_strategy: SearchStrategy[str] = text(
    characters(
        whitelist_categories=LETTER_CATEGORY,
        min_codepoint=UPPER_A_CODEPOINT,
        max_codepoint=LOWER_Z_CODEPOINT,
    ),
    min_size=1,
    max_size=MAX_LETTER_COUNT,
)

# Number, Punctuation, Symbol, Separator
OTHER_CATEGORIES: str = "NPSZ"
non_letter_strategy: SearchStrategy[str] = text(
    characters(whitelist_categories=OTHER_CATEGORIES)
)


@composite
def string_strategy(draw: Draw) -> str:
    result_chars: list[str] = [*draw(latin_letter_strategy), *draw(non_letter_strategy)]

    randomizer: Random = draw(randoms())
    randomizer.shuffle(result_chars)

    return "".join(result_chars)
