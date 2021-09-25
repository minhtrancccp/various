from pytest import mark

from miscellaneous_python.climbing_snail import time_finder


@mark.parametrize(
    "inputs, output",
    [
        ((30, 3, 2), 28),
        ((84, 17, 15), 35),
        ((79, 15, 9), 12),
        ((29, 17, 4), 2),
        ((13, 18, 8), 1),
        ((5, 5, 10), 1),
        ((7, 7, 7), 1),
        ((69, 3, 8), None),
        ((81, 14, 14), None),
    ],
)
def test_time_finder(inputs, output):
    assert time_finder(*inputs) == output
