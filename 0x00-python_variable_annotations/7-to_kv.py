#!/usr/bin/env python3
"""
 type-annotated function to_kv that takes a string k and an int OR float v as
 arguments and returns a tuple. The first element of the tuple is the string
 k. The second element is the square of the int/float v and should be
 annotated as a float.
 """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple where the first element is a string and the second element
    is the square of the given number (int or float).

    Args:
        k (str): The string key.
        v (Union[int, float]): The number to be squared.

    Returns:
        Tuple[str, float]: A tuple containing the string and the squared value.
    """
    return (k, float(v ** 2))
