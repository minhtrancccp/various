from math import factorial

from pytest import fixture, mark

from under_construction.fizz_buzz import FizzBuzz


@fixture
def fizzbuzz_machine():
    return FizzBuzz()


@mark.parametrize("value, output", [(factorial(15), "FizzBuzz")])
def test_fizz_buzz(fizzbuzz_machine, value, output):
    assert fizzbuzz_machine.result(value) == output
