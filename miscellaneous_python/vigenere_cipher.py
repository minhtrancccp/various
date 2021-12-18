"""
References:
    https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
"""

from enum import IntEnum
from itertools import cycle
from string import ascii_lowercase
from typing import Optional

from beartype import beartype

from data_filter import latin_string


class Modes(IntEnum):
    ENCODE = 1
    DECODE = -1


class VigenereCipher:
    _keys: cycle

    def __init__(self) -> None:
        self._mode: Modes = Modes.ENCODE

    @property
    @beartype
    def mode(self) -> Modes:
        return self._mode

    @mode.setter
    @beartype
    def mode(self, value: Modes) -> None:
        self._mode = value

    @beartype
    def switch_mode(self, value: Optional[Modes] = None) -> None:
        if value:
            self._mode = value

        else:
            match self.mode:
                case Modes.ENCODE:
                    self.mode = Modes.DECODE

                case Modes.DECODE:
                    self.mode = Modes.ENCODE

    @beartype
    def _char_converter(self, input_char: str) -> str:
        result_char: latin_string.LatinString = input_char
        if latin_string.LETTER_PATTERN.search(result_char):
            message_letter_index: int = ascii_lowercase.find(result_char.lower())
            key_letter_index: int = ascii_lowercase.find(next(self._keys))
            english_letter_count: int = 26

            result_char = ascii_lowercase[
                (message_letter_index + self.mode.value * key_letter_index)
                % english_letter_count
            ]

            if input_char.isupper():
                result_char = result_char.upper()

        return result_char

    @beartype
    def cipher_machine(
        self, message: latin_string.LatinString, key: latin_string.LatinString
    ) -> latin_string.LatinString:
        key_letters: list[str] = latin_string.letter_filter(
            key, latin_string.CaseConversionModes.LOWERCASE
        )
        if key_letters.count("a") == len(key_letters):
            return message

        self._keys = cycle(key_letters)
        return "".join(map(self._char_converter, message))
