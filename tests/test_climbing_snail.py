from typing import Optional

from various.climbing_snail import time_finder


def test_time_finder():
    test_cases: tuple[tuple[tuple[int, int, int], Optional[int]], ...] = (
        ((30, 3, 2), 28),
        ((84, 17, 15), 35),
        ((79, 15, 9), 12),
        ((29, 17, 4), 2),
        ((13, 18, 8), 1),
        ((5, 5, 10), 1),
        ((7, 7, 7), 1),
        ((69, 3, 8), None),
        ((81, 14, 14), None),
    )

    params: tuple[int, int, int]
    result: Optional[int]
    for params, result in test_cases:
        assert time_finder(*params) == result
