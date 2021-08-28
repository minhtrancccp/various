from codetiming import Timer

from various.vigenere_cipher import vigenere_function,Modes


@Timer(text="\n{} seconds")
def test_vigenere():
    assert vigenere_function("ATTACKATDAWN", Modes.ENCODE, "LEMON") == "LXFOPVEFRNHR"
