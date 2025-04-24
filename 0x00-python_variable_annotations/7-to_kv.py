#!/usr/bin/env python3
"""Module for creating a tuple from a string and an int/float."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Create a tuple from a string and squared int/float.

    Args:
        k (str): The string to be used as first element.
        v (Union[int, float]): The int/float to be squared.

    Returns:
        Tuple[str, float]: A tuple containing the string k and the square of v.
    """
    return (k, float(v ** 2))
