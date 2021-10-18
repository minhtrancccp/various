from numbers import Real
from typing import Optional

from hypothesis import example, given
from hypothesis.strategies import SearchStrategy, floats

from auxiliary.real_numbers import is_positive_real
from miscellaneous_python.climbing_snail import Snail

positive_real_strategies: SearchStrategy[float] = floats(
    min_value=0,
    exclude_min=True,
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
def test_timer(forward: Real, backward: Real, distance: Real) -> None:
    snail: Snail = Snail(forward, backward)

    result: Optional[Real] = snail.timer(distance)
    if distance <= snail.forward:
        assert result == 1

    elif not snail.normal_snail():
        assert result is None

    else:
        assert is_positive_real(result)
