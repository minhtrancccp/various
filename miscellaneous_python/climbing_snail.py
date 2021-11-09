"""
References:
    https://codegolf.stackexchange.com/questions/130290/the-snail-in-the-well
"""
from math import ceil

from beartype import beartype

from type_hints.real_numbers import NaturalNumber, PositiveReal


class Snail:
    """
    A class for emulating a wall-climbing snail
    """

    def __init__(self, forward: PositiveReal, backward: PositiveReal) -> None:
        self.forward: PositiveReal = forward
        self.backward: PositiveReal = backward

    @beartype
    def normal_snail(self) -> bool:
        """
        Return a boolean indicating if the snail is normal, i.e. its forward speed is greater than its backward speed
        """

        return self.forward > self.backward

    @beartype
    def timer(self, distance: PositiveReal) -> NaturalNumber:
        """
        Return the time the snail takes to travel a distance

        If the travel distance isn't greater than the snail's forward speed and the snail is not normal, 0 is returned.
        To check if the snail is normal, use the Snail.normal_snail method.
        """

        if distance <= self.forward:
            return 1

        if not self.normal_snail():
            return 0

        return ceil((distance - self.forward) / (self.forward - self.backward)) + 1
