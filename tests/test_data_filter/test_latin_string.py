from random import Random

from hypothesis import given, strategies

from data_filter import latin_string
from tests import config

# Avg number of letters in an English word * upper avg word count in an English sentence
max_letter_count: int = 5 * 20


@strategies.composite
def string_generator(
    draw: config.Draw,
    latin_only: bool = True,
    latin_count_min: int = 0,
) -> str:
    latin_letter_string: str = draw(
        strategies.text(
            config.latin_letter_strategy,
            min_size=latin_count_min,
            max_size=max_letter_count,
        )
    )
    non_letter_string: str = draw(strategies.text(config.non_letter_strategy))

    result: str = latin_letter_string + non_letter_string

    if not latin_only:
        non_latin_string: str = draw(
            strategies.text(
                strategies.characters(
                    whitelist_categories=config.LETTER_CATEGORY,
                    min_codepoint=config.LOWER_Z_CODEPOINT + 1,
                ),
                min_size=1,
            )
        )
        result += non_latin_string

    sampler: Random = draw(strategies.randoms())
    return "".join(sampler.sample(result, k=len(result)))


@given(string_generator(latin_count_min=1))
def test_valid_string(string: str):
    assert latin_string.string_validator(string)


@given(string_generator(latin_only=False))
def test_invalid_string(string: str):
    assert not latin_string.string_validator(string)


@given(strategies.data())
def test_latin_filter(data_strategy: strategies.DataObject):
    latin_count: int = data_strategy.draw(
        strategies.integers(min_value=1, max_value=max_letter_count)
    )
    drawn_string: str = data_strategy.draw(
        string_generator(latin_count_min=latin_count)
    )

    drawn_case_mode: latin_string.CaseConversionModes = data_strategy.draw(
        strategies.sampled_from(latin_string.CaseConversionModes)
    )

    assert len(latin_string.letter_filter(drawn_string, drawn_case_mode)) >= latin_count
