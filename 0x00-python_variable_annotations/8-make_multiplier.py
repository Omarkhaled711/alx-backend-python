#!/usr/bin/env python3

"""
module for the ninth task
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    It takes a float multiplier as argument and returns a function
    that multiplies a float by multiplier.
    """
    def multiply(num: float) -> float:
        return float(multiplier * num)
    return multiply
