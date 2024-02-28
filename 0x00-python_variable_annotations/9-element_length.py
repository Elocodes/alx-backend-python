#!/usr/bin/env python3
""" iterable objects """
from typing import Iterable, Tuple, List, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples """
    return [(i, len(i)) for i in lst]
