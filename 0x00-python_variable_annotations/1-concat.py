#!/usr/bin/env python3
"""
1-concat.py

This module defines a type-annotated function `concat` that concatenates
two strings.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenate two strings.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        str: The concatenated string.
    """
    return str1 + str2
