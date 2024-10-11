#!/usr/bin/env python3
"""
function’s parameters and return values with the appropriate types
 """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing elements and their respective lengths.

    Args:
        lst (Iterable[Sequence]): A list (or iterable) of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
        an element from the input list and its length.
    """
    return [(i, len(i)) for i in lst]
