"""
References:
    https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher

TODO:
    - Look for str.isalpha documentation (!)
"""
from enum import Enum
from itertools import cycle
from string import ascii_lowercase

from beartype import beartype


class Modes(Enum):
    ENCODE = 1
    DECODE = -1


def _char_converter(message: str, mode: Modes, key: str) -> str:
    result_char: str = ascii_lowercase[
        (ascii_lowercase.find(message.lower()) + mode.value * ascii_lowercase.find(key))
        % len(ascii_lowercase)
    ]

    if message.isupper():
        result_char = result_char.upper()

    return result_char


@beartype
def vigenere_function(message: str, mode: Modes, key: str = "") -> str:
    filtered_key: list[str] = [*filter(str.isalpha, key.lower())]
    if filtered_key.count("a") == len(filtered_key):
        return message

    cycled_key: cycle[str] = cycle(filtered_key)
    return "".join(
        _char_converter(message_char, mode, next(cycled_key))
        if message_char.isalpha()
        else message_char
        for message_char in message
    )
