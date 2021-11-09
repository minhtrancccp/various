from typing import Annotated

from beartype import beartype
from beartype.vale import Is
from numerary.types import IntegralLikeSCU, RealLikeSCU


@beartype
def is_not_negative(value: RealLikeSCU) -> bool:
    """
    Return a boolean indicating whether the given real number is not negative.
    """

    return value >= 0


@beartype
def is_positive_real(value: RealLikeSCU) -> bool:
    """
    Return a boolean indicating whether the given real number is positive.
    """

    return value > 0


NaturalNumber: type[IntegralLikeSCU] = Annotated[IntegralLikeSCU, Is[is_not_negative]]
PositiveInteger: type[IntegralLikeSCU] = Annotated[
    IntegralLikeSCU, Is[is_positive_real]
]

NonNegativeReal: type[RealLikeSCU] = Annotated[RealLikeSCU, Is[is_not_negative]]
PositiveReal: type[RealLikeSCU] = Annotated[RealLikeSCU, Is[is_positive_real]]
