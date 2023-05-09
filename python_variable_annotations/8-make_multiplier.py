#!/usr/bin/env python3
"""
This module contains a function to create a multiplier function.

The make_multiplier function takes a float multiplier as an argument and
returns a new function that multiplies a float argument by the multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier as an argument and returns a function that
    multiplies a float argument by the multiplier.

    Args:
        multiplier (float): The value by which the function will multiply its
        argument.

    Returns:
        function: A new function that takes a float argument and multiplies it
        by the multiplier.
    """
    def multiply(x: float) -> float:
        """
        Multiplies a float argument by the multiplier.

        Args:
            x (float): The value to be multiplied.

        Returns:
            float: The result of multiplying x by the multiplier.
        """
        return x * multiplier
    return multiply
