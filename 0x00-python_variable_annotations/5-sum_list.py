#!/usr/bin/env python3
"""
 function sum_list which takes a list input_list of floats as argument and
 returns their sum as a float.
 """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Takes a list of floats and returns their sum as a float

    Args:
        input_list (List[float]): A list of float numbers.

    Returns:
        float: The sum of the list elements.
    """
    return sum(input_list)
