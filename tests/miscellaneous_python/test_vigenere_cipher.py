"""
TODO: Write tests for switch_mode()
"""

from hypothesis import given
from hypothesis.strategies import SearchStrategy

from data_filter.latin_string import LatinString
from miscellaneous_python.vigenere_cipher import VigenereCipher
from tests.miscellaneous_python.config import string_strategy

testing_string: SearchStrategy[str] = string_strategy()


@given(testing_string, testing_string)
def test_cipher(message: LatinString, key: LatinString):
    cipher: VigenereCipher = VigenereCipher()
    encrypted_message: LatinString = cipher.cipher_machine(message, key)
    cipher.switch_mode()

    assert cipher.cipher_machine(encrypted_message, key) == message
