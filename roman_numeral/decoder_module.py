"""
References:
    https://rosettacode.org/wiki/Roman_numerals/Decode#Python
"""

from typing import Annotated

from beartype import beartype
from beartype.vale import Is
from numerary.types import IntegralLikeSCU

from data_filter.real_numbers import NaturalNumber, PositiveInteger
from roman_numeral.config import ACCEPTED_ROMAN_SYMBOLS

IndicesPair: type[tuple] = tuple[NaturalNumber, IntegralLikeSCU]


@beartype
def _valid_roman(roman: str) -> bool:
    """
    Return a boolean indicating whether the given Roman numeral is valid, i.e. contains only the accepted Roman symbols
    """

    from re import Pattern, compile

    roman_pattern: Pattern = compile(rf"[{ACCEPTED_ROMAN_SYMBOLS}]+")
    return bool(roman_pattern.fullmatch(roman))


@beartype
def _pair_transformation(indices_pair: IndicesPair) -> IntegralLikeSCU:
    """
    Return the equivalent decimal value of a pair of indices

    The value is equal to the first symbol's absolute decimal value v calculated by this formula:

    `v = 10 ^ (i // 2) * 5 ^ (i % 2)`

    where i is the index of the symbol in ACCEPTED_ROMAN_SYMBOLS.
    The value will be negated afterwards if it is used in a subtractive notation.
    """

    from math import prod

    first_index: NaturalNumber
    second_index: IntegralLikeSCU
    first_index, second_index = indices_pair
    delta_index: IntegralLikeSCU = second_index - first_index

    absolute_decimal: PositiveInteger = prod(map(pow, (10, 5), divmod(first_index, 2)))
    subtractive_notation_used: IntegralLikeSCU = (-1) ** (delta_index >= 1)

    return absolute_decimal * subtractive_notation_used


@beartype
def decoder(roman_number: Annotated[str, Is[_valid_roman]]) -> PositiveInteger:
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

    needed_pair_count: PositiveInteger = len(roman_number) + 1
    indices_pairs: pairwise[IndicesPair] = pairwise(
        padded(
            map(ACCEPTED_ROMAN_SYMBOLS.find, roman_number),
            fillvalue=-1,
            n=needed_pair_count,
        )
    )

    return sum(map(_pair_transformation, indices_pairs))
