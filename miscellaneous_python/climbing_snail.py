"""
References:
    https://codegolf.stackexchange.com/questions/130290/the-snail-in-the-well
"""
from math import ceil
from typing import Optional

from beartype import beartype

from auxiliary.real_numbers import PositiveReal


class Snail:
    @beartype
    def __init__(self, forward: PositiveReal, backward: PositiveReal) -> None:
        self.forward: PositiveReal = forward
        self.backward: PositiveReal = backward

    def normal_snail(self) -> bool:
        return self.forward > self.backward

    @beartype
    def timer(self, distance: PositiveReal) -> Optional[PositiveReal]:
        if distance <= self.forward:
            return 1

        if not self.normal_snail():
            return None

        return ceil((distance - self.forward) / (self.forward - self.backward)) + 1
