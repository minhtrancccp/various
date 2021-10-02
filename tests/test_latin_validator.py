from hypothesis import given
from hypothesis.strategies import from_regex
from pytest import mark

from miscellaneous_python.latin_validator import STRING_PATTERN, string_validator


@mark.skip("Prioritize refactoring Git history before improving scripts")
@given(from_regex(STRING_PATTERN))
def test_valid_string(string: str):
    assert string_validator(string)
