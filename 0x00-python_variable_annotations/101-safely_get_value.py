#!/usr/bin/env python3
"""
add type annotations to the function
"""
from typing import Mapping, Any, TypeVar, Optional

T = TypeVar('T')  # Create a type variable


def safely_get_value(dct: Mapping[Any, T], key: Any, default: Optional[T] = None) -> Optional[T]:
    """
    Safely get the value from a dictionary.

    Args:
        dct (Mapping[Any, T]): The dictionary from which to retrieve the value.
        key (Any): The key for which to retrieve the value.
        default (Optional[T]): The default value to return if the key is not
        found.

    Returns:
        Optional[T]: The value associated with the key, or the default value
        if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
