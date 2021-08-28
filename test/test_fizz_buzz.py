from math import factorial

from codetiming import Timer

from various.fizz_buzz import FizzBuzz


@Timer(text="\n{} seconds")
def test_fb():
    new_fizz_buzz: FizzBuzz = FizzBuzz()
    assert new_fizz_buzz.result(factorial(15)) == "FizzBuzz"
