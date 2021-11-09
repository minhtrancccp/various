from typing import Annotated

from beartype import beartype
from beartype.vale import Is
from numerary.types import IntegralLike, RealLike


@beartype
def is_not_negative(value: RealLike) -> bool:
    return value >= 0


@beartype
def is_positive_real(value: RealLike) -> bool:
    return value > 0


NaturalNumber: type[IntegralLike] = Annotated[IntegralLike, Is[is_not_negative]]
PositiveInteger: type[IntegralLike] = Annotated[IntegralLike, Is[is_positive_real]]

NonNegativeReal: type[RealLike] = Annotated[RealLike, Is[is_not_negative]]
PositiveReal: type[RealLike] = Annotated[RealLike, Is[is_positive_real]]
