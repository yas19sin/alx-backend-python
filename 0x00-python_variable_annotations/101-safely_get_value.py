#!/usr/bin/env python3
"""Module for safely getting a value from a dictionary."""
from typing import Mapping, TypeVar, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]: # Changed default annotation
    """Safely get a value from a dictionary.

    Args:
        dct (Mapping): The dictionary to get the value from.
        key (Any): The key to look up in the dictionary.
        default (Union[T, None], optional): The default value to return.
            Defaults to None.

    Returns:
        Union[Any, T]: The value from the dictionary or the default.
    """
    if key in dct:
        return dct[key]
    else:
        return default
