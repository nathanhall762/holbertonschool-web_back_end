#!/usr/bin/env python3
"""
The concat function concatenates two strings str1
and str2 and returns the result as a string.
"""


def concat(str1: str, str2: str) -> str:
    """
    Args:

    str1 (str): The first string to concatenate.
    str2 (str): The second string to concatenate.
    Returns:

    result (str): The concatenation of str1 and str2 as a single string.
    Example:
    >>> concat("hello", "world")
    'helloworld'
    """
    return str1 + str2
