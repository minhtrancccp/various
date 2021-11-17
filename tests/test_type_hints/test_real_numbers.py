from hypothesis import given, strategies
from numerary.types import RealLike

from type_hints.real_numbers import is_not_negative, is_positive_real


def is_zero(value: RealLike) -> bool:
    return is_not_negative(value) and not is_positive_real(value)


@given(
    strategies.one_of(
        strategies.decimals(min_value=0, allow_nan=False),
        strategies.floats(min_value=0),
        strategies.fractions(min_value=0),
        strategies.integers(min_value=0),
    )
)
def test_positive_numbers(value: RealLike) -> None:
    assert (
        is_not_negative(value) and is_positive_real(value) if value else is_zero(value)
    )


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
        not (is_not_negative(value) or is_positive_real(value))
        if value
        else is_zero(value)
    )
