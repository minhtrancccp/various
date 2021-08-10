"""
References:
    https://codegolf.stackexchange.com/questions/130290/the-snail-in-the-well
"""
from math import ceil
from numbers import Real
from typing import Optional


def time_finder(distance: Real, forward: Real, backward: Real) -> Optional[int]:
    if forward >= distance:
        return 1

    elif backward >= forward:
        return None

    else:
        return ceil((distance - forward) / (forward - backward)) + 1


def test_time_finder():
    params: tuple[int]
    result: Optional[int]
    for params, result in [
        [(30, 3, 2), 28],
        [(84, 17, 15), 35],
        [(79, 15, 9), 12],
        [(29, 17, 4), 2],
        [(13, 18, 8), 1],
        [(5, 5, 10), 1],
        [(7, 7, 7), 1],
        [(69, 3, 8), None],
        [(81, 14, 14), None],
    ]:
        assert time_finder(*params) == result
