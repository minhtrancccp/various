"""
References:
    https://en.wikipedia.org/wiki/ISO_basic_Latin_alphabet
    https://en.wikipedia.org/wiki/Basic_Latin_(Unicode_block)

Notes:
    - A valid Latin string must contain and only contain letters in the Basic Latin block and non-letter characters
"""
import re
from typing import Annotated

import regex
from beartype import beartype
from beartype.vale import Is

LETTER_PATTERN: re.Pattern[str] = re.compile(r"[a-zA-Z]")
STRING_PATTERN: regex.Pattern[str] = regex.compile(r"[\p{ASCII}||\P{Letter}]+")


@beartype
def string_validator(string: str) -> bool:
    return bool(LETTER_PATTERN.search(string) and STRING_PATTERN.fullmatch(string))


LatinString: type[str] = Annotated[str, Is[string_validator]]


@beartype
def letter_filter(string: LatinString, lowercase: bool = True) -> list[str]:
    if lowercase:
        string = string.lower()

    return LETTER_PATTERN.findall(string)
