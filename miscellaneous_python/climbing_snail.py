"""
References:
    https://codegolf.stackexchange.com/questions/130290/the-snail-in-the-well
"""
from math import ceil

from beartype import beartype

from type_hints.real_numbers import NonNegativeReal, PositiveReal


class Snail:
    def __init__(self, forward: PositiveReal, backward: PositiveReal) -> None:
        self.forward: PositiveReal = forward
        self.backward: PositiveReal = backward

    @beartype
    def normal_snail(self) -> bool:
        return self.forward > self.backward

    @beartype
    def timer(self, distance: PositiveReal) -> NonNegativeReal:
        if distance <= self.forward:
            return 1

        if not self.normal_snail():
            return 0

        return ceil((distance - self.forward) / (self.forward - self.backward)) + 1
