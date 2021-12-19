from hypothesis import given
from hypothesis.strategies import DataObject, data, integers, sampled_from

from data_filter import latin_string
from data_filter.real_numbers import PositiveInteger
from tests.data_filter.config import MAX_LETTER_COUNT, string_strategy


@given(string_strategy(1))
def test_valid_string(string: str):
    assert latin_string.string_validator(string)


@given(string_strategy(non_latin_included=True))
def test_invalid_string(string: str):
    assert not latin_string.string_validator(string)


@given(data())
def test_latin_filter(data_strategy: DataObject):
    latin_count: PositiveInteger = data_strategy.draw(
        integers(min_value=1, max_value=MAX_LETTER_COUNT)
    )
    drawn_string: str = data_strategy.draw(string_strategy(latin_count))

    drawn_case_mode: latin_string.CaseConversionModes = data_strategy.draw(
        sampled_from(latin_string.CaseConversionModes)
    )

    assert len(latin_string.letter_filter(drawn_string, drawn_case_mode)) >= latin_count
