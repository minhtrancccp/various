from bisect import bisect_left
from collections import Iterator
from heapq import merge

from codetiming import Timer


def sieve(limit: int) -> Iterator[int]:
    exceptions: tuple[int, int] = (2, 5)
    prime_map: dict[int, bool] = dict.fromkeys(
        merge(
            exceptions[: bisect_left(exceptions, limit)],
            *(range(start, limit, 10) for start in (3, 7, 11, 19))
        ),
        True,
    )

    candidate: int
    for candidate in prime_map:
        if prime_map[candidate]:
            yield candidate

            if candidate not in exceptions:
                value: int
                for value in range(candidate ** 2, limit, candidate * 2):
                    if value in prime_map:
                        prime_map[value] = False


def main():
    CONST: int = 10 ** 5
    with Timer():
        print(*sieve(CONST), sep="\n")


if __name__ == "__main__":
    main()
