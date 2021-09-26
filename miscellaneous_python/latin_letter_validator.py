from collections.abc import Iterator
from re import Match, Pattern, compile
from typing import Annotated

from beartype import beartype
from beartype.vale import Is

_LATIN_LETTER_PATTERN: Pattern[str] = compile(r"[a-zA-Z]")


@beartype
def has_latin_letters(string: str) -> bool:
    return bool(_LATIN_LETTER_PATTERN.search(string))


StringType: type[str] = Annotated[str, Is[has_latin_letters]]


@beartype
def latin_letter_filter(string: str, lowercase: bool = True) -> Iterator[str]:
    match: Match[str]
    for match in _LATIN_LETTER_PATTERN.finditer(string):
        matched_string: str = match.group()
        yield matched_string.lower() if lowercase and not matched_string.islower() else matched_string
