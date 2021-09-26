import pytest
from hypothesis import given
from hypothesis.strategies import from_regex

from miscellaneous_python.latin_validator import STRING_PATTERN, string_validator


@given(from_regex(STRING_PATTERN))
def test_valid_string(string: str):
    assert string_validator(string)
