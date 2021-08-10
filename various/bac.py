from random import sample
from string import digits


def _target_producer(length: int) -> str:
    result: list[str] = sample(digits, length)
    return "".join(result) if result[0] >= "1" else _target_producer(length)
