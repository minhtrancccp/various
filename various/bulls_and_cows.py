"""
References:
    https://en.wikipedia.org/wiki/Bulls_and_Cows
"""
from random import randint

from scripts_with_inputs import QUIT_REMINDER, quit_confirmation


# Complimentary function
def is_unique(inp: str) -> bool:
    """
    Check if a string has only unique chars

    :param inp: The checked string
    :return: The boolean value for the check
    """

    return len(inp) == len(set(inp))


# Main functions
def generator(number_of_digits: int) -> str:
    """
    Generate the number to be guessed

    :param number_of_digits: The number of digits to be guessed
    :return: The target str
    """

    if is_unique(
        result := str(randint(10 ** (number_of_digits - 1), 10 ** number_of_digits - 1))
    ):
        return result

    return generator(number_of_digits)


def welcome():
    """
    A function asking for how long the target should be
    """

    input_number: int = 0
    while input_number not in range(2, 11):
        try:
            input_number = int(
                quit_confirmation(
                    "How many digits would you like to number, between 2 and 10 inclusively: "
                )
            )
        except ValueError:
            continue

    game_controller(generator(input_number))


def game_controller(target: str, guess_list: list[str] = None):
    """
    The main function of the game

    :param target: The number to be found
    :param guess_list: The list of all guesses, no need to be filled in
    """

    if guess_list is None:
        guess_list = []

    if (guess := quit_confirmation("What's your number: ")) == target:
        print(f"Congrats, you found the number with {len(guess_list) + 1} number(es)")

        quit_confirmation(
            "Type 'quit' to exit the game, or press enter to play again: "
        )
        welcome()

    elif (
        (len(guess) != (target_len := len(target)))
        or (guess in guess_list)
        or (not guess.isdigit())
        or (not is_unique(guess))
    ):
        print(
            f"Make sure your number is a new one, and it must have exactly {target_len} unique digits"
        )

    else:
        print(
            f"{(bulls := sum(digits_pair[0] == digits_pair[1] for digits_pair in zip(guess, target)))} bull(s)",
            f"{len(set(guess) & set(target)) - bulls} cow(s)",
            sep="\n",
        )

    guess_list.append(guess)
    return game_controller(target, guess_list)


if __name__ == "__main__":
    print(QUIT_REMINDER)
    welcome()
