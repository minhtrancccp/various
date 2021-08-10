"""
A script containing useful constants and functions to be used for scripts with user inputs
"""

from time import sleep

QUIT_REMINDER: str = "Type 'quit' at any time to stop the program\n"


def quit_confirmation(question: str) -> str:
    """

    Parameters
    ----------
    question :

    Returns
    -------

    """
    answer: str = input(question)
    return stop_with_goodbye() if answer == "quit" else answer


def stop_with_goodbye() -> None:
    """
    Print the farewell statement before stopping the program
    """

    print("Thanks for using the program, see ya! From MinhCCCP")
    sleep(3)

    return None


if __name__ == "__main__":
    while True:
        quit_confirmation(
            "This is a trial, type anything, the program will stop if you type 'quit': "
        )
