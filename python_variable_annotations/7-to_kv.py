#!/usr/bin/env python3
"""
This module provides a function for converting a string and numeric value into
a tuple with the string as the first element
and the square of the numeric value as the second element.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Convert a string and numeric value into a tuple.

    Args:
        k (str): The string to be used as the first element of the tuple.
        v (Union[int, float]): The numeric value to be squared and used as the
        second element of the tuple.

    Returns:
        A tuple with the string as the first element and the square of the
        numeric value as the second element.

    Example:
        >>> to_kv("eggs", 3)
        ('eggs', 9.0)
        >>> to_kv("school", 0.02)
        ('school', 0.0004)
    """
    return (k, v**2)
