"""
References:
    https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
"""
from enum import Enum
from itertools import cycle
from string import ascii_lowercase

from beartype import beartype
from black import Mode


class Modes(Enum):
    ENCODE = 1
    DECODE = -1


class VigenereCipher:
    def __init__(self) -> None:
        self._mode: Modes = Modes.ENCODE

    @property
    @beartype
    def mode(self) -> str:
        return self._mode.name

    @mode.setter
    @beartype
    def mode(self, value: Mode) -> None:
        ...


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
    # TODO: Replace str.isalpha with a method for filtering out non-English chars and remove "printable" constraints
    #  for the test method (!)
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
