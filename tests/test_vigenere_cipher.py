from string import printable

from hypothesis import given
from hypothesis.strategies import text

from miscellaneous_python.vigenere_cipher import Modes, vigenere_function


@given(text(printable), text())
def test_vigenere_hypothesis(message, key):
    assert (
        vigenere_function(
            vigenere_function(message, Modes.ENCODE, key), Modes.DECODE, key
        )
        == message
    )
