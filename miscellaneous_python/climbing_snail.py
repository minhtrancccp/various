"""
References:
    https://codegolf.stackexchange.com/questions/130290/the-snail-in-the-well
"""
from math import ceil
from numbers import Real
from typing import Optional

from beartype import beartype


@beartype
def time_finder(distance: Real, forward: Real, backward: Real) -> Optional[int]:
    if distance <= forward:
        return 1

    if forward <= backward:
        return None

    return ceil((distance - forward) / (forward - backward)) + 1
