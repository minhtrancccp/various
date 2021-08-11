"""
References:
    https://en.wikipedia.org/wiki/Bulls_and_Cows
"""
# region
from dataclasses import dataclass
from functools import cache
from random import sample
from string import digits
from typing import Union
from webbrowser import open as open_site

from beartype import beartype
from codetiming import Timer
from humanfriendly import format_timespan

from various.root import inputs_related


# endregion


def quantity_formatter(quantity: int, name: str) -> str:
    return f"{quantity} {name}{'s' * (quantity >= 2)}"


def time_formatter(seconds: float) -> str:
    return f"You used {format_timespan(seconds)} to find the target number."


@dataclass
class Result:
    all_correct: bool = False
    bulls: int = 0
    cows: int = 0


# region
class TargetNumber:
    value: list[str]

    @beartype
    def __init__(self, length: int):
        self.length: int = length
        self.new_value()

    def new_value(self):
        self.value = sample(digits, self.length)

        if self.value[0] == "0":
            return self.new_value()

    @cache
    @beartype
    def verifier(self, testee: Union[str, list[str]]) -> Result:
        if all(map(str.__eq__, self.value, testee)):
            return Result(True, self.length)

        result: Result = Result()

        testee_as_set: set[str] = {*testee}
        if self.side_test(testee_as_set):
            common: str
            for common in testee_as_set.intersection(self.value):
                if testee.index(common) == self.value.index(common):
                    result.bulls += 1

                else:
                    result.cows += 1

        return result

    def side_test(self, testee: set[str]) -> bool:
        return all(map(str.isdigit, testee)) and len(testee) == self.length


# endregion


class CLIVersion:
    target: TargetNumber
    count: int

    def __init__(self, debug_mode: bool = False):
        print(
            f"""\
Welcome to the "Bulls and Cows" version 2.0, made by MinhCCCP!
{inputs_related.QUIT_REMINDER}"""
        )

        if (
                inputs_related.quit_confirmation(
                    "Type y/Y to have a look at the rules of the game:"
                ).lower()
                == "y"
        ):
            open_site("https://en.wikipedia.org/wiki/Bulls_and_Cows")

        self.debug_mode: bool = debug_mode

        self.target_initialization()

    def target_initialization(self):
        value: str = inputs_related.quit_confirmation(
            "\nPlease type the length of the target number (an int between 1 and 10 inclusively): "
        )

        if value.isdigit():
            length: int = int(value)
            if 1 <= length <= 10:
                self.target = TargetNumber(length)
                self.count = 1

                if self.debug_mode:
                    print(f"{self.target.value = }")

                print("Let the game begin!\n")
                return self.main()

        return self.target_initialization()

    def handler(self):
        result: Result = self.target.verifier(
            inputs_related.quit_confirmation("Please type your guess: ")
        )

        if result.all_correct:
            print(
                f"\nCongrats, you found the target number with {quantity_formatter(self.count, 'count')}"
            )

        else:
            print(
                quantity_formatter(result.bulls, "bull"),
                quantity_formatter(result.cows, "cow"),
                sep=", ",
                end="\n" * 2,
            )

            self.count += 1
            return self.handler()

    def main(self):
        with Timer(text=time_formatter):
            self.handler()

        inputs_related.quit_confirmation(
            "\nPlease press enter to play again, or type 'quit' to exit the game: "
        )

        print("The game will continue...")
        return self.target_initialization()


def main():
    CLIVersion()


if __name__ == "__main__":
    main()
