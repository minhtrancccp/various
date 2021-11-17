from hypothesis import given, strategies
from numerary.types import RealLike

from data_filter.real_numbers import not_negative, positive_real


def is_zero(value: RealLike) -> bool:
    return not_negative(value) and not positive_real(value)


@given(
    strategies.one_of(
        strategies.decimals(min_value=0, allow_nan=False),
        strategies.floats(min_value=0),
        strategies.fractions(min_value=0),
        strategies.integers(min_value=0),
    )
)
def test_positive_numbers(value: RealLike) -> None:
    assert not_negative(value) and positive_real(value) if value else is_zero(value)


@given(
    strategies.one_of(
        strategies.decimals(max_value=0, allow_nan=False),
        strategies.floats(max_value=0),
        strategies.fractions(max_value=0),
        strategies.integers(max_value=0),
    )
)
def test_negative_floats(value: RealLike):
    assert (
        not (not_negative(value) or positive_real(value)) if value else is_zero(value)
    )
