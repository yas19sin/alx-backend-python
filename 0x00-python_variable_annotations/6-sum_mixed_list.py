#!/usr/bin/env python3
"""Module for summing a mixed list of integers and floats."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum a list of integers and floats and return their sum as a float.

    Args:
        mxd_lst (List[Union[int, float]]): The list of integers and floats.

    Returns:
        float: The sum of all elements in the list as a float.
    """
    return float(sum(mxd_lst))
