"""
References:
    https://rosettacode.org/wiki/Roman_numerals/Encode#Python
"""

from typing import Annotated

from beartype import beartype
from beartype.vale import Is

from type_hints.real_numbers import PositiveInteger


@beartype
def _valid_decimal(decimal: int) -> bool:
    """
    Return a boolean indicating whether the given decimal number is smaller or equal to the maximum allowed value for
    a Roman numeral, i.e. 3,999
    """

    largest_valid_number: int = 3_999
    return decimal <= largest_valid_number


@beartype
def _roman_symbols(index: int, digit: str) -> str:
    """
    Return the Roman numeral symbols for the given decimal digit
    """

    from roman_numeral.config import ACCEPTED_ROMAN_SYMBOLS

    quotient: int
    remainder: int
    quotient, remainder = divmod(int(digit), 5)
    twice_index: int = 2 * index

    subtractive_notation_available: bool = remainder == 4
    symbol_tuple: tuple[int, ...] = (
        (twice_index, twice_index + quotient + 1)
        if subtractive_notation_available
        else quotient * (twice_index + 1,) + remainder * (twice_index,)
    )

    return "".join(map(ACCEPTED_ROMAN_SYMBOLS.__getitem__, symbol_tuple))


@beartype
def encoder(decimal: Annotated[PositiveInteger, Is[_valid_decimal]]) -> str:
    """
    Return the Roman numeral representation of the given decimal number

    Raises
    ------
    BeartypeCallHintPepParamException
        If the given decimal number is not between 1 and 3,999

    Examples
    --------
    >>> encoder(1)
    'I'

    >>> encoder(3_999)
    'MMMCMXCIX'

    >>> encoder(3_888)
    'MMMDCCCLXXXVIII'
    """

    roman_result: str = ""

    index_digit_pair: tuple[int, str]
    for index_digit_pair in enumerate(reversed(str(decimal))):
        roman_result = _roman_symbols(*index_digit_pair) + roman_result

    return roman_result
