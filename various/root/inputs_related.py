"""
A script containing constants and functions handling with user inputs
"""

from time import sleep

QUIT_REMINDER: str = "Please type 'quit' at any time to stop the program"


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

    raise SystemExit()


def main():
    while True:
        quit_confirmation(
            "This is a trial, type anything, the program will stop if you type 'quit': "
        )


if __name__ == "__main__":
    main()
