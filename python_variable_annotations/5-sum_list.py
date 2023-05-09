#!/usr/bin/env python3
"""
This module contains a function that calculates the sum of a list of floats.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floats.

    Args:
        input_list (List[float]): The list of floats to sum.

    Returns:
        float: The sum of the input list.

    Example:
        >>> sum_list([1.0, 2.0, 3.0])
        6.0
    """
    return sum(input_list)
