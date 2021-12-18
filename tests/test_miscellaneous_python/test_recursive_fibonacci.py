from hypothesis import given
from hypothesis.strategies import integers
from numerary.types import IntegralLikeSCU
from sympy import fibonacci

from data_filter.real_numbers import PositiveInteger
from miscellaneous_python.recursive_fibonacci import recursive_function

# To avoid 'RecursionError: maximum recursion depth exceeded', a max absolute limit is set for testing
max_abs_limit: PositiveInteger = 330


@given(integers(min_value=-max_abs_limit, max_value=max_abs_limit))
def test_recursive_function(index: IntegralLikeSCU):
    assert recursive_function(index) == fibonacci(index)
