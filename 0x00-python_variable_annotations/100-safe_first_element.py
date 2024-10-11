#!/usr/bin/env python3
"""
Augment the following code with the correct duck-typed annotations
"""
from typing import Any, Union, List


def safe_first_element(lst: Union[List[Any], None]) -> Union[Any, None]:
    """
    Return the first element of a list or None if the list is empty.

    Args:
        lst (Union[List[Any], None]): The list to retrieve the first element
        from.

    Returns:
        Union[Any, None]: The first element of the list or None if the list is
        empty.
    """
    if lst is None or len(lst) == 0:
        return None
    return lst[0]
