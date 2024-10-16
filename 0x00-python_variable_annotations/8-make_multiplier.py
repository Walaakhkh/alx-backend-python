#!/usr/bin/env python3
"""
type-annotated function make_multiplier that takes a float multiplier as
argument and returns a function that multiplies a float by multiplier.
 """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier to apply.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        the result of multiplying it by the multiplier.
    """
    def multiply(value: float) -> float:
        return value * multiplier

    return multiply
