from hypothesis import example, given
from hypothesis.strategies import SearchStrategy, floats

from miscellaneous_python.climbing_snail import Snail
from type_hints.real_numbers import PositiveReal, is_positive_real

# The duration between Earth's formation and its destruction is about 12.13 billion years or 4.43e12 days
# So arguments for the Snail class should have at most 12 significant digits to be considered valid
positive_real_strategies: SearchStrategy[float] = floats(
    min_value=1e-12,
    max_value=1e13,
    exclude_max=True,
    allow_nan=False,
    allow_infinity=False,
)


@example(30, 3, 2)
@example(84, 17, 15)
@example(79, 15, 9)
@example(29, 17, 4)
@example(13, 18, 8)
@example(5, 5, 10)
@example(7, 7, 7)
@example(69, 3, 8)
@example(81, 14, 14)
@given(positive_real_strategies, positive_real_strategies, positive_real_strategies)
def test_timer(forward: PositiveReal, backward: PositiveReal, distance: PositiveReal):
    snail: Snail = Snail(forward, backward)

    result: PositiveReal = snail.timer(distance)
    if distance <= snail.forward:
        assert result == 1

    elif not snail.normal_snail():
        assert result == 0

    else:
        assert is_positive_real(result)
