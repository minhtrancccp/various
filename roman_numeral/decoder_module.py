"""
References:
    https://rosettacode.org/wiki/Roman_numerals/Decode#Python
"""

from typing import Annotated

from beartype import beartype
from beartype.vale import Is

from roman_numeral.config import ACCEPTED_ROMAN_SYMBOLS
from type_hints.real_numbers import NaturalNumber


@beartype
def _valid_roman(roman: str) -> bool:
    """
    Return a boolean indicating whether the given Roman numeral is valid, i.e. contains only the accepted Roman symbols
    """

    from re import Pattern, compile

    roman_pattern: Pattern = compile(rf"[{ACCEPTED_ROMAN_SYMBOLS}]+")
    return bool(roman_pattern.fullmatch(roman))


class _IndicesPair:
    """
    Class for transforming a pair of indices into equivalent decimal
    """

    @beartype
    def __init__(self, indices_pair: tuple[NaturalNumber, int]):
        self.first_index: NaturalNumber
        self.second_index: int
        self.first_index, self.second_index = indices_pair

        self.delta_index: int = self.second_index - self.first_index

    @beartype
    def valid_pair(self) -> bool:
        """
        Return a boolean indicating whether the given pair of indices (i.e. a pair of Roman symbols) is valid

        A pair of symbols is valid if either:
        - The first symbol is to the right of the second symbol
        - The first symbol is at most second to the left of the second one & it represents a power of ten (i.e. "IXCM")

        Examples
        --------
        >>> _IndicesPair((0, 2)).valid_pair()
        True

        >>> _IndicesPair((0, 1)).valid_pair()
        True

        >>> _IndicesPair((1, 0)).valid_pair()
        True

        >>> _IndicesPair((1, 1)).valid_pair()
        False

        >>> _IndicesPair((0, 0)).valid_pair()
        True
        """

        return (
            self.delta_index <= -1 or self.delta_index <= 2 and not self.first_index % 2
        )

    @beartype
    def __int__(self) -> int:
        """
        Return the equivalent decimal value of a pair of indices

        The value is equal to the first symbol's absolute decimal value v calculated by this formula:

        `v = 10 ^ (i // 2) * 5 ^ (i % 2)`

        where i is the index of the symbol in ACCEPTED_ROMAN_SYMBOLS.
        The value will be negated afterwards if it is used in a subtractive notation.
        """

        from math import prod

        absolute_decimal: int = prod(map(pow, (10, 5), divmod(self.first_index, 2)))
        subtractive_notation_used: int = (-1) ** (self.delta_index >= 1)
        return absolute_decimal * subtractive_notation_used


@beartype
def _pair_transformation(
    indices_pair: Annotated[_IndicesPair, Is[_IndicesPair.valid_pair]]
) -> int:
    """
    Return the decimal equivalent of the given pair of indices

    Raises
    ------
    BeartypeCallHintPepParamException
        If the given pair of indices is not valid

    """

    return int(indices_pair)


@beartype
def decoder(roman_number: Annotated[str, Is[_valid_roman]]) -> NaturalNumber:
    """
    Return the decimal equivalent of the given Roman numeral

    Raises
    ------
    BeartypeCallHintPepParamException
        If input is not a valid Roman numeral

    Examples
    --------
    >>> decoder("I")
    1

    >>> decoder("MMMCMXCIX")
    3999

    >>> decoder("MMMDCCCLXXXVIII")
    3888
    """

    from itertools import pairwise

    from more_itertools import padded

    needed_pair_count: int = len(roman_number) + 1
    return sum(
        _pair_transformation(_IndicesPair(indices_pair))
        for indices_pair in pairwise(
            padded(
                map(ACCEPTED_ROMAN_SYMBOLS.find, roman_number),
                fillvalue=-1,
                n=needed_pair_count,
            )
        )
    )
