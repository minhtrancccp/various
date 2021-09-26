"""
References:
    https://en.wikipedia.org/wiki/ISO_basic_Latin_alphabet
    https://en.wikipedia.org/wiki/Basic_Latin_(Unicode_block)

Notes:
    - A valid Latin string must contain at least one (1) Latin letter as defined in the Basic Latin Unicode block
"""
import re
from collections.abc import Iterator
from typing import Annotated

import regex
from beartype import beartype
from beartype.vale import Is

LETTER_PATTERN: re.Pattern[str] = re.compile(r"[a-zA-Z]")
STRING_PATTERN: regex.Pattern[str] = regex.compile(
    r"^[\p{BasicLatin}||\P{Alphabetic}]+$"
)


@beartype
def string_validator(string: str) -> bool:
    return bool(LETTER_PATTERN.search(string) and STRING_PATTERN.match(string))


ValidatedStringType: type[str] = Annotated[str, Is[string_validator]]


@beartype
def latin_filter(string: ValidatedStringType, lowercase: bool = True) -> Iterator[str]:
    found_letter: re.Match[str]
    for found_letter in LETTER_PATTERN.finditer(string):
        matched_string: str = found_letter.group()
        yield matched_string.lower() if lowercase and not matched_string.islower() else matched_string
