# From: https://en.wikipedia.org/wiki/Morse_code
from string import ascii_lowercase


def morse_func(func_input: str, sep_char: str = " ") -> str:
    """
    :param func_input: The word to be encoded, only English letter allowed
    :param sep_char: Character to be inserted between the sequences, default is a space
    :return: The Morse representation of the word
    """

    if not (func_input := func_input.lower()).isalpha():
        raise ValueError("Input has non-letter characters")

    ref_sequence: str = (
        ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- "
        "-..- -.-- --.. "
    )
    return sep_char.join(
        ref_sequence.split()[ascii_lowercase.index(letter)] for letter in func_input
    )


if __name__ == "__main__":
    print(morse_func("where"))
    print(morse_func("bits", ""))
    print(morse_func("three", ""))
