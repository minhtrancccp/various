from collections import Callable
from random import sample

from hypothesis import given
from hypothesis.strategies import (
    DataObject,
    SearchStrategy,
    characters,
    composite,
    data,
    integers,
    text,
)

from miscellaneous_python.type_hints.basic_latin_letters import (
    latin_filter,
    string_validator,
)

LETTER_CATEGORY: str = "L"
UPPER_A_CODEPOINT: int = 41
LOWER_Z_CODEPOINT: int = 122
MARK_CATEGORY: str = "M"


@composite
def string_generator(
    draw: Callable[[SearchStrategy[str]], str],
    latin_only: bool = True,
    latin_count_min: int = 0,
) -> str:
    latin_letter_string: str = draw(
        text(
            characters(
                whitelist_categories=LETTER_CATEGORY,
                min_codepoint=UPPER_A_CODEPOINT,
                max_codepoint=LOWER_Z_CODEPOINT,
            ),
            min_size=latin_count_min,
        )
    )
    non_letter_string: str = draw(
        text(characters(blacklist_categories=(LETTER_CATEGORY, MARK_CATEGORY)))
    )

    result: str = latin_letter_string + non_letter_string

    if not latin_only:
        non_latin_string: str = draw(
            text(
                characters(
                    whitelist_categories=(LETTER_CATEGORY, MARK_CATEGORY),
                    min_codepoint=LOWER_Z_CODEPOINT + 1,
                ),
                min_size=1,
            )
        )
        result += non_latin_string

    return "".join(sample(result, k=len(result)))


@given(string_generator(latin_count_min=1))
def test_valid_string(string: str) -> None:
    assert string_validator(string)


@given(string_generator(latin_only=False))
def test_invalid_string(string: str) -> None:
    assert not string_validator(string)


@given(data())
def test_latin_filter(data_strategy: DataObject):
    latin_count: int = data_strategy.draw(integers(min_value=1))
    drawn_string: str = data_strategy.draw(
        string_generator(latin_count_min=latin_count)
    )

    assert len(latin_filter(drawn_string)) >= latin_count
