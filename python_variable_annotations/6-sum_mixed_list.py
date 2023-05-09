#!/usr/bin/env python3
"""
This module contains a function that calculates the sum of a mixed list of
integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of a mixed list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The list of mixed integers and
        floats to sum.

    Returns:
        float: The sum of the mixed list.

    Example:
        >>> sum_mixed_list([1, 2.0, 3, 4.0])
        10.0
    """
    return sum(mxd_lst)
