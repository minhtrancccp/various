"""
References:
    https://codegolf.stackexchange.com/questions/130290/the-snail-in-the-well
"""

from beartype import beartype

from data_filter.real_numbers import NaturalNumber, PositiveReal


class Snail:
    """
    A class for emulating a wall-climbing snail
    """

    @beartype
    def __init__(self, forward: PositiveReal, backward: PositiveReal):
        self.forward: PositiveReal = forward
        self.backward: PositiveReal = backward

    @beartype
    def normal_snail(self) -> bool:
        """
        Return a boolean indicating if the snail is normal, i.e. its forward speed is greater than its backward speed

        Examples
        --------
        >>> Snail(1, 2).normal_snail()
        False

        >>> Snail(2, 1).normal_snail()
        True
        """

        return self.forward > self.backward

    @beartype
    def timer(self, distance: PositiveReal) -> NaturalNumber:
        """
        Return the time the snail takes to travel a distance

        The result is rounded up to the nearest days.
        If the travel distance is greater than the snail's forward speed but the snail isn't normal, 0 is returned.
        To check if the snail is normal, use the Snail.normal_snail method.

        Raises
        ------
        BeartypeCallHintPepParamException
            If the given distance is not a positive real number

        Examples
        --------
        >>> Snail(1, 2).timer(1)
        1

        >>> Snail(1, 2).timer(2)
        0

        >>> Snail(2, 1).timer(3)
        2
        """

        from math import ceil

        if distance <= self.forward:
            return 1

        elif not self.normal_snail():
            return 0

        else:
            return ceil((distance - self.forward) / (self.forward - self.backward)) + 1
