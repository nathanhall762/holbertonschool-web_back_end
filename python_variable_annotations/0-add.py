#!/usr/bin/env python3

"""
A module that provides a function to sum a list of mixed integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list of mixed integers and floats.

    Args:
        mxd_lst: A list of integers and/or floats.

    Returns:
        The sum of the input list as a float.
    """
    return sum(mxd_lst)
