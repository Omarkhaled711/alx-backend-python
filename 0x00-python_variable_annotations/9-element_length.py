#!/usr/bin/env python3

"""
module for the ninth task
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    it calculates the length of a list of sequences
    """
    return [(i, len(i)) for i in lst]
