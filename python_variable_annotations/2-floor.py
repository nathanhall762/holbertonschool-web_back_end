#!/usr/bin/env python3
"""
This module defines a function for computing the floor of a float number.
"""
import math


def floor(n: float) -> int:
    """
    Return the largest integer value less than or equal to the input float.

    Args:
    n (float): The input float to take the floor of.

    Returns:
    The largest integer value less than or equal to the input float.

    Examples:
    >>> floor(3.7)
    3
    >>> floor(4.0)
    4
    """
    return math.floor(n)
