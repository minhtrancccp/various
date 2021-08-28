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
