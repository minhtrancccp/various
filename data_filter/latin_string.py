"""
References:
    https://en.wikipedia.org/wiki/ISO_basic_Latin_alphabet
    https://en.wikipedia.org/wiki/Basic_Latin_(Unicode_block)
"""

import re
from enum import Enum, auto
from typing import Annotated

import regex
from beartype import beartype
from beartype.vale import Is

LETTER_PATTERN: re.Pattern[str] = re.compile(r"[a-zA-Z]")
STRING_PATTERN: regex.Pattern[str] = regex.compile(r"[\p{ASCII}||\P{Letter}]+")


@beartype
def string_validator(string: str) -> bool:
    """
    Return a boolean indicating if the given string is a valid Latin string

    A valid Latin string must contain and only contain letters in the Basic Latin block and non-letter characters

    Examples
    --------
    >>> string_validator("abc")
    True

    >>> string_validator("abc123")
    True

    >>> string_validator("abc123!")
    True

    >>> string_validator("")
    False

    >>> string_validator("ăn uống")
    False
    """

    return bool(LETTER_PATTERN.search(string) and STRING_PATTERN.fullmatch(string))


LatinString: type[str] = Annotated[str, Is[string_validator]]


class CaseConversionModes(Enum):
    """
    Enum class providing case conversion modes for the `case_conversion` param in the `letter_filter` function

    3 options are available:
        - `CaseConversionModes.UNCHANGED`: no case conversion (default)
        - `CaseConversionModes.LOWERCASE`: convert to lowercase
        - `CaseConversionModes.UPPERCASE`: convert to uppercase
    """

    UNCHANGED = auto()
    LOWERCASE = auto()
    UPPERCASE = auto()


@beartype
def letter_filter(
    string: LatinString,
    case_conversion: CaseConversionModes = CaseConversionModes.UNCHANGED,
) -> list[str]:
    """
    Return a list of Latin letters in the given string

    To get the matching letters in a different case than default (i.e. unchanged), use the `case_conversion` parameter.

    Examples
    --------
    >>> letter_filter("abc")
    ['a', 'b', 'c']

    >>> letter_filter("abc", case_conversion=CaseConversionModes.LOWERCASE)
    ['a', 'b', 'c']

    >>> letter_filter("abc", case_conversion=CaseConversionModes.UPPERCASE)
    ['A', 'B', 'C']

    >>> letter_filter("39hgehh349IGEH98t583")
    ['h', 'g', 'e', 'h', 'h', 'I', 'G', 'E', 'H', 't']
    """

    match case_conversion:
        case CaseConversionModes.LOWERCASE:
            string = string.lower()

        case CaseConversionModes.UPPERCASE:
            string = string.upper()

    return LETTER_PATTERN.findall(string)
