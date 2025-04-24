#!/usr/bin/env python3
"""Module for safely getting the first element of a sequence."""
from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of a sequence safely.

    Args:
        lst (Sequence[Any]): The sequence to get the first element from.

    Returns:
        Union[Any, None]: The first element of the sequence or None.
    """
    if lst:
        return lst[0]
    else:
        return None
