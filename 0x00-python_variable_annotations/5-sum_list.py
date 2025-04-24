#!/usr/bin/env python3
"""Module for summing a list of floats."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sum a list of floats and return their sum as a float.

    Args:
        input_list (List[float]): The list of floats.

    Returns:
        float: The sum of all floats in the list.
    """
    return sum(input_list)
