from numbers import Real

from hypothesis import given, strategies

from auxiliary.real_numbers import is_not_negative, is_positive_real


def is_zero(value: Real) -> bool:
    return is_not_negative(value) and not is_positive_real(value)


@given(
    strategies.one_of(
        strategies.decimals(min_value=0, allow_nan=False),
        strategies.floats(min_value=0),
        strategies.fractions(min_value=0),
        strategies.integers(min_value=0),
    )
)
def test_positive_numbers(value: Real) -> None:
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
def test_negative_floats(value: Real) -> None:
    assert (
        not (is_not_negative(value) or is_positive_real(value))
        if value
        else is_zero(value)
    )
