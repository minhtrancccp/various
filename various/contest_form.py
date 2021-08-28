from typing import Iterator


def get_num_input() -> Iterator[int]:
    return map(int, input().split())


def main():
    ...


if __name__ == "__main__":
    for _ in range(int(input())):
        main()
