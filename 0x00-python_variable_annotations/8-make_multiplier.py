#!/usr/bin/env python3
"""Module for creating a function that multiplies a float by multiplier."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that takes a float and
                                  returns a float.
    """
    def multiply(x: float) -> float:
        return x * multiplier

    return multiply
