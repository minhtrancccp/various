"""
References:
    https://youtu.be/pvimAM_SLic
"""
from math import hypot, pi
from multiprocessing import Pool
from random import random

from codetiming import Timer
from prettytable import PrettyTable


def pi_estimation(points_count: int) -> float:
    """
    Estimate Pi based on the formula given in the reference

    Parameters
    ----------
    points_count : int
        Total number of points to be generated inside the square with vertices (0, 0), (0, 1), (1, 0), (1, 1)

    Returns
    -------
    float
        Estimated value of Pi

    """
    points_in_circle_count: int = sum(
        hypot(random(), random()) <= 1 for _ in range(points_count)
    )
    return 4 * points_in_circle_count / points_count


def _factory(magnitude: int) -> tuple[int, int, float, float]:
    number_of_points: int = 10 ** magnitude
    result: float = pi_estimation(number_of_points)
    return magnitude, number_of_points, result, abs(result / pi - 1) * 100


def main():
    print(f"{pi = }")
    new_table: PrettyTable = PrettyTable(
        [
            "Order of magnitude (10^)",
            "Actual count of points",
            "Approximated value",
            "Relative difference (in %)",
        ]
    )
    with Timer(text="Tabulation time: {:0.4f} seconds"):
        new_table.add_rows(Pool().map(_factory, range(1, 9)))
    print(new_table)


if __name__ == "__main__":
    main()
