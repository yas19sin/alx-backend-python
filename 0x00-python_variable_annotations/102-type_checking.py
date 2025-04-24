#!/usr/bin/env python3
"""Module for zooming arrays."""
from typing import Tuple, List, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Zoom in on an array by repeating its elements.

    Args:
        lst (Tuple): The tuple to zoom in on.
        factor (int, optional): The zoom factor. Defaults to 2.

    Returns:
        List: The zoomed list.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
