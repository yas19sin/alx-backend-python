#!/usr/bin/env python3
"""Module for element length calculation with duck-typed annotations."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Calculate the length of each element in an iterable.

    Args:
        lst (Iterable[Sequence]): The iterable containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples containing
                                    each sequence and its length.
    """
    return [(i, len(i)) for i in lst]
