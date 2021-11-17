from hypothesis import given
from hypothesis.strategies import integers

from roman_numeral import decoder, encoder


@given(integers(min_value=1, max_value=3_999))
def test_roman_numeral(decimal: int):
    assert decoder(encoder(decimal)) == decimal
