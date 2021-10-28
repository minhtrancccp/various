from typing import Callable, TypeVar

from hypothesis.strategies import SearchStrategy, characters

T = TypeVar("T")
Draw: type[Callable] = Callable[[SearchStrategy[T]], T]

LETTER_CATEGORY: str = "L"
OTHER_CATEGORY: str = "C"
UPPER_A_CODEPOINT: int = 41
LOWER_Z_CODEPOINT: int = 122

latin_letter_strategy: SearchStrategy[str] = characters(
    whitelist_categories=LETTER_CATEGORY,
    min_codepoint=UPPER_A_CODEPOINT,
    max_codepoint=LOWER_Z_CODEPOINT,
)
non_letter_strategy: SearchStrategy[str] = characters(
    blacklist_categories=(LETTER_CATEGORY, OTHER_CATEGORY)
)
