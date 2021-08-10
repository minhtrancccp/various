"""
References:
    https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
"""
from functools import cache
from itertools import cycle
from string import ascii_lowercase
from typing import Callable, Literal, Type

from codetiming import Timer

_accepted_modes: Type[int] = Literal[1, -1]

_a_letter: str = "a"
_a_ord: int = ord(_a_letter)
_alphabet_length: int = len(ascii_lowercase)

_index_to_letter: Callable[[int], str] = cache(ascii_lowercase.__getitem__)
_is_letter: Callable[[str], bool] = cache(str.isalpha)
_lowercase: Callable[[str], str] = cache(str.lower)
_uppercase: Callable[[str], str] = cache(str.upper)


@cache
def _letter_to_index(letter: str) -> int:
    return ord(letter) - _a_ord


def _letter_converter(message: str, sign: _accepted_modes, key: str) -> str:
    result_char: str = _index_to_letter(
        (_letter_to_index(_lowercase(message)) + sign * _letter_to_index(key))
        % _alphabet_length
    )

    if message.isupper():
        result_char = _uppercase(result_char)

    return result_char


def vigenere_function(
        message: str, decode_mode: _accepted_modes = 1, key: str = ""
) -> str:
    """

    Parameters
    ----------
    message :
    decode_mode :
    key :

    Returns
    -------

    """
    filtered_key: list[str] = [*filter(_is_letter, _lowercase(key))]
    if not filtered_key or filtered_key == [_a_letter]:
        return message

    cycled_key: cycle[str] = cycle(filtered_key)
    return "".join(
        _letter_converter(message_char, decode_mode, next(cycled_key))
        if _is_letter(message_char)
        else message_char
        for message_char in message
    )


@Timer(text="\n{} seconds")
def _test():
    assert vigenere_function("ATTACKATDAWN", 1, "LEMON") == "LXFOPVEFRNHR"
