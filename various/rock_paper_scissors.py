# From: https://en.wikipedia.org/wiki/Rock_paper_scissors
from scripts_with_inputs import QUIT_REMINDER, quit_confirmation

if __name__ == "__main__":
    print(QUIT_REMINDER)

    first_name: str
    second_name: str
    first_name, second_name = quit_confirmation(
        "Type the manes of two players, separated by a space: "
    ).split()

    first_score: int = 0
    second_score: int = 0
    while True:
        if (
            players_input := (
                quit_confirmation(f"What's your move, {first_name}: "),
                quit_confirmation(f"What's your move, {second_name}: "),
            )
        ) in (
            scenarios := [
                ("scissors", "paper"),
                ("rock", "scissors"),
                ("paper", "rock"),
            ]
        ):
            print(f"{first_name} wins!")
            first_score += 1

        elif tuple(reversed(players_input)) in scenarios:
            print(f"{second_name} wins!")
            second_score += 1

        print(f"{first_name} {first_score}-{second_score} {second_name}")
        quit_confirmation("Type 'quit' to exit the game, or press enter to continue: ")
