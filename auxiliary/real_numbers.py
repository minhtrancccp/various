from numbers import Integral, Real
from typing import Annotated

from beartype.vale import Is


def is_not_negative(value: Real) -> bool:
    return value >= 0


def is_positive_real(value: Real) -> bool:
    return value > 0


NaturalNumber: type[Integral] = Annotated[Integral, Is[is_not_negative]]
PositiveInteger: type[Integral] = Annotated[Integral, Is[is_positive_real]]

NonNegativeReal: type[Real] = Annotated[Real, Is[is_not_negative]]
PositiveReal: type[Real] = Annotated[Real, Is[is_positive_real]]
