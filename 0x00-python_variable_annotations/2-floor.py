#!/usr/bin/env python3
"""
2-floor.py

This module defines a type-annotated function `floor` that returns the
floor of a float.
"""


import math


def floor(n: float) -> int:
    """
    Return the floor of a float.

    Args:
        n (float): The float value to floor.

    Returns:
        int: The floor of the float value.
    """
    return math.floor(n)
