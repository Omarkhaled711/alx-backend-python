#!/usr/bin/env python3

"""
module for the eighth task
"""
from typing import Tuple, Union


def to_kv(k: str,  v: Union[int, float]) -> Tuple[str, float]:
    """
    It takes a string k and an int OR float v as arguments and returns a tuple.
    The first element of the tuple is the string k.
    The second element is the square of the int/float v
    """
    return (k, float(v**2))
